# Content-elastic event systems

*Opportunity* · `content-elastic-events` · status: **asserted**

Remove the authoring ceiling on event chains, requests, and dilemmas by generating schema-constrained variants from designer templates and validating them against game state.

| field | value |
|---|---|
| opportunity type | Authoring tool |
| involves | [Triggered event chains](../mechanic/triggered-event-chains.md), [Villager requests](../mechanic/villager-requests.md), [Dilemma cards](../mechanic/dilemma-cards.md), [Procedural characters](../mechanic/procedural-characters.md), [Storyteller director](../mechanic/storyteller-director.md) |
| applies | [LLM game master and narrative director](../technique/llm-game-master.md), [Grammar-constrained decoding for valid game actions](../technique/constrained-decoding.md), [Agent-based automated playtesting and balancing](../technique/automated-playtesting.md) |
| precedent | [Crusader Kings III](../game/crusader-kings-3.md), [Stardew Valley](../game/stardew-valley.md), [Animal Crossing: New Horizons](../game/animal-crossing-new-horizons.md), [Reigns](../game/reigns.md), [Frostpunk](../game/frostpunk.md) |
| novelty | 3 |
| feasibility | 4 |
| impact | 3 |
| horizon | Now |
| falsifiable signal | {'prediction': 'A grand strategy, life sim, or narrative management game will ship runtime-generated events constrained by an event schema, disclosed on its Steam page.', 'resolve_by': '2027-12-31', 'criteria': 'Steam AI disclosure or developer documentation describing runtime-generated events in a released title.'} |
| priority *(computed)* | 3.318 |

## Summary

Remove the authoring ceiling on event chains, requests, and dilemmas by generating schema-constrained variants from designer templates and validating them against game state.

## Thesis

Event chains, villager requests, and dilemma cards are capped by writing budgets: players exhaust the deck and recognize repeats. Language models can generate variants, but unconstrained text breaks game logic. Templates with typed slots, constrained decoding into the event schema, and automated checks against preconditions let a small team ship a deck that keeps producing valid, state-aware events.

## Design Sketch

Designers write 200 event templates with preconditions, effects, and tone notes. At build time or runtime, a generator instantiates variants that reference specific characters, places, and history from the save, emits schema-valid events, and passes them through a validator that rejects anything whose effects violate invariants. Generated events are tagged so players can filter them.

## Key Risks

- Generated text quality below authored text lowers perceived quality.
- Disclosure and player backlash against AI-generated writing.
- Validation catches logic errors but not tone errors.

## Validation Experiment

Take 50 authored events from an existing design, generate 500 variants, have blind raters compare authored and generated events on quality, and run a validator on every variant. Success: generated events rated within 0.5 points of authored ones with 99 percent passing validation.

## Falsifiable signal

- **Prediction:** A grand strategy, life sim, or narrative management game will ship runtime-generated events constrained by an event schema, disclosed on its Steam page.
- **Resolve by:** 2027-12-31
- **Criteria:** Steam AI disclosure or developer documentation describing runtime-generated events in a released title.

## Relations

**applies**

- [LLM game master and narrative director](../technique/llm-game-master.md)
- [Grammar-constrained decoding for valid game actions](../technique/constrained-decoding.md)
- [Agent-based automated playtesting and balancing](../technique/automated-playtesting.md)

**involves**

- [Triggered event chains](../mechanic/triggered-event-chains.md)
- [Villager requests](../mechanic/villager-requests.md)
- [Dilemma cards](../mechanic/dilemma-cards.md)
- [Procedural characters](../mechanic/procedural-characters.md)
- [Storyteller director](../mechanic/storyteller-director.md)

**precedent**

- [Crusader Kings III](../game/crusader-kings-3.md)
- [Stardew Valley](../game/stardew-valley.md)
- [Animal Crossing: New Horizons](../game/animal-crossing-new-horizons.md)
- [Reigns](../game/reigns.md)
- [Frostpunk](../game/frostpunk.md)

---
Provenance: created in run `2026-10-24-synthesis`.
