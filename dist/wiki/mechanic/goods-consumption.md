# Goods consumption

*Mechanic* · `goods-consumption` · status: **sourced**

A population consumes goods at per-capita rates; unmet consumption lowers satisfaction or blocks advancement.

| field | value |
|---|---|
| aliases | population needs, demand for goods, consumption baskets |
| family | Resources & production |
| substrate | Aggregate stocks, Agent-based |
| math basis | System dynamics / ODEs, Optimization |
| feedback | Both |
| player interface | Observation only, Placement |
| legibility | 3 |
| emergence potential | 3 |
| authoring cost | 2 |
| compute cost | 2 |
| tuning difficulty | 3 |
| ai leverage | 2 |
| maturity | Classic |
| core count *(computed)* | 7 |
| earliest game *(computed)* | [Hamurabi](../game/hamurabi.md) |
| earliest year *(computed)* | 1968 |
| prevalence *(computed)* | 16 |
| prevalence share *(computed)* | 0.092 |
| subgenre spread *(computed)* | 6 |
| technique count *(computed)* | 0 |
| technique exposure *(computed)* | 0.0 |

## Definition

Each household, residence, or population tier consumes a basket of goods at fixed per-capita or per-residence rates. Consumption draws from a market, warehouse, or delivered stock; the satisfied fraction of each need feeds population size, satisfaction, tax income, or eligibility to upgrade. Anno 1800 splits needs into basic needs, which raise inhabitants per house, and luxury needs, which raise taxes and happiness, and requires full houses before residents advance a tier. Caesar III houses evolve only when supplied with several food types and goods such as pottery, furniture, oil, and wine, and devolve when supply lapses. Victoria 3 pops buy goods from a market to meet their needs. Inputs: population counts and supplied goods. Outputs: stock drawdown, fulfillment ratios, and growth or downgrade signals.

## Player Experience

The population is a mouth the player must keep feeding at scale. Players compute production ratios, such as producers per hundred residents, and expand supply ahead of demand. Each tier upgrade raises income but adds new goods to the basket, so success creates the next shortage.

## Design Levers

- consumption rate per capita for each good and how it scales with tier
- which needs are mandatory for population or upgrades versus optional bonuses
- substitutability between goods (any of several food types) versus strict requirements
- penalty curve for unmet needs: lost population, lower taxes, unrest, or downgrade
- delivery path from stock to consumer: global pool, market radius, or walker delivery

## Failure Modes

- Fixed rates make ideal ratios solvable once, after which consumption becomes a spreadsheet exercise.
- Downgrade cascades, where one lapsed good devolves a district and collapses its labor supply, feel disproportionate.
- Too many required goods per tier create micromanagement that crowds out spatial decisions.

## Dynamics

- Population growth raises consumption, which requires more production, which requires more workers: the expansion loop of Anno-style builders.
- Tier requirements create layered dependency trees that couple distant islands or regions through trade.
- Shortages propagate to labor because unhappy or downgraded populations work less or leave.

## Open Questions

- Can learned demand models give populations preferences that shift with culture and events instead of fixed baskets?
- What is the smallest basket that still produces interesting supply-chain planning?

## Relations

**synergy**

- [Population strata](../mechanic/population-strata.md): Each tier consumes new goods, so advancement drives production expansion (Anno).

## Backlinks (computed)

**used by:** [Anno 117: Pax Romana](../game/anno-117.md), [Anno 1800](../game/anno-1800.md), [Autonauts](../game/autonauts.md), [Banished](../game/banished.md), [Caesar III](../game/caesar-3.md), [Captain of Industry](../game/captain-of-industry.md), [Farthest Frontier](../game/farthest-frontier.md), [Foundation](../game/foundation.md), [Hamurabi](../game/hamurabi.md), [Manor Lords](../game/manor-lords.md), [M.U.L.E.](../game/mule.md), [Offworld Trading Company](../game/offworld-trading-company.md), [Pharaoh](../game/pharaoh.md), [Stellaris](../game/stellaris.md), [Victoria 3](../game/victoria-3.md), [Workers & Resources: Soviet Republic](../game/workers-and-resources.md)

## Sources

- [Needs](../source/src-anno1800wiki-2026-needs.md)

---
Provenance: created in run `2026-10-24-taxonomy-m1`.
