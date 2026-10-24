# Military operations

*Mechanic* · `military-operations` · status: **sourced**

Units with modeled sensors, weapons, platforms, and doctrine conduct operations at operational fidelity, mostly under player orders and automated behavior.

| field | value |
|---|---|
| aliases | operational wargaming, sensor and weapons simulation |
| family | Conflict & defense |
| substrate | Agent-based, Continuous physics, Stochastic events |
| math basis | Probability / statistics, Classical mechanics, Information theory |
| feedback | Both |
| player interface | Orders, Parameter |
| legibility | 2 |
| emergence potential | 4 |
| authoring cost | 4 |
| compute cost | 3 |
| tuning difficulty | 4 |
| ai leverage | 3 |
| maturity | Established |
| core count *(computed)* | 4 |
| earliest game *(computed)* | [Silent Hunter III](../game/silent-hunter-3.md) |
| earliest year *(computed)* | 2005 |
| prevalence *(computed)* | 4 |
| prevalence share *(computed)* | 0.023 |
| subgenre spread *(computed)* | 3 |
| technique count *(computed)* | 3 |
| technique exposure *(computed)* | 0.938 |

## Definition

Each unit is an agent with a platform record (speed, endurance, signatures), sensors with detection models against target signatures, weapons with ranges and hit or kill probabilities, and a doctrine or rules-of-engagement profile that governs when it fires and emits. The simulation advances in continuous or stepped time with acceleration; contacts are detected, classified, and engaged under that doctrine, often without per-shot player input. Command: Modern Operations, from Warfare Sims, gives operational control of units on a map of Earth through missions or direct orders, runs scenarios lasting hours to days with time acceleration, and draws platforms and weapons from databases such as DB3000; a Professional Edition adds database editing and Monte Carlo analysis for defense customers. Harpoon is the lineage ancestor. Inputs: orders, missions, doctrine settings. Outputs: detections, engagements, losses, and mission outcomes.

## Player Experience

The player is a commander, not a pilot. They plan patrols, set emission and engagement rules, manage fuel and munitions, and watch detections develop, so most decisions concern information and timing. Success comes from planning; failure arrives as a missile on the screen that should have been detected earlier.

## Design Levers

- fidelity of sensor and signature models
- kill probabilities and countermeasure effects
- doctrine, rules-of-engagement, and emission-control settings available to the player
- database breadth and accuracy
- time acceleration and command granularity (mission versus direct orders)

## Failure Modes

- High fidelity buries the player in parameters, and new players cannot tell why an engagement failed.
- Database errors or outdated data undermine credibility with expert players.
- Automated unit behavior that ignores doctrine settings reads as the simulation disobeying orders.

## Dynamics

- Emission control creates cat-and-mouse play, because radiating sensors reveal the radiating unit.
- Munitions and fuel limits turn engagements into logistics problems over long scenarios.
- Monte Carlo repetition shows outcome distributions, so planning targets probabilities rather than certainties.

## Open Questions

- Can reinforcement-learning opponents trained in operational simulators provide credible adversaries without scripted behavior?
- Can language interfaces let players issue operational orders at the level of commander's intent?

## Relations

**synergy**

- [Supply lines](../mechanic/supply-lines.md): Operations stall when supply is cut.

## Backlinks (computed)

**affected by:** [Regret minimization and search for imperfect-information games](../technique/imperfect-information-solvers.md), [Self-play planning with learned models (AlphaZero, MuZero, Dreamer)](../technique/model-based-planning-muzero.md), [Monte Carlo tree search for game AI](../technique/monte-carlo-tree-search.md)

**used by:** [Arma 3](../game/arma-3.md), [Command: Modern Operations](../game/command-modern-operations.md), [DCS World](../game/dcs-world.md), [Silent Hunter III](../game/silent-hunter-3.md)

## Sources

- [Command: Modern Operations](../source/src-wikipedia-command-modern-operations.md)

---
Provenance: created in run `2026-10-24-taxonomy-m7`.
