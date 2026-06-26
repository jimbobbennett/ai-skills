---
name: evaluate-the-week
description: Produce a script outline for "Evaluate the Week" — Jim Bennett's short weekly video summarizing the week in AI plus the latest from Arize, styled after Christina Warren's *The Download*. Gathers the past week's stories from free AI-news, framework, and fun/viral sources plus Arize's own channels, then maps the winners onto a ~7–8 minute segment skeleton. Use when the user wants to prep the weekly recording, asks for "this week's AI roundup", or says "evaluate the week".
---

# Evaluate the Week

Generates the **script outline** for a weekly ~7–8 minute video where Jim summarizes the week in AI for AI engineers (the Arize audience) and folds in the latest from Arize. Modeled on the format of *The Download with Christina Warren*: fast, curated, ~80% substantive / 20% delight, with named recurring segments.

The deliverable is an **outline only** — bullets per segment with links and suggested b-roll. Jim writes the actual narration in his own voice (use the `write-blog-post` skill's voice guide as a reference if you draft any prose).

## When to use this skill

Trigger when the user asks you to:

- Prep / draft this week's "Evaluate the Week" recording
- Get "the week in AI" roundup for the show
- Refresh the candidate stories before recording

## The format to hit (from *The Download*)

~7–8 minutes, news-anchor tempo. Keep segment names consistent week to week.

| # | Segment | Time | What goes here |
|---|---------|------|----------------|
| 1 | **Cold open / intro** | 0:00–0:30 | Branded hello, tease 2–3 headlines. Energetic, personal. |
| 2 | **Headline stories ×3–5** | ~1:00–5:30 | The week's biggest AI-engineering news: model releases, framework/tooling drops, eval & observability news, notable papers. 60–120s each. Give the single biggest story a ~2-min deep dive. |
| 3 | **Project Spotlight** | ~5:30 | One cool/quirky open-source AI project of the week — *and* this is the natural slot for the **latest from Arize** (a Phoenix release, a blog post, a new AX feature). Tie Arize in here rather than as an ad. |
| 4 | **Pick of the Week** | final ~45s | The fun/viral item — a delightful demo, meme, or non-work nerd-culture pick. Personality payoff + sign-off. |

Style notes to preserve: curatorial trusted-friend voice ("here's what actually mattered this week"), authentic not corporate, every item links to a source, anchor news back to Arize/evals where it's natural — never forced.

**Jim's voice rules for the script (apply when drafting narration):**
- **Clean cold open — no filler opener.** Do NOT start the first line with "Right,", "So,", "Okay,", "Alright," or similar throat-clearing. Open straight on the substance (e.g. "Big week." not "Right — big week."). Jim does this verbally on instinct; the script should not bake it in.
- **No "let's get into it" (or equivalent) before the title card.** End the cold open on the branded hello itself ("I'm Jim, this is Evaluate the Week.") — don't tack on a "let's dive in" / "let's get into it" call-to-action.
- Otherwise use Jim's written voice as the reference: conversational, first person, contractions, dry/understated humour, light British phrasing, genuine enthusiasm ("pretty cool") over hype, self-deprecating where natural.

## Workflow

### 1. Gather the week's candidates

Run the gather script — it pulls the last 7 days from all free, no-auth sources (RSS/Atom feeds, Hacker News, Hugging Face, GitHub Trending, Arize's own channels) and writes a grouped digest:

```bash
python3 scripts/gather_week.py --days 7 --out /tmp/etw-candidates.md --json
```

- stdlib only — no `pip install` needed.
- Output groups candidates into **AI news**, **Framework & tooling releases**, **Arize**, and **Fun & viral**, each item with source, date, link, and an engagement signal (points / upvotes / likes) where available.
- A "Sources that failed" section lists any feed that errored — check those manually if a key one is missing.
- An "Excluded — competitors" section lists items filtered out because they reference an Arize competitor (see below) — **never feature these in the show**.
- Edit the `FEEDS` / `HN_QUERIES` / `REDDIT_SUBS` config blocks at the top of the script to tune what the show watches.

### 2. Rank and select

Read the digest and pick the lineup:

- **Headlines (3–5):** prioritize by genuine impact for engineers building agents — major model releases, significant framework releases (breaking changes, new agent capabilities), eval/observability developments, papers with high HF/HN upvotes. Cross-source corroboration (a story appearing in multiple feeds) is a strong signal. Dedup the same story across sources.
- **Project Spotlight + Arize:** pick the single best Arize item of the week (newest Phoenix release with real features, a strong blog post, or an AX changelog entry) and, if there's room, one delightful OSS project. The Arize tie-in should connect to a headline where possible (e.g. "everyone shipped agents this week — here's how you'd actually evaluate one").
- **Pick of the Week:** the most fun/viral item — rank by engagement signal, favor visual demos and genuinely funny things over hype. One clear winner.
- **Never feature a competitor.** The script auto-filters known competitors into an "Excluded" section, but apply judgment too: if a headline's main subject is a rival observability/eval platform, drop it. Don't frame a story so it promotes a competitor's product.

## Competitor filtering

Arize competes in **LLM observability / evaluation / tracing**, so the script filters that category out of the digest (into a transparent "Excluded" section — not silently dropped). The `COMPETITORS` list at the top of `scripts/gather_week.py` covers LangSmith, Pydantic Logfire, Langfuse, Braintrust, W&B Weave, Comet/Opik, Helicone, Galileo, Fiddler, WhyLabs, HoneyHive, Humanloop, LangWatch, Traceloop, Confident AI/DeepEval, PromptLayer, Literal AI, Maxim, Patronus, Athina, Langtrace, Portkey, Lunary, TruEra, and Datadog LLM Observability.

**The filtering is surgical by design.** Several companies ship *both* an agent framework Arize integrates with *and* a competing observability product:

- **Pydantic** — Pydantic **AI** (framework) is an integration partner and stays in the digest; Pydantic **Logfire** (observability) is a competitor and is filtered.
- **LangChain** — the LangChain/LangGraph framework stays; **LangSmith** is filtered.

So framework release news still comes through; only the competing *products* are blocked. To exclude a company wholesale, add its framework name/domain to that company's entry in `COMPETITORS` (e.g. add `"pydantic-ai"` or `"langchain"`). To see everything including competitors, run with `--include-competitors`.

### 3. Emit the outline

Write the outline to a file Jim can record from. For each segment include: a one-line hook, 2–4 bullet talking points, the source link(s), and a **b-roll** note (what to screen-record or show). Keep it tight — this is a script *outline*, not narration.

## Source coverage (v1 = free / no-auth only)

What the script pulls automatically:

- **Arize:** blog RSS (`arize.com/blog/feed/`), Phoenix + OpenInference GitHub releases (`.atom`), Arize YouTube (channel RSS), **and recently-merged PRs on `Arize-ai/docs` (private) + `Arize-ai/openinference`** via the `gh` CLI — see below.
- **AI news:** AI News (smol.ai), Latent Space, Import AI, **TLDR AI** (`tldr.tech/api/rss/ai`), **Lenny's Newsletter**, OpenAI, Google DeepMind, Google Developers, Hugging Face blog, **Vercel** (`vercel.com/atom`), arXiv cs.CL; HN front-page (AI-filtered); HF Daily Papers (by upvotes).
- **Frameworks:** GitHub `releases.atom` for LangChain, LangGraph, LlamaIndex, CrewAI, OpenAI Agents SDK, vLLM, Ollama, DSPy, Pydantic AI, MCP spec.
- **Fun & viral:** HN Show HN, GitHub Trending (weekly RSS), HF Spaces (trending this week), and Reddit top-of-week (r/aivideo, r/StableDiffusion, r/singularity, r/ProgrammerHumor, r/aimemes) **when Reddit OAuth credentials are set** — see below.

### Arize integration radar (a key editorial angle)

The most valuable "latest from Arize" story is often **"a big tool launched this week, and Arize already supports it."** This is exactly why the script tracks merged PRs on `Arize-ai/docs` and `Arize-ai/openinference`: a new integration shows up there (often days before a blog post). For example, the week of 2026-06-24 the docs PRs included *"add Vercel Eve integration guide"* and *"docs(vercel): AI SDK v7 tracing guide"* while Vercel's own feed announced Eve — a perfect headline-plus-Arize-tie-in pairing. When you see a launch in the AI-news section that also has a matching Arize docs/openinference PR, lead the Project Spotlight with that pairing.

### GitHub PRs (needs the `gh` CLI)

The Arize docs repo is **private**, so PR review uses the **`gh` CLI** under your signed-in account rather than an API token. Run `gh auth login` once. If `gh` is missing or unauthenticated, those two repos are skipped with a clear note (the rest of the digest is unaffected). PRs with housekeeping prefixes (`chore`/`ci`/`build`/`style`/`test`/`refactor`) are filtered out as noise; `feat`/`fix`/`docs` come through. Edit `GITHUB_PR_REPOS` / `PR_NOISE` in the script to tune.

### Reddit (gated — off by default)

Reddit is **not pulled automatically** and self-service app registration no longer works. Two layers of friction, both confirmed 2026-06:

1. The public `.json`/`.rss` endpoints return 403 for all unauthenticated clients (any User-Agent, any IP — not a sandbox/CI limitation).
2. Under Reddit's [Responsible Builder Policy](https://support.reddithelp.com/hc/en-us/articles/42728983564564-Responsible-Builder-Policy) (updated 2026-06-05), creating *any* API app — including free, personal, read-only — requires a pre-approval application: a written project description, a ~2–4 week review, and evaluation of account age / karma / community participation. A brand-new account is unlikely to be approved.

The script still supports Reddit via application-only OAuth **if** you have approved credentials — set `REDDIT_CLIENT_ID` and `REDDIT_CLIENT_SECRET` and it pulls the subreddits in `REDDIT_SUBS`; otherwise it skips Reddit with a single note. Given the approval cost, the practical play is to **leave Reddit off and check r/aivideo + r/StableDiffusion by hand in a browser** while recording if you want the best visual viral picks. The automated fun segment runs off HN Show HN, GitHub Trending, and HF Spaces.

### Other gaps / caveats
- **Scrape-only labs** (Anthropic, Meta, Mistral) have no RSS and are not pulled — check `anthropic.com/news` etc. manually for major releases.
- **AX release notes** (`arize.com/docs/ax/release-notes`) have no RSS, but the weekly "Release Notes AX" PR usually shows up in the `Arize-ai/docs` PR feed — so they're now partly covered via `gh`. Glance at the page directly if you need the rendered detail.
- **X/Twitter & TikTok** (strongest fun/viral signal) need paid scraping and are deliberately out of v1. To add the fun segment's best source, seed candidates from curator accounts @venturetwins and @minchoi manually, or wire a paid scraper later.
- If running inside the Arize marketing-agents repo, the `youtube`, `typefully`, `twitter`, `linkedin`, `zuddl`, and `luma` skills give richer Arize/social data than the no-auth feeds here — prefer them when available.

## Production (optional): automating the recording with Descript

Descript has an **MCP connector for Claude**, which can take the finished transcript all the way to a published video draft — no manual narration if you use a cloned voice.

**Recommended for the weekly agent: connect from Claude Code (no desktop app).** Descript's connector is a remote **Streamable-HTTP MCP server** at `https://api.descript.com/v2/mcp` (verified live 2026-06-26: "Descript MCP Server" v1.3.0). This is the **media-generation-capable** endpoint — i.e. the Claude Code path gives you the full custom setup, not the limited directory connector. Add it once, reused across projects:

```bash
claude mcp add --transport http --scope user descript https://api.descript.com/v2/mcp
```

Then in a Claude Code session run `/mcp` and complete the Descript browser OAuth (no API token — it uses your Descript login and connects to whichever Drive you're signed into). Verify with `claude mcp list` / `claude mcp get descript`. (Headless/SSH: `claude mcp login descript --no-browser`.)

**Tools the server exposes** (from the live server's own description):
- `import_media` — import media via URL or direct file upload (auto-transcribes); also creates empty projects.
- `prompt_project_agent` — natural-language agent that creates/edits projects: trim, rearrange, **remove filler words, add captions**, generate AI images/video, import stock media, and more. Multi-turn via `conversation_id`.
- `list_projects` / `get_project` — discover project + composition IDs before editing.
- `wait_for_job` / `list_jobs` / `cancel_job` — jobs run async; `import_media` and `prompt_project_agent` return a `job_id` + `project_url` immediately, then poll with `wait_for_job`.

Note: cloned-voice narration ("AI Speaker") is driven through `prompt_project_agent` and needs your AI Speaker set up in Descript first — confirm it works with a small test before relying on it weekly. The desktop **directory connector** is the alternative but **can't generate media**; skip it for this use case.

**Possible end-to-end weekly pipeline:**
1. `gather_week.py` → digest
2. Claude drafts the transcript per this skill (clean cold open, segment skeleton, Jim's voice rules)
3. Descript MCP: **AI Speaker** narrates the transcript in Jim's cloned voice → **Underlord** adds captions / Studio Sound / strips filler → **publish** a draft link to review

**Heads-up — it costs credits.** Per Descript's docs, using the MCP **consumes media minutes (imports) and AI credits (Underlord edits + AI Speaker generation)**. A weekly automated run is a recurring cost — pick a Descript plan that covers ~52 episodes/yr of generation + editing.

**Other notes:**
- The Claude Code "network egress / code execution" toggles from the desktop app **don't apply** to Claude Code — MCP access there is governed by permission rules, not those toggles.
- Sanity-test after connecting: *"Create a new Descript project called 'Test' and generate a short video about morning coffee."* Descript's docs confirm a full *"write a script, turn it into a video, and publish it"* flow works in one conversation.
- Alternatives to the interactive MCP: the **desktop app directory connector** (no media generation — skip for this) or the **Descript API** for a fully headless weekly cron.
- Docs: [Connect Descript to Claude](https://help.descript.com/hc/en-us/articles/45008080343053-Connect-Descript-to-Claude), [Descript MCP overview](https://help.descript.com/hc/en-us/articles/46056322186509-Descript-MCP-overview).

## Background

Full research (format breakdown of *The Download*, ranked source lists, Descript automation notes) lives in `~/.research/2026-06-26-evaluate-the-week/`.
