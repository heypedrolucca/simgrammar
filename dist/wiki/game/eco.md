# Eco

*Game* · `eco` · status: **sourced**

A multiplayer civilization survival game in which players on one server share a simulated ecosystem, specialize in skills, craft and trade with player-made currencies, and pass enforceable laws while researching how to stop a meteor due in thirty days without wrecking the environment.

| field | value |
|---|---|
| year | 2018 |
| developer | Strange Loop Games |
| platforms | PC |
| subgenre | MMO world |
| subgenre secondary | Ecosystem / evolution, Sandbox world |
| sim domain | Biological / ecological, Economic, Political / governance |
| player role | Inhabitant |
| agency model | Direct avatar, Policy / parameter |
| time model | Asynchronous persistent |
| sim scale | Planet |
| fidelity | Systemic |
| perspective | First-person |
| win structure | Scenario goals |
| failure model | Cascading collapse |
| narrative mode | Emergent |
| multiplayer | Single-player, Co-op, Persistent MMO |
| modding | Scripting |
| production tier | Indie |
| agent count order | ~1,000 |
| emergence | 3 |
| influence | 2 |
| cluster *(computed)* | C01 |
| core count *(computed)* | 4 |
| mechanic count *(computed)* | 14 |

## Summary

A multiplayer civilization survival game in which players on one server share a simulated ecosystem, specialize in skills, craft and trade with player-made currencies, and pass enforceable laws while researching how to stop a meteor due in thirty days without wrecking the environment.

## Core Loop

gather from the shared ecosystem -> specialize in skills and craft at tables -> trade through player stores and currencies -> propose and vote on laws and taxes -> research technology to stop the meteor -> manage pollution and species populations before impact

## Design Notes

Eco makes the ecosystem a shared commons: each player's harvesting and pollution changes species populations and the climate for everyone on the server. Its answer to overexploitation is player-made institutions rather than designer rules, with enforceable laws, taxes, and currencies, and simulation data that players can cite as evidence in debates. It began as an educational project funded in part by the U.S. Department of Education.

## Relations

**uses**

- [Food web](../mechanic/food-web.md) (core): Thousands of plants and animals from dozens of species grow across the world; overhunting or overharvesting can drive a species extinct, and a disruption in one species cascades across the planet.
- [Pollution spread](../mechanic/pollution-spread.md) (core): Mining waste and industrial pollution poison rivers and kill farms, and excessive air pollution raises sea levels.
- [Player legislation](../mechanic/player-legislation.md) (core): Players propose laws in a programmable rule system and vote on them, the game enforces ratified laws, and elections set tax rates and community funds; governments range from dictatorships to lawless, trust-based communities.
- [Crisis countdown](../mechanic/crisis-countdown.md) (core): A meteor is set to strike in thirty days, and players must gather resources and research technology to stop it without harming the world.
- [Renewable regrowth](../mechanic/renewable-regrowth.md) (supporting): Plant and animal populations recover over time unless harvested faster than they regrow; cutting too many trees reduces how much air pollution is absorbed.
- [Planetary climate](../mechanic/planetary-climate.md) (supporting): Accumulated pollution changes the climate and sea level.
- [Elections](../mechanic/elections.md) (supporting)
- [Taxation](../mechanic/taxation.md) (supporting)
- [Player-driven markets](../mechanic/player-driven-market.md) (supporting): Players run stores and currency exchanges with fiat or resource-backed currencies and set exchange rates.
- [Contracts and orders](../mechanic/contracts-orders.md) (supporting): Players post labor contracts for others to fulfill.
- [Agent skills](../mechanic/agent-skills.md) (supporting): Varied food and larger homes earn skill points spent on specialties such as farming, hunting, trade, and engineering.
- [Production chains](../mechanic/production-chain.md) (supporting): More than 30 craft tables turn materials into goods across hundreds of recipes.
- [Tech tree](../mechanic/tech-tree.md) (supporting)
- [Seasonal world reset](../mechanic/seasonal-world-reset.md) (supporting): Each world is bounded by a meteor due in thirty days, so a server's run ends with stopping it or with impact, and servers are commonly wiped and restarted as fresh worlds.

## Backlinks (computed)

**precedent for:** [Natural-language legislation](../opportunity/natural-language-legislation.md)

## Sources

- [Eco (2018 video game)](../source/src-wikipedia-eco-2018.md)
- [Eco on Steam](../source/src-steam-2018-eco.md)

---
Provenance: created in run `2026-10-24-catalog-gi`.
