# From Dust

*Game* · `from-dust` · status: **sourced**

A god game in which the player carries sand, water, and lava across islands whose material simulation erodes, floods, and hardens terrain, protecting a tribe as it founds villages at totems.

| field | value |
|---|---|
| year | 2011 |
| developer | Ubisoft Montpellier |
| platforms | Console, PC, Web |
| subgenre | God game |
| subgenre secondary | Physics sandbox |
| sim domain | Planetary / natural, Physical / mechanical |
| player role | God |
| agency model | Supernatural intervention, Direct unit control |
| time model | Real-time |
| sim scale | Region |
| fidelity | Stylized |
| perspective | Free 3D camera |
| win structure | Campaign |
| failure model | Soft / recoverable |
| narrative mode | Authored |
| multiplayer | Single-player |
| modding | None |
| production tier | AA |
| agent count order | ~100 |
| emergence | 3 |
| influence | 2 |
| influenced by | [Populous](../game/populous.md) |
| cluster *(computed)* | C07 |
| core count *(computed)* | 3 |
| mechanic count *(computed)* | 8 |

## Summary

A god game in which the player carries sand, water, and lava across islands whose material simulation erodes, floods, and hardens terrain, protecting a tribe as it founds villages at totems.

## Core Loop

carry sand, water, and lava with the Breath -> reshape terrain to open paths -> send villagers to totems to found villages -> vegetation spreads across soil -> divert tsunamis, floods, fires, and eruptions -> unlock powers and reach the portal

## Design Notes

Designed by Eric Chahi and presented as a spiritual successor to Populous, it replaces discrete land raising with a continuous material simulation: water flows and erodes, lava cools into solid rock, and soil lets vegetation spread once a village is founded, fast enough that islands can be reshaped within minutes. The cursor, called the Breath, carries matter and changes appearance to match it, replacing a conventional HUD. Disasters are announced shortly before they hit, so each map alternates between building and short preparation windows.

## Relations

**influenced by**

- [Populous](../game/populous.md)

**uses**

- [Terraforming](../mechanic/terraforming.md) (core): The Breath picks up and deposits sand, water, and lava in real time to build land bridges, dams, and barriers.
- [Hydrology](../mechanic/hydrology.md) (core): Water flows over the terrain, erodes it, and floods low ground and villages; tsunamis sweep across islands.
- [Material interactions](../mechanic/material-interactions.md) (core): Lava cools into solid rock, water erodes soil, fire burns vegetation, and powers can jellify or remove water.
- [God powers](../mechanic/god-powers.md) (supporting): Powers such as jellifying water are granted by completing objectives; magical stones protect against water and fire.
- [Random disasters](../mechanic/random-disasters.md) (supporting): Tsunamis and eruptions, announced shortly before by shamans.
- [Fire spread](../mechanic/fire-spread.md) (supporting): Wildfires spread through vegetation and can be extinguished.
- [Unit commands](../mechanic/unit-commands.md) (supporting): Villagers are sent to totems to found villages.
- [Scenario objectives](../mechanic/scenario-objectives.md) (supporting): Each map is cleared by settling every totem to open a portal.

## Sources

- [From Dust](../source/src-wikipedia-from-dust.md)

---
Provenance: created in run `2026-10-24-catalog-gb`.
