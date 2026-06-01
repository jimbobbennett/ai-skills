# Keynote deck automation for Jim's talks

You are helping Jim Bennett build, modify, audit, or export Apple Keynote decks via AppleScript. This skill captures the patterns that work, the gotchas that don't, and Jim's visual-style defaults.

## When to use this skill

Trigger when the user asks you to:

- Build a new Keynote deck from a slide outline
- Modify an existing deck (text updates, slide reordering, master changes)
- Extract a deck's contents to markdown (titles, bodies, presenter notes)
- Export deck slides as PNG for visual review
- Inspect a deck's theme, slide size, or master-slide inventory
- Fork an existing Jim deck as the starting point for a new talk

If the user wants help writing the *content* of the talk, defer to the `write-conference-talk` skill — this skill is about producing and manipulating the `.key` file itself.

## Jim's visual-style defaults

Locked in by inspection of his recent decks (Terrible API, Prompt Learning, EDD, CO2):

| Setting | Value |
|---|---|
| **Theme** | Basic Black |
| **Slide size** | 1920 × 1080 (16:9 widescreen) |
| **Type style** | Helvetica Neue Bold (theme default) |
| **Background** | Solid black |
| **Text colour** | White |
| **Slide 1** | Talk title + bio block + photo of Jim on right — built from the "Title" master with custom photo |
| **Final slide** | Identity card ("Hi, I'm Jim") + bio block + photo — same structure as slide 1 |
| **NO** | Agenda slides, "thanks for having me" slides, multi-CTA stacks, code-on-slides |

When building a new deck for Jim, **fork an existing deck** (typically `~/Desktop/build-an-api-for-people-you-hate.key`) rather than starting from scratch. Forking preserves the photo, bio styling, custom layouts, and Pieces/Arize logo placement. You only need to update the text on slide 1 and the final slide, and insert your content slides between them.

Note: the reference deck still has the *Pieces* logo on slides 1 and 34. When delivering for Arize, replace it manually in Keynote — call this out in speaker notes so it isn't forgotten.

## Basic Black master slide cheat sheet

Inventory from `~/Desktop/build-an-api-for-people-you-hate.key`. Some masters render text via the **body** placeholder, not the title — getting this wrong gives you blank slides.

| Master | Renders title? | Renders body? | Use for |
|---|---|---|---|
| **Title** | ✓ | ✓ | Title slide with bio + photo (forked from reference) |
| **Title Only** | ✓ | — | Single-statement slides at top-left |
| **Statement** | ✗ stored, not rendered | ✓ | Centered single-sentence statements |
| **Big Fact** | ✗ stored, not rendered | ✓ | Massive-text reveal slides (the climax) |
| **Section** | ✓ | — | Single-word section anchors |
| **Title & Bullets** | ✓ | ✓ | Multi-line build slides; recap lists |
| **Title & Photo** | ✓ | photo placeholder | Slides with a single supporting image |
| **Blank** | — | — | Fully-custom hand-laid-out slides |
| **Quote** | ✓ | ✓ | Pull quotes (rarely used) |

**The Statement / Big Fact trap**: AppleScript will *accept* `set object text of default title item` without error, but those masters don't display the title placeholder — only the body. Always set the body too (typically to the same text) when using these masters. The generator in this skill handles this automatically via the `BODY_VIA_TITLE_MASTERS` set.

## AppleScript fundamentals for Keynote

### Strings (quoting and newlines)

AppleScript string literals use straight double quotes. To embed a quote, concatenate the `quote` constant. For newlines, concatenate `linefeed`:

```applescript
set msg to "She said " & quote & "hello" & quote
set body to "Line one." & linefeed & linefeed & "Line two."
```

The generator at `scripts/gen_keynote_deck_template.py` includes a `to_applescript_string` helper that converts a Python string (with `"` and `\n`) to an AppleScript expression that compiles correctly. Use it when writing generators.

### Insertion points — the "at slide N" trap

