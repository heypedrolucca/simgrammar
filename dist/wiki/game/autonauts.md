# Autonauts

*Game* · `autonauts` · status: **sourced**

A colony automation game in which the player crafts workerbots from parts and teaches them farming, crafting, and cooking routines in a Scratch-style visual language, so that bots supply the food, housing, and care that a growing population of Folk needs.

| field | value |
|---|---|
| year | 2019 |
| developer | Denki |
| platforms | PC, Console, Handheld |
| subgenre | Programming sim |
| subgenre secondary | Factory / automation, Farming sim |
| sim domain | Computational / abstract, Industrial / logistics, Biological / ecological |
| player role | Programmer |
| agency model | Direct avatar, Programmatic |
| time model | Real-time |
| sim scale | Settlement |
| fidelity | Stylized |
| perspective | Free 3D camera |
| win structure | Open sandbox |
| failure model | Soft / recoverable |
| narrative mode | None |
| multiplayer | Single-player |
| modding | Content |
| production tier | Indie |
| agent count order | ~100 |
| emergence | 2 |
| influence | 1 |
| influenced by |  |
| cluster *(computed)* | C06 |
| core count *(computed)* | 5 |
| mechanic count *(computed)* | 12 |

## Summary

A colony automation game in which the player crafts workerbots from parts and teaches them farming, crafting, and cooking routines in a Scratch-style visual language, so that bots supply the food, housing, and care that a growing population of Folk needs.

## Core Loop

gather sticks and stone by hand -> craft tools and a workerbot -> teach the bot a task by demonstrating it -> edit the visual script into a loop -> chain bots into farming, crafting, and cooking lines -> supply Folk with food, housing, and care -> unlock new buildings and bot parts

## Design Notes

Autonauts, from Denki and designers Gary Penn and Aaron Puzey, makes automation a matter of teaching: the player performs an action while a bot watches, the bot records it as blocks in a Scratch-style visual language, and the player adds repeat loops and conditions so the routine runs unattended. Programs are bounded by bot hardware: the head sets maximum instructions (12 at Mk 0 to 32 at Mk 3, raised by brain upgrades) and search range, the body sets hand, backpack, and upgrade slots, and the drive sets speed, battery, and recharge time, so better routines need better-built bots. Folk are the demand side, consuming food that lasts from 10 seconds for water to 120 seconds for apple pie or cooked fish and needing housing and baths, and they are either fully happy or unhappy. Colonise mode introduces components step by step, while Free and Creative modes unlock everything.

## Sources

- src-wikipedia-autonauts
- src-steam-2026-autonauts
- src-scottishgames-2019-autonauts-out-now
- src-autonautswiki-2026-bots
- src-autonautswiki-2026-folk
- src-dekudeals-2026-autonauts

## Relations

**uses**

- [Player programming](../mechanic/player-programming.md) (core): Bots learn a task by recording the player's demonstrated actions as Scratch-style blocks that the player edits into loops and conditions; the bot's head caps the number of instructions at 12 to 32 plus brain upgrades.
- [Modular assembly](../mechanic/modular-assembly.md) (core): Bots are built from a head, body, and drive at Mk 0 to Mk 3 that set instruction limit and search range, hand and backpack slots, and speed, battery, and recharge time, with upgrade slots for brain, sensor, speed, and energy parts.
- [Production chains](../mechanic/production-chain.md) (core): Workbenches and crafting stations turn crops, clay, wood, and other materials into tools, pottery, baked food, and clothing through multi-step recipes that bots run in chains.
- [Goods consumption](../mechanic/goods-consumption.md) (core): Housed Folk consume food whose satiation lasts from 10 seconds (water) to 120 seconds (apple pie, cooked fish) and need baths after messy meals; each Folk is either fully happy or unhappy.
- [Hand crafting](../mechanic/hand-crafting.md) (supporting): The Autonaut harvests sticks and stone and crafts the first tools, workbenches, and bot parts from blueprints before bots take over.
- [Crop cultivation](../mechanic/crop-cultivation.md) (supporting): Bots plant, grow, and harvest crops that feed cooking chains.
- [Animal husbandry](../mechanic/animal-husbandry.md) (supporting): Animal husbandry and fishing supply food and materials alongside farming.
- [Tech tree](../mechanic/tech-tree.md) (supporting): Research unlocks new buildings, recipes, and bot parts, and bots can be programmed to do science.
- [Direct avatar control](../mechanic/direct-avatar.md) (supporting): The player's Autonaut walks the map, carries items, and performs each task once so bots can learn it.
- [Modding API](../mechanic/modding-api.md) (supporting): Players share Automods, including bots and scripts, on Steam Workshop.
- [Execution budget](../mechanic/execution-budget.md) (supporting): A bot's head caps its program at 12 to 32 instructions, raised by brain upgrades, so longer routines need better-built bots.
- [Programming by demonstration](../mechanic/programming-by-demonstration.md) (core): Bots watch the player perform a task and record it as Scratch-style blocks, which the player edits into loops and conditions; this teaching step is the game's main interface to automation.

## Backlinks (computed)

**precedent for:** [Teachable sim companion](../opportunity/teachable-sim-companion.md)

## Claims

- A public demo was released on itch.io on 2017-07-05 and the full PC game on Steam on 2019-10-17; `year` records the 2019 release rather than the demo. Nintendo Switch, PlayStation 4, and Xbox One versions released on 2022-06-16. *(confidence: medium)* [[1](../source/src-wikipedia-autonauts.md), [2](../source/src-steam-2026-autonauts.md), [3](../source/src-dekudeals-2026-autonauts.md)]

## Sources

- [Autonauts (Denki article)](../source/src-wikipedia-autonauts.md)
- [Autonauts](../source/src-steam-2026-autonauts.md)
- [OUT NOW: Autonauts (Denki)](../source/src-scottishgames-2019-autonauts-out-now.md)
- [Bots](../source/src-autonautswiki-2026-bots.md)
- [Folk](../source/src-autonautswiki-2026-folk.md)
- [Autonauts](../source/src-dekudeals-2026-autonauts.md)

---
Provenance: created in run `2026-10-24-catalog-gh`.
