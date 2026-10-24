# Planet Coaster

*Game* · `planet-coaster` · status: **sourced**

A 3D theme park builder with a spline and piece coaster editor, modular scenery, and individually simulated guests and staff, built around sharing creations through the Steam Workshop.

| field | value |
|---|---|
| year | 2016 |
| developer | Frontier Developments |
| platforms | PC, Console |
| subgenre | Management / tycoon |
| sim domain | Economic, Physical / mechanical |
| player role | Manager / owner |
| agency model | Zoning / placement, Design then test, Policy / parameter |
| time model | Real-time with pause |
| sim scale | Facility |
| fidelity | Stylized |
| perspective | Free 3D camera |
| win structure | Open sandbox |
| failure model | Soft / recoverable |
| narrative mode | None |
| multiplayer | Single-player, Async / shared content |
| modding | Content |
| production tier | AA |
| agent count order | ~1,000 |
| emergence | 3 |
| influence | 2 |
| influenced by | [RollerCoaster Tycoon](../game/rollercoaster-tycoon.md) |
| cluster *(computed)* | C01 |
| core count *(computed)* | 4 |
| mechanic count *(computed)* | 17 |

## Summary

A 3D theme park builder with a spline and piece coaster editor, modular scenery, and individually simulated guests and staff, built around sharing creations through the Steam Workshop.

## Core Loop

sculpt terrain and build modular scenery -> design coasters and test their ratings -> guests choose rides, shops, and paths -> manage staff, prices, and finances -> share parks and blueprints on the Workshop

## Design Notes

Planet Coaster keeps the RollerCoaster Tycoon structure of rated rides and guests with preferences and moves the emphasis to construction: a hybrid spline and piece coaster editor, a voxel terrain editor, and modular pieces that snap into custom buildings. The Workshop is part of play, since players import coasters, scenery blueprints, and whole parks made by others. Frontier calls it a spiritual successor to its own RollerCoaster Tycoon 3, and both run on Frontier's Cobra engine. Career, Challenge (limited funds and research), and Sandbox (unlimited funds) modes share one simulation.

## Relations

**influenced by**

- [RollerCoaster Tycoon](../game/rollercoaster-tycoon.md)

**uses**

- [Modular assembly](../mechanic/modular-assembly.md) (core): Coasters are built in a hybrid spline and piece-by-piece editor, and structures are assembled from modular wall, roof, and prop pieces.
- [Design performance rating](../mechanic/design-performance-rating.md) (core): Coasters are test-run and rated on excitement, fear, and nausea, which set guest demand and ride value.
- [Crowd preferences](../mechanic/crowd-preferences.md) (core): Thousands of guests with individual needs, preferences, and budgets choose rides and shops and show thoughts about prices and park conditions.
- [Content sharing](../mechanic/content-sharing.md) (core): Coasters, scenery blueprints, and parks are uploaded to and downloaded from the Steam Workshop or Frontier Workshop.
- [Blueprints](../mechanic/blueprints.md) (supporting): Any selection of pieces can be saved as a blueprint and placed again.
- [Staff hiring and rosters](../mechanic/staff-hiring.md) (supporting): Janitors, mechanics, entertainers, vendors, and security guards are hired and assigned.
- [Customer value choice](../mechanic/customer-value-choice.md) (supporting): Ticket, ride, and shop prices are weighed against ride ratings and guest budgets.
- [Wear and breakdown](../mechanic/wear-breakdown.md) (supporting): Rides age and break down without mechanic inspections.
- [Terraforming](../mechanic/terraforming.md) (supporting): A voxel terrain editor sculpts and tunnels the ground.
- [Tech tree](../mechanic/tech-tree.md) (supporting): Challenge and Career modes gate rides and items behind research.
- [Needs decay](../mechanic/needs-decay.md) (supporting): Guests need food, drink, toilets, and rest during their visit.
- [Scenario objectives](../mechanic/scenario-objectives.md) (supporting): Career scenarios set goals such as building coasters, reaching park ratings, and hiring staff; a scenario editor was added in 2017.
- [Decoration and beauty](../mechanic/decoration-beauty.md) (supporting): Scenery around rides and paths raises guest happiness and ride appeal.
- [Track laying](../mechanic/track-laying.md) (supporting): Coasters are built in a hybrid spline and piece-by-piece editor, joining track elements end to end.
- [Pause and speed control](../mechanic/variable-speed.md) (supporting)
- [Building placement](../mechanic/free-placement.md) (supporting)
- [Utility action selection](../mechanic/utility-action-selection.md) (supporting)

## Backlinks (computed)

**influenced:** [Planet Zoo](../game/planet-zoo.md)

**precedent for:** [Generative decoration catalogs](../opportunity/generative-decoration-catalogs.md), [Human-calibrated customers](../opportunity/human-calibrated-customers.md), [Mean-field crowds and traffic](../opportunity/mean-field-crowds.md)

## Sources

- [Planet Coaster](../source/src-wikipedia-planet-coaster.md)
- [RollerCoaster Tycoon](../source/src-wikipedia-rollercoaster-tycoon-series.md)

---
Provenance: created in run `2026-10-24-catalog-ge`; reviewed in `2026-10-24-review-fixes`.
