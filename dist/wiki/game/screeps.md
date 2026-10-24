# Screeps

*Game* · `screeps` · status: **sourced**

A persistent MMO strategy game in which players control colonies only by writing JavaScript that the server runs every tick, directing creeps assembled from body parts to harvest energy, upgrade room controllers, trade, and fight other players' code under a CPU budget.

| field | value |
|---|---|
| year | 2014 |
| year full release | 2016 |
| developer | Screeps, LLC |
| platforms | PC, Web |
| subgenre | Programming sim |
| subgenre secondary | MMO world |
| sim domain | Computational / abstract, Military / conflict, Economic |
| player role | Programmer |
| agency model | Programmatic |
| time model | Asynchronous persistent |
| sim scale | Region |
| fidelity | Abstract |
| perspective | Top-down / side 2D |
| win structure | Open sandbox |
| failure model | Soft / recoverable |
| narrative mode | None |
| multiplayer | Persistent MMO, Competitive, Single-player |
| modding | Scripting |
| production tier | Indie |
| agent count order | ~100 |
| emergence | 3 |
| influence | 2 |
| influenced by |  |
| cluster *(computed)* | C06 |
| core count *(computed)* | 6 |
| mechanic count *(computed)* | 12 |

## Summary

A persistent MMO strategy game in which players control colonies only by writing JavaScript that the server runs every tick, directing creeps assembled from body parts to harvest energy, upgrade room controllers, trade, and fight other players' code under a CPU budget.

## Core Loop

write and commit JavaScript -> each tick the script reads room state and issues orders -> creeps harvest energy for spawns, extensions, and the controller -> controller levels unlock structures -> claim and defend rooms against other players' code -> profile and rewrite code within the CPU limit

## Design Notes

Screeps removes direct control entirely: the only input to the persistent world is the player's main module, which the server runs once per tick against a fixed snapshot, queuing commands that resolve together at tick end, so the colony keeps acting while the player is offline. Computation is the scarce resource: each tick has a CPU limit (20 without CPU Unlock, otherwise rising with Global Control Level to 300), with unused CPU banked in a 10,000-unit bucket that allows bursts of up to 500. Creeps are designed in code as bodies of up to 50 parts (WORK, CARRY, MOVE, ATTACK, RANGED_ATTACK, HEAL, CLAIM, TOUGH) that set cost, ability, and fatigue, and they die after 1,500 ticks, so a colony is a replacement pipeline. Room Controller Levels 1 to 8 unlock structures and decay if not fed energy, and every player's AI meets the others in shared 50x50 rooms, so strategy is emergent competition between programs. The server is open source and runnable privately.

## Sources

- src-steam-2026-screeps-world
- src-screeps-2026-docs-introduction
- src-screeps-2026-docs-creeps
- src-screeps-2026-docs-control
- src-screeps-2026-docs-market
- src-screeps-2026-docs-cpu-limit
- src-screeps-2026-docs-game-loop
- src-screeps-2014-indiegogo-updates
- src-screeps-2015-game-situation-review
- src-screeps-2016-private-server-released

## Relations

**uses**

- [Player programming](../mechanic/player-programming.md) (core): Players write JavaScript (or C, C++, Rust, Go, C#, and others via WebAssembly) whose main loop runs every tick under a per-tick CPU limit with a 10,000-unit bucket; globals reset between ticks and actions resolve together at tick end.
- [Persistent shared world](../mechanic/persistent-world.md) (core): Official shards run continuously with ticks every 2 to 5 seconds, so colonies harvest, build, and fight while their owners are offline; rooms link through exits and shards through portals.
- [Modular assembly](../mechanic/modular-assembly.md) (core): Code spawns creeps from up to 50 body parts of eight types; part counts set harvest, carry, attack, and heal rates, MOVE parts offset fatigue of 1, 2, or 10 per part on road, plain, or swamp, and each part has 100 hits.
- [Resource extraction](../mechanic/resource-extraction.md) (core): WORK parts harvest energy from sources that refill every 300 ticks, and extractors at RCL 6 mine minerals for labs and the market.
- [Tech tree](../mechanic/tech-tree.md) (core): Energy spent on a room controller raises its level from 1 to 8 at cumulative costs up to 10.9 million, unlocking spawns, extensions, towers, storage, links, labs, terminal, factory, observer, and nuker; unfed controllers downgrade and become neutral.
- [Raid defense](../mechanic/raid-defense.md) (supporting): Towers, ramparts, and walls defend rooms against other players and NPC invaders, and a newly placed first spawn grants safe mode.
- [Player-driven markets](../mechanic/player-driven-market.md) (supporting): Terminals post public buy and sell orders priced in credits with a 5% order fee; the party executing a deal pays an energy cost that grows with distance, and NPC terminals sit at highway crossroads.
- [Agent pathfinding](../mechanic/agent-pathfinding.md) (supporting): Movement costs are 1 on roads, 2 on plains, and 10 on swamps, and route searches consume the player's CPU, so caching paths is a core optimization.
- [Wear and breakdown](../mechanic/wear-breakdown.md) (supporting): Roads and other structures lose hits over time and must be repaired by creeps.
- [Lifecycle and aging](../mechanic/lifecycle-aging.md) (supporting): Every creep dies after 1,500 ticks, so code must schedule replacements before roles go unfilled.
- [Modding API](../mechanic/modding-api.md) (supporting): The open-source private server supports mods and community servers that change rules and tick rates.
- [Execution budget](../mechanic/execution-budget.md) (core): Each tick has a CPU limit (20 without CPU Unlock), unused CPU banks in a bucket of up to 10,000, a tick may burst to 500, and scripts are terminated at the limit, so pathfinding and caching strategies are shaped by CPU cost.

## Backlinks (computed)

**precedent for:** [Simulation games as agent benchmarks](../opportunity/sims-as-agent-benchmarks.md), [Specification programming games](../opportunity/specification-programming-games.md)

## Claims

- In late 2014 Screeps was publicly playable in its browser Simulation mode during its Indiegogo campaign, and a December 2015 post dates the initial launch a year earlier; the persistent MMO opened to backers in May 2015, and the Steam full release followed on 2016-11-16. `year` records the 2014 public launch. *(confidence: medium)* [[34](../source/src-screeps-2014-indiegogo-updates.md), [35](../source/src-screeps-2015-game-situation-review.md), [36](../source/src-screeps-2016-private-server-released.md), [37](../source/src-steam-2026-screeps-world.md)]

## Sources

- [Screeps: World](../source/src-steam-2026-screeps-world.md)
- [Introduction](../source/src-screeps-2026-docs-introduction.md)
- [Creeps](../source/src-screeps-2026-docs-creeps.md)
- [Control](../source/src-screeps-2026-docs-control.md)
- [Market](../source/src-screeps-2026-docs-market.md)
- [How does CPU limit work](../source/src-screeps-2026-docs-cpu-limit.md)
- [Understanding game loop, time and ticks](../source/src-screeps-2026-docs-game-loop.md)
- [Screeps blog: Indiegogo updates, November 2014 to February 2015](../source/src-screeps-2014-indiegogo-updates.md)
- [Game situation review: December 11, 2015](../source/src-screeps-2015-game-situation-review.md)
- [Screeps private server released!](../source/src-screeps-2016-private-server-released.md)

---
Provenance: created in run `2026-10-24-catalog-gh`.
