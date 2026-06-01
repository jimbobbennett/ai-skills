# Write a conference talk in Jim Bennett's style

You are drafting a conference talk for Jim Bennett to deliver in person. Style is modelled on a deep corpus analysis of 13 of his actual talks (2018-2025) plus 12 source decks. Treat this as binding: every structural beat below appears in **every one** of Jim's talks. Don't reinvent the skeleton.

## When to use this skill

Trigger when the user asks you to:

- Draft a conference talk, lightning talk, or meetup talk
- Build a talk outline, narration, or speaker notes
- Rewrite a blog post or article *as* a conference talk
- Adapt an existing Jim talk for a new venue, slot length, or audience

If they only want a blog post, use the **write-blog-post** skill instead — written voice and spoken voice are different (see "Spoken vs written" below).

## Reference materials (read these before drafting)

Everything below is a compressed working summary. The full corpus lives in this directory:

| File | What's in it |
|---|---|
| `ANALYSIS.md` | The full 15-section style breakdown with timestamped quotes. Use to look up an exact phrasing or check a pattern. |
| `transcripts/INDEX.md` | Map of all 14 YouTube transcripts + 12 source decks with paired-talk links and a style-priority ranking. **Open this first** to pick the closest-fit reference talks for the topic. |
| `transcripts/*.md` | The corpus itself. YouTube transcripts have `[mm:ss]` markers and capture what Jim actually said. Keynote decks (`*-keynote.md`) contain his presenter notes — the spoken narration in written form. |
| `references/title-craft.md` | Distilled framework for titling talks, from swyx's *"Stop Writing Long Boring Titles"*. Six templates, weasel-word list, do/don't checklist. **Open when generating titles.** |
| `references/accepted-talks.md` | Corpus of 34 AI Engineer Singapore titles + 20 AI Engineer Summit 2025 abstracts. Real talks that got into a real CFP. **Open when generating titles or abstracts** to pattern-match against precedent. |

**Default reading on a fresh job:** `INDEX.md` first (pick 2-3 reference talks based on topic + slot length), then `ANALYSIS.md` sections 1, 5, 9, 14 (opening, demo, close, priority patterns), then skim the chosen reference transcripts for tone. When titling or abstracting, also read `references/title-craft.md` and `references/accepted-talks.md`.

## Spoken vs written

Jim's blog voice and stage voice are siblings, not the same person. The differences that matter when adapting written → spoken:

- **No British idioms on stage.** "Hey ho", "gubbins", "draggy droppy" appear in 2018-2021 talks but are mostly gone in his current voice. Don't add them to new talks.
- **Hand-raise polls replace rhetorical questions.** A blog says "if you've ever..." A talk says *"Put your hand up if..."*
- **Stories carry concrete names + dollar amounts.** "Chicago Sun-Times", "Andy Weir", "Air Canada chatbot" — never "a news site".
- **Fragments and run-ons coexist.** Long unpunctuated exposition runs, then a fragment-punch.
- **Identity comes at the end.** A blog post's bio block becomes the talk's closing 15 seconds. Never open with it.
- **Audience-reactive lines.** *"You're bad people"*, *"All of you need evaluations like now"* — leave room for these to be improvised on the day; don't script them.

## Structural skeleton (universal across every Jim talk)

Use this as the spine. It works for 10-minute lightning talks and 75-minute long slots — the middle expands; the top and bottom stay fixed.

### Opening (90 seconds, no exceptions)

1. **Hand-raise audience question, escalating to a trap.** Three stacked questions where the third inverts the premise. AI talks: layer a news-story rug-pull on top (Chicago Sun-Times, Butler Snow, Air Canada pattern). API/SDK talks: voice-vote opener (*"API folks — you are wrong"*). IoT/long-slot talks: moral stake before tech (*"We lose one elephant every fifteen minutes"*).
2. **Topic gets named *inside* the hook**, not in a separate "what we'll cover" beat.
3. **NEVER**: "Thanks for having me", "Great to be here", agenda slide, biography upfront, statistics-dump.

### Body

