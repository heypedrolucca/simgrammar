# Milestone unlocks

*Mechanic* · `milestone-unlocks` · status: **asserted**

Reaching thresholds such as population, output, or score unlocks new buildings, areas, or features.

| field | value |
|---|---|
| aliases | milestones, population tiers, progression thresholds |
| family | Progression & goals |
| substrate | Rule system, Aggregate stocks |
| math basis | System dynamics / ODEs |
| feedback | Reinforcing (positive) |
| player interface | Observation only |
| legibility | 5 |
| emergence potential | 1 |
| authoring cost | 2 |
| compute cost | 1 |
| tuning difficulty | 2 |
| ai leverage | 2 |
| maturity | Established |
| core count *(computed)* | 4 |
| earliest game *(computed)* | [Elite](../game/elite.md) |
| earliest year *(computed)* | 1984 |
| prevalence *(computed)* | 21 |
| prevalence share *(computed)* | 0.121 |
| subgenre spread *(computed)* | 11 |
| technique count *(computed)* | 1 |
| technique exposure *(computed)* | 0.3 |

## Definition

A milestone is a predicate over aggregate state (population at least 1,000, output of an item, cumulative revenue, a tier of residents) paired with a set of unlocks. State owned: the ordered list of milestones and which are reached. Update rule: periodically test the next milestones; on success, permanently unlock their content and notify the player. Unlike research, the player spends nothing directly; progress is a side effect of growth. Canonical forms: Cities: Skylines population milestones that unlock services, zoning types, policies, and map tiles; Anno resident tiers whose population thresholds unlock new buildings. Satisfactory names its HUB unlocks milestones, but they are paid for with item deliveries, which places them closer to a tech tree.

## Player Experience

Growth is rewarded with options. The player expands toward the next threshold, gets a burst of new tools, and learns systems in the order the designer chose rather than all at once.

## Design Levers

- threshold variable: population, output, money, or satisfaction
- spacing of thresholds, linear or geometric
- which content is gated and in what order
- whether milestones can be lost if the variable falls back
- option to disable gating for sandbox play

## Failure Modes

- Gating essential services, such as sewage or healthcare, behind milestones forces players to build broken cities before they can fix them.
- Thresholds hit too quickly flood the player with unexplained tools.
- Thresholds placed far apart produce long stretches of growing without new decisions.

## Dynamics

- Players inflate the gated variable artificially, such as dense cheap housing to reach a population tier, then rebuild.
- Milestone order shapes city or factory layout, since early buildings lock in space before later ones arrive.
- As a tutorial pacing tool it teaches systems in sequence; experienced players disable it.

## Open Questions

- Can milestones be selected adaptively from what the player has not yet engaged with, rather than fixed by the designer?
- Does gating by behavior (built a working transit line) teach better than gating by aggregate size?

## Backlinks (computed)

**affected by:** [Agent-based automated playtesting and balancing](../technique/automated-playtesting.md)

**involved in:** [Generated recipe graphs](../opportunity/generated-recipe-graphs.md), [Quality-diversity scenario libraries](../opportunity/qd-scenario-libraries.md)

**used by:** [Animal Crossing: New Horizons](../game/animal-crossing-new-horizons.md), [Anno 1800](../game/anno-1800.md), [Cities: Skylines](../game/cities-skylines.md), [Cities: Skylines II](../game/cities-skylines-2.md), [Elite](../game/elite.md), [Equilinox](../game/equilinox.md), [Foundation](../game/foundation.md), [Game Dev Tycoon](../game/game-dev-tycoon.md), [Islanders](../game/islanders.md), [Jurassic World Evolution](../game/jurassic-world-evolution.md), [Nintendogs](../game/nintendogs.md), [PC Building Simulator](../game/pc-building-simulator.md), [Reigns](../game/reigns.md), [Schedule I](../game/schedule-i.md), [SimTower](../game/simtower.md), [SnowRunner](../game/snowrunner.md), [Spore](../game/spore.md), [Tomodachi Life](../game/tomodachi-life.md), [Two Point Hospital](../game/two-point-hospital.md), [Valheim](../game/valheim.md), [Viva Piñata](../game/viva-pinata.md)

---
Provenance: created in run `2026-10-24-taxonomy-m6`.
