# Mindustry

*Game* · `mindustry` · status: **sourced**

An open-source automation tower defense game in which the player belts ore into factories that supply turrets, units, and the core against enemy waves while capturing campaign sectors on two planets, with an assembly-like logic language for controlling blocks and units.

| field | value |
|---|---|
| year | 2017 |
| developer | Anuke |
| platforms | PC, Mobile |
| subgenre | Factory / automation |
| sim domain | Industrial / logistics, Military / conflict |
| player role | Engineer / designer |
| agency model | Zoning / placement, Direct unit control, Programmatic |
| time model | Real-time with pause |
| sim scale | Settlement |
| fidelity | Abstract |
| perspective | Top-down / side 2D |
| win structure | Campaign |
| failure model | Hard restart |
| narrative mode | None |
| multiplayer | Single-player, Co-op, Competitive |
| modding | Scripting |
| production tier | Hobbyist / free |
| agent count order | ~100 |
| emergence | 3 |
| influence | 2 |
| influenced by | [Factorio](../game/factorio.md) |
| cluster *(computed)* | C02 |
| core count *(computed)* | 4 |
| mechanic count *(computed)* | 16 |

## Summary

An open-source automation tower defense game in which the player belts ore into factories that supply turrets, units, and the core against enemy waves while capturing campaign sectors on two planets, with an assembly-like logic language for controlling blocks and units.

## Core Loop

drill ore -> belt items to the core and factories -> build and supply turrets -> survive scheduled enemy waves -> research new blocks with core resources -> capture sectors and launch resources between them

## Design Notes

Mindustry began as a 2017 itch.io jam game and fuses Factorio-style belt logistics with tower defense: turrets consume belted ammunition, power, and coolant, so the factory's layout is the defense, and survival maps send progressively stronger waves at the core on a timer. Version 6 (2020) added RTS units built in factories and upgraded through reconstructors, and Mindustry Logic, an assembly-like language that runs on processor blocks, reads sensors and memory cells, and can bind and command units. The campaign spans Serpulo and Erekir with 35 hand-made maps and 250+ procedural sectors whose production continues while the player is elsewhere and is moved between sectors by launch pads. The game is GPL-3.0 and free from the author while also sold on Steam, so community servers, plugins, and mods are unrestricted.

## Relations

**influenced by**

- [Factorio](../game/factorio.md)

**uses**

- [Conveyor transport](../mechanic/conveyor-transport.md) (core): Conveyors, junctions, routers, sorters, overflow gates, and bridges move items from drills to the core, factories, and turret ammo inputs.
- [Production chains](../mechanic/production-chain.md) (core): Smelters, presses, kilns, separators, and mixers turn copper, lead, sand, coal, titanium, and thorium into graphite, silicon, plastanium, and surge alloy.
- [Raid defense](../mechanic/raid-defense.md) (core): Enemy waves spawn on a schedule and path toward the core; about 18 Serpulo and 10 Erekir turret types consume ammo items, liquids, or power, backed by walls, menders, and shield projectors.
- [Adaptive threat scaling](../mechanic/adaptive-threat-scaling.md) (supporting): Survival maps send progressively stronger waves with tougher unit types and bosses as wave numbers rise; the cited sources do not tie wave strength to the player's own wealth.
- [Resource extraction](../mechanic/resource-extraction.md) (core): Mechanical, pneumatic, laser, and airblast drills mine ore tiles at speeds set by drill tier and ore hardness, with optional water boosting.
- [Player programming](../mechanic/player-programming.md) (supporting): Micro, logic, and hyper processors run Mindustry Logic, an assembly-like language with one operation per instruction that reads sensors and memory cells, controls linked buildings and turrets, and binds units with ubind to command them.
- [Crisis countdown](../mechanic/crisis-countdown.md) (supporting): A visible timer counts down to the next wave, and wave timing can be changed in custom game rules.
- [Tech tree](../mechanic/tech-tree.md) (supporting): Over 250 technology blocks are researched by spending core resources along a tree that also gates campaign sectors.
- [Power grid](../mechanic/power-grid.md) (supporting): Combustion, steam, solar, thorium, and impact generators feed node-linked grids with batteries; turrets, shields, and factories draw power.
- [Fluid pipe networks](../mechanic/fluid-pipe-network.md) (supporting): Conduits carry water, slag, oil, and cryofluid; optional coolant and lubricant raise turret and factory rates.
- [Unit commands](../mechanic/unit-commands.md) (supporting): Since version 7 units can be selected and commanded RTS-style, while others follow default AI or logic control.
- [Blueprints](../mechanic/blueprints.md) (supporting): Schematics save layouts as shareable text and are traded on Steam Workshop.
- [Scenario objectives](../mechanic/scenario-objectives.md) (supporting): Campaign sectors set win conditions such as surviving a number of waves or destroying enemy cores on attack maps.
- [Modding API](../mechanic/modding-api.md) (supporting): The GPL-3.0 source allows unrestricted mods, and community servers run plugins for custom maps and game modes.
- [Machine boosting](../mechanic/machine-boosting.md) (supporting): Optional coolant and lubricant fed to turrets and factories raise their rates, and water boosts drill speed.
- [Building placement](../mechanic/free-placement.md) (supporting)

## Claims

- Mindustry was created for the April 2017 itch.io Metal Monstrosity game jam and came to Steam in 2019 (version 3, store date 2019-09-26). *(confidence: high)* [[25](../source/src-wikipedia-mindustry.md), [26](../source/src-steam-2026-mindustry.md)]
- Coverage compares Mindustry to Factorio, and its README describes it as an automation tower defense RTS; the influenced_by edge reflects that widely noted lineage rather than a developer statement. *(confidence: medium)* [[25](../source/src-wikipedia-mindustry.md), [27](../source/src-anuke-2026-mindustry-repository.md)]

## Sources

- [Mindustry](../source/src-wikipedia-mindustry.md)
- [Mindustry](../source/src-steam-2026-mindustry.md)
- [Mindustry source repository](../source/src-anuke-2026-mindustry-repository.md)
- [Mindustry Logic: Introduction](../source/src-mindustry-2026-logic-introduction.md)

---
Provenance: created in run `2026-10-24-catalog-gh`; reviewed in `2026-10-24-review-fixes`.
