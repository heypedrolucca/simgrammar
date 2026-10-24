# Kingdoms and Castles

*Game* · `kingdoms-and-castles` · status: **sourced**

A medieval town builder in which peasants farm and stockpile for an annual winter while the player stacks castle blocks into walls and towers to defend against vikings, dragons, and ogres.

| field | value |
|---|---|
| year | 2017 |
| developer | Lion Shield |
| platforms | PC, Console |
| subgenre | City builder |
| sim domain | Urban, Military / conflict |
| player role | Ruler / statesman |
| agency model | Zoning / placement, Policy / parameter |
| time model | Real-time with pause |
| sim scale | Settlement |
| fidelity | Stylized |
| perspective | Free 3D camera |
| win structure | Open sandbox |
| failure model | Soft / recoverable |
| narrative mode | Emergent |
| multiplayer | Single-player |
| modding | Content |
| production tier | Indie |
| agent count order | ~100 |
| emergence | 2 |
| influence | 1 |
| cluster *(computed)* | C02 |
| core count *(computed)* | 2 |
| mechanic count *(computed)* | 16 |

## Summary

A medieval town builder in which peasants farm and stockpile for an annual winter while the player stacks castle blocks into walls and towers to defend against vikings, dragons, and ogres.

## Core Loop

place a keep and houses on an island -> peasants farm, cut wood, and quarry -> store food for the annual winter -> tax peasants to pay workers and unlock buildings -> stack castle blocks into walls and towers -> repel vikings, dragons, and ogres

## Design Notes

Kingdoms and Castles pairs a light town economy with a block-built castle: walls and towers form from how blocks are stacked, and taller archer towers reach farther, so defense is shaped geometry rather than a building menu. Each villager and resource is individually simulated, and an annual winter that destroys crops sets a regular survival check. Raiders kidnap peasants and burn buildings, and a dragon targets granaries, linking defense to food security.

## Relations

**uses**

- [Raid defense](../mechanic/raid-defense.md) (core): Vikings kidnap peasants, steal resources, and burn the town; dragons torch granaries; ogres attack; soldiers and archer towers defend.
- [Seasons](../mechanic/seasons.md) (core): An annual winter destroys crops, so food must be stored in granaries to prevent starvation.
- [Modular assembly](../mechanic/modular-assembly.md) (supporting): Castle blocks stack into walls and towers whose shape forms automatically; taller archer towers have longer range.
- [Taxation](../mechanic/taxation.md) (supporting): Peasant taxes pay workers and unlock buildings.
- [Citizen satisfaction](../mechanic/citizen-satisfaction.md) (supporting): Happiness from layout, churches, taverns, and festivals.
- [Immigration by attractiveness](../mechanic/immigration-attractiveness.md) (supporting): Happiness and housing attract new residents.
- [Random disasters](../mechanic/random-disasters.md) (supporting): Lightning starts fires.
- [Contagion](../mechanic/contagion.md) (supporting): Plagues spread and must be healed.
- [Crop cultivation](../mechanic/crop-cultivation.md) (supporting)
- [Renewable regrowth](../mechanic/renewable-regrowth.md) (supporting): Foresters cut and replant trees.
- [Faction diplomacy](../mechanic/faction-diplomacy.md) (supporting): Diplomats make trade agreements, alliances, and wars with AI kingdoms.
- [Procedural terrain](../mechanic/procedural-terrain.md) (supporting)
- [Pause and speed control](../mechanic/variable-speed.md) (supporting)
- [Building placement](../mechanic/free-placement.md) (supporting)
- [Fire spread](../mechanic/fire-spread.md) (supporting)
- [Storage and buffers](../mechanic/storage-capacity.md) (supporting)

## Sources

- [Kingdoms and Castles](../source/src-wikipedia-kingdoms-and-castles.md)
- [Kingdoms and Castles on Steam](../source/src-steam-2026-kingdoms-and-castles.md)

---
Provenance: created in run `2026-10-24-catalog-ga`; reviewed in `2026-10-24-review-fixes`.
