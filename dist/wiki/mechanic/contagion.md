# Contagion

*Mechanic* · `contagion` · status: **sourced**

Disease spreads between agents or regions via contact rates and moves hosts through compartments such as susceptible, infected, and recovered.

| field | value |
|---|---|
| aliases | disease spread, epidemics, plague |
| family | Environment & ecology |
| substrate | Agent-based, Network / graph, Aggregate stocks |
| math basis | Epidemiology, Markov / stochastic processes, Social network models |
| feedback | Both |
| player interface | Observation only, Parameter, Choice / cards |
| legibility | 3 |
| emergence potential | 4 |
| authoring cost | 2 |
| compute cost | 2 |
| tuning difficulty | 4 |
| ai leverage | 3 |
| maturity | Established |
| core count *(computed)* | 2 |
| earliest game *(computed)* | [Creatures](../game/creatures.md) |
| earliest year *(computed)* | 1996 |
| prevalence *(computed)* | 10 |
| prevalence share *(computed)* | 0.057 |
| subgenre spread *(computed)* | 6 |
| technique count *(computed)* | 2 |
| technique exposure *(computed)* | 0.2 |

## Definition

Each host (agent, building, settlement, or country) carries a disease state from a small compartment set, usually susceptible, infected, recovered or immune, and dead. Each tick infected hosts transmit to susceptible contacts with a probability per contact (agent-based) or at a rate proportional to infected times susceptible (aggregate), and leave infection at a recovery or death rate. Inputs are contact structure (adjacency, shared rooms, trade and travel links), host resistance, and interventions such as quarantine, vaccination, or medicine; outputs are cases, deaths, and lost labor. Kermack and McKendrick showed that an epidemic occurs only above a threshold set by infectivity and recovery rates. Plague Inc. spreads a player-evolved pathogen between countries until a cure completes; Theme Hospital has contagious patients who infect others inside the hospital; World of Warcraft's 2005 Corrupted Blood debuff spread by proximity and escaped its raid through suspended pets and fast travel to cities.

## Player Experience

Watching an invisible quantity become visible too late. Early cases look harmless, then counts climb faster than responses can be built, so the player learns to act on leading indicators: isolating carriers, closing links, stockpiling medicine, or, in Plague Inc., keeping symptoms mild so the disease spreads widely before lethality alerts the world. Most responses trade economic activity against spread.

## Design Levers

- transmission probability per contact or aggregate rate, and which contacts count (adjacency, shared rooms, trade routes, flights)
- infectious period, incubation length, and whether carriers can be asymptomatic
- recovery, death, and immunity rules, including whether recovery confers lasting immunity
- intervention set and costs: quarantine, closing borders or ports, vaccination, treatment
- spatial resolution: per agent, per building, per settlement, or per country
- how much disease state is shown: case counts, overlays, or only visible symptoms

## Failure Modes

- A reproduction number far above any real pathogen makes spread unstoppable and interventions pointless; Lofgren and Fefferman noted Corrupted Blood's exceeded any observed real disease.
- Contact channels the designer did not model, such as Corrupted Blood's suspended pets and fast travel, carry infection past intended boundaries.
- Hidden infection with no leading indicator reads as a random wipeout rather than a failed response.
- Aggregate compartments with no spatial structure give every outbreak the same curve, so the player learns one fixed response.

## Dynamics

- Hubs such as cities, hospitals, and transport nodes become superspreaders, so network topology matters more than total population.
- Sick workers leave jobs, cutting production of the food, medicine, or care that would end the outbreak.
- Agents or players bypass quarantine for convenience, so enforcement becomes its own problem, as in the Corrupted Blood outbreak.
- Depletion of susceptible hosts ends waves on its own, producing boom-and-bust waves that can look like successful policy.

## Open Questions

- Can LLM-driven agents produce plausible behavioral responses to outbreaks (compliance, panic, rumor) that change the effective contact rate in play?
- What is the minimum contact structure that still makes intervention placement a meaningful spatial decision?

## Relations

**synergy**

- [Service coverage](../mechanic/service-coverage.md): Health coverage determines whether outbreaks are contained.

## Backlinks (computed)

**affected by:** [Differentiable simulation](../technique/differentiable-simulation.md), [Simulation-based inference for calibrating simulators](../technique/simulation-based-inference.md)

**involved in:** [Calibrated serious simulations](../opportunity/calibrated-serious-sims.md)

**used by:** [Banished](../game/banished.md), [Creatures](../game/creatures.md), [Farthest Frontier](../game/farthest-frontier.md), [inZOI](../game/inzoi.md), [Jurassic World Evolution](../game/jurassic-world-evolution.md), [Kingdoms and Castles](../game/kingdoms-and-castles.md), [Oxygen Not Included](../game/oxygen-not-included.md), [Plague Inc.](../game/plague-inc.md), [Theme Hospital](../game/theme-hospital.md), [Two Point Hospital](../game/two-point-hospital.md)

## Sources

- [A Contribution to the Mathematical Theory of Epidemics](../source/src-kermack-1927-epidemic-theory.md)
- [The untapped potential of virtual game worlds to shed light on real world epidemics](../source/src-lofgren-2007-corrupted-blood.md)
- [Corrupted Blood incident](../source/src-wikipedia-corrupted-blood-incident.md)
- [Plague Inc.](../source/src-wikipedia-plague-inc.md)

---
Provenance: created in run `2026-10-24-taxonomy-m5`.
