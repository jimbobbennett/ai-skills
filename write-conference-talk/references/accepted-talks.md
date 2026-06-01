# Accepted-talk corpus — AI Engineer events

Conference-talk titles and abstracts that **actually got accepted** at recent
developer-conference CFPs. Use as a pattern-library when generating candidates
for a new submission. Three sources:

1. **AI Engineer Singapore (Nov 2025)** — title-only schedule from
   <https://www.ai.engineer/singapore>. Useful for current title fashion;
   no abstracts published on the schedule page.
2. **AI Engineer Summit 2025 (Feb 2025, NYC)** — title + abstract from
   <https://www.ai.engineer/summit/2025/schedule>. Useful for both title and
   abstract patterns.
3. **NDC Sydney 2026 (Apr 2026)** — title + full abstract from
   <https://ndcsydney.com/agenda> (one detail-page fetch per talk). Broader
   tech conference (not AI-specific); useful as a contrast to AI Engineer's
   style.

Workshops, panels, keynote-only slots, and social events excluded.

---

## Part 1 — AI Engineer Singapore titles (Nov 2025)

Format note: most slots are 10-minute talks; a handful are 15 or 20 minutes.
Tracks: Software, Design, Physical AI, Demo Stage.

| Title | Speaker / org | Format |
|---|---|---|
| NanoClaw's agent factory: how autonomous NanoClaw agents triage, review, and test every pull request on NanoClaw | Gavriel Cohen, NanoCo | 15m |
| Codex for Everyone: From Coding Agent to Computer Work Agent | Thibault Sottiaux, OpenAI | 20m |
| From Pilot to Platform: How Singapore Is driving AI Transformation in Government | Dr Feng Yuzhang, GovTech | 15m |
| The Friction Worth Keeping | Annie Luo, Google | 10m |
| Prompts Don't Have Opinions. You Do. | Jay Demetillo, Canva | 10m |
| Ship what's next | Jimmy Lai, Vercel | 20m |
| Why Sandboxes Are Non-Negotiable for Autonomous AI Agents | Vedran Jukic, Daytona | 10m |
| What We Learned From Analyzing Five Million Vibecoded PRs | Vaishant Kameswaran & Rohan Kumar, Greptile | 10m |
| AI Agents in Your Code Quality Pipeline: Shipping, Securing, and Measuring Them | Yuntong Zhang, Sonar | 10m |
| WTF Do People Use Open Models For? | Eugene Cheah, Featherless | 10m |
| November 24th 2025 — What Comes Next? | Max Buckley, Exa AI | 10m |
| Minions: Stripe's one-shot, end-to-end coding agents | Mark Doyle, Stripe | 15m |
| From Playing Solitaire to Operating ERP Software: Why Does Your Computer Need to Learn Click and Type? | Li Hau Tan, Simular | 10m |
| Designing the Agent-Native IDE: When Designers Ship the Code | Ryo Lu, Cursor | 20m |
| Designing multi-modal, multiplayer AI | Aosheng Ran, Figma | 10m |
| Agentic frontends: Building apps where AI can act, not just chat | Yangshun Tay, GreatFrontEnd | 10m |
| Noise Is All You Need: Engineering Sim-to-Real for Open-Source Humanoids | Selim Arguel, Menlo Research | 10m |
| World Models: a look at the future | Alberto Taiuti, Reactor | 10m |
| Agents Are the Next Billion Web Users | Nikola Balic, Steel | 10m |
| The Android Moment for Robots: Building an Open OS for Embodied AI | Jan Liphardt, OpenMind | 10m |
| Why prompting is the wrong way to make AI videos | Varick Lim, Voltade | 10m |
| Scaling low-latency LLM inference at GroqCloud | Andrew Tan, Groq | 10m |
| MoE at Scale: From GPUs to Wafer-Scale AGI | Daria Soboleva, Cerebras | 10m |
| GLM-5.1: Towards Long-Horizon Tasks | Zixuan Li, Z.ai | 20m |
| Give Your Chat Agent a Voice | Boris Starkov, ElevenLabs | 10m |
| Continual Learning for Long-Running Agents: Agents That Keep Getting Better | Jack Min, Prime Intellect | 10m |
| For AI to be Emotionally Intelligent | Michelle Julia, Bluelabs | 10m |
| Toward World Models: From Language to Physical Intelligence | Jacky Mok, Reka | 10m |
| Simulation, Games, and the Future of Robotics | Gokul Srinivasan, Antim Labs | 10m |
| A different playbook: the wisdom behind eastern product building | Wei Wei Hsu, Lentil | 10m |
| Voice AI is not a model issue. | Anun Joshi, Bland | 10m |
| Beyond Flat Design Output and Autocomplete: Solving the Complex Design Problems and Enterprise Design bottleneck with AI | Linh Nguyen, Obello | 10m |
| Sovereign AI: Localizing Frontier Models for Japan | Stefania Druga, Sakana | 10m |
| The Rise of the Agent Lab: What AI Engineers Build After Chatbots | Swyx, Cognition | 15m |

### Singapore title patterns observed

Tagged by which swyx template (or anti-pattern) each fits:

