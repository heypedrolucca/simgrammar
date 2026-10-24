# Sid Meier's Civilization

*Game* · `civilization` · status: **sourced**

A turn-based 4X game in which the player guides a civilization from 4000 BC toward the space age by founding cities, researching a technology tree, building one-per-world wonders, and competing with rival civilizations by diplomacy or war.

| field | value |
|---|---|
| aliases | Civilization, Civ |
| year | 1991 |
| developer | MicroProse |
| platforms | PC, Console |
| subgenre | 4X strategy |
| sim domain | Political / governance, Military / conflict, Economic |
| player role | Ruler / statesman |
| agency model | Direct unit control, Policy / parameter |
| time model | Turn-based |
| sim scale | Nation / polity |
| fidelity | Stylized |
| perspective | Top-down / side 2D |
| win structure | Competitive victory |
| failure model | Hard restart |
| narrative mode | Emergent |
| multiplayer | Single-player |
| modding | None |
| production tier | AA |
| agent count order | ~100 |
| emergence | 3 |
| influence | 5 |
| influenced by | [SimCity](../game/simcity-1989.md), [Populous](../game/populous.md), [Railroad Tycoon](../game/railroad-tycoon.md) |
| cluster *(computed)* | C04 |
| core count *(computed)* | 3 |
| mechanic count *(computed)* | 13 |

## Summary

A turn-based 4X game in which the player guides a civilization from 4000 BC toward the space age by founding cities, researching a technology tree, building one-per-world wonders, and competing with rival civilizations by diplomacy or war.

## Core Loop

explore with units -> found and grow cities -> allocate production and research -> unlock advances and wonders -> expand, trade, or fight rivals -> win by conquest or the space race

## Design Notes

Meier and Shelley combined the technology tree of Francis Tresham's board game with Empire's exploration and conquest and Railroad Tycoon's idea of several interacting systems managed at once; a SimCity-style zoning layer in an early prototype was dropped. Each city works surrounding terrain tiles for food, production, and trade, a worked-tile yield model the taxonomy does not yet name (proposal worked-tile-yields), and battles resolve from unit attack and defense values (proposal stat-combat-resolution). Wonders exist once per world, so building one denies it to every rival.

## Relations

**influenced by**

- [SimCity](../game/simcity-1989.md)
- [Populous](../game/populous.md)
- [Railroad Tycoon](../game/railroad-tycoon.md)

**uses**

- [Tech tree](../mechanic/tech-tree.md) (core): Advances are researched one at a time through a prerequisite graph adapted from Tresham's 1980 board game, from Pottery and the Wheel to Nuclear Fission and Space Flight; each unlocks units, city improvements, wonders, or governments, so research order shapes the game.
- [Turn structure](../mechanic/turn-structure.md) (core): Turns run from 4000 BC to as late as AD 2100; each turn every city produces and every unit moves, against two to seven AI civilizations.
- [Fog of war](../mechanic/fog-of-war.md) (core): The map starts hidden and is revealed by exploring units; barbarians emerge from huts, unclaimed land, and the sea, and become rarer as exploration proceeds.
- [Faction diplomacy](../mechanic/faction-diplomacy.md) (supporting): Relations with rival civilizations lead to alliances, peace, or war.
- [Policy toggles](../mechanic/policy-toggles.md) (supporting): Government forms unlocked by research change the economic and military rules of the civilization.
- [Taxation](../mechanic/taxation.md) (supporting): The player sets tax rates and the share of trade spent on research.
- [Citizen satisfaction](../mechanic/citizen-satisfaction.md) (supporting): Cities track content and unhappy citizens; luxuries, temples, and wonders keep cities out of civil disorder.
- [Road networks](../mechanic/road-network.md) (supporting): Settlers build roads and later railroads that speed movement between cities.
- [Procedural terrain](../mechanic/procedural-terrain.md) (supporting): Random worlds are generated for each game, with an alternative Earth map.
- [Advisors](../mechanic/advisors.md) (supporting)
- [Corruption leakage](../mechanic/corruption-leakage.md) (supporting): Corruption removes part of each city's trade, rising with distance from the Palace and depending on government type; a Courthouse reduces it.
- [Territorial control](../mechanic/territorial-control.md) (supporting): Cities are captured by moving a military unit into them, transferring the city and its worked tiles to the conqueror.
- [Statistical combat resolution](../mechanic/stat-combat-resolution.md) (supporting): Combat compares the attacker's attack value with the defender's defense under terrain and fortification modifiers and a random draw, and the loser is destroyed.

## Backlinks (computed)

**precedent for:** [Negotiating faction AI](../opportunity/negotiating-faction-ai.md), [Research by named scientists](../opportunity/scientists-not-tech-trees.md)

## Sources

- [Civilization (video game)](../source/src-wikipedia-civilization.md)
- [Technology tree](../source/src-wikipedia-technology-tree.md)
- [Sid Meier](../source/src-wikipedia-sid-meier.md)

---
Provenance: created in run `2026-10-24-catalog-gi`.
