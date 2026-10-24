# The Long Dark

*Game* · `the-long-dark` · status: **sourced**

A first-person wilderness survival sim set in frozen northern Canada where the player manages warmth, calories, thirst, fatigue, and afflictions against cold, weather, and wildlife.

| field | value |
|---|---|
| year | 2014 |
| year full release | 2017 |
| developer | Hinterland Studio |
| platforms | PC, Console, Handheld |
| subgenre | Survival sim |
| sim domain | Biological / ecological, Planetary / natural |
| player role | Inhabitant |
| agency model | Direct avatar |
| time model | Real-time |
| sim scale | Individual |
| fidelity | Systemic |
| perspective | First-person |
| win structure | Survival duration |
| failure model | Hard restart |
| narrative mode | Emergent |
| multiplayer | Single-player |
| modding | Scripting |
| production tier | Indie |
| agent count order | ~10 |
| emergence | 3 |
| influence | 2 |
| cluster *(computed)* | C05 |
| core count *(computed)* | 3 |
| mechanic count *(computed)* | 9 |

## Summary

A first-person wilderness survival sim set in frozen northern Canada where the player manages warmth, calories, thirst, fatigue, and afflictions against cold, weather, and wildlife.

## Core Loop

explore a frozen region -> scavenge, hunt, and harvest -> manage calories, thirst, fatigue, and warmth -> weather, night, and wildlife threaten condition -> craft, repair, and shelter -> survive another day until death

## Design Notes

Survival mode has no zombies or authored goal; the cold, wildlife, and dwindling supplies are the opposition, and death deletes the save. All needs feed a single condition stock: an empty warmth bar drains condition about 20% per hour while empty hunger or fatigue drain about 1% and thirst 2%, so cold is the fast killer and food is the slow one. Time is treated as the scarce resource because every action costs calories and in-game hours. The episodic Wintermute story mode has no permadeath.

## Relations

**uses**

- [Survival meters](../mechanic/survival-meters.md) (core): Warmth, fatigue, hunger, and thirst feed one condition stock; when a need is empty, condition drains per hour (warmth 20%, fatigue 1%, hunger 1%, thirst 2%), and afflictions such as hypothermia, frostbite, and dysentery drain or cap it.
- [Weather](../mechanic/weather.md) (core): Wind, falling temperatures, and blizzards change how fast warmth drops and how far the player can travel; nights are significantly colder.
- [Permadeath](../mechanic/permadeath.md) (core): In Survival mode the save is deleted on death; a later DLC option allows up to three resurrections per save at a difficulty cost, and Misery mode always uses permadeath.
- [Day-night cycle](../mechanic/day-night-cycle.md) (supporting): Nights are darker and colder, shaping travel and shelter.
- [Hand crafting](../mechanic/hand-crafting.md) (supporting): Hides, guts, and wood are crafted into clothing, tools, and arrows.
- [Wear and breakdown](../mechanic/wear-breakdown.md) (supporting): Clothing and tools lose condition with use and must be repaired.
- [Spoilage](../mechanic/spoilage.md) (supporting): Food loses condition over time.
- [Deposit depletion](../mechanic/deposit-depletion.md) (supporting): Manufactured supplies are finite, so long runs shift from looting to hunting and crafting.
- [Direct avatar control](../mechanic/direct-avatar.md) (supporting)

## Sources

- [The Long Dark](../source/src-wikipedia-the-long-dark.md)
- [The Long Dark on Steam](../source/src-steam-2026-the-long-dark.md)
- [Condition](../source/src-longdarkwiki-2026-condition.md)

---
Provenance: created in run `2026-10-24-catalog-gb`.
