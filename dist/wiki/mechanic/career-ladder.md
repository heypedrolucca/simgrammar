# Career ladder

*Mechanic* · `career-ladder` · status: **sourced**

Characters advance through ranked job levels by meeting skill, relationship, and performance requirements.

| field | value |
|---|---|
| aliases | jobs and promotions, career tracks |
| family | Progression & goals |
| substrate | Rule system, Agent-based |
| math basis | Scheduling |
| feedback | Reinforcing (positive) |
| player interface | Observation only, Choice / cards |
| legibility | 4 |
| emergence potential | 2 |
| authoring cost | 3 |
| compute cost | 1 |
| tuning difficulty | 2 |
| ai leverage | 3 |
| maturity | Classic |
| core count *(computed)* | 3 |
| earliest game *(computed)* | [Princess Maker 2](../game/princess-maker-2.md) |
| earliest year *(computed)* | 1993 |
| prevalence *(computed)* | 12 |
| prevalence share *(computed)* | 0.069 |
| subgenre spread *(computed)* | 3 |
| technique count *(computed)* | 1 |
| technique exposure *(computed)* | 0.3 |

## Definition

A career is an ordered list of levels, each with a title, pay, schedule, and promotion requirements. State owned: per character, current career and level, and a job performance meter. Update rule: each work period, performance changes based on attendance and inputs such as mood, skills, or task completion; when performance and the next level's requirements are met, the character is promoted; very low performance or missed shifts cause demotion or firing. Inputs come from other mechanics (skills, relationships, needs); outputs are income, schedule, and status. Canonical form: The Sims 2, where adult careers have ten levels, teen careers three, promotion requires advances in three skills, a number of household friends, and high mood, and missing work two days in a row gets a Sim fired; The Sims 4 adds daily career tasks and branching tracks.

## Player Experience

A long-term arc for one character. The player schedules skill-building and socializing around work, watches the performance bar before a promotion, and feels the status jump of a new title and pay. It gives sandbox life a direction.

## Design Levers

- number of levels and spacing of requirements
- requirement types: skills, relationships, mood, or task completion
- performance meter rate and decay
- branching tracks at upper levels
- random work events with choices, such as The Sims chance cards
- pay and schedule curve across levels

## Failure Modes

- Requirements become a checklist that drains spontaneity from life simulation.
- Rabbit-hole careers where the Sim leaves the lot make the career invisible to play.
- Pay grows faster than costs, so money stops mattering by mid-career.

## Dynamics

- Career requirements route characters' free time into skill and friend grinding, coupling work to social and needs systems.
- Schedule conflicts between household members' careers create household logistics problems.
- Promotions raise income and enable home upgrades, a reinforcing loop toward comfort.

## Open Questions

- Can generated workplaces with colleagues, tasks, and politics replace authored rabbit-hole careers without large writing costs?
- Does requirement opacity, like a real workplace, make careers more engaging than explicit checklists?

## Backlinks (computed)

**affected by:** [Agent-based automated playtesting and balancing](../technique/automated-playtesting.md)

**used by:** [Gran Turismo](../game/gran-turismo.md), [Gran Turismo 7](../game/gran-turismo-7.md), [inZOI](../game/inzoi.md), [iRacing](../game/iracing.md), [Microsoft Flight Simulator 2024](../game/microsoft-flight-simulator-2024.md), [Paralives](../game/paralives.md), [Princess Maker 2](../game/princess-maker-2.md), [Silent Hunter III](../game/silent-hunter-3.md), [The Sims](../game/the-sims.md), [The Sims 2](../game/the-sims-2.md), [The Sims 3](../game/the-sims-3.md), [The Sims 4](../game/the-sims-4.md)

## Claims

- In The Sims 2 adult careers have ten levels and teen careers three; promotion requires advancing three skills, enough household friends, and high mood, and missing work two days in a row causes firing. *(confidence: medium)* [[63](../source/src-strategywiki-2026-sims-2-careers.md)]

## Sources

- [The Sims 2/Careers](../source/src-strategywiki-2026-sims-2-careers.md)

---
Provenance: created in run `2026-10-24-taxonomy-m6`.
