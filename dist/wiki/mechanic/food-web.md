# Food web

*Mechanic* · `food-web` · status: **sourced**

Species eat and are eaten along a feeding graph, so populations rise, crash, and oscillate under predator-prey dynamics.

| field | value |
|---|---|
| aliases | predator-prey, trophic web, ecosystem simulation |
| family | Environment & ecology |
| substrate | Aggregate stocks, Agent-based, Network / graph |
| math basis | Population dynamics, System dynamics / ODEs |
| feedback | Balancing (negative) |
| player interface | Placement, Observation only |
| legibility | 2 |
| emergence potential | 4 |
| authoring cost | 3 |
| compute cost | 2 |
| tuning difficulty | 4 |
| ai leverage | 3 |
| maturity | Established |
| core count *(computed)* | 3 |
| earliest game *(computed)* | [SimLife](../game/simlife.md) |
| earliest year *(computed)* | 1992 |
| prevalence *(computed)* | 4 |
| prevalence share *(computed)* | 0.023 |
| subgenre spread *(computed)* | 3 |
| technique count *(computed)* | 1 |
| technique exposure *(computed)* | 0.1 |

## Definition

Owns population counts per species (aggregate) or individual animals (agent-based) and a directed feeding graph of who eats whom. Each tick prey grow toward a carrying capacity set by plants or habitat, predators remove prey in proportion to encounters, and predators reproduce from food eaten and starve without it. The Lotka-Volterra form, published by Volterra in 1926, has prey growing at rate a and consumed at rate b times predators, and predators converting prey into growth while dying at a constant rate; the result cycles without damping. Games add carrying capacity, starvation, migration, and respawn so species do not drift to extinction. SimLife and Species: Artificial Life, Real Evolution let creatures eat each other on a shared map; Eco simulates plant and animal populations that players can overhunt; Viva Pinata attracts visitors and predators according to garden contents. Inputs are species, habitat, and harvesting; outputs are population trajectories.

## Player Experience

Tending a system the player cannot command. Adding a predator to fix overgrazing can crash the herbivores and then starve the predator a few generations later. The player learns to act through balance and delay, watches population graphs, and feels responsible when a species disappears.

## Design Levers

- feeding graph topology: number of species, diet breadth, and omnivores
- prey growth rate and carrying capacity from plants or habitat
- predation efficiency and conversion of food into offspring
- starvation and natural death rates, and the minimum population before extinction
- immigration or respawn rules that rescue extinct species
- aggregate populations versus individually simulated animals

## Failure Modes

- Undamped predator-prey cycles drift until a population hits zero, so ecosystems collapse without any player error.
- Hidden population floors or respawns added to prevent extinction make overhunting consequence-free.
- Long delays between action and population response hide cause and effect, so players read crashes as random.

## Dynamics

- Trophic cascades: removing a top predator lets herbivores strip vegetation, which lowers carrying capacity for everything.
- Player hunting or harvesting acts as an extra predator and can tip a stable cycle into collapse.
- Coupled with habitat or climate change, species ranges shift and new feeding links form.

## Open Questions

- Can learned behavior models give individually simulated animals plausible foraging and avoidance at ecosystem scale without hand-written AI?
- Which visualizations make delayed predator-prey feedback legible without population graphs?

## Relations

**synergy**

- [Natural selection](../mechanic/natural-selection.md): Predation supplies selective pressure; selection reshapes the food web over generations.
- [Habitat suitability](../mechanic/habitat-suitability.md): Habitat defines which species can co-occur, which sets the possible food webs.

## Backlinks (computed)

**affected by:** [Simulation-based inference for calibrating simulators](../technique/simulation-based-inference.md)

**involved in:** [Open-ended evolution sandbox](../opportunity/open-ended-evolution-sandbox.md)

**used by:** [Eco](../game/eco.md), [Equilinox](../game/equilinox.md), [SimLife](../game/simlife.md), [Viva Piñata](../game/viva-pinata.md)

## Sources

- [Fluctuations in the Abundance of a Species considered Mathematically](../source/src-volterra-1926-fluctuations.md)

---
Provenance: created in run `2026-10-24-taxonomy-m5`.