- **{BENEFIT} without {DOWNSIDE}**: *Codex for Everyone: From Coding Agent to Computer Work Agent* (sort of — promise + scope expansion).
- **{OPINION}, don't {THING YOU DO}**: *Prompts Don't Have Opinions. You Do.* (the strongest example on the list). *Why prompting is the wrong way to make AI videos*.
- **{POPULAR THING} IS DEAD** / **You Might Not Need**: *Voice AI is not a model issue.* (the negation move).
- **The Rise of {THING}**: *The Rise of the Agent Lab*.
- **{NUMBER} from {EXPERIENCE}**: *What We Learned From Analyzing Five Million Vibecoded PRs* (specific scale carries it).
- **Bold-claim-as-statement (no colon)**: *Ship what's next*, *The Friction Worth Keeping*, *Agents Are the Next Billion Web Users*, *Why Sandboxes Are Non-Negotiable for Autonomous AI Agents*, *The Android Moment for Robots*.
- **Curiosity question**: *WTF Do People Use Open Models For?*, *November 24th 2025 — What Comes Next?*, *Why Does Your Computer Need to Learn Click and Type?*.
- **Conscripts a buzzword and inverts it**: *Noise Is All You Need: Engineering Sim-to-Real for Open-Source Humanoids* ("noise is all you need" inverts *attention is all you need*).
- **Anti-pattern (still got in)**: *Beyond Flat Design Output and Autocomplete: Solving the Complex Design Problems and Enterprise Design bottleneck with AI* — long, "beyond" + "solving" + "with AI", a colon doing nothing. Counter-example: swyx is right that some titles succeed *despite* themselves.

### Most-quotable Singapore titles (top picks)

These are the ones that read like things you'd say to a friend at lunch. Use them as model-fits when drafting:

1. *Prompts Don't Have Opinions. You Do.* — opinionated, period-stops, 5 words.
2. *The Friction Worth Keeping* — counterintuitive claim, 4 words.
3. *Ship what's next* — verb-first command, 3 words.
4. *Voice AI is not a model issue.* — flat denial with a period.
5. *Agents Are the Next Billion Web Users* — provocative reframing, no jargon.
6. *Why prompting is the wrong way to make AI videos* — names the opinion, names the target.
7. *Noise Is All You Need* — earns the colon by inverting a famous title.

---

## Part 2 — AI Engineer Summit 2025 abstracts (Feb 2025, NYC)

Two days, two tracks: **AI Leadership** (day 1, mostly strategy + enterprise),
**Agent Engineering** (day 2, mostly engineering).

### AI Leadership Track

**Beyond the Consensus: Navigating AI's Frontier in 2025**
*Grace Isford, Lux Capital*
> Lux Capital Partner Grace Isford discusses the AI Frontier in NYC, sharing 10 "hot takes" on where the industry is going from a technical perspective.

**How To Build an AI Strategy That Fails**
*Hamel Husain (Parlance Labs), Greg Ceccarelli (SpecStory)*
> Explores reliable methods to waste resources while building AI strategies, emphasizing the disconnect between builders and executives, then demonstrates how to overcome these failures.

**Balancing Innovation with Security & Safety**
*Don Bosco Durai, Privacera*
> Examines how to "safeguard these systems without stifling innovation" through robust security frameworks and adaptive strategies in multi-agent systems.

**Building Self-Coding Agents**
*Colin Flaherty, Augment Code*
> Explores AI coding agents that improve their own codebases, discussing supervision at scale and "what might unlock when AI handles complexity."

**Anchoring Enterprise GenAI with Knowledge Graphs**
*Stephen Chin (Neo4j), Jonathan Lowe (Pfizer)*
> Discusses connecting organizational datasets through knowledge graphs to "enable higher accuracy and more explainable retrieval using GraphRAG."

**Building AI Agents with Real ROI in the Enterprise SDLC**
*Bruno Passos (Booking.com), Beyang Liu (Sourcegraph)*
> Case study of large-scale code migration using AI agents, covering "agents for large-scale code migration, code review, and internal dev tools."

**Building Trust in Enterprise AI: Evaluating Domain-Specific LLMs for Real-World Financial Scenarios**
*Waseem Alshikh, Writer*
> Challenges "the scaling narrative around general-purpose models" and demonstrates how domain-specific LLMs deliver superior performance in finance.

**Lessons from Building LinkedIn's GenAI Platform**
*Xiaofeng Wang, LinkedIn*
> Explores developing "a scalable and adaptable GenAI technology stack" within Java-based infrastructure, including multi-agent system architectures.

**Specialized RAG Agents: Lessons learned from deploying complex AI systems in production**
*Douwe Kiela, Contextual AI*
> Addresses the principle "garbage in; garbage out" and shares lessons from "deploying enterprise RAG systems at scale" for Fortune 500 companies.

### Agent Engineering Track

**Why Agent Engineering**
*swyx, Latent.Space*
> An anthropological approach to agent engineering.

**Building and evaluating AI Agents That Matter**
*Sayash Kapoor, AI Snake Oil*
> Explores how current agents "fall far short of their claimed performance" and presents best practices for agent evaluation.

