# Player programming

*Mechanic* · `player-programming` · status: **sourced**

The player writes code in a language the game executes to control units, machines, or the world.

| field | value |
|---|---|
| aliases | scripting, coding gameplay, programming puzzles |
| family | Control & automation |
| substrate | Player-authored logic |
| math basis | Computation theory |
| feedback | Reinforcing (positive) |
| player interface | Programming |
| legibility | 3 |
| emergence potential | 3 |
| authoring cost | 2 |
| compute cost | 3 |
| tuning difficulty | 3 |
| ai leverage | 4 |
| maturity | Established |
| core count *(computed)* | 7 |
| earliest game *(computed)* | [Second Life](../game/second-life.md) |
| earliest year *(computed)* | 2003 |
| prevalence *(computed)* | 10 |
| prevalence share *(computed)* | 0.057 |
| subgenre spread *(computed)* | 5 |
| technique count *(computed)* | 2 |
| technique exposure *(computed)* | 0.5 |

## Definition

The player authors programs in a textual or visual language that the game interprets each tick to drive entities. State owned: program source, interpreter state (instruction pointer, registers, memory), and an execution budget. Update rule: each tick, run each program for up to a budget of instructions or CPU time, read sensors through an API, and issue commands that the simulation resolves. Languages range from real ones (JavaScript in Screeps and Bitburner, Python-like code in The Farmer Was Replaced) to assembly-like puzzle languages (TIS-100, Shenzhen I/O, Exapunks) and visual instruction tracks (SpaceChem waldos, Opus Magnum arms). Screeps is canonical for a persistent world: each player's main module runs once per tick against a fixed state, commands are applied together at tick end, and a CPU limit with a carryover bucket constrains computation.

## Player Experience

The player designs behavior rather than performing it. Writing, running, and debugging a program that then works unattended is satisfying in a way direct control is not, and failures are logic errors the player can find and fix.

## Design Levers

- language: real general-purpose, constrained assembly, or visual
- execution budget per tick (instructions or CPU milliseconds)
- sensor and actuator API surface
- debugging tools: stepping, logs, breakpoints, visualization
- persistence: programs keep running while the player is offline
- scoring of programs by size, speed, or cost

## Failure Modes

- A steep entry cost excludes players who cannot already program.
- A real language with a rich API lets players import libraries and copied code, so the community's code replaces the puzzle.
- Execution budgets set too tight make debugging feel like fighting the platform.
- Weak debugging tools turn failures into opaque guessing.

## Dynamics

- Automation through code lets players operate at scales no one could control by hand.
- In shared worlds, players' programs compete directly, producing an arms race of strategies and exploits.
- Code sharing builds communities around libraries and frameworks.

## Open Questions

- When code assistants can write competent bots from a description, what remains of the programming puzzle, and does play shift to specification and review?
- Can games teach programming effectively by letting AI assistants scaffold and then withdraw?

## Relations

**synergy**

- [Signal circuits](../mechanic/signal-circuits.md): Both express automation as logic; games that offer both span visual and textual programming.

## Backlinks (computed)

**affected by:** [LLM-guided evolutionary program search](../technique/alphaevolve-algorithm-discovery.md), [LLM-written skill libraries (Voyager)](../technique/voyager-skill-libraries.md)

**involved in:** [Mechanic modding by description](../opportunity/language-modding.md), [Specification programming games](../opportunity/specification-programming-games.md), [Teachable sim companion](../opportunity/teachable-sim-companion.md)

**required by:** [Execution budget](../mechanic/execution-budget.md)

**used by:** [Autonauts](../game/autonauts.md), [Bitburner](../game/bitburner.md), [Mindustry](../game/mindustry.md), [Opus Magnum](../game/opus-magnum.md), [Screeps](../game/screeps.md), [Second Life](../game/second-life.md), [Space Engineers](../game/space-engineers.md), [SpaceChem](../game/spacechem.md), [Stationeers](../game/stationeers.md), [The Farmer Was Replaced](../game/the-farmer-was-replaced.md)

## Claims

- In Screeps each player's main module runs once per tick against a fixed game state, and queued commands are applied together at the end of the tick. *(confidence: high)* [[82](../source/src-screeps-2026-docs-game-loop.md)]
- Screeps limits CPU per tick (20 without CPU Unlock), with unused CPU accumulating into a bucket of up to 10,000 that allows bursts up to 500 per tick. *(confidence: high)* [[83](../source/src-screeps-2026-docs-cpu-limit.md)]

## Sources

- [Understanding game loop, time and ticks](../source/src-screeps-2026-docs-game-loop.md)
- [How does CPU limit work](../source/src-screeps-2026-docs-cpu-limit.md)

---
Provenance: created in run `2026-10-24-taxonomy-m6`.
