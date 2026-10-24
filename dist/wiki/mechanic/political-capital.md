# Political capital

*Mechanic* · `political-capital` · status: **sourced**

An abstract governing currency accrues each period from leaders, factions, or population welfare and is spent on policy changes, edicts, and other state actions.

| field | value |
|---|---|
| aliases | action currency, monarch points, political power, welfare currency, unity |
| family | Governance & policy |
| substrate | Aggregate stocks |
| math basis | System dynamics / ODEs, Optimization |
| feedback | Both |
| player interface | Choice / cards, Parameter |
| legibility | 4 |
| emergence potential | 2 |
| authoring cost | 1 |
| compute cost | 1 |
| tuning difficulty | 3 |
| ai leverage | 2 |
| maturity | Established |
| core count *(computed)* | 1 |
| earliest game *(computed)* | [Europa Universalis IV](../game/europa-universalis-4.md) |
| earliest year *(computed)* | 2013 |
| prevalence *(computed)* | 7 |
| prevalence share *(computed)* | 0.04 |
| subgenre spread *(computed)* | 4 |
| technique count *(computed)* | 0 |
| technique exposure *(computed)* | 0.0 |

## Summary

An abstract governing currency accrues each period from leaders, factions, or population welfare and is spent on policy changes, edicts, and other state actions.

## Definition

Owns one or more non-monetary stocks or capacities, each with a per-period income, an optional cap, and a price list of state actions. Income comes from the skill or loyalty of rulers and ministers, faction support, prestige, or satisfied population needs; spending buys discrete actions such as enacting or repealing a policy, issuing an edict, researching, raising stability, claiming territory, or rushing construction. Unlike a treasury, the stock usually cannot be borrowed or traded and its income comes from political or welfare state rather than economic activity, so it rations institutional change per period. Democracy 4 charges political capital, earned through loyal ministers, to introduce or cancel policies. Europa Universalis IV pays administrative, diplomatic, and military monarch points set by the ruler's skills, which buy technology among other things. Hearts of Iron IV spends political power on laws and ministers. Captain of Industry yields about 1 to 2 Unity per fully satisfied need per month, spent on edicts, outposts, quick builds, and emergency repairs. Policy-toggles owns the policies; this mechanic owns the currency that rations them.

## Player Experience

Every turn or month has a political budget. The player decides which reform is worth this period's points, saves up for a large one, and feels the quality of the ruler or cabinet as a faster or slower clock of change. Weak leaders and unhappy populations show up as a shortage of options rather than only as a penalty.

## Design Levers

- income sources (ruler skill, minister loyalty, faction approval, satisfied needs) and their weights
- cap on the stock and whether overflow is lost
- one pool versus several (administrative, diplomatic, and military points)
- action prices relative to income, and whether prices scale with realm size or development
- banked stock versus a capacity that ongoing commitments draw against
- whether the currency converts to or from money

## Failure Modes

- Hitting the cap with nothing worth buying wastes income and makes the currency invisible.
- Several parallel currencies with separate shops become spreadsheet optimization detached from the fiction.
- Income tied to leader skill makes one bad succession a long drought with few meaningful choices.
- Cheap actions let players toggle policies every period, undoing the rationing.

## Dynamics

- Spending on stability or welfare raises future income, a reinforcing loop for well-run states.
- Players time large reforms for when income peaks, such as after a strong heir succeeds or the cabinet is loyal.
- Saving for expensive actions creates long-term plans that compete with spending to answer crises.

## Open Questions

- Could political capital be replaced by negotiated backing from simulated ministers or factions without losing the clarity of a single number?
- Does currency earned from welfare, as in Captain of Industry, make players value population needs differently from currency earned from leaders?

## Backlinks (computed)

**used by:** [Captain of Industry](../game/captain-of-industry.md), [Crusader Kings III](../game/crusader-kings-3.md), [Democracy 4](../game/democracy-4.md), [Europa Universalis IV](../game/europa-universalis-4.md), [Hearts of Iron IV](../game/hearts-of-iron-4.md), [Stellaris](../game/stellaris.md), [Victoria 3](../game/victoria-3.md)

## Claims

- Democracy 4 constrains the player with political capital. *(confidence: medium)* [[84](../source/src-wikipedia-democracy-4.md)]
- Europa Universalis IV uses administrative, diplomatic, and military monarch power to buy technology, and Hearts of Iron IV uses political power for laws and ministers. *(confidence: medium)* [[85](../source/src-wikipedia-europa-universalis-4.md), [86](../source/src-wikipedia-hearts-of-iron-4.md)]
- In Captain of Industry each fully satisfied settlement need yields about 1-2 Unity per month, spent on edicts, outposts, quick trades, contracts, quick-build, vehicle recovery, emergency repairs, and building boosts. *(confidence: medium)* [[87](../source/src-coiwiki-2026-unity.md)]

## Sources

- [Democracy 4](../source/src-wikipedia-democracy-4.md)
- [Europa Universalis IV](../source/src-wikipedia-europa-universalis-4.md)
- [Hearts of Iron IV](../source/src-wikipedia-hearts-of-iron-4.md)
- [Unity](../source/src-coiwiki-2026-unity.md)

---
Provenance: created in run `2026-10-24-taxonomy-triage-a`.
