# Aurora 4X

*Game* · `aurora-4x` · status: **sourced**

A free space 4X simulation by a single developer in which the player runs an interstellar empire through ship design from components, mineral mining, sensor-based detection, missile and beam combat, and named officers, with time advanced in steps from seconds to days.

| field | value |
|---|---|
| aliases | Aurora, C# Aurora |
| year | 2004 |
| developer | Steve Walmsley |
| platforms | PC |
| subgenre | 4X strategy |
| subgenre secondary | Space sim |
| sim domain | Cosmic / space, Military / conflict, Industrial / logistics |
| player role | Ruler / statesman |
| agency model | Direct unit control, Order queue |
| time model | Turn-based |
| sim scale | Interplanetary+ |
| fidelity | Systemic |
| perspective | Text / UI |
| win structure | Open sandbox |
| failure model | Soft / recoverable |
| narrative mode | Emergent |
| multiplayer | Single-player |
| modding | None |
| production tier | Hobbyist / free |
| agent count order | ~100 |
| emergence | 4 |
| influence | 2 |
| cluster *(computed)* | C01 |
| core count *(computed)* | 3 |
| mechanic count *(computed)* | 13 |

## Summary

A free space 4X simulation by a single developer in which the player runs an interstellar empire through ship design from components, mineral mining, sensor-based detection, missile and beam combat, and named officers, with time advanced in steps from seconds to days.

## Core Loop

survey bodies and jump points -> mine Trans-Newtonian minerals and build installations -> research components -> design ship classes -> build fleets and assign officers -> detect and fight with sensors, missiles, and beams -> colonize and expand

## Design Notes

Aurora began as a helper program for the Starfire board wargame and grew into a standalone simulation with no fixed goals. It exposes almost every subsystem as windows of numbers, from mineral accessibility to officer bonuses and ship maintenance. Time advances in player-chosen steps from 5 seconds to 30 days, so the same engine resolves both strategic expansion and individual missile salvos. The Visual Basic 6 original was superseded by a C# rewrite released in 2020.

## Relations

**uses**

- [Modular assembly](../mechanic/modular-assembly.md) (core): Ship classes are designed from researched components (engines, sensors, weapons, armor), and the player sets armor, speed, and range per class; weapons and sensors must themselves be researched and designed first.
- [Fog of war](../mechanic/fog-of-war.md) (core): Jump points and mineral deposits stay unknown until gravitational and geological survey sensors sweep each body or survey point, and other ships are known only within sensor detection range.
- [Deposit depletion](../mechanic/deposit-depletion.md) (core): Eleven Trans-Newtonian Elements sit in finite deposits on planets and asteroids, each with an accessibility rating from 0.1 to 1 that scales mining output; all construction consumes them.
- [Resource extraction](../mechanic/resource-extraction.md) (supporting): Mines on colonies and asteroid mining extract the minerals.
- [Tech tree](../mechanic/tech-tree.md) (supporting): Research labs are assigned to scientists with field specialties.
- [Agent skills](../mechanic/agent-skills.md) (supporting): Scientists, administrators, naval officers, and ground commanders gain bonuses and improve over time.
- [Habitat suitability](../mechanic/habitat-suitability.md) (supporting): Colony cost depends on a world's gravity, atmosphere, and temperature.
- [Planetary climate](../mechanic/planetary-climate.md) (supporting): Terraforming alters a world's atmosphere to lower its colony cost.
- [Procedural terrain](../mechanic/procedural-terrain.md) (supporting): Star systems are randomly generated or built from real star data.
- [Treasury and budget](../mechanic/budget-treasury.md) (supporting): Wealth comes from taxes and exports and is spent on construction, research, and maintenance.
- [Wear and breakdown](../mechanic/wear-breakdown.md) (supporting): Ships require maintenance support, which can be disabled in setup.
- [Turn structure](../mechanic/turn-structure.md) (supporting): The player chooses each time increment, from 5 seconds to 30 days, and the engine resolves movement, detection, combat, and production for it.
- [Real-world data feeds](../mechanic/real-world-data-feeds.md) (supporting): Star systems can be built from real star data instead of generated at random.

## Sources

- [Aurora (Giant Bomb wiki)](../source/src-giantbomb-2026-aurora.md)
- [Starfire](../source/src-wikipedia-starfire.md)
- [An Aurora, Sharpened in the Key of C](../source/src-metafilter-2020-aurora-csharp.md)

---
Provenance: created in run `2026-10-24-catalog-gi`.
