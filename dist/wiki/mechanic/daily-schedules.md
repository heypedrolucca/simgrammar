# Daily schedules

*Mechanic* · `daily-schedules` · status: **sourced**

Agents follow time-blocked routines for work, sleep, and leisure that create rhythms of demand across the day.

| field | value |
|---|---|
| aliases | routines, regimes, timetables |
| family | Agents & behavior |
| substrate | Rule system, Agent-based |
| math basis | Scheduling, Queueing theory |
| feedback | None |
| player interface | Parameter, Observation only |
| legibility | 4 |
| emergence potential | 3 |
| authoring cost | 2 |
| compute cost | 1 |
| tuning difficulty | 2 |
| ai leverage | 4 |
| maturity | Classic |
| core count *(computed)* | 3 |
| earliest game *(computed)* | [Little Computer People](../game/little-computer-people.md) |
| earliest year *(computed)* | 1985 |
| prevalence *(computed)* | 8 |
| prevalence share *(computed)* | 0.046 |
| subgenre spread *(computed)* | 6 |
| technique count *(computed)* | 1 |
| technique exposure *(computed)* | 0.75 |

## Definition

Owns a timetable per agent or group mapping time-of-day blocks to activity categories (sleep, work, eat, leisure), set by the player, authored, or generated. Each tick the current block filters or biases which actions an agent may choose and which areas it may enter; block boundaries trigger mass movement. Prison Architect regimes are hourly schedules per risk category (Lockup, Sleep, Eat, Yard, Shower, Free Time, Work variants) that confine prisoners to areas rather than forcing actions, and cooks start four hours before an Eat block. RimWorld's schedule assigns each colonist's hours to sleep, recreation, work, or anything. Generative Agents (2023) has a language model draft a day plan of five to eight broad chunks, then decompose it into hour-long and 5-15 minute actions and replan on events. Inputs: clock, block assignments, disruptions. Outputs: synchronized demand peaks and occupancy by room and hour.

## Player Experience

The player thinks in time: staggering shifts so the canteen is not mobbed, protecting sleep, and noticing when one block is starved. Schedules make agents look like they have lives and give the world a daily rhythm the player learns and exploits.

## Design Levers

- block granularity (hourly, shift-based, or free-form plans)
- who sets the schedule: player, authored routine, or agent-generated plan
- strictness: hard confinement, soft bias, or ignorable when needs are urgent
- per-group or per-agent schedules and shift staggering
- response to disruption: skip the block, delay, or replan

## Failure Modes

- Synchronized blocks create rush hours that overwhelm shared facilities such as canteens, showers, and transit.
- Agents follow the schedule into danger because blocks override situational awareness.
- Authored routines repeat visibly, so the world reads as clockwork after a few days.
- Schedules that conflict with needs create deadlocks in which agents go hungry or sleepless between blocks.

## Dynamics

- Shared blocks produce peaks on food, transit, and services, generating queues and congestion at predictable hours.
- Staggered shifts emerge as a player strategy that trades coordination effort for throughput.
- Coupled with day-night cycles and crime, schedules create time-dependent risk such as unattended night hours.

## Open Questions

- Can language-model day plans stay coherent across weeks of game time while remaining cheap enough for hundreds of agents?
- How much schedule variation is needed before a town stops reading as clockwork?

## Relations

**synergy**

- [Traffic congestion](../mechanic/traffic-congestion.md): Synchronized commutes produce rush-hour peaks that stress the network.
- [Needs decay](../mechanic/needs-decay.md): Schedules decide when needs can be met, creating crowding at meals and bedtime.

## Backlinks (computed)

**affected by:** [Generative agents (memory stream, reflection, planning)](../technique/generative-agents.md)

**involved in:** [Intent-level orders](../opportunity/intent-level-orders.md)

**used by:** [Big Ambitions](../game/big-ambitions.md), [Frostpunk](../game/frostpunk.md), [Generative Agents (Smallville)](../game/generative-agents-smallville.md), [Little Computer People](../game/little-computer-people.md), [Prison Architect](../game/prison-architect.md), [SimTower](../game/simtower.md), [Stardew Valley](../game/stardew-valley.md), [The Sims 3](../game/the-sims-3.md)

## Sources

- [Regime](../source/src-paradoxwikis-2026-prison-architect-regime.md)
- [Generative Agents: Interactive Simulacra of Human Behavior](../source/src-park-2023-generative-agents.md)

---
Provenance: created in run `2026-10-24-taxonomy-m3`.
