# ADR-0005: Fixes from the AI contributor pilot

- Status: accepted
- Date: 2026-10-25
- Contract version: 1.1 (no version change; the schema change only widens an accepted form)
- Runs: `2026-10-25-ai-pilot`. The pilots ran as `2026-10-25-store-ids-pilot`, `2026-10-25-source-claims-pilot`, `2026-10-25-catalog-game-pilot`, and an archive run that changed nothing and was not committed.

## Context

Before inviting outside contributors, four agents each took one task end to end: archive 25 sources, add verbatim quotes to 8 records, add store ids to 10 games, and catalogue 3 candidate games. Each worked from the docs alone, in its own worktree, and reported a friction log. The briefs were `archive-sources`, `source-claims`, `store-ids`, and `catalog-game`. Their findings fell into four groups.

1. **A catalog PR could break the report without changing a finding.** The §5.5 white-space table admitted mechanics used by at least 8% of games. `embodied-skill-control` sat exactly on the bar (14 of 174), so adding two games that lack it dropped it from the table. §5.5's assertion on that pair then failed as an "unknown reference" (E019), which hid the cause. ADR-0004 tested removing one game and adding one duplicate, not adding several new games.
2. **Checks that passed without checking.** `check_sources.py` printed only warnings when every fetch failed, which looked like a pass. `make pr-check` fell back to `$USER` when `git config github.user` was unset, which skipped the operator check silently. `pr_scope.py` skipped run-file checks when a PR changed no records.
3. **Brief gaps.** The briefs did not cover:
   - which Wayback snapshot to use, or raw files;
   - which store edition counts for a game first released free or on another platform;
   - what to do with claims that overreach, bundle facts, state an absence, or cite a repository root;
   - whether adding quotes is verification;
   - partial results;
   - runs that change nothing.

   `reviewed` was appended to records that were looked at but not re-checked.
4. **Agent web tools.** In the pilot sandbox, agents could not reach archive.org, Wikidata, or IGDB. The shell had no network. The fetch tool returned short verbatim fragments, so long quotes were stitched together. CI then found 26 of 32 quotes in the first pilot PR, warned on 5 unreachable pages, and failed 1. That one quote is on the rendered page but was not found in the page CI fetched.

## Decision

1. **Count threshold.** The white-space table admits mechanics used by at least a fixed number of games (`whitespace.min_prevalence_games: 14`, which was 8% of the catalog when fixed). Adding games can no longer drop a mechanic from the table. §5.5 cites the threshold with a stat token. Today's table is byte-identical. With the three pilot games added, and with up to 20 further duplicated games, every report assertion holds; under the old share rule the pilot games alone failed one.
2. **A row that leaves a table is a failed assertion, not a typo.** A `rank.` reference whose ids are all real records but are no longer in the table returns 9999. It fails as E029 with a message naming the cause. An id that is neither in the table nor a record is still a malformed reference (E019).
3. **Checks say when they checked nothing.**
   - `check_sources.py` prints NOTHING CHECKED when every fetch failed. A failed quote reports how far it matched and what the page has instead. Wikipedia-style footnote markers are ignored on both sides. `--ids` scopes a check to a task's records.
   - `pr_scope.py` checks the run file of a run-only PR and rejects a PR that adds a run and changes nothing.
   - `make pr-check` requires `git config github.user`.
4. **Briefs rewritten from the friction logs.**
   - `archive-sources`, `store-ids`, `source-claims`, and `catalog-game` give the missing rules.
   - Quoting runs as `maintenance`, because it needs no independence and changes no status.
   - `reviewed` marks only records actually re-checked.
   - A run that changes nothing is reported on its issue, not opened as a PR.
   - A data PR that moves a report finding is opened with the error quoted, and a maintainer rewrites the prose.
5. **Schema.** `archived` also accepts the Wayback `id_` form, for raw files and PDFs.

## Consequences

- A fixed count drifts the other way: as the catalog grows, 14 games becomes a smaller share and "common" loosens. Revisit when the catalog passes about 250 games, as with the cluster k.
- Report assertions can still fail on a genuine change: a pair that starts co-occurring, or a rank overtaken by a pair with a larger gap. That is their purpose. Contributors open such PRs with the error quoted, and the report is maintainer-owned (CODEOWNERS).
- Tasks that need archive.org, Wikidata, or IGDB suit invited humans, or agents running locally with network access. `tasks/humans-with-agents.md` says so.
- The one quote that failed in CI needs a reviewer to compare the fetched page with the rendered one. The new FAIL message is meant to make that comparison quick.
