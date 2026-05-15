---
title: 'Prompt Learning — optimize your coding agent against your own codebase'
conference: 'unknown (deck source only)'
year: 2025
source: 'Keynote deck'
source_file: '~/Desktop/prompt-learning.key'
slide_count_total: 37
slides_included: '7–37 (skipped event code-of-conduct + empty title cards 1–6)'
extraction_method: 'osascript /tmp/extract_keynote.applescript'
---

_Source: Apple Keynote deck. No video / no timestamps. Structured by slide
number. Each slide section captures the on-slide text (title + body) and Jim's
presenter notes — the notes are the spoken narration._

## Slide 7 — Who used to actually write code by hand?

**Notes:**
Who used to write code by hand? Yeah, I know we don't do this anymore.
When writing code, a lot of teams had standards — standard ways of doing
things, standard practices, architectural standards, documentation standards
and so on.
We also had standards and guidance when fixing bugs, usually based on the
experience of the team. Fix in the base class, not the derived class, follow
DRY and move code into helpers when it is repeated, and so on.
We also needed time to learn the code and understand its nuances.

## Slide 8 — How did we enforce these standards?

**Notes:**
So how did we enforce these?
Manually, via detailed PR reviews. Giving new folks time to learn the code base.

## Slide 9 — What about coding agents?

**Notes:**
What about with AI?
How can we make AI not only better with our code base, but also follow our guidance?

## Slide 10 — claude.md

**Notes:**
There are files to guide your agent, like claude.md that can provide instructions.
But how do we write this file? We could try to do it by hand, but we will probably miss important things.

Better to have it created for us. To do this we need:
A source of truth that reflects the real way the code has been written
A way to create the file, then test it, then iterate

So what techniques can we use to do this? Prompt learning!

## Slide 11 — Prompt Learning

**Notes:**
Prompt learning is kind of like fine tuning a prompt, similar to how you fine tune a model. Except instead of tweaking the underlying model, you are tweaking the prompt.

Instead of numerical scores, this is based off human feedback in natural language.

## Slide 14 — Prompt Learning

**Notes:**
So how does prompt learning work.
Essentially, you have an agent with a prompt.
It does a thing.
You then run an eval over the result — using an LLM-as-a-judge, or even human feedback. This gives you English language feedback rather than a simple numeric score.
This is where tools like AX or Phoenix from Arize are really important as they can run the experiments and evaluations for you.
You then use this feedback to update the prompt using an LLM to create an updated prompt.
Rinse and repeat a few times until you get the agent working the way you want.

This is essentially an evals loop, with automated prompt updates in a loop.
Not numerical output like reinforcement learning, no model fine tuning, just iterating on the prompt to see what works.

## Slide 15 — Prompt Learning

**Notes:**
Evals — Arize AX or Phoenix.

## Slide 16 — Prompt Learning

**Notes:**
Think of it like a student. They have knowledge (system prompt), they take a test, the teacher evaluates the results of the test, then gives the student feedback in English to improve their knowledge. Over multiple tests with multiple feedback, the student eventually grasps the topic and is successful on the exams.

## Slide 17 — What does this look like in the real world

**Notes:**
This all sounds great in theory, but what does this look like in the real world?
Well we tested it out using SWEBench to see if we could optimize Claude Code.
Obviously optimizing via the Claude.md file, not using the leaked source code.

## Slide 18 — Measure first.

**Notes:**
We used SWE bench lite, the benchmarking tool for code agents coding with Python. This contains 300 real world issue-commit pairs across different python repositories. So it has the repo, the issue, and the actual solution committed as a ground truth.

We can use 150 for training, 150 for testing.

This gives us the ability to point the coding agent at a repo and an issue, then the agent lets rip on a fix. These are real issues, not noddy hello world type problems, but real coding issues that need a deep understanding of the repo.

These repos have unit tests that we can use to test the fix.

Once fixed, we can then use another LLM to review the fix against the ground truth from the real commit.

## Slide 19 — Prompt Learning

