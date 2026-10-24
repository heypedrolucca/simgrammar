# Tiny Glade

*Game* · `tiny-glade` · status: **sourced**

A medieval building sandbox in which drawn walls, paths, and building outlines are assembled by procedural rules into detailed castles and cottages, with no goals, management, or failure states.

| field | value |
|---|---|
| year | 2024 |
| developer | Pounce Light |
| platforms | PC |
| subgenre | City builder |
| sim domain | Urban |
| player role | Engineer / designer |
| agency model | Zoning / placement |
| time model | Real-time |
| sim scale | Settlement |
| fidelity | Abstract |
| perspective | Free 3D camera |
| win structure | Open sandbox |
| failure model | None |
| narrative mode | None |
| multiplayer | Single-player |
| modding | None |
| production tier | Indie |
| agent count order | ~10 |
| emergence | 2 |
| influence | 1 |
| boundary case | True |
| cluster *(computed)* | C16 |
| core count *(computed)* | 1 |
| mechanic count *(computed)* | 3 |

## Summary

A medieval building sandbox in which drawn walls, paths, and building outlines are assembled by procedural rules into detailed castles and cottages, with no goals, management, or failure states.

## Core Loop

draw walls, paths, and building outlines -> procedural rules assemble bricks, roofs, doors, and supports to fit -> reshape terrain and add water -> ivy grows and sheep wander the paths -> keep editing

## Design Notes

Tiny Glade takes the Townscaper approach to freehand strokes: a path drawn through a building produces a door, and raising a building adds columns and beams to support it, so local rules respond to how elements meet. The two-person studio built it on a custom fork of the Rust engine Bevy. It is a boundary case: the only autonomous elements are ambient life such as growing ivy and wandering sheep.

## Relations

**uses**

- [Procedural build assist](../mechanic/procedural-build-assist.md) (core): Walls, paths, and building outlines are turned into detailed geometry; a path through a building creates a door and raising a building adds supporting columns and beams.
- [Building placement](../mechanic/free-placement.md) (supporting): Strokes are drawn freely without a grid.
- [Terraforming](../mechanic/terraforming.md) (supporting): Terrain height can be changed and rivers and ponds added.

## Backlinks (computed)

**precedent for:** [Generative decoration catalogs](../opportunity/generative-decoration-catalogs.md), [Learned build assist for cities](../opportunity/learned-build-assist.md), [Symbolic simulation, neural rendering](../opportunity/symbolic-sim-neural-render.md)

## Sources

- [Tiny Glade](../source/src-wikipedia-tiny-glade.md)
- [Tiny Glade on Steam](../source/src-steam-2026-tiny-glade.md)

---
Provenance: created in run `2026-10-24-catalog-ga`.
