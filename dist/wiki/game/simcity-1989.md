# SimCity

*Game* · `simcity-1989` · status: **sourced**

The city builder in which a mayor zones residential, commercial, and industrial land, lays power and roads, and sets taxes while grid maps of land value, crime, pollution, and traffic drive where the city grows.

| field | value |
|---|---|
| aliases | SimCity Classic, Micropolis |
| year | 1989 |
| developer | Maxis |
| platforms | PC, Console, Mobile |
| subgenre | City builder |
| sim domain | Urban, Economic |
| player role | Planner / mayor |
| agency model | Zoning / placement, Policy / parameter |
| time model | Real-time with pause |
| sim scale | City |
| fidelity | Systemic |
| perspective | Top-down / side 2D |
| win structure | Open sandbox |
| failure model | Soft / recoverable |
| narrative mode | Emergent |
| multiplayer | Single-player |
| modding | Content |
| production tier | Indie |
| agent count order | Aggregate only |
| emergence | 3 |
| influence | 5 |
| cluster *(computed)* | C09 |
| core count *(computed)* | 5 |
| mechanic count *(computed)* | 17 |

## Summary

The city builder in which a mayor zones residential, commercial, and industrial land, lays power and roads, and sets taxes while grid maps of land value, crime, pollution, and traffic drive where the city grows.

## Core Loop

zone residential, commercial, and industrial land -> connect roads and power -> RCI demand and land value grow zones -> collect taxes each year -> fund police, fire, and roads -> respond to crime, pollution, traffic, and disasters

## Design Notes

Will Wright grew the game out of the map editor he built for Raid on Bungeling Bay and drew its model from Jay Forrester's Urban Dynamics. The simulation is a set of coarse grid maps (land value, crime, pollution, traffic density, police and fire effect) recomputed in passes, plus three RCI demand valves that integrate city-wide balance; a zone grows when its local score plus the valve passes a random test. The 2008 GPL release as Micropolis made these update rules, including crime = 128 - land value + density - police effect, inspectable.

## Relations

**uses**

- [Zoning](../mechanic/zoning.md) (core): The player paints 3x3 residential, commercial, and industrial zones; simulated developers build, densify, or abandon them.
- [RCI demand](../mechanic/rci-demand.md) (core): Three valves move by the ratio of projected to actual residents, commerce, and industry plus a tax offset, clamped to +/-2000 or +/-1500 (Micropolis source).
- [Land value](../mechanic/land-value.md) (core): Each 2x2 block's value falls with distance from the population-weighted center, rises near trees and water, and drops with pollution and high crime, clamped to 1-250.
- [Power grid](../mechanic/power-grid.md) (core): Zones must connect to coal or nuclear plants through power lines or adjacent zones; unpowered zones do not grow and lower the city score.
- [Treasury and budget](../mechanic/budget-treasury.md) (core): Tax revenue is collected periodically from population, land value, and tax rate; police, fire, and road funding fractions scale their effects, and underfunded roads decay.
- [Taxation](../mechanic/taxation.md) (supporting): One city-wide tax rate adds a positive offset to demand at low rates and a negative offset at high rates.
- [Service coverage](../mechanic/service-coverage.md) (supporting): Police and fire stations write funding-scaled effect values to a block map that is smoothed outward.
- [Crime and policing](../mechanic/crime-policing.md) (supporting): Crime per cell is 128 - land value + density minus smoothed police effect, clamped 0-250.
- [Pollution spread](../mechanic/pollution-spread.md) (supporting): Industry and traffic write a pollution map that depresses land value and can summon the monster.
- [Traffic congestion](../mechanic/traffic-congestion.md) (supporting): Zones generate trips along roads; the resulting traffic density map adds to pollution and complaints.
- [Data overlays](../mechanic/data-overlays.md) (supporting): Map windows show land value, crime, pollution, traffic density, police and fire coverage, and population density.
- [Random disasters](../mechanic/random-disasters.md) (supporting): Fire, flood, tornado, earthquake, and a pollution-gated monster fire at 1/481, 1/241, or 1/61 per cycle by difficulty.
- [Scenario objectives](../mechanic/scenario-objectives.md) (supporting): Time-limited scenarios such as Detroit 1972 set a goal to reach before the clock ends, added at Broderbund's suggestion.
- [Citizen satisfaction](../mechanic/citizen-satisfaction.md) (supporting): A yearly evaluation turns problem scores into a 0-1000 rating and an approval poll.
- [Pause and speed control](../mechanic/variable-speed.md) (supporting)
- [Building placement](../mechanic/free-placement.md) (supporting)
- [Fire spread](../mechanic/fire-spread.md) (supporting)

## Backlinks (computed)

**influenced:** [Caesar III](../game/caesar-3.md), [Sid Meier's Civilization](../game/civilization.md), [Railroad Tycoon](../game/railroad-tycoon.md), [SimCity 2000](../game/simcity-2000.md)

**precedent for:** [Participatory planning sandboxes](../opportunity/participatory-planning-sandboxes.md)

## Sources

- [SimCity (1989 video game)](../source/src-wikipedia-simcity-1989.md)
- [Micropolis: open-source SimCity source code](../source/src-hopkins-2008-micropolis.md)

---
Provenance: created in run `2026-10-24-catalog-ga`; reviewed in `2026-10-24-review-fixes`.
