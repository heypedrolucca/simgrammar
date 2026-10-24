# Manor Lords

*Game* · `manor-lords` · status: **sourced**

An early-access medieval city builder in which families settle gridless burgage plots along curved roads, fields depend on soil fertility and crop rotation, and the lord fields retinue and militia in real-time battles.

| field | value |
|---|---|
| year | 2024 |
| developer | Slavic Magic |
| platforms | PC |
| subgenre | City builder |
| sim domain | Urban, Economic, Military / conflict |
| player role | Ruler / statesman |
| agency model | Zoning / placement, Policy / parameter, Direct unit control |
| time model | Real-time with pause |
| sim scale | Settlement |
| fidelity | Stylized |
| perspective | Free 3D camera |
| win structure | Open sandbox |
| failure model | Soft / recoverable |
| narrative mode | Emergent |
| multiplayer | Single-player |
| modding | Content |
| production tier | Indie |
| agent count order | ~100 |
| emergence | 3 |
| influence | 1 |
| cluster *(computed)* | C01 |
| core count *(computed)* | 2 |
| mechanic count *(computed)* | 12 |

## Summary

An early-access medieval city builder in which families settle gridless burgage plots along curved roads, fields depend on soil fertility and crop rotation, and the lord fields retinue and militia in real-time battles.

## Core Loop

draw curved roads and burgage plots -> families move in and staff workplaces -> fields, backyard extensions, and production chains feed the market -> taxes, tithes, and trade fund a retinue -> defend against bandits and rival lords

## Design Notes

Manor Lords drops the zoning grid: the player draws plots against freely curved roads, the game divides them into burgage plots, and households extend them with backyard gardens, chickens, or goats, so housing is also production. Fields carry soil fertility per crop that rotation preserves, and hunting depends on animal populations that overexpansion drives away. Militia levies come from the town's own families, so each battle death is a lost worker; the game remained in early access as of August 2026.

## Relations

**uses**

- [Zoning](../mechanic/zoning.md) (core): Residential plots drawn along roads are divided into burgage plots that families build on and extend with backyard production.
- [Crop cultivation](../mechanic/crop-cultivation.md) (core): Fields depend on soil fertility per crop; rotation and fallow maintain yields, and overuse exhausts soil.
- [Road networks](../mechanic/road-network.md) (supporting): Roads curve freely and plots and buildings take their shape from them.
- [Seasons](../mechanic/seasons.md) (supporting): Spring rains and winter snow change work and needs.
- [Production chains](../mechanic/production-chain.md) (supporting): Raw materials pass through workshops into goods, weapons, and armor.
- [Goods consumption](../mechanic/goods-consumption.md) (supporting): Households need basic goods and luxuries; shortfalls lower satisfaction.
- [Citizen satisfaction](../mechanic/citizen-satisfaction.md) (supporting): Approval responds to supply, taxes, and tithes.
- [Taxation](../mechanic/taxation.md) (supporting): Six tax types, a yearly King's tax, and tithes on villagers.
- [Renewable regrowth](../mechanic/renewable-regrowth.md) (supporting): Hunting grounds depend on animal populations; overexpansion drives deer away and deforests land.
- [Unit commands](../mechanic/unit-commands.md) (supporting): Real-time battles with fatigue, weather, and equipment; retinue, mercenaries, and militia drawn from townspeople.
- [Raid defense](../mechanic/raid-defense.md) (supporting): Bandit raids threaten the town and loot stores.
- [Trade routes](../mechanic/trade-routes.md) (supporting): Surpluses sold to traveling merchants; imports and exports balanced through trade.

## Backlinks (computed)

**precedent for:** [Learned build assist for cities](../opportunity/learned-build-assist.md), [Placement that tells stories](../opportunity/placement-that-tells-stories.md)

## Sources

- [Manor Lords](../source/src-wikipedia-manor-lords.md)
- [Manor Lords on Steam](../source/src-steam-2026-manor-lords.md)

---
Provenance: created in run `2026-10-24-catalog-ga`.
