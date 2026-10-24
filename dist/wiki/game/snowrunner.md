# SnowRunner

*Game* · `snowrunner` · status: **sourced**

An off-road trucking sim in which the player hauls cargo across mud, snow, and water whose surfaces deform under each truck's weight and tires, upgrading a fleet to reach harder terrain.

| field | value |
|---|---|
| year | 2020 |
| developer | Saber Interactive |
| platforms | PC, Console, Handheld |
| subgenre | Vehicle sim |
| sim domain | Physical / mechanical, Industrial / logistics |
| player role | Operator / pilot |
| agency model | Direct avatar |
| time model | Real-time |
| sim scale | Individual |
| fidelity | Systemic |
| perspective | Third-person |
| win structure | Completion |
| failure model | Soft / recoverable |
| narrative mode | None |
| multiplayer | Single-player, Co-op |
| modding | Content |
| production tier | AA |
| agent count order | None |
| emergence | 3 |
| influence | 2 |
| cluster *(computed)* | C03 |
| core count *(computed)* | 3 |
| mechanic count *(computed)* | 7 |

## Summary

An off-road trucking sim in which the player hauls cargo across mud, snow, and water whose surfaces deform under each truck's weight and tires, upgrading a fleet to reach harder terrain.

## Core Loop

take a delivery or repair task -> pick truck, tires, and attachments -> drive into deforming mud, snow, or water -> recover when stuck -> deliver cargo -> earn money and rank -> unlock upgrades and new trucks

## Design Notes

Terrain is the antagonist: mud, snow, and water respond to vehicle weight, speed, and momentum, so route choice and tire type matter more than speed, and optional timed contests pay more for faster completion. The physics engine is the one Pavel Zagrebelnyy built for MudRunner, the sequel to Spintires. Mechanical upgrades such as snorkels and chain tires are gated behind progress thresholds, and up to four players can share a map.

## Relations

**uses**

- [Terrain deformation](../mechanic/terrain-deformation.md) (core): Mud, snow, and water react to each truck's weight, speed, and momentum, so ground conditions change as vehicles pass and can bog down underpowered or wrongly fitted trucks.
- [Vehicle dynamics](../mechanic/vehicle-dynamics.md) (core): Tire types, frame attachments, and accessories such as exhaust snorkels for deep water and chain tires for snow change how each of over 60 trucks copes with terrain.
- [Contracts and orders](../mechanic/contracts-orders.md) (core): Missions deliver cargo or complete construction and repair jobs; optional timed contests pay more the faster they are finished.
- [Wear and breakdown](../mechanic/wear-breakdown.md) (supporting): Damage is shown on the vehicle model and in the interface and must be repaired.
- [Milestone unlocks](../mechanic/milestone-unlocks.md) (supporting): Mechanical upgrades require reaching a progress threshold.
- [Fog of war](../mechanic/fog-of-war.md) (supporting)
- [Embodied skill control](../mechanic/embodied-skill-control.md) (supporting)

## Sources

- [SnowRunner](../source/src-wikipedia-snowrunner.md)
- [SnowRunner on Steam](../source/src-steam-2026-snowrunner.md)

---
Provenance: created in run `2026-10-24-catalog-gf`.
