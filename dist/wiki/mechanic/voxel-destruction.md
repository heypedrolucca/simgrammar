# Voxel destruction

*Mechanic* · `voxel-destruction` · status: **sourced**

The world is built from small destructible units that can be removed, broken loose, and burned anywhere.

| field | value |
|---|---|
| aliases | destructible voxels, block breaking, destructible environments |
| family | Physics & materials |
| substrate | Cellular grid, Continuous physics |
| math basis | Classical mechanics, Graph search |
| feedback | None |
| player interface | Direct manipulation, Embodied skill |
| legibility | 4 |
| emergence potential | 4 |
| authoring cost | 2 |
| compute cost | 4 |
| tuning difficulty | 3 |
| ai leverage | 3 |
| maturity | Established |
| core count *(computed)* | 2 |
| earliest game *(computed)* | [Space Engineers](../game/space-engineers.md) |
| earliest year *(computed)* | 2013 |
| prevalence *(computed)* | 2 |
| prevalence share *(computed)* | 0.011 |
| subgenre spread *(computed)* | 2 |
| technique count *(computed)* | 2 |
| technique exposure *(computed)* | 0.75 |

## Definition

The world is stored as voxels with a material per cell, sometimes in several separate volumes. Tools, explosions, and fire remove or convert voxels; the engine then recomputes connectivity, and pieces cut loose either become rigid bodies or stay in place. In Teardown every level is built from destructible voxels; each voxel's material comes from an 8-bit palette setting color, roughness, emissiveness, reflectivity, and physical type; the world is split into several voxel volumes; and the engine does not model compressive stress. Minecraft breaks blocks after a mining time set by tool and material, and only some blocks, such as sand and gravel, fall when unsupported. Outputs are the edited world, debris bodies, and new paths.

## Player Experience

Total freedom of route. Any wall can become a door, so players plan paths through buildings and enjoy demolition for its own sake. The world remembers what they broke.

## Design Levers

- voxel size relative to the player
- material hardness and which tools break which materials
- connectivity and support rules for loose pieces
- debris lifetime and cleanup
- fire and explosion coupling
- unbreakable materials that preserve level structure

## Failure Modes

- Level design is hard because walls and doors cannot block players; Teardown relied on elevation, distance, water, and unbreakable objects.
- Synchronizing voxel physics over a network is hard; Teardown's team originally judged multiplayer infeasible, and co-op arrived only in a 2026 update.
- Structures stand on implausibly little support when only connectivity is checked.
- Destruction at scale caps performance and map size.

## Dynamics

- Players cut their own routes, turning levels into planning puzzles, as in Teardown's heist missions.
- Fire and collapses chain through flammable and weakened structures.
- Persistent edits accumulate, so the world reflects a session's history.

## Open Questions

- Can generative models author voxel levels whose structure holds up to arbitrary destruction?
- Can learned fracture models give voxel destruction plausible stress without full physical simulation?

## Backlinks (computed)

**affected by:** [Diffusion and autoregressive neural game engines](../technique/diffusion-game-engines.md), [Neural cellular automata](../technique/neural-cellular-automata.md)

**involved in:** [Learned material surrogates at world scale](../opportunity/learned-material-surrogates.md)

**used by:** [Space Engineers](../game/space-engineers.md), [Teardown](../game/teardown.md)

## Sources

- [Teardown (video game)](../source/src-wikipedia-teardown.md)

---
Provenance: created in run `2026-10-24-taxonomy-m4`.
