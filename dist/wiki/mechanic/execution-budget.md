# Execution budget

*Mechanic* · `execution-budget` · status: **sourced**

Player-written programs are metered against a simulated compute budget, such as CPU per tick, tick cost per operation, instruction slots, or RAM, which makes efficiency the scarce resource.

| field | value |
|---|---|
| aliases | CPU limit, instruction limit, tick cost, script RAM |
| family | Control & automation |
| substrate | Player-authored logic, Aggregate stocks |
| math basis | Computation theory, Optimization |
| feedback | Balancing (negative) |
| player interface | Programming, Observation only |
| legibility | 3 |
| emergence potential | 2 |
| authoring cost | 1 |
| compute cost | 1 |
| tuning difficulty | 3 |
| ai leverage | 3 |
| maturity | Established |
| requires | [Player programming](../mechanic/player-programming.md) |
| core count *(computed)* | 1 |
| earliest game *(computed)* | [Screeps](../game/screeps.md) |
| earliest year *(computed)* | 2014 |
| prevalence *(computed)* | 4 |
| prevalence share *(computed)* | 0.023 |
| subgenre spread *(computed)* | 1 |
| technique count *(computed)* | 0 |
| technique exposure *(computed)* | 0.0 |

## Summary

Player-written programs are metered against a simulated compute budget, such as CPU per tick, tick cost per operation, instruction slots, or RAM, which makes efficiency the scarce resource.

## Definition

Owns a compute budget and the cost charged against it: a per-tick allowance with an optional carryover bucket, a time cost per operation, or a fixed capacity such as instruction slots or memory. Each run or tick the game charges each operation or program its cost; when the budget runs out the program is terminated, throttled, or simply takes longer in game time, and unused allowance may accumulate. Screeps gives each player a CPU limit per tick (20 without CPU Unlock), banks unused CPU in a bucket of up to 10,000, lets a tick draw up to 500 from it, and terminates scripts at the limit. The Farmer Was Replaced charges simulated ticks per operation: literals and assignment are free, arithmetic costs 1, and a successful move() costs 200. Autonauts caps each bot's program at 12 to 32 instructions by its head part. Bitburner charges each script a RAM cost that must fit on the server running it. Player-programming owns the language and interpreter; this mechanic owns only the metering, so one language can run under tight, loose, or no budgets.

## Player Experience

Optimization becomes the game once the code works. Players profile, cache paths, batch work, and count moves, because the same behavior written more cheaply runs more units, farms faster, or fits on the bot. A routine that finally fits under the cap, or a tick that stops overrunning, feels like a real engineering win.

## Design Levers

- budget type: real CPU time, simulated tick cost per operation, instruction count, or memory
- size of the per-tick allowance and of a carryover bucket that allows bursts
- per-operation cost table, especially the ratio between cheap computation and expensive actions such as moves
- overrun consequence: termination, throttling, or slower simulated time
- how the budget grows: progression, hardware parts, or payment

## Failure Modes

- Budgets measured in real CPU time vary with server load, so the same code can pass or fail unpredictably.
- Budgets that are too tight make debugging feel like fighting the platform rather than solving the problem.
- When budget increases are bought, as with Screeps' CPU Unlock, competitive outcomes mix code quality with spending.
- Cost tables that charge almost nothing for computation let players brute-force problems the budget was meant to constrain.

## Dynamics

- Players adopt caching, memoization, and scheduling patterns that resemble real systems engineering.
- Expensive actions relative to computation push players toward code that plans a lot and acts rarely.
- Communities share profilers and optimized libraries, spreading efficient patterns across players.

## Open Questions

- When AI assistants write working code from a description, does the budget become the main remaining challenge, and does that keep programming games interesting?
- Which budget types (time per tick, cost per operation, memory) teach the most transferable efficiency skills?

## Relations

**requires**

- [Player programming](../mechanic/player-programming.md)

## Backlinks (computed)

**used by:** [Autonauts](../game/autonauts.md), [Bitburner](../game/bitburner.md), [Screeps](../game/screeps.md), [The Farmer Was Replaced](../game/the-farmer-was-replaced.md)

## Sources

- [How does CPU limit work](../source/src-screeps-2026-docs-cpu-limit.md)
- [Operation Costs](../source/src-tfwrwiki-2026-operation-costs.md)
- [Bots](../source/src-autonautswiki-2026-bots.md)

---
Provenance: created in run `2026-10-24-taxonomy-triage-b`.
