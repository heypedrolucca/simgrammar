# Viva Piñata

*Game* · `viva-pinata` · status: **sourced**

A garden sim in which the player shapes terrain, plants, and water to attract 60 piñata species, then meets each species' requirements to make them residents, breed them, and manage the predators among them.

| field | value |
|---|---|
| year | 2006 |
| developer | Rare |
| platforms | Console, PC |
| subgenre | Ecosystem / evolution |
| subgenre secondary | Farming sim |
| sim domain | Biological / ecological |
| player role | Caretaker |
| agency model | Indirect incentive, Zoning / placement, Caretaking interaction |
| time model | Real-time |
| sim scale | Facility |
| fidelity | Stylized |
| perspective | Free 3D camera |
| win structure | Open sandbox |
| failure model | Soft / recoverable |
| narrative mode | Hybrid |
| multiplayer | Single-player, Async / shared content |
| modding | None |
| production tier | AAA |
| agent count order | ~100 |
| emergence | 2 |
| influence | 2 |
| cluster *(computed)* | C07 |
| core count *(computed)* | 4 |
| mechanic count *(computed)* | 9 |

## Summary

A garden sim in which the player shapes terrain, plants, and water to attract 60 piñata species, then meets each species' requirements to make them residents, breed them, and manage the predators among them.

## Core Loop

dig, plant, and water the garden -> species outlines appear when appear requirements are met -> resident requirements turn visitors into residents -> residents meet romance requirements and lay eggs -> predators and sours disrupt -> sell or trade piñatas -> attract new species

## Design Notes

Viva Piñata turns habitat suitability into a readable checklist: each species has staged appear, visit, resident, and romance requirements, shown as a black-and-white outline that fills in when residency is met. Because piñatavores must eat other piñatas to become residents or breed, attracting one species can consume another, so the garden is a hand-built food web the player tunes by fencing, spacing, and timing. Sours and Professor Pester's ruffians supply authored pressure, and romance requirements can be bypassed with candy once a species has bred, trading early difficulty for collection speed.

## Relations

**uses**

- [Habitat suitability](../mechanic/habitat-suitability.md) (core): Each of the 60 species has staged requirements (garden contents, plants, water, terrain, or having eaten a specific item) that turn an outline into a visitor and then a resident.
- [Food web](../mechanic/food-web.md) (core): Piñatavores must eat other piñatas to become residents or breed, and visiting predators eat residents to meet their own requirements.
- [Animal husbandry](../mechanic/animal-husbandry.md) (core): Two residents of a species that meet romance requirements perform a romance dance and a maze minigame that yields an egg; piñatas are ungendered, and candy skips romance requirements after a species' first romance.
- [Collection goals](../mechanic/collection-goals.md) (core): The journal of 60 species, each with requirements to discover, is the long-term goal structure.
- [Crop cultivation](../mechanic/crop-cultivation.md) (supporting): Seeds sown with tools grow into flowers, vegetables, and trees that species eat or require; weeds spread and destroy vegetable rows if not removed.
- [Terraforming](../mechanic/terraforming.md) (supporting): The shovel and other tools plough soil, dig ponds, and sculpt terrain.
- [Building placement](../mechanic/free-placement.md) (supporting)
- [Milestone unlocks](../mechanic/milestone-unlocks.md) (supporting)
- [Asynchronous shared regions](../mechanic/async-shared-region.md) (supporting): Eggs and piñatas could be sent to other players over Xbox Live.

## Sources

- [Viva Piñata (video game)](../source/src-wikipedia-viva-pinata.md)

---
Provenance: created in run `2026-10-24-catalog-gd`.
