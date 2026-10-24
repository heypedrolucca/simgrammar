# Satisfactory

*Game* · `satisfactory` · status: **sourced**

A first-person 3D factory automation game in which a pioneer taps infinite resource nodes on an alien planet and connects machines with belts, pipes, trains, and drones to deliver project parts to FICSIT's Space Elevator.

| field | value |
|---|---|
| year | 2019 |
| year full release | 2024 |
| developer | Coffee Stain Studios |
| platforms | PC, Console |
| subgenre | Factory / automation |
| sim domain | Industrial / logistics, Physical / mechanical |
| player role | Engineer / designer |
| agency model | Direct avatar, Zoning / placement |
| time model | Real-time |
| sim scale | Facility |
| fidelity | Stylized |
| perspective | First-person |
| win structure | Open sandbox |
| failure model | Soft / recoverable |
| narrative mode | Authored |
| multiplayer | Single-player, Co-op |
| modding | Scripting |
| production tier | AA |
| agent count order | ~100 |
| emergence | 2 |
| influence | 3 |
| influenced by | [Factorio](../game/factorio.md) |
| cluster *(computed)* | C01 |
| core count *(computed)* | 6 |
| mechanic count *(computed)* | 18 |

## Summary

A first-person 3D factory automation game in which a pioneer taps infinite resource nodes on an alien planet and connects machines with belts, pipes, trains, and drones to deliver project parts to FICSIT's Space Elevator.

## Core Loop

scout resource nodes -> place miners -> belt ore through smelters, constructors, and assemblers -> deliver parts to the HUB and Space Elevator -> unlock the next tier -> expand power and logistics to distant nodes

## Design Notes

Satisfactory moves the Factorio-style ratio puzzle into a hand-built 3D world explored on foot, so verticality, foundations, and architecture become part of layout and many players build for appearance as well as throughput. Resource nodes never deplete and are graded impure, normal, or pure (0.5x, 1x, 2x), so expansion is driven by needing more node types and output rather than by exhaustion. The power grid fails as a whole: when demand exceeds supply and storage is empty the fuse trips and every connected building stops until the player resets it, unlike grids that slow machines proportionally. Clock speed (1% to 250%, with Power Shards and a power exponent of about 1.32) and 106 alternate recipes from crash-site hard drives give each factory a recipe-selection layer that the taxonomy folds into production-chain; this run proposed a machine-boosting mechanic for clock speed and similar systems, and a megaproject-sink mechanic for the Space Elevator. There are no base-raiding enemies; fauna threaten only the pioneer.

## Sources

- src-wikipedia-satisfactory
- src-satisfactorywiki-2026-resource-node
- src-satisfactorywiki-2026-conveyor-belts
- src-satisfactorywiki-2026-power
- src-satisfactorywiki-2026-alternate-recipes
- src-satisfactorywiki-2026-space-elevator
- src-satisfactorywiki-2026-pipeline
- src-satisfactorywiki-2026-blueprint-designer
- src-satisfactorywiki-2026-clock-speed
- src-satisfactorywiki-2026-drone

## Relations

**influenced by**

- [Factorio](../game/factorio.md)

**uses**

