# Schedule I

*Game* · `schedule-i` · status: **sourced**

A first-person crime business sim in which the player grows and cooks drugs, mixes ingredients to create products with effects customers want, sells them around a city under police pressure, and automates production with hired staff.

| field | value |
|---|---|
| year | 2025 |
| developer | TVGS |
| platforms | PC |
| subgenre | Business / economic sim |
| sim domain | Economic, Industrial / logistics |
| player role | Manager / owner |
| agency model | Direct avatar, Direct unit control |
| time model | Real-time |
| sim scale | City |
| fidelity | Stylized |
| perspective | First-person |
| win structure | Campaign |
| failure model | Soft / recoverable |
| narrative mode | Authored |
| multiplayer | Single-player, Co-op |
| modding | Scripting |
| production tier | Indie |
| agent count order | ~100 |
| emergence | 2 |
| influence | 1 |
| cluster *(computed)* | C03 |
| core count *(computed)* | 5 |
| mechanic count *(computed)* | 11 |

## Summary

A first-person crime business sim in which the player grows and cooks drugs, mixes ingredients to create products with effects customers want, sells them around a city under police pressure, and automates production with hired staff.

## Core Loop

grow or cook a base product -> mix in ingredients to add effects -> sell to customers who want those effects -> avoid police searches and curfews -> hire dealers and staff -> buy properties -> unlock new regions

## Design Notes

Schedule I runs a production business through a first-person avatar: the player waters plants, operates mixing and cooking stations, and walks or drives deals across Hyland Point before hiring dealers, botanists, cooks, and janitors to automate the chain. Mixing common ingredients such as soft drinks or paracetamol into a product adds effects that raise its sale value, and customers want particular effects, so recipe discovery is the product-development layer. Police pressure rises with growth through random searches, roadblocks, and curfews, and being seen breaking the law sets a wanted status, a player-heat rule the taxonomy lacks (proposed as heat-wanted-level). The game is in early access, with an exit planned for Q4 2027.

## Relations

**uses**

- [Product development](../mechanic/product-development.md) (core): Mixing ingredients such as soft drinks or paracetamol into a base product adds named effects that raise its value and match customer preferences.
- [Customer value choice](../mechanic/customer-value-choice.md) (core): Customers have preferred effects and price tolerances; matching them builds repeat orders and relationships that open further customers.
- [Crop cultivation](../mechanic/crop-cultivation.md) (core): Plants are grown in pots with soil and water over a growth timer, then harvested as the base product.
- [Direct avatar control](../mechanic/direct-avatar.md) (core): The player personally grows, cooks, mixes, and delivers in first person until staff take over.
- [Staff hiring and rosters](../mechanic/staff-hiring.md) (core): Dealers sell to their own customer lists for a cut, and botanists, cooks, and janitors run production at owned properties.
- [Crime and policing](../mechanic/crime-policing.md) (supporting): Police pressure grows with operations through patrols, random searches, roadblocks, and night curfews; being seen raises a wanted status that can end in arrest.
- [Production chains](../mechanic/production-chain.md) (supporting): Higher products need multi-step chains such as cooking methamphetamine at chemistry stations.
- [Quality tiers](../mechanic/quality-tiers.md) (supporting): Product quality varies with inputs such as soil and additives and affects price.
- [Day-night cycle](../mechanic/day-night-cycle.md) (supporting): A daily clock with a night curfew shapes when deals can be made.
- [Building placement](../mechanic/free-placement.md) (supporting): Grow tents, stations, and storage are placed inside bought properties.
- [Milestone unlocks](../mechanic/milestone-unlocks.md) (supporting): Rank and story progress unlock new regions, customers, and equipment.

## Sources

- [Schedule I (video game)](../source/src-wikipedia-schedule-i.md)
- [Schedule I on Steam](../source/src-steam-2026-schedule-i.md)

---
Provenance: created in run `2026-10-24-catalog-ge`.
