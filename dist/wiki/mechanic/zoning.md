# Zoning

*Mechanic* · `zoning` · status: **sourced**

The player paints land-use zones, and the simulation decides whether and what to build, upgrade, or abandon on each zoned lot.

| field | value |
|---|---|
| aliases | land-use zoning, RCI zones, growables |
| family | Space & construction |
| substrate | Cellular grid, Agent-based, Rule system |
| math basis | Cellular automata, System dynamics / ODEs |
| feedback | Reinforcing (positive) |
| player interface | Placement |
| legibility | 3 |
| emergence potential | 4 |
| authoring cost | 3 |
| compute cost | 2 |
| tuning difficulty | 3 |
| ai leverage | 3 |
| maturity | Classic |
| core count *(computed)* | 9 |
| earliest game *(computed)* | [SimCity](../game/simcity-1989.md) |
| earliest year *(computed)* | 1989 |
| prevalence *(computed)* | 9 |
| prevalence share *(computed)* | 0.052 |
| subgenre spread *(computed)* | 1 |
| technique count *(computed)* | 1 |
| technique exposure *(computed)* | 0.375 |

## Definition

The player paints a land-use type, often with density, onto tiles or lots. A zone places nothing by itself. Each update the simulation checks zoned lots and grows, upgrades, downgrades, or abandons buildings based on demand, access, utilities, services, pollution, crime, and nearby uses. In SimCity (1989) players zone residential, commercial, and industrial land, and the Sims choose what to build and upgrade based on traffic, power, crime, and proximity to other buildings, so homes next to a power plant seldom reach the highest grade. Cities: Skylines grows buildings in low- and high-density zones along roads. Games without zoning, such as Anno, have the player place every house directly. State: zone type per tile plus building level per lot.

## Player Experience

Indirect control. Players paint intent and watch a city grow into it, like gardening. The main skill is diagnosing why a zone stalls or decays and fixing the conditions rather than the buildings.

## Design Levers

- zone categories and density tiers
- development rule: growth probability, thresholds, and upgrade conditions
- hard requirements such as road access, power, and water
- lot size and shape rules
- abandonment and decline rules
- whether the player can also place specific buildings directly

## Failure Modes

- Zones fail to develop with no visible reason, forcing players to hunt through overlays and demand meters.
- Cheap zoning paint encourages over-zoning, leaving large empty tracts.
- Uniform growth rules produce monotonous cities with little local character.

## Dynamics

- City form emerges from the interaction of zones, transport, and land value rather than from direct design.
- Nuisance uses push residential away, producing segregated districts and commute traffic.
- Successful zones raise demand and land value, which invites more zoning, a growth loop until services saturate.

## Open Questions

- Can LLM-driven developer agents make zoned growth explain itself and vary by local character?
- Can generated building assets end the repetition of growable buildings across a large city?

## Backlinks (computed)

**affected by:** [Wave Function Collapse and constraint-based tile generation](../technique/wave-function-collapse.md)

**involved in:** [Learned build assist for cities](../opportunity/learned-build-assist.md), [Participatory planning sandboxes](../opportunity/participatory-planning-sandboxes.md), [Symbolic simulation, neural rendering](../opportunity/symbolic-sim-neural-render.md)

**required by:** [RCI demand](../mechanic/rci-demand.md)

**used by:** [Cities: Skylines](../game/cities-skylines.md), [Cities: Skylines II](../game/cities-skylines-2.md), [Foundation](../game/foundation.md), [Frostpunk 2](../game/frostpunk-2.md), [Manor Lords](../game/manor-lords.md), [SimCity](../game/simcity-1989.md), [SimCity 2000](../game/simcity-2000.md), [SimCity (2013)](../game/simcity-2013.md), [SimCity 4](../game/simcity-4.md)

## Sources

- [SimCity (1989 video game)](../source/src-wikipedia-simcity-1989.md)

---
Provenance: created in run `2026-10-24-taxonomy-m4`.
