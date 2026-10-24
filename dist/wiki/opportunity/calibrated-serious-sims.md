# Calibrated serious simulations

*Opportunity* · `calibrated-serious-sims` · status: **asserted**

Use simulation-based inference and differentiable simulators to calibrate game-grade models of epidemics, traffic, and markets to real data, with published fit metrics.

| field | value |
|---|---|
| opportunity type | Non-game transfer |
| involves | [Contagion](../mechanic/contagion.md), [Traffic congestion](../mechanic/traffic-congestion.md), [Supply-demand pricing](../mechanic/supply-demand-pricing.md), [Forecasting](../mechanic/forecasting.md), [Stats dashboards](../mechanic/stats-dashboards.md) |
| applies | [Simulation-based inference for calibrating simulators](../technique/simulation-based-inference.md), [Differentiable simulation](../technique/differentiable-simulation.md), [Massively parallel GPU simulation](../technique/massively-parallel-simulation.md) |
| precedent | [Plague Inc.](../game/plague-inc.md), [Rebel Inc.](../game/rebel-inc.md), [Cities: Skylines](../game/cities-skylines.md), [Capitalism](../game/capitalism.md) |
| novelty | 3 |
| feasibility | 4 |
| impact | 2 |
| horizon | 1-2 years |
| key risks | Users over-trust calibrated outputs., Data availability limits domains., Calibration may reduce play value. |
| falsifiable signal | {'prediction': 'A serious-game or educational simulation will publish posterior-calibrated parameters with fit metrics as part of its release.', 'resolve_by': '2028-12-31', 'criteria': 'Release notes or paper accompanying a playable simulation that reports calibration method and fit.'} |
| priority *(computed)* | 2.764 |

## Summary

Use simulation-based inference and differentiable simulators to calibrate game-grade models of epidemics, traffic, and markets to real data, with published fit metrics.

## Thesis

Plague Inc. and Rebel Inc. are used in classrooms and briefings despite stylized models. Simulation-based inference and differentiable simulation make it practical to fit agent-based and compartment models to observed data and quantify uncertainty. Shipping calibrated parameter sets with published fit metrics lets game interfaces carry real insight while keeping play.

## Design Sketch

A contagion sim offers a 'calibrated scenario' mode where parameters come from posterior distributions fitted to historical outbreaks. Outcomes show credible intervals; a fit report explains what data the model matches and where it is unreliable.

## Key Risks

- Users over-trust calibrated outputs.
- Data availability limits domains.
- Calibration may reduce play value.

## Validation Experiment

Fit a game-grade SIR network model to a public historical outbreak with simulation-based inference and report posterior predictive coverage. Success: 90 percent interval coverage on held-out weeks.

## Falsifiable signal

- **Prediction:** A serious-game or educational simulation will publish posterior-calibrated parameters with fit metrics as part of its release.
- **Resolve by:** 2028-12-31
- **Criteria:** Release notes or paper accompanying a playable simulation that reports calibration method and fit.

## Relations

**applies**

- [Simulation-based inference for calibrating simulators](../technique/simulation-based-inference.md)
- [Differentiable simulation](../technique/differentiable-simulation.md)
- [Massively parallel GPU simulation](../technique/massively-parallel-simulation.md)

**involves**

- [Contagion](../mechanic/contagion.md)
- [Traffic congestion](../mechanic/traffic-congestion.md)
- [Supply-demand pricing](../mechanic/supply-demand-pricing.md)
- [Forecasting](../mechanic/forecasting.md)
- [Stats dashboards](../mechanic/stats-dashboards.md)

**precedent**

- [Plague Inc.](../game/plague-inc.md)
- [Rebel Inc.](../game/rebel-inc.md)
- [Cities: Skylines](../game/cities-skylines.md)
- [Capitalism](../game/capitalism.md)

---
Provenance: created in run `2026-10-24-synthesis`.
