# RollerCoaster Tycoon

*Game* · `rollercoaster-tycoon` · status: **sourced**

An amusement park management game in which the player builds rides and custom coasters piece by piece, rated for excitement, intensity, and nausea, to satisfy guests with individual preferences and meet scenario goals.

| field | value |
|---|---|
| year | 1999 |
| developer | Chris Sawyer Productions |
| platforms | PC, Console |
| subgenre | Management / tycoon |
| sim domain | Economic, Physical / mechanical |
| player role | Manager / owner |
| agency model | Zoning / placement, Design then test, Policy / parameter |
| time model | Real-time with pause |
| sim scale | Facility |
| fidelity | Stylized |
| perspective | Isometric |
| win structure | Scenario goals |
| failure model | Hard restart |
| narrative mode | Emergent |
| multiplayer | Single-player |
| modding | Content |
| production tier | Indie |
| agent count order | ~1,000 |
| emergence | 3 |
| influence | 4 |
| influenced by | [Transport Tycoon](../game/transport-tycoon.md) |
| cluster *(computed)* | C03 |
| core count *(computed)* | 5 |
| mechanic count *(computed)* | 17 |

## Summary

An amusement park management game in which the player builds rides and custom coasters piece by piece, rated for excitement, intensity, and nausea, to satisfy guests with individual preferences and meet scenario goals.

## Core Loop

build paths, rides, and shops -> design coasters and test their ratings -> guests choose rides by intensity preference and budget -> thoughts reveal problems -> adjust prices, staff, and layout -> meet the scenario goal

## Design Notes

RollerCoaster Tycoon makes ride design measurable: every built ride is test-run and rated on excitement, intensity, and nausea, and each guest has a preferred intensity and a nausea tolerance, so the ratings decide who will ride and who gets sick afterward. Guests are individual agents with money, needs, and a stream of readable thoughts, which makes park problems inspectable one guest at a time. Rides lose reliability with age and break down unless mechanics inspect them on a player-set interval. Scenario goals (guest counts and park rating by a deadline) chain 21 base parks. OpenRCT2, a reimplementation of RCT2, carries the systems forward, and Planet Coaster and Parkitect are described as spiritual successors.

## Relations

**influenced by**

- [Transport Tycoon](../game/transport-tycoon.md)

**uses**

- [Design performance rating](../mechanic/design-performance-rating.md) (core): Each ride is test-run and rated on excitement, intensity, and nausea from its track geometry, speeds, and g-forces; ratings set demand and fair price.
- [Crowd preferences](../mechanic/crowd-preferences.md) (core): Guests have money, a preferred ride intensity, a nausea tolerance, and needs, and they report thoughts such as a ride being too intense or a price too high.
- [Modular assembly](../mechanic/modular-assembly.md) (core): Coasters are built track piece by piece on a tile grid, choosing direction, height, steepness, and elements such as loops and corkscrews.
- [Customer value choice](../mechanic/customer-value-choice.md) (core): Guests compare ride and shop prices with ride value and their remaining cash; overpriced items show up as complaints in guest thoughts.
- [Wear and breakdown](../mechanic/wear-breakdown.md) (core): Ride reliability decays with use and age; breakdown chance rises as reliability falls, and mechanics inspect and repair on a set interval.
- [Staff hiring and rosters](../mechanic/staff-hiring.md) (supporting): Handymen sweep, empty bins, and mow; mechanics fix rides; security guards prevent vandalism; entertainers cheer guests.
- [Agent inspection](../mechanic/agent-inspection.md) (supporting): Clicking a guest shows cash, needs, thoughts, and ride history.
- [Needs decay](../mechanic/needs-decay.md) (supporting): Guests get hungry, thirsty, tired, and need toilets during a visit.
- [Service queues](../mechanic/service-queues.md) (supporting): Guests wait in ride queues and leave long lines unhappy.
- [Terraforming](../mechanic/terraforming.md) (supporting): Land can be raised and lowered and water added to fit rides and add appeal.
- [Scenario objectives](../mechanic/scenario-objectives.md) (supporting): Each of 21 base scenarios sets a goal such as a guest count with a minimum park rating by a deadline; completing one unlocks the next.
- [Tech tree](../mechanic/tech-tree.md) (supporting): Paid research unlocks new rides and improvements over time.
- [Decoration and beauty](../mechanic/decoration-beauty.md) (supporting): Scenery and trees improve guest views and ride appeal.
- [Loans and debt](../mechanic/loans-debt.md) (supporting): Parks start with a loan, such as $50,000 in Mega Park.
- [Agent pathfinding](../mechanic/agent-pathfinding.md) (supporting): Guests navigate the path network and can get lost in mazes of paths.
- [Advertising and awareness](../mechanic/advertising-awareness.md) (supporting): The marketing panel runs time-limited paid campaigns, such as park or ride advertising and free-entry or half-price vouchers, that raise guest arrivals or demand for a chosen ride or stall while they last.
- [Track laying](../mechanic/track-laying.md) (supporting): Coaster track is built piece by piece on the tile grid by direction, height, steepness, and elements such as loops and corkscrews, and the result is rated by test run.

## Backlinks (computed)

**influenced:** [Planet Coaster](../game/planet-coaster.md)

**precedent for:** [Human-calibrated customers](../opportunity/human-calibrated-customers.md), [Quality-diversity scenario libraries](../opportunity/qd-scenario-libraries.md)

## Sources

- [RollerCoaster Tycoon (video game)](../source/src-wikipedia-rollercoaster-tycoon.md)
- [RollerCoaster Tycoon](../source/src-wikipedia-rollercoaster-tycoon-series.md)

---
Provenance: created in run `2026-10-24-catalog-ge`.
