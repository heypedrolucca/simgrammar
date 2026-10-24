# Placement that tells stories

*Opportunity* · `placement-that-tells-stories` · status: **asserted**

City builders where where and what the player builds triggers specific, state-aware story events about the inhabitants of those buildings.

| field | value |
|---|---|
| opportunity type | New mechanic |
| involves | [Building placement](../mechanic/free-placement.md), [Triggered event chains](../mechanic/triggered-event-chains.md), [Adjacency scoring](../mechanic/adjacency-scoring.md), [Villager requests](../mechanic/villager-requests.md), [History chronicle](../mechanic/history-chronicle.md) |
| applies | [LLM game master and narrative director](../technique/llm-game-master.md), [Grammar-constrained decoding for valid game actions](../technique/constrained-decoding.md) |
| precedent | [Frostpunk](../game/frostpunk.md), [Manor Lords](../game/manor-lords.md), [Islanders](../game/islanders.md), [Crusader Kings III](../game/crusader-kings-3.md) |
| novelty | 4 |
| feasibility | 4 |
| impact | 3 |
| horizon | Now |
| key risks | Event frequency that interrupts building flow., Players gaming layout for favorable events., Generated vignettes repeat in tone. |
| falsifiable signal | {'prediction': 'A released city builder will advertise placement-triggered narrative events tied to specific inhabitants as a core feature.', 'resolve_by': '2028-12-31', 'criteria': 'Store page or developer material describing events triggered by player placement decisions and affecting named inhabitants.'} |
| priority *(computed)* | 3.514 |

## Thesis

Building placement and triggered event chains are both common but rarely combined: city builders tell almost no stories about what players build, and event-driven games rarely have spatial building. Events keyed to placement, adjacency, and the inhabitants affected (a tavern next to the temple, a mill that floods a farmer's field) give layout a narrative consequence. Constrained generation can instantiate such events from templates at scale while keeping effects inside the rules.

## Design Sketch

When the player places or removes a building, the event system evaluates templates against neighbors, inhabitants, and history; a few fire as short vignettes with choices whose effects are typed (happiness, faction, resource). The chronicle records them so a district accumulates a history.

## Key Risks

- Event frequency that interrupts building flow.
- Players gaming layout for favorable events.
- Generated vignettes repeat in tone.

## Validation Experiment

Add 50 placement-triggered event templates to a small city-builder prototype and measure whether players recall and describe their towns in narrative terms more often than a control. Success: a significant increase in narrative descriptions with no drop in building time.

## Falsifiable signal

- **Prediction:** A released city builder will advertise placement-triggered narrative events tied to specific inhabitants as a core feature.
- **Resolve by:** 2028-12-31
- **Criteria:** Store page or developer material describing events triggered by player placement decisions and affecting named inhabitants.

## Relations

**applies**

- [LLM game master and narrative director](../technique/llm-game-master.md)
- [Grammar-constrained decoding for valid game actions](../technique/constrained-decoding.md)

**involves**

- [Building placement](../mechanic/free-placement.md)
- [Triggered event chains](../mechanic/triggered-event-chains.md)
- [Adjacency scoring](../mechanic/adjacency-scoring.md)
- [Villager requests](../mechanic/villager-requests.md)
- [History chronicle](../mechanic/history-chronicle.md)

**precedent**

- [Frostpunk](../game/frostpunk.md)
- [Manor Lords](../game/manor-lords.md)
- [Islanders](../game/islanders.md)
- [Crusader Kings III](../game/crusader-kings-3.md)

---
Provenance: created in run `2026-10-24-synthesis`.
