# Travel mode choice

*Mechanic* · `travel-mode-choice` · status: **sourced**

Agents choose among walking, cycling, driving, and transit for each trip by comparing time, money, and comfort costs, which sets how demand splits across networks.

| field | value |
|---|---|
| aliases | mode choice, modal split, mode share |
| family | Logistics & networks |
| substrate | Agent-based, Network / graph |
| math basis | Utility / decision theory, Network flow |
| feedback | Balancing (negative) |
| player interface | Parameter, Placement, Observation only |
| legibility | 2 |
| emergence potential | 3 |
| authoring cost | 1 |
| compute cost | 3 |
| tuning difficulty | 3 |
| ai leverage | 3 |
| maturity | Established |
| core count *(computed)* | 0 |
| earliest game *(computed)* | [Cities: Skylines](../game/cities-skylines.md) |
| earliest year *(computed)* | 2015 |
| prevalence *(computed)* | 2 |
| prevalence share *(computed)* | 0.011 |
| subgenre spread *(computed)* | 1 |
| technique count *(computed)* | 2 |
| technique exposure *(computed)* | 0.287 |

## Summary

Agents choose among walking, cycling, driving, and transit for each trip by comparing time, money, and comfort costs, which sets how demand splits across networks.

## Definition

Owns, per trip or agent, the set of available modes (walk, bicycle, car, taxi, transit), the cost weights used to compare them, and car ownership and parking state. For each trip it computes a generalized cost per mode, such as weighted travel time plus money (fares, fuel, parking fees) plus discomfort (transfers, waiting, crowding, walking distance), and picks the cheapest mode or samples one with logit-style probabilities. Cities: Skylines II combines time, comfort, money, and behavior into its route cost, adds parking fees to driving, and has citizens compare driving, transit, and walking. Outputs are mode shares that load trips onto roads, transit lines, and paths. Unlike public-transit, which owns lines and vehicles, traffic-congestion, which owns per-segment volume, and agent-pathfinding, which searches routes within one network, this mechanic owns the choice between networks.

## Player Experience

The player shapes behavior indirectly. Instead of ordering citizens onto buses, they raise parking fees, add frequency, or shorten walks to stops, then watch mode share shift in the info views. Success shows up as emptier roads; failure as a new metro line nobody rides.

## Design Levers

- weights on time, money, comfort, and transfers, and whether they vary by age, wealth, or household
- car ownership rates and parking supply and pricing
- deterministic cheapest-mode choice versus probabilistic choice that spreads demand
- transfer and waiting penalties for transit
- whether choice is recomputed per trip or fixed per agent

## Failure Modes

- Sticky or opaque choice models keep transit from relieving traffic, so players stop investing in it.
- Deterministic choice flips whole populations between modes after a small change, producing oscillating congestion.
- Cost terms the player cannot see make empty transit lines look like a bug.

## Dynamics

- Congestion raises driving cost and pushes riders to transit, a balancing loop between roads and lines.
- Parking pricing becomes a policy lever that moves demand without building anything.
- Dense mixed-use districts shorten trips enough that walking takes a large share, coupling zoning to traffic.

## Open Questions

- Can discrete-choice models estimated from real travel surveys be simplified enough for players to design against?
- Would letting players inspect a citizen's per-mode cost breakdown make transit planning feel fair rather than random?

## Backlinks (computed)

**affected by:** [LLM models of individual human choice](../technique/human-behavior-simulation-models.md), [Mean field games and mean-field learning](../technique/mean-field-games.md)

**used by:** [Cities: Skylines](../game/cities-skylines.md), [Cities: Skylines II](../game/cities-skylines-2.md)

## Sources

- [Cities: Skylines II Feature Highlight #2: Traffic AI](../source/src-paradox-2023-cs2-traffic-ai.md)

---
Provenance: created in run `2026-10-24-taxonomy-triage-b`.
