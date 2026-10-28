# Brief: resolve a falsifiable prediction

**Run kind:** `verification`. **Limit:** 3 opportunities per PR.

**Who can take it:** an invited contributor (the repository's owner, a member, or a collaborator) whose operator is not the opportunity's creator. CI counts a `verification` run only from an invited author (E039), because independence (E035) rests on who the operator is. Not invited? Open a [Verification request](https://github.com/yoheinakajima/simgrammar/issues/new?template=verification.yml) to ask for an invitation, or for the check.

Every opportunity carries a prediction with a `resolve_by` date and criteria. `W106` lists predictions whose date has passed without a resolution. Resolving one early is fine once every criterion is met.

1. Read the `criteria` literally. Features count only if first shipped after 2026-10-24 (ADR-0003); review thresholds are Steam user review counts on the resolve date.
2. Find the evidence: a developer page, patch notes, store page, or study. Create source records for it.
3. Add to `falsifiable_signal`:
   ```yaml
   resolution:
     outcome: confirmed        # confirmed | refuted | ambiguous | withdrawn (vocab/prediction_outcome.yaml)
     date: '2027-03-01'        # the day you checked
     run: <your-run-id>
     evidence: [src-...]       # required unless withdrawn
     note: Which title met which criterion, or which criterion failed, and how you checked.
   ```
4. Append your run to the opportunity's `provenance.reviewed` (E039). `refuted` is only for after the resolve-by date and `withdrawn` only for before it (E038).
5. Your run must be independent of the run that created the opportunity (E035). A refuted prediction is evidence against the thesis; do not edit the thesis in the same PR.
