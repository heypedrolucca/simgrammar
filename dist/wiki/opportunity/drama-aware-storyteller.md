# Drama-aware storyteller

*Opportunity* · `drama-aware-storyteller` · status: **asserted**

A storyteller that models characters' arcs and relationships, not only threat budgets, choosing authored incidents that create meaningful stakes for specific colonists.

| field | value |
|---|---|
| opportunity type | Mechanic upgrade |
| involves | [Storyteller director](../mechanic/storyteller-director.md), [Triggered event chains](../mechanic/triggered-event-chains.md), [Relationship values](../mechanic/relationship-values.md), [Memories and thoughts](../mechanic/memories-thoughts.md), [History chronicle](../mechanic/history-chronicle.md) |
| applies | [LLM game master and narrative director](../technique/llm-game-master.md), [Grammar-constrained decoding for valid game actions](../technique/constrained-decoding.md) |
| precedent | [RimWorld](../game/rimworld.md), [Crusader Kings III](../game/crusader-kings-3.md), [Frostpunk](../game/frostpunk.md), [This War of Mine](../game/this-war-of-mine.md) |
| novelty | 3 |
| feasibility | 4 |
| impact | 3 |
| horizon | Now |
| key risks | Players perceive arc-shaped events as rigged., Narrative scoring adds latency at incident time., Arcs can repeat across runs if scoring is too deterministic. |
| falsifiable signal | {'prediction': 'A colony sim or survival management game will ship an event director that uses a language model to evaluate narrative state when choosing authored events.', 'resolve_by': '2028-06-30', 'criteria': 'Developer documentation describing model-based narrative scoring in event selection.'} |
| priority *(computed)* | 3.318 |

## Summary

A storyteller that models characters' arcs and relationships, not only threat budgets, choosing authored incidents that create meaningful stakes for specific colonists.

## Thesis

RimWorld's storytellers select incidents mostly by threat budget and timing. They create tension but not arcs: they do not know that two colonists are estranged siblings or that the doctor is the colony's only hope. A model that reads relationship and memory state can score candidate incidents by narrative relevance while the incidents themselves stay authored and rules-bound, adding arc awareness without surrendering control to generation.

## Design Sketch

Each candidate incident from the authored deck is scored on threat budget plus a narrative score: which characters it involves, whether it resolves or escalates an open thread, and whether it pays off a setup. The chosen incident is logged with the narrative reason, readable in the chronicle.

## Key Risks

- Players perceive arc-shaped events as rigged.
- Narrative scoring adds latency at incident time.
- Arcs can repeat across runs if scoring is too deterministic.

## Validation Experiment

Add narrative scoring to an incident deck in a colony prototype; run blind playthroughs and ask players to recount their run a week later. Success: players recall more named characters and causal links with the narrative storyteller.

## Falsifiable signal

- **Prediction:** A colony sim or survival management game will ship an event director that uses a language model to evaluate narrative state when choosing authored events.
- **Resolve by:** 2028-06-30
- **Criteria:** Developer documentation describing model-based narrative scoring in event selection.

## Relations

**applies**

- [LLM game master and narrative director](../technique/llm-game-master.md)
- [Grammar-constrained decoding for valid game actions](../technique/constrained-decoding.md)

**involves**

- [Storyteller director](../mechanic/storyteller-director.md)
- [Triggered event chains](../mechanic/triggered-event-chains.md)
- [Relationship values](../mechanic/relationship-values.md)
- [Memories and thoughts](../mechanic/memories-thoughts.md)
- [History chronicle](../mechanic/history-chronicle.md)

**precedent**

- [RimWorld](../game/rimworld.md)
- [Crusader Kings III](../game/crusader-kings-3.md)
- [Frostpunk](../game/frostpunk.md)
- [This War of Mine](../game/this-war-of-mine.md)

---
Provenance: created in run `2026-10-24-synthesis`.
