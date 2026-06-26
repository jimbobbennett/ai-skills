# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

A collection of Claude Code **skills** authored by Jim Bennett. There is no application to build, run, or test — each top-level directory is a self-contained skill that an agent loads at runtime. "Working in this repo" means authoring or editing skill content, not compiling code. The only executable code lives inside skills as helper scripts (AppleScript, Python) that the skill's own instructions invoke.

## Skill anatomy

Each skill is a directory containing:

- `SKILL.md` — the instructions an agent reads when the skill activates. This is the primary artifact.
- Optional `references/` — long-form corpus/reference material the SKILL.md points to (read on demand, not inlined). E.g. `write-conference-talk/references/accepted-talks.md`, `title-craft.md`.
- Optional `scripts/` — executable helpers the skill drives. E.g. `keynote-decks/scripts/` holds AppleScript (`extract_keynote`, `export_keynote_pngs`, `inspect_keynote_theme`) and a Python deck generator template.
- Optional `transcripts/` and analysis files (e.g. `write-conference-talk/ANALYSIS.md`) — source material the skill was distilled from and still references.

When adding a skill, register it in `README.md` under `## Skills` — that list is maintained by hand.

## Frontmatter convention (inconsistent — match the modern form)

The newer skills (`blog-diagrams`, `review-work`, `save-research`) begin with YAML frontmatter:

```
---
name: <kebab-case-name>
description: <what it does + when to use / when to skip, written as activation triggers>
---
```

The `description` is the activation contract: it states both what the skill does and the trigger phrases / conditions under which an agent should reach for it (and often what to use *instead*). Write descriptions that way.

Older skills (`keynote-decks`, `write-blog-post`, `write-conference-talk`) start directly with an `#` heading and no frontmatter. Prefer the frontmatter form for new or edited skills.

## Cross-skill relationships

Skills reference each other and defer rather than duplicate:

- `write-blog-post` (written voice) vs `write-conference-talk` (spoken voice) — distinct voices; each tells the agent when to defer to the other.
- `keynote-decks` produces/manipulates the `.key` file; it defers talk *content* to `write-conference-talk`.
- `blog-diagrams` is the matplotlib path; it explicitly hands off to Excalidraw/JS/seaborn for cases it doesn't cover.
- `save-research` persists artifacts to `~/.research/` (the user's home, deliberately outside any project) so research survives across sessions.

When editing one skill, keep these hand-off boundaries intact rather than absorbing another skill's scope.

## Authoring notes

- The voice/style skills (`write-blog-post`, `write-conference-talk`) are derived from a corpus analysis. Treat their stated rules as binding constraints distilled from real talks/posts, not suggestions — when editing them, change rules only with corpus evidence.
- SKILL.md files address the agent in the second person ("You are...") and lead with a "When to use this skill" section listing concrete trigger actions. Follow that structure.