**Notes:**
Coding agent writes code based off an SWE Bench test.
Unit tests are run — these are the unit tests from the ground truth, so they are our measure of success.
Check if it passes or fails.
All this data is then fed into Arize AX to store the data as datasets and test it in experiments.
AX runs eval against the pass/fail, ground truth solution and get verbal feedback.
Evals are the important part here — these are powered by GPT-5 using LLM as a judge. The prompt is in our repo.
Use GPT-5 to optimize rules using a meta-prompt, a prompt designed to tweak prompts.
Repeat 5 times, each time updating the coding agent rules.

## Slide 20 — Our baseline

**Notes:**
Measurement is important.
We ran Claude Code as is out the box against SWEBench lite, and it resolved 40% of the issues based off the unit tests from the ground truth.

## Slide 21 — Our result

**Notes:**
After running 150 training iterations, we tested on the other 150 and now we're at over 45% success, a 12% relative improvement.

This is generic though, the dataset was from different repos all using Python.

## Slide 22 — (rule examples, slide body)

**Body (on-slide rules text):**
- When modifying or generating APIs that provide string representations (e.g., __str__, __repr__), always ensure the output matches user expectations and established library interface contracts, especially when type or context may change.
- When overriding equality (__eq__) or hashing (__hash__) logic for objects that can have mutable or nested structures, ensure comparisons are both order-insensitive (where applicable) and type-consistent, and that objects of different structures (e.g., error_dict vs error_list) are never treated as equal.
- When handling serialization and deserialization logic (e.g., for sessions, cookies, migrations), always validate, sanitize, and handle corrupted or malformed input gracefully; never assume that external data is valid and avoid propagating exceptions that would crash core application flows.
- When rewriting, generating, or transforming code (e.g., AST, SQL, or migrations), always take care to operate on canonical (fully normalized or de-aliased) representations; ensure that identifiers, aliases, and references are resolved correctly to avoid ambiguity, conflicts, or collisions.
- Do not assume that attributes, configuration values, or settings are always present, not-None, or have valid types; always check types and presence explicitly before applying operations (e.g., str, in, method calls).
- When optimizing or reducing operation sequences (such as in migration or data-processing optimizers), ensure the result preserves correct semantic ordering, idempotence, and does not inadvertently drop necessary intermediate operations.

## Slide 23 — (rule examples, slide body)

**Body (on-slide rules text):**
- Always propagate all contextual parameters (e.g., "using" for database, "request" for URL generation, scripting environment, or permission context) through layers of abstraction to avoid silent routing errors or implicit global fallback.
- When expanding or rewriting comprehensions, loops, or expression trees, do so only under conditions that preserve semantic equivalence — avoid transformation if filters, multiple generators, or side effects could alter behavior.
- When combining or deduplicating value lists in output generation, keep ordering, grouping, and deduplication idempotent and deterministic; always avoid introducing duplicate entries or unintended reordering that could change output semantics.
- Always log exceptions or error events at the point of exception handling — especially when silently catching exceptions intended for robustness (e.g., in signal dispatchers, hooks, or extensibility APIs) — to ensure issues are visible for debugging and monitoring.
- For any API that accepts or passes through arbitrary user input, configuration, or template values, always validate for correct types and formats and provide clear, actionable error or warning messages.
- When creating or rewriting objects that may contain non-standard or non-picklable values (e.g., dict_keys, custom iterables), normalize these into safe, serializable, and copyable types before deep copying or passing them further.
- Avoid in-place modification of arguments or cached properties that are global, thread-local, or context-dependent unless thread safety, request-safety, and correct per-request/per-thread value propagation is ensured.

## Slide 24 — Django only was up 20%!

**Notes:**
What if we only used one repo?

We did with Django, and got a 20% relative improvement.
Django is a good test case for this because it's a large, complex codebase with very particular conventions.
It has specific rules about how you do migrations, how querysets work, how signals fire, how deprecation warnings should behave.
An agent that's been told nothing about Django's conventions is going to keep tripping over the same things.
An agent that's been given rules derived from real Django failures is going to avoid those traps.

## Slide 25 — (Django rule examples, slide body)

