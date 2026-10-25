# Brief: resolve a falsifiable prediction

**Run kind:** `verification`. **Limit:** 3 opportunities per PR.

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
4. Your run must be independent of the run that created the opportunity (E035). A refuted prediction is evidence against the thesis; do not edit the thesis in the same PR.
