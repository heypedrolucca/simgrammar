# Factorio

*Game* · `factorio` · status: **sourced**

A factory automation game in which the player builds belt, train, robot, and circuit networks that mine, refine, and assemble items on an alien planet while pollution provokes native biters that evolve over time.

| field | value |
|---|---|
| year | 2013 |
| year full release | 2020 |
| developer | Wube Software |
| platforms | PC, Console, Handheld |
| subgenre | Factory / automation |
| sim domain | Industrial / logistics, Computational / abstract, Military / conflict |
| player role | Engineer / designer |
| agency model | Direct avatar, Zoning / placement, Programmatic |
| time model | Real-time |
| sim scale | Facility |
| fidelity | Stylized |
| perspective | Top-down / side 2D |
| win structure | Open sandbox |
| failure model | Soft / recoverable |
| narrative mode | None |
| multiplayer | Single-player, Co-op, Competitive |
| modding | Total conversion |
| production tier | Indie |
| agent count order | ~1,000 |
| emergence | 3 |
| influence | 4 |
| influenced by | [Minecraft](../game/minecraft.md) |
| cluster *(computed)* | C02 |
| core count *(computed)* | 8 |
| mechanic count *(computed)* | 28 |

## Summary

A factory automation game in which the player builds belt, train, robot, and circuit networks that mine, refine, and assemble items on an alien planet while pollution provokes native biters that evolve over time.

## Core Loop

mine ore -> smelt and assemble on belts and inserters -> feed science packs to labs -> research new machines -> pollution draws biter attacks -> defend and expand outposts by rail -> launch a rocket

## Design Notes

Lead designer Michal Kovarik cited the Minecraft tech mods IndustrialCraft and BuildCraft; Factorio turned their pipes and machines into a standalone game where ratio planning and layout are the challenge. Item movement is discrete and deterministic (belts carry 15, 30, 45, or 60 items per second across two lanes), which makes throughput legible and lets the lockstep multiplayer simulate identical worlds. Pollution couples industry to combat: chunks above 15 units diffuse 2% to neighbors, spawners that absorb it send attack groups, and total pollution produced drives the enemy evolution factor. Each layer of logistics (belts, trains with block signals, roboport-based logistic and construction robots, circuit combinators) is a mechanic the player adopts when the previous one stops scaling, and blueprints let solved layouts be reused. Speed, productivity, and efficiency modules and beacons that trade power for throughput, and the rocket silo as a terminal sink for produced parts, have no taxonomy entry; this run proposed both.

## Sources

- src-wikipedia-factorio
- src-rose-2014-factorio-trailer
- src-factoriowiki-2026-enemies
- src-factoriowiki-2026-pollution
- src-factoriowiki-2026-transport-belt-physics
- src-factoriowiki-2026-electric-system
- src-factoriowiki-2026-crude-oil
- src-factoriowiki-2026-rail-signal
- src-factoriowiki-2026-logistic-network
- src-factoriowiki-2026-space-age
- src-wube-2015-fff-88-combinators
- src-wube-2016-fff-170-blueprint-library
- src-wube-2023-fff-375-quality
- src-wube-2024-fff-414-spoils-of-agriculture
- src-wube-2024-fff-416-fluids
- src-wube-2026-factorio-lua-api

## Relations

**influenced by**

- [Minecraft](../game/minecraft.md)

**uses**

