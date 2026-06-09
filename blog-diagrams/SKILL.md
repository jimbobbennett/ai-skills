---
name: blog-diagrams
description: Build matplotlib diagrams for blog posts — architecture comparisons, taxonomies, timelines, multi-panel charts, gap diagrams. Use when a piece needs supporting visualizations and you want a consistent aesthetic without rebuilding the layout primitives each time. Skip for sketchy/hand-drawn diagrams (use Excalidraw via MCP), interactive visualizations (use a JS lib), or precise statistical charts (use seaborn).
---

# Blog Diagrams

Builds clean, publication-ready PNG diagrams for technical blog posts. Optimized for the common shapes that recur across architecture, taxonomy, and timeline posts.

## When to use

- The piece needs at least one architectural diagram (side-by-side comparison, multi-step flow, taxonomy grid, timeline).
- You want consistent typography and palette across several diagrams in the same post or across a series.
- The output is PNG for insertion into markdown, Google Docs, or a CMS.

## When not to use

- **Sketchy / hand-drawn aesthetic** — use Excalidraw via the MCP `create_view` tool instead.
- **Interactive visualizations** — use D3, Observable, or similar.
- **Statistical charts where the data is the point** — seaborn/plotnine produce better axes and labels than the patterns here.

## Setup

Requires matplotlib (any 3.x). No other dependencies.

```bash
python -m pip install matplotlib
```

Save diagrams to a piece-specific subdirectory so they group cleanly:

```
generated/blog/images/<post-slug>/
  diagram-1.png
  diagram-2.png
```

## Palette (starting point)

These six colours plus two greys cover all the patterns below. Override per project as needed — the patterns work with any palette.

```python
DEEP = "#3F2A56"        # primary, used for titles and dark text
PURPLE = "#7C5CA8"      # accent A
TEAL = "#3CA8AB"        # accent B
ORANGE = "#E89A3C"      # accent C (warning / one-of-two sides)
RED = "#C44D4D"         # negative / failure
GREEN = "#5BA66A"       # positive / success / preserved
GRAY = "#9A9A9A"        # secondary text, neutral edges
LIGHT_GRAY = "#E6E6E6"  # grid lines, dividers
SOFT_BG = "#F7F4FA"     # soft fill behind boxes
TEXT = "#222222"        # body text
```

Standard rcParams to apply once at the top of every script:

```python
plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 10.5,
    "axes.edgecolor": TEXT,
    "xtick.color": TEXT,
    "ytick.color": TEXT,
})
```

## Pattern 1: Side-by-side architecture comparison

Two architectural approaches contrasted across a vertical divider. Each side: title, sequence of boxes connected by arrows, optional loop arrow, footer summary. Use one accent colour per side.

Scaffold:

```python
fig, ax = plt.subplots(figsize=(14, 9))
ax.set_xlim(0, 100); ax.set_ylim(0, 100); ax.axis("off")

ax.text(50, 94, "Title", ha="center", fontsize=17, fontweight="bold", color=DEEP)
ax.text(50, 90, "Subtitle", ha="center", fontsize=11, color=GRAY, style="italic")

# Divider down the middle
ax.plot([50, 50], [12, 84], color=LIGHT_GRAY, linestyle="--", linewidth=1.5)

# Left side title (e.g. green/preserved)
ax.text(25, 80, "Approach A", ha="center", fontsize=14, fontweight="bold", color=GREEN)

# Boxes flow top-to-bottom on the left
box = FancyBboxPatch((10, 60), 30, 10,
                    boxstyle="round,pad=0.5,rounding_size=0.6",
                    facecolor="white", edgecolor=GREEN, linewidth=2)
ax.add_patch(box)
ax.text(25, 65, "Step 1 label", ha="center", va="center", fontsize=11)

# Arrows between boxes
ax.annotate("", xy=(25, 58), xytext=(25, 50),
            arrowprops=dict(arrowstyle="->", color=DEEP, lw=1.6))

# Right side mirrors left
# Loop arrow back to top (for in-place / iterated pattern)
loop = FancyArrowPatch((60, 19), (60, 65),
                       arrowstyle="->", color=ORANGE, lw=2,
                       connectionstyle="arc3,rad=-0.55", mutation_scale=18)
ax.add_patch(loop)

# Footer banner at bottom
footer = FancyBboxPatch((10, 2), 80, 6,
                        boxstyle="round,pad=0.4,rounding_size=0.6",
                        facecolor=DEEP, edgecolor=DEEP, alpha=0.95)
ax.add_patch(footer)
ax.text(50, 5, "One-line synthesis", ha="center", va="center",
        fontsize=11, color="white", style="italic", fontweight="bold")
```

