# Creature care

*Mechanic* · `creature-care` · status: **sourced**

The player directly feeds, cleans, and plays with a creature whose needs decay; neglect causes sickness, stunted growth, or death.

| field | value |
|---|---|
| aliases | virtual pet, pet care |
| family | Biology & health |
| substrate | Agent-based, Aggregate stocks |
| math basis | System dynamics / ODEs, Control theory |
| feedback | Balancing (negative) |
| player interface | Direct manipulation, Choice / cards, Language |
| legibility | 4 |
| emergence potential | 2 |
| authoring cost | 4 |
| compute cost | 1 |
| tuning difficulty | 2 |
| ai leverage | 4 |
| maturity | Classic |
| specializes | [Needs decay](../mechanic/needs-decay.md) |
| core count *(computed)* | 5 |
| earliest game *(computed)* | [Little Computer People](../game/little-computer-people.md) |
| earliest year *(computed)* | 1985 |
| prevalence *(computed)* | 6 |
| prevalence share *(computed)* | 0.034 |
| subgenre spread *(computed)* | 4 |
| technique count *(computed)* | 0 |
| technique exposure *(computed)* | 0.0 |

## Definition

Owns one or a few creatures, each with need meters (hunger, happiness, hygiene, health, discipline), a life stage, and often an affection or obedience value. Meters decay in game or real time, and the player restores them with direct care actions: feeding, cleaning, playing, giving medicine, or scolding. Neglect accumulates into sickness, a worse adult form, running away, or death. Tamagotchi (1996) shows hunger and happy meters and a discipline meter, leaves droppings that cause sickness if not cleaned, cures illness with medicine, and ages the pet through life stages in real time; Nintendogs adds stylus petting and voice-recognized commands; Seaman responds to the player's speech. Inputs are care actions and elapsed time; outputs are the creature's condition, form, and behavior.

## Player Experience

Responsibility and attachment. The player checks in often, notices small changes, and feels guilt when the creature gets sick from being forgotten. Care is direct and tactile rather than managerial, and the creature's growth or decline mirrors the player's attention.

## Design Levers

- number of needs and their decay rates in game or real time
- severity of neglect consequences: mood, sickness, altered growth, death, leaving
- care actions available and whether they are menu choices or direct manipulation
- whether care quality shapes the adult form or personality
- pause or vacation options that suspend decay

## Failure Modes

- Real-time decay with no pause punishes absence; the first Tamagotchi units could stop time only through the clock-setting mode.
- Once the optimal care routine is known, interactions become a checklist and attachment fades.
- Creatures with too few reactions repeat the same animations, breaking the illusion of a living pet.

## Dynamics

- Check-in frequency becomes the main loop, coupling the game to the player's daily schedule.
- Care quality branching into different adult forms motivates replays and comparison between players.
- Shared or shown-off pets turn care quality into social status.

## Open Questions

- Can language models give pets memory and open-ended conversational responses while keeping their needs legible?
- Does generated animation or behavior reduce the repetition that ends attachment?

## Relations

**specializes**

- [Needs decay](../mechanic/needs-decay.md)

**synergy**

- [Real-time clock](../mechanic/real-time-clock.md): Wall-clock decay makes care a daily ritual and absence meaningful (Tamagotchi).

## Backlinks (computed)

**involved in:** [Trainable creatures revival](../opportunity/trainable-creatures-revival.md)

**used by:** [Black & White](../game/black-and-white.md), [Creatures](../game/creatures.md), [Little Computer People](../game/little-computer-people.md), [Nintendogs](../game/nintendogs.md), [Seaman](../game/seaman.md), [Tamagotchi](../game/tamagotchi.md)

## Sources

- [Tamagotchi](../source/src-wikipedia-tamagotchi.md)

---
Provenance: created in run `2026-10-24-taxonomy-m5`.