**Going deep on Gemini Deep Research**
*Mukund Sridhar (DeepMind), Aarush Selvan (Google Gemini)*
> Discusses building tools to "turbocharge this process" of research automation across complex information gathering tasks.

**How We Build Effective Agents**
*Barry Zhang, Anthropic*
(No published abstract.)

**Sierra's Agent Development Life Cycle**
*Zack Reneau-Wedeen, Sierra*
> Describes methodology enabling "Sierra agents to be reliable, testable, and incredibly capable" across consumer brands.

**What RL Means for Agents**
*Will Brown, Morgan Stanley*
(No published abstract.)

**Agents in Investment Management: Aladdin Copilot**
*Brennan Rosales, BlackRock*
> Details "a multi-agent platform that enables federated application development in a controlled and explainable environment."

**Building AI-Powered Developer Tools at Jane Street**
*John Crepezzi, Jane Street*
> Explores creating custom assistants for OCaml, covering "data collection and model training to seamless editor integrations."

**Challenges to Scaling Agents for Generative AI Products**
*Anju Kambadur, Bloomberg*
(No published abstract.)

**Trust, but Verify: High-Fidelity Reasoning in Agentic Workflows**
*Mike Conover, Brightwave*
> Details engineering patterns for "automated creation of high-signal, information-dense investment research reports."

**Agents are built at the fringe: getting from 90 to 100**
*Kevin Hou, Windsurf*
(No published abstract.)

**How we scaled 500m AI agents in production with 2 engineers**
*Mustafa Ali (Method Financial), Kyle Corbitt (OpenPipe)*
(No published abstract.)

**Voice AI: Your Bot Isn't Special**
*Nik Caryotakis, SuperDial*
> Discusses voice AI orchestration tooling and building "reliable voice agents that navigate phone trees" in healthcare.

**Scaffold Wisely: How the Bitter Lesson Applies to AI Agents**
*Rahul Sengottuvelu, Ramp*
> Explores how "embracing the bitter lesson can transform our approach to building AI agents."

**Creating Agents That Co-Create**
*Karina Nguyen, OpenAI*
> Discusses "shifting our perspective of AI from narrow, task-focused tools to collaborative agents."

**Building Perfect Memory**
*Maria de Lourdes Zollo (Bee.Computer), Ethan Sutin (Bee.Computer)*
(No published abstract.)

**Tools for the Next Generation of AI Engineers**
*Stefania Druga, Google*
> Explores "open-source multimodal agents that are proactive and nudge you to explore different topics."

**What does it take to build a personal, local, private AI Agent that augments you deeply?**
*Soumith Chintala, Meta PyTorch*
> Addresses whether agents can "run locally, fast, keep your information access in your control."

### Abstract patterns observed

Across the 20 abstracts above, the shape is consistent:

1. **First sentence names the problem or stakes.** *"current agents fall far short of their claimed performance"*; *"scaling narrative around general-purpose models"*; *"the disconnect between builders and executives"*. The problem is *named* in the first 10-15 words; there's no scene-setting.

2. **One concrete artifact / technique / claim.** *"a multi-agent platform that enables federated application development"*; *"high-signal, information-dense investment research reports"*; *"reliable voice agents that navigate phone trees"*. The talk is anchored to *one* thing the speaker built or learned, not a survey.

3. **Length: 25-50 words is the sweet spot.** Longer than that and the abstract starts to feel like a brochure. Many abstracts on the list are a single sentence.

4. **No first-person.** Almost all abstracts are written in third person (*"Explores", "Discusses", "Demonstrates", "Details"*). This is conference-shorthand; if Jim's voice prefers first-person, that's allowed but contrarian for the format.

5. **Stakes language, not feature language.** *"safeguard these systems without stifling innovation"* (stakes) beats *"introduces a new framework with novel features"* (features).

6. **Quote-able phrases in scare quotes.** Notice how many abstracts quote a phrase: *"garbage in; garbage out"*, *"hot takes"*, *"the bitter lesson"*, *"actually work"*. These signal the speaker has a memorable framing and is staking a claim on a phrase.

7. **The strongest abstracts target a target.** *"How To Build an AI Strategy That Fails"* targets executives. *"Voice AI: Your Bot Isn't Special"* targets people who think their bot is special. Stating who's wrong is more activating than stating who's right.

### Strongest abstracts as templates

These are the three abstracts most worth copying the shape of:

**"Voice AI: Your Bot Isn't Special"** — title is the punchline, abstract names the concrete artifact (orchestration tooling for phone trees) and the domain (healthcare). 25 words.

**"How To Build an AI Strategy That Fails"** — title hooks via inversion, abstract names the target (the disconnect between builders and executives) and previews the payoff (how to overcome). 30 words.

**"Building Trust in Enterprise AI: Evaluating Domain-Specific LLMs..."** — abstract opens by *challenging* a popular position (*"the scaling narrative around general-purpose models"*) and previews the contrary evidence. 30 words.

---

## Part 3 — NDC Sydney 2026 (Apr 2026)

