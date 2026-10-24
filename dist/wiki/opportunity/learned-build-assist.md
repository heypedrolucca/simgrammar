# Learned build assist for cities

*Opportunity* · `learned-build-assist` · status: **asserted**

Extend Townscaper-style procedural assist to full city builders with learned style priors, so rough strokes become plausible districts the simulation then evaluates.

| field | value |
|---|---|
| opportunity type | Mechanic upgrade |
| involves | [Procedural build assist](../mechanic/procedural-build-assist.md), [Zoning](../mechanic/zoning.md), [Building placement](../mechanic/free-placement.md), [Adjacency scoring](../mechanic/adjacency-scoring.md), [Land value](../mechanic/land-value.md) |
| applies | [Wave Function Collapse and constraint-based tile generation](../technique/wave-function-collapse.md), [Learned level and map generation (PCGRL, MarioGPT, LLM generators)](../technique/learned-level-generation.md), [Quality-diversity search (MAP-Elites) for content and balance](../technique/quality-diversity-search.md) |
| precedent | [Townscaper](../game/townscaper.md), [Tiny Glade](../game/tiny-glade.md), [Manor Lords](../game/manor-lords.md), [Cities: Skylines II](../game/cities-skylines-2.md) |
| novelty | 3 |
| feasibility | 4 |
| impact | 3 |
| horizon | Now |
| key risks | Assist removes the planning players enjoy., Learned priors import real-world layout biases., Unclear ownership of generated layouts. |
| falsifiable signal | {'prediction': 'A city builder will ship a machine-learned layout generator that turns player strokes into detailed streets or districts.', 'resolve_by': '2028-06-30', 'criteria': 'Feature first shipped after 2026-10-24 in a title with at least 1,000 Steam user reviews; developer documentation states that a model trained on layout data, as opposed to hand-written procedural rules, generates the layout from player brushes or strokes.'} |
| priority *(computed)* | 3.318 |

## Summary

Extend Townscaper-style procedural assist to full city builders with learned style priors, so rough strokes become plausible districts the simulation then evaluates.

## Thesis

Townscaper, Tiny Glade, and Manor Lords showed that assisted building (the game completes detail around the player's gesture) is joyful. Constraint solving such as wave function collapse covers local consistency; learned layout generators add district-level plausibility. Feeding the result back into the simulation makes assist a gameplay tool rather than only an aesthetic one.

## Design Sketch

The player paints a rough block outline and selects intent (dense market street, quiet residential). The assist proposes building footprints and lanes using a learned prior constrained by WFC rules; the simulation scores walkability, land value, and traffic, and the player accepts or tweaks.

## Key Risks

- Assist removes the planning players enjoy.
- Learned priors import real-world layout biases.
- Unclear ownership of generated layouts.

## Validation Experiment

Train a layout generator on open street-network data and compare player-built districts with and without assist on build time and simulated performance. Success: 50 percent less build time at equal or better simulated metrics, with players preferring assist.

## Falsifiable signal

- **Prediction:** A city builder will ship a machine-learned layout generator that turns player strokes into detailed streets or districts.
- **Resolve by:** 2028-06-30
- **Criteria:** Feature first shipped after 2026-10-24 in a title with at least 1,000 Steam user reviews; developer documentation states that a model trained on layout data, as opposed to hand-written procedural rules, generates the layout from player brushes or strokes.

## Relations

**applies**

- [Wave Function Collapse and constraint-based tile generation](../technique/wave-function-collapse.md)
- [Learned level and map generation (PCGRL, MarioGPT, LLM generators)](../technique/learned-level-generation.md)
- [Quality-diversity search (MAP-Elites) for content and balance](../technique/quality-diversity-search.md)

**involves**

- [Procedural build assist](../mechanic/procedural-build-assist.md)
- [Zoning](../mechanic/zoning.md)
- [Building placement](../mechanic/free-placement.md)
- [Adjacency scoring](../mechanic/adjacency-scoring.md)
- [Land value](../mechanic/land-value.md)

**precedent**

- [Townscaper](../game/townscaper.md)
- [Tiny Glade](../game/tiny-glade.md)
- [Manor Lords](../game/manor-lords.md)
- [Cities: Skylines II](../game/cities-skylines-2.md)

---
Provenance: created in run `2026-10-24-synthesis`; reviewed in `2026-10-24-review-fixes`.
