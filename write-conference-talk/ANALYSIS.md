# Jim Bennett conference-talk style — consolidated analysis

Synthesis of three parallel deep-reads across 13 conference talks (2018-2025).
Excluded: the Edge Impulse 2022 multi-speaker stream and two "All Things Mobile"
panels. Self-care intros (audience stretch/breathe segments) excluded from
analysis per user instruction.

Citations use `[talk:HH:MM]` where talk is one of: **AIE25** (AI Engineer 2025),
**NDC25** (NDC London 2025), **DNC24** (dotnetconf 2024), **ATO24** (All Things
Open 2024), **APN24** / **NORD24a** (apidays NY / Nordic Austin — Terrible API),
**NORD24b** / **APIW23** (Nordic / APIWorld — APIs to SDKs), **YES21** (YES
Digital 2021 IoT), **MSB20s** (MS Build 2020 speech), **MSB20i** (MS Build 2020
smart-home), **FAB** (NDC Fabulous), **THANKS** (NDC Thanks).

---

## 1. Hook / opening (skip self-care)

**Workhorse: stacked hand-raise audience questions, escalating to a trap.**

The trap is the move. He asks something the audience will answer one way, then
flips it. Examples:

- **AIE25 [00:11]**: *"Who uses AI? Is that Jim's stupid most stupid question of
  the day? Probably. Who trusts AI? Right. If you'd like to meet me after, I've
  got some snake oil you might be interested in buying."*
- **AIE25 [02:39]**: *"Who's a coder? Who writes code? Okay. Who writes unit
  tests? Is that the same number of hands? I'm not sure it is. You're bad
  people."*
- **NORD24a [00:08]**: *"Who here has worked with someone they hated? Pretty
  much every single hand."*
- **NORD24b [00:08]**: *"Who here creates APIs put your hand up... who consumes
  APIs... team API put your hand up team SDK put your hand up. Right, I actually
  don't need to give this talk anymore. See you later, you've all given me the
  right answer."*

**Variants by talk type:**

- **AI/agents talks**: hand-raise + news-story rug-pull (Chicago Sun-Times,
  Butler Snow, Air Canada).
- **API/SDK talks**: hand-raise question funnel (3 stacked questions).
- **IoT/long-slot talks** (2018-2021): moral-stake hook before tech ("we lose
  one elephant every 15 minutes" YES21 [00:00]; "broke both arms skiing" speech
  control MSB20s [15:06]).
- **Star Wars / pop-culture talks**: "who likes the original trilogy" hand-raise
  segue.

**Common to all hooks:**

- No "thanks for having me," no agenda slide, no biography upfront.
- Bio comes at the **end**, with the CTA. Universal pattern.
- Topic gets named **within the hook**, not in a separate "what we'll cover" beat.

---

## 2. Signature phrases / verbal tics

Frequency-ranked, with examples and durability notes (durable = appears across
2018-2025; period = 2018-2021 only).

| Phrase | Durability | Examples |
|---|---|---|
| **"Right."** / **"Right, so…"** | durable | AIE25 [00:32]; NORD24b throughout; YES21 throughout |
| **"Yeah."** as punctuation | durable | every talk |
| **"kind of"** hedge | durable but heavier in older talks | FAB constant; AIE25 still present |
| **"Now…"** as topic pivot | durable | "Now, different question" AIE25 [00:32] |
| **"So…"** as connective | durable | every talk, most common section start |
| **"You know…"** filler | durable | very frequent in old talks; less in current |
| **"As we know…"** premise frame | durable | AIE25 [13:01]; ATO24 [03:08] |
| **"That's a great question, we'll be getting to that"** | durable | AIE25 [04:46]; YES21 multiple |
| **"Awesome"** / **"Cool"** single-word landing | durable | AIE25; ATO24 [10:03]; YES21 |
| **"Pretty cool" / "pretty sweet" / "really cool"** | period (heavier 2018-2021) | FAB 20+; YES21 [13:11] |
| **"Absolutely fantastic / bananas / amazing"** | period | MSB20s [13:31] *"absolutely bananas"* |
| **"Funky"** / **"gubbins"** / **"gump"** / **"draggy droppy"** | period Britishisms | FAB [44:17, 23:46, 24:18, 55:12 YES21] |
| **"All over the internet at Jim Bob Bennett"** | durable signature | every talk's sign-off |
| **"And with that, thank you"** | durable dismount | THANKS [12:10]; FAB [55:45] |
| **"Maximum X minimum Y"** rhetorical inversion | durable | "maximum developer experience minimum developer effort" NORD24b [18:33] |
| **"Bang it works"** / **"Bang straight away"** demo punch | durable | NORD24b [16:29]; APIW23 [04:11] |
| **"Pray to the demo gods"** | durable | NORD24b [12:46]; ATO24 [10:03] |
| **"Things like that"** filler closer | durable | every talk |
| **"All the things"** | durable | "I'm lazy I automate all the things" NORD24b [11:09] |

