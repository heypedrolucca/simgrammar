# Negotiation

*Mechanic* · `negotiation` · status: **sourced**

The player and an AI party exchange offers and counteroffers over wages, prices, or contract terms against the AI's hidden reservation value until a deal is struck or talks fail.

| field | value |
|---|---|
| aliases | haggling, contract talks, bargaining, wage negotiation |
| family | Economy & finance |
| substrate | Rule system, Agent-based |
| math basis | Game theory, Utility / decision theory |
| feedback | Balancing (negative) |
| player interface | Choice / cards, Parameter |
| legibility | 3 |
| emergence potential | 2 |
| authoring cost | 2 |
| compute cost | 1 |
| tuning difficulty | 3 |
| ai leverage | 4 |
| maturity | Classic |
| core count *(computed)* | 0 |
| earliest game *(computed)* | [Theme Park](../game/theme-park.md) |
| earliest year *(computed)* | 1994 |
| prevalence *(computed)* | 4 |
| prevalence share *(computed)* | 0.023 |
| subgenre spread *(computed)* | 2 |
| technique count *(computed)* | 3 |
| technique exposure *(computed)* | 0.625 |

## Summary

The player and an AI party exchange offers and counteroffers over wages, prices, or contract terms against the AI's hidden reservation value until a deal is struck or talks fail.

## Definition

Owns a negotiation session: the terms on the table (wage, fee, price, length, bonuses, clauses), the counterpart's reservation value and preferred terms, a patience or round budget, and the outcome. Each round the player proposes terms; the counterpart accepts if the offer clears its reservation value and otherwise counters toward its preference, and patience falls with each round or with offers far from acceptable. When patience runs out talks end, sometimes with a consequence such as a strike, a lost transfer, or damaged goodwill. Reservation values come from simulation state such as the counterpart's ability, reputation, market rates, alternatives, and relationship with the player. Theme Park (1994) has wage negotiations with staff and supply negotiations, where failure brings strikes or lost shipments; sports management games run contract and transfer talks with players, agents, and clubs. It differs from staff-hiring, which owns the roster and wages once agreed, and from faction-diplomacy, which owns standing relations and treaty acceptance rather than a bounded bargaining session over terms.

## Player Experience

A small poker game inside the management sim. The player probes how low a star will go, risks a walkout or a strike by pushing too hard, and weighs a deal now against losing the target. Talks put a face on the economy's prices.

## Design Levers

- spread between the counterpart's reservation value and its opening demand
- number of rounds or patience, and what drains it
- how much of the counterpart's position is revealed (hints, agent comments, mood)
- which terms can be traded against each other (wage, length, bonuses, clauses)
- consequence of failure (walkout, strike, lost deal, damaged relationship)
- whether rival bidders negotiate at the same time

## Failure Modes

- Fixed, discoverable acceptance rules let players always find the minimum, turning talks into a ritual.
- Refusals with no visible reason feel random and push players to accept the first offer.
- Long multi-clause talks repeated for every signing become busywork.
- AI counterparts that accept deals clearly bad for themselves break the economy.

## Dynamics

- Reservation values tied to reputation and form make success raise future wage demands, a balancing loop on dominant teams.
- Competing bidders turn talks into auctions that push prices up for scarce talent.
- Failed wage talks cascade into service failures when staff strike, as in Theme Park.

## Open Questions

- Can language-model counterparts bargain in natural language while their concessions stay consistent with a calibrated reservation value?
- How much of the counterpart's position should be revealed so talks reward reading people rather than brute-force probing?

## Backlinks (computed)

**affected by:** [Language models grounded in strategic planning for negotiation games](../technique/cicero-strategic-dialogue.md), [LLM models of individual human choice](../technique/human-behavior-simulation-models.md), [Regret minimization and search for imperfect-information games](../technique/imperfect-information-solvers.md)

**used by:** [Football Manager](../game/football-manager.md), [Motorsport Manager](../game/motorsport-manager.md), [Out of the Park Baseball](../game/out-of-the-park-baseball.md), [Theme Park](../game/theme-park.md)

## Claims

- Theme Park includes wage and supply negotiations. *(confidence: medium)* [[81](../source/src-wikipedia-theme-park.md)]

## Sources

- [Theme Park (video game)](../source/src-wikipedia-theme-park.md)

---
Provenance: created in run `2026-10-24-taxonomy-triage-a`.