A general developer conference, not AI-specific. .NET-heavy but increasingly AI-themed. **All 29 talks below are 60 minutes** — note the slot length when copying abstract length.

> Source: <https://ndcsydney.com/agenda> + 29 individual talk detail pages.
> Five abstracts were returned partially-summarised by the fetcher rather than verbatim (marked inline below). The remaining 24 are verbatim quotes.

### 3.1 NDC Sydney titles — pattern observations

Compared to the AI Engineer corpus (Parts 1 + 2), NDC Sydney titles:

- **Use colons freely** — 11 of 29 titles have a colon. Most use colon for a setup-payoff pattern: *"Pwned with Purpose: Where Motives Meet Mayhem"*, *"Bulletproof - Designing for risk, resiliency and recovery"*, *"Production-Grade LLM Architecture: Lessons from Processing 50 Million AI Requests"*. swyx would push back on most of these; the venue tolerates them.
- **Are longer** — most titles are 7-12 words. Compare to AI Engineer Singapore where many titles are 3-5 words.
- **Lean heavily on pop-culture and metaphor** — *Wile E. Coyote*, *Indiana Jones*, *Garden of Eden*. These talks tend to be the most popular slots.
- **Use the "X That Don't Suck" / "X That Actually Works" pattern openly** — *"AI Agents That Don't Suck"* — a less polished version of the AI Engineer *"Voice AI: Your Bot Isn't Special"* move. Same pick-a-fight energy.
- **Period-stop and pure declarative are rare** — only *"Your website does not need JavaScript"* lands that way. The Singapore corpus has many more of these.

### 3.2 NDC Sydney abstracts — pattern observations

Compared to AI Engineer Summit abstracts (~25-50 words, third-person, single-sentence-often):

- **Longer.** Most NDC Sydney abstracts are **100-200 words** in 2-3 paragraphs. The 60-min slot earns the extra space.
- **Heavier signposting.** *"In this session, we'll explore..."*, *"You'll learn how to..."*, *"In this talk I'll share..."*. AI Engineer abstracts mostly skip the signposting.
- **Takeaway-focused close.** Most NDC abstracts end with *"You'll leave with..."* or *"Whether you're X or Y, you'll walk away with..."*. AI Engineer abstracts more often end with the artifact, not the audience benefit.
- **Story-led openings are common.** *"When I started out in development, unit testing was all the rage"* (Bogard, talk 9). *"Some of the best things we build as programmers never ship to customers"* (Thulke, talk 10). *"In the first paper on using LLMs trained on code in 2021..."* (Shaw, talk 16). Personal-anecdote opener is on-trend for NDC.
- **"In this session we'll..." opening verbs.** Inventory of openings in the corpus: *examine, dive, walk through, build, show, share, explore, examine, learn, present*. All third-person plural future. Pick one that fits the talk's shape.

### 3.3 Strongest precedents for Jim's context-graphs talk

Pulled out because they're the closest topical fit:

**7. AI Agents Need Permission Slips** — Heather Downing — **same permission theme** as Jim's cycle-2 insight. The abstract's structure: *"MCP servers connect AI agents... but most examples aren't specific about what they have access to..."* → names the failure mode (*"reorganize your file system or email your entire customer database"*) → names the solution (*"dynamic permission scoping, context-aware authorization, human approval gates"*) → audience promise (*"useful enough to deploy but constrained enough to trust with production data"*). 130 words. **Note**: this talk uses *"permission"* in the title where Jim's draft uses *"allowed to decide"* in the abstract. Worth checking if the overlap is fine or if Jim's title should re-stake the ground.

**18. Production-Grade LLM Architecture: Lessons from Processing 50 Million AI Requests** — Vaishnavi Gudur — strong **scale-as-credibility** opener: *"Most AI talks show you how to call an API. This one shows you how to build production systems that don't fall over when real users arrive."* — picks a fight with other AI talks, then quotes a number (50M monthly). Replicable shape for Jim: *"Most teams treat the gap as noise. This talk treats it as the training set."*

**27. AI Agents That Don't Suck: How to Build Ones That Actually Drive Business Value** — Robert Koch — title is a fight; abstract opens with *"AI agents are everywhere — but most of them don't work."* Then names the cost (*"drain engineering time, frustrate end users, burn budgets"*). Three concrete pains before any solution. Lesson: AI Engineer abstracts open with the technical problem; NDC abstracts open with the *human* problem.

**5. From Copilot to the Garden of Eden** — Adam Cogan — metaphor title, abstract uses the metaphor as the through-line. Replicable if Jim wants to retitle his talk around a metaphor (*"From Override to Override-As-Data"* etc.) — though current direction doesn't lean on metaphor.

### 3.4 Talks in the corpus

#### 1. The Next Steps to Becoming a Space-Faring Civilization
*Richard Campbell* — Fun, People
> What will it take for humanity to become a space-faring civilization? Join Richard Campbell as he talks about the near-term technologies that are moving this idea closer to reality. The first problem is getting up there — and improvements in rocket design have substantially lowered the cost of access to space. Then the question — what do we do up there? And how do we stay? And is that even possible in the long term? Why bother being a space-faring civilization?

