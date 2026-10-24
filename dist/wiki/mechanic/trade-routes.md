# Trade routes

*Mechanic* · `trade-routes` · status: **sourced**

Goods are exchanged between settlements, regions, or foreign markets along routes with price differences, tariffs, and transit time.

| field | value |
|---|---|
| aliases | trade lanes, caravans, import and export |
| family | Economy & finance |
| substrate | Network / graph, Aggregate stocks |
| math basis | Network flow, Optimization |
| feedback | Balancing (negative) |
| player interface | Orders, Parameter |
| legibility | 3 |
| emergence potential | 3 |
| authoring cost | 1 |
| compute cost | 2 |
| tuning difficulty | 3 |
| ai leverage | 2 |
| maturity | Classic |
| core count *(computed)* | 4 |
| earliest game *(computed)* | [Elite](../game/elite.md) |
| earliest year *(computed)* | 1984 |
| prevalence *(computed)* | 17 |
| prevalence share *(computed)* | 0.098 |
| subgenre spread *(computed)* | 5 |
| technique count *(computed)* | 0 |
| technique exposure *(computed)* | 0.0 |

## Definition

Owns a set of routes, each linking a source market to a destination market for a good, with a volume level or capacity, a transport cost or transit time, and tariffs. Each period profit per unit = destination price - source price - transport cost - tariffs; volume grows when profitable and shrinks when not, which narrows the price gap. In Victoria 3 (2022) routes start at level 1 and change level weekly mainly by profitability, purchase and sale prices are the midpoints of each market's pre- and post-trade prices, tariffs are charged per unit on the base price, sea routes depend on convoys, and each route has a fixed bureaucracy cost that replaced an earlier cap on route count. Civilization's caravans set up routes whose income depends on distance and the cities involved, and Railroad Tycoon pays for delivering goods to stations that demand them.

## Player Experience

Connecting surplus to scarcity. The player finds where a good is cheap and where it is dear, opens routes, and watches the gap close as the trade succeeds. Tariffs, embargoes, and blockades make trade a lever in diplomacy and a target in war.

## Design Levers

- how volume responds to profit (player-set, automatic growth, or capped by vehicles)
- transport cost model (distance, time, convoys, ships)
- tariffs, trade agreements, embargoes, and their calculation basis
- fixed costs per route versus per-unit costs, which decide whether many small or few large routes win
- how much information about remote prices the player gets

## Failure Modes

- Static price gaps that trade does not close create permanent money loops.
- With no fixed cost per route, many tiny routes become optimal and flood the interface.
- Automated routes that never fail or need attention become set-and-forget income.

## Dynamics

- Arbitrage narrows price gaps, so the most profitable routes erode over time.
- Trade makes markets interdependent, so a war or blockade in one region causes shortages elsewhere.
- Per-unit tariffs on base price hurt high-volume, low-margin routes most, shaping which goods are traded.

## Open Questions

- Can AI merchant agents discover and contest routes on their own, giving players competition for arbitrage instead of a static spreadsheet?
- What route cost structure keeps trade decisions meaningful without micromanagement?

## Backlinks (computed)

**involved in:** [Agent ambassadors between player worlds](../opportunity/agent-ambassadors-async.md)

**used by:** [Against the Storm](../game/against-the-storm.md), [Anno 117: Pax Romana](../game/anno-117.md), [Anno 1800](../game/anno-1800.md), [Banished](../game/banished.md), [Caesar III](../game/caesar-3.md), [Captain of Industry](../game/captain-of-industry.md), [Dwarf Fortress](../game/dwarf-fortress.md), [Elite](../game/elite.md), [Elite Dangerous](../game/elite-dangerous.md), [Europa Universalis IV](../game/europa-universalis-4.md), [Farthest Frontier](../game/farthest-frontier.md), [Foundation](../game/foundation.md), [Manor Lords](../game/manor-lords.md), [Pharaoh](../game/pharaoh.md), [Songs of Syx](../game/songs-of-syx.md), [Tropico 6](../game/tropico-6.md), [Workers & Resources: Soviet Republic](../game/workers-and-resources.md)

## Sources

- [Victoria 3 Dev Diary #54: Trade Revisions](../source/src-paradox-2022-vic3-trade-revisions.md)
- [Railroad Tycoon (video game)](../source/src-wikipedia-railroad-tycoon.md)

---
Provenance: created in run `2026-10-24-taxonomy-m2`.
