---
name: save-research
description: Persist research artifacts to ~/.research/ so they survive across Claude sessions, machine crashes, context compaction, and branch/worktree switches. Use whenever you are gathering substantive source material from the web, external repos, papers, conference pages, docs, or codebases that informs a deliverable (blog post, talk, plan, design doc, report, brief). Save sources and synthesis incrementally as you find them — do not wait until the end. Triggers on: fetching multiple URLs, cloning a repo for reference, reading a paper, summarizing several sources, or any research that took more than ~3 tool calls to gather. Skip for one-off file reads or trivial lookups.
---

# Save Research

A session's context window disappears the moment the session ends, the computer crashes, or context is compacted. The most expensive thing to redo is **research** — URLs you fetched, repos you cloned, abstracts you pulled, quotes you found, decisions you made about what's relevant. This skill makes that work survive.

All research lives under `~/.research/` (the user's home directory — **not** the current project). It survives crashes, branch switches, worktree cleanups, and is reachable from any session in any project.

## When to use

Use whenever you are gathering substantive material that informs work the user will pick up later, or that took more than ~3 tool calls to gather:

- Fetching web pages, blog posts, abstracts, conference session pages
- Cloning or reading external repos for source material
- Reading PDFs / papers / specs
- Synthesizing findings across multiple sources for a deliverable
- Anything you would be sad to lose if the session ended right now

Do **not** use for:

- One-off file reads in the current repo
- Trivial fact lookups (syntax, error messages, "what's the flag for X")
- Output already being written into a tracked file (the file IS the artifact)

## Where to save

```
~/.research/
  YYYY-MM-DD-<topic-slug>/
    index.md         # running synthesis: framing, key findings, open questions
    sources.md       # one block per source: URL, what's there, key excerpts
    raw/             # optional: full page fetches, READMEs, paper text
```

- One folder per research topic
- `YYYY-MM-DD` is when research **started** — do not change it on later updates
- `<topic-slug>` is short kebab-case (e.g. `microsoft-assert-openinference`)
- Use the absolute path `~/.research/` or `$HOME/.research/` — never rely on the current working directory

## How to save (incrementally, not at the end)

The whole point is that the **next** crash costs you nothing. Don't batch.

1. **First substantive find** — create the topic folder, write `index.md` with a one-paragraph framing of what you're researching and what deliverable it supports. Create an empty `sources.md`.
2. **Each new source** — append a block to `sources.md`: URL, 1-line "what's here," any direct quote or fact worth citing. If it's long (a repo README, a paper), save the relevant chunk under `raw/`.
3. **Each new insight** — append to `index.md` under **Key findings**. Organize by theme, not chronology.
4. **Before declaring research done** — re-read `index.md`. Could a fresh Claude session in a different project pick this up cold? If not, fix it.

## Continuing prior research

Before starting a new topic folder, check `~/.research/` for an existing folder on the same topic. If one exists, **append** to it — don't start a parallel folder. The user will accumulate research on recurring themes over time and expects continuity.

## File formats

### `index.md`

```markdown
# <topic title>

**Started:** YYYY-MM-DD
**For:** <the deliverable this research supports — e.g. "blog post on Microsoft ASSERT", "Q3 planning doc", "DEM361 talk">
**Status:** in-progress | done

## Framing

<1–3 paragraphs on what we're researching and why it matters>

## Key findings

- <finding, with inline link or `(see sources.md#...)` reference>

## Open questions

- <questions still to resolve>
```

### `sources.md`

```markdown
## <URL or repo path>

**What:** <1-line summary of what this source contains>
**Found:** YYYY-MM-DD

> <direct quote worth citing>

<other notes, facts, or excerpts from this source>

---
```

## Notes

- `~/.research/` is intentionally a dotfile so it doesn't clutter `ls ~`. The user knows it's there.
- If the user asks "what research do I have on X", search `~/.research/` first.
- If the user asks for the research from "yesterday's session" or similar, check folder dates.
- Do not move or rename existing research folders unless the user asks.
- This skill complements (does not replace) auto-memory. Memory stores *facts about the user and project*; `~/.research/` stores *the raw material of a deliverable*.