#### 2. From Pair to Peer Programmer
*Aaron Powell (Microsoft)* — AI, Tools
> Let's be honest: AI tools in development are being pushed into our workflows, and not everyone's thrilled about it. But they're here — and they're changing. What started as autocomplete has become chat assistants, CLI tools, and cloud agents, with their evolution being claimed as a shift from a pair programmer to that of a peer in our virtual team. This session takes a practical look at how we can work with these tools effectively, optimise them for real-world use, and critically assess when they're genuinely contributing… and when they're just getting in the way.

#### 3. The Wile E. Coyote approach to AI for backyard beast management
*Todd Whitehead* — AI, Architecture, Cloud, Fun, IoT, Security
> A funny, practical tour of AI + IoT for backyard beast management — humane deterrents, edge vision, and a Wile E. Coyote approach to iterating without (much) collateral damage.
>
> Australia's backyard fauna are nature's ultimate chaos engineers. In this fast-paced, demo heavy session, we'll channel our inner Wile E. Coyote — optimistic, iterative, occasionally singed — and show how combining AI, IoT, and a bit of ACME-grade creativity can turn your backyard, deck and shed into a humane, real-time defence system.

#### 4. Effortless Distributed Systems with Aspire
*Jason Taylor (Particular Software)* — .NET, Architecture, Cloud, DevOps
> Distributed systems can be overwhelming — but with .NET Aspire, building them feels refreshingly simple. In this session, we'll explore a multi-service, message-driven application and see how Aspire streamlines orchestration, configuration, and diagnostics across your system.
>
> Along the way, I'll show how easily you can plug in messaging, persistence, and observability without the usual wiring and complexity. Once it's running locally, we'll set up CI/CD and deploy the whole thing to the cloud — with minimal effort.
>
> Whether you're modernizing an existing solution or starting from scratch, you'll walk away with practical ideas and a new appreciation for Aspire's end-to-end developer experience.

#### 5. From Copilot to the Garden of Eden
*Adam Cogan (SSW)* — AI
> Move beyond the underwhelming 2023 'Copilot hype' to the tools actually delivering value for developers. SSW's Adam Cogan cuts through the noise, exploring how AI is fundamentally reshaping the enterprise stack, from Copilot and Cowork to agentic workflows and CLI-based coding.
>
> Learn how roles are shifting, which AI assistants are winning, and what an AI-integrated 'Garden of Eden' looks like. Leave with a practical roadmap to build, analyze, and automate with confidence.

#### 6. The Azure AI Ecosystem for Real-World Enterprise ROI
*Adam Stephensen (Agile Insights)* — AI, .NET, Architecture, Cloud
> Enterprise AI success is no longer about choosing the right model or writing better prompts — it's about building the right ecosystem. In this session, we explore the Azure AI ecosystem from a delivery and architecture perspective, showing how real-world AI solutions emerge from the combination of data platforms, semantic foundations, agent orchestration, pro-code and low-code experiences, and securely exposed tools and APIs. Drawing on Microsoft's latest Ignite announcements — Fabric IQ, Foundry IQ, and Work IQ — we'll unpack how Microsoft is converging on a unified intelligence layer that finally makes AI agents useful at enterprise scale. You'll see how these capabilities map to practical architectures, where teams typically go wrong on the path to AI ROI, and which patterns consistently succeed. The focus is on delivering measurable value today — search, summarisation, decision support — while deliberately preparing for the next wave of agent-driven systems. This talk is aimed at developers and architects who want to move beyond demos and build AI platforms that scale, govern, and deliver real outcomes.

#### 7. AI Agents Need Permission Slips
*Heather Downing* — AI, Security
> MCP servers connect AI agents to enterprise systems, but most examples aren't specific about what they have access to — they just assume you know. This works until your assistant decides to reorganize your file system or email your entire customer database. Turns out giving AI agents broad permissions is like giving a toddler car keys.
>
> This session guides authorization for AI workflows beyond RBAC (Role-Based Access Control). We'll implement dynamic permission scoping, context-aware authorization, and most importantly, human approval gates for dangerous operations. You'll learn to build agentic workflows that are useful enough to deploy but constrained enough to trust with production data.

#### 8. Build your own Flight Tracker with Microsoft Agent Framework
*Arafat Tehsin (Fedorai, Microsoft MVP)* — AI, .NET
> Imagine a world where your AI agent doesn't just respond, but actively plans, reasons, and takes action across multiple systems like a true digital copilot. That's the power of the Microsoft Agent Framework, the latest innovation from Microsoft that unifies the best of Semantic Kernel and AutoGen into a single, enterprise grade platform.
>
> In this session, we'll build a Flight Tracker from scratch, powered by the Agent Framework. Along the way, you'll learn how you can orchestrate agents that can fetch live flight data, manage context, and respond in natural language as well as use tools, connectors, and memory to make your agent reliable and context-aware.
>
> We will also explore human-in-the-loop approvals as well as learn to integrate with famous protocols like A2A and MCP so your agent doesn't just act but acts responsibly.
>
> By the end, you'll see how the Microsoft Agent Framework makes it easier than ever to go from idea to prototype to production-grade AI agent, with enterprise reliability built in. It's going to be demo-packed, developer-focused session where you'll discover how to harness the Agent Framework to bring your own AI agents to life whether that's a Flight Tracker or the next big AI-first app.

