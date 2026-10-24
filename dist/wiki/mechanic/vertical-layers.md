# Vertical layers

*Mechanic* · `vertical-layers` · status: **asserted**

The world has stacked layers such as z-levels, floors, or underground networks, and rules connect what happens between them.

| field | value |
|---|---|
| aliases | z-levels, underground layer, multi-floor |
| family | Space & construction |
| substrate | Cellular grid, Network / graph |
| math basis | Graph search |
| feedback | None |
| player interface | Placement, Observation only |
| legibility | 3 |
| emergence potential | 3 |
| authoring cost | 2 |
| compute cost | 3 |
| tuning difficulty | 2 |
| ai leverage | 2 |
| maturity | Classic |
| open questions | Can automatic camera and cutaway selection make deep 3D colonies as legible as a single-layer map? |
| core count *(computed)* | 2 |
| earliest game *(computed)* | [SimAnt](../game/simant.md) |
| earliest year *(computed)* | 1991 |
| prevalence *(computed)* | 8 |
| prevalence share *(computed)* | 0.046 |
| subgenre spread *(computed)* | 5 |
| technique count *(computed)* | 0 |
| technique exposure *(computed)* | 0.0 |

## Definition

The map is a stack of layers indexed by depth or named by function. Each layer holds its own grid, and cross-layer rules link them: stairs and ramps for movement, support from below, fluids and objects falling through openings, and utilities in a hidden layer serving the surface tiles above. Dwarf Fortress models a full 3D map of z-levels where dwarves dig down, build stairs and channels, and water and magma flow downward through openings. SimCity 2000 adds an underground view for water pipes and subways under the surface grid. Cities: Skylines places metro tunnels and pipes underground, and Factorio: Space Age adds elevated rails over ground tracks. State: per-layer grids plus inter-layer links; update: per-layer rules plus transfer rules at the links.

## Player Experience

Depth and hidden infrastructure. Players dig toward risk and reward, route utilities out of sight, and switch camera layers to manage what they cannot see at once.

## Design Levers

- number of layers and whether they are uniform or functionally distinct
- what crosses layers: movement, fluids, support, light, utilities
- visibility tools: cutaways, layer toggles, isometric views
- cost and hazard gradient with depth

## Failure Modes

- Legibility collapses when players must mentally stack many layers; Dwarf Fortress players used third-party visualizers to see their fortresses in 3D.
- A utility layer that mirrors the surface grid becomes a chore with no decisions of its own.
- Pathfinding and fluid updates across many layers become a major performance cost.

## Dynamics

- Digging into water or magma floods layers below or above, a classic Dwarf Fortress disaster.
- Vertical separation lets transit and utilities cross without conflicts, relieving surface congestion.
- Defenses gain a vertical dimension through chokepoints, drops, and layered walls.

## Open Questions

- Can automatic camera and cutaway selection make deep 3D colonies as legible as a single-layer map?

## Backlinks (computed)

**used by:** [Dwarf Fortress](../game/dwarf-fortress.md), [Factorio](../game/factorio.md), [Going Medieval](../game/going-medieval.md), [shapez 2](../game/shapez-2.md), [SimAnt](../game/simant.md), [SimCity 2000](../game/simcity-2000.md), [SimTower](../game/simtower.md), [Timberborn](../game/timberborn.md)

---
Provenance: created in run `2026-10-24-taxonomy-m4`.
