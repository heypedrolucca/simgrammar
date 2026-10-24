# Seaman

*Game* · `seaman` · status: **sourced**

A Dreamcast virtual pet in which the player talks through a microphone to a sardonic human-faced fish, managing its tank's heat, water, and food while it matures through five life stages.

| field | value |
|---|---|
| year | 1999 |
| developer | Vivarium |
| platforms | Console |
| subgenre | Virtual pet |
| sim domain | Biological / ecological, Social / interpersonal |
| player role | Caretaker |
| agency model | Caretaking interaction, Conversational |
| time model | Real-world clock |
| sim scale | Individual |
| fidelity | Stylized |
| perspective | First-person |
| win structure | Completion |
| failure model | Hard restart |
| narrative mode | Hybrid |
| multiplayer | Single-player |
| modding | None |
| production tier | AA |
| agent count order | ~1 |
| emergence | 2 |
| influence | 2 |
| cluster *(computed)* | C13 |
| core count *(computed)* | 4 |
| mechanic count *(computed)* | 8 |

## Summary

A Dreamcast virtual pet in which the player talks through a microphone to a sardonic human-faced fish, managing its tank's heat, water, and food while it matures through five life stages.

## Core Loop

check the tank each real day -> adjust heat, clean water, and feed -> talk to Seaman through the microphone -> it learns words and asks about the player -> the life stage advances through breeding and die-off -> raise the Frogman generation and release it

## Design Notes

Yoot Saito built Seaman around speech: a microphone accessory lets the player answer questions and make small talk, early Gillmen repeat the player's words back as gibberish, and the creature's vocabulary grows while it keeps insulting the player. The care loop is sparse but strict, with roughly one check per real day needed to keep it alive, so the game paces itself to the player's calendar. Its life cycle is scripted and harsh: Gillmen fight until two remain, Podfish die after mating, Tadmen eat each other until two remain, and the final Frogmen are released into the wild. Leonard Nimoy narrates the English version as a guide who explains only part of the rules.

## Relations

**uses**

- [Creature care](../mechanic/creature-care.md) (core): The player sets tank heat, cleans dirty water, and supplies food, and later runs a sprinkler to keep Frogmen moist.
- [Natural-language interaction](../mechanic/natural-language-interaction.md) (core): Microphone speech is matched against the creature's current vocabulary; it asks for the player's birthday and other details and answers in conversation.
- [Lifecycle and aging](../mechanic/lifecycle-aging.md) (core): Mushroomer, Gillman, Podfish, Tadman, and Frogman stages; Podfish parents die after mating and the aquarium becomes a terrarium.
- [Real-time clock](../mechanic/real-time-clock.md) (core): Time follows the real calendar; going much longer than a day without a check can kill the creature.
- [Creature learning](../mechanic/creature-learning.md) (supporting): Vocabulary grows through conversation, and the creature becomes tamer over time.
- [Memories and thoughts](../mechanic/memories-thoughts.md) (supporting): It remembers facts the player shares, such as a birthday, and later tells historical events from that date.
- [Habitat suitability](../mechanic/habitat-suitability.md) (supporting): Tank temperature and water cleanliness must suit the current life stage.
- [Permadeath](../mechanic/permadeath.md) (supporting): A neglected creature dies permanently.

## Backlinks (computed)

**precedent for:** [Trainable creatures revival](../opportunity/trainable-creatures-revival.md)

## Sources

- [Seaman (video game)](../source/src-wikipedia-seaman.md)

---
Provenance: created in run `2026-10-24-catalog-gc`.
