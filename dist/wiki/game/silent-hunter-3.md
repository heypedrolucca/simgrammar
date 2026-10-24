# Silent Hunter III

*Game* · `silent-hunter-3` · status: **sourced**

A World War II U-boat sim with a dynamic campaign that generates convoys and escorts, manual torpedo targeting, and a persistent crew that gains rank, experience, and morale across patrols.

| field | value |
|---|---|
| aliases | SH3 |
| year | 2005 |
| developer | Ubisoft Bucharest |
| platforms | PC |
| subgenre | Vehicle sim |
| subgenre secondary | Wargame / military sim |
| sim domain | Military / conflict, Physical / mechanical |
| player role | Commander |
| agency model | Direct avatar, Direct unit control |
| time model | Real-time with pause |
| sim scale | Individual |
| fidelity | Systemic |
| perspective | First-person |
| win structure | Campaign |
| failure model | Hard restart |
| narrative mode | Emergent |
| multiplayer | Single-player |
| modding | Content |
| production tier | AA |
| agent count order | ~100 |
| emergence | 3 |
| influence | 2 |
| cluster *(computed)* | C06 |
| core count *(computed)* | 2 |
| mechanic count *(computed)* | 10 |

## Summary

A World War II U-boat sim with a dynamic campaign that generates convoys and escorts, manual torpedo targeting, and a persistent crew that gains rank, experience, and morale across patrols.

## Core Loop

receive a patrol grid -> transit under time compression -> detect contacts -> identify the target and solve speed, angle on the bow, and gyro angle -> fire torpedoes -> evade escorts -> return to base and promote crew

## Design Notes

The campaign engine generates convoys, destroyer escorts, and task forces in each patrol area rather than scripting engagements, so a career starting between 1939 and 1943 is a sequence of unplanned encounters. Realism settings scale the procedure: at the hardest, the player identifies class and nationality and computes speed, angle on the bow, and gyro angle; with manual targeting off a Weapons Officer solves the problem while approach geometry still matters. Crew members persist between patrols with rank, experience, morale, and decorations.

## Relations

**uses**

- [Military operations](../mechanic/military-operations.md) (core): The campaign engine generates convoys, destroyer escorts, and task forces in assigned patrol grids, and the player chooses targets and approaches.
- [Procedural checklists](../mechanic/procedural-checklists.md) (core): Manual targeting requires identifying a vessel's class and nationality and computing its speed, angle on the bow, and gyro angle before setting torpedo depth and spread.
- [Agent skills](../mechanic/agent-skills.md) (supporting): Crew members carry rank, experience, morale, and decorations between patrols.
- [Career ladder](../mechanic/career-ladder.md) (supporting): A career begins at the rank of Lieutenant, Jr., with a U-boat base assignment between 1939 and 1943.
- [Delegation to AI managers](../mechanic/delegation-to-ai.md) (supporting): With manual targeting off, a Weapons Officer computes the firing solution.
- [Fog of war](../mechanic/fog-of-war.md) (supporting)
- [Pause and speed control](../mechanic/variable-speed.md) (supporting)
- [Weather](../mechanic/weather.md) (supporting)
- [Day-night cycle](../mechanic/day-night-cycle.md) (supporting)
- [Projectile ballistics](../mechanic/projectile-ballistics.md) (supporting): Torpedoes run at a set speed, depth, and gyro angle toward an intercept computed from target speed and angle on the bow, so a bad solution misses.

## Sources

- [Silent Hunter III](../source/src-wikipedia-silent-hunter-3.md)

---
Provenance: created in run `2026-10-24-catalog-gf`.
