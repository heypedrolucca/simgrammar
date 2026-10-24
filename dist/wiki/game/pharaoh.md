# Pharaoh

*Game* · `pharaoh` · status: **sourced**

An Egyptian city builder on the Caesar III engine in which a yearly Nile flood waters floodplain farms, walkers carry services to housing, five gods must be appeased, and monuments take years of labor and materials.

| field | value |
|---|---|
| year | 1999 |
| developer | Impressions Games |
| platforms | PC |
| subgenre | City builder |
| sim domain | Urban, Economic |
| player role | Planner / mayor |
| agency model | Zoning / placement, Policy / parameter |
| time model | Real-time with pause |
| sim scale | City |
| fidelity | Stylized |
| perspective | Isometric |
| win structure | Campaign |
| failure model | Soft / recoverable |
| narrative mode | Hybrid |
| multiplayer | Single-player |
| modding | None |
| production tier | AA |
| agent count order | ~100 |
| emergence | 3 |
| influence | 2 |
| influenced by | [Caesar III](../game/caesar-3.md) |
| cluster *(computed)* | C02 |
| core count *(computed)* | 3 |
| mechanic count *(computed)* | 15 |

## Summary

An Egyptian city builder on the Caesar III engine in which a yearly Nile flood waters floodplain farms, walkers carry services to housing, five gods must be appeased, and monuments take years of labor and materials.

## Core Loop

lay out housing, roads, and floodplain farms -> the yearly Nile flood waters the farms -> walkers deliver services, food, and goods to houses -> houses evolve and pay taxes -> appease five gods and build monuments to meet mission goals

## Design Notes

Pharaoh reuses Caesar III's walker model and adds a calendar driven by the Nile: floodplain farms can only be worked between floods, irrigation ditches raise fertility, and the god Osiris can improve or worsen the flood. Monuments need worker facilities and delivered materials and take in-game years, a construction-logistics system with no exact taxonomy match (see run proposal). Five gods (Ra, Bast, Osiris, Ptah, Seth) grant gifts when appeased with shrines and temples and send disasters when angered.

## Relations

**influenced by**

- [Caesar III](../game/caesar-3.md)

**uses**

- [Walker service delivery](../mechanic/walker-service-delivery.md) (core): Fire marshals, constables, and other service walkers roam roads from their buildings and cover the houses they pass.
- [Population strata](../mechanic/population-strata.md) (core): Housing improves in level when demands for goods, services, and surroundings are met.
- [Hydrology](../mechanic/hydrology.md) (core): A yearly Nile flood waters floodplain farms; irrigation ditches extend fertile land, and Osiris can raise or lower the flood quality.
- [Crop cultivation](../mechanic/crop-cultivation.md) (supporting): Floodplain and meadow farms yield by fertility and season.
- [Seasons](../mechanic/seasons.md) (supporting): The flood season fixes when floodplain land can be farmed.
- [Production chains](../mechanic/production-chain.md) (supporting)
- [Goods consumption](../mechanic/goods-consumption.md) (supporting): Houses need food and goods to advance.
- [Trade routes](../mechanic/trade-routes.md) (supporting): Raw materials and goods trade with other cities for money.
- [Scenario objectives](../mechanic/scenario-objectives.md) (supporting): Missions set population, rating, and monument goals.
- [Labor market](../mechanic/labor-market.md) (supporting): Buildings and monument crews draw workers from housing.
- [Megaproject sink](../mechanic/megaproject-sink.md) (supporting): Monuments such as pyramids need delivered materials and worker crews over in-game years, and many missions require completing them.
- [Pause and speed control](../mechanic/variable-speed.md) (supporting)
- [Building placement](../mechanic/free-placement.md) (supporting)
- [Fire spread](../mechanic/fire-spread.md) (supporting)
- [Storage and buffers](../mechanic/storage-capacity.md) (supporting)

## Sources

- [Pharaoh (video game)](../source/src-wikipedia-pharaoh.md)

---
Provenance: created in run `2026-10-24-catalog-ga`; reviewed in `2026-10-24-review-fixes`.
