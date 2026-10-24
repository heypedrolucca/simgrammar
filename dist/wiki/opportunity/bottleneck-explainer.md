# Bottleneck explainer for production networks

*Opportunity* · `bottleneck-explainer` · status: **asserted**

Explain where and why a production network is starved or blocked by combining sensitivity analysis of the actual simulation with grounded language explanations.

| field | value |
|---|---|
| opportunity type | Legibility layer |
| involves | [Production chains](../mechanic/production-chain.md), [Conveyor transport](../mechanic/conveyor-transport.md), [Storage and buffers](../mechanic/storage-capacity.md), [Stats dashboards](../mechanic/stats-dashboards.md), [Data overlays](../mechanic/data-overlays.md) |
| applies | [Differentiable simulation](../technique/differentiable-simulation.md), [LLM explanation of simulation state](../technique/llm-explanation-of-state.md), [Grammar-constrained decoding for valid game actions](../technique/constrained-decoding.md) |
| precedent | [Factorio](../game/factorio.md), [Satisfactory](../game/satisfactory.md), [Anno 1800](../game/anno-1800.md), [Oxygen Not Included](../game/oxygen-not-included.md) |
| novelty | 3 |
| feasibility | 5 |
| impact | 3 |
| horizon | Now |
| falsifiable signal | {'prediction': "A factory or city-building game will ship a feature that names the binding constraint in the player's production network by testing the simulation, not by displaying static ratios.", 'resolve_by': '2028-06-30', 'criteria': "Feature first shipped after 2026-10-24 in a released title or official mod tool with at least 1,000 Steam user reviews; patch notes or a developer blog state that it perturbs or re-runs the player's network to identify the limiting resource, machine, or link."} |
| priority *(computed)* | 3.587 |

## Thesis

No technique in the dataset is linked to production chains, yet the mechanic's main documented failure is diagnosis: starvation far upstream is hard to see, so players blame the wrong building. Differentiable or finite-difference sensitivity of output to each machine, buffer, and route identifies the binding constraint exactly; a constrained language layer turns that into a short explanation with links to the machines involved. The same tool supports designers checking recipe balance.

## Design Sketch

A bottleneck lens colors every producer by how much one more unit of it would raise the selected output, and a sentence explains the top constraint ('circuits are limited by copper cable, which is starved because the smelter column shares a belt with iron'). Clicking jumps to the machine.

## Key Risks

- Players who enjoy diagnosis lose the puzzle; must be optional or costly.
- Nonlinear buffers make one-step sensitivity misleading.
- Explanations wrong in edge cases erode trust.

## Validation Experiment

Implement sensitivity analysis over a factory prototype's production graph and test whether players fix an injected bottleneck faster with the lens. Success: 50 percent faster fixes with no drop in reported satisfaction among experienced players when the lens is optional.

## Falsifiable signal

- **Prediction:** A factory or city-building game will ship a feature that names the binding constraint in the player's production network by testing the simulation, not by displaying static ratios.
- **Resolve by:** 2028-06-30
- **Criteria:** Feature first shipped after 2026-10-24 in a released title or official mod tool with at least 1,000 Steam user reviews; patch notes or a developer blog state that it perturbs or re-runs the player's network to identify the limiting resource, machine, or link.

## Relations

**applies**

- [Differentiable simulation](../technique/differentiable-simulation.md)
- [LLM explanation of simulation state](../technique/llm-explanation-of-state.md)
- [Grammar-constrained decoding for valid game actions](../technique/constrained-decoding.md)

**involves**

- [Production chains](../mechanic/production-chain.md)
- [Conveyor transport](../mechanic/conveyor-transport.md)
- [Storage and buffers](../mechanic/storage-capacity.md)
- [Stats dashboards](../mechanic/stats-dashboards.md)
- [Data overlays](../mechanic/data-overlays.md)

**precedent**

- [Factorio](../game/factorio.md)
- [Satisfactory](../game/satisfactory.md)
- [Anno 1800](../game/anno-1800.md)
- [Oxygen Not Included](../game/oxygen-not-included.md)

---
Provenance: created in run `2026-10-24-synthesis`; reviewed in `2026-10-24-review-fixes`.
