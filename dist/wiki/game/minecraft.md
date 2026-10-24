# Minecraft

*Game* · `minecraft` · status: **sourced**

A procedurally generated voxel sandbox where players mine blocks, craft tools, survive hostile night mobs and hunger, farm and trade, and build circuits from redstone.

| field | value |
|---|---|
| year | 2009 |
| year full release | 2011 |
| developer | Mojang Studios |
| platforms | PC, Console, Handheld, Mobile |
| subgenre | Sandbox world |
| subgenre secondary | Survival sim |
| sim domain | Planetary / natural, Biological / ecological, Computational / abstract |
| player role | Inhabitant |
| agency model | Direct avatar |
| time model | Real-time |
| sim scale | Region |
| fidelity | Stylized |
| perspective | First-person |
| win structure | Open sandbox |
| failure model | Soft / recoverable |
| narrative mode | Emergent |
| multiplayer | Single-player, Co-op, Competitive, Persistent MMO |
| modding | Total conversion |
| production tier | Indie |
| agent count order | ~100 |
| emergence | 4 |
| influence | 5 |
| influenced by | [Dwarf Fortress](../game/dwarf-fortress.md) |
| cluster *(computed)* | C05 |
| core count *(computed)* | 5 |
| mechanic count *(computed)* | 15 |

## Summary

A procedurally generated voxel sandbox where players mine blocks, craft tools, survive hostile night mobs and hunger, farm and trade, and build circuits from redstone.

## Core Loop

explore a generated world -> mine blocks and gather resources -> craft tools, armor, and workstations -> build shelter before night mobs spawn -> farm, breed, and trade -> dig deeper or travel to the Nether and End for rarer materials

## Design Notes

The world is an effectively infinite grid of one-meter blocks generated from a seed with biomes, caves, and ore distributions, and every block can be removed or placed, so terrain is both resource and building material. Survival pressure is light (hunger, health, light-level mob spawning on a 20-minute day cycle) and leaves room for self-set goals. Redstone gives the block world wires, power sources, repeaters, and pistons, which players use to build farms, logic gates, and working computers. The game began as a public alpha in May 2009 and reached 1.0 in November 2011.

## Relations

**influenced by**

- [Dwarf Fortress](../game/dwarf-fortress.md)

**uses**

- [Procedural terrain](../mechanic/procedural-terrain.md) (core): Worlds generate from a seed into biomes, caves, ravines, villages, and ore layers that vary by depth; terrain extends effectively without limit in horizontal directions.
- [Hand crafting](../mechanic/hand-crafting.md) (core): A 2x2 inventory grid and a 3x3 crafting table turn blocks and items into tools, armor, and blocks from shaped recipes; furnaces, anvils, and enchanting tables extend the recipe set.
- [Resource extraction](../mechanic/resource-extraction.md) (core): Blocks are mined by hand or with tools whose tier (wood, stone, iron, diamond, netherite) sets mining speed and which ores drop items.
- [Survival meters](../mechanic/survival-meters.md) (core): Survival mode has health and hunger bars; food restores hunger, high hunger regenerates health, and starvation, falls, drowning, and mobs deal damage.
- [Day-night cycle](../mechanic/day-night-cycle.md) (core): A 20-minute real-time day; hostile mobs spawn in low light, so night and caves are dangerous, and beds skip the night.
- [Building placement](../mechanic/free-placement.md) (supporting): Any block can be placed on the voxel grid, so building has no fixed footprint.
- [Signal circuits](../mechanic/signal-circuits.md) (supporting): Redstone dust carries power from levers, buttons, and sensors through repeaters and comparators to pistons, doors, and dispensers.
- [Crop cultivation](../mechanic/crop-cultivation.md) (supporting): Crops grow in stages on farmland, faster with water nearby and light.
- [Animal husbandry](../mechanic/animal-husbandry.md) (supporting): Passive mobs breed when fed their preferred food and yield food, wool, and leather.
- [Fluid and gas simulation](../mechanic/fluid-gas-simulation.md) (supporting): Water and lava flow a limited number of blocks out from source blocks; where they meet they form cobblestone, stone, or obsidian.
- [Fire spread](../mechanic/fire-spread.md) (supporting): Fire spreads to nearby flammable blocks such as wood and wool and burns them away.
- [Tech tree](../mechanic/tech-tree.md) (supporting): Material tiers gate progression: iron tools mine diamonds, diamond tools mine obsidian, and Nether materials gate brewing and the End.
- [Modding API](../mechanic/modding-api.md) (supporting): Java Edition mods (Forge, Fabric) and Bedrock add-ons, datapacks, and server plugins are widely used.
- [Persistent shared world](../mechanic/persistent-world.md) (supporting): Public multiplayer servers and Realms host worlds that persist for many players.
- [Loss on death](../mechanic/loss-on-death.md) (supporting): On death in survival the player's inventory and some experience drop at the death site and despawn after a few minutes if not recovered.

## Backlinks (computed)

**deploys:** [Real-time generative restyling of game video](../technique/real-time-video-restyling.md)

**influenced:** [Factorio](../game/factorio.md)

**precedent for:** [Generated recipe graphs](../opportunity/generated-recipe-graphs.md), [Generative decoration catalogs](../opportunity/generative-decoration-catalogs.md), [Mechanic modding by description](../opportunity/language-modding.md), [Simulation games as agent benchmarks](../opportunity/sims-as-agent-benchmarks.md), [Teachable sim companion](../opportunity/teachable-sim-companion.md)

## Sources

- [Minecraft](../source/src-wikipedia-minecraft.md)

---
Provenance: created in run `2026-10-24-catalog-gg`.
