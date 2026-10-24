# Game Dev Tycoon

*Game* · `game-dev-tycoon` · status: **sourced**

A game-studio business sim where the player picks topic, genre, and platform for each game, splits development effort across design and technology focus areas, and lives or dies by review scores across the history of the industry.

| field | value |
|---|---|
| year | 2012 |
| developer | Greenheart Games |
| platforms | PC, Mobile, Handheld |
| subgenre | Business / economic sim |
| sim domain | Economic, Occupational |
| player role | Manager / owner |
| agency model | Policy / parameter |
| time model | Real-time with pause |
| sim scale | Facility |
| fidelity | Stylized |
| perspective | Isometric |
| win structure | Score / ranking |
| failure model | Hard restart |
| narrative mode | Hybrid |
| multiplayer | Single-player |
| modding | Scripting |
| production tier | Indie |
| agent count order | ~10 |
| emergence | 2 |
| influence | 2 |
| cluster *(computed)* | C03 |
| core count *(computed)* | 3 |
| mechanic count *(computed)* | 11 |

## Summary

A game-studio business sim where the player picks topic, genre, and platform for each game, splits development effort across design and technology focus areas, and lives or dies by review scores across the history of the industry.

## Core Loop

choose topic, genre, platform, and audience -> allocate focus across three development stages -> design and technology points accumulate with bugs -> reviews score the game -> sales and fans -> research, engines, and hires

## Design Notes

Game Dev Tycoon reduces game making to a configuration problem scored by a hidden market model: each topic and genre pair, each genre and audience pair, and each platform carry fit weights, and each genre favors a particular split of effort across the development stages. Review scores compare the new game against the player's previous best, so the bar rises as the studio improves. A fictional timeline of parody consoles enters and leaves the market from the 1980s onward, which forces platform bets (date-driven availability is proposed as dated-tech-timeline). Greenheart released its own cracked copy in which piracy bankrupts the in-game studio.

## Relations

**uses**

- [Product development](../mechanic/product-development.md) (core): Each game is a topic, genre, platform, and audience pick plus focus sliders across three development stages; reviews score its fit and quality against the studio's best.
- [Staff hiring and rosters](../mechanic/staff-hiring.md) (core): After moving out of the garage, the player hires designers and programmers with design, technology, and speed stats and assigns them to development tasks.
- [Tech tree](../mechanic/tech-tree.md) (core): Research points unlock new topics, genres, and engine features; custom engines bundle researched features and raise technology output.
- [Agent skills](../mechanic/agent-skills.md) (supporting): Staff gain experience and can be sent to training to raise stats or specialize.
- [Treasury and budget](../mechanic/budget-treasury.md) (supporting): Salaries, office upkeep, and development costs drain cash between releases; running out ends the game.
- [Milestone unlocks](../mechanic/milestone-unlocks.md) (supporting): Bigger offices, R&D and hardware labs, and larger projects unlock as money and fans grow.
- [Reputation](../mechanic/reputation.md) (supporting): A fan count from past releases scales sales of future games.
- [Triggered event chains](../mechanic/triggered-event-chains.md) (supporting): Industry news, console launches, and studio events fire on a fixed historical timeline.
- [Modding API](../mechanic/modding-api.md) (supporting): Mods are written in JavaScript through the gdt-modAPI and shared on the Steam Workshop.
- [Advertising and awareness](../mechanic/advertising-awareness.md) (supporting): Marketing campaigns bought during development raise a game's hype, which boosts its launch sales.
- [Dated technology timeline](../mechanic/dated-tech-timeline.md) (supporting): Fictional consoles launch and retire on a fixed in-game calendar from the 1980s onward, so platform choice is a bet on a console's remaining market life.

## Backlinks (computed)

**precedent for:** [Human-calibrated customers](../opportunity/human-calibrated-customers.md), [Research by named scientists](../opportunity/scientists-not-tech-trees.md)

## Sources

- [Game Dev Tycoon](../source/src-wikipedia-game-dev-tycoon.md)

---
Provenance: created in run `2026-10-24-catalog-ge`.
