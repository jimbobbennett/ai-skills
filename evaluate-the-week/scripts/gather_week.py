#!/usr/bin/env python3
"""Gather the past week's candidate stories for an "Evaluate the Week" episode.

Pulls only free, no-auth sources (RSS/Atom + a few public JSON APIs) and writes a
single candidates digest the agent then turns into a script outline. stdlib only —
no pip install required.

Usage:
    python3 gather_week.py [--days 7] [--out PATH] [--json]

Output: a markdown digest grouped by area (Arize / AI news / Fun & viral), each item
with title, source, date, link, and an engagement signal where available. With --json
it also writes a machine-readable sidecar next to the markdown.

Sources are defined in the FEEDS / config blocks below — edit those to tune the show.
Keyed sources (YouTube Data API, Product Hunt, paid X/TikTok scrapers) are intentionally
NOT here in v1; the no-auth feeds below cover the bulk of the signal.

Two auth-dependent exceptions:
  * Reddit — as of 2025 Reddit blocks unauthenticated clients (the public .json endpoint
    returns 403 regardless of User-Agent or IP), so it's pulled via OAuth when
    REDDIT_CLIENT_ID and REDDIT_CLIENT_SECRET are set, and skipped otherwise. Register a
    free "script" app at https://www.reddit.com/prefs/apps.
  * GitHub PRs (merged PRs on the Arize docs + OpenInference repos) — pulled via the `gh`
    CLI so private repos work under the signed-in user's auth. Needs `gh auth login`; if
    `gh` is missing or unauthenticated those repos are skipped with a clear note.
"""

from __future__ import annotations

import argparse
import base64
import datetime as dt
import json
import os
import re
import subprocess
import sys
import urllib.request
import urllib.error
import urllib.parse
from concurrent.futures import ThreadPoolExecutor
from email.utils import parsedate_to_datetime
from xml.etree import ElementTree as ET

UA = "evaluate-the-week/1.0 (weekly AI roundup; +https://arize.com)"
TIMEOUT = 20

# ---------------------------------------------------------------------------
# Source config — edit these to tune what the show watches.
# ---------------------------------------------------------------------------

# RSS/Atom feeds: (area, source_label, url)
FEEDS = [
    # --- Arize ---
    ("arize", "Arize Blog", "https://arize.com/blog/feed/"),
    ("arize", "Phoenix releases", "https://github.com/Arize-ai/phoenix/releases.atom"),
    ("arize", "OpenInference releases", "https://github.com/Arize-ai/openinference/releases.atom"),
    ("arize", "Arize YouTube", "https://www.youtube.com/feeds/videos.xml?channel_id=UCrVHzD-psX5IMCGoEWHXmGw"),

    # --- AI news: newsletters ---
    ("ai-news", "AI News (smol.ai)", "https://buttondown.com/ainews/rss"),
    ("ai-news", "Latent Space", "https://www.latent.space/feed"),
    ("ai-news", "Import AI", "https://importai.substack.com/feed"),
    ("ai-news", "TLDR AI", "https://tldr.tech/api/rss/ai"),
    ("ai-news", "Lenny's Newsletter", "https://www.lennysnewsletter.com/feed"),

    # --- AI news: platforms / tooling vendors (catches integration-worthy launches) ---
    ("ai-news", "Vercel", "https://vercel.com/atom"),

    # --- AI news: labs (clean RSS only; Anthropic/Meta/Mistral are scrape-only, omitted) ---
    ("ai-news", "OpenAI", "https://openai.com/news/rss.xml"),
    ("ai-news", "Google DeepMind", "https://deepmind.google/blog/rss.xml"),
    ("ai-news", "Google Developers", "https://developers.googleblog.com/feed/"),
    ("ai-news", "Hugging Face blog", "https://huggingface.co/blog/feed.xml"),

    # --- AI news: framework releases (GitHub releases.atom) ---
    ("frameworks", "LangChain", "https://github.com/langchain-ai/langchain/releases.atom"),
    ("frameworks", "LangGraph", "https://github.com/langchain-ai/langgraph/releases.atom"),
    ("frameworks", "LlamaIndex", "https://github.com/run-llama/llama_index/releases.atom"),
    ("frameworks", "CrewAI", "https://github.com/crewAIInc/crewAI/releases.atom"),
    ("frameworks", "OpenAI Agents SDK", "https://github.com/openai/openai-agents-python/releases.atom"),
    ("frameworks", "vLLM", "https://github.com/vllm-project/vllm/releases.atom"),
    ("frameworks", "Ollama", "https://github.com/ollama/ollama/releases.atom"),
    ("frameworks", "DSPy", "https://github.com/stanfordnlp/dspy/releases.atom"),
    ("frameworks", "Pydantic AI", "https://github.com/pydantic/pydantic-ai/releases.atom"),
    ("frameworks", "MCP spec", "https://github.com/modelcontextprotocol/modelcontextprotocol/releases.atom"),

    # --- AI news: research ---
    ("ai-news", "arXiv cs.CL", "https://rss.arxiv.org/rss/cs.CL"),

    # --- Fun & viral: GitHub trending ---
    ("fun", "GitHub Trending (weekly)", "https://mshibanami.github.io/GitHubTrendingRSS/weekly/all.xml"),
]

