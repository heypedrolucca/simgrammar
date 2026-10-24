# Going Medieval

*Game* · `going-medieval` · status: **sourced**

A colony sim set after a plague in which settlers with traits, needs, and moods dig into and build up a multi-level voxel terrain to survive seasons and raids.

| field | value |
|---|---|
| year | 2021 |
| year full release | 2026 |
| developer | Foxy Voxel |
| platforms | PC |
| subgenre | Colony sim |
| sim domain | Social / interpersonal, Physical / mechanical, Military / conflict |
| player role | Overseer |
| agency model | Order queue, Zoning / placement, Indirect incentive, Direct unit control |
| time model | Real-time with pause |
| sim scale | Settlement |
| fidelity | Systemic |
| perspective | Free 3D camera |
| win structure | Open sandbox |
| failure model | Cascading collapse |
| narrative mode | Emergent |
| multiplayer | Single-player |
| modding | Content |
| production tier | Indie |
| agent count order | ~10 |
| emergence | 3 |
| influence | 1 |
| influenced by | [RimWorld](../game/rimworld.md) |
| cluster *(computed)* | C04 |
| core count *(computed)* | 4 |
| mechanic count *(computed)* | 17 |

## Core Loop

dig into and build up voxel terrain -> assign settlers to roles and jobs -> settlers meet needs and mood shifts -> seasons change food supply -> raiders and beasts attack the walls -> research, build higher, and take in newcomers

## Design Notes

It follows the RimWorld pattern of named settlers with traits, perks, skills, needs, and moods, and is widely compared to RimWorld and Dwarf Fortress. Its distinctive layer is a fully three-dimensional voxel map: the player can dig cellars and caverns, raise multi-storey stone and timber forts, and reshape earth and water, so defensive geometry and storage depth are design problems in three dimensions. Early access ran from June 2021 to the 1.0 release in March 2026.

## Relations

**influenced by**

- [RimWorld](../game/rimworld.md)

**uses**

- [Terraforming](../mechanic/terraforming.md) (core): A 3D terrain toolset digs out or fills voxel earth and water on a randomly generated multi-level map, so cellars, moats, and caverns are carved from the ground.
- [Vertical layers](../mechanic/vertical-layers.md) (core): Settlements stack multi-storey buildings above ground and cellars and caverns below, connected by stairs and ladders.
- [Needs decay](../mechanic/needs-decay.md) (core): Settlers track needs such as hunger, sleep, clothing preferences, and religion, and meeting them keeps settlers content.
- [Raid defense](../mechanic/raid-defense.md) (core): Repeated bandit raids and animal attacks are met with walls, traps, and settlers equipped and commanded in battle.
- [Mood and breakdowns](../mechanic/mood-breakdown.md) (supporting): Settlers in poor conditions become dissatisfied and may leave the settlement.
- [Personality traits](../mechanic/personality-traits.md) (supporting): Backgrounds, traits, and perks set at settler creation.
- [Agent skills](../mechanic/agent-skills.md) (supporting): Skills such as Animal Handling improve through use, including hunting and combat.
- [Work priorities](../mechanic/work-priorities.md) (supporting): Settlers are assigned to roles that fit their skills.
- [Designation orders](../mechanic/designation-orders.md) (supporting)
- [Structural integrity](../mechanic/structural-integrity.md) (supporting): Built structures need support, and unsupported sections collapse.
- [Room recognition](../mechanic/room-recognition.md) (supporting): Workshops, chapels, libraries, and bedrooms are furnished and decorated rooms.
- [Seasons](../mechanic/seasons.md) (supporting): Seasonal changes govern food production and storage.
- [Spoilage](../mechanic/spoilage.md) (supporting): Food keeps longer in cool storage such as cellars.
- [Crop cultivation](../mechanic/crop-cultivation.md) (supporting)
- [Animal husbandry](../mechanic/animal-husbandry.md) (supporting)
- [Tech tree](../mechanic/tech-tree.md) (supporting): Research unlocks medieval technology.
- [Permadeath](../mechanic/permadeath.md) (supporting)

## Sources

- [Going Medieval](../source/src-wikipedia-going-medieval.md)
- [Going Medieval on Steam](../source/src-steam-2026-going-medieval.md)

---
Provenance: created in run `2026-10-24-catalog-gb`.
