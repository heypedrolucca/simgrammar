# Specification programming games

*Opportunity* · `specification-programming-games` · status: **asserted**

Programming puzzles where an AI writes the code and the player writes the specification and tests, scored on how precisely the spec pins down correct behavior.

| field | value |
|---|---|
| opportunity type | New genre |
| involves | [Player programming](../mechanic/player-programming.md), [Comparative histograms](../mechanic/comparative-histograms.md), [Design performance rating](../mechanic/design-performance-rating.md), [Scenario objectives](../mechanic/scenario-objectives.md) |
| applies | [LLM-guided evolutionary program search](../technique/alphaevolve-algorithm-discovery.md), [Grammar-constrained decoding for valid game actions](../technique/constrained-decoding.md), [Automated generation of game rules and mechanics](../technique/automated-rule-generation.md) |
| precedent | [SpaceChem](../game/spacechem.md), [Opus Magnum](../game/opus-magnum.md), [Screeps](../game/screeps.md), [Bitburner](../game/bitburner.md), [The Farmer Was Replaced](../game/the-farmer-was-replaced.md) |
| novelty | 5 |
| feasibility | 4 |
| impact | 2 |
| horizon | Now |
| key risks | Niche audience., Model behavior changes over versions alter puzzle difficulty., Players may find being a reviewer less fun than being a builder. |
| falsifiable signal | {'prediction': 'A programming game will make specifying or testing AI-written code its core loop.', 'resolve_by': '2028-06-30', 'criteria': 'Title released after 2026-10-24 with at least 1,000 Steam user reviews; its Steam page describes players specifying, testing, or verifying AI-generated code as the main mechanic.'} |
| priority *(computed)* | 3.062 |

## Thesis

Zachtronics games and Screeps made writing code the play. Code generation changes what programming skill means: specifying behavior and catching wrong implementations. A genre built around writing specs and adversarial tests, with a model as an unreliable implementer, teaches the skill that now matters and has a natural scoring rule: how many plausible wrong programs your tests reject.

## Design Sketch

Each puzzle is a machine to control. The player writes a specification and test cases; a model generates implementations, some subtly wrong; the player's score counts wrong implementations caught, test cost, and spec length, plotted on histograms against other players.

## Key Risks

- Niche audience.
- Model behavior changes over versions alter puzzle difficulty.
- Players may find being a reviewer less fun than being a builder.

## Validation Experiment

Ship a 10-puzzle web prototype where a model generates candidate implementations with injected faults; measure completion rates and whether score distributions separate skilled from unskilled testers. Success: a stable leaderboard where test-writing skill predicts score.

## Falsifiable signal

- **Prediction:** A programming game will make specifying or testing AI-written code its core loop.
- **Resolve by:** 2028-06-30
- **Criteria:** Title released after 2026-10-24 with at least 1,000 Steam user reviews; its Steam page describes players specifying, testing, or verifying AI-generated code as the main mechanic.

## Relations

**applies**

- [LLM-guided evolutionary program search](../technique/alphaevolve-algorithm-discovery.md)
- [Grammar-constrained decoding for valid game actions](../technique/constrained-decoding.md)
- [Automated generation of game rules and mechanics](../technique/automated-rule-generation.md)

**involves**

- [Player programming](../mechanic/player-programming.md)
- [Comparative histograms](../mechanic/comparative-histograms.md)
- [Design performance rating](../mechanic/design-performance-rating.md)
- [Scenario objectives](../mechanic/scenario-objectives.md)

**precedent**

- [SpaceChem](../game/spacechem.md)
- [Opus Magnum](../game/opus-magnum.md)
- [Screeps](../game/screeps.md)
- [Bitburner](../game/bitburner.md)
- [The Farmer Was Replaced](../game/the-farmer-was-replaced.md)

---
Provenance: created in run `2026-10-24-synthesis`; reviewed in `2026-10-24-review-fixes`.
