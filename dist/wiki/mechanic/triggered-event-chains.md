# Triggered event chains

*Mechanic* · `triggered-event-chains` · status: **sourced**

Authored event templates fire when state conditions hold, and their outcomes schedule follow-up events that chain into multi-step stories.

| field | value |
|---|---|
| aliases | scripted events, event chains, story events |
| family | Narrative & generation |
| substrate | Rule system, Stochastic events |
| math basis | Markov / stochastic processes, Computation theory |
| feedback | None |
| player interface | Choice / cards, Observation only |
| legibility | 3 |
| emergence potential | 3 |
| authoring cost | 5 |
| compute cost | 2 |
| tuning difficulty | 3 |
| ai leverage | 4 |
| maturity | Classic |
| core count *(computed)* | 2 |
| earliest game *(computed)* | [Princess Maker 2](../game/princess-maker-2.md) |
| earliest year *(computed)* | 1993 |
| prevalence *(computed)* | 17 |
| prevalence share *(computed)* | 0.098 |
| subgenre spread *(computed)* | 11 |
| technique count *(computed)* | 1 |
| technique exposure *(computed)* | 0.75 |

## Definition

Each template holds a trigger predicate over state, a selection weight or mean time to happen, an immediate effect block, options with effects, and calls that schedule follow-up events with delays. Hooks such as yearly pulses, births, or deaths evaluate eligible templates and fire them. In Crusader Kings III, events do not fire on their own: on_actions, decisions, or interactions call them; an on_action can fire a list of events, weighted random_events, or the first valid one; and trigger_event schedules a follow-up such as days = { 7 14 } later, so a chain carries saved scopes and flags across months. Europa Universalis IV and Stellaris use the same Paradox script family; Frostpunk and Banished use simpler condition-fired events. Unlike a storyteller director, which paces generic incidents, chains carry authored story state forward. Inputs: state predicates and flags. Outputs: effects, flags, and scheduled events.

## Player Experience

The simulation seems to notice what the player did. A rival's illness leads to a succession dispute, which leads to a war invitation. Players feel stories unfolding from their situation, learn to set up conditions for chains they want, and dread chains they recognize.

## Design Levers

- trigger specificity: broad pulses versus narrow state predicates
- weights, mean time to happen, and random delay ranges between links
- branching factor and how many chain steps carry state forward
- whether follow-ups re-check conditions so chains can fail when the world changes
- cooldowns and once-per-game flags that limit repetition

## Failure Modes

- Players see the same chains every playthrough once the event pool is exhausted.
- Chains ignore world changes made between links, producing contradictions such as an event about a ruler who has died.
- Broad iteration in frequent pulses (the CK3 modding wiki warns against every_living_character in pulse on_actions) causes late-game slowdown.
- Authored text quality caps depth, because each branch must be written by hand.

## Dynamics

- Chains link otherwise separate systems, such as health, inheritance, and war, into multi-year storylines.
- Overlapping chains on the same characters produce compound situations that no single template described.
- Modders extend event pools until mods conflict on shared hooks.

## Open Questions

- Can a language model write follow-up links conditioned on the actual state reached, keeping chains coherent with world changes?
- What fraction of authored chain content could be replaced by generated text while keeping effects hand-tuned?

## Backlinks (computed)

**affected by:** [LLM game master and narrative director](../technique/llm-game-master.md)

**involved in:** [Content-elastic event systems](../opportunity/content-elastic-events.md), [Drama-aware storyteller](../opportunity/drama-aware-storyteller.md), [Placement that tells stories](../opportunity/placement-that-tells-stories.md)

**used by:** [Contraband Police](../game/contraband-police.md), [Crusader Kings III](../game/crusader-kings-3.md), [Democracy 4](../game/democracy-4.md), [Europa Universalis IV](../game/europa-universalis-4.md), [Façade](../game/facade.md), [FTL: Faster Than Light](../game/ftl.md), [Game Dev Tycoon](../game/game-dev-tycoon.md), [Hearts of Iron IV](../game/hearts-of-iron-4.md), [Papers, Please](../game/papers-please.md), [Princess Maker 2](../game/princess-maker-2.md), [Rebel Inc.](../game/rebel-inc.md), [Reigns](../game/reigns.md), [Stellaris](../game/stellaris.md), [Surviving Mars](../game/surviving-mars.md), [Suzerain](../game/suzerain.md), [This War of Mine](../game/this-war-of-mine.md), [Whispers from the Star](../game/whispers-from-the-star.md)

## Sources

- [Event modding (Crusader Kings III)](../source/src-paradoxwikis-2026-ck3-event-modding.md)

---
Provenance: created in run `2026-10-24-taxonomy-m7`.
