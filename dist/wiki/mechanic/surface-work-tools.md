# Surface work tools

*Mechanic* · `surface-work-tools` · status: **sourced**

The player applies a tool to surfaces to clean, paint, or strip them, and a per-surface coverage state shows visible progress toward completion.

| field | value |
|---|---|
| aliases | cleaning sim, painting tools, coverage tools |
| family | Operation & procedure |
| substrate | Cellular grid, Continuous physics |
| math basis | Optimization |
| feedback | None |
| player interface | Embodied skill, Direct manipulation |
| legibility | 5 |
| emergence potential | 1 |
| authoring cost | 3 |
| compute cost | 2 |
| tuning difficulty | 2 |
| ai leverage | 2 |
| maturity | Emerging |
| core count *(computed)* | 3 |
| earliest game *(computed)* | [House Flipper](../game/house-flipper.md) |
| earliest year *(computed)* | 2018 |
| prevalence *(computed)* | 3 |
| prevalence share *(computed)* | 0.017 |
| subgenre spread *(computed)* | 1 |
| technique count *(computed)* | 0 |
| technique exposure *(computed)* | 0.0 |

## Definition

Each surface carries a coverage mask (a texture or vertex grid) storing remaining dirt, paint, or material per cell, sometimes in several layers with different hardness. The tool casts a footprint with radius, falloff, and strength, and each frame it reduces or adds coverage under the footprint, scaled by distance, angle, and tool type versus layer type. Objects report the percentage done and count as complete past a threshold. PowerWash Simulator has four nozzles with different power and spray width, dirt types (dirt, grime, lichen, moss, rust), surface-specific soaps, progress bars per object and level, and a highlight for remaining dirt. House Flipper uses the same pattern for cleaning and painting walls; Hardspace: Shipbreaker's laser cutter is a cutting variant in which cutting electrical wires or coolant pipes can cause an explosion. Inputs: tool parameters and aim. Outputs: coverage state and completion events tied to payment.

## Player Experience

Calm, absorbing, visibly productive work. Players sweep a tool across grime and watch clean surface appear, chase the last stubborn patches, and feel satisfied when an object pings complete. The appeal is relaxation and order, not challenge.

## Design Levers

- tool footprint size, strength, and falloff
- layer types and which tools or consumables work on them
- completion threshold per object
- remaining-coverage highlighting and other assists
- texture resolution of the coverage mask
- tool upgrades and their price

## Failure Modes

- High completion thresholds turn the last few percent into a hunt for invisible specks; PowerWash Simulator added a highlight for this.
- Weak tools or huge areas make sessions drag.
- Consumables with unclear benefits feel pointless; reviewers criticized PowerWash Simulator's soap system.

## Dynamics

- Players develop efficient sweep patterns, a real coverage-path optimization.
- Tool upgrades change which strategy is efficient, renewing early levels on replay.
- Completion feedback rewards perfectionism, which is the core motivation loop.

## Open Questions

- Can generative texture models produce varied dirt and wear layouts on arbitrary scanned objects to cut level-authoring cost?
- Which feedback cues sustain the relaxation loop across long sessions?

## Backlinks (computed)

**used by:** [Hardspace: Shipbreaker](../game/hardspace-shipbreaker.md), [House Flipper](../game/house-flipper.md), [PowerWash Simulator](../game/powerwash-simulator.md)

## Sources

- [PowerWash Simulator](../source/src-wikipedia-powerwash-simulator.md)
- [Hardspace: Shipbreaker](../source/src-wikipedia-hardspace-shipbreaker.md)

---
Provenance: created in run `2026-10-24-taxonomy-m7`.
