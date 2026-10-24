# Terraforming

*Mechanic* · `terraforming` · status: **sourced**

The player raises, lowers, flattens, or repaints terrain, usually at a cost, to make land usable or to reshape water and paths.

| field | value |
|---|---|
| aliases | landscaping, terrain editing, raise and lower land |
| family | Space & construction |
| substrate | Cellular grid |
| math basis | Cellular automata |
| feedback | None |
| player interface | Direct manipulation, Placement |
| legibility | 4 |
| emergence potential | 3 |
| authoring cost | 1 |
| compute cost | 2 |
| tuning difficulty | 2 |
| ai leverage | 3 |
| maturity | Classic |
| core count *(computed)* | 4 |
| earliest game *(computed)* | [Populous](../game/populous.md) |
| earliest year *(computed)* | 1989 |
| prevalence *(computed)* | 19 |
| prevalence share *(computed)* | 0.109 |
| subgenre spread *(computed)* | 10 |
| technique count *(computed)* | 0 |
| technique exposure *(computed)* | 0.0 |

## Definition

Terrain is a height field, often with surface material and water layers. A brush raises, lowers, levels, smooths, or paints cells under the cursor; slope limits propagate the edit to neighbors, and a cost is charged per cell or per volume moved. Downstream systems read the new heights: buildability, water flow, pathing, and views. In Populous (1989) raising and lowering land is the basic divine power, used mainly to give followers flat land for houses, which grows followers and mana. SimCity 2000 and RollerCoaster Tycoon charge money for land edits. Planet Coaster uses voxel terrain that also allows tunnels and overhangs. From Dust moves sand, water, and lava as simulated materials rather than as height edits.

## Player Experience

Shaping the world directly. Players prepare sites, carve scenery, and sometimes wield terrain as a weapon. The pleasure is tactile and godlike; the constraint is cost and the knock-on effects on water and access.

## Design Levers

- brush shapes and sizes
- slope limits and how edits spread to neighbors
- cost per cell or per volume, and whether material must be conserved
- whether terraforming is available in play or only in an editor
- how water, pathing, and buildings respond to edited terrain

## Failure Modes

- Cheap unlimited terraforming flattens the map and removes terrain as a design constraint.
- Edits silently break water flow or paths and cause floods or stranded buildings.
- Fiddly brush controls make precise shaping tedious.

## Dynamics

- In Populous, flattening land leads to more houses, more followers, and more mana for more powers, a reinforcing loop.
- Coupled with hydrology, terrain edits create dams, floods, and reservoirs.
- Terraforming against an opponent, such as sinking their land, turns it into a weapon.

## Open Questions

- Can semantic terrain brushes ("carve a canyon here") backed by generative terrain models keep edits predictable?
- How should material conservation be enforced so terraforming stays a resource decision rather than free sculpting?

## Backlinks (computed)

**used by:** [Animal Crossing: New Horizons](../game/animal-crossing-new-horizons.md), [Captain of Industry](../game/captain-of-industry.md), [Equilinox](../game/equilinox.md), [From Dust](../game/from-dust.md), [Going Medieval](../game/going-medieval.md), [Planet Coaster](../game/planet-coaster.md), [Populous](../game/populous.md), [RollerCoaster Tycoon](../game/rollercoaster-tycoon.md), [SimCity 2000](../game/simcity-2000.md), [SimCity 4](../game/simcity-4.md), [SimEarth](../game/simearth.md), [SimLife](../game/simlife.md), [Spore](../game/spore.md), [Terra Nil](../game/terra-nil.md), [Timberborn](../game/timberborn.md), [Tiny Glade](../game/tiny-glade.md), [Transport Tycoon](../game/transport-tycoon.md), [Universe Sandbox](../game/universe-sandbox.md), [Viva Piñata](../game/viva-pinata.md)

## Sources

- [Populous (video game)](../source/src-wikipedia-populous.md)
- [Planet Coaster](../source/src-wikipedia-planet-coaster.md)

---
Provenance: created in run `2026-10-24-taxonomy-m4`.