## Pattern 2: Multi-column taxonomy

N parallel columns, each describing one bucket/category. Rows below for mechanism, examples, what-it-solves, etc. Use a distinct accent colour per column.

Scaffold (4-column variant):

```python
buckets = [
    ("1", "Title A", PURPLE, "Mechanism", ["Example", "Example"], "What it solves"),
    ("2", "Title B", ORANGE, "...", [...], "..."),
    ("3", "Title C", TEAL, "...", [...], "..."),
    ("4", "Title D", GREEN, "...", [...], "..."),
]
col_w, gap = 22, 2.5
start_x = (100 - 4*col_w - 3*gap) / 2

for i, (num, name, color, mech, examples, solves) in enumerate(buckets):
    cx = start_x + i * (col_w + gap) + col_w / 2
    # Title block (coloured header)
    ax.add_patch(FancyBboxPatch((cx - col_w/2, 73), col_w, 11,
                                boxstyle="round,pad=0.6", facecolor=color,
                                edgecolor=color, linewidth=2))
    ax.text(cx, 78, name, ha="center", va="center",
            fontsize=12, fontweight="bold", color="white")
    # Mechanism, examples, solves rows below — each its own FancyBboxPatch
```

## Pattern 3: Horizontal timeline with two tracks

A chronological lineage split into two thematic tracks. Year anchors along the top, two horizontal lines below, named events on each line with one-line subtitles. Use distinct colours per track.

Critical gotcha: **single-line subtitles only**. Multi-line subtitles with `va="bottom"` collide with the title above them. Stick to one line per event.

Helper function:

```python
def node(ax, x, y, title, sub, color, above=True):
    """One event on a track. above=True puts label above the track line."""
    ax.plot([x, x], [y-1.4, y+1.4], color=color, linewidth=2.4)  # tick
    ax.plot(x, y, marker="o", markersize=10, color=color,
            markeredgecolor="white", markeredgewidth=1.6)         # dot
    if above:
        ax.plot([x, x], [y+1.6, y+6], color=color, lw=1, alpha=0.55)
        ax.text(x, y+7, sub, ha="center", va="center",
                fontsize=8.5, color=TEXT, style="italic")
        ax.text(x, y+10, title, ha="center", va="center",
                fontsize=10, fontweight="bold", color=DEEP)
    else:
        ax.plot([x, x], [y-1.6, y-6], color=color, lw=1, alpha=0.55)
        ax.text(x, y-7, title, ha="center", va="center",
                fontsize=10, fontweight="bold", color=DEEP)
        ax.text(x, y-10, sub, ha="center", va="center",
                fontsize=8.5, color=TEXT, style="italic")
```

Lay out year anchors first, then call `node()` for each event. Space events so subtitles don't horizontally overlap: rule of thumb is 14 units minimum between events on the same track if subtitles are full-length.

## Pattern 4: Multi-panel chart row

Three side-by-side charts illustrating the same finding across different benchmarks. Use `plt.subplots(1, 3, figsize=(15, 6.5))` so the panels share styling and the figure title spans all three.

```python
fig, axes = plt.subplots(1, 3, figsize=(15, 6.5))
fig.suptitle("Same finding, three benchmarks", fontsize=15,
             fontweight="bold", color=DEEP, y=1.02)

# Per panel: set title with pad=8 so it sits above the axes cleanly
ax.set_title("Panel title", fontsize=11, fontweight="bold", color=DEEP, pad=8)

# Use ax.text(0.5, -0.25, "...", transform=ax.transAxes, ...) for one-line
# caption below each panel — gives all panels a consistent caption row
```

## Pattern 5: 2×2 grid with empty centre (gap diagram)

Four buckets arranged around a central labelled void. Useful for "the missing X sits between these N approaches" framings.

