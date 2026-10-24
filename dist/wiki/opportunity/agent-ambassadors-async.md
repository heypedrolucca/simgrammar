# Agent ambassadors between player worlds

*Opportunity* · `agent-ambassadors-async` · status: **asserted**

Let each player's simulation send language-agent representatives that trade and negotiate with other players' worlds while they are offline.

| field | value |
|---|---|
| opportunity type | New mechanic |
| involves | [Asynchronous shared regions](../mechanic/async-shared-region.md), [Trade routes](../mechanic/trade-routes.md), [Faction diplomacy](../mechanic/faction-diplomacy.md), [Contracts and orders](../mechanic/contracts-orders.md), [Natural-language interaction](../mechanic/natural-language-interaction.md) |
| applies | [Many-agent LLM societies](../technique/llm-agent-societies.md), [Language models grounded in strategic planning for negotiation games](../technique/cicero-strategic-dialogue.md), [Grammar-constrained decoding for valid game actions](../technique/constrained-decoding.md) |
| precedent | [SimCity (2013)](../game/simcity-2013.md), [Animal Crossing: New Horizons](../game/animal-crossing-new-horizons.md), [EVE Online](../game/eve-online.md), [Offworld Trading Company](../game/offworld-trading-company.md) |
| novelty | 4 |
| feasibility | 3 |
| impact | 3 |
| horizon | 1-2 years |
| key risks | Agents exploited by adversarial players., Mandate violations create disputes., Server cost of agent negotiation. |
| falsifiable signal | {'prediction': "A game will let each player's AI representative trade or negotiate with other players' worlds while those players are offline.", 'resolve_by': '2029-06-30', 'criteria': 'Feature first shipped after 2026-10-24 in a title with at least 1,000 Steam user reviews or a console release; developer material (store page, patch notes, documentation, or talk) states that an AI agent acts for an absent player in trades or negotiations with other players.'} |
| priority *(computed)* | 3.178 |

## Thesis

Asynchronous shared regions (SimCity 2013) and visits (Animal Crossing) connect players thinly because the other player is absent. Agents that represent a player's interests, constrained by the player's standing instructions, can conduct trade and diplomacy between worlds asynchronously, turning a set of single-player games into a living network.

## Design Sketch

The player appoints an envoy with a mandate (export grain, import steel, never sell land). Envoys meet other envoys in a shared hub, negotiate deals constrained by mandates, and report back with transcripts and outcomes the player can ratify.

## Key Risks

- Agents exploited by adversarial players.
- Mandate violations create disputes.
- Server cost of agent negotiation.

## Validation Experiment

Run 100 simulated player worlds with envoy agents under mandates for 30 days; measure mandate violations, trade volume, and player-rated fairness in a pilot. Success: zero hard mandate violations and positive fairness ratings.

## Falsifiable signal

- **Prediction:** A game will let each player's AI representative trade or negotiate with other players' worlds while those players are offline.
- **Resolve by:** 2029-06-30
- **Criteria:** Feature first shipped after 2026-10-24 in a title with at least 1,000 Steam user reviews or a console release; developer material (store page, patch notes, documentation, or talk) states that an AI agent acts for an absent player in trades or negotiations with other players.

## Relations

**applies**

- [Many-agent LLM societies](../technique/llm-agent-societies.md)
- [Language models grounded in strategic planning for negotiation games](../technique/cicero-strategic-dialogue.md)
- [Grammar-constrained decoding for valid game actions](../technique/constrained-decoding.md)

**involves**

- [Asynchronous shared regions](../mechanic/async-shared-region.md)
- [Trade routes](../mechanic/trade-routes.md)
- [Faction diplomacy](../mechanic/faction-diplomacy.md)
- [Contracts and orders](../mechanic/contracts-orders.md)
- [Natural-language interaction](../mechanic/natural-language-interaction.md)

**precedent**

- [SimCity (2013)](../game/simcity-2013.md)
- [Animal Crossing: New Horizons](../game/animal-crossing-new-horizons.md)
- [EVE Online](../game/eve-online.md)
- [Offworld Trading Company](../game/offworld-trading-company.md)

---
Provenance: created in run `2026-10-24-synthesis`; reviewed in `2026-10-24-review-fixes`.
