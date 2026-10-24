# Day-night cycle

*Mechanic* · `day-night-cycle` · status: **sourced**

A diurnal cycle changes light, visibility, temperature, and which agents are active, so activity follows the hour of the day.

| field | value |
|---|---|
| aliases | diurnal cycle, time of day |
| family | Environment & ecology |
| substrate | Rule system |
| math basis | Scheduling, Information theory |
| feedback | None |
| player interface | Observation only, Placement |
| legibility | 5 |
| emergence potential | 2 |
| authoring cost | 2 |
| compute cost | 1 |
| tuning difficulty | 2 |
| ai leverage | 2 |
| maturity | Classic |
| open questions | Can learned relighting or neural rendering make time-of-day visual variety nearly free, moving authoring effort to behavioral differences? |
| core count *(computed)* | 3 |
| earliest game *(computed)* | [X-Plane](../game/x-plane.md) |
| earliest year *(computed)* | 1995 |
| prevalence *(computed)* | 20 |
| prevalence share *(computed)* | 0.115 |
| subgenre spread *(computed)* | 12 |
| technique count *(computed)* | 1 |
| technique exposure *(computed)* | 0.75 |

## Definition

Owns a time-of-day value that advances each tick and wraps at a fixed day length, usually split into phases such as day, dusk, and night. Each phase sets ambient light, sometimes temperature, and flags read by other systems: agent schedules, spawn tables, growth, sanity or fear, and shop hours. Don't Starve uses an 8-minute real-time day of sixteen 30-second segments whose day, dusk, and night split shifts with the season; in total darkness the monster Charlie attacks and sanity drains at 50 per minute. Minecraft has a 20-minute day and spawns hostile mobs in low light, and The Long Dark makes nights colder. Inputs are elapsed time and season; outputs are phase flags and light levels.

## Player Experience

A rhythm of safety and threat. Day is for travel and work, dusk is a warning to head home, light fires, or finish tasks, and night is spent defending, sleeping, or risking the dark for better rewards. The player plans each day around the remaining light and learns to read the sky as a clock.

## Design Levers

- day length in real time and the day, dusk, and night split, fixed or varying by season
- how dark night gets and whether light sources are required to act
- which systems read the phase: spawns, agent schedules, temperature, growth, prices
- penalty for being caught in darkness, from reduced visibility to direct damage
- whether the player can skip the night by sleeping

## Failure Modes

- Night that is only darker visuals with no mechanical difference becomes an annoyance players remove by raising brightness.
- Nights that are too punishing make every night identical: retreat and wait, wasting play time.
- Long real-time days make planning trivial; very short ones make players feel unable to finish trips.

## Dynamics

- Bases cluster around light sources, and trips shrink to what can be done before dusk.
- Combined with daily schedules, synchronized agents create rush hours at dawn and dusk.
- Night becomes a high-risk, high-reward window when rare resources or creatures appear only in darkness.

## Open Questions

- Can learned relighting or neural rendering make time-of-day visual variety nearly free, moving authoring effort to behavioral differences?

## Backlinks (computed)

**affected by:** [Neural rendering in the graphics pipeline](../technique/neural-rendering-shaders.md)

**used by:** [Arma 3](../game/arma-3.md), [Cities: Skylines II](../game/cities-skylines-2.md), [Don't Starve](../game/dont-starve.md), [Dyson Sphere Program](../game/dyson-sphere-program.md), [Euro Truck Simulator 2](../game/euro-truck-simulator-2.md), [Harvest Moon](../game/harvest-moon.md), [Microsoft Flight Simulator (2020)](../game/microsoft-flight-simulator-2020.md), [Microsoft Flight Simulator 2024](../game/microsoft-flight-simulator-2024.md), [Minecraft](../game/minecraft.md), [Planet Zoo](../game/planet-zoo.md), [Project Zomboid](../game/project-zomboid.md), [Schedule I](../game/schedule-i.md), [Silent Hunter III](../game/silent-hunter-3.md), [Subnautica](../game/subnautica.md), [Tamagotchi](../game/tamagotchi.md), [The Long Dark](../game/the-long-dark.md), [This War of Mine](../game/this-war-of-mine.md), [Where Winds Meet](../game/where-winds-meet.md), [X-Plane](../game/x-plane.md), [The Legend of Zelda: Breath of the Wild](../game/zelda-breath-of-the-wild.md)

## Sources

- [Day-Night Cycle](../source/src-dontstarvewiki-2026-day-night-cycle.md)
- [The Long Dark](../source/src-wikipedia-the-long-dark.md)

---
Provenance: created in run `2026-10-24-taxonomy-m5`.
