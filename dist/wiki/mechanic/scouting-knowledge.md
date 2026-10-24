# Scouting knowledge

*Mechanic* · `scouting-knowledge` · status: **asserted**

Entity attributes are known only with uncertainty that scouting effort reduces.

| field | value |
|---|---|
| aliases | attribute masking, scouting reports, rating uncertainty |
| family | Information & legibility |
| substrate | Agent-based, Stochastic events |
| math basis | Information theory, Probability / statistics |
| feedback | None |
| player interface | Orders, Observation only |
| legibility | 3 |
| emergence potential | 3 |
| authoring cost | 1 |
| compute cost | 2 |
| tuning difficulty | 3 |
| ai leverage | 3 |
| maturity | Established |
| core count *(computed)* | 2 |
| earliest game *(computed)* | [Out of the Park Baseball](../game/out-of-the-park-baseball.md) |
| earliest year *(computed)* | 1999 |
| prevalence *(computed)* | 4 |
| prevalence share *(computed)* | 0.023 |
| subgenre spread *(computed)* | 3 |
| technique count *(computed)* | 1 |
| technique exposure *(computed)* | 0.188 |

## Definition

Each entity attribute has a true hidden value and, per player, a knowledge level or confidence interval. Scouting actions (assigning a scout, watching matches, spending time or money) raise knowledge for specific entities or regions; knowledge may decay. The display shows a masked value, a range, a noisy point estimate, or a star rating whose noise scales with the scout's judging skill and the knowledge level. State owned: (player, entity, attribute) knowledge and the current estimate. Update rule: knowledge increases with effort and observer skill; estimate = true value plus noise scaled by remaining uncertainty, or hidden until a threshold. Canonical forms: Football Manager attribute masking, regional scouting knowledge, and scout ability and potential star ratings; Out of the Park Baseball, where displayed ratings are your scouting staff's opinion and accuracy is a setting.

## Player Experience

Recruitment becomes investment under uncertainty. The player decides where to send scouts, weighs a cheap unknown against a known star, and feels vindicated or burned when performance reveals the true value.

## Design Levers

- representation of uncertainty: masked, range, noisy estimate, or rating
- scouting cost and speed per entity or region
- scout skill as the noise level of reports
- whether knowledge decays over time
- whether true values are ever fully revealed, for example after signing
- separate uncertainty for current ability and future potential

## Failure Modes

- Third-party editors and database tools reveal true attributes, collapsing the mechanic for players who use them.
- Cheap, complete scouting turns uncertainty into a delay rather than a decision.
- Uncertainty that persists after acquisition and long observation feels arbitrary.

## Dynamics

- Information asymmetry creates market behavior: overpaying for hyped players and bargains in under-scouted regions.
- Uncertain potential couples with skill growth to make youth signings speculative bets.
- Rival AI clubs with better knowledge outbid the player, making scouting investment competitive.

## Open Questions

- Can language-model scouts write reports whose hedges and biases track their numeric noise, so reading reports is itself a skill?
- Does Bayesian updating from observed performance, shown to the player, make uncertainty feel fairer than fixed masking?

## Backlinks (computed)

**affected by:** [Regret minimization and search for imperfect-information games](../technique/imperfect-information-solvers.md)

**used by:** [Big Pharma](../game/big-pharma.md), [Command: Modern Operations](../game/command-modern-operations.md), [Football Manager](../game/football-manager.md), [Out of the Park Baseball](../game/out-of-the-park-baseball.md)

---
Provenance: created in run `2026-10-24-taxonomy-m6`.
