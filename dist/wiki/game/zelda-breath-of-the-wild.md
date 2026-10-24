# The Legend of Zelda: Breath of the Wild

*Game* · `zelda-breath-of-the-wild` · status: **sourced**

An open-world action adventure whose physics and chemistry engines let fire, wind, electricity, temperature, and material properties combine, so puzzles and fights accept solutions the designers did not script.

| field | value |
|---|---|
| aliases | Breath of the Wild, BotW |
| year | 2017 |
| developer | Nintendo EPD |
| platforms | Console, Handheld |
| subgenre | Sandbox world |
| subgenre secondary | Physics sandbox, Survival sim |
| sim domain | Physical / mechanical, Planetary / natural |
| player role | Inhabitant |
| agency model | Direct avatar |
| time model | Real-time with pause |
| sim scale | Region |
| fidelity | Stylized |
| perspective | Third-person |
| win structure | Completion |
| failure model | Soft / recoverable |
| narrative mode | Authored |
| multiplayer | Single-player |
| modding | Content |
| production tier | AAA |
| agent count order | ~100 |
| emergence | 3 |
| influence | 3 |
| boundary case | True |
| cluster *(computed)* | C05 |
| core count *(computed)* | 3 |
| mechanic count *(computed)* | 10 |

## Summary

An open-world action adventure whose physics and chemistry engines let fire, wind, electricity, temperature, and material properties combine, so puzzles and fights accept solutions the designers did not script.

## Core Loop

spot a landmark -> climb, glide, or ride toward it under stamina limits -> solve shrines and fights with physics and elemental interactions -> gather and cook ingredients -> replace broken weapons -> push farther into the world

## Design Notes

The game is mostly authored content (map, shrines, story) and is included for its systemic layer. A modified Havok physics engine and a separate chemistry engine give objects material properties, so fire burns grass and creates updrafts, metal draws lightning and conducts electricity, wind carries flames and gliders, and cold or heat drains health unless countered by clothing or cooked food. Weapon durability and stamina force continual scavenging and route choice, and shrine puzzles accept any solution that satisfies the physical end condition.

## Relations

**uses**

- [Material interactions](../mechanic/material-interactions.md) (core): The chemistry engine gives objects properties such as flammable, metallic, or conductive; fire ignites wood and grass, metal attracts lightning in storms and conducts electricity, and ice melts near fire.
- [Rigid-body physics](../mechanic/rigid-body-physics.md) (core): A modified Havok engine moves crates, boulders, and weapons; Magnesis lifts metal objects, Stasis freezes an object so stored hits launch it, and Cryonis raises ice pillars from water, giving shrines and fights unscripted solutions.
- [Survival meters](../mechanic/survival-meters.md) (core): A stamina wheel limits sprinting, climbing, swimming, and gliding; hearts are health, and ambient cold and heat damage the player without matching clothing or elixirs.
- [Fire spread](../mechanic/fire-spread.md) (supporting): Fire spreads across grass in the wind direction and produces updrafts that the paraglider can ride.
- [Weather](../mechanic/weather.md) (supporting): Rain makes surfaces too slippery to climb, and thunderstorms strike metal equipment with lightning.
- [Heat transfer](../mechanic/heat-transfer.md) (supporting): Region temperature and fire sources set a temperature gauge that damages the player beyond tolerance.
- [Hand crafting](../mechanic/hand-crafting.md) (supporting): Cooking combines up to five ingredients in a pot into meals or elixirs whose effects and duration depend on the ingredients.
- [Wear and breakdown](../mechanic/wear-breakdown.md) (supporting): Weapons, bows, and shields lose durability with use and shatter; the Master Sword recharges instead.
- [Day-night cycle](../mechanic/day-night-cycle.md) (supporting): Time of day changes enemy and creature activity, and the Blood Moon respawns defeated enemies.
- [Direct avatar control](../mechanic/direct-avatar.md) (supporting): Link can climb almost any surface, glide, ride horses, and use runes.

## Sources

- [The Legend of Zelda: Breath of the Wild](../source/src-wikipedia-zelda-breath-of-the-wild.md)

---
Provenance: created in run `2026-10-24-catalog-gg`.
