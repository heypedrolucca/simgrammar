# Space Haven

*Game* · `space-haven` · status: **sourced**

A spaceship colony sim in which the player builds a ship tile by tile and keeps a crew with needs, moods, and relationships alive inside a tile-based simulation of oxygen, CO2, heat, and power.

| field | value |
|---|---|
| year | 2020 |
| year full release | 2026 |
| developer | Bugbyte |
| platforms | PC |
| subgenre | Colony sim |
| subgenre secondary | Space sim |
| sim domain | Social / interpersonal, Physical / mechanical, Cosmic / space |
| player role | Overseer |
| agency model | Zoning / placement, Order queue, Indirect incentive, Direct unit control |
| time model | Real-time with pause |
| sim scale | Household / crew |
| fidelity | Systemic |
| perspective | Top-down / side 2D |
| win structure | Open sandbox |
| failure model | Cascading collapse |
| narrative mode | Emergent |
| multiplayer | Single-player |
| modding | Content |
| production tier | Indie |
| agent count order | ~10 |
| emergence | 3 |
| influence | 1 |
| influenced by | [RimWorld](../game/rimworld.md), [Dwarf Fortress](../game/dwarf-fortress.md), [Oxygen Not Included](../game/oxygen-not-included.md) |
| cluster *(computed)* | C04 |
| core count *(computed)* | 4 |
| mechanic count *(computed)* | 15 |

## Summary

A spaceship colony sim in which the player builds a ship tile by tile and keeps a crew with needs, moods, and relationships alive inside a tile-based simulation of oxygen, CO2, heat, and power.

## Core Loop

build the ship tile by tile -> balance oxygen, CO2, temperature, and power -> crew work and meet needs -> jump through hyperspace to a new sector -> mine, salvage derelicts, trade, or fight factions -> grow the ship and crew

## Design Notes

Bugbyte describes it as combining RimWorld-style emergent storytelling with a tile-based gas simulation, and names RimWorld, Dwarf Fortress, Spacebase DF-9, and Oxygen Not Included as inspirations. The ship is both the base and the vehicle, so layout choices (a bed beside the ship core disrupts sleep) and life support are coupled to combat, where fire, smoke, gas, and hull breaches cascade through the same simulation. Early access began in May 2020 and 1.0 shipped in May 2026.

## Relations

**influenced by**

- [RimWorld](../game/rimworld.md)
- [Dwarf Fortress](../game/dwarf-fortress.md)
- [Oxygen Not Included](../game/oxygen-not-included.md)

**uses**

- [Fluid and gas simulation](../mechanic/fluid-gas-simulation.md) (core): Each tile holds gas quantities; life support modules produce oxygen and remove CO2, and hazardous gases from facilities, fires, or explosions spread until scrubbed or vented.
- [Building placement](../mechanic/free-placement.md) (core): Hull, walls, doors, and facilities are placed freely tile by tile to form the ship, which can be expanded or rebuilt at any time.
- [Needs decay](../mechanic/needs-decay.md) (core): Crew needs for food, sleep, comfort, safety, and friends drive mood, alongside conditions such as starvation or feeling unhygienic.
- [Mood and breakdowns](../mechanic/mood-breakdown.md) (core): Neglected crew suffer mental breaks ranging from starting fights to venting other crew into space.
- [Heat transfer](../mechanic/heat-transfer.md) (supporting): Thermal regulators keep compartments at comfortable temperatures.
- [Power grid](../mechanic/power-grid.md) (supporting): Power nodes distribute electricity across the ship.
- [Relationship values](../mechanic/relationship-values.md) (supporting): Crew relationships added in 2022.
- [Personality traits](../mechanic/personality-traits.md) (supporting)
- [Agent skills](../mechanic/agent-skills.md) (supporting)
- [Reputation](../mechanic/reputation.md) (supporting): Standing with pirates, slavers, merchants, cults, and android factions.
- [Resource extraction](../mechanic/resource-extraction.md) (supporting): Asteroids are mined for raw materials.
- [Production chains](../mechanic/production-chain.md) (supporting): Raw materials are refined into building materials.
- [Unit commands](../mechanic/unit-commands.md) (supporting): Crew are drafted and equipped for ground combat and away missions.
- [Fire spread](../mechanic/fire-spread.md) (supporting): Fire and smoke spread through damaged compartments.
- [Procedural terrain](../mechanic/procedural-terrain.md) (supporting): Each playthrough generates a new galaxy of sectors, stations, and ships.

## Sources

- [Space Haven](../source/src-wikipedia-space-haven.md)
- [Space Haven on Steam](../source/src-steam-2026-space-haven.md)
- [Space Haven](../source/src-bugbyte-2026-space-haven.md)

---
Provenance: created in run `2026-10-24-catalog-gb`.