#### 9. Building the Ultimate Safety Net with Integration Tests
*Jimmy Bogard* — .NET, Testing
> When I started out in development, unit testing was all the rage. We broke functionality into smaller and smaller classes, building mocks as we went. There was a hidden menace here — one refactoring change would break a slew of tests, and I became disillusioned.
>
> This is when I discovered integration tests — a far more effective safety net for ensuring our system works as expected. But building effective integration tests is much more challenging than isolated unit tests.
>
> In this session, I'll break down the common tools used in integration tests for .NET, including the testing package for Microsoft and other extensions such as FastEndpoints. I'll also cover dealing with shared state and infrastructure like databases using TestContainers, and external uncontrollable dependencies.
>
> Finally, I'll share patterns for building effective and maintainable integration tests for a variety of application types, from web apps, to APIs, to messaging endpoints.

#### 10. Accidentally Levelling Up Your Career with Personal Projects
*Bron Thulke (YouLive to Travel)* — Fun, .NET, Tools, Work skills
> Some of the best things we build as programmers never ship to customers — they live in our homes, our budgeting processes, our daily tasks, and our random weekend experiments.
>
> *(Detail page returned remainder summarised, not verbatim.)*

#### 11. 10 tips to level up your ai-assisted coding
*Aleksander Stensby* — AI
> AI coding assistants are rapidly reshaping how developers write, debug, and ship software. Tools like Cursor and Claude Code can supercharge productivity — only if you know how to use them effectively.
>
> In this session, we'll cut through the hype and focus on practical, developer-tested strategies for getting the most out of AI in your workflow. You'll learn how to master prompting and context engineering, make the most of long context windows, streamline debugging and testing, and integrate AI into your daily development practices without sacrificing code quality or security. We'll also explore how emerging standards like Model Context Protocol (MCP) unlock new workflows by connecting your AI assistant directly to tools such as GitHub, Slack, Playwright or Figma — turning it from a code generator into a true development teammate.
>
> Whether you're new to AI-assisted coding or already experimenting with it daily, you'll leave this talk with concrete ideas and techniques you can apply immediately to level up your development process.

#### 12. Meditations on Code As Art
*David Whitney (NewDay, Electric Head Software)* — People, Ethics, Fun
> Code can be beautiful, elegant and performant, but can it deliberately be artistic?
>
> *(Detail page returned remainder summarised, not verbatim.)*

