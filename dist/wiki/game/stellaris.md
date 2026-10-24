# Stellaris

*Game* · `stellaris` · status: **sourced**

A real-time-with-pause space 4X and grand strategy game in which the player designs a species and empire, expands across a procedurally generated hyperlane galaxy from 2200, manages pops, jobs, ethics-based factions, and research card draws, and faces late-game crises.

| field | value |
|---|---|
| year | 2016 |
| developer | Paradox Development Studio |
| platforms | PC, Console |
| subgenre | 4X strategy |
| subgenre secondary | Grand strategy |
| sim domain | Cosmic / space, Political / governance, Military / conflict |
| player role | Ruler / statesman |
| agency model | Direct unit control, Policy / parameter, Zoning / placement |
| time model | Real-time with pause |
| sim scale | Interplanetary+ |
| fidelity | Stylized |
| perspective | Free 3D camera |
| win structure | Competitive victory |
| failure model | Soft / recoverable |
| narrative mode | Hybrid |
| multiplayer | Single-player, Competitive |
| modding | Total conversion |
| production tier | AA |
| agent count order | ~100 |
| emergence | 3 |
| influence | 2 |
| influenced by | [Europa Universalis IV](../game/europa-universalis-4.md) |
| cluster *(computed)* | C04 |
| core count *(computed)* | 3 |
| mechanic count *(computed)* | 20 |

## Summary

A real-time-with-pause space 4X and grand strategy game in which the player designs a species and empire, expands across a procedurally generated hyperlane galaxy from 2200, manages pops, jobs, ethics-based factions, and research card draws, and faces late-game crises.

## Core Loop

survey systems with science ships -> claim systems and colonize planets -> build districts that create jobs for pops -> draw research cards and build fleets -> negotiate or fight neighboring empires -> survive the late-game crisis

## Design Notes

Stellaris combines a space 4X opening (survey, claim, colonize) with Paradox grand strategy systems: real time with pause, internal factions, and event chains. Its research model replaces a visible tree with weighted random card draws, so two runs of the same empire research in different orders. Hyperlane-only travel turns the galaxy into a graph with chokepoints. Henrik Fahraeus named Star Control II, Master of Orion II, and Europa Universalis IV as roughly equal influences.

## Relations

**influenced by**

- [Europa Universalis IV](../game/europa-universalis-4.md)

**uses**

- [Tech tree](../mechanic/tech-tree.md) (core): Physics, society, and engineering research each offer three semi-random project cards weighted by ethics, the scientist's traits, and known technologies; rare technologies and anomaly-granted cards vary each run, and costs rise as the game goes on.
- [Population strata](../mechanic/population-strata.md) (core): Pops fill jobs created by planetary districts and buildings in worker, specialist, and ruler strata; each job consumes and produces resources such as energy, minerals, food, consumer goods, and alloys.
- [Triggered event chains](../mechanic/triggered-event-chains.md) (core): Anomalies found by science ships open authored event chains, and galactic crises such as marauder invasions, awakened machine empires, and extradimensional invaders begin after set periods.
- [Faction diplomacy](../mechanic/faction-diplomacy.md) (supporting): Empires negotiate, form federations, and go to war; ethics such as xenophobe or xenophile shape AI attitudes.
- [Interest groups](../mechanic/interest-groups.md) (supporting): Pops join political factions according to ethics, and faction support produces unity.
- [Stability and unrest](../mechanic/stability-unrest.md) (supporting)
- [Delegation to AI managers](../mechanic/delegation-to-ai.md) (supporting): Planets beyond the core limit can be grouped into sectors run by AI governors with a player-set focus.
- [Modular assembly](../mechanic/modular-assembly.md) (supporting): Ships are designed from hull sections and components.
- [Procedural terrain](../mechanic/procedural-terrain.md) (supporting): Each galaxy is generated with star systems linked only by hyperlanes.
- [Personality traits](../mechanic/personality-traits.md) (supporting): Species traits and leader traits modify output and behavior.
- [Policy toggles](../mechanic/policy-toggles.md) (supporting): Ethics, civics, policies, and edicts change empire rules.
- [Goods consumption](../mechanic/goods-consumption.md) (supporting)
- [Fog of war](../mechanic/fog-of-war.md) (supporting)
- [Pause and speed control](../mechanic/variable-speed.md) (supporting)
- [Political capital](../mechanic/political-capital.md) (supporting): Unity, produced partly by faction support, buys traditions, and influence pays for new outposts and territorial claims.
- [Corruption leakage](../mechanic/corruption-leakage.md) (supporting): Empire size grows with systems, colonies, and pops, and size beyond administrative capacity raises technology and tradition costs; bureaucrat jobs add capacity to offset it.
- [Culture and religion conversion](../mechanic/culture-religion-conversion.md) (supporting): Each pop holds an ethic that drifts toward ethics with higher attraction, modified by government ethics, policies, and living conditions, and pop ethics decide faction membership.
- [Territorial control](../mechanic/territorial-control.md) (supporting): Empires take systems by building outposts, borders follow owned systems, and claims bought with influence set what wars can take.
- [War score and peace terms](../mechanic/war-score-peace.md) (supporting): War exhaustion rises from losses and occupation, and a side at maximum exhaustion can be forced into a status quo peace.
- [Statistical combat resolution](../mechanic/stat-combat-resolution.md) (supporting): Fleet battles resolve from ship weapons, shields, armor, and hull values against each other, and ground combat compares army attack and health.

## Backlinks (computed)

**influenced:** [Dyson Sphere Program](../game/dyson-sphere-program.md)

**precedent for:** [Explained delegation to AI managers](../opportunity/explained-delegation.md), [Negotiating faction AI](../opportunity/negotiating-faction-ai.md), [Research by named scientists](../opportunity/scientists-not-tech-trees.md)

## Sources

- [Stellaris (video game)](../source/src-wikipedia-stellaris.md)
- [Stellaris Dev Diary #11: Research & Technology](../source/src-paradox-2015-stellaris-dev-diary-11.md)
- [Stellaris Dev Diary #21: Administrative Sectors](../source/src-paradox-2016-stellaris-dev-diary-21-sectors.md)

---
Provenance: created in run `2026-10-24-catalog-gi`.