**Body (on-slide rules text):**
- Make the smallest, most localized change that addresses the issue; modify the correct layer/entry-point (method/class) where the behavior is defined rather than adding wrappers or unrelated helpers.
- Mirror established patterns and conventions in the codebase (naming, logging style, repr/str formatting, id_for_label semantics, backend-specific overrides like as_sqlite()/as_oracle()) to maintain compatibility with existing tests and style.
- When changing error messages, include required placeholders and pass params so messages render exactly as expected; do not rephrase messages or change punctuation/quoting styles used across the codebase.
- Do not add demonstration scripts, debug files, or extraneous modules; only modify production code and, when appropriate, existing tests relevant to the change.
- Respect immutability and hashing semantics: if implementing __eq__, also implement a consistent __hash__ so that equal objects have equal hashes; avoid identity-based hashing for value-equal objects; for collections of errors, ignore ordering where appropriate and use stable, hashable representations.
- Prefer reusing existing helpers/utilities (e.g., HasKey, get_email_field_name(), deconstruct()) instead of reimplementing logic; when cloning complex objects (like Q), prefer deconstruct()/reconstruct over deepcopy to avoid copying unpickleable objects.

## Slide 26 — (Django rule examples, slide body)

**Body (on-slide rules text):**
- Normalize non-pickleable, iterator-like values (e.g., dict_keys, dict_values, dict_items) to concrete types during deconstruction/serialization paths; when reconstructing iterables from resolved lookup values, preserve the original container type and detect namedtuples via _make/_fields, unpacking with *values.
- For exec/evaluation contexts, provide the appropriate globals() (not an empty dict) to allow access to imports and module globals while executing dynamic code.
- When handling Q/combinator logic, support combining with conditional expressions (objects exposing conditional=True) by accepting and/or wrapping them; when cloning/combining with empty Q, reconstruct from deconstruct() rather than deepcopy; implement commutative behavior (e.g., __rand__/__ror__) where appropriate.
- For combined query operations, enforce unsupported operations early with clear errors (e.g., distinct() on UNION/INTERSECT/EXCEPT); propagate "empty" state to combined queries and short-circuit execution (e.g., raise EmptyResultSet) when appropriate; ensure .none() on combined queries returns no results.
- For database/backend-specific behavior, use the correct backend hooks and SQL helpers; ensure lookups distinguish between missing keys and explicit JSON nulls, following backend primitives (e.g., JSON_TYPE on SQLite, composite predicates on Oracle).
- When reordering operations (e.g., migrations), prefer adjusting generation order rather than bolting on complex dependencies; ensure operations that depend on synthesized fields (e.g., _order) are generated after AlterOrderWithRespectTo creates them.

## Slide 27 — (Django rule examples, slide body)

**Body (on-slide rules text):**
- Validate and normalize inputs early (e.g., expand user paths, absolutize, strip trailing path separators before os.path.basename) so downstream logic receives canonical values.
- Ensure subclass/instance checks for metaclasses honor inheritance of known subclasses and their subclasses (e.g., use issubclass against a tuple of supported subclasses) so custom subclasses pass framework checks.
- Keep repr/str outputs aligned with existing formatting (correct quoting and route/url_name formatting); when displaying wrapped callables (e.g., functools.partial), match project expectations for repr while preserving self.func unchanged (e.g., include repr(self.func) in __repr__ but compute view_name from the unwrapped underlying callable).
- Avoid broad behavior changes that alter public APIs or cached behavior beyond the scope of the fix; keep diffs minimal and targeted to the reported issue.
- For widget labeling, return None from id_for_label when the widget renders no labelable element; for subwidgets, prefer IDs supplied via attrs (e.g., ChoiceWidget.options) over reconstructed IDs.
- When extending token/hash generation with additional fields (e.g., email), use model APIs (e.g., get_email_field_name()), handle None safely, and preserve backward compatibility where required (e.g., accept legacy tokens).
- When adding logging around error-swallowing code paths (e.g., send_robust, session decoding fallbacks), use the project's logger name and format; include exc_info with the actual exception object; don't modify control flow beyond logging and returning safe defaults (e.g., on BadSignature/base64 errors, fall back to legacy decode and return an empty session if necessary).

