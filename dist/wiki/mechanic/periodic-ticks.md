# Periodic ticks

*Mechanic* · `periodic-ticks` · status: **sourced**

Some state changes, such as budgets, harvests, or growth, resolve in batches at fixed intervals like a month or a year rather than continuously.

| field | value |
|---|---|
| aliases | monthly tick, accounting period, yearly resolution |
| family | Time & pacing |
| substrate | Aggregate stocks, Rule system |
| math basis | System dynamics / ODEs, Scheduling |
| feedback | None |
| player interface | Observation only, Parameter |
| legibility | 4 |
| emergence potential | 1 |
| authoring cost | 1 |
| compute cost | 2 |
| tuning difficulty | 2 |
| ai leverage | 1 |
| maturity | Classic |
| open questions | Can learned surrogates settle long periods in one step so players can skip ahead without simulating every day? |
| core count *(computed)* | 1 |
| earliest game *(computed)* | [Utopia](../game/utopia.md) |
| earliest year *(computed)* | 1982 |
| prevalence *(computed)* | 4 |
| prevalence share *(computed)* | 0.023 |
| subgenre spread *(computed)* | 3 |
| technique count *(computed)* | 0 |
| technique exposure *(computed)* | 0.0 |

## Definition

Owns a period length and a set of update functions that run only when the period elapses. Between ticks the simulation runs continuously or not at all; at the tick, accumulated quantities settle: tax income and upkeep are booked, population grows, crops are harvested, research advances, or reports are produced. Hamurabi resolves a whole year per round: harvest, rats, immigration, plague, and starvation; SimCity books taxes and service funding at each year's budget; Paradox grand strategy games apply income and many modifiers on a monthly tick inside a daily simulation. Different systems can run on different periods in the same game. Inputs are activity accumulated during the period; outputs are discrete jumps in stocks and a report.

## Player Experience

Bookkeeping beats. The player watches the date approach the next settlement, makes changes just before it, and reads the report afterward to judge the period. Ticks create small moments of anticipation and give a long continuous game recurring checkpoints.

## Design Levers

- period length, and whether different systems use different periods
- which quantities settle at the tick and which change continuously
- what the player sees at the tick: reports, prompts, or a forced pause
- whether actions just before the tick can game the settlement

## Failure Modes

- Players time actions around a tick to exploit settlement rules, such as building just after upkeep is charged.
- Large batched computations at the tick cause visible stutter in late game.
- Long periods delay feedback until players cannot connect a decision to its result.

## Dynamics

- Batched income creates sawtooth cash curves, so players keep buffers to survive between ticks.
- Synchronized ticks across many agents produce simultaneous demand spikes.
- Reports at each tick become the main legibility tool for slow variables.

## Open Questions

- Can learned surrogates settle long periods in one step so players can skip ahead without simulating every day?

## Backlinks (computed)

**used by:** [Captain of Industry](../game/captain-of-industry.md), [Mini Metro](../game/mini-metro.md), [Railroad Tycoon](../game/railroad-tycoon.md), [Utopia](../game/utopia.md)

## Sources

- [Hamurabi (video game)](../source/src-wikipedia-hamurabi.md)

---
Provenance: created in run `2026-10-24-taxonomy-m5`.
