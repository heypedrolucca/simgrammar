# Branch preview of policy futures

*Opportunity* · `branch-preview-forecasts` · status: **asserted**

Fork the simulation in the background and show the player likely futures of a decision before committing, using parallel or surrogate simulation.

| field | value |
|---|---|
| opportunity type | New mechanic |
| involves | [Forecasting](../mechanic/forecasting.md), [Policy toggles](../mechanic/policy-toggles.md), [Data overlays](../mechanic/data-overlays.md), [Stats dashboards](../mechanic/stats-dashboards.md), [Pause and speed control](../mechanic/variable-speed.md) |
| applies | [Massively parallel GPU simulation](../technique/massively-parallel-simulation.md), [Graph network simulators and neural operators](../technique/graph-network-simulators.md), [Differentiable simulation](../technique/differentiable-simulation.md) |
| precedent | [Frostpunk](../game/frostpunk.md), [Democracy 4](../game/democracy-4.md), [Surviving Mars](../game/surviving-mars.md) |
| novelty | 4 |
| feasibility | 4 |
| impact | 4 |
| horizon | 1-2 years |
| falsifiable signal | {'prediction': "At least one commercial city builder, colony sim, or grand strategy game will ship a feature that simulates multiple stochastic futures of the player's current state before a decision.", 'resolve_by': '2028-06-30', 'criteria': 'Store page, patch notes, or developer talk describing multi-run forward simulation of the live game state shown to players.'} |
| priority *(computed)* | 4.0 |

## Thesis

Forecasting in shipped games is shallow: a runway counter, a weather icon, a predicted approval delta. Accelerated and learned simulators make it cheap to run many short futures of the actual game state. Showing a distribution of outcomes for a pending law, budget, or layout change turns opaque coupling into a visible tradeoff and makes long feedback delays playable. Deterministic, event-sourced simulations can fork from any tick, so the preview runs the real rules rather than a hand-built predictor.

## Design Sketch

Before enacting a policy the player opens Preview: the game forks 32 to 256 copies from the current tick with stochastic seeds, fast-forwards each one in-game year on spare cores (or a learned surrogate), and shows fan charts for key indicators plus the two most divergent futures as short replays. Preview costs an in-game resource so it remains a decision.

## Key Risks

- Previews reveal hidden randomness and can make play feel solved.
- Simulations with large state may not fork cheaply on consumer hardware.
- Surrogate predictions that disagree with the real run break trust.

## Validation Experiment

Take a deterministic city or colony prototype, implement state snapshot plus N-way fork, and measure fork-and-simulate cost for one in-game year at mid-game scale. Playtest with preview off and on; measure decision regret (outcome versus best available) and session length. Success: preview of 64 branches under 5 seconds on a mid-range PC and a measurable drop in regret without lower engagement.

## Falsifiable signal

- **Prediction:** At least one commercial city builder, colony sim, or grand strategy game will ship a feature that simulates multiple stochastic futures of the player's current state before a decision.
- **Resolve by:** 2028-06-30
- **Criteria:** Store page, patch notes, or developer talk describing multi-run forward simulation of the live game state shown to players.

## Relations

**applies**

- [Massively parallel GPU simulation](../technique/massively-parallel-simulation.md)
- [Graph network simulators and neural operators](../technique/graph-network-simulators.md)
- [Differentiable simulation](../technique/differentiable-simulation.md)

**involves**

- [Forecasting](../mechanic/forecasting.md)
- [Policy toggles](../mechanic/policy-toggles.md)
- [Data overlays](../mechanic/data-overlays.md)
- [Stats dashboards](../mechanic/stats-dashboards.md)
- [Pause and speed control](../mechanic/variable-speed.md)

**precedent**

- [Frostpunk](../game/frostpunk.md)
- [Democracy 4](../game/democracy-4.md)
- [Surviving Mars](../game/surviving-mars.md)

---
Provenance: created in run `2026-10-24-synthesis`.