## Slide 28 — (Django rule examples, slide body)

**Body (on-slide rules text):**
- For combined group-by/annotation generation, avoid ambiguous aliases; if an annotation alias collides with joined column names, group by the full expression instead of the alias.
- In ForeignKey assignment, when the related object's PK is set after assignment, update the FK field when its value is in field.empty_values (not just None) to reflect the related object's saved primary key.
- In Management/CLI code, ensure parsers are instantiated with the computed program name (prog) rather than relying on sys.argv; preserve consistent help/usage output across environments.
- For ordering across relationships, base comparisons on the final path component (e.g., pieces[-1]) and avoid injecting related model default ordering when ordering by pk or an explicit attribute/attname; preserve requested ASC/DESC.
- When validating model default PK configuration, do not warn on child models inheriting a parent_link OneToOneField primary key; only warn on truly auto-created PKs lacking explicit configuration.
- For form/field validation, include the offending value in invalid_choice errors via params (e.g., {'value': value}); for model instances, include a useful scalar (e.g., pk) in the message where applicable.

## Slide 29 — (Django rule examples, slide body)

**Body (on-slide rules text):**
- When serializing Enums in migrations, reference members by name (e.g., MyEnum['A']) rather than by value to avoid breakage from translated or changed values; preserve callables in migration state and only resolve at runtime where intended.
- To prevent duplicate rows introduced by joins in choice-restricting filters (e.g., limit_choices_to), prefer correlated subqueries with Exists/OuterRef over plain join-based filters; do not rely on distinct() as a workaround.
- For async-capable handlers (e.g., ASGI), provide async equivalents of sync methods (e.g., get_response_async) using sync_to_async; maintain thread safety (thread_sensitive=True) when interacting with Django internals or threadlocals.
- When comparing/ordering framework Field instances (e.g., for abstract model inheritance), include both creation_counter and model identity (app_label, model_name) in equality, ordering, and hashing to avoid collisions across models.
- In autoreload or filesystem scanning code, defensively handle OS/path resolution errors (e.g., ValueError due to embedded null bytes) by skipping problematic paths and logging at debug level instead of raising.

## Slide 30 — But why should I care?

**Notes:**
So we've seen a boost by training on SWE bench data for a single project, over training on lots of projects.
But why should you care? Your project isn't in SWE Bench.
No, but you do have your own version — your git history!
You could repeat this process on your history — use the GitHub issues, jira tickets, whatever, along with your accepted PRs and use that to optimize your claude.md file.

## Slide 31 — Won't this be overfitting?

**Notes:**
Yes! And you know what, that's ok. It overfits to your repo, which is fine.
You are not building a generic solution for everyone to use, you are specializing it for your own code.

## Slide 32 — Works for any coding agent.. Or any AI agent

**Notes:**
We're talking about claude here, but this works with any coding agent.
Or any agent! If you have a ground truth, and a way of checking the output of the agent, like the unit tests we used here, or your own evals, you can run the same prompt learning loop.

## Slide 33 — Demo

**Notes:**
Let's see this with a customer service agent using Phoenix, our free OSS tool. I'm using the cloud version but you can spin this up locally in a docker container.

## Slide 34 — You have the skills and the power!

**Notes:**
At Arize we are making it easier for you to, we've even added a skill to do prompt optimization, as well as a button in AX. That last demo was in Phoenix our OSS version, but if you use AX our enterprise version which has a nice free tier, you can do a one click prompt optimize.

This can take your traces and evals, even if you only have a few of them, and use these to optimize your prompts.
You can build a dataset of your traces, run evals, use the prompt optimizer skill inside your coding agent, and have it check the eval results and explanations, and use these to adjust the prompt, automatically iterate, then give you the final optimized prompt.

## Slide 35 — github.com/arize-ai/prompt-learning

**Notes:**
Get the code and a load of examples.

## Slide 36 — github.com/arize-ai/arize-skills

**Notes:**
Get the code and a load of examples.

## Slide 37 — Jim Bennett (sign-off / CTA)

**Body:**
Principal Developer Experience Engineer
@JimBobBennett
