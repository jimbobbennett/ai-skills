---
name: review-work
description: Review code changes against a multi-criteria checklist (spec compliance, test coverage, consistency, DRY, linter, runtime correctness), fix issues found, and re-run the review until it passes. Use when the user asks to "review your work", "review the code", "do a review pass", or similar.
---

# Review Work

Review the code changes you have made in this session against the checklist below. Make multiple passes. When a pass surfaces issues, fix them, then run the review again. Repeat until a full pass produces no findings.

## Review checklist

For every pass, evaluate the changes against each of these criteria:

1. **Spec compliance** — Do the changes implement what was originally asked? Re-read the original request/spec and verify every requirement is met. Flag missing pieces, scope creep, or anything that drifted from intent.
2. **Unit test coverage** — Are the new/changed code paths covered by unit tests? Are edge cases tested? Are the tests meaningful (asserting behavior, not just running code)?
3. **Consistency with the codebase** — Match the surrounding code's style, naming conventions, commenting patterns, and architectural choices. Don't introduce a new pattern when an existing one fits.
4. **Code reuse / DRY** — Is anything duplicated that should be extracted? Is there an existing helper, utility, or abstraction this code should use instead of reimplementing?
5. **Linter** — Run the project's linter(s). The code must pass with no new warnings or errors.
6. **Does the code work** — Run the tests. Run the build. Where applicable, exercise the feature (CLI invocation, dev server, etc.) to confirm runtime behavior matches the spec. Type-checking and tests passing is necessary but not sufficient — verify the feature actually does what it should.

## Process

1. Identify the scope of changes to review (the work done in this session, or the diff against the base branch — whichever matches the user's request).
2. Run a full pass over all changed code, evaluating against every checklist item. Collect findings.
3. If findings exist, fix them. Don't batch — fix and move on.
4. Re-run the full review. Continue until a complete pass produces zero findings.
5. Report the final result: confirm each checklist item passes, and summarize what was fixed during the review (if anything).

## Notes

- Don't stop after one pass. The first round of fixes can introduce new issues; the loop is the point.
- Run linters and tests with the project's actual commands (check `package.json` scripts, `Makefile`, `pyproject.toml`, etc.). Don't assume `npm test` works if the project uses something else.
- If a check is genuinely not applicable (e.g., a docs-only change has no linter target), say so explicitly rather than skipping silently.
- If you cannot verify runtime behavior (no way to exercise the feature in this environment), say so explicitly — don't claim "it works" based on tests alone.
