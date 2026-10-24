# Why-query over the simulation log

*Opportunity* · `causal-why-query` · status: **asserted**

Let players ask why something happened and answer from the simulation's own event log, making deep systemic games legible without simplifying them.

| field | value |
|---|---|
| opportunity type | Legibility layer |
| involves | [Causal breakdown tooltips](../mechanic/causal-tooltips.md), [Agent inspection](../mechanic/agent-inspection.md), [Advisors](../mechanic/advisors.md), [History chronicle](../mechanic/history-chronicle.md), [Stats dashboards](../mechanic/stats-dashboards.md), [Alerts feed](../mechanic/alerts-feed.md) |
| applies | [LLM explanation of simulation state](../technique/llm-explanation-of-state.md), [Grammar-constrained decoding for valid game actions](../technique/constrained-decoding.md) |
| precedent | [Dwarf Fortress](../game/dwarf-fortress.md), [Victoria 3](../game/victoria-3.md), [RimWorld](../game/rimworld.md), [Cities: Skylines II](../game/cities-skylines-2.md) |
| novelty | 4 |
| feasibility | 4 |
| impact | 5 |
| horizon | 1-2 years |
| falsifiable signal | {'prediction': "A simulation or strategy title in Steam's top 100 by concurrent players will ship a natural-language why-query grounded in game state.", 'resolve_by': '2027-12-31', 'criteria': "Official release notes or store page describing a player-facing feature that answers causal questions about the player's own game state in natural language."} |
| priority *(computed)* | 4.423 |

## Thesis

The strongest constraint on simulation depth has been legibility: players abandon systems they cannot diagnose, so designers cap coupling. Overlays and causal tooltips help with current values but not with histories ('why did the hospital close?'). If the simulation records an event log with causes, a language model can retrieve the relevant chain and narrate it with citations to specific events, and a constrained output format can force every claim to point at a logged record. This turns the event log, which many engines already keep for replays and debugging, into a player-facing explanation layer.

## Design Sketch

A query box and a right-click 'why?' on any entity. The answer is three to six sentences, each linked to log events the player can jump to on the timeline, plus a small causal graph. Answers that cannot be grounded say so. Advisors use the same pipeline proactively when a key indicator crosses a threshold.

## Key Risks

- Ungrounded but fluent answers teach players wrong models of the system.
- Event logs in shipped engines often lack cause links; instrumenting them is real work.
- Explanations can make optimal play too easy, flattening difficulty.

## Validation Experiment

Instrument an open-source simulation (a city or colony sim) to log events with parent-cause ids. Give two player groups the same failing save; one gets the why-query. Measure time to correct diagnosis and the share of answer sentences whose cited events actually support them (human audit). Success: 40 percent faster diagnosis with at least 95 percent supported sentences.

## Falsifiable signal

- **Prediction:** A simulation or strategy title in Steam's top 100 by concurrent players will ship a natural-language why-query grounded in game state.
- **Resolve by:** 2027-12-31
- **Criteria:** Official release notes or store page describing a player-facing feature that answers causal questions about the player's own game state in natural language.

## Relations

**applies**

- [LLM explanation of simulation state](../technique/llm-explanation-of-state.md)
- [Grammar-constrained decoding for valid game actions](../technique/constrained-decoding.md)

**involves**

- [Causal breakdown tooltips](../mechanic/causal-tooltips.md)
- [Agent inspection](../mechanic/agent-inspection.md)
- [Advisors](../mechanic/advisors.md)
- [History chronicle](../mechanic/history-chronicle.md)
- [Stats dashboards](../mechanic/stats-dashboards.md)
- [Alerts feed](../mechanic/alerts-feed.md)

**precedent**

- [Dwarf Fortress](../game/dwarf-fortress.md)
- [Victoria 3](../game/victoria-3.md)
- [RimWorld](../game/rimworld.md)
- [Cities: Skylines II](../game/cities-skylines-2.md)

---
Provenance: created in run `2026-10-24-synthesis`.