**Note on hedge density**: 2018-2021 talks have markedly more "kind of / yeah /
you know" per minute than 2024-2025. Current voice is tighter but the *patterns*
are the same — fewer instances per minute, not different vocabulary.

---

## 3. Section transitions / verbal signposts

- **"So…"** — most frequent. Starts most new beats.
- **"Now…"** as topic shift: *"Now, different question."* (AIE25 [00:32])
- **"Right, so…"** — declarative pivot.
- **"OK, so what have we learned today?"** — universal closing signpost,
  **always phrased as a question to the audience**. AIE25 [14:33]; DNC24 [22:22];
  ATO24 [38:21].
- **"Step N…"** / **"OK thing number N…"** — numbered structural skeleton in
  Terrible API talks (APN24, NORD24a). Used as visible scaffold.
- **"So how do we do it?"** / **"So how do we normally fix this as developers?"**
  — problem→solution pivot. AIE25 [03:42]; APIW23 [09:25].
- **"This is where X comes in."** — AIE25 [06:17] *"this is where evaluations
  comes in."*
- **"What about X?"** — rhetorical question to introduce next topic. YES21
  [41:09] *"What about connectivity? What about bandwidth?"*
- **"Now what's also cool is…"** — feature pivot, AIE25 [11:58].
- **"So what have we got so far?"** / **"What have we done?"** — explicit
  in-talk recap loops. MSB20i [17:50, 19:26].
- **"And so…"** — connective glue between beats.

---

## 4. Audience engagement moves

**Hand-raise polls** are the workhorse. Used to:

- Validate premises ("who has worked with someone they hated").
- Calibrate technical depth ("who's used OpenAPI? OK, we all know what that is").
- Set up co-conspirator framing ("who has started a job and found the team doesn't follow standards").
- Self-deprecating angles ("who here likes being mean to people? OK, a few hands — most of you are nice people, there's only a few of us who are mean" NORD24a [01:09]).

**Reactive calibration** — he counts the hands and reacts in real time:

- AIE25 [02:39]: *"Is that the same number of hands? I'm not sure it is. You're
  bad people."*
- AIE25 [08:53]: *"All of you need evaluations like now."*

**Trap questions** — set up both answers as right then drive the point:

- AIE25 [06:17]: *"Who thinks the whole AI chatbot worked? Who thinks it didn't
  work? More hands. Yes, you're right. It didn't work."*

**Plants for callbacks**:

- *"Any Brits in the room other than me? Yay."* (AIE25 [03:42])
- *"Who was here earlier watching JAM show all cool stuff?"* (MSB20i [18:21])

**Mid-talk question handling** is a load-bearing pattern:

- **"That's a great question, we'll be getting to that"** — defers without
  breaking flow. AIE25 [04:46], YES21 throughout.
- **Returns to the question later** with *"Going back to your question
  there…"* (AIE25 [08:22] returning to [04:46]).
- **Credits specific audience members**: *"Gentlemen at the back there very
  kindly managed to get me connected to an actual physical cable"* (AIE25
  [04:14]).

**Live-chat adaptation** (virtual talks, e.g. APIW23): replaces hand-raises
with *"drop something in the chat"* and calls out names: *"shiron Dabble… Vang
gives me a thumbs up Stefan thumbs up"* (APIW23 [00:31]).

**Venue jokes** are improv:

- *"My boss is over there"* — NORD24a [15:48], points across the room.
- *"You might see a llama wandering around"* — NORD24a [17:22], booth reference.
- *"Yes, this is Microsoft Build and I'm coding on a Mac"* — MSB20s [19:59].

---

## 5. Demo / code handling — **most distinctive category**

**Pre-empt failure aggressively.** Acknowledge demo gods early.

- *"I'm not gonna do this demo live because conference Wi-Fi. Have you all had
  fun with Wi-Fi? Yes."* (AIE25 [04:14])
