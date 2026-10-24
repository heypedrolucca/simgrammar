# Dilemma cards

*Mechanic* · `dilemma-cards` · status: **sourced**

Discrete choice events present a situation with a few options that each shift meters, values, or flags in tradeoff.

| field | value |
|---|---|
| aliases | choice events, decision cards, swipe choices |
| family | Narrative & generation |
| substrate | Rule system, Stochastic events |
| math basis | Utility / decision theory, Markov / stochastic processes |
| feedback | Balancing (negative) |
| player interface | Choice / cards |
| legibility | 4 |
| emergence potential | 2 |
| authoring cost | 5 |
| compute cost | 1 |
| tuning difficulty | 3 |
| ai leverage | 4 |
| maturity | Established |
| core count *(computed)* | 3 |
| earliest game *(computed)* | [Football Manager](../game/football-manager.md) |
| earliest year *(computed)* | 2004 |
| prevalence *(computed)* | 7 |
| prevalence share *(computed)* | 0.04 |
| subgenre spread *(computed)* | 5 |
| technique count *(computed)* | 2 |
| technique exposure *(computed)* | 0.225 |

## Definition

A card holds a prompt, two to four options, and per-option effects on meters, resources, relationships, or flags, sometimes with hidden or delayed outcomes. A deck sampler draws the next card by weights conditioned on state and history. In Reigns, advisors present cards that the player swipes left or right; each choice moves some of four meters (church, people, army, treasury), and the reign ends if any meter becomes completely full or empty, after which a successor continues with newly unlocked cards. FTL beacon events, This War of Mine encounters, and Paradox event pop-ups use the same option-and-effect format inside larger simulations. Inputs: current meters and flags. Outputs: meter deltas, flag changes, and the next card's eligibility.

## Player Experience

Quick, weighty decisions where every answer costs something. Players weigh which meter can absorb the hit, try to predict hidden effects, and learn the deck over many runs. Two-sided limits, as in Reigns, make even popular choices dangerous.

## Design Levers

- number of options per card and whether one is a safe default
- how much of each option's effect is shown in advance (which meters, direction, magnitude)
- effect magnitudes and whether meters fail at one bound or both
- deck weighting, repetition limits, and state conditions for eligibility
- delayed consequences that resolve cards later

## Failure Modes

- Repeated cards expose a small deck and turn dilemmas into memorized answers.
- A dominant option on common cards removes the tradeoff.
- Fully hidden effects make outcomes feel random; fully shown effects make them arithmetic.
- Without a simulation underneath, choices do not interact and the format becomes a sequence of isolated quizzes.

## Dynamics

- Two-sided meters push players to keep every value near the middle, which creates oscillation as they correct overshoots.
- When eligibility depends on earlier flags, players steer toward or away from card lines across runs.
- Inside a larger sim, choice effects feed other systems, so a cheap answer can surface as a crisis many turns later.

## Open Questions

- Can a language model write cards conditioned on live simulation state while keeping effects inside a balanced, typed budget?
- How much effect preview maximizes deliberation time without reducing choices to arithmetic?

## Relations

**synergy**

- [Policy toggles](../mechanic/policy-toggles.md): Laws presented as dilemmas make policy a moral choice with permanent consequences (Frostpunk).

## Backlinks (computed)

**affected by:** [Grammar-constrained decoding for valid game actions](../technique/constrained-decoding.md), [LLM models of individual human choice](../technique/human-behavior-simulation-models.md)

**involved in:** [Content-elastic event systems](../opportunity/content-elastic-events.md), [Generated inspection shifts](../opportunity/generated-inspection-shifts.md)

**used by:** [Democracy 4](../game/democracy-4.md), [Football Manager](../game/football-manager.md), [Frostpunk](../game/frostpunk.md), [Papers, Please](../game/papers-please.md), [Reigns](../game/reigns.md), [Suzerain](../game/suzerain.md), [This War of Mine](../game/this-war-of-mine.md)

## Sources

- [Reigns (video game)](../source/src-wikipedia-reigns.md)
- [FTL: Faster Than Light](../source/src-wikipedia-ftl.md)

---
Provenance: created in run `2026-10-24-taxonomy-m7`.
