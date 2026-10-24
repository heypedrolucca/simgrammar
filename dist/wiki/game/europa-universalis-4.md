# Europa Universalis IV

*Game* · `europa-universalis-4` · status: **sourced**

A real-time-with-pause grand strategy game in which the player directs one of over 500 nations from 1444 to 1821 through monarch-point spending, trade-node competition, colonization, diplomacy, and war on a province map.

| field | value |
|---|---|
| aliases | EU4 |
| year | 2013 |
| developer | Paradox Development Studio |
| platforms | PC |
| subgenre | Grand strategy |
| sim domain | Political / governance, Military / conflict, Economic |
| player role | Ruler / statesman |
| agency model | Policy / parameter, Direct unit control |
| time model | Real-time with pause |
| sim scale | Nation / polity |
| fidelity | Systemic |
| perspective | Top-down / side 2D |
| win structure | Open sandbox |
| failure model | Soft / recoverable |
| narrative mode | Hybrid |
| multiplayer | Single-player, Competitive |
| modding | Total conversion |
| production tier | AA |
| agent count order | ~100 |
| emergence | 4 |
| influence | 3 |
| cluster *(computed)* | C01 |
| core count *(computed)* | 5 |
| mechanic count *(computed)* | 20 |

## Summary

A real-time-with-pause grand strategy game in which the player directs one of over 500 nations from 1444 to 1821 through monarch-point spending, trade-node competition, colonization, diplomacy, and war on a province map.

## Core Loop

accrue administrative, diplomatic, and military monarch points -> buy technology, stability, ideas, and development -> steer trade and colonize -> ally and declare wars -> occupy and annex provinces -> manage unrest, estates, and coalitions

## Design Notes

EU4 converts ruler quality into three spendable currencies (administrative, diplomatic, and military monarch points) that buy technology, stability, ideas, and province development, which makes each succession an economic event. Expansion is checked by systems rather than scripts: aggressive expansion feeds defensive coalitions, and conquered provinces stay restless until integrated. Monarch points, war score, province integration, and missionary conversion are not yet mechanics in the taxonomy (proposals political-capital, war-score-peace, territorial-claims-integration, culture-religion-conversion).

## Relations

**uses**

- [Faction diplomacy](../mechanic/faction-diplomacy.md) (core): Alliances, vassals, tributaries, and royal marriages bind nations; aggressive expansion raises other nations' hostility until they form a defensive coalition against the expander.
- [Trade routes](../mechanic/trade-routes.md) (core): Trade value generated in provinces flows downstream through a fixed directed network of trade nodes; merchants either collect in a node or steer value toward the player's home node, and trade power in each node sets the share taken.
- [Stability and unrest](../mechanic/stability-unrest.md) (core): Provinces accumulate unrest from foreign culture, religion, and recent conquest, and high unrest spawns rebel armies; national stability is a separate stock raised with administrative monarch points.
- [Tech tree](../mechanic/tech-tree.md) (supporting): Administrative, diplomatic, and military technology tracks are bought with matching monarch points; institutions such as feudalism spread between provinces and raise technology cost until embraced.
- [Interest groups](../mechanic/interest-groups.md) (supporting): Estates hold loyalty and influence over the crown and grant bonuses or demands.
- [Dynasty succession](../mechanic/dynasty-succession.md) (supporting): Each monarch's administrative, diplomatic, and military skill sets monthly monarch point income; on death an heir succeeds, with risks of regency, succession wars, or personal unions.
- [Opinion modifiers](../mechanic/opinion-modifiers.md) (supporting): AI opinion of the player is an itemized sum of modifiers such as improved relations, royal marriage, and aggressive expansion.
- [Triggered event chains](../mechanic/triggered-event-chains.md) (supporting): Historical and flavor events fire from national history and current state.
- [Reputation](../mechanic/reputation.md) (supporting): Prestige and power projection modify diplomacy and stability.
- [Policy toggles](../mechanic/policy-toggles.md) (supporting): Idea groups, policies, and government reforms change national rules.
- [Loans and debt](../mechanic/loans-debt.md) (supporting): Deficits are covered by loans, and unmanageable debt ends in bankruptcy.
- [Fog of war](../mechanic/fog-of-war.md) (supporting)
- [Causal breakdown tooltips](../mechanic/causal-tooltips.md) (supporting)
- [Pause and speed control](../mechanic/variable-speed.md) (supporting)
- [Political capital](../mechanic/political-capital.md) (core): Administrative, diplomatic, and military monarch points accrue monthly from the ruler's skills (plus advisors) and buy technology, ideas, stability, and province development, so each succession changes the nation's budget of action.
- [Corruption leakage](../mechanic/corruption-leakage.md) (supporting): A national corruption value accumulates from several state conditions and falls with a monthly budget line for rooting out corruption; while high it raises the cost of technology and other state actions.
- [Culture and religion conversion](../mechanic/culture-religion-conversion.md) (supporting): Provinces have a culture and a religion; missionaries convert province religion over time against resistance, and non-state religion or non-accepted culture adds unrest.
- [Territorial control](../mechanic/territorial-control.md) (core): Provinces have an owner and a controller; sieges flip control, peace deals transfer ownership, and new provinces must be cored with administrative power, with uncored land adding overextension and unrest.
- [War score and peace terms](../mechanic/war-score-peace.md) (supporting): War score from battles, occupation, and the war goal caps peace demands, each priced in score (provinces, gold, vassalage).
- [Statistical combat resolution](../mechanic/stat-combat-resolution.md) (supporting): Land battles roll dice each phase of fire and shock, modified by general skill and terrain, and drain each army's strength and morale until one side retreats.

## Backlinks (computed)

**influenced:** [Stellaris](../game/stellaris.md)

**precedent for:** [Negotiating faction AI](../opportunity/negotiating-faction-ai.md)

## Sources

- [Europa Universalis IV](../source/src-wikipedia-europa-universalis-4.md)

---
Provenance: created in run `2026-10-24-catalog-gi`.
