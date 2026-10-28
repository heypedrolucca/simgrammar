# Brief: calibrate, then add independent ratings

**Run kind:** `verification`. **Limit:** 10 records per PR.

**Who can take it:** an invited contributor (the repository's owner, a member, or a collaborator) whose operator is not the creator of the mechanics you rate. CI counts a `verification` run only from an invited author (E039), because independence (E035) rests on who the operator is. Not invited? Open a [Verification request](https://github.com/yoheinakajima/simgrammar/issues/new?template=verification.yml) to ask for an invitation, or for the check.

Every rubric score in the dataset so far comes from one model rater. Independent ratings turn those scores into measured agreement (`dist/analysis/rater-agreement.csv`).

1. **Calibrate first.** `python scripts/calibrate.py sheet > sheet.yaml` writes 20 frozen mechanics with their definitions and the rubric anchors, without stored scores. Score every row from the sheet alone, before you open `data/mechanics/` or the website. The reference scores are public, so nothing but your procedure keeps this blind; score once and record what you got. Then `python scripts/calibrate.py score sheet.yaml --write-run <run-id>` records your raw scores in the run file. The validator computes agreement from them; you need within-one agreement of at least 0.8 (E036). Below that, reread the anchors where you disagreed and recalibrate in a new run.
2. **Rate.** For each mechanic in the issue, add one `ratings` entry per scale you scored: `field`, `value` (an anchor level), `run` (your run), and a `rationale` naming the anchor text that matched and why the neighbouring anchors did not.
3. **Keep the stored value honest.** A field with ratings must include the original score as a rating from the creating run (E037). If it has none yet, add one first: the creating run's id, the score exactly as stored, and the rationale "original score" (CI accepts this one rating attributed to another run, and only unchanged). Then store the lower median of all ratings. One rater gives one rating per field; a second run by the same operator and model does not count as another rater.
4. Append your run to each record's `provenance.reviewed` (E039).
5. Changing a score on a calibration-set mechanic also changes the current set in `calibration/` and needs maintainer review. Leave those to the maintainer and say so in the PR.
