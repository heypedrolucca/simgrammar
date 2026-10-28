# ADR-0007: Rules from a three-lab review

- Status: accepted
- Date: 2026-10-25
- Contract version: 1.1. The rules tighten what a pull request may do. No merged record breaks: no record is `verified` yet.
- Run: `2026-10-25-gemini-review`

## Context

Three models from other labs reviewed the project cold:

- gemini-3.1-pro-preview reviewed the paper and the contribution documents.
- meta/muse-spark-1.3 got the same two prompts.
- openai/gpt-5.3-codex reviewed the scripts that enforce pull-request scope.

Each finding was checked against the data or the code before anything changed. The run lists what was accepted and what was rejected.

Two weaknesses mattered most, because each let a contributor turn an unchecked claim into a checked-looking one:

1. **Review credit could be borrowed.** A pull request could append an earlier merged run to a record's `provenance.reviewed`. Combined with a run-only pull request that touched one unrelated file, a verification run that verified nothing could be merged first and then credited later.
2. **`verified` left no trace of the work.** It required a verification run, independence, and a non-wiki source, but nothing showing that the verifier had read the sources.

## Decision

1. **E039: a PR credits only its own run.** A pull request may append only its own run to `provenance.reviewed`.
2. **E039: run-only PRs come from invited authors.** A pull request that adds a run but changes no records or sources is rejected, unless it also changes other files and its author is the owner, a member, or an invited collaborator.
3. **E039: verification comes from invited authors.** A `verification` run counts only when its author is the owner, a member, or an invited collaborator.
4. **E039: rewording a sourced claim needs evidence.** Changing the text of a claim on a `sourced` or `verified` record requires a new quote or a `disputes` entry (invariant I13).
5. **E039: deprecations stand alone.** A deprecation keeps the rest of the record unchanged.
6. **E039: sign-offs are real trailers.** A sign-off must be a `Signed-off-by` trailer line; the key is matched case-insensitively. The operator signs off after reading the diff, so agents commit without `-s`.
7. **E034: verified needs quotes.** `verified` requires a verbatim quote on every claim and key result.
8. **Rule text matches the code.** The E021 and E029 descriptions now say what the code does.

## Consequences

- Verifying a record now means quoting it. That is most of the work, and it is the work the independence rule was meant to secure.
- An invited contributor whose agent runs the same model as the creating run cannot verify that run's records (E035). `tasks/humans-with-agents.md` tells them to choose another model or check by hand.
- Self-declared operators and models, and public calibration answers, remain limits. ADR-0004 records them, and these rules narrow them without closing them.
