# Nintendogs

*Game* · `nintendogs` · status: **sourced**

A Nintendo DS puppy sim in which the player pets, washes, feeds, and walks up to three dogs, teaches them tricks with recorded voice commands, and enters disc, agility, and obedience trials.

| field | value |
|---|---|
| year | 2005 |
| developer | Nintendo EAD |
| platforms | Handheld |
| subgenre | Virtual pet |
| sim domain | Biological / ecological, Domestic / personal |
| player role | Caretaker |
| agency model | Caretaking interaction, Conversational |
| time model | Real-world clock |
| sim scale | Individual |
| fidelity | Stylized |
| perspective | First-person |
| win structure | Open sandbox |
| failure model | Soft / recoverable |
| narrative mode | None |
| multiplayer | Single-player, Async / shared content |
| modding | None |
| production tier | AAA |
| agent count order | ~1 |
| emergence | 2 |
| influence | 3 |
| cluster *(computed)* | C13 |
| core count *(computed)* | 2 |
| mechanic count *(computed)* | 7 |

## Summary

A Nintendo DS puppy sim in which the player pets, washes, feeds, and walks up to three dogs, teaches them tricks with recorded voice commands, and enters disc, agility, and obedience trials.

## Core Loop

care for the dog by touch -> teach tricks by voice -> walk the dog and find items -> enter disc, agility, and obedience trials -> earn prize money and trainer points -> buy supplies and unlock new breeds

## Design Notes

Nintendogs was built to show off DS hardware: the touchscreen handles petting, grooming, and washing, and the microphone handles the dog's name and trick commands. Care runs on the DS clock, so hunger, thirst, and coat condition worsen with elapsed time, but dogs cannot die, breed, or age, which makes neglect a recoverable setback rather than a fail state. Trials have five classes from Beginner to Championship, and placing third or better promotes a dog. Bark Mode lets nearby players' dogs meet and exchange presents.

## Relations

**uses**

- [Creature care](../mechanic/creature-care.md) (core): Touch petting, brushing, and washing plus food and water bowls maintain hunger, thirst, and coat condition; walks, balls, discs, and toys add play.
- [Creature learning](../mechanic/creature-learning.md) (core): When the dog strikes a pose such as sit, the player records a spoken command; repeating the pairing teaches the trick, and the dog later responds to the voice cue.
- [Natural-language interaction](../mechanic/natural-language-interaction.md) (supporting): The microphone recognizes the dog's name and trick words by matching the player's voice against recorded samples.
- [Needs decay](../mechanic/needs-decay.md) (supporting): Hunger, thirst, and dirtiness worsen with real elapsed time.
- [Real-time clock](../mechanic/real-time-clock.md) (supporting): Care state advances with the DS internal clock and calendar.
- [Milestone unlocks](../mechanic/milestone-unlocks.md) (supporting): Trial prize money and trainer points unlock new breeds and supplies.
- [Asynchronous shared regions](../mechanic/async-shared-region.md) (supporting): Bark Mode lets nearby DS owners meet each other's dogs and exchange presents.

## Backlinks (computed)

**precedent for:** [Trainable creatures revival](../opportunity/trainable-creatures-revival.md)

## Sources

- [Nintendogs](../source/src-wikipedia-nintendogs.md)

---
Provenance: created in run `2026-10-24-catalog-gc`.
