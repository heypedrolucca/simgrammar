# Black & White

*Game* · `black-and-white` · status: **sourced**

A god game in which the player wins villagers' belief through miracles, help, or fear while training a giant creature whose behavior is learned from the player's rewards and punishments.

| field | value |
|---|---|
| aliases | Black and White |
| year | 2001 |
| developer | Lionhead Studios |
| platforms | PC |
| subgenre | God game |
| subgenre secondary | Artificial life |
| sim domain | Social / interpersonal, Biological / ecological |
| player role | God |
| agency model | Supernatural intervention, Caretaking interaction, Indirect incentive |
| time model | Real-time |
| sim scale | Region |
| fidelity | Stylized |
| perspective | Free 3D camera |
| win structure | Campaign |
| failure model | Soft / recoverable |
| narrative mode | Authored |
| multiplayer | Single-player, Competitive |
| modding | None |
| production tier | AAA |
| agent count order | ~100 |
| emergence | 3 |
| influence | 3 |
| influenced by | [Populous](../game/populous.md) |
| cluster *(computed)* | C13 |
| core count *(computed)* | 3 |
| mechanic count *(computed)* | 9 |

## Summary

A god game in which the player wins villagers' belief through miracles, help, or fear while training a giant creature whose behavior is learned from the player's rewards and punishments.

## Core Loop

impress villagers with miracles, help, or fear -> belief grows and worship generates prayer power -> cast miracles with the Hand and gestures -> train the creature with strokes and slaps -> the creature acts on learned desires -> convert rival villages and move to the next island

## Design Notes

Richard Evans built the creature on a belief-desire-intention model after Bratman: beliefs are lists of data about world objects, desires are simplified perceptrons, and opinions are decision trees about how to satisfy a desire; the creature picks the belief with the best opinion for each desire as its intention, and strokes and slaps adjust those opinions by reinforcement. A leash directs the creature's attention so it can learn by observation. The player's actions also move a good-evil alignment that changes the land, interface, music, and followers' view of the god, with a good and an evil advisor arguing each case; alignment has no mechanic id yet (proposal filed). The interface is an animated hand that throws objects and casts gestures instead of icons and panels.

## Relations

**influenced by**

- [Populous](../game/populous.md)

**uses**

- [Creature learning](../mechanic/creature-learning.md) (core): The creature forms intentions from a belief-desire-intention model with perceptron desires and decision-tree opinions; stroking rewards and slapping discourages the last action, the creature remembers and generalizes these responses, and a leash focuses it on actions the player demonstrates.
- [God powers](../mechanic/god-powers.md) (core): Miracles such as food, wood, healing, shields, fireballs, and lightning are cast from the Temple or Village Centre or by drawing gestures with the Hand, powered by villagers' worship, sacrifices, or one-shot Miracle Dispensers.
- [Reputation](../mechanic/reputation.md) (core): Each villager holds a belief level in the player's god, raised by help or intimidation; villagers tire of repeated tactics, and a village converts when enough believe.
- [Creature care](../mechanic/creature-care.md) (supporting): The creature must be fed and taught what and when to eat, and it grows over the game.
- [Needs decay](../mechanic/needs-decay.md) (supporting): Villagers need food, healing, and rest before they will worship.
- [Advisors](../mechanic/advisors.md) (supporting): A good and an evil advisor push the player toward each alignment.
- [Building placement](../mechanic/free-placement.md) (supporting): Buildings are placed from Workshop blueprints and built by villagers.
- [Resource extraction](../mechanic/resource-extraction.md) (supporting): Villagers gather wood and food, for example by fishing.
- [Weather](../mechanic/weather.md) (supporting): Real local weather can be imported.

## Backlinks (computed)

**precedent for:** [Language-agent society terrarium](../opportunity/llm-society-terrarium.md), [Trainable creatures revival](../opportunity/trainable-creatures-revival.md)

## Sources

- [Black & White (video game)](../source/src-wikipedia-black-and-white.md)

---
Provenance: created in run `2026-10-24-catalog-gb`.