# Hacker News Algolia queries: (area, label, query, tags)
HN_QUERIES = [
    ("ai-news", "HN front page", "AI LLM agent", "front_page"),
    ("fun", "HN Show HN", "AI LLM agent", "show_hn"),
]
HN_MIN_POINTS = 100

# Reddit subreddits to pull top-of-week: (area, subreddit)
REDDIT_SUBS = [
    ("ai-news", "LocalLLaMA"),
    ("ai-news", "MachineLearning"),
    ("fun", "aivideo"),
    ("fun", "StableDiffusion"),
    ("fun", "singularity"),
    ("fun", "ProgrammerHumor"),
    ("fun", "aimemes"),
]
REDDIT_MIN_SCORE = 200

# Hugging Face trending: spaces (fun demos) and daily papers (research signal)
HF_SPACES_URL = "https://huggingface.co/api/spaces?sort=likes7d&limit=15"
HF_PAPERS_URL = "https://huggingface.co/api/daily_papers?limit=40"

# GitHub repos to pull recently-MERGED PRs from (via the `gh` CLI, so private repos work
# under the user's auth). Merged PRs are how new integrations show up before a release —
# e.g. "docs(eve): Vercel/Eve tracing" or "feat(js): Vercel AI SDK spans". (area, label, repo)
GITHUB_PR_REPOS = [
    ("arize", "Arize docs PR", "Arize-ai/docs"),            # private — needs `gh auth login`
    ("arize", "OpenInference PR", "Arize-ai/openinference"),
]

