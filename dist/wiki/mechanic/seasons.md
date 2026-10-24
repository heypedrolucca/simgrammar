# Seasons

*Mechanic* · `seasons` · status: **sourced**

A seasonal calendar cycles conditions such as temperature, daylight, and growing windows that govern growth, demand, and risk.

| field | value |
|---|---|
| aliases | seasonal cycle, calendar seasons |
| family | Environment & ecology |
| substrate | Rule system |
| math basis | System dynamics / ODEs, Scheduling |
| feedback | None |
| player interface | Observation only |
| legibility | 4 |
| emergence potential | 2 |
| authoring cost | 3 |
| compute cost | 1 |
| tuning difficulty | 2 |
| ai leverage | 2 |
| maturity | Classic |
| open questions | Can generative asset models make seasonal variants of every asset cheap enough that seasons become a default rather than a budget decision? |
| core count *(computed)* | 4 |
| earliest game *(computed)* | [Harvest Moon](../game/harvest-moon.md) |
| earliest year *(computed)* | 1996 |
| prevalence *(computed)* | 16 |
| prevalence share *(computed)* | 0.092 |
| subgenre spread *(computed)* | 5 |
| technique count *(computed)* | 0 |
| technique exposure *(computed)* | 0.0 |

## Definition

Owns a calendar position that advances by day and maps to a season index, usually four. Each season sets parameters other systems read: which crops can grow, temperature, day length, weather odds, animal behavior, demand for heat or food, and scheduled events. Stardew Valley has four 28-day seasons, and seasonal crops must generally be harvested before the next season arrives; Don't Starve's base cycle alternates 20 summer days and 16 winter days and changes the day, dusk, and night split with them; Banished and Farthest Frontier force food stockpiling for winters without harvests. Inputs are elapsed days; outputs are season flags and parameter sets. Some games make season length a setting.

## Player Experience

Planning in cycles. The player plants for this season while saving for the next, treats the end of a season as a deadline, and gets a fresh start each spring. Winter tests the year's preparation, and the cycle gives long games a felt rhythm.

## Design Levers

- number and length of seasons, and whether lengths vary or can be set
- which systems each season modifies: growth, temperature, weather, events, prices
- severity of the harshest season and how much stockpiling it demands
- transition rules, such as crops dying at the change or gradual change
- season-unique content: crops, festivals, creatures

## Failure Modes

- Seasons that only swap textures add art cost without changing decisions.
- A harsh season survivable only with one known stockpile size becomes a checklist.
- Season-gated content locks players out for long stretches when they miss a window.

## Dynamics

- Seasonal production with year-round consumption creates demand for storage, preservation, and trade.
- Combined with a crisis countdown, the approach of winter structures the year as preparation.
- Labor shifts between seasonal tasks, creating idle periods and peaks.

## Open Questions

- Can generative asset models make seasonal variants of every asset cheap enough that seasons become a default rather than a budget decision?

## Backlinks (computed)

**involved in:** [Learned regional weather](../opportunity/learned-weather-layer.md)

**used by:** [Against the Storm](../game/against-the-storm.md), [Animal Crossing: New Horizons](../game/animal-crossing-new-horizons.md), [Banished](../game/banished.md), [Cities: Skylines II](../game/cities-skylines-2.md), [Don't Starve](../game/dont-starve.md), [Farming Simulator 25](../game/farming-simulator-25.md), [Farthest Frontier](../game/farthest-frontier.md), [Going Medieval](../game/going-medieval.md), [Harvest Moon](../game/harvest-moon.md), [Kingdoms and Castles](../game/kingdoms-and-castles.md), [Manor Lords](../game/manor-lords.md), [Pharaoh](../game/pharaoh.md), [Project Zomboid](../game/project-zomboid.md), [Stardew Valley](../game/stardew-valley.md), [This War of Mine](../game/this-war-of-mine.md), [Workers & Resources: Soviet Republic](../game/workers-and-resources.md)

## Sources

- [Stardew Valley](../source/src-wikipedia-stardew-valley.md)
- [Day-Night Cycle](../source/src-dontstarvewiki-2026-day-night-cycle.md)

---
Provenance: created in run `2026-10-24-taxonomy-m5`.
