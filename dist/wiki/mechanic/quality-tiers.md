# Quality tiers

*Mechanic* · `quality-tiers` · status: **sourced**

Produced items carry quality grades derived from inputs, worker skill, or chance, scaling their value or effect.

| field | value |
|---|---|
| aliases | item quality, quality grades, rarity tiers |
| family | Resources & production |
| substrate | Stochastic events, Rule system |
| math basis | Probability / statistics, Markov / stochastic processes |
| feedback | Reinforcing (positive) |
| player interface | Observation only, Parameter |
| legibility | 3 |
| emergence potential | 2 |
| authoring cost | 2 |
| compute cost | 1 |
| tuning difficulty | 3 |
| ai leverage | 2 |
| maturity | Established |
| core count *(computed)* | 0 |
| earliest game *(computed)* | [Capitalism](../game/capitalism.md) |
| earliest year *(computed)* | 1995 |
| prevalence *(computed)* | 4 |
| prevalence share *(computed)* | 0.023 |
| subgenre spread *(computed)* | 3 |
| technique count *(computed)* | 0 |
| technique exposure *(computed)* | 0.0 |

## Definition

Each produced item carries a discrete grade drawn when it is made. The draw depends on input quality, worker or player skill, tool or module bonuses, and a random roll; the grade then multiplies the item's value, durability, or effect. Factorio: Space Age has five levels (normal, uncommon, rare, epic, legendary) with bonuses from +30% to +150%; a quality module 1 adds a +1% chance of a higher grade, each further step is ten times less likely, and a recycler returning 25% of ingredients lets players reroll. RimWorld grades crafted items from awful to legendary by crafter skill, and Dwarf Fortress grades by skill up to masterful items. Stardew Valley crops come in normal, silver, gold, and iridium quality depending on farming level and fertilizer. Inputs: ingredient grades, skill, modifiers, random draw. Outputs: graded items whose stats scale by tier.

## Player Experience

A gamble layered on production. Players chase rare outputs, sort and filter by grade, and decide whether to sell, use, or recycle low rolls. In colony sims a legendary item from a favored crafter is a memorable event; in Factorio quality becomes an expected-value problem of reroll loops.

## Design Levers

- number of tiers and the stat multiplier per tier
- base chance and how skill, inputs, or modules raise it
- whether rolls can skip tiers and how steeply odds fall per step
- reroll or recycling paths and their loss rate
- whether low-grade items have a use or are pure waste

## Failure Modes

- Many tiers multiply item variants and storage slots, cluttering logistics.
- Reroll loops without enough loss become net-positive generators; Factorio sets recycler returns at 25% and caps productivity at +300% to prevent this.
- Low tiers with no use make most production feel wasted.

## Dynamics

- Players build sorting and filtering stages, adding logistics complexity that scales with tier count.
- Skill coupling makes specific workers valuable, so losing a master crafter is a real setback.
- Higher-grade machines and modules work faster or roll better, so quality compounds once established.
- At scale, reroll loops convert a random mechanic into a predictable expected-value pipeline.

## Open Questions

- Could quality be judged by a learned model of an item's form and function, for example a player-designed object, instead of a hidden roll?
- What tier count keeps grades meaningful without overwhelming storage and sorting?

## Backlinks (computed)

**used by:** [Capitalism](../game/capitalism.md), [Factorio](../game/factorio.md), [Schedule I](../game/schedule-i.md), [Stardew Valley](../game/stardew-valley.md)

## Sources

- [Friday Facts #375 - Quality](../source/src-wube-2023-fff-375-quality.md)

---
Provenance: created in run `2026-10-24-taxonomy-m1`.