# Competitors — items matching these are filtered out of the digest (listed in a
# separate "excluded" section, not silently dropped) so the show never promotes a
# rival. Arize competes in LLM OBSERVABILITY / EVALUATION / TRACING, so this targets
# that category specifically. NOTE the surgical scope: companies like LangChain and
# Pydantic ship BOTH an agent framework (which Arize/Phoenix integrates with — keep)
# AND a competing observability product (LangSmith, Pydantic Logfire — exclude). The
# keywords below match the competing *products*, not the frameworks, so framework
# release news still comes through. To exclude a company wholesale, add its framework
# name/domain too (e.g. add "langchain" / "pydantic-ai"). Match = competitor domain in
# the link's host OR a keyword substring (case-insensitive) in the title.
COMPETITORS = [
    {"name": "LangSmith", "domains": ["smith.langchain.com"], "keywords": ["langsmith"]},
    {"name": "Pydantic Logfire", "domains": ["logfire.pydantic.dev"], "keywords": ["logfire"]},
    {"name": "Langfuse", "domains": ["langfuse.com"], "keywords": ["langfuse"]},
    {"name": "Braintrust", "domains": ["braintrust.dev", "braintrustdata.com"], "keywords": ["braintrust"]},
    {"name": "Weights & Biases (Weave)", "domains": ["wandb.ai", "wandb.com"], "keywords": ["wandb", "weights & biases", "w&b weave"]},
    {"name": "Comet (Opik)", "domains": ["comet.com", "comet.ml"], "keywords": ["opik"]},
    {"name": "Helicone", "domains": ["helicone.ai"], "keywords": ["helicone"]},
    {"name": "Galileo", "domains": ["galileo.ai", "rungalileo.io"], "keywords": ["rungalileo"]},
    {"name": "Fiddler AI", "domains": ["fiddler.ai"], "keywords": ["fiddler ai"]},
    {"name": "WhyLabs", "domains": ["whylabs.ai"], "keywords": ["whylabs", "langkit"]},
    {"name": "HoneyHive", "domains": ["honeyhive.ai"], "keywords": ["honeyhive"]},
    {"name": "Humanloop", "domains": ["humanloop.com"], "keywords": ["humanloop"]},
    {"name": "LangWatch", "domains": ["langwatch.ai"], "keywords": ["langwatch"]},
    {"name": "Traceloop (OpenLLMetry)", "domains": ["traceloop.com"], "keywords": ["traceloop", "openllmetry"]},
    {"name": "Confident AI (DeepEval)", "domains": ["confident-ai.com"], "keywords": ["confident ai", "deepeval"]},
    {"name": "PromptLayer", "domains": ["promptlayer.com"], "keywords": ["promptlayer"]},
    {"name": "Literal AI", "domains": ["literalai.com"], "keywords": ["literal ai"]},
    {"name": "Maxim AI", "domains": ["getmaxim.ai"], "keywords": ["getmaxim"]},
    {"name": "Patronus AI", "domains": ["patronus.ai"], "keywords": ["patronus ai"]},
    {"name": "Athina AI", "domains": ["athina.ai"], "keywords": ["athina ai"]},
    {"name": "Langtrace", "domains": ["langtrace.ai"], "keywords": ["langtrace"]},
    {"name": "Portkey", "domains": ["portkey.ai"], "keywords": ["portkey"]},
    {"name": "Lunary", "domains": ["lunary.ai"], "keywords": ["lunary"]},
    {"name": "TruEra (TruLens)", "domains": ["truera.com"], "keywords": ["truera", "trulens"]},
    {"name": "Datadog LLM Observability", "domains": [], "keywords": ["datadog llm"]},
]


def competitor_match(item: dict) -> str | None:
    """Return the competitor name if this item references one, else None."""
    title = (item.get("title") or "").lower()
    netloc = urllib.parse.urlparse((item.get("link") or "").lower()).netloc
    for c in COMPETITORS:
        if any(d in netloc for d in c["domains"]):
            return c["name"]
        if any(kw in title for kw in c["keywords"]):
            return c["name"]
    return None


# ---------------------------------------------------------------------------
# Fetch helpers
# ---------------------------------------------------------------------------

def _get(url: str) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "*/*"})
    with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
        return resp.read()


def _get_json(url: str):
    return json.loads(_get(url).decode("utf-8", "replace"))


def _parse_date(text: str | None):
    if not text:
        return None
    text = text.strip()
    # RFC 822 (RSS)
    try:
        d = parsedate_to_datetime(text)
        if d.tzinfo is None:
            d = d.replace(tzinfo=dt.timezone.utc)
        return d
    except (TypeError, ValueError, IndexError):
        pass
    # ISO 8601 (Atom)
    try:
        d = dt.datetime.fromisoformat(text.replace("Z", "+00:00"))
        if d.tzinfo is None:
            d = d.replace(tzinfo=dt.timezone.utc)
        return d
    except ValueError:
        return None


def _strip_ns(tag: str) -> str:
    return tag.rsplit("}", 1)[-1]