```python
bucket_layout = [
    (28, 70, "1", "Title A", PURPLE),
    (72, 70, "2", "Title B", ORANGE),
    (28, 32, "3", "Title C", TEAL),
    (72, 32, "4", "Title D", GREEN),
]
for cx, cy, num, name, color in bucket_layout:
    ax.add_patch(FancyBboxPatch((cx-18, cy-9), 36, 18,
                                boxstyle="round,pad=0.6", facecolor=SOFT_BG,
                                edgecolor=color, linewidth=2.5))
    ax.text(cx, cy, name, ha="center", va="center",
            fontsize=12, fontweight="bold", color=TEXT)

# Centre gap
ax.add_patch(FancyBboxPatch((38, 44), 24, 14,
                            boxstyle="round,pad=0.6", facecolor=DEEP,
                            edgecolor=DEEP, linewidth=3, alpha=0.95))
ax.text(50, 53, "Missing thing", ha="center", va="center",
        fontsize=15, fontweight="bold", color="white")

# Inward dashed arrows from each bucket to the gap
for x1, y1, x2, y2 in [(39, 60.5, 43, 56), (61, 60.5, 57, 56),
                        (39, 41.5, 43, 46), (61, 41.5, 57, 46)]:
    ax.annotate("", xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle="->", color=GRAY, lw=1.4,
                                linestyle=(0, (3, 2))))
```

## Pattern 6: Bar / line chart with annotations

Standard matplotlib bar or line plot dressed up to match the rest of the diagram set.

```python
bars = ax.bar(labels, values, color=colors, edgecolor=DEEP, linewidth=1.2, width=0.6)
for bar, value in zip(bars, values):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1.5,
            f"{value}%", ha="center", va="bottom",
            fontsize=13, fontweight="bold", color=DEEP)

# Standard axis cleanup
ax.set_axisbelow(True)
ax.yaxis.grid(True, linestyle="--", color=LIGHT_GRAY, alpha=0.8)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_color(LIGHT_GRAY)
ax.spines["bottom"].set_color(LIGHT_GRAY)
ax.tick_params(axis="x", which="both", length=0)

# Annotate specific points with style="italic" and color matching the data line
ax.annotate("baseline reached", xy=(x, y), xytext=(x, y_above),
            fontsize=8.5, color=ORANGE, style="italic",
            arrowprops=dict(arrowstyle="->", color=ORANGE, lw=1))
```

## Common pitfalls

- **Timeline label collisions.** Multi-line subtitles with `va="bottom"` extend upward and overlap the title placed just above. Use single-line subtitles for timeline events.
- **Multi-line text + `va="center"`.** Works fine for centred labels in boxes; do not mix with `va="bottom"` in adjacent positions or layouts will collide.
- **Two events at the same year.** If two timeline events share a year, the dot-and-label scaffolding crashes. Either drop one or stagger horizontally by ~6 units (and treat as separate ticks on the same year).
- **Headline-y placement in `suptitle`.** When using `plt.subplots(1, N)`, the figure-level title needs `y=1.02` or higher to clear the panel titles.
- **Figure size.** For complex diagrams (architecture comparisons, 2×2 grids), `figsize=(14, 9)` or larger gives enough room for boxes plus a footer banner. Cramped figures look amateur.
- **DPI.** Save at `dpi=200` for crisp output in Google Docs / web. `dpi=300` is overkill for most blog use.

## Output convention

```python
plt.tight_layout()
plt.savefig(OUT / "diagram-name.png", dpi=200,
            bbox_inches="tight", facecolor="white")
plt.close()
```

`bbox_inches="tight"` trims whitespace around the figure. `facecolor="white"` keeps the background opaque (important for slides and Google Docs).

## When to combine with Excalidraw

For pieces that need both a clean architecture diagram (matplotlib) and a sketchy / annotated whiteboard-style diagram (Excalidraw via MCP), build the architecture diagrams here and use the MCP `create_view` tool for the annotated whiteboard. The two aesthetics complement rather than compete.

## Iteration tips

- **Render small first.** Test layouts with `dpi=100` to iterate faster, then bump to 200 for final.
- **Read the PNG.** Build the diagram, then `Read` the PNG to verify it before committing. A render that looks fine in code can have label collisions you only see in the image.
- **One pass to fix collisions.** Timeline diagrams especially. If two labels overlap, widen spacing or shorten subtitles before declaring done.

$ARGUMENTS
