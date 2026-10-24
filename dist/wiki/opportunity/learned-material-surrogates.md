# Learned material surrogates at world scale

*Opportunity* · `learned-material-surrogates` · status: **asserted**

Use learned and GPU-parallel physics surrogates to bring per-particle fluids, gases, and destruction from small arenas to large persistent worlds.

| field | value |
|---|---|
| opportunity type | Infrastructure |
| involves | [Fluid and gas simulation](../mechanic/fluid-gas-simulation.md), [Heat transfer](../mechanic/heat-transfer.md), [Voxel destruction](../mechanic/voxel-destruction.md), [Falling-sand materials](../mechanic/falling-sand-materials.md), [Structural integrity](../mechanic/structural-integrity.md), [Soft-body deformation](../mechanic/soft-body-deformation.md) |
| applies | [Graph network simulators and neural operators](../technique/graph-network-simulators.md), [Massively parallel GPU simulation](../technique/massively-parallel-simulation.md), [Neural cellular automata](../technique/neural-cellular-automata.md) |
| precedent | [Noita](../game/noita.md), [Teardown](../game/teardown.md), [Oxygen Not Included](../game/oxygen-not-included.md), [BeamNG.drive](../game/beamng-drive.md), [The Powder Toy](../game/the-powder-toy.md) |
| novelty | 4 |
| feasibility | 2 |
| impact | 4 |
| horizon | 3-5 years |
| falsifiable signal | {'prediction': 'A commercial game will use a learned surrogate for fluid, gas, or destruction simulation at runtime.', 'resolve_by': '2029-12-31', 'criteria': 'Developer documentation or technical talk confirming a trained neural model simulating physical materials during play.'} |
| priority *(computed)* | 3.138 |

## Thesis

Noita, Teardown, BeamNG, and Oxygen Not Included show players love worlds where every particle or voxel is simulated, but compute caps these simulations to small areas or 2D. Graph-network simulators and neural operators learn fluid, cloth, and deformation dynamics at large speedups, and GPU-parallel simulators make the remaining numerical work cheap. Combining a learned surrogate for the far field with exact simulation near the player could extend material simulation to whole maps.

## Design Sketch

A colony or sandbox world where water, heat, gas, and structural stress are simulated everywhere at coarse resolution by a learned surrogate and exactly within a radius of active play, with consistent hand-off at the boundary. Players can flood a valley or collapse a mountain and see effects propagate realistically across the map.

## Key Risks

- Surrogates break conservation laws, producing exploitable infinite water or energy.
- Boundary artifacts between surrogate and exact zones.
- Determinism across GPUs for multiplayer.

## Validation Experiment

Train a graph-network surrogate on a 2D falling-sand fluid simulator and measure mass conservation error and speedup over 10,000 steps at four times the training domain size. Success: mass error under 1 percent with a speedup above 10 times.

## Falsifiable signal

- **Prediction:** A commercial game will use a learned surrogate for fluid, gas, or destruction simulation at runtime.
- **Resolve by:** 2029-12-31
- **Criteria:** Developer documentation or technical talk confirming a trained neural model simulating physical materials during play.

## Relations

**applies**

- [Graph network simulators and neural operators](../technique/graph-network-simulators.md)
- [Massively parallel GPU simulation](../technique/massively-parallel-simulation.md)
- [Neural cellular automata](../technique/neural-cellular-automata.md)

**involves**

- [Fluid and gas simulation](../mechanic/fluid-gas-simulation.md)
- [Heat transfer](../mechanic/heat-transfer.md)
- [Voxel destruction](../mechanic/voxel-destruction.md)
- [Falling-sand materials](../mechanic/falling-sand-materials.md)
- [Structural integrity](../mechanic/structural-integrity.md)
- [Soft-body deformation](../mechanic/soft-body-deformation.md)

**precedent**

- [Noita](../game/noita.md)
- [Teardown](../game/teardown.md)
- [Oxygen Not Included](../game/oxygen-not-included.md)
- [BeamNG.drive](../game/beamng-drive.md)
- [The Powder Toy](../game/the-powder-toy.md)

---
Provenance: created in run `2026-10-24-synthesis`.
