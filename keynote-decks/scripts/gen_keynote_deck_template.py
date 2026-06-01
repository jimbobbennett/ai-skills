"""Template generator for a Jim-style Keynote deck.

Copy this file to /tmp/ (or anywhere) and customise:
  1. SLIDES — the list of (title, body, notes, master) tuples for your deck.
  2. Optional bio/title constants at the top.
  3. Optional REFERENCE_DECK / TARGET_DECK paths.

Then run: python3 gen_keynote_deck_template.py

The script:
  - Copies the REFERENCE_DECK to TARGET_DECK (so we inherit Jim's title +
    identity slide styling, including the photo and the bio block).
  - Opens TARGET_DECK in Keynote.
  - Deletes all reference content except the title slide (1) and the
    identity slide (63 in the reference deck — adjust if you fork a
    different deck).
  - Updates the text on the title slide and the identity slide.
  - Inserts your SLIDES at the end of the deck.
  - Moves the identity slide to be the last slide in the deck.
  - Saves.

Final deck order: title (1) → your content slides → identity (last).
"""

from __future__ import annotations

import subprocess
from pathlib import Path

# --- CONFIGURATION ------------------------------------------------------------

REFERENCE_DECK = Path.home() / "Desktop" / "build-an-api-for-people-you-hate.key"
TARGET_DECK = Path.home() / "Desktop" / "MY_NEW_TALK.key"

# Reference-deck slide indices we want to keep as templates.
# Adjust if you fork a different deck — `inspect_keynote_theme.applescript`
# will tell you the slide count.
REFERENCE_TITLE_SLIDE = 1
REFERENCE_IDENTITY_SLIDE = 63
REFERENCE_TOTAL_SLIDES = 65

# Talk-specific copy — fill in.
TITLE_SLIDE_TITLE = "Your Talk Title Here."
TITLE_SLIDE_BODY = (
    "Jim Bennett\n\n"
    "Principal Developer Experience Engineer\n\n\n\n"
    "@jimbobbennett\n"
    "linktr.ee/jimbobbennett"
)
TITLE_SLIDE_NOTES = (
    "Speaker notes for the title slide.\n\n"
    "Hand-raise opening goes here (verbal, not on slide).\n\n"
    "NOTE: replace the Pieces logo manually with an Arize logo before delivery."
)

IDENTITY_SLIDE_TITLE = "Hi, I'm Jim"
IDENTITY_SLIDE_BODY = (
    "He/Him\n"
    "Principal Developer Experience Engineer\n\n\n\n"
    "@jimbobbennett\n"
    "linktr.ee/jimbobbennett"
)
IDENTITY_SLIDE_NOTES = (
    "Identity / closing slide.\n\n"
    "Speaker: 'I'm Jim Bennett at Arize. All over the internet at Jim Bob Bennett. Thank you very much.'\n"
    "Then stop. No 'any questions?'."
)

# Your content slides. Each tuple: (title, body, notes, master)
# Empty body is OK for most masters; the generator auto-handles
# Statement/Big Fact which need body set to title text for visible rendering.
SLIDES: list[tuple[str, str, str, str]] = [
    # Example: thesis slide
    ("The gap is the signal.", "", "Big single-line thesis.", "Statement"),
    # Example: section anchor
    ("Capture.", "", "Section anchor with loop diagram.", "Section"),
    # Example: punchy statement
    ("Most teams capture nothing.", "", "Pick-the-fight.", "Title Only"),
    # Example: progressive build (3 lines on one slide)
    (
        "Your reviewer is the domain expert.",
        "Your agent is the policy doc.\n\nThey will disagree.",
        "Animate > Build In > By Paragraph.",
        "Title & Bullets",
    ),
    # Example: photo placeholder
    (
        "Three cycles. No retraining.",
        "",
        "Insert chart.png — agreement-with-Vera trajectory.",
        "Title & Photo",
    ),
    # Example: massive reveal
    (
        "It just lacked permission.",
        "",
        "THE REVEAL. Biggest text on the deck.",
        "Big Fact",
    ),
]

# --- HELPERS ------------------------------------------------------------------

# Masters that render text via the BODY placeholder rather than the title.
# For these, if no explicit body is supplied, we set the body to the title text
# so the slide renders visibly.
BODY_VIA_TITLE_MASTERS = {"Statement", "Big Fact"}


def to_applescript_string(s: str) -> str:
    """Convert a Python string to an AppleScript string-expression.

    Handles double quotes (replaced with the `quote` constant) and newlines
    (replaced with the `linefeed` constant). Empty strings become "".
    """
    if not s:
        return '""'
    parts_quotes = s.split('"')
    pieces: list[str] = []
    for i, q_piece in enumerate(parts_quotes):
        if i > 0:
            pieces.append("quote")
        if q_piece == "":
            continue
        lines = q_piece.split("\n")
        line_pieces: list[str] = []
        for j, ln in enumerate(lines):
            if j > 0:
                line_pieces.append("linefeed")
            if ln != "":
                line_pieces.append(f'"{ln}"')
        if line_pieces:
            pieces.append(" & ".join(line_pieces))
    return " & ".join(pieces) if pieces else '""'


