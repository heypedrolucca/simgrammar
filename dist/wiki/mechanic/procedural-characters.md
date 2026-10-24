# Procedural characters

*Mechanic* · `procedural-characters` · status: **sourced**

Characters are generated with names, backstories, traits, skills, and appearance sampled from constrained tables or grammars.

| field | value |
|---|---|
| aliases | character generation, pawn generation, procedural NPCs |
| family | World generation |
| substrate | Stochastic events, Rule system |
| math basis | Probability / statistics, Procedural noise / generative grammars, Combinatorics |
| feedback | None |
| player interface | Observation only, Parameter |
| legibility | 4 |
| emergence potential | 3 |
| authoring cost | 3 |
| compute cost | 1 |
| tuning difficulty | 2 |
| ai leverage | 4 |
| maturity | Classic |
| core count *(computed)* | 1 |
| earliest game *(computed)* | [Little Computer People](../game/little-computer-people.md) |
| earliest year *(computed)* | 1985 |
| prevalence *(computed)* | 6 |
| prevalence share *(computed)* | 0.034 |
| subgenre spread *(computed)* | 4 |
| technique count *(computed)* | 2 |
| technique exposure *(computed)* | 0.75 |

## Definition

A generator samples a character record from tables and rules: name from culture-specific lists or grammars, age, appearance parameters, traits under compatibility constraints, skills, and backstory fragments that modify the other fields. RimWorld gives every pawn a childhood backstory and, if generated at 20 or older, an adulthood backstory; each adds flat skill bonuses, disables or enables work types, and grants or forbids traits, and 25% of regular pawns and all faction leaders first try a fixed player-made bio before falling back to shuffled ones. Dwarf Fortress generates personalities, preferences, and appearance; The Sims and Crusader Kings generate townies and courtiers. Inputs: faction or culture, role requirements, random seed. Outputs: a character record consumed by needs, skills, and social systems.

## Player Experience

Each new arrival is a small unwrapping. Players read the backstory and traits, decide whether to recruit, and form a picture of the person that makes later events personal. Rerolling starting characters is itself a common ritual.

## Design Levers

- number of trait, skill, and backstory fragments, and their compatibility constraints
- how strongly backstory fragments change mechanics such as skills and disabled work
- share of fixed, hand-written or community-written characters versus fully generated ones
- name and appearance generators per culture
- player rerolls and edits at game start

## Failure Modes

- Small fragment pools repeat, and players recognize the same backstories across runs.
- Incompatible combinations produce incoherent characters, such as a pacifist whose backstory is soldier.
- Mechanically weak characters feel like dead weight, which drives heavy rerolling.

## Dynamics

- Disabled work types and traits force colony role planning around the people who arrive.
- Generated quirks seed conflicts once relationships and mood systems act on them.
- Community-submitted fixed characters appear across many players' games, creating shared recognizable figures.

## Open Questions

- Can language models generate backstories that stay consistent with the mechanical traits and skills they imply?
- How many independent fragments are needed before players stop recognizing repeats?

## Backlinks (computed)

**affected by:** [LLM game master and narrative director](../technique/llm-game-master.md), [Realtime speech-to-speech and expressive TTS for characters](../technique/realtime-voice-models.md)

**involved in:** [Content-elastic event systems](../opportunity/content-elastic-events.md), [Generated inspection shifts](../opportunity/generated-inspection-shifts.md), [Illustrated chronicles](../opportunity/illustrated-chronicles.md), [Local-first AI simulation games](../opportunity/local-first-ai-sims.md)

**used by:** [Contraband Police](../game/contraband-police.md), [Football Manager](../game/football-manager.md), [Little Computer People](../game/little-computer-people.md), [Out of the Park Baseball](../game/out-of-the-park-baseball.md), [Papers, Please](../game/papers-please.md), [RimWorld](../game/rimworld.md)

## Sources

- [Backstories](../source/src-rimworldwiki-2026-backstories.md)

---
Provenance: created in run `2026-10-24-taxonomy-m7`.
