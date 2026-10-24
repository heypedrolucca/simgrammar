# Populous

*Game* · `populous` · status: **sourced**

The first god game, in which the player raises and lowers land so followers can build and multiply, then spends the mana they generate on disasters against a rival deity's people.

| field | value |
|---|---|
| year | 1989 |
| developer | Bullfrog Productions |
| platforms | PC, Console, Handheld |
| subgenre | God game |
| sim domain | Planetary / natural, Military / conflict |
| player role | God |
| agency model | Supernatural intervention, Indirect incentive |
| time model | Real-time |
| sim scale | Region |
| fidelity | Abstract |
| perspective | Isometric |
| win structure | Competitive victory |
| failure model | Hard restart |
| narrative mode | None |
| multiplayer | Single-player, Competitive |
| modding | None |
| production tier | Indie |
| agent count order | ~100 |
| emergence | 2 |
| influence | 5 |
| cluster *(computed)* | C07 |
| core count *(computed)* | 2 |
| mechanic count *(computed)* | 5 |

## Summary

The first god game, in which the player raises and lowers land so followers can build and multiply, then spends the mana they generate on disasters against a rival deity's people.

## Core Loop

raise and lower land to make flat ground -> followers settle and build houses -> houses breed followers and raise mana -> spend mana on knights, earthquakes, swamps, volcanoes, and floods -> overwhelm the rival deity's followers

## Design Notes

Populous established the god game by making terrain the player's main tool and population the player's currency: flat land lets followers build larger houses, houses produce followers, and followers produce mana for powers, so shaping the land is also running the economy. The landscape type of each world (desert, lava, snow and ice) changes how followers develop. Population growth from housing has no mechanic id yet (proposal filed). The game ships 500 worlds, each won by outgrowing and destroying the opposing population.

## Relations

**uses**

- [Terraforming](../mechanic/terraforming.md) (core): Raising and lowering land is the basic power; its main use is creating flat ground on which followers can build larger settlements.
- [God powers](../mechanic/god-powers.md) (core): Mana from the follower population unlocks progressively stronger interventions: knights, earthquakes, swamps, volcanoes, and floods.
- [Unit commands](../mechanic/unit-commands.md) (supporting): A papal magnet and behavior modes send followers to settle, gather, or fight.
- [Habitat suitability](../mechanic/habitat-suitability.md) (supporting): Landscape type changes how followers develop.
- [Scenario objectives](../mechanic/scenario-objectives.md) (supporting): 500 worlds, each won by defeating the enemy's followers.

## Backlinks (computed)

**influenced:** [Black & White](../game/black-and-white.md), [Sid Meier's Civilization](../game/civilization.md), [From Dust](../game/from-dust.md)

## Sources

- [Populous (video game)](../source/src-wikipedia-populous.md)

---
Provenance: created in run `2026-10-24-catalog-gb`.
