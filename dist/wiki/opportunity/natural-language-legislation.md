# Natural-language legislation

*Opportunity* · `natural-language-legislation` · status: **asserted**

Players write laws in plain language that are compiled into typed policy parameters, while simulated interest groups argue, lobby, and comply.

| field | value |
|---|---|
| opportunity type | New mechanic |
| involves | [Policy toggles](../mechanic/policy-toggles.md), [Interest groups](../mechanic/interest-groups.md), [Player legislation](../mechanic/player-legislation.md), [Natural-language interaction](../mechanic/natural-language-interaction.md), [Elections](../mechanic/elections.md), [Stability and unrest](../mechanic/stability-unrest.md) |
| applies | [Grammar-constrained decoding for valid game actions](../technique/constrained-decoding.md), [Many-agent LLM societies](../technique/llm-agent-societies.md), [Language models grounded in strategic planning for negotiation games](../technique/cicero-strategic-dialogue.md) |
| precedent | [Democracy 4](../game/democracy-4.md), [Suzerain](../game/suzerain.md), [Eco](../game/eco.md), [A Tale in the Desert](../game/a-tale-in-the-desert.md), [Victoria 3](../game/victoria-3.md) |
| novelty | 4 |
| feasibility | 3 |
| impact | 3 |
| horizon | 1-2 years |
| falsifiable signal | {'prediction': 'A political or city-building game will let players enact free-text laws that change simulation parameters.', 'resolve_by': '2028-12-31', 'criteria': 'Feature first shipped after 2026-10-24 (early access counts) in a title with at least 1,000 Steam user reviews; documentation shows free-text law input mapped to changes in simulation rules or parameters.'} |
| priority *(computed)* | 3.178 |

## Thesis

Policy mechanics have been menus: a fixed list of toggles chosen by designers. Constrained decoding can compile free-text proposals into a typed policy object over the simulation's actual parameters, and language-model interest groups can respond in character with positions grounded in how the policy affects their simulated welfare. Player-written law moves governance games from choosing among authored options toward authoring rules, which A Tale in the Desert and Eco explored with players as legislators and humans as the parsers.

## Design Sketch

The player drafts 'Ban coal plants within 2 km of housing; subsidize heat pumps by 30 percent.' The compiler returns a structured policy card listing the parameters it maps to and anything it could not map. Interest groups (miners, residents, industrialists) post positions computed from projected welfare changes and voiced by a model. Votes and compliance follow simulation state, not rhetoric.

## Key Risks

- Players write laws the simulation cannot represent; the unmapped remainder must be visible.
- Group rhetoric can diverge from the computed welfare that actually drives votes.
- Politically sensitive content needs moderation.

## Validation Experiment

Build a policy compiler over a 40-parameter city model. Collect 300 player-written laws, have the compiler map them, and have two humans judge mapping fidelity. Success: 85 percent of laws mapped faithfully or with clearly flagged gaps, and playtesters prefer authoring to menus in a within-subjects test.

## Falsifiable signal

- **Prediction:** A political or city-building game will let players enact free-text laws that change simulation parameters.
- **Resolve by:** 2028-12-31
- **Criteria:** Feature first shipped after 2026-10-24 (early access counts) in a title with at least 1,000 Steam user reviews; documentation shows free-text law input mapped to changes in simulation rules or parameters.

## Relations

**applies**

- [Grammar-constrained decoding for valid game actions](../technique/constrained-decoding.md)
- [Many-agent LLM societies](../technique/llm-agent-societies.md)
- [Language models grounded in strategic planning for negotiation games](../technique/cicero-strategic-dialogue.md)

**involves**

- [Policy toggles](../mechanic/policy-toggles.md)
- [Interest groups](../mechanic/interest-groups.md)
- [Player legislation](../mechanic/player-legislation.md)
- [Natural-language interaction](../mechanic/natural-language-interaction.md)
- [Elections](../mechanic/elections.md)
- [Stability and unrest](../mechanic/stability-unrest.md)

**precedent**

- [Democracy 4](../game/democracy-4.md)
- [Suzerain](../game/suzerain.md)
- [Eco](../game/eco.md)
- [A Tale in the Desert](../game/a-tale-in-the-desert.md)
- [Victoria 3](../game/victoria-3.md)

---
Provenance: created in run `2026-10-24-synthesis`; reviewed in `2026-10-24-review-fixes`.
