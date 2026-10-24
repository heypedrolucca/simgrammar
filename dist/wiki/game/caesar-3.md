# Caesar III

*Game* · `caesar-3` · status: **sourced**

A Roman city builder in which service walkers roam the roads from their buildings, houses evolve only where food, goods, and services actually reach them, and missions are won on culture, prosperity, peace, and favor ratings.

| field | value |
|---|---|
| year | 1998 |
| developer | Impressions Games |
| platforms | PC |
| subgenre | City builder |
| sim domain | Urban, Economic, Military / conflict |
| player role | Planner / mayor |
| agency model | Zoning / placement, Policy / parameter, Direct unit control |
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
| influence | 4 |
| influenced by | [SimCity](../game/simcity-1989.md) |
| cluster *(computed)* | C02 |
| core count *(computed)* | 3 |
| mechanic count *(computed)* | 17 |

## Summary

A Roman city builder in which service walkers roam the roads from their buildings, houses evolve only where food, goods, and services actually reach them, and missions are won on culture, prosperity, peace, and favor ratings.

## Core Loop

place housing plots and roads -> walkers from service buildings roam the roads and cover the houses they pass -> houses evolve when food, goods, and services reach them -> taxes and trade fund the city -> raise culture, prosperity, peace, and favor ratings to win the mission

## Design Notes

Coverage is delivered by individual walkers whose routes depend on road layout, so the same buildings serve a block well or badly depending on junctions; the developers cited SimCity's static placement as what they wanted to make less static. In the logic preserved by the Julius re-implementation, a walker sets a house's coverage to 96 and coverage decays by 1 per update, while prefects zero fire risk and engineers zero collapse risk. City and empire share one map, and gods that punish neglect have no matching taxonomy mechanic (see run proposal).

## Relations

**influenced by**

- [SimCity](../game/simcity-1989.md)

**uses**

- [Walker service delivery](../mechanic/walker-service-delivery.md) (core): Service walkers leave their building and roam roads; each house passed gets coverage set to 96, which decays by 1 per update until the next visit.
- [Population strata](../mechanic/population-strata.md) (core): Housing evolves through levels from tents up to villas and palaces when food, goods, services, and desirability are met, and devolves when they lapse.
- [Scenario objectives](../mechanic/scenario-objectives.md) (core): Each assignment sets population and thresholds for four ratings: culture, prosperity, peace, and favor.
- [Goods consumption](../mechanic/goods-consumption.md) (supporting): Higher houses need food plus pottery, furniture, oil, and wine delivered by market walkers.
- [Production chains](../mechanic/production-chain.md) (supporting): Raw materials such as clay, olives, and timber become pottery, oil, and furniture in workshops.
- [Trade routes](../mechanic/trade-routes.md) (supporting): An empire map opens land and sea routes to cities that buy and sell specific goods.
- [Wear and breakdown](../mechanic/wear-breakdown.md) (supporting): Buildings accumulate fire and collapse risk that prefects and engineers reset to zero.
- [Reputation](../mechanic/reputation.md) (supporting): Favor with Caesar rises with timely tribute and gifts and falls when requests are missed.
- [Raid defense](../mechanic/raid-defense.md) (supporting): Military assignments bring invasions; legions, walls, and towers defend the city map.
- [Labor market](../mechanic/labor-market.md) (supporting): Buildings need workers from housing; shortages idle walkers and industry.
- [Decoration and beauty](../mechanic/decoration-beauty.md) (supporting): Gardens, statues, and plazas raise desirability that houses need to evolve.
- [Road networks](../mechanic/road-network.md) (supporting): Walkers and goods move on roads, so road layout sets coverage.
- [Taxation](../mechanic/taxation.md) (supporting)
- [Pause and speed control](../mechanic/variable-speed.md) (supporting)
- [Building placement](../mechanic/free-placement.md) (supporting)
- [Fire spread](../mechanic/fire-spread.md) (supporting)
- [Storage and buffers](../mechanic/storage-capacity.md) (supporting)

## Backlinks (computed)

**influenced:** [Pharaoh](../game/pharaoh.md)

## Sources

- [Caesar III](../source/src-wikipedia-caesar-iii.md)
- [Julius: an open source re-implementation of Caesar III](../source/src-bvschaik-2026-julius.md)

---
Provenance: created in run `2026-10-24-catalog-ga`; reviewed in `2026-10-24-review-fixes`.
