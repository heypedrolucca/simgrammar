# Turn structure

*Mechanic* · `turn-structure` · status: **sourced**

The simulation advances in discrete turns, each divided into ordered phases in which players decide and the world then resolves.

| field | value |
|---|---|
| aliases | turn-based play, phases, WEGO |
| family | Time & pacing |
| substrate | Rule system |
| math basis | Game theory, Scheduling |
| feedback | None |
| player interface | Orders, Choice / cards |
| legibility | 5 |
| emergence potential | 1 |
| authoring cost | 1 |
| compute cost | 1 |
| tuning difficulty | 2 |
| ai leverage | 1 |
| maturity | Classic |
| open questions | Can learned opponents that negotiate in natural language make phase-based diplomacy viable against AI rather than only humans? |
| core count *(computed)* | 6 |
| earliest game *(computed)* | [Hamurabi](../game/hamurabi.md) |
| earliest year *(computed)* | 1968 |
| prevalence *(computed)* | 11 |
| prevalence share *(computed)* | 0.063 |
| subgenre spread *(computed)* | 8 |
| technique count *(computed)* | 1 |
| technique exposure *(computed)* | 0.2 |

## Definition

Owns the turn counter, the current phase, and the order of actors. Within a turn players act in sequence or submit orders simultaneously; then the world resolves production, growth, movement, combat, and events, and the next turn begins. A turn stands for a fixed span of game time, from a year in Hamurabi to two weeks in The Oregon Trail. Phased variants split a turn into stages, as in Agricola's work and harvest phases or Imperium Romanum II's taxation every third turn; simultaneous variants, called WEGO, such as Diplomacy and Combat Mission, collect all orders and then execute them together. Civilization is the canonical sequential form in strategy simulation. Inputs are player orders; outputs are the resolved world state each turn.

## Player Experience

Unlimited time to think. The player studies the state, plans, and commits, then watches the consequences resolve at once. Turns make cause and effect easy to trace and support a 'one more turn' rhythm, while simultaneous turns add the tension of predicting what others will do.

## Design Levers

- game time per turn and whether it changes over the game
- sequential, simultaneous, or mixed actor order
- phase decomposition and which systems update in which phase
- per-turn action limits or action points
- time limits on turns in multiplayer

## Failure Modes

- Late-game turns with many units or cities take long to play and process, producing micromanagement fatigue.
- Sequential order gives first-mover or last-mover advantages that need compensation.
- Waiting for other players' turns makes multiplayer sessions long and idle.

## Dynamics

- Players optimize per-turn efficiency, making the turn itself the unit of strategy.
- Batched world resolution makes chains of consequences visible as discrete steps.
- Simultaneous orders create bluffing and prediction between players.

## Open Questions

- Can learned opponents that negotiate in natural language make phase-based diplomacy viable against AI rather than only humans?

## Backlinks (computed)

**affected by:** [Automated generation of game rules and mechanics](../technique/automated-rule-generation.md)

**used by:** [AI Dungeon](../game/ai-dungeon.md), [Aurora 4X](../game/aurora-4x.md), [Balance of Power](../game/balance-of-power.md), [Caves of Qud](../game/caves-of-qud.md), [Sid Meier's Civilization](../game/civilization.md), [Democracy 4](../game/democracy-4.md), [Hamurabi](../game/hamurabi.md), [Lemonade Stand](../game/lemonade-stand.md), [M.U.L.E.](../game/mule.md), [The Oregon Trail](../game/oregon-trail.md), [Princess Maker 2](../game/princess-maker-2.md)

## Sources

- [Turns, rounds and time-keeping systems in games](../source/src-wikipedia-turns-rounds-and-time-keeping.md)
- [Hamurabi (video game)](../source/src-wikipedia-hamurabi.md)
- [The Oregon Trail (1971 video game)](../source/src-wikipedia-oregon-trail-1971.md)

---
Provenance: created in run `2026-10-24-taxonomy-m5`.
