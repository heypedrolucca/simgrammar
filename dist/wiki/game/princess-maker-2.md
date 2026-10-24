# Princess Maker 2

*Game* · `princess-maker-2` · status: **sourced**

A raising sim in which the player, as a father figure, schedules a daughter's training, part-time jobs, rest, and adventures from age 10 to 18, and her accumulated attributes decide one of 74 endings.

| field | value |
|---|---|
| year | 1993 |
| developer | Gainax |
| platforms | PC, Console, Handheld, Mobile |
| subgenre | Life sim |
| sim domain | Domestic / personal, Social / interpersonal |
| player role | Caretaker |
| agency model | Direct unit control, Caretaking interaction, Direct avatar |
| time model | Turn-based |
| sim scale | Individual |
| fidelity | Abstract |
| perspective | Text / UI |
| win structure | Scenario goals |
| failure model | Soft / recoverable |
| narrative mode | Hybrid |
| multiplayer | Single-player |
| modding | None |
| production tier | AA |
| agent count order | ~1 |
| emergence | 2 |
| influence | 3 |
| cluster *(computed)* | C14 |
| core count *(computed)* | 4 |
| mechanic count *(computed)* | 9 |

## Summary

A raising sim in which the player, as a father figure, schedules a daughter's training, part-time jobs, rest, and adventures from age 10 to 18, and her accumulated attributes decide one of 74 endings.

## Core Loop

set three activity periods for the month -> training and jobs change attributes, money, and fatigue -> events and festivals test her attributes -> rest or vacation to prevent illness -> she ages a year -> at 18 her attributes select a career ending

## Design Notes

Takami Akai designed the sequel to answer complaints that the original was repetitive, adding more reactions and events around a schedule-and-attributes core. Each month splits into early, middle, and late periods, each assigned to training (academic, artistic, religious, military, or magical), a part-time job, adventure, or free time, under a small annual income. Jobs unlock with age and pay promotion and streak bonuses, rival girls age alongside the daughter as benchmarks, and October festivals hold contests in martial arts, dance, art, and cooking. At 18 her attributes and history select one of 74 career endings, a branching-outcome model captured by the care-dependent-development mechanic.

## Relations

**uses**

- [Agent skills](../mechanic/agent-skills.md) (core): Training courses and part-time jobs raise and lower her attributes; attributes gate jobs, decide October festival contests in martial arts, dance, art, and cooking against rival girls, and select the final career.
- [Daily action budget](../mechanic/daily-action-budget.md) (core): Each month has three activity slots (early, middle, late), so every period spent training, working, adventuring, or resting is a period not spent on the others.
- [Lifecycle and aging](../mechanic/lifecycle-aging.md) (core): The daughter ages from 10 to 18; jobs and events unlock with age, and the game ends at 18.
- [Career ladder](../mechanic/career-ladder.md) (supporting): Repeating a part-time job leads to promotions, higher pay, and bonuses for unbroken success streaks.
- [Needs decay](../mechanic/needs-decay.md) (supporting): Stress from work and training is relieved by free time, vacations, spa stays, or bed rest; poor rest management leads to illness and weaker performance.
- [Treasury and budget](../mechanic/budget-treasury.md) (supporting): A small annual income pays for lessons, clothing, food, treatment, and shopping; jobs supplement it.
- [Turn structure](../mechanic/turn-structure.md) (supporting): The month is the turn, split into three phases that resolve after the player sets the schedule.
- [Triggered event chains](../mechanic/triggered-event-chains.md) (supporting): Events and reactions fire on age, attributes, and season, leading into 74 career endings with retrospective sequences.
- [Care-dependent development](../mechanic/care-dependent-development.md) (core): Eight years of scheduled training, jobs, and rest shape the daughter's attributes, and at 18 her attributes and history select one of 74 career endings.

## Sources

- [Princess Maker 2](../source/src-wikipedia-princess-maker-2.md)

---
Provenance: created in run `2026-10-24-catalog-gc`.
