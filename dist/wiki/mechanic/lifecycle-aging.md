# Lifecycle and aging

*Mechanic* · `lifecycle-aging` · status: **sourced**

Agents are born, age through life stages with different capabilities, and die.

| field | value |
|---|---|
| aliases | life stages, aging, birth and death |
| family | Population & lineage |
| substrate | Agent-based, Aggregate stocks |
| math basis | Population dynamics, Markov / stochastic processes |
| feedback | Balancing (negative) |
| player interface | Observation only, Parameter |
| legibility | 4 |
| emergence potential | 4 |
| authoring cost | 3 |
| compute cost | 1 |
| tuning difficulty | 3 |
| ai leverage | 2 |
| maturity | Classic |
| core count *(computed)* | 5 |
| earliest game *(computed)* | [SimAnt](../game/simant.md) |
| earliest year *(computed)* | 1991 |
| prevalence *(computed)* | 22 |
| prevalence share *(computed)* | 0.126 |
| subgenre spread *(computed)* | 9 |
| technique count *(computed)* | 0 |
| technique exposure *(computed)* | 0.0 |

## Definition

Owns each agent's age (or an age-structured population count) and a table of life stages with durations, capabilities, needs, and mortality. Each tick age advances; crossing a stage boundary changes what the agent can do (work, marry, study), what it needs, and how it looks; mortality rises with age until death. Births add agents through reproduction rules. The Sims 2 has seven stages (baby, toddler, child, teen, young adult with University, adult, elder): babies become toddlers after 3 Sim days, children become teens after 8, teens live 15 days, adults become elders after 29, and elder lifespan depends on the aspiration meter. Victoria 3 aggregates the same idea: natural growth is birth rate minus mortality, both falling as standard of living rises. Inputs: time, health, birth rules. Outputs: workforce and dependents, deaths, succession and inheritance triggers.

## Player Experience

Time becomes personal: the player watches characters grow up and grow old, plans careers and heirs, and grieves. Aging turns a static roster into a pipeline in which the player raises the next generation of workers.

## Design Levers

- number and duration of life stages relative to the game calendar
- capabilities and needs per stage, such as child labor rules or elder frailty
- mortality curve and whether death is fixed-age or probabilistic
- birth rules and fertility windows
- player controls such as aging toggles and lifespan settings

## Failure Modes

- Lifespans short relative to play pace make characters die before players attach, so games add lifespan settings or aging toggles.
- Demographic echoes: one founding cohort ages together and causes a labor collapse or mass death decades later.
- Children are pure cost with nothing to do, so players avoid births.

## Dynamics

- Age structure sets dependency ratios that throttle labor and drive housing and school demand.
- Founding cohorts create waves of births, retirements, and deaths that repeat across generations.
- Deaths trigger inheritance, succession, and grief, coupling lifecycle to social and dynastic systems.

## Open Questions

- Can generative models keep a character recognizable across ages in appearance and personality while allowing growth?
- What ratio of lifespan to play pace maximizes attachment and generational play?

## Relations

**synergy**

- [Trait inheritance](../mechanic/trait-inheritance.md): Generations turn over, carrying inherited traits forward.
- [Romance and family](../mechanic/romance-family.md): Families form and produce the next generation.

## Backlinks (computed)

**involved in:** [Factories with a living workforce](../opportunity/living-workforce-factories.md)

**used by:** [Banished](../game/banished.md), [Cities: Skylines](../game/cities-skylines.md), [Creatures](../game/creatures.md), [Crusader Kings III](../game/crusader-kings-3.md), [Equilinox](../game/equilinox.md), [Football Manager](../game/football-manager.md), [inZOI](../game/inzoi.md), [Out of the Park Baseball](../game/out-of-the-park-baseball.md), [Paralives](../game/paralives.md), [Planet Zoo](../game/planet-zoo.md), [Princess Maker 2](../game/princess-maker-2.md), [Screeps](../game/screeps.md), [Seaman](../game/seaman.md), [SimAnt](../game/simant.md), [SimLife](../game/simlife.md), [Species: Artificial Life, Real Evolution](../game/species-alre.md), [Tamagotchi](../game/tamagotchi.md), [The Sims 2](../game/the-sims-2.md), [The Sims 3](../game/the-sims-3.md), [The Sims 4](../game/the-sims-4.md), [Timberborn](../game/timberborn.md), [Zoo Tycoon](../game/zoo-tycoon.md)

## Sources

- [The Sims 2](../source/src-wikipedia-the-sims-2.md)
- [Pops](../source/src-paradoxwikis-2026-vic3-pops.md)

---
Provenance: created in run `2026-10-24-taxonomy-m3`.
