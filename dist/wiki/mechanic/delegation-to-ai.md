# Delegation to AI managers

*Mechanic* · `delegation-to-ai` · status: **sourced**

Subsystems are handed to AI managers or governors that pursue player-set goals within bounds.

| field | value |
|---|---|
| aliases | governors, sector AI, automation, AI managers |
| family | Control & automation |
| substrate | Rule system, Agent-based |
| math basis | Utility / decision theory, Control theory |
| feedback | Balancing (negative) |
| player interface | Parameter, Orders |
| legibility | 3 |
| emergence potential | 3 |
| authoring cost | 2 |
| compute cost | 2 |
| tuning difficulty | 4 |
| ai leverage | 4 |
| maturity | Established |
| core count *(computed)* | 2 |
| earliest game *(computed)* | [Capitalism](../game/capitalism.md) |
| earliest year *(computed)* | 1995 |
| prevalence *(computed)* | 7 |
| prevalence share *(computed)* | 0.04 |
| subgenre spread *(computed)* | 6 |
| technique count *(computed)* | 3 |
| technique exposure *(computed)* | 1.062 |

## Definition

The player assigns a subsystem (a city, sector, colony, fleet, department, or set of planets) to an AI controller and sets objectives and constraints: a focus, a budget, permissions, and policies. Each decision interval the controller runs the same decision logic the game's opponent AI uses, restricted to that subsystem, and issues actions on the player's behalf. State owned: assignment, goal settings, and permissions per delegated unit; the rest is read from the subsystem. Inputs: subsystem state and player settings. Outputs: build, research, production, or movement actions. Canonical forms: Stellaris sectors, which a 2016 dev diary justified with a core-world limit and in which sector governors develop planets and build mining stations under a player-set focus, Hearts of Iron IV battle plans executed by AI-controlled generals, automated workers in the Civilization series, Football Manager staff responsibilities, and automated traders and miners in X4: Foundations.

## Player Experience

The player moves up a level of abstraction and manages managers. Delegation trades control for attention and enables play at empire scale. When the AI does something dumb it feels like losing control; when it works it feels like governing.

## Design Levers

- granularity of goals: single focus, weighted priorities, or explicit rules
- permissions such as may build, may demolish, may spend reserves
- transparency: whether the manager explains its choices
- manager competence relative to a good player
- incentives to delegate: hard limits on direct control versus voluntary convenience
- ease of reclaiming control and per-item overrides

## Failure Modes

- Managers that underperform a competent player turn delegation into a penalty that players avoid at all costs.
- Opaque managers make unexplained choices that players cannot correct without micromanaging.
- Managers that are too strong remove the game: the optimal play is to delegate everything.
- Forced delegation through control caps is widely resented; Stellaris sectors were reworked in later updates.

## Dynamics

- Delegation allows simulations far larger than one player could micromanage, shifting play to allocation among managers.
- Partial delegation creates principal-agent tension: players watch managers and intervene at thresholds.
- Delegated units pursuing local goals can conflict with each other, such as two governors competing for one resource.

## Open Questions

- Can language-model managers take natural-language mandates (keep morale high but never let the treasury go negative), explain their tradeoffs, and remain competent?
- Does delegation to a learned policy trained against the game's simulation make managers better than humans, and what is left for the player if so?

## Relations

**tension**

- [Embodied skill control](../mechanic/embodied-skill-control.md): Automating a subsystem removes the skill expression that made it the point.

## Backlinks (computed)

**affected by:** [Generalist instructable game agents (SIMA)](../technique/generalist-game-agents.md), [Monte Carlo tree search for game AI](../technique/monte-carlo-tree-search.md), [LLM-written skill libraries (Voyager)](../technique/voyager-skill-libraries.md)

**involved in:** [Explained delegation to AI managers](../opportunity/explained-delegation.md), [Intent-level orders](../opportunity/intent-level-orders.md), [Teachable sim companion](../opportunity/teachable-sim-companion.md)

**used by:** [Big Ambitions](../game/big-ambitions.md), [Capitalism](../game/capitalism.md), [Command: Modern Operations](../game/command-modern-operations.md), [Farming Simulator 25](../game/farming-simulator-25.md), [Hearts of Iron IV](../game/hearts-of-iron-4.md), [Silent Hunter III](../game/silent-hunter-3.md), [Stellaris](../game/stellaris.md)

## Claims

- Stellaris launched with a limit on directly controlled core worlds, beyond which penalties applied, and sectors run by governors who develop planets under a player-set focus and taxation. *(confidence: high)* [[72](../source/src-paradox-2016-stellaris-dev-diary-21-sectors.md)]

## Sources

- [Stellaris Dev Diary #21: Administrative Sectors](../source/src-paradox-2016-stellaris-dev-diary-21-sectors.md)

---
Provenance: created in run `2026-10-24-taxonomy-m6`.
