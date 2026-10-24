# Soft-body deformation

*Mechanic* · `soft-body-deformation` · status: **sourced**

Objects built from mass nodes and spring beams bend, crumple, and break under stress, and deformation persists.

| field | value |
|---|---|
| aliases | soft-body physics, node-beam physics, deformable bodies |
| family | Physics & materials |
| substrate | Continuous physics |
| math basis | Continuum mechanics, Classical mechanics |
| feedback | None |
| player interface | Embodied skill, Direct manipulation |
| legibility | 4 |
| emergence potential | 3 |
| authoring cost | 3 |
| compute cost | 4 |
| tuning difficulty | 3 |
| ai leverage | 3 |
| maturity | Emerging |
| core count *(computed)* | 1 |
| earliest game *(computed)* | [BeamNG.drive](../game/beamng-drive.md) |
| earliest year *(computed)* | 2013 |
| prevalence *(computed)* | 1 |
| prevalence share *(computed)* | 0.006 |
| subgenre spread *(computed)* | 1 |
| technique count *(computed)* | 4 |
| technique exposure *(computed)* | 0.9 |

## Definition

An object is a network of nodes (point masses) linked by beams (massless springs with damping). Each step every beam applies force from its length deviation and damping, nodes integrate, and collisions push nodes. A beam whose force passes a deform threshold permanently changes its rest length, and one that passes its strength breaks, so parts detach. In BeamNG.drive vehicles are authored in JBeam: nodes have weight, beams have beamSpring (stiffness), beamDamp, beamDeform, and beamStrength. Beams do not resist bending or twisting, so cross braces are needed for rigidity, and stiff beams on light nodes vibrate or explode (the documentation's example stabilizes a structure by raising nodes from 6 kg to 7 kg). Finite-element and position-based methods are alternatives.

## Player Experience

Visceral, readable damage. Crashes crumple metal where they hit, and the damage changes how the vehicle drives. Players experiment with crashes as much as they drive.

## Design Levers

- node density and placement
- beam stiffness and damping per part
- deform and break thresholds
- physics step rate
- which parts are soft and which are rigid or cosmetic
- coupling of deformation to function, such as steering or engine damage

## Failure Modes

- Stiff beams on light nodes vibrate or explode, so every structure needs stability tuning.
- CPU cost per vehicle limits how many soft bodies can run at once.
- Hand-building node-beam structures for every vehicle is a large authoring cost.
- Too-soft settings make solid objects look like jelly.

## Dynamics

- Damage changes handling, which changes driving, which causes more damage.
- Crash testing becomes its own play style and community genre.
- Deformed tires and suspension couple to grip and vehicle dynamics.

## Open Questions

- Can node-beam structures be generated automatically from a visual mesh and material labels?
- Can learned deformation surrogates run many soft bodies at once on consumer hardware?

## Relations

**synergy**

- [Vehicle dynamics](../mechanic/vehicle-dynamics.md): Deforming chassis change handling after impacts (BeamNG.drive).

## Backlinks (computed)

**affected by:** [Differentiable simulation](../technique/differentiable-simulation.md), [3D Gaussian Splatting](../technique/gaussian-splatting.md), [Graph network simulators and neural operators](../technique/graph-network-simulators.md), [Subspace neural physics and learned deformers](../technique/subspace-neural-physics.md)

**involved in:** [Learned material surrogates at world scale](../opportunity/learned-material-surrogates.md)

**used by:** [BeamNG.drive](../game/beamng-drive.md)

## Sources

- [Introduction to JBeam](../source/src-beamng-2026-intro-jbeam.md)

---
Provenance: created in run `2026-10-24-taxonomy-m4`.
