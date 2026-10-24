# Statistical combat resolution

*Mechanic* · `stat-combat-resolution` · status: **asserted**

Battles between units resolve from attack, defense, morale, terrain, and random rolls in rounds rather than from physics or modeled sensors and weapons.

| field | value |
|---|---|
| aliases | dice combat, combat resolution tables, strength comparison, auto-resolve |
| family | Conflict & defense |
| substrate | Stochastic events, Aggregate stocks, Rule system |
| math basis | Probability / statistics, Markov / stochastic processes, System dynamics / ODEs |
| feedback | Reinforcing (positive) |
| player interface | Orders, Observation only |
| legibility | 3 |
| emergence potential | 3 |
| authoring cost | 2 |
| compute cost | 1 |
| tuning difficulty | 4 |
| ai leverage | 2 |
| maturity | Classic |
| core count *(computed)* | 0 |
| earliest game *(computed)* | [Sid Meier's Civilization](../game/civilization.md) |
| earliest year *(computed)* | 1991 |
| prevalence *(computed)* | 7 |
| prevalence share *(computed)* | 0.04 |
| subgenre spread *(computed)* | 4 |
| technique count *(computed)* | 1 |
| technique exposure *(computed)* | 0.3 |

## Definition

Owns, per engaged unit or stack, strength pools (hit points, manpower, organization, morale) and a vector of combat stats, and, per engagement, a round counter and modifiers from terrain, commanders, and supply. Each round, each side's damage is computed from its attack against the opponent's defense, scaled by modifiers and a random draw, and subtracted from the opponent's pools; a side whose morale or organization breaks retreats or is destroyed. Sid Meier's Civilization compares a unit's attack with the defender's defense under terrain and fortification modifiers and a random draw. Europa Universalis IV rolls dice in alternating fire and shock phases modified by general skill and terrain, and morale damage usually ends the battle. Hearts of Iron IV compares divisions' attack against defense or breakthrough, draining organization. FTL rolls each shot against the target's evasion and absorbs shots with shield layers. Unlike military-operations, there are no modeled sensors, signatures, or flight paths; unlike attribute-match-engine, the output is attrition of unit pools rather than a stream of sports events.

## Player Experience

Battles are prepared rather than performed. The player stacks advantages (terrain, a better general, the right unit mix, a fresh army) and then watches the bars move, knowing the dice can still go against them. Reading a combat preview and deciding whether the odds justify an attack is the core skill.

## Design Levers

- stat set: attack and defense only, or separate stats for different damage types and targets
- randomness: dice range per round versus deterministic expected values
- morale or organization as a separate pool that ends battles before units are destroyed
- terrain, river crossing, fortification, and commander modifiers
- round length and the number of rounds before a battle resolves
- how much of the formula and odds the game previews

## Failure Modes

- One unit composition or stat dominates once players find the formula's best ratio, a recurring issue in strategy communities.
- High variance lets a weak unit defeat a much stronger one, which reads as unfair when the odds were not shown.
- Opaque modifier stacks make losses impossible to diagnose without community spreadsheets.

## Dynamics

- Players optimize army compositions and commanders around the formula, producing a meta that patches revise.
- Morale breaking before units die produces retreats and pursuits, giving campaigns a rhythm of decisive and indecisive battles.
- Terrain modifiers make certain regions natural defensive lines, shaping fronts and borders.

## Open Questions

- Can generated battle narration explain why a stat-resolved battle went as it did, so players can separate luck from preparation?
- Could learned surrogate models of tactical combat give abstract resolution more of the texture of simulated battles at low cost?

## Backlinks (computed)

**affected by:** [Agent-based automated playtesting and balancing](../technique/automated-playtesting.md)

**used by:** [Sid Meier's Civilization](../game/civilization.md), [Crusader Kings III](../game/crusader-kings-3.md), [Europa Universalis IV](../game/europa-universalis-4.md), [FTL: Faster Than Light](../game/ftl.md), [Hearts of Iron IV](../game/hearts-of-iron-4.md), [Kenshi](../game/kenshi.md), [Stellaris](../game/stellaris.md)

---
Provenance: created in run `2026-10-24-taxonomy-triage-b`.
