# Intent-level orders

*Opportunity* · `intent-level-orders` · status: **asserted**

Players state goals in plain language and the game compiles them into priorities, designations, and schedules, cutting micromanagement in colony and management sims.

| field | value |
|---|---|
| opportunity type | New mechanic |
| involves | [Work priorities](../mechanic/work-priorities.md), [Designation orders](../mechanic/designation-orders.md), [Daily schedules](../mechanic/daily-schedules.md), [Unit commands](../mechanic/unit-commands.md), [Natural-language interaction](../mechanic/natural-language-interaction.md), [Delegation to AI managers](../mechanic/delegation-to-ai.md) |
| applies | [Grammar-constrained decoding for valid game actions](../technique/constrained-decoding.md), [On-device small language models for characters](../technique/on-device-language-models.md), [LLM explanation of simulation state](../technique/llm-explanation-of-state.md) |
| precedent | [RimWorld](../game/rimworld.md), [Dwarf Fortress](../game/dwarf-fortress.md), [Oxygen Not Included](../game/oxygen-not-included.md), [Prison Architect](../game/prison-architect.md) |
| novelty | 3 |
| feasibility | 4 |
| impact | 3 |
| horizon | Now |
| key risks | Ambiguous intents compile to surprising rules., Hides the very systems some players enjoy mastering., Conflicting standing rules produce opaque behavior. |
| falsifiable signal | {'prediction': 'A released colony or management sim will let players issue standing natural-language orders that compile into its job and priority systems.', 'resolve_by': '2028-06-30', 'criteria': 'Patch notes, store page, or developer statement describing the feature in a shipped title or official expansion.'} |
| priority *(computed)* | 3.318 |

## Summary

Players state goals in plain language and the game compiles them into priorities, designations, and schedules, cutting micromanagement in colony and management sims.

## Thesis

Colony and management sims hit a micromanagement wall: the work-priority grid, stockpile filters, and schedules grow until play becomes clerical. Players think in intents ('keep the clinic staffed through winter', 'stop hauling during raids'). Constrained decoding can translate intents into the game's existing control primitives, and the result stays inspectable because it compiles into the same grids the player already understands.

## Design Sketch

An orders panel accepts sentences; each becomes a standing rule shown as a card with the exact priority changes, conditions, and expiry it compiled into. Rules can be edited in the classic UI. Conflicts between rules are flagged with an explanation.

## Key Risks

- Ambiguous intents compile to surprising rules.
- Hides the very systems some players enjoy mastering.
- Conflicting standing rules produce opaque behavior.

## Validation Experiment

Collect 200 player-stated intents from colony sim forums, compile them into a prototype's control primitives, and have players judge fidelity; measure clicks per in-game day with and without intents. Success: 80 percent judged faithful and a 30 percent drop in management clicks.

## Falsifiable signal

- **Prediction:** A released colony or management sim will let players issue standing natural-language orders that compile into its job and priority systems.
- **Resolve by:** 2028-06-30
- **Criteria:** Patch notes, store page, or developer statement describing the feature in a shipped title or official expansion.

## Relations

**applies**

- [Grammar-constrained decoding for valid game actions](../technique/constrained-decoding.md)
- [On-device small language models for characters](../technique/on-device-language-models.md)
- [LLM explanation of simulation state](../technique/llm-explanation-of-state.md)

**involves**

- [Work priorities](../mechanic/work-priorities.md)
- [Designation orders](../mechanic/designation-orders.md)
- [Daily schedules](../mechanic/daily-schedules.md)
- [Unit commands](../mechanic/unit-commands.md)
- [Natural-language interaction](../mechanic/natural-language-interaction.md)
- [Delegation to AI managers](../mechanic/delegation-to-ai.md)

**precedent**

- [RimWorld](../game/rimworld.md)
- [Dwarf Fortress](../game/dwarf-fortress.md)
- [Oxygen Not Included](../game/oxygen-not-included.md)
- [Prison Architect](../game/prison-architect.md)

---
Provenance: created in run `2026-10-24-synthesis`.