def parse_feed(area: str, label: str, url: str, cutoff: dt.datetime) -> list[dict]:
    """Parse an RSS or Atom feed into recent items."""
    raw = _get(url)
    root = ET.fromstring(raw)
    items: list[dict] = []

    # RSS: channel/item ; Atom: feed/entry
    nodes = [n for n in root.iter() if _strip_ns(n.tag) in ("item", "entry")]
    for node in nodes:
        title = link = date_text = None
        for child in node:
            t = _strip_ns(child.tag)
            if t == "title" and child.text:
                title = child.text.strip()
            elif t == "link":
                # RSS puts URL in text; Atom in href attr
                href = child.attrib.get("href")
                if href and (child.attrib.get("rel", "alternate") == "alternate"):
                    link = href
                elif child.text and not link:
                    link = child.text.strip()
            elif t in ("pubDate", "published", "updated", "date") and not date_text:
                date_text = child.text
        date = _parse_date(date_text)
        if date and date < cutoff:
            continue
        items.append({
            "area": area, "source": label, "title": title or "(untitled)",
            "link": link, "date": date.isoformat() if date else None, "signal": None,
        })
    return items


def fetch_hn(area: str, label: str, query: str, tags: str, cutoff: dt.datetime) -> list[dict]:
    ts = int(cutoff.timestamp())
    # Algolia only allows numeric filters on whitelisted attributes (created_at_i,
    # not points) — so filter the date server-side and points client-side.
    url = (
        "https://hn.algolia.com/api/v1/search"
        f"?query={urllib.parse.quote(query)}&tags={tags}"
        f"&numericFilters={urllib.parse.quote(f'created_at_i>{ts}')}"
        "&hitsPerPage=30"
    )
    data = _get_json(url)
    out = []
    for h in data.get("hits", []):
        if h.get("points", 0) < HN_MIN_POINTS:
            continue
        out.append({
            "area": area, "source": label,
            "title": h.get("title") or h.get("story_title") or "(untitled)",
            "link": h.get("url") or f"https://news.ycombinator.com/item?id={h.get('objectID')}",
            "date": h.get("created_at"),
            "signal": f"{h.get('points', 0)} pts / {h.get('num_comments', 0)} comments",
        })
    return out


def get_reddit_token() -> str | None:
    """Application-only OAuth token via client_credentials. Returns None if no creds."""
    cid = os.environ.get("REDDIT_CLIENT_ID")
    secret = os.environ.get("REDDIT_CLIENT_SECRET")
    if not cid or not secret:
        return None
    auth = base64.b64encode(f"{cid}:{secret}".encode()).decode()
    body = urllib.parse.urlencode({"grant_type": "client_credentials"}).encode()
    req = urllib.request.Request(
        "https://www.reddit.com/api/v1/access_token", data=body,
        headers={"Authorization": f"Basic {auth}", "User-Agent": UA},
    )
    with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
        return json.loads(resp.read().decode("utf-8")).get("access_token")


def fetch_reddit(area: str, sub: str, cutoff: dt.datetime, token: str) -> list[dict]:
    # Use the OAuth API host; the public www.reddit.com .json endpoint is 403-blocked.
    url = f"https://oauth.reddit.com/r/{sub}/top?t=week&limit=15"
    req = urllib.request.Request(
        url, headers={"Authorization": f"bearer {token}", "User-Agent": UA},
    )
    with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
        data = json.loads(resp.read().decode("utf-8", "replace"))
    out = []
    for child in data.get("data", {}).get("children", []):
        d = child.get("data", {})
        if d.get("score", 0) < REDDIT_MIN_SCORE:
            continue
        created = dt.datetime.fromtimestamp(d.get("created_utc", 0), tz=dt.timezone.utc)
        out.append({
            "area": area, "source": f"r/{sub}",
            "title": d.get("title", "(untitled)"),
            "link": "https://www.reddit.com" + d.get("permalink", ""),
            "date": created.isoformat(),
            "signal": f"{d.get('score', 0)} upvotes / {d.get('num_comments', 0)} comments",
        })
    return out


# Conventional-commit prefixes that are housekeeping noise, not show-worthy news.
PR_NOISE = re.compile(r"^(chore|ci|build|style|test|refactor)[(:]", re.IGNORECASE)


