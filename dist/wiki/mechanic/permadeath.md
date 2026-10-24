# Permadeath

*Mechanic* · `permadeath` · status: **sourced**

Death of agents or the avatar is permanent, and the save system prevents undoing it.

| field | value |
|---|---|
| aliases | permanent death, ironman, hardcore mode |
| family | Risk & failure |
| substrate | Rule system |
| math basis | Markov / stochastic processes, Utility / decision theory |
| feedback | Reinforcing (positive) |
| player interface | Observation only, Parameter |
| legibility | 5 |
| emergence potential | 3 |
| authoring cost | 1 |
| compute cost | 1 |
| tuning difficulty | 2 |
| ai leverage | 2 |
| maturity | Classic |
| core count *(computed)* | 3 |
| earliest game *(computed)* | [The Oregon Trail](../game/oregon-trail.md) |
| earliest year *(computed)* | 1971 |
| prevalence *(computed)* | 20 |
| prevalence share *(computed)* | 0.115 |
| subgenre spread *(computed)* | 9 |
| technique count *(computed)* | 0 |
| technique exposure *(computed)* | 0.0 |

## Definition

Death is an absorbing state: when an entity's health or survival condition fails, the entity and its accumulated state (skills, gear, relationships) are removed with no reload. Enforcement lives in the save system: Rogue deleted the save file when it was loaded, and modern ironman modes keep a single autosave. Two scopes exist. Avatar permadeath ends the run, as in FTL, which deletes the save when the ship is destroyed or all crew die, and Project Zomboid. Agent permadeath removes a member from a continuing game, as with RimWorld colonists, Dwarf Fortress dwarves, and Fire Emblem units. Softeners include FTL's clone bay, which revives crew with a skill penalty, downed states before death, and meta-progression that survives the run. Inputs: lethal events from combat, injury, or survival systems. Outputs: entity removal, run termination, or succession.

## Player Experience

Every risky decision carries weight because losses cannot be reversed. Players grow attached to named survivors, play more cautiously, and remember specific deaths as the turning points of a run. A loss late in a long run is the most memorable and the most frustrating moment the mechanic produces.

## Design Levers

- scope: avatar death ends the run versus agent death inside a continuing game
- save policy: single autosave, optional ironman toggle, or tolerated save scumming
- what persists past death: unlocks, world state, heirs, or nothing
- recovery tools such as revival with penalties, downed states, or medical rescue windows
- replacement cost and time for lost agents

## Failure Modes

- A single high-variance event ends a long run, which reads as unfair rather than consequential.
- Players back up and restore save files (save scumming), bypassing the design.
- Fear of loss pushes players into slow, repetitive grinding instead of bold play; Richard Bartle's analysis of virtual worlds notes most MMORPGs avoid permadeath for this and retention reasons.
- Bugs or connection drops that kill characters become catastrophic.

## Dynamics

- Losing a key specialist cascades: a colony without its only doctor loses more colonists to untreated wounds.
- Attachment plus loss produces the personal stories players share from colony sims and roguelikes.
- Combined with procedural generation, it makes each run a fresh attempt rather than a retry of the same state.

## Open Questions

- Does making lost agents persist as memories, ghosts, or chronicle entries change how much risk players accept?
- What variance profile of lethal events keeps permadeath consequential without making long runs feel like lotteries?

## Relations

**synergy**

- [Procedural characters](../mechanic/procedural-characters.md): Unique generated characters make permanent loss felt.

## Backlinks (computed)

**used by:** [Caves of Qud](../game/caves-of-qud.md), [Creatures](../game/creatures.md), [Don't Starve](../game/dont-starve.md), [FTL: Faster Than Light](../game/ftl.md), [Going Medieval](../game/going-medieval.md), [Kenshi](../game/kenshi.md), [Kerbal Space Program](../game/kerbal-space-program.md), [Noita](../game/noita.md), [The Oregon Trail](../game/oregon-trail.md), [Project Zomboid](../game/project-zomboid.md), [Reigns](../game/reigns.md), [RimWorld](../game/rimworld.md), [Seaman](../game/seaman.md), [Subnautica](../game/subnautica.md), [Tamagotchi](../game/tamagotchi.md), [The Long Dark](../game/the-long-dark.md), [The Sims](../game/the-sims.md), [The Sims 2](../game/the-sims-2.md), [The Sims 3](../game/the-sims-3.md), [This War of Mine](../game/this-war-of-mine.md)

## Sources

- [Permadeath](../source/src-wikipedia-permadeath.md)
- [FTL: Faster Than Light](../source/src-wikipedia-ftl.md)

---
Provenance: created in run `2026-10-24-taxonomy-m7`.
