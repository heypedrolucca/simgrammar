# Resource extraction

*Mechanic* · `resource-extraction` · status: **sourced**

Workers or machines harvest raw materials from map nodes (ore, trees, fish, oil) at rates set by tools, labor, and node richness.

| field | value |
|---|---|
| aliases | harvesting, gathering, mining |
| family | Resources & production |
| substrate | Rule system, Agent-based, Aggregate stocks |
| math basis | System dynamics / ODEs, Optimization |
| feedback | Reinforcing (positive) |
| player interface | Placement, Orders, Direct manipulation |
| legibility | 5 |
| emergence potential | 2 |
| authoring cost | 2 |
| compute cost | 2 |
| tuning difficulty | 2 |
| ai leverage | 1 |
| maturity | Classic |
| open questions | Could procedural geology tied to visible terrain features make extraction sites a matter of inference rather than icons? |
| core count *(computed)* | 10 |
| earliest game *(computed)* | [Utopia](../game/utopia.md) |
| earliest year *(computed)* | 1982 |
| prevalence *(computed)* | 29 |
| prevalence share *(computed)* | 0.167 |
| subgenre spread *(computed)* | 13 |
| technique count *(computed)* | 0 |
| technique exposure *(computed)* | 0.0 |

## Definition

Map nodes (ore patches, trees, fishing spots, oil wells) hold a resource type and a richness or purity value. An extractor, which is a placed machine, an assigned worker, or the avatar with a tool, produces units at a base rate multiplied by tool tier, worker skill, richness, and modifiers. Output goes to an adjacent buffer or is carried away by hauling. Satisfactory multiplies extraction by node purity (impure 0.5x, normal 1.0x, pure 2.0x); Factorio drills mine a fixed rate per tile with productivity research; RTS games such as Age of Empires assign villagers who gather by walking to nodes and back; Minecraft and Valheim gate which blocks can be mined by tool tier. Inputs: node, extractor, labor or power. Outputs: a stream of raw materials and, where depletion exists, a decrement to the node.

## Player Experience

The first link in every chain. Players scout for rich nodes, claim them, and judge how many extractors a site justifies. In avatar games, swinging a tool at a rock is a tactile, repeatable earning loop; in factory games, placing drills on the best patch is an early, high-leverage decision.

## Design Levers

- base rate per extractor and tool or tier multipliers
- richness or purity variation across nodes
- labor model: machine, assigned worker, or avatar action
- node placement and distance from base
- whether extraction depletes the node (see deposit depletion) or is infinite

## Failure Modes

- Uniform nodes make location choice irrelevant.
- Extraction rates far above processing capacity create endless stockpiles and remove pressure.
- Avatar gathering that never automates becomes grind late in a run.

## Dynamics

- Rich nodes far from base create a tradeoff between yield and logistics cost.
- Contested nodes become flashpoints in multiplayer and RTS maps.
- Extraction is the root of every production chain, so its rate caps the whole economy.

## Open Questions

- Could procedural geology tied to visible terrain features make extraction sites a matter of inference rather than icons?

## Backlinks (computed)

**required by:** [Deposit depletion](../mechanic/deposit-depletion.md)

**used by:** [A Tale in the Desert](../game/a-tale-in-the-desert.md), [Aurora 4X](../game/aurora-4x.md), [Bitburner](../game/bitburner.md), [Black & White](../game/black-and-white.md), [Capitalism](../game/capitalism.md), [Captain of Industry](../game/captain-of-industry.md), [Dyson Sphere Program](../game/dyson-sphere-program.md), [Elite](../game/elite.md), [Elite Dangerous](../game/elite-dangerous.md), [EVE Online](../game/eve-online.md), [Factorio](../game/factorio.md), [Frostpunk](../game/frostpunk.md), [Frostpunk 2](../game/frostpunk-2.md), [Jurassic World Evolution](../game/jurassic-world-evolution.md), [Kerbal Space Program](../game/kerbal-space-program.md), [Mindustry](../game/mindustry.md), [Minecraft](../game/minecraft.md), [M.U.L.E.](../game/mule.md), [Offworld Trading Company](../game/offworld-trading-company.md), [Project Sid](../game/project-sid.md), [Satisfactory](../game/satisfactory.md), [Screeps](../game/screeps.md), [shapez 2](../game/shapez-2.md), [Space Engineers](../game/space-engineers.md), [Space Haven](../game/space-haven.md), [Stationeers](../game/stationeers.md), [Surviving Mars](../game/surviving-mars.md), [Ultima Online](../game/ultima-online.md), [Utopia](../game/utopia.md)

## Sources

- [Resource node](../source/src-satisfactorywiki-2026-resource-node.md)

---
Provenance: created in run `2026-10-24-taxonomy-m1`.