- *"This is an AI application, there's no guarantee it's actually going to
  break the way I want it to break when I'm demoing it to you because it's
  non-deterministic."* (AIE25 [04:46])
- *"So pray to them, my God this is going to work."* (NORD24b [12:46])

**Invite the audience in.** Never just starts a demo cold.

- *"So instead of me talking about, shall we see it? See the code? Yes."*
  (MSB20i [05:19])
- *"Shall we do more demos? Yeah let's do it."* (MSB20i [12:34])

**Narrate keystrokes / values in real time.**

- *"So if I just run this app, this is measuring distance, give me a distance
  measured of 8.191 meters."* (YES21 [25:02])
- *"I start by creating a speech config. With these values of key and region…
  my language recognition of en-GB English."* (MSB20s [06:45])

**Lean into failure as the lesson.** The demo breaking IS the point.

- AIE25 [05:47]: *"I was hoping when I did this demo, it would come back and
  say 'You've got X amount of money.' Instead, it came back to say, 'Please
  could you let me know the name of your checking account.' So I didn't even
  know what my bot was going to do."* — demo not working becomes the entry
  point to evaluations.
- MSB20i [08:22] thumb-warming the temperature sensor: *"OBVIOUSLY BIT CHILLY
  IN HERE… I SHOULD HAVE HUGGED A CUP OF COFFEE BEFORE DOING THIS, SHOULDN'T
  I?… COME ON, WARM UP. OH. THE AIR QUALITY HAS HERE TOO GOOD."*
- MSB20s [05:11] daughter Evie's voice demo: *"things aren't always perfect.
  She spoke more this way. My speakers right microphone is more over that way"*
  — diagnoses on-mic without panicking.

**Deliberately fail first** in the Terrible API/SDK talks. The structural move:
run the wrong code, get an error, play dumb, then fix it.

- *"Failed, why did it fail, let's have a look what happened here."*
  (NORD24b [01:43])
- *"Bang straight away I get an error, this doesn't look like there's anything
  wrong with my code, there's no red squigglies."* (APIW23 [03:41])
- *"All this, this looks like me, I'm doing some dumb coding here. But really
  this is the kind of experience you get when you're working directly with an
  API."* (APIW23 [06:48])

**Props are characters.** Polar bear and lynx toys (YES21 [37:30]), pet store →
llama store (NORD24b/APIW23). He holds them up, anthropomorphises them, riffs.

**Demo recap closer.** Every demo ends with explicit summary.

- *"So that's my hardware. That's my device software. That's all working
  pretty sweet."* (MSB20i [08:53])
- *"Bang it works."* (NORD24b [16:29])

**Offers private follow-up for things that won't run live**: *"If you want to
come and see this in action, come to Galileo booth and I'll demo it."* (AIE25
[04:46])

---

## 6. Humour / self-deprecation

**Patterns by category:**

| Category | Examples |
|---|---|
| **Self-mockery** | *"Is that Jim's stupid most stupid question of the day? Probably."* (AIE25 [00:11]); *"I do horrible C code."* (MSB20i [13:09]); *"I'm a smart ass but that's not always true."* (FAB [05:45]); *"My spelling is atrocious."* (MSB20s [22:04]) |
| **British accent / identity** | *"In my very, very poor French."* (MSB20s [08:50]); *"This is an English hence my evil villain accent."* (MSB20s [02:05]); *"Sorry for speaking dollars, I've been in the US for the past five and a half years."* (NDC25 [35:18]) |
| **Mac-at-Microsoft-Build transgression** | *"Yes, this is at Microsoft Build and I'm coding on a Mac. I love Macs."* (MSB20s [19:59]) |
| **Donation jokes** | *"If anyone wants to donate, would appreciate that."* (AIE25 [05:16]); *"If you don't like making money, send it to me."* (AIE25 [08:22]) |
| **Political snark (sparingly)** | *"Score one against the prisons."* (AIE25 [02:00]); *"We use Fahrenheit, some nonsense."* (NDC25 [27:27]); *"I'm not on the Nazi platform."* (NDC25 [55:13]) |
| **Twitter-as-X jab** | *"Someone who will take over a social media company, fill it for the white supremacy, and lay off half the staff."* (APN24 [00:03]) — opener joke |
| **Pop-culture (Star Wars in copilot talks)** | Yoda inversions; "Order 66" as ecommerce conversation summary; "entire script of Return of the Jedi" as context-window example |
| **Self-deprecating opinion drops** | *"Pineapple is perfect on pizza"* (APIW23 [14:06]); *"I despise Commission-based sales"* (THANKS [05:25]) |
| **Classic dev jokes deployed exactly** | *"Four hard things in computer science. Naming things, cache invalidation, off-by-one errors. Yeah, someone got the joke. Cool."* (AIE25 [06:17]) |
| **Stack Overflow joke** | *"Control C, control V when you're copying and pasting code from Stack Overflow."* (YES21 [69:45]) |

