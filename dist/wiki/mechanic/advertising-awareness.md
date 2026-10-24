# Advertising and awareness

*Mechanic* · `advertising-awareness` · status: **sourced**

Spending on advertising raises a demand or awareness stock that decays without upkeep and scales how many customers arrive or buy.

| field | value |
|---|---|
| aliases | marketing, brand awareness, hype, advertising campaigns |
| family | Economy & finance |
| substrate | Aggregate stocks |
| math basis | System dynamics / ODEs, Optimization |
| feedback | Both |
| player interface | Parameter, Choice / cards |
| legibility | 3 |
| emergence potential | 2 |
| authoring cost | 1 |
| compute cost | 1 |
| tuning difficulty | 3 |
| ai leverage | 3 |
| maturity | Classic |
| core count *(computed)* | 0 |
| earliest game *(computed)* | [Lemonade Stand](../game/lemonade-stand.md) |
| earliest year *(computed)* | 1973 |
| prevalence *(computed)* | 6 |
| prevalence share *(computed)* | 0.034 |
| subgenre spread *(computed)* | 2 |
| technique count *(computed)* | 1 |
| technique exposure *(computed)* | 0.188 |

## Definition

Owns an awareness, brand, or hype stock per business, product, or venue and the rule that maps it onto customer traffic. Each period paid campaigns add to the stock with diminishing returns, and the stock decays toward a baseline when spending stops; its current level multiplies arrivals, the share of customers who consider the offering, or launch sales. Lemonade Stand (1973) reduces it to a daily input with no carryover: advertising signs bought before the day resolves raise sales alongside price and the weather. Two Point Hospital has assistants run marketing campaigns that bring in more patients. Capitalism and Game Dev Tycoon use advertising or marketing spend to build brand or pre-release hype. It differs from customer-value-choice, which owns how a customer who is already present chooses among offerings by price and value; this mechanic owns how many customers show up or consider the offering at all.

## Player Experience

Buying customers. The player decides how much to spend before the demand exists, watches arrivals rise and fall with each campaign, and learns that awareness fades: a store or game the market has forgotten needs fresh spending, while a strong brand lets prices rise.

## Design Levers

- cost per campaign unit and campaign duration
- decay rate of awareness after spending stops
- saturation curve, or diminishing returns per unit spent
- targeting by customer segment, product, or condition
- whether awareness raises arrivals, conversion, or willingness to pay
- whether advertising can sell a poor product or only amplifies quality

## Failure Modes

- Linear returns make maximum advertising always correct and remove the decision.
- Effects too small to see in the statistics teach players to skip advertising entirely.
- Without decay, one early campaign buys permanent demand.
- Advertising that overrides quality lets poor products sell and undermines the product-quality systems.

## Dynamics

- Advertising raises traffic and revenue that fund more advertising, a reinforcing loop limited by saturation.
- Pre-release hype front-loads sales, so campaign timing and release timing couple.
- Extra arrivals load service capacity, so a campaign can create queues that lower satisfaction.

## Open Questions

- Could simulated customers with stated tastes respond to generated ad copy, making campaign content rather than only spend a lever?
- Which decay and saturation curves keep advertising a recurring decision instead of a one-time setting?

## Backlinks (computed)

**affected by:** [LLM models of individual human choice](../technique/human-behavior-simulation-models.md)

**used by:** [Big Ambitions](../game/big-ambitions.md), [Capitalism](../game/capitalism.md), [Game Dev Tycoon](../game/game-dev-tycoon.md), [Lemonade Stand](../game/lemonade-stand.md), [RollerCoaster Tycoon](../game/rollercoaster-tycoon.md), [Two Point Hospital](../game/two-point-hospital.md)

## Claims

- Lemonade Stand's daily inputs are glasses made, advertising signs, and price per glass, set against a weather report. *(confidence: medium)* [[52](../source/src-wikipedia-lemonade-stand.md)]
- In Two Point Hospital assistants run marketing. *(confidence: medium)* [[53](../source/src-wikipedia-two-point-hospital.md)]

## Sources

- [Lemonade Stand](../source/src-wikipedia-lemonade-stand.md)
- [Two Point Hospital](../source/src-wikipedia-two-point-hospital.md)

---
Provenance: created in run `2026-10-24-taxonomy-triage-a`.
