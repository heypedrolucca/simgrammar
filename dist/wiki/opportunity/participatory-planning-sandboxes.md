# Participatory planning sandboxes

*Opportunity* · `participatory-planning-sandboxes` · status: **asserted**

City-builder interfaces over calibrated urban models with simulated resident voices, used by communities and planners to explore tradeoffs together.

| field | value |
|---|---|
| opportunity type | Non-game transfer |
| involves | [Zoning](../mechanic/zoning.md), [Traffic congestion](../mechanic/traffic-congestion.md), [Citizen satisfaction](../mechanic/citizen-satisfaction.md), [Data overlays](../mechanic/data-overlays.md), [Forecasting](../mechanic/forecasting.md), [Treasury and budget](../mechanic/budget-treasury.md) |
| applies | [Simulation-based inference for calibrating simulators](../technique/simulation-based-inference.md), [LLM models of individual human choice](../technique/human-behavior-simulation-models.md), [Many-agent LLM societies](../technique/llm-agent-societies.md) |
| precedent | [Cities: Skylines](../game/cities-skylines.md), [SimCity](../game/simcity-1989.md), [Democracy 4](../game/democracy-4.md) |
| novelty | 3 |
| feasibility | 3 |
| impact | 3 |
| horizon | 1-2 years |
| key risks | Simulated residents substitute for real community input., False precision of calibrated models., Political misuse. |
| falsifiable signal | {'prediction': 'A city government will publicly use a game-style calibrated simulation with simulated resident feedback in a formal planning consultation.', 'resolve_by': '2029-12-31', 'criteria': 'Public planning document or press release naming the tool and its use in consultation.'} |
| priority *(computed)* | 3.0 |

## Thesis

Planners already use city builders to communicate, but the games' models are not calibrated to real cities and residents are absent. Simulation-based inference can calibrate traffic, housing, and service models to local data; language-model residents grounded in survey data can voice how proposals affect them. The city builder becomes a deliberation interface, with game mechanics (overlays, budgets, forecasts) as the legibility layer.

## Design Sketch

A neighborhood is loaded from open data. Participants zone, budget, and route transit; overlays show calibrated effects; simulated residents from different groups react, each tied to the data that grounds them. Sessions export a report of options and tradeoffs.

## Key Risks

- Simulated residents substitute for real community input.
- False precision of calibrated models.
- Political misuse.

## Validation Experiment

Calibrate a traffic and housing model for one district, run three participatory sessions, and measure whether participants' understanding of tradeoffs (pre and post quiz) improves relative to a slide presentation. Success: significant improvement with participants rating the tool as fair.

## Falsifiable signal

- **Prediction:** A city government will publicly use a game-style calibrated simulation with simulated resident feedback in a formal planning consultation.
- **Resolve by:** 2029-12-31
- **Criteria:** Public planning document or press release naming the tool and its use in consultation.

## Relations

**applies**

- [Simulation-based inference for calibrating simulators](../technique/simulation-based-inference.md)
- [LLM models of individual human choice](../technique/human-behavior-simulation-models.md)
- [Many-agent LLM societies](../technique/llm-agent-societies.md)

**involves**

- [Zoning](../mechanic/zoning.md)
- [Traffic congestion](../mechanic/traffic-congestion.md)
- [Citizen satisfaction](../mechanic/citizen-satisfaction.md)
- [Data overlays](../mechanic/data-overlays.md)
- [Forecasting](../mechanic/forecasting.md)
- [Treasury and budget](../mechanic/budget-treasury.md)

**precedent**

- [Cities: Skylines](../game/cities-skylines.md)
- [SimCity](../game/simcity-1989.md)
- [Democracy 4](../game/democracy-4.md)

---
Provenance: created in run `2026-10-24-synthesis`.
