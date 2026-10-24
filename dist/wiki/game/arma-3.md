# Arma 3

*Game* · `arma-3` · status: **sourced**

A first-person military simulation on large open terrains in which infantry, vehicles, and aircraft fight under modeled ballistics, recoil, and load-based stamina, extended by the Eden editor, SQF scripting, and a large mod community.

| field | value |
|---|---|
| year | 2013 |
| developer | Bohemia Interactive |
| platforms | PC |
| subgenre | Wargame / military sim |
| sim domain | Military / conflict, Physical / mechanical |
| player role | Inhabitant |
| agency model | Direct avatar, Direct unit control |
| time model | Real-time |
| sim scale | Individual |
| fidelity | Systemic |
| perspective | First-person |
| win structure | Scenario goals |
| failure model | Hard restart |
| narrative mode | Emergent |
| multiplayer | Single-player, Co-op, Competitive |
| modding | Total conversion |
| production tier | AA |
| agent count order | ~100 |
| emergence | 3 |
| influence | 3 |
| cluster *(computed)* | C06 |
| core count *(computed)* | 4 |
| mechanic count *(computed)* | 10 |

## Summary

A first-person military simulation on large open terrains in which infantry, vehicles, and aircraft fight under modeled ballistics, recoil, and load-based stamina, extended by the Eden editor, SQF scripting, and a large mod community.

## Core Loop

load a scenario or join a server -> move and coordinate as infantry or vehicle crew -> spot and engage under ballistics and recoil -> manage load, stamina, and wounds -> complete objectives or die -> build and share new scenarios

## Design Notes

Arma 3 treats the battlefield as a sandbox: large terrains of up to 163 square kilometers host infantry, vehicles, and aircraft under the same ballistic rules, and scenarios define the war. Much of its life comes from community scenarios and mods built with the Eden editor and SQF scripting, while Bohemia's military consultants reviewed its Tac-Ops missions. Projectile ballistics is not yet a mechanic in the taxonomy (proposal projectile-ballistics).

## Relations

**uses**

- [Direct avatar control](../mechanic/direct-avatar.md) (core): The player is one soldier in first person; clothing and carried equipment add weight that reduces movement speed and stamina.
- [Military operations](../mechanic/military-operations.md) (core): Infantry, armor, helicopters, jets, and boats share one large terrain, and weapons are heavily affected by external ballistics and recoil, so range and load-out shape every engagement.
- [Modding API](../mechanic/modding-api.md) (core): The Eden 3D editor and the SQF scripting language let players build single-player and multiplayer scenarios and mods, from realism overhauls to new game modes.
- [Unit commands](../mechanic/unit-commands.md) (supporting): Squad leaders issue orders to AI subordinates.
- [Injury body model](../mechanic/injury-body-model.md) (supporting)
- [Scenario objectives](../mechanic/scenario-objectives.md) (supporting)
- [Content sharing](../mechanic/content-sharing.md) (supporting): Scenarios and mods are shared through the Steam Workshop.
- [Weather](../mechanic/weather.md) (supporting)
- [Day-night cycle](../mechanic/day-night-cycle.md) (supporting)
- [Projectile ballistics](../mechanic/projectile-ballistics.md) (core): Weapons are heavily affected by external ballistics and recoil, so shooters account for drop and travel time at range.

## Sources

- [Arma 3](../source/src-wikipedia-arma-3.md)

---
Provenance: created in run `2026-10-24-catalog-gi`.
