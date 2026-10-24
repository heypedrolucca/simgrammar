# ADR-0002: Hardening after an independent drift test

- Status: accepted
- Date: 2026-10-24
- Contract version: 1.0 (pre-release; no published data depended on the earlier rules)

## Context

An independent agent, given only the repository, followed AGENTS.md to add a game and then tried eleven ways to introduce drift. Most were caught. Several were not: verification by any second run, literal counts phrased with an intervening word or as percentages, interpretive prose with no data check, deleted GENERATED markers, lowercase placeholders, future game years, full source dates, run contract versions, summaries with em-dashes or hype, mechanics created by non-taxonomy runs, and an unenforced source id convention. The documented finishing order (`make check` before `make build`) could never succeed after an edit.

## Decision

1. Runs carry a required `kind`. Only `taxonomy` and `bootstrap` runs create mechanics; only `verification` runs, distinct from and not earlier than the creating run, can justify `status: verified` (E031).
2. Report prose may pin interpretations with `{{assert:<stat or derived.id.field> <op> <value or reference>}}`; failures are E029.
3. E021 matches numbers and percentages up to one word before a dataset noun, exempting sentences that carry a citation (external figures) and headings.
4. E027 covers TODO, TBD, FIXME in any case, in data, runs, vocab, and report prose. E030 lints names and summaries for em-dashes, markdown, and hype words.
5. The build requires the GENERATED blocks it owns (E023); E024 checks game years and full source dates; E028 checks each run's contract version and reports unresolvable schemas instead of crashing.
6. Source ids are constrained by schema pattern (two forms). W103 warns on games with fewer than five mechanics.
7. Contract surfaces (`vocab/`, `schema/`, `scripts/`, `CONTRACT.md`, `AGENTS.md`) require maintainer review through CODEOWNERS, because the validator can enforce the contract but cannot judge changes to it.

## Consequences

Existing runs were assigned kinds by their purpose. The finishing order is now `make build` then `make check`. Remaining unenforced areas are judgment calls (whether a vocab change is justified, whether prose without numbers is accurate) and are handled by review.
