# Dyson Sphere Program

*Game* · `dyson-sphere-program` · status: **sourced**

A 3D factory automation game in which the player's mech builds production lines on rotating planets, links star systems with logistics drones and warp vessels, and launches sails and rockets to assemble Dyson spheres around stars.

| field | value |
|---|---|
| year | 2021 |
| developer | Youthcat Studio |
| platforms | PC |
| subgenre | Factory / automation |
| subgenre secondary | Space sim |
| sim domain | Industrial / logistics, Cosmic / space, Military / conflict |
| player role | Engineer / designer |
| agency model | Direct avatar, Zoning / placement |
| time model | Real-time |
| sim scale | Interplanetary+ |
| fidelity | Stylized |
| perspective | Free 3D camera |
| win structure | Open sandbox |
| failure model | Soft / recoverable |
| narrative mode | None |
| multiplayer | Single-player |
| modding | Scripting |
| production tier | Indie |
| agent count order | ~1,000 |
| emergence | 2 |
| influence | 2 |
| influenced by | [Stellaris](../game/stellaris.md) |
| cluster *(computed)* | C02 |
| core count *(computed)* | 7 |
| mechanic count *(computed)* | 18 |

## Summary

A 3D factory automation game in which the player's mech builds production lines on rotating planets, links star systems with logistics drones and warp vessels, and launches sails and rockets to assemble Dyson spheres around stars.

## Core Loop

mine planetary veins -> belt ores through smelters and assemblers -> craft matrix cubes for research -> link planets and stars with logistics stations -> launch solar sails and carrier rockets -> Dyson sphere power feeds endgame production

## Design Notes

Dyson Sphere Program scales the factory puzzle from one map to a randomly generated cluster of stars: each planet is a rotating sphere whose day-night cycle affects solar power, and logistics stations match per-item local and remote supply and demand, sending up to 100 drones within a planet and 10 vessels between planets or, with Space Warpers, between stars. The Dyson sphere is a megastructure designed in a node-and-frame editor and built by ejecting solar sails (36 kW each at base, scaled by star luminosity, expiring after 5,400 seconds unless captured by a completed shell) and launching carrier rockets; ray receivers return its energy to planets or convert it to critical photons. The December 2023 Dark Fog update added hives and planetary bases whose threat rises with the player's power generation and combat, a variant of pollution-driven aggression. The developers drew inspiration from Stellaris, which included Dyson sphere construction. The sphere works as a goal sink that absorbs very large quantities of sails and rockets; no taxonomy mechanic covers such megaproject sinks, so this run proposed one.

## Sources

- src-wikipedia-dyson-sphere-program
- src-steam-2026-dyson-sphere-program
- src-dspwiki-2026-interstellar-logistics-station
- src-dspwiki-2026-dyson-sphere
- src-dspwiki-2026-dark-fog

## Relations

**influenced by**

- [Stellaris](../game/stellaris.md)

**uses**

- [Production chains](../mechanic/production-chain.md) (core): Smelters, assemblers, chemical plants, refineries, and particle colliders run fixed recipes that build up to six matrix cube types and Dyson sphere components; proliferator coating adds extra products or speed.
- [Conveyor transport](../mechanic/conveyor-transport.md) (core): Three belt tiers carry items between sorters and machines on a planetary grid that wraps around a sphere and narrows toward the poles.
- [Tech tree](../mechanic/tech-tree.md) (core): Labs in research mode consume matrix cubes in technology-specific mixes, all stacked labs working on the front of one queue; labs can instead be switched to manufacture matrices.
- [Resource extraction](../mechanic/resource-extraction.md) (core): Mining machines and advanced miners extract iron, copper, titanium, silicon, and rare veins whose distribution differs by planet and star type; pumps and oil extractors tap fluids.
- [Power grid](../mechanic/power-grid.md) (core): Wind, thermal, solar, fusion, and artificial-star generators feed tower-linked grids; logistics stations charge at 30 to 300 MW, and Dyson sphere energy reaches planets through ray receivers at 30% base efficiency.
- [Modular assembly](../mechanic/modular-assembly.md) (supporting): The Dyson sphere editor places nodes, frames, and shells on multiple orbital layers around a star, and its power output depends on built structure and absorbed sails.
- [Raid defense](../mechanic/raid-defense.md) (supporting): Dark Fog planetary bases and space hives attack factories and the player's mech, countered by turrets, energy shields, and player combat units.
- [Adaptive threat scaling](../mechanic/adaptive-threat-scaling.md) (supporting): Dark Fog threat accumulates from the player's power generation and from combat, bases and hives gain levels from experience, and aggressiveness settings scale attack sizes.
- [Procedural terrain](../mechanic/procedural-terrain.md) (supporting): Each seed generates a star cluster with star types, planet types, and mineral distributions, including neutron stars, white dwarfs, and black holes.
- [Blueprints](../mechanic/blueprints.md) (supporting): Layouts are saved and pasted as blueprints, and the mech's construction drones place them.
- [Day-night cycle](../mechanic/day-night-cycle.md) (supporting): Planets rotate around their axes and orbit their stars, so solar panel output varies with the local day.
- [Storage and buffers](../mechanic/storage-capacity.md) (supporting): Storage boxes, tanks, and per-slot capacity in logistics stations buffer flows between planets.
- [Hand crafting](../mechanic/hand-crafting.md) (supporting): The Icarus mech hand-crafts early buildings from inventory before assemblers take over.
- [Direct avatar control](../mechanic/direct-avatar.md) (supporting): The player flies the Icarus mech across planets and through space to build within its range.
- [Megaproject sink](../mechanic/megaproject-sink.md) (core): The Dyson sphere is designed in a node-and-frame editor and built from solar sails fired by EM-Rail Ejectors and frames carried by rockets; unabsorbed sails expire after 5,400 seconds, and the finished sphere's energy feeds endgame production.
- [Machine boosting](../mechanic/machine-boosting.md) (supporting): Proliferator coating on input items lets the consuming machine choose extra products or faster production.
- [Request-provider logistics](../mechanic/request-provider-logistics.md) (core): Logistics stations set each item slot to local or remote supply, demand, or storage and are paired automatically by priority; up to 100 drones per station haul within a planet and 10 vessels between planets, with range and minimum-load sliders.
- [Building placement](../mechanic/free-placement.md) (supporting)

## Backlinks (computed)

**precedent for:** [Generated recipe graphs](../opportunity/generated-recipe-graphs.md)

## Claims

- Dyson Sphere Program was still labeled Early Access on Steam when accessed in October 2026, so no full-release year is recorded. *(confidence: high)* [[17](../source/src-steam-2026-dyson-sphere-program.md)]
- Reviewers compare it favorably to Factorio and Satisfactory, but the cited source names only Stellaris as a design inspiration, so no Factorio influence edge is recorded. *(confidence: medium)* [[18](../source/src-wikipedia-dyson-sphere-program.md)]

## Sources

- [Dyson Sphere Program](../source/src-wikipedia-dyson-sphere-program.md)
- [Dyson Sphere Program](../source/src-steam-2026-dyson-sphere-program.md)
- [Interstellar Logistics Station](../source/src-dspwiki-2026-interstellar-logistics-station.md)
- [Dyson Sphere](../source/src-dspwiki-2026-dyson-sphere.md)
- [Dark Fog](../source/src-dspwiki-2026-dark-fog.md)

---
Provenance: created in run `2026-10-24-catalog-gh`; reviewed in `2026-10-24-review-fixes`.