**Tone**: deadpan-overcommitted. The Terrible API talk's whole comedic engine
is sarcastic enthusiasm for anti-patterns; he never breaks frame mid-section.
The "nice Jim wouldn't do this" pivot at section ends is what releases tension.

---

## 7. Stories / anecdotes

**The shape is consistent across all talks:**

1. Real specific detail (named company, specific timing, specific person).
2. Human consequence (someone fired, money lost, system broken).
3. Tech connection (this is what the talk's about).

**Examples by talk type:**

| Type | Story | Talk |
|---|---|---|
| **News story** | Chicago Sun-Times AI summer reading list hallucinated Andy Weir book | AIE25 [01:04] |
| **News story** | Butler Snow lawyers cited false case law for Alabama prisons | AIE25 [01:35] |
| **News story** | Air Canada chatbot refund legally binding | AIE25 [02:06] |
| **News story** | Lawyer fired for using AI in court (callback) | ATO24 [39:25] |
| **Personal anecdote** | Wife is elementary school teacher, 12-year-old brings germs home | NDC25 [11:09] |
| **Personal anecdote** | Broke both arms skiing → voice control | MSB20s [15:06]; YES21 [09:51] |
| **Personal anecdote** | Microsoft sends financial statements as screenshots embedded in Excel | APN24 [02:07] |
| **Personal anecdote** | Garage door / pacific-northwest heat dome / house lights | recurring in IoT talks |
| **Real-world hack** | Fish tank casino IoT hack | YES21 [28:10] |
| **Real-world disaster** | Ferrari bricked by update in parking garage | YES21 [42:42] |
| **Policy** | New Zealand fuel tax via vehicle tracking | YES21 [14:02] |
| **Banking horror** | Missing field → can't retry → DBA called weekend → contractors paid | APN24 [14:39]; NORD24a [12:40] — identical |
| **Workplace** | Helen the tester, invisible work, intervention, recognition | THANKS [10:36] |
| **Twitter survey** | "56% said SDKs; not scientific" — used twice, caveat always | NORD24b [07:01]; APIW23 [13:01] |
| **Self-evidence** | "I have seen this in the wild" framing | every Terrible API beat |

**Stories are short** (10-30 seconds), **never indulgent**, **always payload-bearing**.
He doesn't tell stories for atmosphere; they always carry a point.

---

## 8. Pacing rhythm

- **Continuous forward motion**, not dramatic silence. Long unpunctuated
  run-ons during exposition; short fragments during demos and punchlines.
- **Fragment-punch closers** after long setups:
  - *"Well, you can't. Doesn't exist."* (AIE25 [01:04])
  - *"Job done, no exceptions."* (APN24 [10:28])
  - *"That's what nice Jim would do."* (APN24 [15:42], section closer)
  - *"There we go. Fan comes on. Thank you very much."* (MSB20i [08:22])
- **Rule-of-three lists**, often ascending in stakes:
  - *"This is the thing that kills meetings… kills classrooms… kills the planet."*
    (NDC25 [04:18])
  - *"Mainframes then desktop then web then mobile."* (both SDK talks)
- **Repetition for emphasis (three-beat)**:
  - *"Did it work? Did it work? What do we think?"* (AIE25 [06:17])
  - *"Step one, add evaluations to your agent."* (AIE25 [14:33])
- **Whole-clause duplication** (older talks):
  - *"I want to know about it so I can celebrate with you when you build a cool
    project I want to know about it so I can celebrate with you."* (YES21
    [02:06])
- **Recap loops** in longer slots: every 10-15 minutes, *"So what have we got
  so far?"* lists the architecture stack covered.
- **Q&A as energy reset** in virtual/long talks (YES21).
- **Speeds up through technical middle, slows for jokes and audience moments.**

---

## 9. Closings

**Consistent structure across all talks**:

1. **Recap question**: *"OK so what have we learned today?"* or *"Let's wrap up
   and think what have we learned today?"* (AIE25 [14:33]; DNC24 [22:22])