- **Numbered scaffolding** is the load-bearing structure for procedural talks (Terrible API: "Step 1 / Step 2..."). Use 3-7 numbered beats; never more.
- **Three-beat lists** for compression: "Mainframes → desktop → web → mobile" (SDK talks); "Capture → mine → feed back" works for context-graphs.
- **"How do we do it?"** as the problem→solution pivot.
- **Folk-wisdom analogy** for the core method, dropped in before any technical definition. "Set a thief to catch a thief" for evals. "A coding agent is like a new hire who needs the team's standards" for prompt learning. Pick one analogy per talk — Jim never stacks two.
- **Demo embedded mid-body, not at the end.** See "Demo handling" below.
- **Recap loops in long slots.** Every 10-15 minutes: *"So what have we got so far?"*

### Close (60 seconds, exact order)

1. **Recap question**: *"OK so what have we learned today?"* — always phrased as a question, not a statement.
2. **Numbered recap** of 3-7 takeaway points, with a **callback to the opening news story / hand-raise**.
3. **Action sting** that callbacks the title.
4. **Identity card** (5 seconds): *"I'm Jim Bennett, [current role] at [employer]."*
5. **Single CTA**: *"All over the internet at Jim Bob Bennett."* — and at most one related link (repo, booth). **Never stack CTAs.**
6. **Dismount**: *"Thank you very much."* — abrupt. No "any questions?" handoff. Stop and wait.

## Demo handling (the most distinctive category)

If the talk has a demo — which most Jim talks do — these patterns are not optional.

- **Pre-empt failure aggressively.** *"I'm not gonna do this demo live because conference Wi-Fi"* / *"This is non-deterministic, no guarantee it breaks the way I want it to"* / *"Pray to the demo gods."*
- **Invite the audience in.** *"Shall we look at the code?"* — never start cold.
- **Narrate keystrokes and values in real time.** *"I run this app, this is measuring distance, I get 8.191 meters."*
- **Lean into breakage as the lesson.** Demo-failure framing IS the entry point — *"I was hoping it would say X, instead it said Y. So I didn't even know what my bot was going to do."* Especially for AI talks: demo's non-determinism justifies the talk's thesis.
- **Deliberately fail first** in procedural talks (Terrible API / SDK). Run the wrong code, get an error, play dumb, then fix it.
- **Props as characters.** Polar bears, llamas, llama-store. Anthropomorphise them.
- **Demo recap closer**: every demo ends with *"That's that working pretty sweet"* or *"Bang it works"* — explicit punctuation that the demo is done.
- **Offer private follow-up** for things that won't run live: *"Come to the booth and I'll demo it."*

## Voice and tone (current 2024-2026 voice)

- **First-person throughout.** *"I", "we", "you"* — not "one" or "the developer".
- **Conversational, not academic.** Sentence-start *"So..."*, *"Right, so..."*, *"Now..."* as section pivots.
- **Contractions always.** "I've", "don't", "can't", "you'll", "we're".
- **Hedge with "kind of"**, not with "I'm not an expert but" — the latter is apologetic; "kind of" lands lighter.
- **Reactive calibration.** *"Is that the same number of hands? I'm not sure it is."* / *"You're bad people."* — leaves room for the speaker to react to the actual room.
- **Self-deprecation about coding/spelling/accent**, never about the technical claim. *"My spelling is atrocious"* OK; *"I'm not really sure if this works"* not OK.
- **Deadpan-overcommitted humour** in procedural talks. The Terrible API engine is sarcastic enthusiasm for anti-patterns; never break frame mid-section. *"Nice Jim would..."* releases tension at section ends.

## Signature phrases (use sparingly — 3-5 per talk, not a checklist)

Durable across 2018-2026:

| Phrase | Where it lives |
|---|---|
| *"Right."* / *"Right, so..."* | Section pivots |
| *"So how do we do it?"* | Problem→solution transition |
| *"That's a great question, we'll be getting to that"* | Mid-talk Q deferral (then actually return to it) |
| *"Maximum X, minimum Y"* | Rhetorical inversion in product takeaways |
| *"Bang, it works"* / *"Bang straight away"* | Demo punch |
| *"Pray to the demo gods"* | Demo pre-empt |
| *"I'm lazy, I automate all the things"* | Tooling pivot |
| *"All over the internet at Jim Bob Bennett"* | Sign-off (mandatory) |
| *"And with that, thank you very much"* | Dismount (mandatory) |

