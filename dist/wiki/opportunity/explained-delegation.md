# Explained delegation to AI managers

*Opportunity* · `explained-delegation` · status: **asserted**

Subsystem managers that learn the player's preferences from their past decisions and explain each action, so delegation scales play without hiding it.

| field | value |
|---|---|
| opportunity type | Mechanic upgrade |
| involves | [Delegation to AI managers](../mechanic/delegation-to-ai.md), [Advisors](../mechanic/advisors.md), [Policy toggles](../mechanic/policy-toggles.md), [Stats dashboards](../mechanic/stats-dashboards.md), [Staff hiring and rosters](../mechanic/staff-hiring.md) |
| applies | [Generalist instructable game agents (SIMA)](../technique/generalist-game-agents.md), [LLM explanation of simulation state](../technique/llm-explanation-of-state.md), [Self-play planning with learned models (AlphaZero, MuZero, Dreamer)](../technique/model-based-planning-muzero.md) |
| precedent | [Stellaris](../game/stellaris.md), [Football Manager](../game/football-manager.md), [Anno 1800](../game/anno-1800.md), [Victoria 3](../game/victoria-3.md) |
| novelty | 3 |
| feasibility | 4 |
| impact | 3 |
| horizon | 1-2 years |
| key risks | Imitating a novice player perpetuates mistakes., Explanations that rationalize rather than explain., Late-game play becomes approval clicking. |
| falsifiable signal | {'prediction': "A grand strategy or management game will ship AI managers that learn from the individual player's past decisions.", 'resolve_by': '2028-12-31', 'criteria': 'Developer documentation describing per-player preference learning for delegated subsystems.'} |
| priority *(computed)* | 3.318 |

## Thesis

Delegation exists (Stellaris sectors, Football Manager staff, automated trade routes) but managers are weak and opaque, so players either micromanage or tolerate bad decisions. Imitation of the player's own past choices plus explanation grounded in game state makes delegation trustworthy: the manager does what you would do and tells you why.

## Design Sketch

Hand a region, department, or supply chain to a manager. It proposes actions with reasons referencing indicators and the player's past choices; the player can approve, veto, or adjust standing preferences. A weekly report summarizes what changed.

## Key Risks

- Imitating a novice player perpetuates mistakes.
- Explanations that rationalize rather than explain.
- Late-game play becomes approval clicking.

## Validation Experiment

Train a manager by imitation on a player's first 10 hours of decisions in a strategy prototype, then measure agreement with the player's choices in held-out situations and player trust ratings. Success: 75 percent agreement and higher trust than the baseline AI manager.

## Falsifiable signal

- **Prediction:** A grand strategy or management game will ship AI managers that learn from the individual player's past decisions.
- **Resolve by:** 2028-12-31
- **Criteria:** Developer documentation describing per-player preference learning for delegated subsystems.

## Relations

**applies**

- [Generalist instructable game agents (SIMA)](../technique/generalist-game-agents.md)
- [LLM explanation of simulation state](../technique/llm-explanation-of-state.md)
- [Self-play planning with learned models (AlphaZero, MuZero, Dreamer)](../technique/model-based-planning-muzero.md)

**involves**

- [Delegation to AI managers](../mechanic/delegation-to-ai.md)
- [Advisors](../mechanic/advisors.md)
- [Policy toggles](../mechanic/policy-toggles.md)
- [Stats dashboards](../mechanic/stats-dashboards.md)
- [Staff hiring and rosters](../mechanic/staff-hiring.md)

**precedent**

- [Stellaris](../game/stellaris.md)
- [Football Manager](../game/football-manager.md)
- [Anno 1800](../game/anno-1800.md)
- [Victoria 3](../game/victoria-3.md)

---
Provenance: created in run `2026-10-24-synthesis`.
