# Project Zomboid

*Game* · `project-zomboid` · status: **sourced**

An isometric zombie survival sandbox in which one survivor manages moodles, injuries, skills, and failing utilities across a large Kentucky map until an inevitable death.

| field | value |
|---|---|
| year | 2011 |
| developer | The Indie Stone |
| platforms | PC |
| subgenre | Survival sim |
| subgenre secondary | Sandbox world |
| sim domain | Biological / ecological, Urban |
| player role | Inhabitant |
| agency model | Direct avatar |
| time model | Real-time with pause |
| sim scale | Individual |
| fidelity | Systemic |
| perspective | Isometric |
| win structure | Survival duration |
| failure model | Permadeath |
| narrative mode | Emergent |
| multiplayer | Single-player, Co-op |
| modding | Scripting |
| production tier | Indie |
| agent count order | ~1,000 |
| emergence | 4 |
| influence | 2 |
| cluster *(computed)* | C05 |
| core count *(computed)* | 4 |
| mechanic count *(computed)* | 17 |

## Summary

An isometric zombie survival sandbox in which one survivor manages moodles, injuries, skills, and failing utilities across a large Kentucky map until an inevitable death.

## Core Loop

loot houses and stores -> avoid or fight zombies drawn by sight and noise -> manage hunger, fatigue, injuries, and moodles -> utilities fail and seasons turn -> barricade, farm, and level skills -> survive until death

## Design Notes

The framing question is how the character dies, not whether: zombie infection is always fatal in an unmodified game, so play is about extending a doomed run. Water and power shut off within the first month, after which erosion and overgrowth spread, giving the sandbox a scheduled decline. Zombies respond to sight and hearing and hordes migrate, so noise from actions shapes risk; there is no mechanic id for noise attraction yet (proposal filed). The game has been in early access since a paid tech demo in May 2011, with Steam early access from November 2013 and Build 42 in open beta from December 2024.

## Relations

**uses**

- [Survival meters](../mechanic/survival-meters.md) (core): Moodles for hunger, thirst, fatigue, endurance, panic, stress, boredom, unhappiness, temperature, wetness, pain, bleeding, and sickness each grow in severity and penalize combat, movement, carrying, or healing.
- [Injury body model](../mechanic/injury-body-model.md) (core): Wounds such as scratches, lacerations, bites, and fractures are tracked per body part with bleeding and bandaging; zombie infection is spread by saliva and blood and is always fatal.
- [Agent skills](../mechanic/agent-skills.md) (core): Skills such as carpentry and cooking level from activities, and skill books and magazines speed or unlock progress.
- [Crisis countdown](../mechanic/crisis-countdown.md) (supporting): Water and power shut off within about a month, forcing preparation.
- [Personality traits](../mechanic/personality-traits.md) (supporting): Occupation and positive or negative traits are chosen at character creation; occupation also sets spawn location.
- [Hand crafting](../mechanic/hand-crafting.md) (supporting): Weapons, tools, and barricades are crafted; Build 42 overhauled crafting.
- [Building placement](../mechanic/free-placement.md) (supporting): Carpentry builds walls, barricades, and forts.
- [Crop cultivation](../mechanic/crop-cultivation.md) (supporting)
- [Seasons](../mechanic/seasons.md) (supporting): A climate system with seasons changes gear needs.
- [Weather](../mechanic/weather.md) (supporting)
- [Day-night cycle](../mechanic/day-night-cycle.md) (supporting)
- [Spoilage](../mechanic/spoilage.md) (supporting): Food rots, and refrigeration ends when power fails.
- [Vehicle dynamics](../mechanic/vehicle-dynamics.md) (supporting): Vehicles have physics and part condition.
- [Fog of war](../mechanic/fog-of-war.md) (supporting): A vision cone limits what the survivor sees.
- [Permadeath](../mechanic/permadeath.md) (supporting): Death ends the character; a new survivor can start in the same world.
- [Modding API](../mechanic/modding-api.md) (supporting): Full Lua modding through the Steam Workshop.
- [Stimulus attraction](../mechanic/stimulus-attraction.md) (core): Zombies respond to sight and hearing, so noise from actions such as gunfire or breaking windows draws them toward the survivor, and hordes migrate.

## Sources

- [Project Zomboid](../source/src-wikipedia-project-zomboid.md)
- [Project Zomboid on Steam](../source/src-steam-2026-project-zomboid.md)
- [Moodles](../source/src-pzwiki-2026-moodles.md)

---
Provenance: created in run `2026-10-24-catalog-gb`.
