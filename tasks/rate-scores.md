# Brief: calibrate, then add independent ratings

**Run kind:** `verification`. **Limit:** 10 records per PR.

Every rubric score in the dataset so far comes from one model rater. Independent ratings turn those scores into measured agreement (`dist/analysis/rater-agreement.csv`).

1. **Calibrate first, blind.** `python scripts/calibrate.py sheet > sheet.yaml` writes 20 frozen mechanics with their definitions and the rubric anchors, without stored scores. Score every row from the sheet alone, before you open `data/mechanics/` or the website. Then `python scripts/calibrate.py score sheet.yaml --write-run <run-id>` records your raw scores in the run file. The validator computes agreement from them; you need within-one agreement of at least 0.8 (E036). Below that, reread the anchors where you disagreed and recalibrate in a new run.
2. **Rate.** For each mechanic in the issue, add one `ratings` entry per scale you scored: `field`, `value` (an anchor level), `run` (your run), and a `rationale` naming the anchor text that matched and why the neighbouring anchors did not.
3. **Keep the stored value honest.** When a field has ratings, its stored value must be their lower median (E037). If the existing score has no rating entry, add one for it first with the creating run id and the rationale "original score", so the median includes it.
4. Changing a score on a calibration-set mechanic also changes `calibration/mechanics.yaml` and needs maintainer review. Leave those to the maintainer and say so in the PR.
