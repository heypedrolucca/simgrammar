# This War of Mine

*Game* · `this-war-of-mine` · status: **sourced**

A survival sim about civilians in a besieged city who maintain a shelter by day, scavenge by night, and face moral choices that change their mood until a randomized ceasefire.

| field | value |
|---|---|
| year | 2014 |
| developer | 11 bit studios |
| platforms | PC, Mobile, Console, Handheld |
| subgenre | Survival sim |
| sim domain | Military / conflict, Social / interpersonal, Domestic / personal |
| player role | Overseer |
| agency model | Direct unit control |
| time model | Real-time |
| sim scale | Household / crew |
| fidelity | Stylized |
| perspective | Top-down / side 2D |
| win structure | Survival duration |
| failure model | Permadeath |
| narrative mode | Hybrid |
| multiplayer | Single-player |
| modding | Content |
| production tier | Indie |
| agent count order | ~10 |
| emergence | 3 |
| influence | 2 |
| cluster *(computed)* | C14 |
| core count *(computed)* | 4 |
| mechanic count *(computed)* | 12 |

## Summary

A survival sim about civilians in a besieged city who maintain a shelter by day, scavenge by night, and face moral choices that change their mood until a randomized ceasefire.

## Core Loop

spend the day in the shelter crafting, cooking, trading, and treating -> assign night roles -> one survivor scavenges a location -> encounters force moral choices -> hunger, wounds, illness, and mood shift -> survive until the ceasefire

## Design Notes

The game turns war into a resource-and-conscience problem: survival needs push the player toward theft or violence, and those acts lower survivors' mood, so material and moral states are coupled. A day-night split separates base management (snipers keep survivors inside by day) from risky scavenging by one chosen survivor, and the length of the war is randomized so the player cannot plan to a known end. The radio reports weather, prices, and war news that let the player anticipate shortages. It draws on the 1992-96 Siege of Sarajevo.

## Relations

**uses**

- [Day-night cycle](../mechanic/day-night-cycle.md) (core): Snipers confine survivors to the shelter by day for crafting, cooking, and care; at night survivors are assigned to sleep, guard, or scavenge.
- [Needs decay](../mechanic/needs-decay.md) (core): Each survivor tracks hunger, fatigue, health, and mood, and the player must keep them up until the ceasefire.
- [Mood and breakdowns](../mechanic/mood-breakdown.md) (core): Mood falls with hunger, illness, loss of companions, and morally weighted acts such as stealing or killing; depressed or broken survivors refuse tasks and may leave the shelter or take their own lives.
- [Dilemma cards](../mechanic/dilemma-cards.md) (core): Scavenging encounters and visitors at the door pose choices, such as robbing vulnerable NPCs or giving away supplies, that trade material gain against mood and each survivor's ending.
- [Personality traits](../mechanic/personality-traits.md) (supporting): Each survivor has one or two traits, such as Good Cook, plus hidden stats.
- [Hand crafting](../mechanic/hand-crafting.md) (supporting): Workshops craft weapons, alcohol, beds, stoves, and shelter upgrades from scavenged materials.
- [Forecasting](../mechanic/forecasting.md) (supporting): Radio broadcasts give weather warnings, economic updates, and war news.
- [Supply-demand pricing](../mechanic/supply-demand-pricing.md) (supporting): Barter values change with conditions announced on the radio.
- [Seasons](../mechanic/seasons.md) (supporting): Winter raises demand for heating fuel.
- [Triggered event chains](../mechanic/triggered-event-chains.md) (supporting): Neighbors and strangers arrive with requests tied to the shelter's state.
- [Permadeath](../mechanic/permadeath.md) (supporting)
- [Stimulus attraction](../mechanic/stimulus-attraction.md) (supporting): Noisy actions while scavenging at night, such as breaking through obstacles, can alert people at the location.

## Backlinks (computed)

**influenced:** [Frostpunk](../game/frostpunk.md)

**precedent for:** [Drama-aware storyteller](../opportunity/drama-aware-storyteller.md)

## Sources

- [This War of Mine](../source/src-wikipedia-this-war-of-mine.md)
- [This War of Mine on Steam](../source/src-steam-2026-this-war-of-mine.md)

---
Provenance: created in run `2026-10-24-catalog-gb`.
