# Victoria 3

*Game* · `victoria-3` · status: **sourced**

An economic grand strategy game set from 1836 to 1936 in which the player industrializes a nation by building production chains, passing laws through interest-group politics, and pursuing diplomatic plays while population strata respond through wages, needs, and radicalism.

| field | value |
|---|---|
| aliases | Vic3 |
| year | 2022 |
| developer | Paradox Development Studio |
| platforms | PC |
| subgenre | Grand strategy |
| subgenre secondary | Political sim |
| sim domain | Economic, Political / governance, Industrial / logistics |
| player role | Ruler / statesman |
| agency model | Policy / parameter, Order queue, Indirect incentive |
| time model | Real-time with pause |
| sim scale | Nation / polity |
| fidelity | Systemic |
| perspective | Top-down / side 2D |
| win structure | Open sandbox |
| failure model | Soft / recoverable |
| narrative mode | Hybrid |
| multiplayer | Single-player, Competitive |
| modding | Scripting |
| production tier | AA |
| agent count order | Aggregate only |
| emergence | 3 |
| influence | 2 |
| cluster *(computed)* | C04 |
| core count *(computed)* | 4 |
| mechanic count *(computed)* | 19 |

## Summary

An economic grand strategy game set from 1836 to 1936 in which the player industrializes a nation by building production chains, passing laws through interest-group politics, and pursuing diplomatic plays while population strata respond through wages, needs, and radicalism.

## Core Loop

queue construction of buildings -> buildings hire pops and run production methods -> goods trade at shifting market prices -> wages and needs set standard of living and interest-group support -> enact laws and pursue diplomatic plays -> expand industry

## Design Notes

Victoria 3 moves the player's main lever from units to the economy: the player queues construction and sets laws, and pops, prices, and wages respond, while armies are handled by generals assigned to fronts. Politics is an output of economics, since pops' economic status sets their interest-group affiliation and political strength. Diplomatic plays turn war declaration into a timed escalation of demands and counter-demands with a chance to back down (proposal crisis-escalation).

## Sources

- src-wikipedia-victoria-3
- src-paradox-2021-vic3-interest-groups
- src-paradox-2021-vic3-national-markets
- src-paradox-2023-vic3-law-enactment
- src-pcgamesn-2022-victoria-3-nested-tooltips
- src-paradox-2023-victoria-3-dev-diary-74

## Relations

**uses**

- [Interest groups](../mechanic/interest-groups.md) (core): Pops' political strength, from wealth and enfranchisement, flows into interest groups such as the Devout, Industrialists, and Rural Folk; clout is each group's share of the national total, approval comes from laws and government membership, and enacting a law runs phases whose advance or stall chances depend on group endorsement.
- [Production chains](../mechanic/production-chain.md) (core): Buildings such as mines, farms, and factories convert input goods to outputs; switchable production methods change the input mix, output, and which professions are employed.
- [Supply-demand pricing](../mechanic/supply-demand-pricing.md) (core): Each good has a base price, and the market price moves with the ratio of buy orders from consumption to sell orders from production, scaled by market access from infrastructure; prices feed back into building profitability, wages, and pops' cost of living.
- [Population strata](../mechanic/population-strata.md) (core): The population is stored as pops by profession, culture, and religion in lower, middle, and upper strata, each with its own wages, needs, and political leanings.
- [Goods consumption](../mechanic/goods-consumption.md) (supporting): Pops buy goods to meet needs, and the share met sets their standard of living.
- [Labor market](../mechanic/labor-market.md) (supporting): Buildings hire pops by profession and qualification, so labor shortages throttle new industry.
- [Policy toggles](../mechanic/policy-toggles.md) (supporting): Laws such as Free Trade and Laissez-Faire change economic and political rules.
- [Stability and unrest](../mechanic/stability-unrest.md) (supporting): Pops whose needs fall short become radicals, and radical interest groups can start a revolutionary movement with a revolution clock.
- [Faction diplomacy](../mechanic/faction-diplomacy.md) (supporting): Diplomatic plays present a demand, allow counter-demands, run a countdown to mobilize and gather backers, and become war if unresolved.
- [Tech tree](../mechanic/tech-tree.md) (supporting): Technologies such as the Atmospheric Engine unlock buildings and production methods.
- [Taxation](../mechanic/taxation.md) (supporting)
- [Treasury and budget](../mechanic/budget-treasury.md) (supporting)
- [Immigration by attractiveness](../mechanic/immigration-attractiveness.md) (supporting)
- [Causal breakdown tooltips](../mechanic/causal-tooltips.md) (supporting): Nested tooltips break values into contributing modifiers, extended to battle and market calculations.
- [Political capital](../mechanic/political-capital.md) (supporting): Authority, influence, and bureaucracy are capacities with monthly supply and ongoing usage: decrees draw on authority and diplomatic pacts on influence.
- [Culture and religion conversion](../mechanic/culture-religion-conversion.md) (supporting): Pops carry a culture and a religion; over time pops assimilate toward primary cultures and convert toward the state religion, and citizenship and church laws decide which identities face discrimination.
- [Territorial control](../mechanic/territorial-control.md) (supporting): States change hands through diplomatic plays and wars, and newly acquired states are incorporated over time before they count fully.
- [War score and peace terms](../mechanic/war-score-peace.md) (supporting): Each side's war support falls with exhaustion until one capitulates or the sides settle on the demands from the diplomatic play.
- [Pause and speed control](../mechanic/variable-speed.md) (supporting)

## Backlinks (computed)

**precedent for:** [Why-query over the simulation log](../opportunity/causal-why-query.md), [Explained delegation to AI managers](../opportunity/explained-delegation.md), [Natural-language legislation](../opportunity/natural-language-legislation.md)

## Sources

- [Victoria 3](../source/src-wikipedia-victoria-3.md)
- [Victoria 3 Dev Diary #6: Interest Groups](../source/src-paradox-2021-vic3-interest-groups.md)
- [Victoria 3 Dev Diary #9: National Markets](../source/src-paradox-2021-vic3-national-markets.md)
- [Victoria 3 Dev Diary #80: Law Enactment and Revolution Clock in 1.3](../source/src-paradox-2023-vic3-law-enactment.md)
- [Victoria 3 nested tooltip system](../source/src-pcgamesn-2022-victoria-3-nested-tooltips.md)
- [Victoria 3 Dev Diary #74 - UX Improvements](../source/src-paradox-2023-victoria-3-dev-diary-74.md)

---
Provenance: created in run `2026-10-24-catalog-gi`; reviewed in `2026-10-24-review-fixes`.
