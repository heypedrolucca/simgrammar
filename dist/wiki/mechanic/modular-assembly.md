# Modular assembly

*Mechanic* · `modular-assembly` · status: **sourced**

The player builds machines, vehicles, or creatures from parts whose stats and physical arrangement determine how the result behaves.

| field | value |
|---|---|
| aliases | part-based construction, vehicle builder, creature editor |
| family | Space & construction |
| substrate | Rule system, Continuous physics, Player-authored logic |
| math basis | Combinatorics, Classical mechanics, Optimization |
| feedback | Balancing (negative) |
| player interface | Placement, Direct manipulation |
| legibility | 3 |
| emergence potential | 4 |
| authoring cost | 3 |
| compute cost | 3 |
| tuning difficulty | 4 |
| ai leverage | 4 |
| maturity | Established |
| core count *(computed)* | 17 |
| earliest game *(computed)* | [The Incredible Machine](../game/the-incredible-machine.md) |
| earliest year *(computed)* | 1993 |
| prevalence *(computed)* | 27 |
| prevalence share *(computed)* | 0.155 |
| subgenre spread *(computed)* | 15 |
| technique count *(computed)* | 4 |
| technique exposure *(computed)* | 1.35 |

## Definition

A design is a set of parts joined at attachment points. Each part carries stats (mass, thrust, fuel, capacity, power, abilities) and sometimes a collision body. Behavior is computed either by aggregating stats or by simulating the assembled structure. Kerbal Space Program stacks tanks, engines, and decouplers into stages whose delta-v follows from mass ratios and simulates the craft as jointed parts. Besiege simulates blocks, hinges, and powered wheels as rigid bodies. Spore's creature editor grants abilities from attached parts. Armored Core assembles mechs from frame parts under weight and energy limits. Space Engineers builds small and large grids from blocks such as thrusters, reactors, conveyors, and deformable armor. Constraints such as budget, mass, power, or part count bound the design space.

## Player Experience

Tinkering and test-to-failure. Players build, watch the contraption flip, explode, or fail to lift off, diagnose why, and rebuild. A working design earns engineering pride, and many get shared.

## Design Levers

- part catalog size and granularity
- stat aggregation versus full physical simulation of the assembly
- attachment rules: fixed nodes, free attachment, symmetry tools
- constraints: cost, mass, energy, part count
- test environment and how clearly failure causes are shown

## Failure Modes

- Joint strength limits and physics instability in large assemblies make craft wobble or break apart; Kerbal Space Program players call unexplained destruction the Kraken.
- Part count drives simulation cost, so ambitious builds slow the game down.
- A dominant part combination becomes the only competitive build.
- Catalog bloat buries useful parts and overwhelms new players.

## Dynamics

- Players invent contraptions designers did not anticipate, such as flying machines in Besiege, and share them.
- When parts are unlocked by progression, the assembly space widens over time and old designs get rebuilt.
- Coupled with physics, small design changes produce large behavioral differences, which drives iteration.

## Open Questions

- Can reinforcement-learned controllers make arbitrary player-built bodies walk, swim, or fly convincingly at runtime?
- Can generated parts with stats derived from their geometry replace hand-authored part catalogs?

## Relations

**synergy**

- [Rigid-body physics](../mechanic/rigid-body-physics.md): Physics decides whether an assembled machine works, so building becomes experimentation (Besiege).
- [Orbital mechanics](../mechanic/orbital-mechanics.md): Rocket design is meaningful because orbits demand specific delta-v budgets (Kerbal Space Program).

## Backlinks (computed)

**affected by:** [Differentiable simulation](../technique/differentiable-simulation.md), [Massively parallel GPU simulation](../technique/massively-parallel-simulation.md), [Quality-diversity search (MAP-Elites) for content and balance](../technique/quality-diversity-search.md), [Text- and image-to-3D asset generation](../technique/text-to-3d-assets.md)

**used by:** [Anno 117: Pax Romana](../game/anno-117.md), [Aurora 4X](../game/aurora-4x.md), [Autonauts](../game/autonauts.md), [Besiege](../game/besiege.md), [Dyson Sphere Program](../game/dyson-sphere-program.md), [Elite Dangerous](../game/elite-dangerous.md), [EVE Online](../game/eve-online.md), [Foundation](../game/foundation.md), [Garry's Mod](../game/garrys-mod.md), [Gran Turismo](../game/gran-turismo.md), [Hearts of Iron IV](../game/hearts-of-iron-4.md), [Kerbal Space Program](../game/kerbal-space-program.md), [Kingdoms and Castles](../game/kingdoms-and-castles.md), [Noita](../game/noita.md), [Opus Magnum](../game/opus-magnum.md), [PC Building Simulator](../game/pc-building-simulator.md), [Planet Coaster](../game/planet-coaster.md), [Planet Zoo](../game/planet-zoo.md), [Poly Bridge](../game/poly-bridge.md), [RollerCoaster Tycoon](../game/rollercoaster-tycoon.md), [Screeps](../game/screeps.md), [Second Life](../game/second-life.md), [Space Engineers](../game/space-engineers.md), [Spore](../game/spore.md), [Stellaris](../game/stellaris.md), [The Incredible Machine](../game/the-incredible-machine.md), [X-Plane](../game/x-plane.md)

## Sources

- [Kerbal Space Program](../source/src-wikipedia-kerbal-space-program.md)
- [Besiege (video game)](../source/src-wikipedia-besiege.md)
- [Space Engineers](../source/src-wikipedia-space-engineers.md)

---
Provenance: created in run `2026-10-24-taxonomy-m4`.
