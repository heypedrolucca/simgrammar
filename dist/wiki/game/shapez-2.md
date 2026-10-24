# shapez 2

*Game* · `shapez-2` · status: **sourced**

A combat-free factory automation game in which the player builds multi-level factories on space platforms that cut, rotate, stack, and paint layered geometric shapes and deliver them to a central Vortex to meet escalating milestone and operator goals.

| field | value |
|---|---|
| year | 2024 |
| year full release | 2026 |
| developer | tobspr Games |
| platforms | PC |
| subgenre | Factory / automation |
| sim domain | Computational / abstract, Industrial / logistics |
| player role | Engineer / designer |
| agency model | Zoning / placement, Programmatic |
| time model | Real-time |
| sim scale | Facility |
| fidelity | Abstract |
| perspective | Free 3D camera |
| win structure | Open sandbox |
| failure model | None |
| narrative mode | None |
| multiplayer | Single-player |
| modding | Scripting |
| production tier | Indie |
| agent count order | None |
| emergence | 2 |
| influence | 2 |
| influenced by |  |
| cluster *(computed)* | C02 |
| core count *(computed)* | 5 |
| mechanic count *(computed)* | 12 |

## Summary

A combat-free factory automation game in which the player builds multi-level factories on space platforms that cut, rotate, stack, and paint layered geometric shapes and deliver them to a central Vortex to meet escalating milestone and operator goals.

## Core Loop

read the requested shape code -> extract raw shapes from asteroids -> cut, rotate, stack, and paint on belts across levels -> deliver to the Vortex -> earn platform units and research -> build bigger platforms and train networks

## Design Notes

shapez 2 removes enemies, money, and building costs (all buildings are free) and keeps only the throughput puzzle: the product is an abstract shape of up to four layers of four quadrants, each part with a type and one of nine colors, written as a shape code. Parts obey a support rule (no floating pieces) and crystals shatter when cut from or stacked onto other crystals, so processing order is part of the puzzle. Space is the scarce resource: machines sit on space platforms whose count is limited by Platform Units earned from goals, and platforms connect through edge notches, space belts, and colored train lines whose routing is set per color at splitters. After the fixed milestones, operator goal lines grow exponentially in cost per level (for example 15,000 shapes at 18% growth), turning the endgame into scaling a design rather than designing a new one.

## Sources

- src-wikipedia-shapez-2
- src-steam-2026-shapez-2
- src-shapez2wiki-2026-shapes
- src-shapez2wiki-2026-trains
- src-shapez2wiki-2026-operator-level
- src-shapez2wiki-2026-space-platforms
- src-shapez2wiki-2026-modding

## Relations

**uses**

- [Production chains](../mechanic/production-chain.md) (core): Cutters, rotators, stackers, swappers, painters, pin pushers, and crystal generators each transform shapes by fixed rules; a target shape code implies a processing sequence the player must lay out.
- [Conveyor transport](../mechanic/conveyor-transport.md) (core): Belts, splitters, mergers, and lifts move shapes across three building levels per platform, and space belts carry them between platforms.
- [Tech tree](../mechanic/tech-tree.md) (core): Delivering each milestone's required shapes to the Vortex unlocks the next buildings and mechanics, such as fluids, painting, crystals, and trains; afterwards, operator goal lines with exponentially rising shape costs reward platform units, blueprint points, and research points.
- [Building placement](../mechanic/free-placement.md) (core): Space platforms in 20x20 chunks are the limited building surface, capped by Platform Units, with notches at chunk edges as the only connection points between platforms.
- [Blueprints](../mechanic/blueprints.md) (core): Copying and pasting factory sections costs Blueprint Points earned from goals, making repeated modules the intended way to scale.
- [Vertical layers](../mechanic/vertical-layers.md) (supporting): Each platform has three stacked building levels, and shapes carry up to four or five vertical layers that must be supported from below.
- [Vehicle routes and schedules](../mechanic/vehicle-route-scheduling.md) (supporting): Space trains load fixed-size packages at loader stations and unload at stops; each rail carries trains of several colors that take their own color's branch at splitters, and wagons hold one package per machine level.
- [Fluid pipe networks](../mechanic/fluid-pipe-network.md) (supporting): Pipes and space pipes carry fluids such as paint from asteroid pumps to painters, and fluid launchers move them across notches.
- [Signal circuits](../mechanic/signal-circuits.md) (supporting): Wire machines carry signals that read and control machines, and wireless senders and receivers pass signals across platform notches.
- [Resource extraction](../mechanic/resource-extraction.md) (supporting): Asteroid miners and pumps on platforms extract raw shape fields and fluid deposits from a procedurally generated world.
- [Modding API](../mechanic/modding-api.md) (supporting): Mods load natively through the ShapezShifter API and are distributed on Steam Workshop.
- [Megaproject sink](../mechanic/megaproject-sink.md) (supporting): After the fixed milestones, operator goal lines at the Vortex demand shapes in quantities that grow exponentially per level (for example 15,000 shapes at 18% growth), absorbing late-game output.

## Claims

- shapez 2 is the sequel to Shapez (2020, also known as shapez.io), which has no entry in this dataset, so the lineage is recorded here rather than as an influenced_by edge. *(confidence: high)* [[38](../source/src-wikipedia-shapez-2.md)]
- Early access began on 2024-08-15 and version 1.0 released on 2026-04-23. *(confidence: high)* [[38](../source/src-wikipedia-shapez-2.md), [39](../source/src-steam-2026-shapez-2.md)]

## Sources

- [Shapez 2](../source/src-wikipedia-shapez-2.md)
- [shapez 2](../source/src-steam-2026-shapez-2.md)
- [Shapes](../source/src-shapez2wiki-2026-shapes.md)
- [Trains](../source/src-shapez2wiki-2026-trains.md)
- [Operator Level](../source/src-shapez2wiki-2026-operator-level.md)
- [Space Platforms](../source/src-shapez2wiki-2026-space-platforms.md)
- [Modding](../source/src-shapez2wiki-2026-modding.md)

---
Provenance: created in run `2026-10-24-catalog-gh`.