def fetch_github_prs(area: str, label: str, repo: str, cutoff: dt.datetime) -> list[dict]:
    """Recently-merged PRs for a repo via the `gh` CLI (works for private repos)."""
    cmd = ["gh", "pr", "list", "--repo", repo, "--state", "merged",
           "--limit", "100", "--json", "title,url,mergedAt"]
    try:
        proc = subprocess.run(cmd, capture_output=True, text=True, timeout=TIMEOUT)
    except FileNotFoundError:
        raise RuntimeError("gh CLI not installed — install GitHub CLI and run `gh auth login`") from None
    if proc.returncode != 0:
        tail = (proc.stderr.strip().splitlines() or ["unknown error"])[-1]
        raise RuntimeError(f"{repo}: {tail} (is `gh` authenticated? run `gh auth login`)")
    out = []
    for pr in json.loads(proc.stdout or "[]"):
        d = _parse_date(pr.get("mergedAt"))
        if d and d < cutoff:
            continue
        title = pr.get("title", "(untitled)")
        if PR_NOISE.match(title):  # drop chore/ci/test/build/etc. housekeeping PRs
            continue
        out.append({
            "area": area, "source": label, "title": title,
            "link": pr.get("url"), "date": pr.get("mergedAt"), "signal": None,
        })
    return out


def fetch_hf_spaces() -> list[dict]:
    data = _get_json(HF_SPACES_URL)
    out = []
    for s in data[:15]:
        sid = s.get("id", "")
        out.append({
            "area": "fun", "source": "HF Spaces (trending)",
            "title": sid, "link": f"https://huggingface.co/spaces/{sid}",
            "date": s.get("lastModified") or s.get("createdAt"),
            "signal": f"{s.get('likes', 0)} likes (trending {round(s.get('trendingScore', 0))})",
        })
    return out


def fetch_hf_papers(cutoff: dt.datetime) -> list[dict]:
    data = _get_json(HF_PAPERS_URL)
    out = []
    for p in data:
        paper = p.get("paper", {})
        pub = _parse_date(p.get("publishedAt") or paper.get("publishedAt"))
        if pub and pub < cutoff:
            continue
        pid = paper.get("id", "")
        out.append({
            "area": "ai-news", "source": "HF Daily Papers",
            "title": paper.get("title", "(untitled)"),
            "link": f"https://huggingface.co/papers/{pid}",
            "date": pub.isoformat() if pub else None,
            "signal": f"{paper.get('upvotes', 0)} upvotes",
        })
    return out


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def gather(days: int, include_competitors: bool = False) -> tuple[list[dict], list[dict], list[str]]:
    cutoff = dt.datetime.now(dt.timezone.utc) - dt.timedelta(days=days)
    results: list[dict] = []
    errors: list[str] = []
    tasks = []

    # Reddit needs OAuth (the public .json endpoint is 403-blocked). Get one token
    # up front; if there are no credentials, skip Reddit with a single clear note.
    reddit_token = None
    try:
        reddit_token = get_reddit_token()
    except Exception as e:  # noqa: BLE001
        errors.append(f"Reddit OAuth token: {type(e).__name__}: {e}")
    if reddit_token is None and REDDIT_SUBS:
        errors.append(
            "Reddit skipped — set REDDIT_CLIENT_ID and REDDIT_CLIENT_SECRET to include it "
            "(register a free 'script' app at https://www.reddit.com/prefs/apps)."
        )

    with ThreadPoolExecutor(max_workers=12) as ex:
        for area, label, url in FEEDS:
            tasks.append((f"{label} feed", ex.submit(parse_feed, area, label, url, cutoff)))
        for area, label, query, tags in HN_QUERIES:
            tasks.append((label, ex.submit(fetch_hn, area, label, query, tags, cutoff)))
        if reddit_token:
            for area, sub in REDDIT_SUBS:
                tasks.append((f"r/{sub}", ex.submit(fetch_reddit, area, sub, cutoff, reddit_token)))
        for area, label, repo in GITHUB_PR_REPOS:
            tasks.append((label, ex.submit(fetch_github_prs, area, label, repo, cutoff)))
        tasks.append(("HF Spaces", ex.submit(fetch_hf_spaces)))
        tasks.append(("HF Daily Papers", ex.submit(fetch_hf_papers, cutoff)))

        for name, fut in [(n, t) for n, t in tasks]:
            try:
                results.extend(fut.result())
            except Exception as e:  # noqa: BLE001 - one bad source shouldn't kill the run
                errors.append(f"{name}: {type(e).__name__}: {e}")

    # Filter competitors (kept transparent in a separate list, not silently dropped).
    # Never filter Arize's own content: an Arize blog/PR/release that names a competitor
    # (e.g. an OpenInference instrumentation *for* OpenLLMetry) is Arize's product surface,
    # not competitor promotion.
    excluded: list[dict] = []
    if not include_competitors:
        kept = []
        for r in results:
            name = None if r["area"] == "arize" else competitor_match(r)
            if name:
                r["competitor"] = name
                excluded.append(r)
            else:
                kept.append(r)
        results = kept

    # newest first within each area
    results.sort(key=lambda r: (r["area"], r["date"] or ""), reverse=True)
    excluded.sort(key=lambda r: r["date"] or "", reverse=True)
    return results, excluded, errors


