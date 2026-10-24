# Pause and speed control

*Mechanic* · `variable-speed` · status: **sourced**

The player pauses the simulation and switches between speed multipliers, trading attention against elapsed game time.

| field | value |
|---|---|
| aliases | real-time with pause, time compression, fast-forward |
| family | Time & pacing |
| substrate | Rule system |
| math basis | System dynamics / ODEs, Scheduling |
| feedback | None |
| player interface | Parameter |
| legibility | 5 |
| emergence potential | 1 |
| authoring cost | 1 |
| compute cost | 1 |
| tuning difficulty | 1 |
| ai leverage | 2 |
| maturity | Classic |
| open questions | Can learned surrogate simulators let players skip long quiet stretches without running full-fidelity ticks? |
| core count *(computed)* | 1 |
| earliest game *(computed)* | [Conway's Game of Life](../game/game-of-life.md) |
| earliest year *(computed)* | 1970 |
| prevalence *(computed)* | 19 |
| prevalence share *(computed)* | 0.109 |
| subgenre spread *(computed)* | 13 |
| technique count *(computed)* | 0 |
| technique exposure *(computed)* | 0.0 |

## Definition

Owns a time scale, paused or one of several multipliers, and the rule that converts real time into simulation ticks. At higher speeds the loop runs more ticks per real second up to hardware limits; while paused no ticks run but the player can still give orders. Some games pause or slow automatically on events. RimWorld runs 60 ticks per second at normal speed and multiplies that by 3, 6, or 15, the last only in development mode, and runs as close to the target as the machine allows; SimCity and Paradox grand strategy games offer pause and several speeds; flight simulators call it time compression. Inputs are the player's speed choice and event triggers; outputs are the tick rate of every other system.

## Player Experience

Control over attention. The player slows down or pauses for crises and detailed orders, then fast-forwards through quiet stretches such as waiting for crops or construction. Pause makes real-time games playable at a thoughtful pace, and fast-forward removes dead time.

## Design Levers

- number of speeds and their multipliers
- whether orders can be given while paused
- auto-pause and auto-slowdown triggers, such as raids or letters
- speed restrictions in multiplayer or during events
- whether higher speeds change simulation fidelity, such as larger time steps

## Failure Modes

- High speeds the hardware cannot sustain silently run slower than shown, so late-game fast-forward feels broken.
- Larger time steps at high speed can destabilize physics or give different outcomes than normal speed.
- Multiplayer games must reconcile players' speed preferences, often by host control or voting.

## Dynamics

- Players alternate between paused planning and fast-forward waiting, creating a two-tempo play pattern.
- Fast-forward exposes the compute cost of every other system, making simulation performance a gameplay issue.
- Auto-pause rules decide which events players notice.

## Open Questions

- Can learned surrogate simulators let players skip long quiet stretches without running full-fidelity ticks?

## Backlinks (computed)

**involved in:** [Branch preview of policy futures](../opportunity/branch-preview-forecasts.md)

**used by:** [Command: Modern Operations](../game/command-modern-operations.md), [Europa Universalis IV](../game/europa-universalis-4.md), [FTL: Faster Than Light](../game/ftl.md), [Conway's Game of Life](../game/game-of-life.md), [Hearts of Iron IV](../game/hearts-of-iron-4.md), [Kerbal Space Program](../game/kerbal-space-program.md), [Mini Metro](../game/mini-metro.md), [Motorsport Manager](../game/motorsport-manager.md), [Plague Inc.](../game/plague-inc.md), [Railroad Tycoon](../game/railroad-tycoon.md), [RimWorld](../game/rimworld.md), [Silent Hunter III](../game/silent-hunter-3.md), [SimEarth](../game/simearth.md), [SimLife](../game/simlife.md), [Species: Artificial Life, Real Evolution](../game/species-alre.md), [Stellaris](../game/stellaris.md), [The Powder Toy](../game/the-powder-toy.md), [Theme Park](../game/theme-park.md), [Universe Sandbox](../game/universe-sandbox.md)

## Sources

- [Time](../source/src-rimworldwiki-2026-time.md)
- [Turns, rounds and time-keeping systems in games](../source/src-wikipedia-turns-rounds-and-time-keeping.md)

---
Provenance: created in run `2026-10-24-taxonomy-m5`.
