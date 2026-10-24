# Signal circuits

*Mechanic* · `signal-circuits` · status: **sourced**

In-world wires, sensors, and logic elements carry signals that read machine state and control machines.

| field | value |
|---|---|
| aliases | circuit network, logic wiring, combinators, redstone |
| family | Control & automation |
| substrate | Player-authored logic, Network / graph |
| math basis | Computation theory, Control theory |
| feedback | Balancing (negative) |
| player interface | Programming, Placement |
| legibility | 3 |
| emergence potential | 3 |
| authoring cost | 1 |
| compute cost | 2 |
| tuning difficulty | 2 |
| ai leverage | 3 |
| maturity | Established |
| core count *(computed)* | 0 |
| earliest game *(computed)* | [The Incredible Machine](../game/the-incredible-machine.md) |
| earliest year *(computed)* | 1993 |
| prevalence *(computed)* | 12 |
| prevalence share *(computed)* | 0.069 |
| subgenre spread *(computed)* | 7 |
| technique count *(computed)* | 0 |
| technique exposure *(computed)* | 0.0 |

## Definition

The player places wires between entities and logic elements to build control systems inside the world. State owned: the wire graph, signal values on each network, and logic element configuration. Update rule: each tick, sensors and connected entities write signals (item counts, fluid levels, power, conditions) onto their networks; logic elements read input networks and write outputs, often with a one-tick delay; actuators enable or disable themselves or change settings by condition. Canonical form: the Factorio circuit network, where red and green wires carry item-count signals, signals from both wires entering one entity are summed, and arithmetic, decider, and constant combinators operate on them; Factorio 2.0 added a selector combinator and multi-condition deciders. Others: Minecraft redstone, Oxygen Not Included automation wires with sensors and logic gates, Stationeers logic and IC chips, and Mindustry logic processors.

## Player Experience

The player turns a passive factory into one that senses and responds: lamps that show stock, trains that go where they are needed, power that switches on demand. Building memory, timers, or displays from parts feels like engineering, and the most ambitious players build computers inside the game.

## Design Levers

- signal type: binary, integer, or multi-channel item vectors
- logic primitives provided and whether higher-level elements are deliberately withheld
- timing: propagation delay per element and tick order
- which entities can read and write signals
- debugging aids: signal readouts, wire visualization, element descriptions
- physical cost of wires and logic elements

## Failure Modes

- Invisible signal values and per-tick delays make circuits hard to debug without readouts.
- Circuit control is optional in many games, so most players never engage and designers cannot build challenges around it.
- Missing primitives force contraptions for simple tasks, while too many make the logic trivial.

## Dynamics

- Turing-complete primitives lead players to build CPUs, displays, and games inside the game.
- Demand-driven control (produce only when stock falls) dampens the oscillations and gluts of always-on production.
- Shared circuit designs spread as blueprints, coupling this mechanic to community design culture.

## Open Questions

- Can a model synthesize circuit layouts from a behavior spec (keep 2,000 plates buffered) and explain existing circuits to newcomers?
- What minimal primitive set gives the widest range of player designs without making simple tasks contraptions?

## Backlinks (computed)

**used by:** [Besiege](../game/besiege.md), [Factorio](../game/factorio.md), [Garry's Mod](../game/garrys-mod.md), [Minecraft](../game/minecraft.md), [Oxygen Not Included](../game/oxygen-not-included.md), [Poly Bridge](../game/poly-bridge.md), [shapez 2](../game/shapez-2.md), [Space Engineers](../game/space-engineers.md), [Stationeers](../game/stationeers.md), [The Incredible Machine](../game/the-incredible-machine.md), [The Powder Toy](../game/the-powder-toy.md), [Timberborn](../game/timberborn.md)

## Claims

- Factorio introduced arithmetic, decider, and constant combinators on a circuit network where red and green wire signals entering one entity are summed. *(confidence: high)* [[89](../source/src-wube-2015-fff-88-combinators.md)]
- Factorio developers stated a design principle of not adding dedicated logic, bit, or timer combinator types during the 0.13 circuit network work. *(confidence: high)* [[90](../source/src-wube-2016-fff-122-better-circuit-network.md)]
- Factorio 2.0 added a selector combinator and decider combinators with multiple AND/OR conditions, multiple outputs, and per-wire input selection. *(confidence: high)* [[91](../source/src-wube-2023-fff-384-combinators-2.md)]

## Sources

- [Friday Facts #88 - Combinators](../source/src-wube-2015-fff-88-combinators.md)
- [Friday Facts #122 - Better Circuit Network I](../source/src-wube-2016-fff-122-better-circuit-network.md)
- [Friday Facts #384 - Combinators 2.0](../source/src-wube-2023-fff-384-combinators-2.md)

---
Provenance: created in run `2026-10-24-taxonomy-m6`.