2. **Numbered recap**: 3-7 takeaway points, often with callback to opening.
   AIE25 [14:33]: *"Step one, add evaluations to your agent… You do not want to
   be the next Chicago Sun-Times."* (callback to [01:04]).
3. **Action sting**: *"If your AI agent goes rogue, maybe you need to be woken
   up. So that is how you can tame AI agents with evaluations."* (AIE25
   [15:36]) — title callback.
4. **Identity card**: *"I'm Jim Bennett, I'm a principal developer advocate at
   [employer]."* — 5 seconds, late in the close, never up front.
5. **Single CTA**: *"All over the internet at Jim Bob Bennett."* — universal.
   Sometimes "come to the booth" / "find me on LinkedIn" variants.
6. **Dismount**: *"Thank you very much."* — abrupt. No formal "any questions?"
   transition. He stops and waits.

**Tactical closers, never grand.** No manifesto, no rallying cry. The strongest
line is usually mid-recap.

---

## 10. Don't-do list (conspicuously absent)

- No "thanks for having me" or "great to be here" openings.
- No agenda slide / "here's what we'll cover today."
- No "as you can see on this slide" — narrates around bullets, never recites.
- No reading code or slides aloud.
- No apologetic hedges ("I'm not an expert but…") — uses "kind of" softener
  instead, which lands lighter.
- No biography upfront — name and title come at the *end*, not the start.
- No long thanks-to-organisers segment.
- No multi-stacked CTA ("scan QR, sign up for newsletter, follow X AND Y") —
  always single CTA = his handle.
- No "any questions?" formal handoff — stops and waits.
- No corporate marketing despite each talk being effectively a company pitch —
  employer mention is one line, dropped in mid-talk or at the end.
- No statistics-dump openings ("85% of enterprises…").
- No "best practices" framing — speaks in concrete projects and stories.
- No deep theoretical detours.

---

## 11. AI/agents-specific framing (load-bearing for the new talk)

**Problem setup is always news-led, not theory-led.** Two recent (same-week)
news stories → "AI makes stuff up" → "detecting problems with AI is hard" →
"how do we do it?" → solution.

**Observability/evaluation framed as folk wisdom**:

- *"Set a thief to catch a thief"* — *"we can set an AI to verify an AI… AIs
  are not bad at this. They're about as good as a human."* (AIE25 [03:42])
- *"The best time to put evaluations in is as you're doing prompt engineering.
  The second best time is now."* (AIE25 [09:23]) — proverb-style, reused.

**Load-bearing words**:

- **"Non-deterministic"** — the word that separates AI from regular software.
  Returns to it repeatedly.
- **"Hallucination"** — paired with news examples, never abstract.
- **"Granularity"** — *"It's not just that binary did my agent work yes or no
  question. It's at what step in the process did my agent fail."* (AIE25
  [07:50])
- **"Human in the loop"** — *"As a human, I can look at this and say, 'Yeah,
  this is the fix that I want to make.'"* (AIE25 [13:31]). Acknowledges that
  evals themselves can be wrong ([14:02]).

**Technical depth strategy**: analogy first ("set a thief"), then trace
screenshot, then named metrics with concrete examples from the demo. Never
defines a term before showing why it matters.

**Vendor mentions**: brief, late, transparent. *"Something Galileo offers is a
custom-trained LLM…"* — one sentence, then back to principles.

---

## 12. Repeat-talk variation (what's scripted vs improv)

From paired API/SDK talks (Terrible API: APN24 vs NORD24a; APIs-to-SDKs:
APIW23 vs NORD24b):

**Scripted to the word** (identical across paired talks):

- Microwave-fish + Musk opener (Terrible API)
- Three-question audience funnel (SDK)
- "Four hardest things in computer science" joke
- HTTP verbs → CRUD mapping
- 418 I'm a teapot beat
- Break-glass-account weekend-DBA banking story
- "I'm lazy, I automate all the things"
- Twitter 56% survey with "not scientific" caveat
- Mainframes→desktop→web→mobile→DX history beat
- "All over the internet at Jim Bob Bennett" sign-off

**Audience-adapted** (changes between venues):

- Boss-in-the-room callouts (NORD24a only)
- Booth-specific jokes ("llama wandering around" NORD24a only)
- Hand-raises ↔ chat-drops swap for virtual format
- Whole sections sometimes added (Terrible API grew a 7th step between
  APN24 and NORD24a)

