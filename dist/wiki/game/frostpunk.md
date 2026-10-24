# Frostpunk

*Game* · `frostpunk` · status: **sourced**

A survival city builder in which the leader of the last city around a coal generator must keep falling temperatures at bay while signing laws that trade citizens' welfare against productivity under hope and discontent meters.

| field | value |
|---|---|
| year | 2018 |
| developer | 11 bit studios |
| platforms | PC, Console, Mobile |
| subgenre | City builder |
| subgenre secondary | Survival sim |
| sim domain | Urban, Political / governance, Planetary / natural |
| player role | Ruler / statesman |
| agency model | Zoning / placement, Policy / parameter |
| time model | Real-time with pause |
| sim scale | Settlement |
| fidelity | Stylized |
| perspective | Free 3D camera |
| win structure | Survival duration |
| failure model | Hard restart |
| narrative mode | Hybrid |
| multiplayer | Single-player |
| modding | None |
| production tier | AA |
| agent count order | ~100 |
| emergence | 3 |
| influence | 3 |
| influenced by | [This War of Mine](../game/this-war-of-mine.md) |
| cluster *(computed)* | C04 |
| core count *(computed)* | 4 |
| mechanic count *(computed)* | 14 |

## Summary

A survival city builder in which the leader of the last city around a coal generator must keep falling temperatures at bay while signing laws that trade citizens' welfare against productivity under hope and discontent meters.

## Core Loop

keep the coal generator fueled -> heat districts and insulate buildings as temperatures fall -> assign workers to gather coal, wood, steel, and food -> sign laws that trade welfare for productivity -> balance hope and discontent -> survive the storm

## Design Notes

The city is radial around one generator that heats a circular area, so layout is a function of heat range and fuel, and a coal shortage or overload can end the run. The Book of Laws sequences laws so that early compromises such as child labor or extended shifts open harsher later options, and Order or Faith paths lead toward totalitarian rule, turning policy into moral pressure tracked by hope and discontent. Building heat versus falling outside temperature has no exact taxonomy mechanic (see run proposal); 11 bit studios cites This War of Mine as the origin of its aim for meaningful entertainment, now applied to a whole society.

## Relations

**influenced by**

- [This War of Mine](../game/this-war-of-mine.md)

**uses**

- [Policy toggles](../mechanic/policy-toggles.md) (core): The Book of Laws offers adaptation laws such as child labor, extended shifts, and prosthetics, plus Order or Faith paths whose later laws are harsher.
- [Citizen satisfaction](../mechanic/citizen-satisfaction.md) (core): Hope and Discontent meters respond to laws, events, and conditions; hope too low or discontent too high for too long ends the game in revolt.
- [Crisis countdown](../mechanic/crisis-countdown.md) (core): Temperature falls on a schedule toward the Great Storm, which the main scenario must be survived through.
- [Service coverage](../mechanic/service-coverage.md) (core): The generator heats a circular area whose range and level the player raises; buildings outside heat need insulation or heaters.
- [Resource extraction](../mechanic/resource-extraction.md) (supporting): Coal, wood, steel, and food come from thumpers, sawmills, mines, and hunters.
- [Labor market](../mechanic/labor-market.md) (supporting): Workers, engineers, and children fill different job types.
- [Daily schedules](../mechanic/daily-schedules.md) (supporting): Citizens work daylight shifts; emergency shifts extend hours at a cost.
- [Fog of war](../mechanic/fog-of-war.md) (supporting): Scouts explore the frozen wasteland map for survivors and resources, the only way to grow the workforce.
- [Dilemma cards](../mechanic/dilemma-cards.md) (supporting): Individual decisions, such as how to handle an injured child, offer choices that shift hope and discontent.
- [Tech tree](../mechanic/tech-tree.md) (supporting): Workshops research heat, extraction, and automaton technologies.
- [Weather](../mechanic/weather.md) (supporting)
- [Pause and speed control](../mechanic/variable-speed.md) (supporting)
- [Building placement](../mechanic/free-placement.md) (supporting)
- [Storage and buffers](../mechanic/storage-capacity.md) (supporting)

## Backlinks (computed)

**influenced:** [Frostpunk 2](../game/frostpunk-2.md)

**precedent for:** [Branch preview of policy futures](../opportunity/branch-preview-forecasts.md), [Content-elastic event systems](../opportunity/content-elastic-events.md), [Drama-aware storyteller](../opportunity/drama-aware-storyteller.md), [Placement that tells stories](../opportunity/placement-that-tells-stories.md)

## Sources

- [Frostpunk](../source/src-wikipedia-frostpunk.md)

---
Provenance: created in run `2026-10-24-catalog-ga`; reviewed in `2026-10-24-review-fixes`.
