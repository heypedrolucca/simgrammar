# Supply lines

*Mechanic* · `supply-lines` · status: **sourced**

Remote units or outposts need a continuous connection to a supply source; cutting the connection causes attrition.

| field | value |
|---|---|
| aliases | logistics, supply, encirclement |
| family | Logistics & networks |
| substrate | Network / graph |
| math basis | Graph search, Network flow |
| feedback | Both |
| player interface | Orders, Placement, Observation only |
| legibility | 3 |
| emergence potential | 3 |
| authoring cost | 1 |
| compute cost | 2 |
| tuning difficulty | 3 |
| ai leverage | 2 |
| maturity | Established |
| open questions | Could an AI opponent that reasons about supply networks produce more convincing operational play than current scripted AIs? |
| core count *(computed)* | 1 |
| earliest game *(computed)* | [Hearts of Iron IV](../game/hearts-of-iron-4.md) |
| earliest year *(computed)* | 2016 |
| prevalence *(computed)* | 2 |
| prevalence share *(computed)* | 0.011 |
| subgenre spread *(computed)* | 2 |
| technique count *(computed)* | 0 |
| technique exposure *(computed)* | 0.0 |

## Definition

Units or outposts draw supply from sources (hubs, depots, capitals, ports) through a connected path of controlled territory, rail, roads, or sea lanes. Each tick, supply delivered falls off with distance and is capped by the weakest link; units below a supply threshold lose strength, organization, or health. Hearts of Iron IV routes supply from the capital by railway to supply hubs, with hub capacity from 15 to 35 by railway level and capped by the weakest link; supply falls off per province from the hub, and attrition starts at 35% supply or less. Unity of Command makes supply range central to its operational puzzle, and Company of Heroes yields resources only from territory connected to the player's base. Inputs: source capacity, network connectivity, distance. Outputs: per-unit supply level and attrition.

## Player Experience

Strategy at the level of the map. Players plan advances along supply routes, pause to bring up hubs, and seek to cut enemy lines. Encircling an enemy and watching it starve is a strong, systemic win.

## Design Levers

- falloff curve with distance from source
- network carriers: territory, rail, roads, or sea
- attrition thresholds and penalties
- buffers such as stored supply or foraging
- visibility of supply levels and routes

## Failure Modes

- Opaque supply calculations make attrition feel arbitrary.
- Supply too forgiving makes logistics irrelevant.
- Supply too harsh makes offensives impossible and pins the front.

## Dynamics

- Encirclement emerges as the main operational goal.
- Infrastructure investment becomes a military priority.
- Fronts stall when supply limits are hit, producing realistic operational pauses.

## Open Questions

- Could an AI opponent that reasons about supply networks produce more convincing operational play than current scripted AIs?

## Backlinks (computed)

**used by:** [Hearts of Iron IV](../game/hearts-of-iron-4.md), [Songs of Syx](../game/songs-of-syx.md)

## Sources

- [Supply](../source/src-paradoxwikis-2026-hoi4-supply.md)

---
Provenance: created in run `2026-10-24-taxonomy-m1`; reviewed in `2026-10-24-review-fixes`.