**Don't** write `make new slide at slide N`. Keynote interprets this as "create a new slide *replacing* slide N", which silently deletes whatever was there. Three patterns that work:

```applescript
-- Append at the end of the deck
make new slide at end of slides of thisDoc

-- Insert before a specific slide
make new slide at before slide 5 of thisDoc

-- Insert after a specific slide
make new slide at after slide 5 of thisDoc
```

Or — most reliable for building decks while keeping a "template" identity slide at the end — append all content at the end, then `move` the identity slide to the end of the deck once content is in place.

### Setting placeholder text

Wrap in try/end try because not every master has both placeholders:

```applescript
tell currentSlide
    try
        set object text of default title item to "Some title"
    end try
    try
        set object text of default body item to "Some body"
    end try
    set presenter notes to "Speaker notes."
end tell
```

For Statement / Big Fact masters, set the body to the same text as the title (see the cheat sheet above).

### Master assignment

```applescript
set newSlide to make new slide at end of slides of thisDoc ¬
    with properties {base slide:slide layout "Title Only" of thisDoc}
```

The master name must match exactly — case and spacing matter.

### Moving slides

```applescript
move slide 2 of thisDoc to after slide (count of slides of thisDoc) of thisDoc
```

This moves slide 2 to the end. Useful when you want to keep an existing styled slide as the "final" slide while inserting new content above it.

### Saving and overwriting

If you save to an existing path, Keynote prompts for overwrite confirmation, which blocks AppleScript. Two ways around it:

1. **Pre-delete the file** before opening, then `save` to the now-free path.
2. **Open the existing file** and just call `save` (no path argument) — saves in place without a prompt.

The generator template uses approach (2): it does a shell `cp` to seed the target file from a reference, then `open POSIX file targetPath` + `save thisDoc`.

## Working scripts in this skill

Three reusable AppleScripts live in `scripts/`. Each takes positional arguments via `osascript script.applescript arg1 arg2`.

### `scripts/extract_keynote.applescript`

Pulls every slide's title, body text, and presenter notes from a `.key` file to a structured markdown file. Use to audit a deck or diff before/after edits.

```bash
osascript scripts/extract_keynote.applescript ~/Desktop/some-deck.key /tmp/extracted.md
```

### `scripts/export_keynote_pngs.applescript`

Renders every slide as a PNG in a folder. Use to visually review a deck without opening Keynote.

```bash
osascript scripts/export_keynote_pngs.applescript ~/Desktop/some-deck.key /tmp/pngs/
```

Output files are named `<folder-basename>.NNN.png` (one per slide, 1-indexed).

### `scripts/inspect_keynote_theme.applescript`

Reports the theme name, slide dimensions, slide 1's master, and the list of available masters. Use before forking a deck or when troubleshooting an unexpected layout.

```bash
osascript scripts/inspect_keynote_theme.applescript ~/Desktop/some-deck.key
```

## The generator pattern (Python + AppleScript)

For a deck of more than ~10 slides, **don't write AppleScript by hand**. Use a Python script that emits a single AppleScript file, then runs it via `osascript`. The Python side holds the slide data as readable tuples; the AppleScript side does the work.

Template at `scripts/gen_keynote_deck_template.py`. The pattern:

1. Define `SLIDES = [(title, body, notes, master), ...]` in Python.
2. Convert each Python string to an AppleScript expression via `to_applescript_string` (handles `"` → `& quote &` and `\n` → `& linefeed &`).
3. Either:
   - **Build from scratch**: `make new document with properties {document theme:theme "Basic Black", width:1920, height:1080}`, then iterate slides appending at end.
   - **Fork an existing deck**: shell `cp` reference → target, open target, delete slides you don't want, update text on kept template slides, insert new slides at end, move template slides to their final positions.

The fork pattern is what produced `context-graphs-talk.key` from `build-an-api-for-people-you-hate.key`. Forking preserves Jim's photo, bio styling, custom master tweaks, and logo placement automatically.