AREA_TITLES = {
    "arize": "Arize (Project Spotlight / product updates)",
    "ai-news": "AI news (headline candidates)",
    "frameworks": "Framework & tooling releases",
    "fun": "Fun & viral (Pick of the Week candidates)",
}
AREA_ORDER = ["ai-news", "frameworks", "arize", "fun"]


def to_markdown(results: list[dict], excluded: list[dict], errors: list[str], days: int) -> str:
    now = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%d")
    lines = [f"# Evaluate the Week — candidate digest ({now}, last {days} days)", ""]
    by_area: dict[str, list[dict]] = {}
    for r in results:
        by_area.setdefault(r["area"], []).append(r)
    for area in AREA_ORDER:
        items = by_area.get(area, [])
        lines.append(f"## {AREA_TITLES.get(area, area)} — {len(items)} items")
        lines.append("")
        for r in items:
            date = (r["date"] or "")[:10]
            sig = f" — _{r['signal']}_" if r.get("signal") else ""
            lines.append(f"- **[{r['source']}]** [{r['title']}]({r['link']}) ({date}){sig}")
        lines.append("")
    if excluded:
        lines.append(f"## Excluded — competitors ({len(excluded)} items, do NOT feature)")
        lines.append("")
        for r in excluded:
            date = (r["date"] or "")[:10]
            lines.append(f"- _{r['competitor']}_ — [{r['title']}]({r['link']}) ({date}) [{r['source']}]")
        lines.append("")
    if errors:
        lines.append("## Sources that failed (check manually)")
        lines.append("")
        for e in errors:
            lines.append(f"- {e}")
        lines.append("")
    return "\n".join(lines)


def main() -> int:
    ap = argparse.ArgumentParser(description="Gather weekly candidates for Evaluate the Week.")
    ap.add_argument("--days", type=int, default=7, help="lookback window in days (default 7)")
    ap.add_argument("--out", default="-", help="output markdown path, or - for stdout")
    ap.add_argument("--json", action="store_true", help="also write a .json sidecar")
    ap.add_argument("--include-competitors", action="store_true",
                    help="don't filter out competitor items (default: filter them)")
    args = ap.parse_args()

    results, excluded, errors = gather(args.days, include_competitors=args.include_competitors)
    md = to_markdown(results, excluded, errors, args.days)

    if args.out == "-":
        sys.stdout.write(md)
    else:
        with open(args.out, "w", encoding="utf-8") as f:
            f.write(md)
        print(f"Wrote {len(results)} candidates ({len(excluded)} competitor items "
              f"excluded) to {args.out}", file=sys.stderr)
        if args.json:
            jpath = args.out.rsplit(".", 1)[0] + ".json"
            with open(jpath, "w", encoding="utf-8") as f:
                json.dump({"results": results, "excluded": excluded, "errors": errors}, f, indent=2)
            print(f"Wrote JSON sidecar to {jpath}", file=sys.stderr)
    if errors:
        print(f"\n{len(errors)} source(s) failed — see digest.", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