def build_applescript() -> str:
    """Generate the AppleScript that builds the deck."""
    out: list[str] = []
    out.append('on run')
    out.append(f'    set targetPath to "{TARGET_DECK}"')
    out.append('    tell application "Keynote"')
    out.append('        activate')
    out.append('        try')
    out.append('            close every document saving no')
    out.append('        end try')
    out.append('    end tell')
    out.append('    delay 0.5')
    out.append('    tell application "Keynote"')
    out.append('        set thisDoc to open POSIX file targetPath')
    out.append('        delay 1')

    # Delete content slides from the back forward, preserving title (1) and identity.
    # Delete slides AFTER the identity slide first.
    if REFERENCE_TOTAL_SLIDES > REFERENCE_IDENTITY_SLIDE:
        out.append(
            f'        repeat with i from {REFERENCE_TOTAL_SLIDES} to {REFERENCE_IDENTITY_SLIDE + 1} by -1'
        )
        out.append('            delete slide i of thisDoc')
        out.append('        end repeat')
    # Delete slides BETWEEN title (1) and identity.
    if REFERENCE_IDENTITY_SLIDE > REFERENCE_TITLE_SLIDE + 1:
        out.append(
            f'        repeat with i from {REFERENCE_IDENTITY_SLIDE - 1} to {REFERENCE_TITLE_SLIDE + 1} by -1'
        )
        out.append('            delete slide i of thisDoc')
        out.append('        end repeat')
    out.append('        delay 0.5')

    # After deletion: slide 1 = title template, slide 2 = identity template.
    # Update the title slide text.
    t1 = to_applescript_string(TITLE_SLIDE_TITLE)
    b1 = to_applescript_string(TITLE_SLIDE_BODY)
    n1 = to_applescript_string(TITLE_SLIDE_NOTES)
    out.append('        tell slide 1 of thisDoc')
    out.append('            try')
    out.append(f'                set object text of default title item to {t1}')
    out.append('            end try')
    out.append('            try')
    out.append(f'                set object text of default body item to {b1}')
    out.append('            end try')
    out.append(f'            set presenter notes to {n1}')
    out.append('        end tell')

    # Update the identity slide text (currently at slide 2; will move to end).
    t_id = to_applescript_string(IDENTITY_SLIDE_TITLE)
    b_id = to_applescript_string(IDENTITY_SLIDE_BODY)
    n_id = to_applescript_string(IDENTITY_SLIDE_NOTES)
    out.append('        tell slide 2 of thisDoc')
    out.append('            try')
    out.append(f'                set object text of default title item to {t_id}')
    out.append('            end try')
    out.append('            try')
    out.append(f'                set object text of default body item to {b_id}')
    out.append('            end try')
    out.append(f'            set presenter notes to {n_id}')
    out.append('        end tell')

    # Insert content slides at the END.
    out.append('        -- Insert content slides at end of deck')
    for title, body, notes, master in SLIDES:
        effective_body = body
        if not body and master in BODY_VIA_TITLE_MASTERS:
            effective_body = title

        t = to_applescript_string(title)
        b = to_applescript_string(effective_body)
        n = to_applescript_string(notes)
        m = to_applescript_string(master)
        out.append(
            f'        set newSlide to make new slide at end of slides of thisDoc '
            f'with properties {{base slide:slide layout {m} of thisDoc}}'
        )
        out.append('        tell newSlide')
        out.append('            try')
        out.append(f'                set object text of default title item to {t}')
        out.append('            end try')
        if effective_body:
            out.append('            try')
            out.append(f'                set object text of default body item to {b}')
            out.append('            end try')
        if notes:
            out.append('            try')
            out.append(f'                set presenter notes to {n}')
            out.append('            end try')
        out.append('        end tell')

    # Move identity slide (currently at slide 2) to the end.
    out.append('        -- Move identity slide from position 2 to the end')
    out.append(
        '        move slide 2 of thisDoc to after slide (count of slides of thisDoc) of thisDoc'
    )
    out.append('        save thisDoc')
    out.append('    end tell')
    out.append('    return "OK: " & targetPath')
    out.append('end run')
    return "\n".join(out) + "\n"


def main() -> None:
    if not REFERENCE_DECK.exists():
        raise SystemExit(f"Reference deck not found: {REFERENCE_DECK}")

    print(f"Copying reference deck → {TARGET_DECK} …")
    subprocess.run(["cp", "-R", str(REFERENCE_DECK), str(TARGET_DECK)], check=True)

    script_path = Path("/tmp/build_keynote_deck.applescript")
    script_path.write_text(build_applescript(), encoding="utf-8")
    print(f"AppleScript: {script_path} ({script_path.stat().st_size} bytes)")

    result = subprocess.run(
        ["osascript", str(script_path)],
        capture_output=True,
        text=True,
        timeout=600,
    )
    print("--- stdout ---")
    print(result.stdout)
    if result.stderr:
        print("--- stderr ---")
        print(result.stderr)
    print(f"exit: {result.returncode}")


if __name__ == "__main__":
    main()
