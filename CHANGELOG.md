# Changelog

Contract, schema, vocabulary, and rubric changes. Data changes are tracked by run records in `log/runs/` and by git history.

## 1.1 (2026-10-25)

ADR-0004, contributor readiness.

- **Schema:** claim `quote` and `locator`; source `archived` (Wayback snapshot); `assertions` and `ratings` on games, mechanics, techniques, opportunities; game `store_ids` (steam, igdb, wikidata); opportunity `falsifiable_signal.resolution`; run `calibration` (raw blind scores).
- **Vocabulary:** new `prediction_outcome`; `time_model` and `modding` terms declare `requires_mechanic` / `allows_mechanic`; `modding` and `real-time-pausable` definitions sharpened.
- **Registry:** `contract_history` (E028 now accepts any listed version no newer than the current one) and `contribution` limits.
- **Rules:** E032 entity-assertion, E033 field-bound-mechanic, E034 evidence-quality, E035 independence, E036 calibration, E037 ratings, E038 prediction-resolution, E039 pr-scope; W105 source-archive, W106 prediction-overdue, W107 cluster-k-drift. E023 now checks GENERATED blocks only (dist/ is not committed); E029 cluster assertions require stable co-clustering and accept `cooccur.` and `cocluster.` references; E005 hint corrected.
- **Analysis:** cluster count from a stated stability rule (k = 24) over 1,000 hash-assigned subsamples, cluster stability, co-clustering, ARI and NMI against subgenre with a permutation null, `prevalence_rank`, per-mechanic family exposure ranking, prediction status, rater agreement, calibration results.
- **Build and CI:** dist/ gitignored; `build.py --out`; `make determinism` in CI; Pages workflow builds and publishes dist/ with the site; `sources` workflow (claim quotes, store ids, archive suggestions); PR scope check with DCO sign-off.
- **Docs:** CONTRIBUTING.md, CODE_OF_CONDUCT.md, `tasks/` briefs, issue forms, versioned calibration sets (`calibration/mechanics-v1.yaml`), CODEOWNERS for report, analysis, mechanics, opportunities, calibration.
- **After independent review (same release):** subsamples assigned by hash so adding a game redraws nothing; pair thresholds 0.9/0.1; tolerant W107; assertion references hardened (unknown right-hand refs, cluster labels, misspelled rank ids); E028 run dates checked against contract history; E034 judges wikis by url and binds snapshots to their url; E035 normalizes model ids; E037 requires the creator's score, verification raters, one rating per rater; E038 date rules for refuted and withdrawn; E039 binds operator to PR author and protects provenance, rating attribution, and quotes on new claims; `check_sources.py` searches full text before failing.

## 1.1 additions (2026-10-25, AI contributor pilot)

Fixes from the friction logs of the pilot agents that worked task issues end to end.

- **Schema:** `archived` also accepts the Wayback `id_` form (original bytes, for raw files and PDFs).
- **Tooling:** `check_sources.py --ids` scopes a check to the ids a task lists, and `--suggest-archive` prints each snapshot's date beside `accessed`. `pr_scope.py` checks the run file of a run-only PR and rejects a PR that adds a run and changes nothing. `make pr-check` stops if `git config github.user` is unset instead of comparing against `$USER`. `new.py run` prints the run id and says why `make check` is red until `method` is written. `check_sources.py` prints NOTHING CHECKED when every fetch failed, so an offline pass is not mistaken for a real one. Task issues for checkable briefs carry the exact `check_sources.py --ids` command.
- **Docs:** the archive brief says which snapshot to use (dates, raw files, paywalls), what to do without network access to archive.org, and that only sources actually archived are marked reviewed; the store-ids brief gives edition rules (later paid edition of the same game, series records, renamed developers), a fallback when Wikidata and IGDB cannot be opened, and marks only changed games reviewed; the source-claims brief runs as `maintenance` (quoting is not verification and needs no independence) and covers claims that overreach, bundle facts, state an absence, or cite a repository root, copies of DOI-only papers, locator forms, and agent fetch tools that return only fragments; AGENTS.md says a run that changes nothing is reported on the issue, not opened as a PR; the issue size rule names the 30-source limit; CONTRIBUTING.md says the sign-off is the operator's attestation.

## 1.0 (2026-10-23)

- Initial contract (CONTRACT.md), schemas for game, mechanic, technique, opportunity, source, run.
- Closed vocabularies in `vocab/`, edge types with single owners, anchored rubrics and composites.
- Validator rules E001-E031, W101-W104; deterministic build with projections to tables, graph, wiki, paper, and site.
- ADR-0001: repository architecture.
- ADR-0002 (pre-release hardening after an independent drift test): run `kind` with E031 (only taxonomy runs create mechanics; only verification runs verify), report assertions E029, style lint E030, broader literal-count lint E021 with citation exemption, placeholder lint across vocab and report prose, required GENERATED blocks, future-date checks for games and full source dates, run contract version check, W103 thin decompositions, source id pattern in schema, CODEOWNERS for contract surfaces.
- ADR-0003 (pre-release, after an independent content review): inverse-prevalence weighting and k=16 for game clustering, time-and-pacing excluded from white space, `field.` and `rank.` references in report assertions, schema rule that determinism-breaking techniques list determinism as a risk (`risks` up to six), W104 maturity-dates warning, prediction criteria with a post-2026-10-24 window and objective thresholds.

## 1.0 additions (2026-10-25)

- Website projection `dist/web/` (scripts/web.py), published by `.github/workflows/pages.yml`; styled with Register (vendored `web/register.css`, contract `web/DESIGN.md`).
- `{{viz:<name>}}` report token for interactive figures from scripts/viz.py (E019 covers unknown names); figures render as static SVG in paper.md.
- Dependencies pinned in requirements.txt; CI runs Python 3.13.
