# Frostpunk 2

*Game* · `frostpunk-2` · status: **sourced**

The sequel to Frostpunk, in which the Steward builds whole districts on the frost and must pass laws through a council of 100 faction delegates while faction tension can escalate into civil war.

| field | value |
|---|---|
| year | 2024 |
| developer | 11 bit studios |
| platforms | PC, Console |
| subgenre | City builder |
| subgenre secondary | Political sim, Survival sim |
| sim domain | Urban, Political / governance, Planetary / natural |
| player role | Ruler / statesman |
| agency model | Zoning / placement, Policy / parameter |
| time model | Real-time with pause |
| sim scale | City |
| fidelity | Stylized |
| perspective | Free 3D camera |
| win structure | Campaign |
| failure model | Hard restart |
| narrative mode | Hybrid |
| multiplayer | Single-player |
| modding | Content |
| production tier | AA |
| agent count order | Aggregate only |
| emergence | 3 |
| influence | 1 |
| influenced by | [Frostpunk](../game/frostpunk.md) |
| cluster *(computed)* | C01 |
| core count *(computed)* | 4 |
| mechanic count *(computed)* | 9 |

## Summary

The sequel to Frostpunk, in which the Steward builds whole districts on the frost and must pass laws through a council of 100 faction delegates while faction tension can escalate into civil war.

## Core Loop

build food, housing, extraction, and industry districts -> heat districts from the generator -> factions propose ideas and laws -> negotiate council votes -> faction tension rises or falls -> survive whiteouts and found colonies

## Design Notes

Frostpunk 2 moves from single buildings to districts and from one leader's decree to a council: 100 delegates, each tied to a faction, vote on every proposed law, with 51 votes for most laws and two thirds for laws that expand the Steward's power. Negotiated promises that are not kept anger factions, and tension between factions can escalate into murder and civil war, so the developer describes social survival as more important than environmental threats. Population is handled as district-level aggregates rather than individual workers.

## Relations

**influenced by**

- [Frostpunk](../game/frostpunk.md)

**uses**

- [Zoning](../mechanic/zoning.md) (core): Districts for food, housing, extraction, and industry are placed on frost; buildings inside add functions.
- [Elections](../mechanic/elections.md) (core): A council of 100 faction delegates votes on each proposed law; 51 votes pass most laws, two thirds pass laws that grant the Steward more power.
- [Interest groups](../mechanic/interest-groups.md) (core): Factions with conflicting ideals react to adopted ideas and laws; radicals grow within factions.
- [Policy toggles](../mechanic/policy-toggles.md) (core): Laws are proposed, negotiated with promises, and enacted when the council approves.
- [Stability and unrest](../mechanic/stability-unrest.md) (supporting): Faction tension can escalate into murder and civil war.
- [Tech tree](../mechanic/tech-tree.md) (supporting): An Idea Tree of faction-proposed ideas to solve problems.
- [Crisis countdown](../mechanic/crisis-countdown.md) (supporting): Whiteouts are severe storms prepared for with fuel reserves.
- [Resource extraction](../mechanic/resource-extraction.md) (supporting): Food, coal, oil, and steam come from frostland deposits and districts.
- [Scenario objectives](../mechanic/scenario-objectives.md) (supporting): Utopia Builder mode sets an objective and optional challenges that fail the run if missed.

## Sources

- [Frostpunk 2](../source/src-wikipedia-frostpunk-2.md)

---
Provenance: created in run `2026-10-24-catalog-ga`.
