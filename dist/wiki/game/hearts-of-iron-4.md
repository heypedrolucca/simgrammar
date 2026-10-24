# Hearts of Iron IV

*Game* · `hearts-of-iron-4` · status: **sourced**

A World War II grand strategy game starting in 1936 or 1939 in which the player builds factories, turns resources into equipment, designs divisions, follows a national focus tree, and directs fronts and battle plans across land, sea, and air.

| field | value |
|---|---|
| aliases | HOI4 |
| year | 2016 |
| developer | Paradox Development Studio |
| platforms | PC |
| subgenre | Grand strategy |
| subgenre secondary | Wargame / military sim |
| sim domain | Military / conflict, Political / governance, Industrial / logistics |
| player role | Commander |
| agency model | Direct unit control, Policy / parameter, Order queue |
| time model | Real-time with pause |
| sim scale | Nation / polity |
| fidelity | Systemic |
| perspective | Top-down / side 2D |
| win structure | Open sandbox |
| failure model | Soft / recoverable |
| narrative mode | Hybrid |
| multiplayer | Single-player, Competitive, Co-op |
| modding | Total conversion |
| production tier | AA |
| agent count order | ~1,000 |
| emergence | 3 |
| influence | 2 |
| cluster *(computed)* | C01 |
| core count *(computed)* | 4 |
| mechanic count *(computed)* | 16 |

## Summary

A World War II grand strategy game starting in 1936 or 1939 in which the player builds factories, turns resources into equipment, designs divisions, follows a national focus tree, and directs fronts and battle plans across land, sea, and air.

## Core Loop

pick national focuses and spend political power -> assign civilian factories to construction and military factories to equipment -> design and train divisions -> draw fronts and battle plans -> divisions fight on supply, terrain, and weather -> capitulate rivals or hold

## Design Notes

HOI4 separates the industrial war from the field war: civilian factories build capacity and military factories turn resources into equipment, so divisions fight only as well as stockpiles and supply allow. Battle plans let the player act at army-group scale and leave division movement to the AI. National focus trees are the authored branching layer that steers countries toward historical or alternate paths, while battles resolve from unit statistics (proposal stat-combat-resolution).

## Relations

**uses**

- [Modular assembly](../mechanic/modular-assembly.md) (core): Division templates combine battalions (infantry, tanks, cavalry, motorized, mechanized) and support companies, and the mix sets combat statistics and equipment needs; tank, ship, and plane designers added by DLC apply the same idea to equipment.
- [Supply lines](../mechanic/supply-lines.md) (core): Supply hubs connect to the capital by railway, with hub capacity set by railway level and limited by the weakest link; supply falls off per province from the hub, and divisions at 35% supply or less suffer attrition and combat penalties.
- [Delegation to AI managers](../mechanic/delegation-to-ai.md) (core): The player draws front lines and offensive arrows for armies under generals, and the AI moves divisions to carry out the battle plan; divisions can also be ordered directly.
- [Tech tree](../mechanic/tech-tree.md) (core): Research runs in parallel slots, and each country has a national focus tree in which one focus at a time is completed for bonuses such as extra factories or events; at launch only Germany, the UK, the USSR, and the US had unique trees.
- [Production chains](../mechanic/production-chain.md) (supporting): Military factories turn strategic resources into equipment on production lines, dockyards build ships, and civilian factories build infrastructure and handle trade.
- [Faction diplomacy](../mechanic/faction-diplomacy.md) (supporting): Countries join factions and guarantee others; world tension from 0 to 100 gates what democracies can do.
- [Policy toggles](../mechanic/policy-toggles.md) (supporting): Mobilization, conscription, and trade laws and ministers are bought with political power.
- [Stability and unrest](../mechanic/stability-unrest.md) (supporting): Ideology popularity among democratic, communist, fascist, and non-aligned groups shifts the government and can end in civil war.
- [Triggered event chains](../mechanic/triggered-event-chains.md) (supporting)
- [Fog of war](../mechanic/fog-of-war.md) (supporting)
- [Weather](../mechanic/weather.md) (supporting): Sea and air regions have weather that affects operations.
- [Pause and speed control](../mechanic/variable-speed.md) (supporting)
- [Political capital](../mechanic/political-capital.md) (supporting): Political power accrues over time and is spent on laws such as mobilization, conscription, and trade, on ministers, and on decisions.
- [Territorial control](../mechanic/territorial-control.md) (supporting): States are core or non-core, armies occupy enemy states during war, and peace conferences transfer ownership.
- [War score and peace terms](../mechanic/war-score-peace.md) (supporting): When a country capitulates, winners take turns spending peace conference points on annexation, puppets, and other demands.
- [Statistical combat resolution](../mechanic/stat-combat-resolution.md) (supporting): Divisions fight in hourly combat rounds comparing attacks against defense or breakthrough, draining organization and strength under terrain, weather, and supply modifiers.

## Sources

- [Hearts of Iron IV](../source/src-wikipedia-hearts-of-iron-4.md)
- [Supply](../source/src-paradoxwikis-2026-hoi4-supply.md)

---
Provenance: created in run `2026-10-24-catalog-gi`.