## Workflow: build a new deck for Jim

1. **Pick a reference deck** — usually `~/Desktop/build-an-api-for-people-you-hate.key`. The reference's slide 1 (title) and last bio slide are what you'll fork.
2. **Inspect the reference** — `scripts/inspect_keynote_theme.applescript` to confirm theme + size + masters.
3. **Define the SLIDES list** in a Python generator. One tuple per slide: `(title, body, notes, master)`. Empty body is allowed; the generator handles Statement/Big Fact body-via-title automatically.
4. **Run the generator** — it shell-copies the reference, opens it, prunes content, updates the two template slides, inserts the new content, moves the identity slide to the end, and saves.
5. **Extract the result** — `scripts/extract_keynote.applescript` to confirm titles/bodies/notes landed correctly.
6. **Export PNGs** — `scripts/export_keynote_pngs.applescript` to spot-check the visual rendering.
7. **Hand off to user** for the manual touch-ups (image insertion, build animations, logo swap).

## Workflow: modify an existing deck

For text-only edits, the cleanest path is open + modify + save (no fork). For structural changes (insert slides, reorder), use AppleScript or do it manually in Keynote — both work, but AppleScript wins for bulk edits.

For inserting between specific slides, use `at before slide N` or `at after slide N` rather than `at slide N` (see the gotcha above).

## Gotchas (learned the hard way)

1. **`at slide N` replaces, doesn't insert.** Always use `at before slide N`, `at after slide N`, or `at end of slides`.
2. **Statement / Big Fact masters need body text set**, not just title. The title is stored (visible to `extract`) but not rendered. Set both.
3. **`default title item` / `default body item` raise if the master has no such placeholder.** Always wrap in try/end try.
4. **Save-with-path prompts on overwrite.** Pre-delete the target, or open the existing file and call `save` without a path.
5. **Custom photo + bio layout is per-slide, not per-master.** When forking, you keep the photo because it's on the actual slide, not on the master. Don't expect new slides using the same master to inherit the photo.
6. **Pieces logo bleeds through.** The reference deck has Pieces branding on slides 1 and last. Replace manually after forking. Note this in speaker notes during generation.
7. **Newlines in AppleScript literals don't survive.** Use `& linefeed &` concatenation. The `to_applescript_string` helper handles this for you.
8. **Quotes inside speaker notes** need to be escaped (use `quote` constant) or replaced with apostrophes. The helper handles this too.

## Don't-do list

- **No agenda slide** at the start. Jim's talks never have one.
- **No "thanks for having me"** slide. Same reason.
- **No bullets in body text** except where Jim wants a progressive build (and even then, you toggle off the bullet markers in Keynote after generation — the generator can't strip them in AppleScript reliably).
- **No code on slides.** Code lives in the demo terminal.
- **No multi-CTA stacks** at the close. Identity slide gets ONE CTA: Jim's social handle.
- **No bio upfront.** Bio belongs on slide 1 (small block alongside the talk title) and on the final identity slide. Never on a separate "About me" slide.

## When manual Keynote work beats AppleScript

AppleScript can't do (or does poorly):

- **Setting fonts / colours / sizes** on specific text frames (only changes master-level attributes reliably)
- **Build animations** (Animate → Build In → By Paragraph)
- **Image insertion at specific positions** with sizing/cropping
- **Resizing text frames** to accommodate longer text
- **Overlay annotations** (highlight rectangles, callout arrows, etc.)

For all of these, generate the deck via AppleScript first, then do the visual styling pass manually in Keynote. Capture the manual steps in the slide's speaker notes during generation so the user knows what to do.

## Iteration log

Add notes here as we discover more patterns through building actual decks.

- **2026-05-15**: First version. Built `context-graphs-talk.key` by forking `build-an-api-for-people-you-hate.key`. Learned the Statement/Big Fact body-rendering trap, the `at slide N` insertion trap, and the fork-then-prune-then-insert-at-end-then-move pattern.

$ARGUMENTS
