# Human-calibrated customers

*Opportunity* · `human-calibrated-customers` · status: **asserted**

Replace hand-tuned customer and crowd preference curves with models that predict human choices, so tycoon markets respond like real populations.

| field | value |
|---|---|
| opportunity type | Mechanic upgrade |
| involves | [Customer value choice](../mechanic/customer-value-choice.md), [Crowd preferences](../mechanic/crowd-preferences.md), [Product development](../mechanic/product-development.md), [Supply-demand pricing](../mechanic/supply-demand-pricing.md) |
| applies | [LLM models of individual human choice](../technique/human-behavior-simulation-models.md), [Simulation-based inference for calibrating simulators](../technique/simulation-based-inference.md) |
| precedent | [RollerCoaster Tycoon](../game/rollercoaster-tycoon.md), [Planet Coaster](../game/planet-coaster.md), [Game Dev Tycoon](../game/game-dev-tycoon.md), [Big Ambitions](../game/big-ambitions.md) |
| novelty | 4 |
| feasibility | 3 |
| impact | 3 |
| horizon | 1-2 years |
| falsifiable signal | {'prediction': 'A commercial management or tycoon game will state that its customer or citizen preferences were derived from a learned model of human behavior.', 'resolve_by': '2028-12-31', 'criteria': 'Developer blog, talk, or store text attributing in-game demand or preference parameters to a behavioral or language model.'} |
| priority *(computed)* | 3.178 |

## Thesis

Customer behavior in management games is a set of hand-tuned curves: price tolerance, ride intensity preference, satisfaction decay. Research in 2024 and 2025 showed language-model agents and choice models trained on large behavioral datasets predicting individual human responses with useful accuracy. Using such models to generate preference distributions, offline, gives tycoon games demand that behaves like real segments and lets players learn transferable intuitions. The same machinery serves product and policy research outside games.

## Design Sketch

Guest archetypes are generated offline from a human-behavior model conditioned on demographics; each archetype yields compact preference parameters the runtime uses. Players see segment-level reasoning ('families find this ride too intense for the price'). A sandbox mode lets designers test offerings against segments.

## Key Risks

- Models encode demographic stereotypes that are offensive or wrong.
- Calibration to real data may make the game less fun than hand-tuned curves.
- Claims of realism invite scrutiny the model cannot survive.

## Validation Experiment

Generate preference parameters for a theme-park prototype from a behavior model, then compare predicted segment choices with a small real survey (n>=300) on the same priced options. Success: rank correlation above 0.6 between predicted and surveyed choices, and playtesters rate guest behavior as more plausible than the hand-tuned baseline.

## Falsifiable signal

- **Prediction:** A commercial management or tycoon game will state that its customer or citizen preferences were derived from a learned model of human behavior.
- **Resolve by:** 2028-12-31
- **Criteria:** Developer blog, talk, or store text attributing in-game demand or preference parameters to a behavioral or language model.

## Relations

**applies**

- [LLM models of individual human choice](../technique/human-behavior-simulation-models.md)
- [Simulation-based inference for calibrating simulators](../technique/simulation-based-inference.md)

**involves**

- [Customer value choice](../mechanic/customer-value-choice.md)
- [Crowd preferences](../mechanic/crowd-preferences.md)
- [Product development](../mechanic/product-development.md)
- [Supply-demand pricing](../mechanic/supply-demand-pricing.md)

**precedent**

- [RollerCoaster Tycoon](../game/rollercoaster-tycoon.md)
- [Planet Coaster](../game/planet-coaster.md)
- [Game Dev Tycoon](../game/game-dev-tycoon.md)
- [Big Ambitions](../game/big-ambitions.md)

---
Provenance: created in run `2026-10-24-synthesis`.
