# Crisis countdown

*Mechanic* · `crisis-countdown` · status: **sourced**

A known future crisis such as a storm, winter, cure, or deadline is announced in advance, and the remaining time structures preparation.

| field | value |
|---|---|
| aliases | doom clock, known deadline, preparation timer |
| family | Time & pacing |
| substrate | Rule system |
| math basis | Scheduling, Optimization |
| feedback | None |
| player interface | Observation only |
| legibility | 4 |
| emergence potential | 2 |
| authoring cost | 3 |
| compute cost | 1 |
| tuning difficulty | 3 |
| ai leverage | 3 |
| maturity | Established |
| open questions | Can a director model choose crises that target the player's actual weak points while keeping the warning fair? |
| core count *(computed)* | 7 |
| earliest game *(computed)* | [Project Zomboid](../game/project-zomboid.md) |
| earliest year *(computed)* | 2011 |
| prevalence *(computed)* | 10 |
| prevalence share *(computed)* | 0.057 |
| subgenre spread *(computed)* | 7 |
| technique count *(computed)* | 0 |
| technique exposure *(computed)* | 0.0 |

## Definition

Owns a countdown to a scheduled crisis (in days, turns, or progress percent), the crisis's nature, and sometimes its expected severity. Each tick the counter falls; at zero the crisis applies a large state change such as extreme cold, an attack, a flood, or a scenario loss, which the player's preparation mitigates. The timer may be fixed, randomized within a known window, or driven by a rival process the player can slow. Frostpunk's main scenario builds toward the Great Storm, and its Last Autumn scenario races to finish an outpost before a storm; Plague Inc. runs a cure-research percentage that ends the game when it completes; Don't Starve's winter arrives on a fixed schedule; The Legend of Zelda: Majora's Mask frames play around a three-day falling moon. Inputs are elapsed time and actions that shift the clock; outputs are the crisis and its severity.

## Player Experience

Dread and focus. Knowing what is coming and when, the player turns the remaining days into a plan: stockpile coal, insulate homes, finish the walls. The final days narrow choices to triage, and surviving feels earned because the preparation was the player's own.

## Design Levers

- warning lead time and whether the exact date is known
- crisis severity and whether it is shown in advance
- whether player actions can delay, accelerate, or weaken the crisis
- single climactic crisis versus recurring crises of rising strength
- failure handling: scenario loss, heavy damage, or partial survival

## Failure Modes

- A crisis with a fixed required preparation becomes a build order that players replay rather than a plan.
- Too much lead time removes tension; too little makes the crisis an unavoidable random event.
- A single climactic crisis gives a scenario a hard end and little reason to replay.

## Dynamics

- Players shift from expansion to stockpiling as the counter runs down, creating distinct phases within a run.
- Countdowns reward forecasting tools that project resource runways to the deadline.
- Recurring crises such as winters or droughts escalate into a cycle of preparation and recovery.

## Open Questions

- Can a director model choose crises that target the player's actual weak points while keeping the warning fair?

## Relations

**synergy**

- [Seasons](../mechanic/seasons.md): A known winter or storm turns the season calendar into a preparation deadline.
- [Forecasting](../mechanic/forecasting.md): Forecasts let the player plan against the countdown rather than be ambushed by it (Frostpunk).

## Backlinks (computed)

**used by:** [Against the Storm](../game/against-the-storm.md), [Eco](../game/eco.md), [Frostpunk](../game/frostpunk.md), [Frostpunk 2](../game/frostpunk-2.md), [FTL: Faster Than Light](../game/ftl.md), [Mindustry](../game/mindustry.md), [Plague Inc.](../game/plague-inc.md), [Project Zomboid](../game/project-zomboid.md), [Teardown](../game/teardown.md), [Timberborn](../game/timberborn.md)

## Sources

- [Frostpunk](../source/src-wikipedia-frostpunk.md)
- [Plague Inc.](../source/src-wikipedia-plague-inc.md)
- [Day-Night Cycle](../source/src-dontstarvewiki-2026-day-night-cycle.md)

---
Provenance: created in run `2026-10-24-taxonomy-m5`.
