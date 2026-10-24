# Building placement

*Mechanic* · `free-placement` · status: **asserted**

The player places discrete structures on a grid or freely, and placement constraints turn layout into a spatial puzzle.

| field | value |
|---|---|
| aliases | plopping, construction placement, grid placement |
| family | Space & construction |
| substrate | Cellular grid, Rule system |
| math basis | Optimization, Combinatorics |
| feedback | None |
| player interface | Placement |
| legibility | 4 |
| emergence potential | 3 |
| authoring cost | 3 |
| compute cost | 1 |
| tuning difficulty | 2 |
| ai leverage | 2 |
| maturity | Classic |
| core count *(computed)* | 18 |
| earliest game *(computed)* | [Conway's Game of Life](../game/game-of-life.md) |
| earliest year *(computed)* | 1970 |
| prevalence *(computed)* | 75 |
| prevalence share *(computed)* | 0.431 |
| subgenre spread *(computed)* | 17 |
| technique count *(computed)* | 0 |
| technique exposure *(computed)* | 0.0 |

## Definition

The player picks a structure type, position, and usually rotation. The game tests the footprint against occupancy, terrain slope, required neighbors (road access, a water tile, an ore patch), and cost. A valid placement writes the structure into the occupancy grid or spatial index and deducts cost; demolition reverses it, often with a partial refund. Tile grids (SimCity, Factorio, RimWorld) make footprints exact; gridless placement (Manor Lords, Foundation) allows arbitrary angles and curved streets. A ghost preview tinted valid or invalid is the standard interface. The occupancy map is the input to pathing, coverage, adjacency, and room detection.

## Player Experience

A spatial puzzle with immediate feedback. Players plan space, fit footprints together, and live with early decisions as the layout fills. Gridless placement adds expressive freedom but also the chore of aligning things by eye.

## Design Levers

- grid, offset grid, or gridless placement, with or without snapping
- footprint sizes and shapes, and whether rotation changes them
- terrain rules: slope tolerance, water, and foundations
- requirement rules such as road adjacency or resource tiles
- demolition refund and rebuild cost, which set how much commitment a placement carries

## Failure Modes

- Gridless placement leaves slivers and gaps that waste space and look untidy.
- Free demolition and full refunds remove commitment, so placement stops being a decision.
- A red ghost with no reason given makes hidden placement rules feel arbitrary.
- Permissive rules with abundant space make layout trivial.

## Dynamics

- Early placements constrain later ones, producing path-dependent layouts and eventual rebuilds.
- Space becomes a resource that players trade against throughput or beauty.
- Players converge on standard modules, which leads to blueprint copying and sharing.

## Open Questions

- Can natural-language or sketch placement ("put a market near the docks") keep the puzzle while removing the click cost?
- Which footprint rules make gridless placement as plannable as a grid?

## Backlinks (computed)

**involved in:** [Generative decoration catalogs](../opportunity/generative-decoration-catalogs.md), [Learned build assist for cities](../opportunity/learned-build-assist.md), [Placement that tells stories](../opportunity/placement-that-tells-stories.md), [Symbolic simulation, neural rendering](../opportunity/symbolic-sim-neural-render.md)

**required by:** [Adjacency scoring](../mechanic/adjacency-scoring.md), [Room recognition](../mechanic/room-recognition.md)

**used by:** [Against the Storm](../game/against-the-storm.md), [Animal Crossing: New Horizons](../game/animal-crossing-new-horizons.md), [Anno 117: Pax Romana](../game/anno-117.md), [Anno 1800](../game/anno-1800.md), [Banished](../game/banished.md), [Big Ambitions](../game/big-ambitions.md), [Big Pharma](../game/big-pharma.md), [Black & White](../game/black-and-white.md), [Caesar III](../game/caesar-3.md), [Capitalism](../game/capitalism.md), [Captain of Industry](../game/captain-of-industry.md), [Cities: Skylines](../game/cities-skylines.md), [Cities: Skylines II](../game/cities-skylines-2.md), [Dwarf Fortress](../game/dwarf-fortress.md), [Dyson Sphere Program](../game/dyson-sphere-program.md), [Equilinox](../game/equilinox.md), [Factorio](../game/factorio.md), [Farthest Frontier](../game/farthest-frontier.md), [Foundation](../game/foundation.md), [Frostpunk](../game/frostpunk.md), [Frostpunk 2](../game/frostpunk-2.md), [Conway's Game of Life](../game/game-of-life.md), [Going Medieval](../game/going-medieval.md), [House Flipper](../game/house-flipper.md), [inZOI](../game/inzoi.md), [Islanders](../game/islanders.md), [Jurassic World Evolution](../game/jurassic-world-evolution.md), [Kenshi](../game/kenshi.md), [Kingdoms and Castles](../game/kingdoms-and-castles.md), [Manor Lords](../game/manor-lords.md), [Mindustry](../game/mindustry.md), [Minecraft](../game/minecraft.md), [Offworld Trading Company](../game/offworld-trading-company.md), [Oxygen Not Included](../game/oxygen-not-included.md), [Paralives](../game/paralives.md), [Pharaoh](../game/pharaoh.md), [Planet Coaster](../game/planet-coaster.md), [Planet Zoo](../game/planet-zoo.md), [Prison Architect](../game/prison-architect.md), [Project Hospital](../game/project-hospital.md), [Project Zomboid](../game/project-zomboid.md), [Railroad Tycoon](../game/railroad-tycoon.md), [RollerCoaster Tycoon](../game/rollercoaster-tycoon.md), [Satisfactory](../game/satisfactory.md), [Schedule I](../game/schedule-i.md), [shapez 2](../game/shapez-2.md), [SimCity](../game/simcity-1989.md), [SimCity 2000](../game/simcity-2000.md), [SimCity (2013)](../game/simcity-2013.md), [SimCity 4](../game/simcity-4.md), [SimTower](../game/simtower.md), [Songs of Syx](../game/songs-of-syx.md), [Space Haven](../game/space-haven.md), [Stardew Valley](../game/stardew-valley.md), [Stationeers](../game/stationeers.md), [Subnautica](../game/subnautica.md), [Surviving Mars](../game/surviving-mars.md), [Terra Nil](../game/terra-nil.md), [The Sims](../game/the-sims.md), [The Sims 2](../game/the-sims-2.md), [The Sims 3](../game/the-sims-3.md), [The Sims 4](../game/the-sims-4.md), [Theme Hospital](../game/theme-hospital.md), [Theme Park](../game/theme-park.md), [Timberborn](../game/timberborn.md), [Tiny Glade](../game/tiny-glade.md), [Townscaper](../game/townscaper.md), [Transport Tycoon](../game/transport-tycoon.md), [Tropico 6](../game/tropico-6.md), [Two Point Hospital](../game/two-point-hospital.md), [Ultima Online](../game/ultima-online.md), [Utopia](../game/utopia.md), [Viva Piñata](../game/viva-pinata.md), [Workers & Resources: Soviet Republic](../game/workers-and-resources.md), [Zoo Tycoon](../game/zoo-tycoon.md)

---
Provenance: created in run `2026-10-24-taxonomy-m4`.
