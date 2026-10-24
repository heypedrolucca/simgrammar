# Product development

*Mechanic* · `product-development` · status: **asserted**

The player configures a product's features, and a simulated market scores it against trends, quality, and competition.

| field | value |
|---|---|
| aliases | product design, R&D design sliders |
| family | Economy & finance |
| substrate | Rule system, Aggregate stocks |
| math basis | Optimization, Combinatorics, Utility / decision theory |
| feedback | Both |
| player interface | Parameter, Choice / cards |
| legibility | 2 |
| emergence potential | 2 |
| authoring cost | 2 |
| compute cost | 1 |
| tuning difficulty | 3 |
| ai leverage | 4 |
| maturity | Established |
| core count *(computed)* | 3 |
| earliest game *(computed)* | [Game Dev Tycoon](../game/game-dev-tycoon.md) |
| earliest year *(computed)* | 2012 |
| prevalence *(computed)* | 3 |
| prevalence share *(computed)* | 0.017 |
| subgenre spread *(computed)* | 2 |
| technique count *(computed)* | 0 |
| technique exposure *(computed)* | 0.0 |

## Definition

Owns a product in progress: chosen attributes (topic, genre, features, components), an allocation of effort across development areas, quality points accumulated from staff skill and time, and a cost. On release a market evaluator scores the product against hidden or partly revealed ideals (good attribute combinations, the right effort balance), against current trends, and against rivals or the player's own past work, then turns the score into reviews and a sales curve. Game Dev Tycoon (2012) is the canonical form: topic and genre pairs and per-stage effort sliders are rated for fit, and review scores depend on beating the player's earlier releases. Big Pharma (2015) has players build machine lines that refine ingredients and combine their effects into drugs, and Capitalism raises product quality through research projects.

## Player Experience

Iterating on recipes for success. The player picks combinations, adjusts sliders, ships, reads reviews, and infers the hidden scoring rules over many releases. Each product is a hypothesis about what the market wants.

## Design Levers

- size of the attribute space and how many combinations score well
- how much of the scoring rule is revealed through reports or reviews
- rising quality bar (relative to past work or rivals) versus fixed standards
- trend volatility, so last year's best combination fades
- how staff skill, time, and money convert into quality points

## Failure Modes

- Once players look up the best combinations on a wiki, the mechanic collapses into executing a table.
- Scoring relative to the player's own best punishes experimentation, since a novel but weaker product reviews badly.
- Opaque evaluators make poor reviews feel random when the cause is hidden.

## Dynamics

- Players converge on a few proven formulas until trends or a rising bar force variation.
- Revenue from hits funds better staff and technology, which raises quality and the bar together.
- Rival releases in the same category split sales, encouraging release timing.

## Open Questions

- Could generative models let players make an actual product artifact (a game concept, a recipe, a design) that a learned critic scores, replacing slider allocations?
- Can a learned market evaluator stay consistent enough that players can still learn its preferences?

## Backlinks (computed)

**involved in:** [Human-calibrated customers](../opportunity/human-calibrated-customers.md)

**used by:** [Big Pharma](../game/big-pharma.md), [Game Dev Tycoon](../game/game-dev-tycoon.md), [Schedule I](../game/schedule-i.md)

---
Provenance: created in run `2026-10-24-taxonomy-m2`.