- [Production chains](../mechanic/production-chain.md) (core): Smelters, constructors, assemblers, manufacturers, refineries, and blenders run per-minute recipes; 106 alternate recipes chosen from hard-drive scans swap inputs, and clock speed from 1% to 250% rescales any machine.
- [Conveyor transport](../mechanic/conveyor-transport.md) (core): Six belt tiers carry 60, 120, 270, 480, 780, and 1,200 items per minute, with splitters, mergers, lifts, and smart splitters routing flows in 3D.
- [Resource extraction](../mechanic/resource-extraction.md) (core): Miners Mk.1 to Mk.3 sit on infinite ore nodes whose purity multiplies output by 0.5, 1, or 2; water extractors, oil extractors, and resource well pressurizers tap fluids.
- [Power grid](../mechanic/power-grid.md) (core): Generators from 30 MW biomass burners to 2,500 MW nuclear plants feed one grid; if consumption exceeds production with storage empty, the fuse trips and all connected buildings stop until reset.
- [Tech tree](../mechanic/tech-tree.md) (core): HUB milestones are unlocked by delivering crafted parts tier by tier, Space Elevator phases gate tiers 3 to 9, and the MAM researches alien items, power slugs, and hard drives.
- [Direct avatar control](../mechanic/direct-avatar.md) (core): The pioneer walks, jetpacks, ziplines, and drives across a hand-built map, building only within reach and gathering power slugs, hard drives, and samples on foot.
- [Building placement](../mechanic/free-placement.md) (supporting): Foundations, walls, and ramps snap to a grid at any height, so factories are stacked floors connected by belt lifts and pipes.
- [Fluid pipe networks](../mechanic/fluid-pipe-network.md) (supporting): Pipelines carry 300 or 600 m3 per minute; liquids need head lift supplied by pumps, while gases do not.
- [Vehicle routes and schedules](../mechanic/vehicle-route-scheduling.md) (supporting): Trains follow station timetables, trucks and tractors replay recorded routes, and drones shuttle between a home port and one linked port on battery or packaged fuel.
- [Rail signaling](../mechanic/rail-signaling.md) (supporting): Block and path signals divide track so several trains can share a network.
- [Blueprints](../mechanic/blueprints.md) (supporting): A Blueprint Designer (40 x 40 m at Mk.1, larger tiers in 1.0) saves layouts that appear as build-menu entries and draw materials from storage or inventory.
- [Storage and buffers](../mechanic/storage-capacity.md) (supporting): Storage containers, fluid buffers, and industrial tanks buffer production; the Dimensional Depot uploads items for remote building.
- [Byproducts and waste](../mechanic/byproducts-waste.md) (supporting): Refinery recipes emit heavy oil residue or polymer resin that must be routed or the line backs up, and nuclear plants emit waste that has to be stored or reprocessed.
- [Hand crafting](../mechanic/hand-crafting.md) (supporting): Early parts are crafted at a craft bench by holding a button, and equipment is made at the equipment workshop.
- [Modding API](../mechanic/modding-api.md) (supporting): The community-run Satisfactory Mod Loader adds new buildings, recipes, and logic on top of the Unreal Engine game.
- [Megaproject sink](../mechanic/megaproject-sink.md) (supporting): The Space Elevator takes five Project Assembly phases of crafted parts, from 50 Smart Plating in phase 1 to Nuclear Pasta and Ballistic Warp Drives in phase 5, and its phases unlock tiers 3 to 9 and the ending.
- [Machine boosting](../mechanic/machine-boosting.md) (supporting): Clock speed from 1% to 250% rescales any machine; each of up to three Power Shards raises the cap by 50 points, and power scales with exponent about 1.32, so 250% draws about 336% of base power.
- [Programming by demonstration](../mechanic/programming-by-demonstration.md) (supporting): Trucks and tractors replay a route the player records by driving it once, stopping at truck stations along the recorded path.

## Backlinks (computed)

**precedent for:** [Bottleneck explainer for production networks](../opportunity/bottleneck-explainer.md), [Generated recipe graphs](../opportunity/generated-recipe-graphs.md), [Teachable sim companion](../opportunity/teachable-sim-companion.md)

## Claims

- Press coverage compares Satisfactory's building to Factorio, and the game is widely treated as a 3D first-person take on Factorio's factory loop; the cited source records the comparison rather than a developer statement of influence. *(confidence: medium)* [[33](../source/src-wikipedia-satisfactory.md)]

## Sources

- [Satisfactory](../source/src-wikipedia-satisfactory.md)
- [Resource node](../source/src-satisfactorywiki-2026-resource-node.md)
- [Conveyor Belts](../source/src-satisfactorywiki-2026-conveyor-belts.md)
- [Power](../source/src-satisfactorywiki-2026-power.md)
- [Alternate recipes](../source/src-satisfactorywiki-2026-alternate-recipes.md)
- [Space Elevator](../source/src-satisfactorywiki-2026-space-elevator.md)
- [Pipeline](../source/src-satisfactorywiki-2026-pipeline.md)
- [Blueprint Designer](../source/src-satisfactorywiki-2026-blueprint-designer.md)
- [Clock speed](../source/src-satisfactorywiki-2026-clock-speed.md)
- [Drone](../source/src-satisfactorywiki-2026-drone.md)

---
Provenance: created in run `2026-10-24-catalog-gh`.
