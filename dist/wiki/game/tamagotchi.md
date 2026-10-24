# Tamagotchi

*Game* · `tamagotchi` · status: **sourced**

A 1996 keychain virtual pet whose hunger, happiness, and training meters run on a real-time clock, and whose care quality determines which adult form it grows into and how long it lives.

| field | value |
|---|---|
| year | 1996 |
| developer | Bandai |
| platforms | Dedicated device |
| subgenre | Virtual pet |
| sim domain | Biological / ecological |
| player role | Caretaker |
| agency model | Caretaking interaction |
| time model | Real-world clock |
| sim scale | Individual |
| fidelity | Abstract |
| perspective | Device LCD |
| win structure | Survival duration |
| failure model | Hard restart |
| narrative mode | None |
| multiplayer | Single-player |
| modding | None |
| production tier | AA |
| agent count order | ~1 |
| emergence | 2 |
| influence | 4 |
| cluster *(computed)* | C13 |
| core count *(computed)* | 4 |
| mechanic count *(computed)* | 8 |

## Summary

A 1996 keychain virtual pet whose hunger, happiness, and training meters run on a real-time clock, and whose care quality determines which adult form it grows into and how long it lives.

## Core Loop

pet calls for attention -> feed a meal or snack, play, scold, clean, or give medicine -> meters and care history accumulate -> pet ages after each sleep -> care history selects its next form -> it lives on or dies

## Design Notes

Aki Maita and Akihiro Yokoi reduced a pet to three meters (Hunger, Happy, Training) plus droppings and sickness on a three-button LCD device that runs continuously; early units could pause only through the clock settings. Meals fill Hunger, snacks and a minigame raise Happy but excess snacks cause illness, scolding when the pet calls for attention fills Training, and uncleaned droppings lead to sickness shown by a skull. Each life stage lasts a set number of days and age advances when the pet wakes, and care quality selects the adult character, turning care history into a visible outcome (proposed as care-dependent-development).

## Relations

**uses**

- [Creature care](../mechanic/creature-care.md) (core): Care actions are meal, snack, game, scold, clean, and medicine; meals are limited by fullness while snacks are not, and excess snacks cause sickness.
- [Needs decay](../mechanic/needs-decay.md) (core): Hunger and Happy meters, shown as hearts, deplete over real time and are refilled by meals, snacks, and the minigame.
- [Real-time clock](../mechanic/real-time-clock.md) (core): The pet lives on the device clock set at hatching and sleeps nightly; time keeps passing between check-ins.
- [Lifecycle and aging](../mechanic/lifecycle-aging.md) (core): Baby, Child, Teenager, Adult, and Special stages (plus Senior in some models) each last a set number of days, with age advancing on waking; old age eventually ends its life.
- [Permadeath](../mechanic/permadeath.md) (supporting): Poor care, sickness, or old age kills the pet; the A and C buttons start a new egg.
- [Day-night cycle](../mechanic/day-night-cycle.md) (supporting): A nightly sleep period suspends care demands and marks age increments.
- [Alerts feed](../mechanic/alerts-feed.md) (supporting): The device beeps and shows an attention icon when the pet needs care or calls for discipline.
- [Care-dependent development](../mechanic/care-dependent-development.md) (supporting): Care quality during each life stage, such as unanswered calls, overfeeding snacks, and uncleaned droppings, selects the next form, so the same egg can grow into different adult characters.

## Backlinks (computed)

**precedent for:** [Trainable creatures revival](../opportunity/trainable-creatures-revival.md)

## Sources

- [Tamagotchi](../source/src-wikipedia-tamagotchi.md)

---
Provenance: created in run `2026-10-24-catalog-gc`.
