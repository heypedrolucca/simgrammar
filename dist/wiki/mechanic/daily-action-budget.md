# Daily action budget

*Mechanic* · `daily-action-budget` · status: **sourced**

A per-day pool of energy, stamina, or time slots limits how many actions the player can take, and the day's end resets it and forces prioritization.

| field | value |
|---|---|
| aliases | stamina budget, energy bar, time slots |
| family | Time & pacing |
| substrate | Aggregate stocks, Rule system |
| math basis | Optimization, Scheduling |
| feedback | None |
| player interface | Direct manipulation, Choice / cards |
| legibility | 4 |
| emergence potential | 2 |
| authoring cost | 1 |
| compute cost | 1 |
| tuning difficulty | 3 |
| ai leverage | 1 |
| maturity | Classic |
| open questions | Can generated daily events or requests keep each day's allocation decision fresh without hand-authored content? |
| core count *(computed)* | 3 |
| earliest game *(computed)* | [Princess Maker 2](../game/princess-maker-2.md) |
| earliest year *(computed)* | 1993 |
| prevalence *(computed)* | 5 |
| prevalence share *(computed)* | 0.029 |
| subgenre spread *(computed)* | 3 |
| technique count *(computed)* | 0 |
| technique exposure *(computed)* | 0.0 |

## Definition

Owns a budget that refills at the start of each in-game day (energy points, stamina, clock hours, or a fixed number of time slots) and a cost per action. Actions spend from the budget; at zero the player is penalized or the day ends, and sleep restores the budget, sometimes less after staying up late. Stardew Valley gives 270 base energy, raised by Stardrops, charges energy for tool use, exhausts the farmer at 0, and makes them pass out at -15 energy or at 2 a.m.; passing out away from home costs 10% of gold up to 1,000g, and going to bed after midnight restores less. Harvest Moon set the stamina-and-clock farm day that Stardew Valley follows; Persona allocates a fixed number of time slots per day to activities. Inputs are action costs and restoration items; outputs are the actions completed per day.

## Player Experience

Every morning is a planning puzzle. The player picks which crops to water, whom to visit, or which job to take, knowing the rest must wait. The end of each day gives a natural stopping point and a sense of steady progress, and upgrades that stretch the budget feel substantial.

## Design Levers

- budget size and whether it grows with progression
- cost per action and which actions are free
- penalties at or past zero and for staying up late
- restoration sources within the day, such as food
- time slots versus a continuous pool

## Failure Modes

- A budget that is too tight early makes the opening a grind; one that grows too fast stops mattering by midgame.
- When one activity has the best return per point, every day becomes the same routine.
- Harsh pass-out penalties push players to reload rather than accept a bad day.

## Dynamics

- Players batch tasks spatially to save time, which shapes farm and base layout.
- Budget-expanding items become top priorities, forming an upgrade path.
- Automation such as sprinklers frees the budget from chores for new activities, marking progression.

## Open Questions

- Can generated daily events or requests keep each day's allocation decision fresh without hand-authored content?

## Backlinks (computed)

**used by:** [Hardspace: Shipbreaker](../game/hardspace-shipbreaker.md), [Harvest Moon](../game/harvest-moon.md), [Papers, Please](../game/papers-please.md), [Princess Maker 2](../game/princess-maker-2.md), [Stardew Valley](../game/stardew-valley.md)

## Sources

- [Energy](../source/src-stardewvalleywiki-2026-energy.md)

---
Provenance: created in run `2026-10-24-taxonomy-m5`.