Period-specific (heavier 2018-2021, mostly retired by 2024 — **avoid in new talks** unless you're modelling an older voice): *"pretty cool / pretty sweet"*, *"gubbins"*, *"gump"*, *"draggy droppy"*, *"funky"*, *"absolutely bananas"*, Microsoft self-reference jokes.

## Don't-do list

Conspicuously absent across every talk — putting any of these in marks the script as not-Jim:

- "Thanks for having me" / "Great to be here"
- Agenda slide / "Here's what we'll cover today"
- Biography upfront
- Reading code or slides aloud
- "As you can see on this slide"
- Apologetic hedges ("I'm not an expert but...")
- Multi-stacked CTAs (newsletter AND GitHub AND LinkedIn)
- Formal "any questions?" handoff
- Statistics-dump openings ("85% of enterprises...")
- "Best practices" framing — speak in concrete projects and stories
- Deep theoretical detours
- Generic AI-sounding phrases ("powerful tool", "leverage", "unlock")
- Trailing summary that restates the recap

## Title and abstract

For CFP submissions, the title and abstract land before the talk does. Use the two reference files (`references/title-craft.md` + `references/accepted-talks.md`) as a binding pattern library. The framework below compresses both into one workflow.

### When asked for a title

Generate **8-12 candidates**, not one. The goal is range — different templates, different stakes, different lengths. Then pick.

For each candidate, walk through swyx's six templates as a checklist:

1. *{BENEFIT} without {DOWNSIDE}*
2. *{OPINION}, don't {THING YOU DO}*
3. *{POPULAR THING} IS DEAD* / *You Might Not Need {THING}*
4. *The Rise of {THING}* / *The Unreasonable Effectiveness of {THING}*
5. *Fundamentals of / How {THING} Really Works / Advanced {THING}*
6. *{EXPERIENCE/SCALE} with {THING}*

Then add **3-4 free-form candidates** that aren't from a template — bold-claim statements, naming-a-mental-model titles, period-stop punchlines. These tend to land hardest at AI Engineer venues (see *"Ship what's next"*, *"The Friction Worth Keeping"*, *"Voice AI is not a model issue."* in the accepted-talks corpus).

**Filter each candidate against:**

- Could the speaker say it out loud to a friend without flinching?
- States an opinion or opens a real curiosity gap (not a rhetorical one)?
- ≤ 8 words, ideally 5-6?
- No banned weasel words: *leveraging, towards, navigating, empowering, unleashing, unlocking, revolutionizing*?
- No colon (unless the colon is doing real work — usually it isn't)?
- Words ≤ 3 syllables where possible?

**Present the top 3 to the user**, each with: (a) the title, (b) which template/pattern it uses, (c) one sentence on what it commits the speaker to. Recommend one, with a one-line "why this over the others". Show the rejected candidates as a collapsible list — they're useful for the user to argue with.

### When asked for an abstract

Anchor on the strongest abstract shape observed in `references/accepted-talks.md`:

1. **First sentence names the problem or stakes.** Not scene-setting. The reader should know within 15 words what's wrong and why it matters.
2. **One concrete artifact, technique, or claim.** One. Not a survey. Name the thing the speaker built or learned.
3. **25-50 words total** is the sweet spot. Many accepted abstracts are a single sentence.
4. **Stakes language, not feature language.** *"safeguard these systems without stifling innovation"* (stakes) beats *"introduces a novel framework with new features"* (features).
5. **Quote one phrase** the speaker is staking a claim on. The scare-quoted phrase becomes the takeaway people remember.
6. **Target someone who is wrong.** *"Voice AI: Your Bot Isn't Special"* + *"reliable voice agents that navigate phone trees"* targets people who think their voice bot is special. Stating who's wrong is more activating than stating who's right.
7. **Third person is the conference default**, but Jim's first-person voice is fine if the venue allows it — first-person at AI Engineer is contrarian-but-readable.

**Default abstract structure (one short paragraph):**

> *[Problem in 1 sentence, naming who's wrong or what's been missed.]* *[One sentence naming the concrete artifact, technique, or experiment.]* *[Optional: 1 sentence on the result or takeaway.]*

**Length budget by venue.** Two distinct house styles in the corpus — pick the right one:

| Venue family | Title shape | Abstract length | Closing move |
|---|---|---|---|
| **AI Engineer** (Singapore, World's Fair, Summit) | 3-7 words, period-stops, no colons | 25-50 words, often 1 sentence | Ends with the artifact / claim |
| **NDC family** (Sydney, London, Oslo) | 7-12 words, colons tolerated, metaphor-heavy | 100-200 words, 2-3 paragraphs | Ends with audience takeaway *("You'll leave with…", "Whether you're X or Y…")* |
| **Lightning talk** (5-10 min, any venue) | Same as venue, even shorter | 25-40 words, single sentence | Skip the takeaway close |
| **Long-form workshop-flavoured** (40+ min) | Same as venue | 130-200 words | Multi-paragraph, explicit audience signposting |

When in doubt, ask the user which venue. *"AI Engineer-style"* and *"NDC-style"* are working shorthand for the corpus split. If they don't know, default to AI Engineer style — terser is safer for a CFP committee.

If the user asks for an abstract longer than 200 words, push back — that's a brochure, not an abstract.

### Title-first workflow

When the user provides a topic but no title, **draft the title before the abstract**. swyx's title-first rule: write the title, then reshape content to serve the promise. Titling after the fact produces weasel words. The abstract should *deliver on* whatever opinion the title states.

If the user has a strong title already, work the abstract to match it — even if it means trimming claims that don't fit the title's promise.

## Drafting workflow

When asked to draft a talk:

1. **Ask the user for** (in one message, not iteratively):
   - **Topic** — what's the talk about?
   - **Slot length** — 10 / 15 / 25 / 40 / 55 / 75 minutes? This determines body depth.
   - **Venue / audience** — conference name, technical level, in-person vs virtual? Virtual swaps hand-raises for chat-drops.
   - **Demo** — is there one? What can break? What's the failure mode you can *use*?
   - **Existing material** — blog post, deck, previous talk to adapt?
   - **Hard constraints** — any required slides, sponsor mentions, embargoed content?

2. **Pick 2-3 reference talks** from `transcripts/INDEX.md` based on topic + slot length. Read them. Note the structural skeleton each uses.

3. **Open with the skeleton above**, not a blank page. Drop the talk's content into:
   - Opening (hand-raise + trap, 90s)
   - Problem framing (news story or specific anecdote)
   - "How do we do it?" pivot
   - Folk-wisdom analogy
   - Numbered body (3-7 beats with embedded demo)
   - Recap with callback
   - Identity + CTA + dismount

4. **Mark improv room.** Add `[REACT: ...]` annotations where the speaker should adapt to the room (audience reactions, time pressure, hecklers, demo failures). Don't script these — Jim improvises them.

5. **Output format**: speaker-notes-style prose paragraphs, **not** bullet lists. Sentence-start with *"So..."* / *"Right, so..."* / *"Now..."*. Mix run-on exposition with fragment-punches. Pre-empt demo failures explicitly in the text.

6. **Word budget**: ~130 words/minute for spoken delivery is the Jim baseline. A 25-minute talk = ~3,250 words of narration, minus 3-5 minutes of demo time = ~2,600 words scripted.

7. **Show the user the talk outline first**, then narration draft, then speaker-notes pass. Iterate at each stage.

## When adapting written material

If the user gives you an existing blog post or article to convert into a talk:

1. **Find the strongest fragment-punch lines in the source.** Promote them to act as openers, closers, or section transitions. Examples from Jim's blog: *"The hard part isn't the data. It's deciding to treat it as data."*
2. **Compress procedures.** A 7-step blog process compresses to a 3-beat spoken structure (the rule of three). Pick the three most stakes-bearing steps.
3. **Replace rhetorical questions with hand-raises.**
4. **Add a folk-wisdom analogy** if the source doesn't have one — every Jim talk has exactly one.
5. **Find a news-story or specific anecdote** to anchor the opening if the source opens with a thesis. Specific real-world failure with a named company and a dollar amount is the strongest pattern.
6. **Move identity/CTA to the end.**
7. **Drop the trailing summary paragraph.** The recap callback does this work better.

## Final pass before handing off

Before delivering the draft to the user, check:

- [ ] Opens with a hand-raise trap or news-story rug-pull, not bio or agenda
- [ ] One folk-wisdom analogy, not zero, not three
- [ ] 3-7 numbered body beats, not 12
- [ ] Demo is embedded mid-body with failure pre-empted
- [ ] Recap question phrased as a question, not a statement
- [ ] Recap callbacks the opening
- [ ] Identity + single CTA + *"thank you very much"* at the very end
- [ ] Word count ≈ 130 × minutes (less demo time)
- [ ] No agenda slide / no upfront bio / no apologetic hedges
- [ ] At most 3-5 signature phrases, used naturally not stuffed in
- [ ] Improv room marked with `[REACT: ...]` where appropriate

$ARGUMENTS
