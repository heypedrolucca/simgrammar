# Don't Starve

*Game* · `dont-starve` · status: **sourced**

A survival sim in a procedurally generated wilderness where the player balances hunger, health, and sanity, crafts tools and light, and prepares for darkness, hounds, and seasons.

| field | value |
|---|---|
| year | 2012 |
| year full release | 2013 |
| developer | Klei Entertainment |
| platforms | PC, Console, Handheld, Mobile |
| subgenre | Survival sim |
| sim domain | Biological / ecological, Planetary / natural |
| player role | Inhabitant |
| agency model | Direct avatar |
| time model | Real-time |
| sim scale | Individual |
| fidelity | Stylized |
| perspective | Isometric |
| win structure | Survival duration |
| failure model | Hard restart |
| narrative mode | Emergent |
| multiplayer | Single-player |
| modding | Scripting |
| production tier | Indie |
| agent count order | ~100 |
| emergence | 3 |
| influence | 3 |
| cluster *(computed)* | C05 |
| core count *(computed)* | 3 |
| mechanic count *(computed)* | 12 |

## Summary

A survival sim in a procedurally generated wilderness where the player balances hunger, health, and sanity, crafts tools and light, and prepares for darkness, hounds, and seasons.

## Core Loop

explore a generated world by day -> gather and craft tools, food, and light -> manage hunger, health, and sanity -> survive nights, hounds, and seasons -> build a base and stockpile for winter -> die and start a new world

## Design Notes

Three meters interact: empty hunger drains health, and sanity falls at dusk and night and from unpleasant actions until, below 15% of maximum, shadow creatures attack, so the mind is a survival stock alongside the body. The 8-minute day is divided into day, dusk, and night segments whose split shifts with the season, and total darkness is lethal because Charlie attacks anyone without a light. Hound attacks escalate on a schedule tied to days survived, and death deletes the world except through rare resurrection items. Klei released it in beta in 2012 and fully on 23 April 2013.

## Relations

**uses**

- [Survival meters](../mechanic/survival-meters.md) (core): Hunger, health, and sanity meters; default maximum hunger is 150 and drains 75 per game day, and at empty hunger health drains 1.25 per second until the player eats or dies.
- [Hand crafting](../mechanic/hand-crafting.md) (core): Recipes combine gathered items into tools, light, shelter, and weapons; most must first be prototyped at a crafting station such as the science machine, though some characters bypass this.
- [Day-night cycle](../mechanic/day-night-cycle.md) (core): A day lasts 8 real minutes in sixteen 30-second segments of day, dusk, and night; sanity drains 5 per minute at dusk and 50 per minute in total darkness, where Charlie attacks unless the player has light.
- [Seasons](../mechanic/seasons.md) (supporting): Winter shortens days and lengthens nights; seasons change hazards.
- [Adaptive threat scaling](../mechanic/adaptive-threat-scaling.md) (supporting): Hound attacks scale with days survived, from 2 hounds every 5-8 days early to 7-10 hounds every 11-16 days after day 100, with shorter warnings.
- [Spoilage](../mechanic/spoilage.md) (supporting): Food spoils over time; spoiled food restores less hunger and costs health and sanity.
- [Renewable regrowth](../mechanic/renewable-regrowth.md) (supporting): Picked grass, saplings, and berry bushes regrow.
- [Crop cultivation](../mechanic/crop-cultivation.md) (supporting)
- [Fire spread](../mechanic/fire-spread.md) (supporting): Fire spreads across flammable plants and structures.
- [Procedural terrain](../mechanic/procedural-terrain.md) (supporting): Each world is randomly generated.
- [Permadeath](../mechanic/permadeath.md) (supporting): Death deletes the world unless a rare resurrection item is available.
- [Direct avatar control](../mechanic/direct-avatar.md) (supporting)

## Sources

- [Don't Starve](../source/src-wikipedia-dont-starve.md)
- [Hunger](../source/src-dontstarvewiki-2026-hunger.md)
- [Day-Night Cycle](../source/src-dontstarvewiki-2026-day-night-cycle.md)
- [Hound](../source/src-dontstarvewiki-2026-hounds.md)

---
Provenance: created in run `2026-10-24-catalog-gb`.
