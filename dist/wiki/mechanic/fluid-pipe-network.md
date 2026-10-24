# Fluid pipe networks

*Mechanic* · `fluid-pipe-network` · status: **sourced**

Fluids such as water, oil, sewage, or gas flow through pipes with pressure or throughput limits between producers and consumers.

| field | value |
|---|---|
| aliases | pipes, plumbing, liquid networks |
| family | Logistics & networks |
| substrate | Network / graph, Continuous physics, Aggregate stocks |
| math basis | Network flow, Continuum mechanics |
| feedback | None |
| player interface | Placement, Parameter |
| legibility | 3 |
| emergence potential | 3 |
| authoring cost | 1 |
| compute cost | 3 |
| tuning difficulty | 3 |
| ai leverage | 3 |
| maturity | Established |
| core count *(computed)* | 3 |
| earliest game *(computed)* | [SimCity 2000](../game/simcity-2000.md) |
| earliest year *(computed)* | 1993 |
| prevalence *(computed)* | 12 |
| prevalence share *(computed)* | 0.069 |
| subgenre spread *(computed)* | 5 |
| technique count *(computed)* | 0 |
| technique exposure *(computed)* | 0.0 |

## Definition

Pipes connect producers, consumers, tanks, and pumps into networks that carry one fluid type per segment. The update rule ranges from discrete packets to pooled segments to pressure solvers. Oxygen Not Included moves one packet of up to 10 kg per pipe segment per second, giving 10 kg/s per line, and exchanges heat between the liquid, the pipe, and its tile. Factorio 1.x simulated flow between adjacent pipes, so throughput fell with distance and depended on build order; Factorio 2.0 merges connected pipes into segments where producers push freely, consumers pull at a rate proportional to the fill ratio, and fluid does not propagate. SimCity games treat water and sewage as coverage networks; GlassBox modeled units of water as agents moving through pipes. Inputs: producer output, consumer demand, topology, pumps. Outputs: fluid delivered per consumer and stored per segment or tank.

## Player Experience

Plumbing problems. Players learn that fluids behave differently from items: they mix, back up, and run out at the far end. When the model is predictable, routing is satisfying; when it is not, pipes become a source of mysterious shortages.

## Design Levers

- flow model: packets, pooled segments, or pressure simulation
- throughput limits per pipe and whether distance matters
- fluid mixing rules and penalties
- pumps, valves, and priority controls
- thermal and phase-change behavior in pipes

## Failure Modes

- Distance-dependent throughput with no in-game feedback, as in Factorio 1.x, made long pipelines fail mysteriously; the developers rewrote the system for predictability.
- Accidental fluid mixing can contaminate a network permanently if cleanup is costly.
- Pressure models that are realistic but invisible make players guess.

## Dynamics

- Fluid networks couple to thermal systems, as when hot pipes in Oxygen Not Included cook a base or freeze lines.
- Shared networks create priority conflicts between consumers.
- Tanks act as buffers, changing timing behavior across networks.

## Open Questions

- Could learned fluid surrogates give pipe networks pressure realism at low compute while keeping behavior predictable?
- Which fluid behaviors (pressure, mixing, heat) add decisions rather than confusion?

## Backlinks (computed)

**used by:** [Cities: Skylines](../game/cities-skylines.md), [Factorio](../game/factorio.md), [Mindustry](../game/mindustry.md), [Oxygen Not Included](../game/oxygen-not-included.md), [Prison Architect](../game/prison-architect.md), [Satisfactory](../game/satisfactory.md), [shapez 2](../game/shapez-2.md), [SimCity 2000](../game/simcity-2000.md), [SimCity (2013)](../game/simcity-2013.md), [Stationeers](../game/stationeers.md), [Surviving Mars](../game/surviving-mars.md), [Workers & Resources: Soviet Republic](../game/workers-and-resources.md)

## Sources

- [Friday Facts #416 - Fluids 2.0](../source/src-wube-2024-fff-416-fluids.md)
- [Liquid Pipe](../source/src-oniwiki-2026-liquid-pipe.md)

---
Provenance: created in run `2026-10-24-taxonomy-m1`.
