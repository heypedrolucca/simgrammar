# Forecasting

*Mechanic* · `forecasting` · status: **asserted**

The interface projects future states such as resource runway, budget balance, or upcoming weather.

| field | value |
|---|---|
| aliases | projections, runway estimate, weather forecast |
| family | Information & legibility |
| substrate | UI layer, Aggregate stocks |
| math basis | System dynamics / ODEs, Probability / statistics |
| feedback | None |
| player interface | Observation only |
| legibility | 4 |
| emergence potential | 1 |
| authoring cost | 1 |
| compute cost | 1 |
| tuning difficulty | 2 |
| ai leverage | 4 |
| maturity | Established |
| core count *(computed)* | 0 |
| earliest game *(computed)* | [Lemonade Stand](../game/lemonade-stand.md) |
| earliest year *(computed)* | 1973 |
| prevalence *(computed)* | 2 |
| prevalence share *(computed)* | 0.011 |
| subgenre spread *(computed)* | 2 |
| technique count *(computed)* | 1 |
| technique exposure *(computed)* | 0.25 |

## Definition

A forecaster computes and displays projected future values of selected variables: days of food left at current consumption, next period's budget balance, upcoming temperature or storms, population trend, or completion time for a project. It owns a forecast method, a horizon, and a refresh interval, but no simulation state. Common methods are runway (stock divided by net rate), linear extrapolation of recent trend, lookup of an authored or pre-rolled schedule of events, and rarely a short simulated lookahead. Outputs are numbers, countdowns, or projected curves. Canonical forms: Frostpunk's temperature forecast showing cold snaps days ahead, budget projections in SimCity and Cities: Skylines, turns-to-complete counters in Civilization, and Football Manager's projected finances.

## Player Experience

Monitoring turns into planning. The player sees the cliff before reaching it and acts early, buffers to the forecast horizon, and feels dread when the projection is grim. Surprise drops; preparation becomes the challenge.

## Design Levers

- forecast method: runway, extrapolation, authored schedule, or simulated lookahead
- horizon length
- accuracy and whether uncertainty is shown, such as ranges or confidence that improves with upgrades
- which variables get forecasts
- whether forecasts include the player's queued actions
- proactive display versus on demand

## Failure Modes

- Linear extrapolation misleads when rates are seasonal or batched, producing false alarms or false security.
- Perfect forecasts of every threat turn disasters into checklists with no uncertainty.
- Noisy forecasts with no stated error teach players to ignore them.

## Dynamics

- Players stock to the forecast horizon, so a forecast that underestimates causes synchronized shortfalls.
- Forecast crises create preparation sprints followed by slack, a characteristic rhythm in survival city builders.
- Shifting play from reactive to anticipatory raises the value of storage and buffers relative to throughput.

## Open Questions

- Can a learned surrogate of the full simulation give cheap probabilistic forecasts (a 70 percent chance of famine within two seasons) for coupled systems that games now only extrapolate?
- What forecast accuracy maximizes preparation decisions without removing surprise?

## Backlinks (computed)

**affected by:** [Machine-learned weather forecasting](../technique/ml-weather-models.md)

**involved in:** [Branch preview of policy futures](../opportunity/branch-preview-forecasts.md), [Calibrated serious simulations](../opportunity/calibrated-serious-sims.md), [Generated dream and replay views](../opportunity/dream-replay-layer.md), [Event-sourced simulation runtime](../opportunity/event-sourced-sim-runtime.md), [Participatory planning sandboxes](../opportunity/participatory-planning-sandboxes.md), [Weather-coupled energy grids](../opportunity/weather-coupled-grids.md)

**used by:** [Lemonade Stand](../game/lemonade-stand.md), [This War of Mine](../game/this-war-of-mine.md)

---
Provenance: created in run `2026-10-24-taxonomy-m6`.