**Inference for upcoming talk**: structural skeleton is rehearsed; the spice is
improv. Drafting should produce a structural backbone with scripted set-piece
lines, leaving room for room-specific moves.

---

## 13. Style drift signals (2018-2025)

Patterns that read as **period-specific** (mostly 2018-2021, lighter in current
voice):

- **Verbal-hedge density higher**: "kind of / yeah / you know" per minute
  noticeably down.
- **Microsoft self-reference jokes** ("this is Jim from Microsoft trying to
  sell you things"). Gone now (he's at Arize).
- **"Pretty cool / pretty sweet" frequency** is way down in current talks.
- **Britishisms** like "gubbins", "gump", "draggy droppy", "funky" — mostly
  gone in current voice.
- **Pop-culture references** skew older in old talks (1960s sci-fi). Current
  talks lean AI-era touchpoints.

Patterns that are **durable** (consistent across 2018-2025):

- Hand-raise opens.
- "Great question, we'll come back to that" Q&A handling.
- Recap loops in longer slots.
- Moral-stake-then-tech hook (elephants → IoT; AI hallucination → eval).
- "Kind of" hedge (frequency reduced, still present).
- "And with that, thank you" dismount.
- Anthropomorphising demo props.
- Identity-and-CTA placement at the **end**, never the start.
- Demo-failure-as-humour.
- News-story or specific-real-example evidence shape.

---

## 14. Priority patterns for the upcoming context-graphs talk

Ranked by how strongly the corpus signals they'll fit a 25-minute AI/agents
talk demoing the procurement-agent + context-graphs loop:

1. **News-story opener** (Chicago Sun-Times pattern). Find 1-2 recent AI
   failure stories ideally from the same week as the talk. Hallucination >
   reasoning errors; specific names and dollar amounts.

2. **Hand-raise trap**. *"Who's deployed an AI agent in production? Who's had
   it disagree with what your humans actually do?"* — the trap is the gap.

3. **Folk-wisdom analogy for the core method**. "Set a thief to catch a thief"
   for evals. For context graphs, candidate analogies: "your AI has a Brent"
   (since Brent is already in the blog post); "the gap is the data"; "what
   Vera knows".

4. **The blog post's strongest line as the closer**: *"The hard part isn't the
   data. It's deciding to treat it as data."* — fits Jim's fragment-punch close
   pattern.

5. **Recap with "step one… step two…"** at the close, with callback to opening
   news story.

6. **Demo handling**: pre-empt with "this is non-deterministic", invite ("shall
   we look?"), narrate keystrokes, lean into anything that breaks as the
   lesson. Practical: prepare a demo that has a known failure mode you can
   *use*.

7. **Identity + CTA at end only**. "I'm Jim Bennett at Arize. All over the
   internet at Jim Bob Bennett. Repo's at github.com/Arize-ai/context-graphs.
   Thank you very much." — 15 seconds.

8. **Single load-bearing word**. AI talks lean on "non-deterministic". For
   context graphs, candidates: "override" (what Vera does), "signal" (what
   the gap is), "permission" (the cycle-2 insight). "Permission" is the most
   surprising, fits a fragment-punch.

9. **Three-beat lists** for the procedure (the blog post's 7 steps would
   compress to 3 for a talk: capture → mine → feed back).

10. **Avoid**: agenda slides, upfront bio, "thanks for having me", reading
    code, theoretical detours, multi-CTA stack, defining terms before showing
    why they matter.

---

## 15. Quotable lines to reuse or build on

These are signature beats from the corpus that the next talk can callback
or recompose:

- *"The best time to put evaluations in is as you're doing prompt engineering.
  The second best time is now."* (AIE25)
- *"You do not want to be the next Chicago Sun-Times."* (AIE25)
- *"Maximum X, minimum Y."* (SDK talks)
- *"Set a thief to catch a thief."* (AIE25)
- *"And with that, thank you very much."* (universal dismount)
- *"All over the internet at Jim Bob Bennett."* (universal sign-off)

These are signature beats from the blog post that match Jim's spoken style and
can be lifted as set-piece lines:

- *"The hard part isn't the data. It's deciding to treat it as data."*
- *"The agent is correct against policy and wrong against reality. The
  reviewer is right because they hold context the system of record doesn't."*
- *"An over-cautious agent doesn't need more rules. It needs to know when it's
  allowed to decide."*
- *"It just lacked permission."*
- *"Most teams collect the same data and throw it away."*
