# Falling-sand materials

*Mechanic* · `falling-sand-materials` · status: **sourced**

Every pixel or cell holds a material whose class rule makes it fall, flow, or rise by swapping with neighbors, with reactions layered on top.

| field | value |
|---|---|
| aliases | falling sand, pixel physics, powder simulation |
| family | Physics & materials |
| substrate | Cellular grid, Rule system |
| math basis | Cellular automata, Combinatorics |
| feedback | Both |
| player interface | Direct manipulation, Observation only |
| legibility | 4 |
| emergence potential | 5 |
| authoring cost | 2 |
| compute cost | 4 |
| tuning difficulty | 3 |
| ai leverage | 3 |
| maturity | Established |
| core count *(computed)* | 2 |
| earliest game *(computed)* | [The Powder Toy](../game/the-powder-toy.md) |
| earliest year *(computed)* | 2008 |
| prevalence *(computed)* | 2 |
| prevalence share *(computed)* | 0.011 |
| subgenre spread *(computed)* | 1 |
| technique count *(computed)* | 1 |
| technique exposure *(computed)* | 0.25 |

## Definition

The world is a 2D grid where each cell stores a material id and sometimes temperature, velocity, or lifetime. Each update a cell applies its class rule: powders fall straight or diagonally, liquids fall then spread sideways and swap with lower-density neighbors, gases rise then spread, and solids stay. Reaction rules convert cells, such as fire igniting flammable neighbors and water turning to steam. In Noita (2019) liquids compare densities to swap, wood burns for a set time and is destroyed, and explosions turn pixels into collapsing sand. The world is split into 64x64 chunks with dirty rectangles, updated bottom-up across threads in four checkerboard passes, with each pixel able to move 32 pixels beyond its chunk. Rigid bodies made of pixels (Box2D) recompute their shape and split as pixels are destroyed. The Powder Toy (2008), with 258 elements as of 2025, is the long-running sandbox in this lineage.

## Player Experience

Everything is simulated, so play becomes experiment. Players pour, burn, flood, and dig, and they die to chain reactions they set off themselves. Wonder and danger come from the same rules.

## Design Levers

- material catalog and per-material density, flammability, and melting point
- update order and randomization, such as alternating left and right scans
- reaction table between materials
- simulation region: whole world or only near the player
- whether mass is conserved

## Failure Modes

- A fixed scan order biases movement in one direction unless it alternates or randomizes.
- Compute limits restrict simulation to areas near the player, so distant regions freeze.
- Chain reactions kill the player suddenly, which can read as unfair.
- Rules that duplicate or delete material break conservation and enable exploits.

## Dynamics

- Hazard chains such as oil fires spreading, steam forming, and floors collapsing.
- Players engineer traps and terrain with the same rules that threaten them.
- The level is permanently reshaped by play, so no two runs stay alike.

## Open Questions

- Can neural cellular automata or learned rules produce new materials with plausible behavior at runtime?
- Can GPU compute extend per-pixel simulation to whole persistent worlds instead of the area near the player?

## Relations

**synergy**

- [Material interactions](../mechanic/material-interactions.md): Per-pixel materials with reaction rules produce chemistry players can exploit (Noita, Powder Toy).

## Backlinks (computed)

**affected by:** [Neural cellular automata](../technique/neural-cellular-automata.md)

**involved in:** [Learned material surrogates at world scale](../opportunity/learned-material-surrogates.md)

**used by:** [Noita](../game/noita.md), [The Powder Toy](../game/the-powder-toy.md)

## Sources

- [Noita: a Game Based on Falling Sand Simulation](../source/src-80lv-2019-noita-falling-sand.md)
- [Noita (video game)](../source/src-wikipedia-noita.md)
- [The Powder Toy](../source/src-wikipedia-the-powder-toy.md)

---
Provenance: created in run `2026-10-24-taxonomy-m4`.
