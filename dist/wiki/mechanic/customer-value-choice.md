# Customer value choice

*Mechanic* · `customer-value-choice` · status: **sourced**

Customers choose among offerings by comparing price to perceived value and personal preference.

| field | value |
|---|---|
| aliases | willingness to pay, price sensitivity, consumer choice |
| family | Economy & finance |
| substrate | Agent-based, Aggregate stocks |
| math basis | Utility / decision theory, Probability / statistics |
| feedback | Balancing (negative) |
| player interface | Parameter, Observation only |
| legibility | 3 |
| emergence potential | 3 |
| authoring cost | 2 |
| compute cost | 2 |
| tuning difficulty | 3 |
| ai leverage | 3 |
| maturity | Classic |
| core count *(computed)* | 7 |
| earliest game *(computed)* | [Lemonade Stand](../game/lemonade-stand.md) |
| earliest year *(computed)* | 1973 |
| prevalence *(computed)* | 8 |
| prevalence share *(computed)* | 0.046 |
| subgenre spread *(computed)* | 3 |
| technique count *(computed)* | 1 |
| technique exposure *(computed)* | 0.25 |

## Definition

Owns each customer's (or segment's) preference weights and budget, and each offering's price and value attributes. When a customer wants a good or service, the rule scores every reachable offering, typically utility = perceived value x preference match - price - distance or wait, then buys the best one, samples in proportion to scores, or buys nothing when every price exceeds willingness to pay. Lemonade Stand (1973) reduces it to three daily inputs (glasses made, advertising signs, price per glass) whose sales vary with the weather report. RollerCoaster Tycoon guests refuse rides and stalls they judge too expensive for what they offer and say so in their thoughts. Capitalism weighs price, quality, and brand by product category to split demand among competing stores.

## Player Experience

Finding the price people will bear. The player probes prices, watches thoughts or sales drop when they overreach, and invests in quality or marketing to justify charging more. Small numbers become visible crowds walking past or lining up.

## Design Levers

- shape of the utility function and which attributes (quality, brand, novelty, distance, wait) enter it
- price sensitivity per customer segment, income class, or trait
- heterogeneity: one representative customer versus sampled individual preferences
- deterministic best choice versus probabilistic (logit) choice
- whether customers explain rejections through thoughts, reviews, or complaints

## Failure Modes

- A single representative customer yields one optimal price that players find once and never revisit.
- Hidden value thresholds read as random rejection unless thoughts or reviews explain them.
- Weak price sensitivity lets players charge extreme prices with little loss, so gouging dominates.

## Dynamics

- Competing sellers undercut each other until quality or brand differentiation ends the price war.
- Choices propagate congestion: the best-value stall attracts queues that lower its effective value.
- Segmented preferences reward a portfolio of offerings over one best product.

## Open Questions

- Can LLM-driven customers with stated tastes and budgets haggle or complain in language while staying consistent with a calibrated demand curve?
- How much preference heterogeneity is needed before players stop finding a single dominant price?

## Backlinks (computed)

**affected by:** [LLM models of individual human choice](../technique/human-behavior-simulation-models.md)

**involved in:** [Human-calibrated customers](../opportunity/human-calibrated-customers.md)

**used by:** [Big Ambitions](../game/big-ambitions.md), [Capitalism](../game/capitalism.md), [House Flipper](../game/house-flipper.md), [Lemonade Stand](../game/lemonade-stand.md), [Planet Coaster](../game/planet-coaster.md), [RollerCoaster Tycoon](../game/rollercoaster-tycoon.md), [Schedule I](../game/schedule-i.md), [Theme Park](../game/theme-park.md)

## Sources

- [Lemonade Stand](../source/src-wikipedia-lemonade-stand.md)

---
Provenance: created in run `2026-10-24-taxonomy-m2`.
