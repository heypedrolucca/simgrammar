# Simulated history generation

*Mechanic* · `history-generation` · status: **sourced**

World generation simulates years to centuries of civilizations, figures, and events before play begins, producing the starting world.

| field | value |
|---|---|
| aliases | world history simulation, worldgen history, legends generation |
| family | World generation |
| substrate | Agent-based, Rule system, Stochastic events |
| math basis | Population dynamics, Markov / stochastic processes, Social network models |
| feedback | Both |
| player interface | Parameter, Observation only |
| legibility | 2 |
| emergence potential | 5 |
| authoring cost | 3 |
| compute cost | 4 |
| tuning difficulty | 4 |
| ai leverage | 4 |
| maturity | Established |
| core count *(computed)* | 2 |
| earliest game *(computed)* | [Dwarf Fortress](../game/dwarf-fortress.md) |
| earliest year *(computed)* | 2006 |
| prevalence *(computed)* | 2 |
| prevalence share *(computed)* | 0.011 |
| subgenre spread *(computed)* | 2 |
| technique count *(computed)* | 0 |
| technique exposure *(computed)* | 0.0 |

## Definition

After terrain and biomes exist, a coarse simulation runs the world forward for a chosen number of years: civilizations found sites, grow, migrate, trade, make war, and found religions, and a subset of individuals is tracked as historical figures with families, titles, kills, and relationships. The final state is the starting map for play, and the event log feeds a chronicle. In Dwarf Fortress the player sets history length (worlds of 1,000 or 10,000 years are possible), populations and deaths counters rise during generation, only part of each site's population becomes historical figures (nobles, megabeasts, villains, their families), and a cap with optional culling limits their total. Caves of Qud generates sultan histories and Crusader Kings seeds dynasties from authored history instead. Inputs: map, races, parameters. Outputs: sites, factions, figures, artifacts, and an event archive.

## Player Experience

The world feels older than the player. Ruins, feuds, and legendary artifacts have causes the player can look up, and players discover that the world they inherited contains specific grudges, heroes, and lost wars. Long generation times build anticipation.

## Design Levers

- history length in years
- number and type of civilizations and their behavior rules
- which individuals are tracked as historical figures and the cap on their count
- abstraction level of populations, battles, and trade during generation
- event types simulated (wars, migrations, religions, artifacts, monsters)
- how much of the generated history is revealed versus discoverable in play

## Failure Modes

- Long histories take a long time to generate and produce very large saves.
- Coarse rules can produce degenerate worlds, such as one civilization conquering everything or all civilizations dying out.
- History that never surfaces in play is invisible effort.

## Dynamics

- Generated grudges and alliances set the political situation the player starts in, so two seeds play differently.
- Historical figures and artifacts become quest targets, visitors, and threats during play.
- Players share notable generated histories as stories in their own right.

## Open Questions

- Can language models turn coarse simulated histories into readable myths and chronicles without contradicting the record?
- What is the cheapest history abstraction that still yields grudges and relationships players recognize in play?

## Relations

**synergy**

- [Procedural terrain](../mechanic/procedural-terrain.md): Generated terrain constrains where simulated civilizations settle, fight, and leave ruins.

## Backlinks (computed)

**involved in:** [Generated dream and replay views](../opportunity/dream-replay-layer.md), [Illustrated chronicles](../opportunity/illustrated-chronicles.md)

**used by:** [Caves of Qud](../game/caves-of-qud.md), [Dwarf Fortress](../game/dwarf-fortress.md)

## Sources

- [Dwarf Fortress](../source/src-wikipedia-dwarf-fortress.md)
- [Historical figure](../source/src-dfwiki-2026-historical-figure.md)
- [Legends](../source/src-dfwiki-2026-legends.md)

---
Provenance: created in run `2026-10-24-taxonomy-m7`; reviewed in `2026-10-24-review-fixes`.
