## 11. Predictions and research agenda

Every opportunity carries a falsifiable prediction with a resolve-by date and criteria a stranger could check. The first resolves on {{stat:first_prediction_resolves}}. Because predictions are data, resolving one is a pull request: a verification run by a different operator (and model, for agents) adds a `resolution` with its outcome and evidence to the prediction (`tasks/resolve-prediction.md`), and the table, report, and site update. {{stat:n_predictions_open}} of {{stat:n_predictions}} predictions are open.

{{viz:prediction-timeline}}

{{table:predictions}}

### 11.1 Agenda

1. **Instrument a simulation for explanation.** Build the event log with cause links that why-queries, branch previews, and chronicles all need, and measure explanation faithfulness against human audit.
2. **Measure legibility in players, not only in rubrics.** The legibility and emergence scores here are judgments by a single model rater; a shared protocol for measuring how quickly players form correct causal models would let designers compare mechanics empirically.
3. **Connect techniques to the economic core.** Resource and production mechanics are the most used family in the catalog and, per mechanic, among the least targeted by current techniques, and logistics mechanics fare no better (§8.2).{{assert:most_used_family == Resources & production}}{{assert:rank.family-mean-exposure.resources-production >= 16}}{{assert:rank.family-mean-exposure.logistics-networks >= 16}} Balance search, recipe generation, and bottleneck explanation are tractable first steps.
4. **Separate authoritative and generated layers.** Develop and benchmark architectures where learned models render, narrate, or propose, and symbolic state decides.
5. **Extend the dataset.** Add mobile and non-English simulation traditions, score mechanics with a second, calibrated rater (`calibration/`, `tasks/rate-scores.md`), resolve the verification queue, and record design tensions with evidence from postmortems.

### 11.2 How to extend this report

The report is generated. To add a game, mechanic, technique, or opportunity, follow `AGENTS.md`; tables, counts, figures, rankings, and this section's prediction list update on the next build. To change an argument, edit the prose in `report/src/`; every dataset number in it is a token, so the text cannot fall out of date with the data.