- [Production chains](../mechanic/production-chain.md) (core): Assembling machines, furnaces, chemical plants, and refineries run fixed recipes with crafting times; science packs require multi-step trees from ore to circuits, oil products, and rocket parts.
- [Conveyor transport](../mechanic/conveyor-transport.md) (core): Two-lane belts in four tiers carry 15, 30, 45, or 60 items per second; splitters, undergrounds, and lane priorities shape flow, and inserters move items between belts and machines.
- [Tech tree](../mechanic/tech-tree.md) (core): Labs consume science packs of rising recipe complexity to research a technology graph that leads through oil processing, robots, and nuclear power to the rocket silo.
- [Resource extraction](../mechanic/resource-extraction.md) (core): Electric and burner mining drills extract iron, copper, coal, stone, and uranium from ore patches at rates set by drill tier and mining productivity research; pumpjacks extract crude oil.
- [Pollution spread](../mechanic/pollution-spread.md) (core): Machines emit pollution into 32x32 chunks; above 15 units a chunk diffuses 2% to each cardinal neighbor every 64 ticks, and water, grass, and trees absorb it.
- [Raid defense](../mechanic/raid-defense.md) (core): Biter and spitter nests send attack groups when their chunk absorbs pollution, recruiting units at pollution costs from 4 for a small biter to 400 for a behemoth; turrets, walls, and flamethrowers defend.
- [Adaptive threat scaling](../mechanic/adaptive-threat-scaling.md) (core): An evolution factor rises with elapsed time, total pollution produced, and spawners destroyed, squashed as total over one plus total, and unlocks medium, big, and behemoth enemies.
- [Power grid](../mechanic/power-grid.md) (core): Steam engines, solar panels, accumulators, and nuclear reactors feed a pole-connected grid; under shortage power is shared evenly so all machines slow proportionally.
- [Blueprints](../mechanic/blueprints.md) (supporting): Selected areas save to blueprints, books, and a personal library that persists across saves; exchange strings are shared online, and construction robots build pasted ghosts.
- [Rail signaling](../mechanic/rail-signaling.md) (supporting): Rail and chain signals divide track into blocks that one train reserves at a time, letting train networks share track.
- [Vehicle routes and schedules](../mechanic/vehicle-route-scheduling.md) (supporting): Trains run schedules of stations with wait conditions on cargo, time, inactivity, or circuit signals.
- [Signal circuits](../mechanic/signal-circuits.md) (supporting): Red and green wires carry item-count signals into arithmetic, decider, constant, and (in 2.0) selector combinators that control inserters, belts, train stops, and lamps.
- [Fluid pipe networks](../mechanic/fluid-pipe-network.md) (supporting): Pipes and pumps carry water, crude oil, petroleum, and steam; version 2.0 merged pipes into segments that share contents.
- [Deposit depletion](../mechanic/deposit-depletion.md) (supporting): Ore tiles run out as they are mined, and crude oil wells decline toward a 20% yield floor, pushing expansion to new patches.
- [Storage and buffers](../mechanic/storage-capacity.md) (supporting): Chests, storage tanks, and the logistic network's storage chests buffer items, and full outputs stall machines upstream.
- [Hand crafting](../mechanic/hand-crafting.md) (supporting): The engineer crafts early buildings and items from inventory using the same recipes as assemblers, with a crafting queue.
- [Quality tiers](../mechanic/quality-tiers.md) (supporting): The Space Age expansion adds five quality levels from normal to legendary, raised by chance from quality modules, with a recycler that returns 25% of ingredients.
- [Spoilage](../mechanic/spoilage.md) (supporting): In Space Age, Gleba's agricultural products spoil over fixed timers into spoilage, and recipe outputs inherit ingredient freshness.
- [Modding API](../mechanic/modding-api.md) (supporting): Mods use a modified Lua 5.2 with data and control stages and are distributed through an in-game mod portal; overhauls such as Krastorio 2 replace progression.
- [Stats dashboards](../mechanic/stats-dashboards.md) (supporting): Production and consumption graphs per item over time windows and an electric network panel show where ratios fail.
- [Procedural terrain](../mechanic/procedural-terrain.md) (supporting): Maps are generated from a seed with settings for ore frequency, size, and richness, water, cliffs, and enemy bases.
- [Vertical layers](../mechanic/vertical-layers.md) (supporting): Space Age elevated rails let a second track layer cross over ground tracks and buildings.
- [Direct avatar control](../mechanic/direct-avatar.md) (supporting): The engineer walks the map, mines by hand early, and places buildings within reach, later driving cars, tanks, and spidertrons.
- [Megaproject sink](../mechanic/megaproject-sink.md) (supporting): The rocket silo consumes rocket parts for each launch, and launching a rocket ends the base game; Space Age moves the goal to a space platform reaching the edge of the solar system.
- [Machine boosting](../mechanic/machine-boosting.md) (supporting): Speed, productivity, efficiency, and (Space Age) quality modules fill machine slots, and beacons project module effects onto neighboring machines at a power cost; productivity bonuses are capped at +300%.
- [Request-provider logistics](../mechanic/request-provider-logistics.md) (supporting): Roboports define logistic zones where logistic robots carry items among active provider, passive provider, storage, buffer, and requester chests by priority, one item per trip at 3 tiles per second before research.
- [Track laying](../mechanic/track-laying.md) (supporting): Straight and curved rail pieces are placed to build train networks, with elevated rails in Space Age, and the rail planner lays segments between points.
- [Building placement](../mechanic/free-placement.md) (supporting)

