# Farming Simulator 25

*Game* · `farming-simulator-25` · status: **sourced**

The 2024 entry in Giants Software's series in which the player runs a farm business by operating over 400 licensed vehicles and implements across seasonal field work, livestock, forestry, and production chains.

| field | value |
|---|---|
| year | 2024 |
| developer | Giants Software |
| platforms | PC, Console |
| subgenre | Farming sim |
| subgenre secondary | Vehicle sim |
| sim domain | Occupational, Biological / ecological, Economic |
| player role | Operator / pilot |
| agency model | Direct avatar, Direct unit control |
| time model | Real-time with pause |
| sim scale | Facility |
| fidelity | Stylized |
| perspective | Third-person |
| win structure | Open sandbox |
| failure model | Soft / recoverable |
| narrative mode | None |
| multiplayer | Single-player, Co-op |
| modding | Scripting |
| production tier | AA |
| agent count order | ~10 |
| emergence | 2 |
| influence | 2 |
| cluster *(computed)* | C06 |
| core count *(computed)* | 2 |
| mechanic count *(computed)* | 13 |

## Summary

The 2024 entry in Giants Software's series in which the player runs a farm business by operating over 400 licensed vehicles and implements across seasonal field work, livestock, forestry, and production chains.

## Core Loop

buy fields and machinery -> plow, seed, fertilize, and harvest with implements -> store or sell crops or feed productions and animals -> take contracts for extra income -> reinvest in land, buildings, and equipment

## Design Notes

Farming Simulator models agriculture as ordered field operations performed with specific implements, so the challenge is machine operation and fleet logistics rather than market strategy. FS25 lists 25 crop types including two rice varieties grown in paddies, spinach, peas, and green beans, adds water buffalo and goats, adds twisters and hail that damage crops, and deforms soft ground under tires. Dynamically generated contracts pay for work on other farms, and the in-game ModHub distributes developer-tested community vehicles, maps, and scripts.

## Relations

**uses**

- [Crop cultivation](../mechanic/crop-cultivation.md) (core): Fields move through cultivating or plowing, seeding, fertilizing, weeding, and harvesting with matching implements; 25 crop types follow seasonal calendars, with rice grown in paddies.
- [Vehicle dynamics](../mechanic/vehicle-dynamics.md) (core): The player drives over 400 licensed vehicles and implements from more than 150 brands, each with its own power, speed, and weight; GPS-assisted steering automates straight passes.
- [Wear and breakdown](../mechanic/wear-breakdown.md) (supporting): Vehicles accumulate wear and damage that reduce performance until repaired at a workshop.
- [Terrain deformation](../mechanic/terrain-deformation.md) (supporting): Tires leave tracks that deform soft ground.
- [Animal husbandry](../mechanic/animal-husbandry.md) (supporting): Cows, sheep, pigs, chickens, horses, water buffalo, and goats with offspring need feed and care and yield products.
- [Production chains](../mechanic/production-chain.md) (supporting): Productions and farm shops convert crops into processed goods as business ventures.
- [Contracts and orders](../mechanic/contracts-orders.md) (supporting): Dynamically generated contracts such as mowing, fertilizing, or hauling pay for work on other farmers' fields.
- [Delegation to AI managers](../mechanic/delegation-to-ai.md) (supporting): Hired AI helpers drive vehicles to work fields while the player does other tasks.
- [Seasons](../mechanic/seasons.md) (supporting): A seasonal cycle, introduced in FS22, sets planting and harvest windows.
- [Weather](../mechanic/weather.md) (supporting)
- [Random disasters](../mechanic/random-disasters.md) (supporting): Twisters and hail can damage crops.
- [Loans and debt](../mechanic/loans-debt.md) (supporting): Bank loans fund early expansion.
- [Modding API](../mechanic/modding-api.md) (supporting): ModHub distributes developer-tested community mods that add vehicles, maps, and scripts.

## Backlinks (computed)

**precedent for:** [Learned regional weather](../opportunity/learned-weather-layer.md)

## Sources

- [Farming Simulator 25 on Steam](../source/src-steam-2024-farming-simulator-25.md)
- [Farming Simulator](../source/src-wikipedia-farming-simulator.md)

---
Provenance: created in run `2026-10-24-catalog-gc`.
