# SimCity 4

*Game* · `simcity-4` · status: **sourced**

A city builder in which several cities share a region map and trade utilities, while zones develop by density and wealth level and a commute model routes trips across roads and transit.

| field | value |
|---|---|
| year | 2003 |
| developer | Maxis |
| platforms | PC |
| subgenre | City builder |
| sim domain | Urban, Economic |
| player role | Planner / mayor |
| agency model | Zoning / placement, Policy / parameter |
| time model | Real-time with pause |
| sim scale | City |
| fidelity | Systemic |
| perspective | Isometric |
| win structure | Open sandbox |
| failure model | Soft / recoverable |
| narrative mode | Emergent |
| multiplayer | Single-player |
| modding | Content |
| production tier | AAA |
| agent count order | Aggregate only |
| emergence | 3 |
| influence | 2 |
| influenced by | [SimCity 2000](../game/simcity-2000.md) |
| cluster *(computed)* | C09 |
| core count *(computed)* | 4 |
| mechanic count *(computed)* | 16 |

## Summary

A city builder in which several cities share a region map and trade utilities, while zones develop by density and wealth level and a commute model routes trips across roads and transit.

## Core Loop

terraform in God mode -> zone residential, commercial, industrial land at a density and connect roads -> wealth-level demand and desirability grow buildings -> set taxes and per-building service funding -> trade power, water, and garbage with neighbor cities -> grow the region

## Design Notes

SimCity 4 splits each zone type by wealth level, so demand and desirability are tracked per class and neighborhoods can decay or gentrify as conditions change. Cities of 1 to 4 km per side sit in a region and exchange water, electricity, and garbage disposal through neighbor deals, letting several specialized cities depend on each other; this single-player region has no exact match in the taxonomy (see run proposal). Its commute model drew praise from urban planner Jeff Speck, and the Building Architect Tool (2004) sustained a content community for over two decades.

## Relations

**influenced by**

- [SimCity 2000](../game/simcity-2000.md)

**uses**

- [Zoning](../mechanic/zoning.md) (core): Residential, commercial, and industrial zones at low, medium, and high density, with agriculture as a separate industrial zone; buildings need road frontage.
- [RCI demand](../mechanic/rci-demand.md) (core): Demand is reported separately for each wealth level of residents and for commercial and industrial subtypes.
- [Land value](../mechanic/land-value.md) (core): Desirability is computed separately for each wealth level, so the same lot attracts different classes as services and nuisances change.
- [Traffic congestion](../mechanic/traffic-congestion.md) (core): Commuters route trips over roads, rail, and transit; Rush Hour adds traffic flow tracing, avenues, and elevated rail.
- [Population strata](../mechanic/population-strata.md) (supporting): Buildings belong to wealth levels and size stages; areas decay or gentrify.
- [Public transit lines](../mechanic/public-transit.md) (supporting): Bus, subway, and rail stations carry commuters; Rush Hour adds elevated rail.
- [Treasury and budget](../mechanic/budget-treasury.md) (supporting): Civic buildings need ongoing funding set per building.
- [Taxation](../mechanic/taxation.md) (supporting): Tax rates per zone type and wealth level.
- [Service coverage](../mechanic/service-coverage.md) (supporting): Schools, hospitals, police, and fire buildings cover areas; they lose output and gain maintenance cost as they age.
- [Policy toggles](../mechanic/policy-toggles.md) (supporting): City ordinances with monthly costs and effects.
- [Terraforming](../mechanic/terraforming.md) (supporting): God mode reshapes terrain; most terraforming locks once a city is founded.
- [Random disasters](../mechanic/random-disasters.md) (supporting): God mode triggers disasters on the city.
- [Advisors](../mechanic/advisors.md) (supporting): Mayor mode advisors comment on problems and suggest actions.
- [Pollution spread](../mechanic/pollution-spread.md) (supporting): Industry and traffic pollute and reduce desirability.
- [Pause and speed control](../mechanic/variable-speed.md) (supporting)
- [Building placement](../mechanic/free-placement.md) (supporting)

## Backlinks (computed)

**influenced:** [Cities: Skylines](../game/cities-skylines.md), [SimCity (2013)](../game/simcity-2013.md)

## Sources

- [SimCity 4](../source/src-wikipedia-simcity-4.md)

---
Provenance: created in run `2026-10-24-catalog-ga`; reviewed in `2026-10-24-review-fixes`.
