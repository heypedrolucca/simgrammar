# Crowd preferences

*Mechanic* · `crowd-preferences` · status: **sourced**

Large visitor populations with individual preferences, budgets, and tolerances choose attractions and react with visible thoughts.

| field | value |
|---|---|
| aliases | guest thoughts, visitor preferences |
| family | Agents & behavior |
| substrate | Agent-based, Stochastic events |
| math basis | Probability / statistics, Utility / decision theory, Queueing theory |
| feedback | Balancing (negative) |
| player interface | Observation only, Placement, Parameter |
| legibility | 3 |
| emergence potential | 3 |
| authoring cost | 2 |
| compute cost | 3 |
| tuning difficulty | 3 |
| ai leverage | 3 |
| maturity | Classic |
| core count *(computed)* | 4 |
| earliest game *(computed)* | [Theme Park](../game/theme-park.md) |
| earliest year *(computed)* | 1994 |
| prevalence *(computed)* | 6 |
| prevalence share *(computed)* | 0.034 |
| subgenre spread *(computed)* | 1 |
| technique count *(computed)* | 2 |
| technique exposure *(computed)* | 0.375 |

## Definition

Owns a large population of visitor agents, each with preference parameters sampled at spawn (intensity range, nausea tolerance, tastes), a cash budget, and mood stocks such as happiness, energy, hunger, thirst, and toilet. When choosing what to do, a visitor filters attractions by preference and budget, picks among the acceptable ones, and on rejection or experience emits a named thought that changes happiness. In RollerCoaster Tycoon, per the OpenRCT2 reimplementation, a guest rejects a ride whose intensity rating is below its minimum or above its maximum preferred intensity (both widened by happiness), whose nausea rating exceeds its tolerance (300, 600, 800, or 1000 plus happiness), or whose price exceeds twice the ride's value (value quartered when the park charges entry); rejections lower happiness and create thoughts such as bad value, and guests with nothing left to ride head home. Outputs: attendance, spending, park rating, crowding.

## Player Experience

The player reads the crowd as a distribution: thought feeds and aggregate complaints reveal what is missing, and the fix is a layout or pricing change rather than an order. Individual guests are funny and disposable; the crowd's mood is the scoreboard, and pricing becomes a dial between revenue and goodwill.

## Design Levers

- preference distributions sampled at spawn (intensity, nausea, tastes, budget)
- acceptance rule (hard thresholds versus scored choice) and the price-to-value tolerance multiplier
- thought vocabulary and how thoughts aggregate into a park or facility rating
- mood decay rates and leave-the-park thresholds
- crowd size and spawn rate tied to rating, marketing, or price of entry

## Failure Modes

- Price-value rules that ignore context let players overcharge a few attractions with no penalty, or punish small price changes too harshly.
- Thought spam: hundreds of identical thoughts bury the actionable signal.
- Narrow preference sampling makes the crowd behave like one average agent, removing segmentation decisions.
- Large crowds cost pathfinding and update time, capping park size.

## Dynamics

- Preferences spread over intensity create demand for a portfolio of gentle and intense attractions rather than one best ride.
- Rating raises attendance, and the larger crowd congests queues and paths until mood falls, a balancing loop on growth.
- Players learn the value threshold and price every attraction just below it, a stable arbitrage the rule invites.

## Open Questions

- Can visitor preference models fitted to real attendance or survey data make tycoon crowds more segmentable without losing legibility?
- How should thousands of thoughts be summarized so the player sees causes rather than noise?

## Relations

**synergy**

- [Customer value choice](../mechanic/customer-value-choice.md): Individual tastes and budgets make pricing and attraction mix matter.
- [Service queues](../mechanic/service-queues.md): Visible queues and complaints let crowds express capacity problems.

## Backlinks (computed)

**affected by:** [LLM models of individual human choice](../technique/human-behavior-simulation-models.md), [Mean field games and mean-field learning](../technique/mean-field-games.md)

**involved in:** [Human-calibrated customers](../opportunity/human-calibrated-customers.md), [Mean-field crowds and traffic](../opportunity/mean-field-crowds.md), [Learned motion for simulated crowds](../opportunity/neural-npc-motion.md)

**used by:** [Jurassic World Evolution](../game/jurassic-world-evolution.md), [Planet Coaster](../game/planet-coaster.md), [Planet Zoo](../game/planet-zoo.md), [RollerCoaster Tycoon](../game/rollercoaster-tycoon.md), [Theme Park](../game/theme-park.md), [Zoo Tycoon](../game/zoo-tycoon.md)

## Sources

- [OpenRCT2 source: Guest.cpp (guest ride choice and thoughts)](../source/src-openrct2-2026-guest-behaviour.md)
- [RollerCoaster Tycoon (video game)](../source/src-wikipedia-rollercoaster-tycoon.md)

---
Provenance: created in run `2026-10-24-taxonomy-m3`.
