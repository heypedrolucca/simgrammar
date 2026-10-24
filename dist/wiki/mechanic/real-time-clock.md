# Real-time clock

*Mechanic* · `real-time-clock` · status: **sourced**

Game time follows the real-world clock and calendar, so the world advances, ages, and holds events while the game is closed.

| field | value |
|---|---|
| aliases | wall-clock time, persistent real time, offline progress |
| family | Time & pacing |
| substrate | Rule system |
| math basis | Scheduling |
| feedback | None |
| player interface | Observation only |
| legibility | 5 |
| emergence potential | 2 |
| authoring cost | 3 |
| compute cost | 1 |
| tuning difficulty | 3 |
| ai leverage | 2 |
| maturity | Classic |
| open questions | Can generated daily content keep a real-time world changing enough that daily visits stay worthwhile for years? |
| core count *(computed)* | 3 |
| earliest game *(computed)* | [Tamagotchi](../game/tamagotchi.md) |
| earliest year *(computed)* | 1996 |
| prevalence *(computed)* | 7 |
| prevalence share *(computed)* | 0.04 |
| subgenre spread *(computed)* | 4 |
| technique count *(computed)* | 0 |
| technique exposure *(computed)* | 0.0 |

## Definition

Owns a mapping from the device or server clock to game time plus the last-seen timestamp. On launch or each tick, the real time elapsed since the last update is computed and the simulation catches up: needs decay, crops grow, timers finish, or a capped amount of progress is granted. Calendar dates trigger holidays and seasonal events. Tamagotchi (1996) ages its pet through life stages in real time; Animal Crossing uses the console's internal clock and calendar so time of day, seasons, holidays, and tree growth follow the real date, with music that changes each hour; mobile builders and idle games run construction timers and offline earnings on the device or server clock. Inputs are real elapsed time; outputs are catch-up updates and dated events.

## Player Experience

A world that lives alongside the player's own day. Visiting at different hours shows different scenes, shops open and close, and holidays arrive with the real calendar. The player builds a daily habit, and absence has consequences, from weeds to a sick pet, so returning feels like coming home or like guilt.

## Design Levers

- ratio of game time to real time, 1:1 or compressed
- catch-up rule for absence: full simulation, capped progress, or frozen
- penalties or rewards for absence
- calendar-tied events and how often content changes
- handling of player clock changes

## Failure Modes

- Players change the device clock to skip waits (Animal Crossing players call it time travel), which breaks event pacing and timer economies.
- Harsh absence penalties punish ordinary life events and drive players to quit after a missed week.
- Content tied to real dates excludes players in other time zones or hemispheres unless the game adapts it.

## Dynamics

- Daily check-in habits form, and with streak rewards they produce strong retention.
- Offline catch-up must be computed in bulk, pushing designs toward simple closed-form growth.
- Real-time waits become a resource that free-to-play games sell speed-ups for.

## Open Questions

- Can generated daily content keep a real-time world changing enough that daily visits stay worthwhile for years?

## Relations

**tension**

- [Pause and speed control](../mechanic/variable-speed.md): Binding time to the wall clock removes player control of pacing.

## Backlinks (computed)

**used by:** [Animal Crossing: New Horizons](../game/animal-crossing-new-horizons.md), [Bitburner](../game/bitburner.md), [EVE Online](../game/eve-online.md), [Nintendogs](../game/nintendogs.md), [Seaman](../game/seaman.md), [Tamagotchi](../game/tamagotchi.md), [Tomodachi Life](../game/tomodachi-life.md)

## Sources

- [Tamagotchi](../source/src-wikipedia-tamagotchi.md)
- [Animal Crossing](../source/src-wikipedia-animal-crossing.md)

---
Provenance: created in run `2026-10-24-taxonomy-m5`.
