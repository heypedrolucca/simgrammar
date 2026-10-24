# Structural integrity

*Mechanic* · `structural-integrity` · status: **sourced**

Structures carry support values or loads propagated from the ground, and elements that lose support or exceed their limits collapse.

| field | value |
|---|---|
| aliases | structural support, stability, load bearing |
| family | Space & construction |
| substrate | Network / graph, Continuous physics, Rule system |
| math basis | Continuum mechanics, Graph search |
| feedback | Reinforcing (positive) |
| player interface | Placement, Observation only |
| legibility | 3 |
| emergence potential | 4 |
| authoring cost | 2 |
| compute cost | 2 |
| tuning difficulty | 3 |
| ai leverage | 3 |
| maturity | Established |
| core count *(computed)* | 2 |
| earliest game *(computed)* | [Poly Bridge](../game/poly-bridge.md) |
| earliest year *(computed)* | 2015 |
| prevalence *(computed)* | 5 |
| prevalence share *(computed)* | 0.029 |
| subgenre spread *(computed)* | 4 |
| technique count *(computed)* | 1 |
| technique exposure *(computed)* | 0.188 |

## Definition

Structural elements form a connectivity graph rooted at grounded elements. Three update rules are common. Connectivity only: an element with no path to ground falls, as in Dwarf Fortress cave-ins and in Teardown, where disconnected voxel pieces become physics bodies. Decaying support: support propagates outward and drops by a material-specific amount per connection, and pieces past the limit collapse; Valheim shows this with a color scale from blue (grounded) to red (at the limit) while the hammer is equipped, and stone and core wood carry farther than wood. Load and stress: a physics solve computes member forces and breaks members past their strength, as in Poly Bridge. Collapse removes elements, spawns debris or rigid bodies, and re-checks dependents, which can cascade.

## Player Experience

Building with gravity in mind. Players add pillars, braces, and stronger materials, read the support overlay, and feel tension when extending a span. Collapses are spectacular, and demolition becomes a tactic.

## Design Levers

- propagation model: connectivity only, per-step decay, or physical stress
- per-material strength, maximum span, and support loss per connection
- what counts as ground or an anchor
- collapse resolution: instant removal, debris, or simulated rigid bodies
- visualization of support before failure

## Failure Modes

- Connectivity-only models let large structures stand on a few voxels; reviewers noted Teardown does not model compressive stress.
- Per-step decay limits feel arbitrary when they do not match the visual mass of the structure.
- Cascading collapse destroys hours of player work with no warning or undo.
- Large collapses cause frame-time spikes.

## Dynamics

- Attackers and players target supports, turning integrity into a combat and demolition system.
- Material limits shape architectural styles, such as regular pillars and stone bases in Valheim halls.
- Fire, explosions, and digging couple into chained collapses.

## Open Questions

- Can learned surrogates of finite-element stress make physically plausible load paths affordable in large player-built structures?
- What collapse warnings preserve tension without making failure trivial to avoid?

## Relations

**synergy**

- [Voxel destruction](../mechanic/voxel-destruction.md): Destruction matters when removing a piece can collapse what it supported (Teardown).

## Backlinks (computed)

**affected by:** [Graph network simulators and neural operators](../technique/graph-network-simulators.md)

**involved in:** [Learned material surrogates at world scale](../opportunity/learned-material-surrogates.md)

**used by:** [Going Medieval](../game/going-medieval.md), [Poly Bridge](../game/poly-bridge.md), [Stationeers](../game/stationeers.md), [Teardown](../game/teardown.md), [Valheim](../game/valheim.md)

## Sources

- [Teardown (video game)](../source/src-wikipedia-teardown.md)

---
Provenance: created in run `2026-10-24-taxonomy-m4`.
