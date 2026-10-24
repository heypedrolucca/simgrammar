# Stats dashboards

*Mechanic* · `stats-dashboards` · status: **asserted**

Graphs and tables show the recorded history of simulation variables over selectable time windows.

| field | value |
|---|---|
| aliases | graphs, statistics screens, production statistics, reports |
| family | Information & legibility |
| substrate | UI layer, Aggregate stocks |
| math basis | Probability / statistics, System dynamics / ODEs |
| feedback | None |
| player interface | Observation only |
| legibility | 4 |
| emergence potential | 1 |
| authoring cost | 1 |
| compute cost | 2 |
| tuning difficulty | 1 |
| ai leverage | 3 |
| maturity | Classic |
| core count *(computed)* | 0 |
| earliest game *(computed)* | [SimLife](../game/simlife.md) |
| earliest year *(computed)* | 1992 |
| prevalence *(computed)* | 7 |
| prevalence share *(computed)* | 0.04 |
| subgenre spread *(computed)* | 5 |
| technique count *(computed)* | 1 |
| technique exposure *(computed)* | 0.3 |

## Definition

The game samples aggregate variables (population, money, production and consumption per item, prices, power, happiness, crime) at fixed intervals into time series and renders them as line graphs, stacked areas, tables, or pies. State owned: ring buffers of samples per variable, usually at several resolutions with older data downsampled. Update rule: each sample period, append the aggregate; when a buffer fills, merge samples into a coarser tier. The player picks variables, windows, and breakdowns. Canonical forms: the SimCity graphs window, Factorio production statistics per item across windows from seconds to hundreds of hours, Transport Tycoon company graphs for income and cargo delivered, Oxygen Not Included's daily colony report, and market price history in EVE Online and Victoria 3.

## Player Experience

The player steps back from the moment to read trends, confirm a change worked, and spot slow declines that no single frame reveals. A rising curve is its own reward.

## Design Levers

- which variables are logged and at what granularity (per item, per region, per agent class)
- time windows and downsampling scheme
- comparison views: against rivals, against previous periods, production versus consumption
- drill-down from an aggregate line to its contributors
- trend-based alerts and export of data

## Failure Modes

- Graphs show a decline but give no path to its cause.
- Coarse sampling hides short spikes or aliases oscillations into smooth lines.
- Dashboards buried in menus are never opened by most players.
- Long high-resolution histories bloat save files.

## Dynamics

- Visible production and consumption rates make ratio optimization possible, as in finding Factorio bottlenecks from item statistics.
- Trend reading supports experimental play: change one policy, watch the curve, revert.
- Public price histories in shared markets feed speculation and coordinated trading.

## Open Questions

- Can natural-language queries over logged history (why did power drop last winter) replace browsing graphs for most players?
- Which few variables, logged by default, let players diagnose most failures in a given genre?

## Backlinks (computed)

**affected by:** [LLM explanation of simulation state](../technique/llm-explanation-of-state.md)

**involved in:** [Bottleneck explainer for production networks](../opportunity/bottleneck-explainer.md), [Branch preview of policy futures](../opportunity/branch-preview-forecasts.md), [Calibrated serious simulations](../opportunity/calibrated-serious-sims.md), [Why-query over the simulation log](../opportunity/causal-why-query.md), [Explained delegation to AI managers](../opportunity/explained-delegation.md)

**used by:** [Democracy 4](../game/democracy-4.md), [Factorio](../game/factorio.md), [Football Manager](../game/football-manager.md), [Out of the Park Baseball](../game/out-of-the-park-baseball.md), [Plague Inc.](../game/plague-inc.md), [SimLife](../game/simlife.md), [Species: Artificial Life, Real Evolution](../game/species-alre.md)

---
Provenance: created in run `2026-10-24-taxonomy-m6`.