#### 13. Building fun and creative messaging experiences on WhatsApp
*Michelle "MishManners" Duke* — AI, Machine Learning, Tools
> In this talk, I'll show how to turn a simple WhatsApp message into an AI-powered creative experience. Using Twilio, WhatsApp, and OpenAI's image generation APIs, we'll build a workflow where users can send images via WhatsApp; think selfies, pet pics, and photos from the conference, and receive a cartoon, sketch, or fun version of your photo to share on your socials, group chats, and company message boards.
>
> *(Detail page returned a second portion summarised: setting up Twilio's WhatsApp sandbox, processing images, best practices, additional applications.)*

#### 14. Designing AI-Powered Backends with Azure OpenAI: Reliable, Structured, and Production-Ready
*Mark Tinderholt (Microsoft Azure platform engineering)* — AI, .NET, Architecture, Cloud, Microservices
> *(Detail page body returned summarised, not verbatim. Summary: building dependable AI backends using Azure OpenAI, progressing beyond chat to implement intelligent business logic, generating structured outputs like JSON and classifications with strong validation, a practical example showing AI identifying existing entities to prevent duplicates and maintain data integrity, prompt patterns, token management, and architectural strategies to transform Azure OpenAI into a predictable backend service.)*

#### 15. Bulletproof - Designing for risk, resiliency and recovery
*Andrew Cobb (former Azure CTO, Microsoft Australia)* — Architecture, Cloud
> While AI may have changed much about SW development and the types of apps being built, it hasn't removed system failures and the need to plan for absorbing them or recovering from them. Do you get your SLAs, HAs and DRs confused with your RPOs and RTOs? The cloud vendor will take care of recovery right? How does SaaS change the planning? What risks do I need to cater for, and which do I ignore? This session is designed for anyone building enterprise grade systems or being in the position of having to work with stakeholders on requirements, options and costs. With some lightning storms, a bit of math and lots of take home tools and discussion starters, this session is designed to make you feel more confident when designing your next 99.999% uptime system.

#### 16. Are LLMs good software engineers?
*Anthony Shaw* — AI, Programming Languages
> In the first paper on using LLMs trained on code in 2021, the authors at OpenAI warned '[the LLM] may suggest solutions that superficially appear correct but do not actually perform the task the user intended. This could particularly affect novice programmers, and could have significant safety implications depending on the context'.
>
> 5 years later we're starting to grapple with some of the implications of that issue. LLM-generated code is being smuggled into large code bases, some successfully and others not. Open-Source maintainers are creating policies forbidding LLM-generated contributions, yet others are delegating their tech-debt and backlogs to LLMs.
>
> In this talk I'll be sharing some data and insights on the analysis of millions of lines of LLM-generated code. I'll explore some principles of software engineering, maintainability and quality and explore how they apply to an AI-generated toolset. I'll share some techniques for improving software quality when using LLMs and my opinions on the long-term risks with letting the LLM write the code.

#### 17. Indiana Jones and the Temple of Legacy Code
*William Brander (Particular Software, NServiceBus)* — Programming Languages, .NET, Architecture
> Legacy systems are like ancient temples: full of mystery, danger, and long-forgotten knowledge. One wrong move and the whole thing might collapse. But somewhere deep inside lie years of embedded business logic, customer trust, and operational quirks that no rewrite can replace.
>
> In this talk, we'll don the fedora and take up the whip as we explore techniques for exploring legacy codebases without triggering the traps. We'll dig into Source control archaeology, safe refactoring strategies, introducing tests in a hostile environment, and recognizing "cursed" files with high churn or hidden dependencies.
>
> Whether you're maintaining a dusty monolith or inheriting a mystery repo, this session will equip you with tools and tactics to escape with the real treasure: Knowledge of how to extract business value and gradually modernize.

#### 18. Production-Grade LLM Architecture: Lessons from Processing 50 Million AI Requests
*Vaishnavi Gudur (Microsoft)* — AI
> Most AI talks show you how to call an API. This one shows you how to build production systems that don't fall over when real users arrive. Over 18 months, we scaled from 'ChatGPT prototype' to a production AI platform processing 50 million LLM requests monthly.
>
> AI systems aren't merely APIs with sophisticated responses — they function as distributed systems with unpredictable failure modes, variable costs, and reliability obstacles that challenge conventional architectural designs. This presentation provides an in-depth technical examination of constructing AI infrastructure capable of withstanding production environments.

#### 19. Let's build an AI agent
*Phil Nash (IBM, Google Developer Expert)* — AI, JavaScript
> 2025 is the year of agents, but what does that mean? Rather than spend time going over the theory, let's walk through the process of building an agent live. You'll see how large language models, functions, and open source tools fit together to bring to life an agent over the course of the talk. We'll build out an agent that starts simple and graduates to a multi-agent model, with different components managing and performing tasks. You'll leave with a good idea of what you need to know to start building your own powerful agents.

#### 20. Your website does not need JavaScript
*Amy Kapernick* — JavaScript, Fun, Web
> When we build a website these days, there's a 110% chance that it's got some form of JavaScript on it. Whether it's a full framework, for animations, to trigger a popup or as a tracking script, JavaScript is all around us. But what if I told you that you didn't have to use JavaScript at all? Not even as a build process? Thanks to updates in browser technologies, there's now a plethora of native browser features that allow building modern, functional websites, sans JavaScript. So together, we'll build out a *completely* static website, a collection of HTML and CSS files, no tracking, no scripting, no servers, no third-party resources. Let's build a website the way we used to (but no marquees).

#### 21. Pwned with Purpose: Where Motives Meet Mayhem
*Troy Hunt (Have I Been Pwned, Microsoft Regional Director)* — Security
> Every data breach tells a story — not just of compromised information, but of human motive. Drawing on a dozen years of experience running Have I Been Pwned, this talk explores why hackers exfiltrate and share data, what those motives reveal about the evolving threat landscape, and how understanding them helps us respond more effectively in partnership with website operators.

#### 22. Platform Engineering in the age of Generative AI
*Will Velida (Microsoft Industry Solutions Engineering)* — AI, Architecture, Cloud
> Establishing a platform that serves the needs of your developers is a challenge for teams of all sizes. But with Generative AI tools like GitHub Copilot, surely this is now all easy, and all we need is a few prompts, right? Well, no, not really. Your onboarding processes are probably poorly documented, the tools your developers use on a day-to-day basis vary wildly between teams, and the way your teams deploy to production vary from dated bash scripts to crossed fingers over beers on Friday. Hardly the solid context needed for generative AI to actually be helpful. In this talk, we'll explore how platform engineering and generative AI can work together to improve developer experience, if you get the foundations right. We'll look at common organisational and cultural challenges that limit productivity, and how to start addressing them with simple, practical steps. From there, we'll show how "everything-as-code" patterns and AI-assisted tooling (such as MCP servers, coding copilots etc.) can accelerate platform maturity and reduce friction across teams. Whether you're a platform engineer, developer, or tech leader, you'll leave with a clearer view of how to build a platform that AI can actually help with, and how to make your developers happier in the process.

#### 23. Zero Trust in a SaaS and AI World
*George Coldham (Microsoft Cloud Solution Architect)* — Security, AI, Architecture, Tools, Web
> The browser has become the new enterprise perimeter. From engineers pasting proprietary code into ChatGPT, to stolen SaaS session tokens fueling large-scale breaches, real incidents prove that most data leakage and credential abuse now happens *in the browser*.
>
> In this session, we'll examine how Zero Trust principles can be enforced at the browser layer. Using case studies from recent security incidents, we'll map real-world compromises to MITRE ATT&CK techniques and show how enterprise browsers and browser isolation platforms are evolving into critical security control points.
>
> Attendees will learn how to mitigate SaaS and GenAI risks with in-browser DLP, tenant restrictions, OAuth consent governance, and session telemetry — without locking down productivity. Whether you're a CISO, security architect, or practitioner, you'll leave with a clear understanding of why the browser is now your most important Zero Trust battleground.

#### 24. Get a Grip on your Telemetry using the OpenTelemetry Collector
*Adam Gardner (DT Open-Source Program Office)* — DevOps, Tools, Workskills
> In this talk I'll present real use cases that I've collated working with enterprises looking to ingest telemetry via the OpenTelemetry collector. Batching, enrichment, filtering, redaction, sampling — it's all here. No AI, no product pitches, just actionable insight.
>
> This talk will provide a gentle introduction to the collector itself, then dive into the specific examples.

#### 25. Old API, New Tricks: Add MCP to Existing .NET REST Endpoints
*Jonathan "J." Tower (Trailhead Technology Partners)* — DevOps
> Your existing .NET Web APIs have served you well — but what if they could do more with them in the era of AI? In this session, we'll explore how to breathe new life into your existing ASP.NET Web API endpoints built with ASP.NET CORE by adding Model Creation Protocol (MCP) capabilities to them.
>
> We'll look at how the MCP C# SDK makes it simple to annotate your existing controllers, instantly transforming your REST endpoints into AI-powered services that can empower LLMs and agents. We'll also compare this approach to a no-code approaches using Azure API Management.
>
> Finally we'll look at where both of these approaches fall short and are only a starting point for a good long-term MCP design. You can use then to jump start the process and then follow the path we outline together to evolve your APIs from technical plumbing to intelligent, task-focused tools that solve real problems using AI — all without starting from scratch.

#### 26. Spec-Driven Development: The Fast Track to 10x?
*Jerry Nixon (Microsoft SQL Server PM)* — AI
> Spec-Driven Development (SDD) is the brave new world in AI coding we all knew was inevitable. More like a revolution than an evolution of software delivery, SDD produces solutions as artifacts of a structured specification. This specification is the contract for code behavior and the single source of truth guiding developers, tools, and AI agents to generate, test, and validate results. It is software engineering through prompt precision.

#### 27. AI Agents That Don't Suck: How to Build Ones That Actually Drive Business Value
*Robert Koch (Quarterzip)* — AI, Cloud, Machine Learning, Security
> AI agents are everywhere — but most of them don't work. They drain engineering time, frustrate end users, and burn budgets without ever proving their worth.
>
> *(Detail page returned remainder summarised: a practical framework for designing and deploying AI agents that create measurable business impact, a checklist for determining if an agent warrants development, common pilot failure points and mitigation strategies, methods for demonstrating value to stakeholders, and lessons from enterprise implementations that achieved real results rather than remaining demos.)*

#### 28. Web APIs You Should Be Using in 2026: Unlocking Next-Level Web Experiences
*Nhlanhla Lucky Nkosi (BBD)* — Web, Cross-Platform, JavaScript, Mobile
> The web is evolving, and so are the APIs that power it. This talk dives into the newest and most underutilized browser APIs, including the File System Access API, Background Fetch API, WebGPU, Web Share API Level 2, and Contacts Picker API. Attendees will learn how these tools can simplify development, enhance user experience, and bring desktop-like capabilities to the web. Through live demos and practical industry examples, developers will leave with actionable insights and inspiration to integrate these APIs into their own projects.

#### 29. Platform Engineering vs DevOps
*Dylan McCarthy (Versent, Microsoft MVP)* — DevOps
> In the last few years we have seen a rise in the usage of the term Platform Engineering, but what does that actually mean and how does it compare to DevOps? In this talk I will present what these both mean to me as someone who has been a 'DevOps' engineer and is now a Platform Engineer. I'll talk about the 'Platform Engineering Iceberg' showing how what appears to be a simple term hides a mass of complexity and challenges. And to wrap it up I'll talk about Developer Experience and how that ties into all of this.

---

## How to use this corpus when drafting

When generating candidate titles or abstracts:

1. Read the swyx framework (`title-craft.md`) for the templates and don't-do list.
2. **Pick the right corpus weighting by venue.** AI Engineer wants short, period-stop, opinionated titles + 25-50-word abstracts. NDC wants longer titles (colon-tolerant) + 100-200-word abstracts with audience-takeaway closes.
3. Scan this file for the closest **5-7 precedent talks** — by topic *and* by shape. Note their lengths, opening moves, and how they name the stakes.
4. Generate 8-12 candidate titles using the swyx templates; reject anything that hits the weasel-word list.
5. For the abstract, follow the patterns observed above: problem in the first sentence, one concrete artifact, stakes-language, ideally targeting *someone who is wrong*. Match length to the venue.

When a candidate feels "safe", it's probably weasel-worded. The accepted-talk corpus shows both AI Engineer and NDC reward talks that pick a fight or stake an unusual claim.
