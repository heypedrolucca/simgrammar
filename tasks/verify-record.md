# Brief: verify a sourced record

**Run kind:** `verification`. **Limit:** 10 records per PR.

**Who can take it:** an invited contributor (the repository's owner, a member, or a collaborator) whose operator is not the record's creator. CI counts a `verification` run only from an invited author (E039), because independence (E035) rests on who the operator is. Not invited? Open a [Verification request](https://github.com/yoheinakajima/simgrammar/issues/new?template=verification.yml) to ask for an invitation, or for the check.

`verified` is a claim that someone independent re-checked the record against its sources. The validator requires: a reviewed run of kind `verification`, dated on or after the creating run (E031); a different operator from the creating run, and a different model when both are agents (E035); and at least one cited source that is not an encyclopedia or wiki (E034).

1. Pick records at status `sourced` created by someone else (`git log` and `provenance.created` tell you who).
2. For each factual field (dates, developer, platforms, technique results, deployment) find the supporting passage in a cited source. Add a `quote` to each claim while you are there (`source-claims.md`).
3. Check the decomposition or the scores only against their rubric anchors and definitions; you are verifying evidence, not taste. Disagreeing with a score is a rating (`rate-scores.md`), not a verification failure.
4. If everything holds: set `status: verified` and append your run to `provenance.reviewed`. If a source contradicts a field: set `status: contested`, add a claim with `disputes` citing both sides, and do not overwrite the field (I13).
