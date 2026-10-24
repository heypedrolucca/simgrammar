# Heat transfer

*Mechanic* · `heat-transfer` · status: **sourced**

Temperature diffuses between cells, materials, and objects by conductivity and heat capacity, and thresholds trigger phase changes and damage.

| field | value |
|---|---|
| aliases | temperature simulation, thermal simulation, thermodynamics |
| family | Physics & materials |
| substrate | Cellular grid, Aggregate stocks |
| math basis | Continuum mechanics |
| feedback | Balancing (negative) |
| player interface | Placement, Observation only |
| legibility | 3 |
| emergence potential | 4 |
| authoring cost | 2 |
| compute cost | 3 |
| tuning difficulty | 3 |
| ai leverage | 2 |
| maturity | Established |
| open questions | Can forecasting tools that project temperature trends turn slow thermal failure into a readable planning problem? |
| core count *(computed)* | 3 |
| earliest game *(computed)* | [Dwarf Fortress](../game/dwarf-fortress.md) |
| earliest year *(computed)* | 2006 |
| prevalence *(computed)* | 9 |
| prevalence share *(computed)* | 0.052 |
| subgenre spread *(computed)* | 5 |
| technique count *(computed)* | 0 |
| technique exposure *(computed)* | 0.0 |

## Definition

Each cell, room, or object holds a temperature and often mass, specific heat capacity, and thermal conductivity. Each tick heat flows between neighbors in proportion to the temperature difference and a conductance from both materials, and temperature changes by heat divided by mass times heat capacity. Thresholds trigger melting, boiling, freezing, damage, and effects on agents. In Oxygen Not Included a tick is 0.2 s; cell-to-cell transfer uses q = dT x dt x k x 1000, multiplied by 25 between solids and gases and 625 between liquids; transfer stops below a 1 C difference or 0.1 DTU, and one tick may close at most a quarter of the difference. Insulated tiles divide conductivity heavily. RimWorld holds one temperature per room that equalizes with outdoors through walls and doors and is driven by heaters and coolers.

## Player Experience

Thermal engineering. Players insulate, vent, and cool, and they watch overlays for creeping heat. Late failures arrive slowly: a base heats a fraction of a degree per cycle until crops die or machines stop.

## Design Levers

- per-material specific heat capacity and conductivity
- phase-change temperatures and their consequences
- transfer multipliers between solids, liquids, and gases
- tick length and per-tick caps for stability
- insulation strength and environmental heat sinks
- damage and agent thresholds

## Failure Modes

- Rounding and phase-change edge cases let players create or delete heat, which becomes a standard exploit.
- Per-cell diffusion across a large map becomes a late-game performance cost.
- Without overlays, rising temperature is invisible until a threshold fails.
- If equilibrium takes far longer than a session, heat stops mattering; if it is fast, it becomes noise.

## Dynamics

- Machines emit heat as a byproduct, so a growing industrial base slowly overheats itself.
- Seasons, fire, and magma couple to temperature and drive phase changes and evacuations.
- Heat moved by fluids links plumbing layout to thermal management.

## Open Questions

- Can forecasting tools that project temperature trends turn slow thermal failure into a readable planning problem?

## Relations

**synergy**

- [Material interactions](../mechanic/material-interactions.md): Temperature thresholds trigger material state changes and reactions.
- [Spoilage](../mechanic/spoilage.md): Temperature drives rot rates.

## Backlinks (computed)

**involved in:** [Learned material surrogates at world scale](../opportunity/learned-material-surrogates.md)

**used by:** [Dwarf Fortress](../game/dwarf-fortress.md), [Elite Dangerous](../game/elite-dangerous.md), [Kerbal Space Program](../game/kerbal-space-program.md), [Oxygen Not Included](../game/oxygen-not-included.md), [Space Haven](../game/space-haven.md), [Stationeers](../game/stationeers.md), [The Powder Toy](../game/the-powder-toy.md), [Universe Sandbox](../game/universe-sandbox.md), [The Legend of Zelda: Breath of the Wild](../game/zelda-breath-of-the-wild.md)

## Sources

- [Thermal Conductivity](../source/src-oxygennotincludedwiki-2026-thermal-conductivity.md)

---
Provenance: created in run `2026-10-24-taxonomy-m4`.
