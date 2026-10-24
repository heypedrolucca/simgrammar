# War score and peace terms

*Mechanic* · `war-score-peace` · status: **asserted**

Each war tracks a score or exhaustion level from battles, occupation, and war goals, and that value caps what a peace settlement can demand or forces capitulation.

| field | value |
|---|---|
| aliases | war score, war exhaustion, war support, peace conference |
| family | Conflict & defense |
| substrate | Aggregate stocks, Rule system |
| math basis | Game theory, Mechanism design / auctions |
| feedback | Balancing (negative) |
| player interface | Choice / cards, Observation only |
| legibility | 3 |
| emergence potential | 3 |
| authoring cost | 1 |
| compute cost | 1 |
| tuning difficulty | 3 |
| ai leverage | 3 |
| maturity | Established |
| core count *(computed)* | 0 |
| earliest game *(computed)* | [Europa Universalis IV](../game/europa-universalis-4.md) |
| earliest year *(computed)* | 2013 |
| prevalence *(computed)* | 5 |
| prevalence share *(computed)* | 0.029 |
| subgenre spread *(computed)* | 2 |
| technique count *(computed)* | 1 |
| technique exposure *(computed)* | 0.188 |

## Summary

Each war tracks a score or exhaustion level from battles, occupation, and war goals, and that value caps what a peace settlement can demand or forces capitulation.

## Definition

Owns, for each active war, a score per side (or a shared balance) and the list of war goals, plus a menu of peace terms with a cost in score. Each update, battles won, regions occupied, and time spent holding the war goal add score, and casualties and occupation add exhaustion. A peace offer is accepted when its total cost is within the winner's score or when the loser's exhaustion or support crosses a capitulation threshold; otherwise the AI weighs score against demands. Europa Universalis IV prices each demand (provinces, gold, vassalage) in war score. Crusader Kings III lets an attacker enforce the war goal at full war score and allows white peace. Victoria 3 tracks war support that falls with exhaustion until a side capitulates. Hearts of Iron IV holds a peace conference in which winners spend points on demands in turns. In Stellaris a side at maximum war exhaustion can be forced into a status quo peace. Unlike faction-diplomacy, which decides whether factions go to war, this mechanic owns how a war ends and what the winner may take.

## Player Experience

Wars become negotiations with a running tally. The player fights for score as much as for ground, deciding when a battle or a siege is worth the cost and when to cash in. Bargaining over which provinces fit within the score turns the end of a war into a planning problem, and exhaustion forces the question of whether to sue for peace before the home front breaks.

## Design Levers

- score sources and their weights: battles, occupation, blockades, holding the war goal
- cost table for each peace term, and whether costs scale with the target's size
- exhaustion accumulation and its domestic effects such as unrest or lower production
- capitulation or forced-peace thresholds, and whether third parties join the settlement
- truce length after peace

## Failure Modes

- Score dominated by occupation rewards sieging empty land over defeating armies.
- AI that refuses reasonable terms because of hidden acceptance factors makes wars drag on.
- Capitulation thresholds that trigger too early end wars before the strategic situation is resolved.

## Dynamics

- Players carry out limited wars that take exactly what the score allows, then wait out the truce and return.
- Exhaustion couples military campaigns to stability and the economy, so long wars bleed the home front.
- Multi-party peace conferences produce partitions that set up later conflicts.

## Open Questions

- Can language-model negotiators bargain over peace terms in ways players find legible and hard to exploit?
- Would score models that weigh strategic outcomes rather than counts of occupied regions produce more plausible peace deals?

## Backlinks (computed)

**affected by:** [Language models grounded in strategic planning for negotiation games](../technique/cicero-strategic-dialogue.md)

**used by:** [Crusader Kings III](../game/crusader-kings-3.md), [Europa Universalis IV](../game/europa-universalis-4.md), [Hearts of Iron IV](../game/hearts-of-iron-4.md), [Stellaris](../game/stellaris.md), [Victoria 3](../game/victoria-3.md)

---
Provenance: created in run `2026-10-24-taxonomy-triage-b`.
