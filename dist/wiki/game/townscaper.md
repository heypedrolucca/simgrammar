# Townscaper

*Game* · `townscaper` · status: **sourced**

A town-building toy in which clicking colored blocks onto an irregular grid lets a wave function collapse solver assemble houses, arches, stairways, bridges, and gardens, with no goals or resources.

| field | value |
|---|---|
| year | 2020 |
| year full release | 2021 |
| developer | Oskar Stålberg |
| platforms | PC, Console, Handheld, Mobile, Web |
| subgenre | City builder |
| sim domain | Urban |
| player role | Engineer / designer |
| agency model | Zoning / placement |
| time model | Turn-based |
| sim scale | Settlement |
| fidelity | Abstract |
| perspective | Free 3D camera |
| win structure | Open sandbox |
| failure model | None |
| narrative mode | None |
| multiplayer | Single-player |
| modding | None |
| production tier | Indie |
| agent count order | None |
| emergence | 2 |
| influence | 2 |
| boundary case | True |
| cluster *(computed)* | C03 |
| core count *(computed)* | 1 |
| mechanic count *(computed)* | 3 |

## Summary

A town-building toy in which clicking colored blocks onto an irregular grid lets a wave function collapse solver assemble houses, arches, stairways, bridges, and gardens, with no goals or resources.

## Core Loop

click to add or remove a colored block on the irregular grid -> the solver picks modules for that cell and its neighbors -> arches, stairs, roofs, and gardens appear -> keep editing

## Design Notes

The grid is a subdivided, jittered hex grid of irregular quads, and each edit triggers a real-time wave function collapse that narrows the valid corner modules for the changed cells and their neighbors before decoration is applied. The player expresses only occupancy and color; all architectural detail is derived, which makes the game a pure case of procedural build assist. It is a boundary case because nothing evolves without the player; its author calls it more of a toy than a game.

## Relations

**uses**

- [Procedural build assist](../mechanic/procedural-build-assist.md) (core): Each block edit reruns a marching-cubes-style module lookup and a wave function collapse over affected cells, then adds windows, chimneys, and bushes; delay grows with structure size.
- [Building placement](../mechanic/free-placement.md) (supporting): Colored blocks are added or removed anywhere on the grid, stacked vertically.
- [Room recognition](../mechanic/room-recognition.md) (supporting): Enclosed areas are detected and filled with gardens rather than paving.

## Backlinks (computed)

**deploys:** [Wave Function Collapse and constraint-based tile generation](../technique/wave-function-collapse.md)

**precedent for:** [Learned build assist for cities](../opportunity/learned-build-assist.md), [Symbolic simulation, neural rendering](../opportunity/symbolic-sim-neural-render.md)

## Sources

- [Townscaper](../source/src-wikipedia-townscaper.md)
- [Townscaper on Steam](../source/src-steam-2026-townscaper.md)
- [How Townscaper Works: A Story Four Games in the Making](../source/src-thompson-2022-how-townscaper-works.md)

---
Provenance: created in run `2026-10-24-catalog-ga`.
