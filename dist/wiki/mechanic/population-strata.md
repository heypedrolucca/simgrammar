# Population strata

*Mechanic* · `population-strata` · status: **sourced**

The population is divided into classes or tiers with distinct needs, roles, and upgrade paths.

| field | value |
|---|---|
| aliases | population tiers, social classes, citizen tiers |
| family | Population & lineage |
| substrate | Aggregate stocks, Rule system |
| math basis | System dynamics / ODEs, Optimization |
| feedback | Both |
| player interface | Observation only, Placement, Orders |
| legibility | 4 |
| emergence potential | 3 |
| authoring cost | 3 |
| compute cost | 1 |
| tuning difficulty | 3 |
| ai leverage | 2 |
| maturity | Established |
| core count *(computed)* | 8 |
| earliest game *(computed)* | [SimAnt](../game/simant.md) |
| earliest year *(computed)* | 1991 |
| prevalence *(computed)* | 13 |
| prevalence share *(computed)* | 0.075 |
| subgenre spread *(computed)* | 5 |
| technique count *(computed)* | 0 |
| technique exposure *(computed)* | 0.0 |

## Definition

Owns population counts by stratum and the per-stratum tables of needs, consumption rates, labor roles, taxes, and promotion requirements. Each period residences or pops whose stratum's needs are met may advance to the next stratum, and unmet needs can stall, demote, or anger them; production buildings require workers of specific strata. Anno 1800 residences advance from Farmers through Workers, Artisans, and Engineers to Investors (with Jornaleros and Obreros in the New World) when the house is full, basic needs are met, and construction materials exist; luxury needs raise taxes and happiness, and island level follows the highest tier, such as 1,750 Investors for a metropolis. Victoria 3 groups professions into classes and strata whose standard-of-living expectations drive radicalism. Inputs: goods, services, construction materials. Outputs: workforce by tier, tax revenue, demand for higher goods.

## Player Experience

Growth is climbing: each tier unlocks goods and buildings but also new demands, so the player keeps lower tiers staffed while serving the elite. Unmet needs at the top cost revenue, and neglect at the bottom stalls production.

## Design Levers

- number of strata and promotion requirements
- per-stratum needs, consumption rates, and tax yields
- workforce requirements per building by stratum
- demotion or unrest rules when needs fail
- whether promotion is player-triggered or automatic

## Failure Modes

- Upgrading drains lower-tier workers, collapsing basic production; Anno players learn to keep a surplus of each worker type.
- Top-tier demand chains become so long that one missing good stalls the economy.
- Strata as pure progression gates feel like a checklist rather than a society.

## Dynamics

- Each new tier lengthens production chains, so economic complexity grows with population.
- Inequality between tiers creates political pressure when strata link to interest groups or unrest.
- Promotion and demotion cycles oscillate around supply shortfalls.

## Open Questions

- Can strata emerge from agent wealth and occupation dynamics rather than authored tiers, and remain legible?
- How should mobility between strata be modeled so inequality has political consequences without becoming a death spiral?

## Backlinks (computed)

**used by:** [Against the Storm](../game/against-the-storm.md), [Anno 117: Pax Romana](../game/anno-117.md), [Anno 1800](../game/anno-1800.md), [Caesar III](../game/caesar-3.md), [Farthest Frontier](../game/farthest-frontier.md), [Pharaoh](../game/pharaoh.md), [Prison Architect](../game/prison-architect.md), [SimAnt](../game/simant.md), [SimCity (2013)](../game/simcity-2013.md), [SimCity 4](../game/simcity-4.md), [Songs of Syx](../game/songs-of-syx.md), [Stellaris](../game/stellaris.md), [Victoria 3](../game/victoria-3.md)

## Sources

- [Population](../source/src-anno1800wiki-2026-population.md)
- [Needs](../source/src-anno1800wiki-2026-needs.md)
- [Pops](../source/src-paradoxwikis-2026-vic3-pops.md)

---
Provenance: created in run `2026-10-24-taxonomy-m3`.
