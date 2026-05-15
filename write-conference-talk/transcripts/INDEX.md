# Conference talk transcripts — corpus index

Two source types in this corpus:

1. **YouTube transcripts** — auto-extracted via `youtube-transcript-api`.
   Captions are machine-generated unless noted; expect occasional
   technical-term garbling (e.g. "PyTorch" → "pie torch") but the prose flow
   and Jim's verbal patterns are preserved. Source pages:
   [jimbobbennett.dev/conferences](https://jimbobbennett.dev/conferences/).
2. **Keynote decks** — extracted from `.key` files on Jim's Desktop using an
   AppleScript that pulls each slide's title, body, and presenter notes. The
   notes contain the spoken narration (in written form). No timestamps. Files
   tagged `-keynote.md`. Where a deck and a transcript cover the same talk,
   each file's frontmatter has a `paired_transcripts` / `paired_decks` field
   pointing to the partner.

## Corpus — YouTube transcripts (14)

Ordered newest → oldest. The relevance column flags how useful each talk is
for modelling style for the upcoming AI/agents/context-graphs talk.

| Year | Conference | Talk | Length | File | Paired deck | Relevance |
|---|---|---|---|---|---|---|
| 2025 | AI Engineer World's Fair | Taming Rogue AI Agents with Observability-Driven Evaluation | 16m | `2025-ai-engineer-worlds-fair-xJXm4Wcw4m8.md` | `2026-evaluation-driven-development-keynote.md`, `2025-galileo-stop-doing-dumb-things-keynote.md` | ★★★ same topic |
| 2025 | NDC London | Prove going for a walk makes you more productive by measuring CO2 with an IoT device | 55m | `2025-ndc-london-upEgSfqDTIg.md` | `2025-co2-measurement-keynote.md` | ★★ recent, demo-heavy |
| 2024 | dotnetconf | The force is strong in LLMs (Star Wars copilot in .NET) | 24m | `2024-dotnetconf-orYbN8990dA.md` | — | ★★ recent, AI topic |
| 2024 | All Things Open | The force is strong in LLMs (Star Wars copilot, Pieces OS) | (longer cut) | `2024-all-things-open-A-SZWJ-Ye7Q.md` | — | ★★ same talk, longer slot |
| 2024 | apidays New York | Build a terrible API for people you hate | 18m | `2024-apidays-ny-zAOaynEQGbs.md` | `2024-terrible-api-keynote-mar.md`, `2024-terrible-api-keynote-may.md`, `2024-terrible-api-keynote-jun.md` | ★ recent, comedic opener |
| 2024 | Nordic APIs Austin | Build a Terrible API for People You Hate | 18m | `2024-nordicapis-austin-1-h6JUdMrraCk.md` | (same 3 decks above) | ★ same talk, different venue |
| 2024 | Nordic APIs Austin | From APIs to SDKs (developer experience) | (similar) | `2024-nordicapis-austin-2-DfK5a8b79K0.md` | `2024-from-apis-to-sdks-keynote.md`, `2024-3-steps-generate-sdk-keynote.md` | ★ recent, technical-pitch shape |
| 2023 | APIWorld | From APIs to SDKs — automated SDK generation | 26m | `2023-api-world-kKOu_4TYHII.md` | `2024-from-apis-to-sdks-keynote.md`, `2024-3-steps-generate-sdk-keynote.md` | ★ same talk, different venue |
| 2022 | Edge Impulse Imagine | Day 3 (Jim hosting, multi-speaker) | ~6h | `2022-edge-impulse-imagine-AP5ZWreMhC8.md` | — | ✗ skip (multi-speaker stream; transcript has many voices) |
| 2021 | YES Digital | Introduction to IoT using Azure IoT services | 75m | `2021-yes-iot-j-TukPd42ro.md` | — | ★ longer slot, tutorial shape |
| 2020 | Microsoft Build | Recognizing speech with a few lines of Python (COM207) | 30m | `2020-msbuild-speech-h6xbpMPSGEA.md` | — | ★ technical Python talk |
| 2020 | Microsoft Build | Prototyping smart-home device with Azure IoT hub (THR2020) | 20m | `2020-msbuild-iot-smarthome-Dr_nva7q90Q.md` | — | ✗ ALL-CAPS captions; usable but messy |
| (?) | NDC | Build cross-platform mobile apps using Fabulous | 56m | `ndc-fabulous-Hm4EDPNXQqY.md` | possibly `2017-xamarin-mvvm-keynote.md` (different era) | ★ longer slot, tutorial shape |
| (?) | NDC | How thanking people can lead to a better culture | 56m | `ndc-thanks-5hjpxa52PPc.md` | — | ★ non-tech soft-skills talk; useful range signal |

## Corpus — Keynote decks (12)

Source: `.key` files on Jim's Desktop. Extracted via
`osascript /tmp/extract_keynote.applescript`. Each section captures slide
title + body + presenter notes. No timestamps. The notes are the spoken
narration in written form — usually tighter and more telegraphic than the
spoken delivery.

Ordered newest → oldest by deck modification date.

| Year | File | Talk | Slides | Paired transcript | Notes |
|---|---|---|---|---|---|
| 2026-03 | `2026-evaluation-driven-development-keynote.md` | Evaluation-Driven Development of AI apps | 41 | `2025-ai-engineer-worlds-fair-xJXm4Wcw4m8.md` | Same thesis as AI Engineer 2025 ("Taming Rogue AI Agents"). Longer-slot evolution — could be the canonical deck the AI Engineer talk was cut from. |
| 2025-11 | `2025-galileo-stop-doing-dumb-things-keynote.md` | Stop doing dumb things with AI (Galileo demo) | 31 | `2025-ai-engineer-worlds-fair-xJXm4Wcw4m8.md` | Galileo.ai-branded variant of the EDD talk. Opens with the Pakistan Dawn newspaper hallucination story (vs Chicago Sun-Times at AI Engineer). Most recent AI talk in the corpus. |
| 2025 (?) | `2025-prompt-learning-keynote.md` | Prompt Learning — optimize your coding agent against your own codebase | ~37 | — | Closest structural twin of the context-graphs talk. Hand-raise hook → claude.md as the lever → SWE-bench result → "your git history is your ground truth" → overfitting-is-fine → works-for-any-agent → demo → CTA. Use as the primary structural template. |
| 2025-01 | `2025-co2-measurement-keynote.md` | Prove going for a walk makes you more productive by measuring CO2 with an IoT device | 35 | `2025-ndc-london-upEgSfqDTIg.md` | Source deck for the NDC London 2025 talk. Read alongside the 55-minute transcript to see how Jim expands tight notes into spoken delivery. |
| 2024-06 | `2024-terrible-api-keynote-jun.md` | Build A Terrible API For People You Hate (long form) | 64 | `2024-apidays-ny-zAOaynEQGbs.md`, `2024-nordicapis-austin-1-h6JUdMrraCk.md` | Longest version of the deck. Likely the form delivered at Nordic APIs Austin or a later venue. |
| 2024-05 | `2024-terrible-api-keynote-may.md` | Build A Terrible API For People You Hate (May draft) | 30 | (same as above) | Likely the version delivered at apidays NY (May 2024). 6 steps — dropped the consistency step that v1 had. |
| 2024-03 | `2024-terrible-api-keynote-mar.md` | Build A Terrible API For People You Hate (earliest draft) | 36 | (same as above) | Earliest preserved draft on disk. 7 steps. |
| 2024-03 | `2024-from-apis-to-sdks-keynote.md` | From APIs to SDKs — elevating Developer Experience with automated SDK generation | 41 | `2023-api-world-kKOu_4TYHII.md`, `2024-nordicapis-austin-2-DfK5a8b79K0.md` | Source deck for APIWorld 2023 and Nordic APIs Austin 2024 SDK talks. Voice-vote opener ("API folks — you are wrong") and the math-it-out scaling argument (10 microservices × 10 teams = 100 wrappers). |
| 2024-03 | `2024-3-steps-generate-sdk-keynote.md` | 3 Quick Steps to Generate SDKs for Your APIs | 8 | `2023-api-world-kKOu_4TYHII.md`, `2024-nordicapis-austin-2-DfK5a8b79K0.md` | Lightning-talk variant of the SDK pitch (8 slides). |
| 2017-02 | `2017-xamarin-mvvm-keynote.md` | Cross-platform Xamarin apps with MVVM | 32 | — | Jim at EROAD era. No paired transcript. 2017 voice baseline. |
| 2016-09 | `2016-ibeacon-eddystone-keynote.md` | Clicking on the real world with iBeacon and Eddystone | 13 | — | Pre-AI, EROAD era. Useful for style-drift signal — earlier, more written, less hand-raise-trap. |
| 2016-09 | `2016-xamarin-uitest-keynote.md` | Xamarin UITest in the real world | 12 | — | Co-presented with a colleague (Andrew). Telegraphic notes; 2016 voice baseline. |

## Exclusions

- `vQqIXKU98LI` Xamarin Evolve 2016 "All Things Mobile" — multi-person interview (Christina + Jim + Miguel + Simina + Thomas). Excluded per user instruction.
- `_N2mHFgshOU` Microsoft Build 2018 "All Things Mobile" panel — Channel 9 Build Live panel with Christina Warren. Also titled "All Things Mobile" per YouTube. Excluded under the same rule.

## Style-analysis priority

For the AI/agents/context-graphs talk we're writing, the highest-priority subset:

1. **Prompt Learning deck (2025).** Closest structural twin to the context-graphs talk: hand-raise hook ("Who used to actually write code by hand?") → "how did we enforce standards" → claude.md / system-prompt as the lever → real-world experiment with measurable result → "your project has its own ground truth (git history / Vera overrides)" → overfitting-is-fine acceptance → "works for any agent" generalization → demo → CTA. Same prompt-as-config thesis. **Primary structural template.**
2. **AI Engineer 2025 — Taming Rogue AI Agents** + paired decks (`2026-evaluation-driven-development-keynote.md`, `2025-galileo-stop-doing-dumb-things-keynote.md`). Same EDD/evals thesis as #1 from a different angle (Arrange-Act-Evaluate-Assert). The Galileo deck is the most recent AI talk and shows current 2025-2026 voice. **Delivery style baseline** — read the transcript for spoken rhythm and the decks for the tight written notes Jim writes for himself.
3. **NDC London 2025 — CO2 IoT** + paired deck (`2025-co2-measurement-keynote.md`). Demo-heavy, full 55-minute slot. Useful for longer-form pacing and demo handling. Side-by-side comparison: see how 35 slides of tight notes expand to 55 minutes of spoken talk.
4. **From APIs to SDKs** + paired decks. Technical-pitch shape, parallels how a context-graphs talk would justify "do it this way" — the math-it-out scaling argument is the structural ancestor of the SWE-bench numbers in the Prompt Learning deck.
5. **Terrible API talks (3 deck drafts + 2 transcripts).** Comedic opener pattern, audience-question move ("Who has worked with someone they hated?"). Three deck drafts show how Jim iterates the same talk over a 3-month window — useful signal for how patterns stabilize.
6. **dotnetconf 2024 — Star Wars copilot in .NET.** AI talk in Jim's 2024 voice; tighter 24m format. No deck pairing.

If time is tight, items 1-3 cover the patterns we need.

## Known caveats

- **Auto-captions** garble brand names and acronyms. Jim's "Galileo" / "Arize" / "Pieces OS" / "LangChain" / "Fabulous" often come through as something close-but-wrong. Flag and fix manually when extracting quotes.
- **The Edge Impulse stream** is the full Day 3 broadcast; Jim's segments are interspersed with other speakers. Identifying his specific portions would require timestamp-matching against the event programme. Not worth the effort for style analysis — the other 13 transcripts are cleaner and cover the same range.
- **The Dr_nva7q90Q smart-home talk** captions are ALL CAPS for the whole transcript (some YouTube auto-caption oddity). Content is fine, but quoting from it directly needs case correction.
- **Two talks at NDC don't carry a year on Jim's conferences page.** YouTube metadata also doesn't expose upload dates via oEmbed. Best guesses: the Fabulous talk pre-dates the YES Digital IoT talk (~2018-2020), and the Thanks talk is from a similar era.
- **Deck-vs-transcript divergence.** The decks contain presenter notes written for Jim to read; the YouTube transcripts capture what he actually said live. The two often diverge significantly — Jim improvises, swaps stories for newer ones, drops sections under time pressure, and adds audience-reactive content (e.g. "you're bad people"). For voice modelling, weight the transcripts more heavily; for thesis modelling, the decks are the canonical source.
- **The "All Things Mobile" name collision.** Two unrelated multi-speaker panels share this title; both are excluded.