## Backlinks (computed)

**influenced:** [Mindustry](../game/mindustry.md), [Satisfactory](../game/satisfactory.md)

**precedent for:** [Bottleneck explainer for production networks](../opportunity/bottleneck-explainer.md), [Event-sourced simulation runtime](../opportunity/event-sourced-sim-runtime.md), [Generated recipe graphs](../opportunity/generated-recipe-graphs.md), [Mechanic modding by description](../opportunity/language-modding.md), [Automated mechanic discovery](../opportunity/mechanic-discovery-search.md), [Parallel autobalancing of economies](../opportunity/parallel-autobalance.md), [Simulation games as agent benchmarks](../opportunity/sims-as-agent-benchmarks.md), [Teachable sim companion](../opportunity/teachable-sim-companion.md)

## Claims

- Factorio was publicly purchasable as an alpha from its official site in 2013, after the February 2013 Indiegogo campaign, three years before Steam early access on 2016-02-25; `year` records the 2013 alpha. *(confidence: medium)* [[19](../source/src-rose-2014-factorio-trailer.md), [20](../source/src-wikipedia-factorio.md)]
- The design grew out of the Minecraft tech mods IndustrialCraft and BuildCraft, which lead designer Michal Kovarik cited; the `influenced_by` edge to Minecraft records that mod lineage. *(confidence: high)* [[20](../source/src-wikipedia-factorio.md)]

## Sources

- [Factorio](../source/src-wikipedia-factorio.md)
- [How a single game trailer turned the tide for Factorio](../source/src-rose-2014-factorio-trailer.md)
- [Enemies](../source/src-factoriowiki-2026-enemies.md)
- [Pollution](../source/src-factoriowiki-2026-pollution.md)
- [Transport belts/Physics](../source/src-factoriowiki-2026-transport-belt-physics.md)
- [Electric system](../source/src-factoriowiki-2026-electric-system.md)
- [Crude oil](../source/src-factoriowiki-2026-crude-oil.md)
- [Rail signal](../source/src-factoriowiki-2026-rail-signal.md)
- [Logistic network](../source/src-factoriowiki-2026-logistic-network.md)
- [Space Age](../source/src-factoriowiki-2026-space-age.md)
- [Friday Facts #88 - Combinators](../source/src-wube-2015-fff-88-combinators.md)
- [Friday Facts #170 - Blueprint library GUI design and redesign](../source/src-wube-2016-fff-170-blueprint-library.md)
- [Friday Facts #375 - Quality](../source/src-wube-2023-fff-375-quality.md)
- [Friday Facts #414 - Spoils of Agriculture](../source/src-wube-2024-fff-414-spoils-of-agriculture.md)
- [Friday Facts #416 - Fluids 2.0](../source/src-wube-2024-fff-416-fluids.md)
- [Factorio Lua API documentation](../source/src-wube-2026-factorio-lua-api.md)

---
Provenance: created in run `2026-10-24-catalog-gh`; reviewed in `2026-10-24-review-fixes`.
