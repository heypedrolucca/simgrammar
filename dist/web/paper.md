---
title: "The Grammar of Simulation"
subtitle: "A machine-readable atlas of simulation game mechanics and the mathematical, AI, ML, and LLM results that change them"
author:
  - Yohei Nakajima
  - SimGrammar contributors
date: "2026-10-25"
version: "0.2"
dataset_sha256: "7bd89fd5e2618f6f4144cc60a1034cb081f1a456383346c8cb659e03308d167a"
bibliography: references.bib
---
## Abstract

Simulation games are built from a shared but undocumented vocabulary of rule-systems. This report makes that vocabulary explicit and machine-readable, then asks how mathematical, AI, ML, and LLM results from 2019 to 2026 change it. We decompose 174 simulation games (1968 to 2026, 31 subgenres) into 199 atomic mechanics, analyze each mechanic on its own (definition, levers, failure modes, dynamics, mathematical basis, and six anchored scores), map 45 techniques onto mechanics through 218 typed effect edges, and synthesize 42 design opportunities, each with a validation experiment and a dated, falsifiable prediction. All results are projections of a versioned dataset with provenance for every entity and a validator that keeps the report, wiki, tables, and graph consistent.

**Findings.**

1. **Simulation games are compositions of six layers**: substrate, dynamics, coupling, control, legibility, and pacing. Clustering games by the mechanics they use recovers design families (minds, planned economies, build-and-test, hands-on work, authored decisions, generated worlds) that cut across market subgenres; 14 of 16 clusters mix subgenres.
2. **The vocabulary was set early.** 68 percent of mechanics appear in a catalog game released by 2000. 34 mechanics first appear in 2010 or later, and 27.5 percent of possible mechanic pairs have ever co-occurred.
3. **Depth costs legibility.** On rubric scores from a single model rater, legibility falls as emergence potential rises (ρ = -0.42) and as compute cost rises (ρ = -0.35); emergence rises with tuning difficulty (ρ = 0.61).
4. **AI techniques target what games show and say, not what they are built from.** Exposure concentrates in narrative, control, agent, and physics mechanics. 99 mechanics, carrying 51 percent of all mechanic uses in the catalog, are affected by no technique in the set. Explanation is the rarest effect a technique has on a mechanic (5 of 218 edges).
5. **What shipped mostly stays at the edge of simulation state.** Neural rendering, asset and motion generation, and language characters for dialogue and companionship have shipped. The shipped techniques that write into game state are narrow: cached model outputs as crafting rules, language-model characters in a few titles, and learned or search-based opponents. Frame-generating world models and learned physics remain prototypes or research. Of the 34 techniques that can run during play, 10 break reproducibility outright.
6. **The best near-term opportunities keep the simulation symbolic** and let learned models read, explain, decorate, and propose through validated, logged interfaces. The highest-priority opportunity is Why-query over the simulation log.

The dataset, schemas, contract, and every projection are open for extension; the procedure for contributors, human or agent, is in `AGENTS.md`.

## 1. Introduction

A simulation game is a game whose state changes by rules the player did not author and does not fully control. The player builds a road and the traffic is the city's reply; the player sets a tax and the citizens decide whether to stay. Everything distinctive about the form follows from that gap between intent and outcome: the pleasure of watching a system respond, the frustration of not understanding why it did, and the stories players tell about runs no designer scripted.

The genre is old and large. Its lineage runs from text programs on mainframes (a grain-and-population ledger in [Hamurabi](https://simgrammar.yohei.me/game/hamurabi/), a wagon party's rations in [The Oregon Trail](https://simgrammar.yohei.me/game/oregon-trail/)) through [SimCity](https://simgrammar.yohei.me/game/simcity-1989/) and [The Sims](https://simgrammar.yohei.me/game/the-sims/) to [Dwarf Fortress](https://simgrammar.yohei.me/game/dwarf-fortress/), [Factorio](https://simgrammar.yohei.me/game/factorio/), and [EVE Online](https://simgrammar.yohei.me/game/eve-online/). Its methods are less visible than its titles. Designers share a working vocabulary (needs meters, production chains, storytellers, overlays) but no common, inspectable map of which rule-systems exist, which games combine them, how each one fails, and which are near their ceilings.

That map matters now because the ceilings are moving. For forty years the depth of a simulation game was bounded by a few constraints: how much compute a consumer machine could spend per tick, how much content a studio could author, how much hidden state a player could understand, how tightly a multiplayer game had to stay deterministic, and how believable a rule-driven agent could be. Results from 2019 to 2026 in learned world models, language-model agents, learned physics, accelerated simulation, automated design, and on-device inference press on each of those constraints, unevenly and with new costs.

This report does four things:

1. **Catalogs** 174 simulation games across 31 subgenres, from 1968 to 2026, and decomposes each into the mechanics it uses (1952 typed game-to-mechanic edges, each marked core or supporting, with implementation notes for core mechanics).
2. **Analyzes** 199 mechanics one at a time: rule-level definition, player experience, design levers, failure modes, dynamics, mathematical basis, and six anchored scores (legibility, emergence potential, authoring cost, compute cost, tuning difficulty, AI leverage).
3. **Maps** 45 mathematical, AI, ML, and LLM techniques onto those mechanics through 218 typed `affects` edges that say how each technique changes each mechanic (replaces its substrate, deepens it, enables a new form, cuts its authoring cost, explains it, tunes it, or accelerates it).
4. **Synthesizes** 42 design opportunities, each with a validation experiment a small team could run and a falsifiable prediction with a resolve-by date.

Every number in this document is rendered from the dataset at build time; the dataset hash on the title page identifies the exact version. The report, the wiki, the tables, and the graph are projections of the same YAML files, so a correction to one entity updates all of them.

## 2. Method

### 2.1 Unit of analysis: the mechanic

A **mechanic** here is a rule-system that passes four admission tests (CONTRACT.md, I12):

- **Nameable.** Designers would recognize it in games other than the one being examined.
- **Atomic.** It owns one kind of state and one update rule. If it splits into two parts that each appear without the other in shipped games, it is two mechanics.
- **Tunable.** It has at least two levers.
- **Removable.** A game could drop it and keep running.

The tests exclude two common confusions. Dynamics such as "cascading failure" or "death spiral" are outcomes of coupled mechanics, so they appear in mechanics' `dynamics` fields rather than as entities. Genre-level patterns such as "colony management" are combinations, so they appear as game decompositions or opportunities. The result sits between the MDA framework's *mechanics* layer and a designer's pattern language: concrete enough to implement, general enough to recur.

Each mechanic belongs to one of 21 families, assigned by the state it owns rather than the genre it appears in: [Weather](https://simgrammar.yohei.me/mechanic/weather/) is environment, [Labor market](https://simgrammar.yohei.me/mechanic/labor-market/) is economy, [Agent inspection](https://simgrammar.yohei.me/mechanic/agent-inspection/) is information.

### 2.2 Corpus

The game catalog was built to cover every subgenre in the vocabulary, every lineage-defining title from the 1960s onward, recent releases through 2026, research demonstrations that run as interactive simulations (such as [Generative Agents (Smallville)](https://simgrammar.yohei.me/game/generative-agents-smallville/) and [Project Sid](https://simgrammar.yohei.me/game/project-sid/)), and works included for a single mechanic (marked `boundary_case`; 21 such works). The catalog is a purposive sample, not a census: prevalence figures describe this corpus, and the earliest-appearance year of a mechanic is a lower bound on its true origin.

### 2.3 Schema and scoring

Every categorical field draws from a closed vocabulary (`vocab/`), and every ordinal field names an anchored rubric (`vocab/rubrics.yaml`). Scorers match the anchor text and take the lower anchor when between two. This trades resolution for consistency across contributors: a 3 in legibility means "understood after deliberate attention and the game's info tools" whoever assigned it. Every score in this version was assigned by one model rater (claude-opus-5-5) matching the anchor text; scores are judgments, not measurements, and the rubric for each is reproduced in the wiki.

Relations are typed edges with one owner each (`vocab/edge_types.yaml`). Inverses (which games use a mechanic, which techniques affect it) and all aggregates (prevalence, earliest appearance, clusters, technique exposure, opportunity priority) are computed by the build and never stored, so they cannot drift from the edges they summarize.

### 2.4 Evidence

Each entity carries an epistemic status. `asserted` means written from domain knowledge without a citation; `sourced` means at least one cited source supports its factual fields; `verified` requires a second, independent run. Techniques must always cite. At this version, 388 entities are sourced or verified and 71 remain asserted; the asserted ones form a public verification queue (`dist/analysis/verification-queue.csv`).

### 2.5 Production

The dataset was produced by parallel research runs, each recorded in `log/runs/` with its operator, model, method, and the proposals it could not act on. Parallel runs partitioned work by file, not by topic: taxonomy runs analyzed mechanics; catalog runs verified release facts against public sources and decomposed games; technique runs searched the 2019 to 2026 literature and developer announcements. Merge-time runs then edited entities across partitions: the synthesis run added symmetric synergy and tension edges in one pass, and a review run added mechanic tags to games after an independent review found widely shared mechanics (pause controls, placement, tech trees) under-tagged, recoded several decompositions, and tightened every prediction. Each cross-partition edit is attributed in the entity's `provenance.reviewed` list. A validator enforcing the rules in CONTRACT.md §5 gated every merge. The same procedure (AGENTS.md) is what a new contributor, human or agent, follows.

### 2.6 Limitations

- **Sampling.** Commercial, English-language, PC-centric titles are over-represented; mobile management games and non-Western simulation traditions are under-represented.
- **Scoring.** Rubric scores are single-rater judgments by one model (claude-opus-5-5), not independent expert ratings. Correlations among scores (§5.6) and between a score and the technique graph (§8.4) partly reflect that rater's internal consistency. The `verified` status and the review field exist so a second rater, human or model, can confirm or contest them.
- **Decomposition depth.** A game's mechanic list records what is present and meaningful, not a complete specification. Absence of an edge is weak evidence of absence.
- **Recency.** Technique maturity and horizon are judged as of the run date and age quickly; each technique records the sources the judgment rests on.

## 3. The catalog

The corpus spans 1968 to 2026. Its oldest entries are text programs written for teaching ([Hamurabi](https://simgrammar.yohei.me/game/hamurabi/), [The Oregon Trail](https://simgrammar.yohei.me/game/oregon-trail/), [Lemonade Stand](https://simgrammar.yohei.me/game/lemonade-stand/)) and a zero-player automaton ([Conway's Game of Life](https://simgrammar.yohei.me/game/game-of-life/)); its newest are releases from 2024 to 2026 and research demonstrations whose agents are language models.


| decade | games |
|---|---|
| 1960s | 1 |
| 1970s | 3 |
| 1980s | 7 |
| 1990s | 24 |
| 2000s | 23 |
| 2010s | 73 |
| 2020s | 43 |

*Games in the dataset by decade of first release.*


### 3.1 Lineages


| Subgenre | Games |
|---|---:|
| City builder | 29 |
| Life sim | 10 |
| Management / tycoon | 10 |
| Job sim | 8 |
| Survival sim | 8 |
| Business / economic sim | 7 |
| Factory / automation | 7 |
| Vehicle sim | 7 |
| AI-native | 6 |
| Programming sim | 6 |
| Artificial life | 5 |
| Colony sim | 5 |
| MMO world | 5 |
| Physics sandbox | 5 |
| Political sim | 5 |
| Ecosystem / evolution | 4 |
| Flight sim | 4 |
| God game | 4 |
| Grand strategy | 4 |
| Space sim | 4 |
| 4X strategy | 3 |
| Construction / engineering | 3 |
| Farming sim | 3 |
| Systemic RPG | 3 |
| Sandbox world | 3 |
| Social sim | 3 |
| Sports management | 3 |
| Transport / logistics | 3 |
| Virtual pet | 3 |
| Medical sim | 2 |
| Wargame / military sim | 2 |


Subgenre labels name design lineages, not markets. [Prison Architect](https://simgrammar.yohei.me/game/prison-architect/) is a management game by lineage whose inmates carry colony-sim needs and moods; [Kenshi](https://simgrammar.yohei.me/game/kenshi/) is an RPG whose world runs on faction and economic simulation; [The Legend of Zelda: Breath of the Wild](https://simgrammar.yohei.me/game/zelda-breath-of-the-wild/) and [Noita](https://simgrammar.yohei.me/game/noita/) are included as boundary cases because their material systems ([Material interactions](https://simgrammar.yohei.me/mechanic/material-interactions/), [Falling-sand materials](https://simgrammar.yohei.me/mechanic/falling-sand-materials/)) influenced simulation design beyond their genres. Section 5 shows that clustering games by the mechanics they actually use cuts across these labels.

### 3.2 What is simulated


| Simulated domain | Games |
|---|---:|
| Economic | 61 |
| Biological / ecological | 40 |
| Physical / mechanical | 39 |
| Social / interpersonal | 36 |
| Urban | 34 |
| Military / conflict | 30 |
| Industrial / logistics | 27 |
| Political / governance | 24 |
| Domestic / personal | 16 |
| Planetary / natural | 16 |
| Cosmic / space | 15 |
| Computational / abstract | 13 |
| Occupational | 12 |
| Medical | 6 |
| Sports | 6 |


### 3.3 How failure and story work


| Failure model | Games |
|---|---:|
| Soft / recoverable | 83 |
| Hard restart | 41 |
| None | 26 |
| Cascading collapse | 12 |
| Permadeath | 12 |



| Narrative mode | Games |
|---|---:|
| Emergent | 58 |
| None | 56 |
| Hybrid | 40 |
| Authored | 15 |
| Generative | 5 |


Generative narrative (a learned model producing story text or events at runtime) is still rare in the catalog and concentrated in recent AI-native titles:


| name | year | developer | subgenre | production tier |
|---|---|---|---|---|
| [AI Dungeon](https://simgrammar.yohei.me/game/ai-dungeon/) | 2019 | Latitude | ai-native | indie |
| [Generative Agents (Smallville)](https://simgrammar.yohei.me/game/generative-agents-smallville/) | 2023 | Stanford University and Google Research | ai-native | academic |
| [Suck Up!](https://simgrammar.yohei.me/game/suck-up/) | 2023 | Proxima Enterprises | ai-native | indie |
| [Project Sid](https://simgrammar.yohei.me/game/project-sid/) | 2024 | Altera | ai-native | academic |
| [Whispers from the Star](https://simgrammar.yohei.me/game/whispers-from-the-star/) | 2025 | Anuttacon | ai-native | aa |


### 3.4 Most emergent titles


| name | year | subgenre | mechanics | emergence | influence |
|---|---|---|---|---|---|
| [Conway's Game of Life](https://simgrammar.yohei.me/game/game-of-life/) | 1970 | artificial-life | 3 | 5 | 5 |
| [Dwarf Fortress](https://simgrammar.yohei.me/game/dwarf-fortress/) | 2006 | colony-sim | 29 | 5 | 5 |
| [EVE Online](https://simgrammar.yohei.me/game/eve-online/) | 2003 | mmo-world | 12 | 5 | 4 |
| [RimWorld](https://simgrammar.yohei.me/game/rimworld/) | 2013 | colony-sim | 24 | 5 | 4 |
| [Minecraft](https://simgrammar.yohei.me/game/minecraft/) | 2009 | sandbox-world | 15 | 4 | 5 |
| [Cities: Skylines](https://simgrammar.yohei.me/game/cities-skylines/) | 2015 | city-builder | 17 | 4 | 4 |
| [Football Manager](https://simgrammar.yohei.me/game/football-manager/) | 2004 | sports-management | 15 | 4 | 4 |
| [Ultima Online](https://simgrammar.yohei.me/game/ultima-online/) | 1997 | mmo-world | 10 | 4 | 4 |
| [Creatures](https://simgrammar.yohei.me/game/creatures/) | 1996 | artificial-life | 12 | 4 | 3 |
| [Europa Universalis IV](https://simgrammar.yohei.me/game/europa-universalis-4/) | 2013 | grand-strategy | 20 | 4 | 3 |
| [Oxygen Not Included](https://simgrammar.yohei.me/game/oxygen-not-included/) | 2017 | colony-sim | 23 | 4 | 3 |
| [Aurora 4X](https://simgrammar.yohei.me/game/aurora-4x/) | 2004 | 4x-strategy | 13 | 4 | 2 |
| [Caves of Qud](https://simgrammar.yohei.me/game/caves-of-qud/) | 2015 | rpg-sim | 9 | 4 | 2 |
| [Crusader Kings III](https://simgrammar.yohei.me/game/crusader-kings-3/) | 2020 | grand-strategy | 20 | 4 | 2 |
| [Kenshi](https://simgrammar.yohei.me/game/kenshi/) | 2013 | rpg-sim | 16 | 4 | 2 |
| [Noita](https://simgrammar.yohei.me/game/noita/) | 2019 | physics-sandbox | 11 | 4 | 2 |
| [Project Zomboid](https://simgrammar.yohei.me/game/project-zomboid/) | 2011 | survival-sim | 18 | 4 | 2 |
| [The Powder Toy](https://simgrammar.yohei.me/game/the-powder-toy/) | 2008 | physics-sandbox | 9 | 4 | 2 |
| [Sid Meier's Civilization](https://simgrammar.yohei.me/game/civilization/) | 1991 | 4x-strategy | 13 | 3 | 5 |
| [SimCity](https://simgrammar.yohei.me/game/simcity-1989/) | 1989 | city-builder | 17 | 3 | 5 |


Emergence and influence are rubric scores (`vocab/rubrics.yaml`): emergence 5 means players report histories no one could have authored; influence 5 means the game created a lineage or changed the medium.

## 4. A grammar of simulation games

### 4.1 Six layers

Decomposing the catalog suggests that every simulation game is assembled from six layers. A mechanic usually lives in one layer, and a game's character comes from which layers it invests in.

1. **Substrate: what exists.** State is held as aggregate stocks (a treasury, a population count), individual agents (a colonist with needs), fields on a grid (pollution, temperature, land value), networks (roads, pipes, social ties), or continuous bodies (a wing, a chassis). The substrate fixes the cost curve: aggregates are cheap and faceless, agents are expensive and legible, fields scale with map area, continuous physics scales with contacts and timestep. The `substrate` field on every mechanic records this (
| Substrate | Mechanics |
|---|---:|
| Rule system | 107 |
| Agent-based | 70 |
| Aggregate stocks | 69 |
| Cellular grid | 38 |
| Stochastic events | 33 |
| Network / graph | 31 |
| Continuous physics | 18 |
| Player-authored logic | 9 |
| UI layer | 9 |
| Learned model | 4 |
).
2. **Dynamics: how it changes.** Update rules form feedback loops. Most simulation games pair a reinforcing growth loop (more citizens, more taxes, more buildings) with balancing loops that resist it (congestion, pollution, unrest, raids). Difficulty is the relative strength of those loops; a death spiral is a reinforcing loop running in reverse. The `feedback` field records the dominant polarity per mechanic.
3. **Coupling: how subsystems touch.** Depth comes less from the number of systems than from how many share state. Systems couple through shared stocks (power, money, labor), shared space (a factory lowers neighboring land value), and shared agents (the same colonist hauls, eats, and grieves). [Dwarf Fortress](https://simgrammar.yohei.me/game/dwarf-fortress/) is deep because nearly everything touches nearly everything else; a game with many isolated systems feels like many small games.
4. **Control: how intent enters.** The player acts directly (an avatar, a unit), places and zones, sets parameters, issues orders that agents pick up, writes programs, or speaks. Each step away from direct control widens the *control gap*, the designed distance between what the player wants and what happens. Too narrow and the game is a toy; too wide and the player is a spectator. 
| Agency model | Games |
|---|---:|
| Zoning / placement | 70 |
| Policy / parameter | 65 |
| Direct avatar | 61 |
| Direct unit control | 48 |
| Indirect incentive | 25 |
| Design then test | 18 |
| Programmatic | 15 |
| Order queue | 12 |
| Conversational | 11 |
| Caretaking interaction | 9 |
| Supernatural intervention | 6 |

5. **Legibility: how state leaves.** Overlays, inspectors, tooltips, advisors, alerts, graphs, chronicles, and forecasts expose hidden state. This layer is what lets deep simulations ship: [RimWorld](https://simgrammar.yohei.me/game/rimworld/) itemizes every mood modifier, and Paradox games nest tooltips until each number decomposes into causes. Legibility mechanics own no simulation state of their own; they are the interface between coupling and comprehension.
6. **Pacing and stakes: when the player looks and what can be lost.** Time models (pause, speed, turns, wall clock), failure models (soft setbacks, permadeath, cascading collapse), and narrative directors decide when attention is demanded and what a mistake costs. 
| Time model | Games |
|---|---:|
| Real-time with pause | 84 |
| Real-time | 50 |
| Turn-based | 20 |
| Asynchronous persistent | 7 |
| Run on demand | 7 |
| Real-world clock | 6 |


A compact description of a simulation game is its investment profile across these layers. City builders invest in substrate (fields and networks) and legibility (overlays); colony sims in agents, coupling, and pacing (storytellers); vehicle sims in continuous substrate and direct control; programming games in control alone, with nearly no hidden state. The clustering in §5 recovers these profiles from the data without being told the subgenres.

### 4.2 The families, one at a time

Each family below is described by the state it owns, its canonical mechanics, how it characteristically fails, and what it couples to. Tables list every mechanic in the family with how many catalog games use it and its rubric scores; each mechanic's full analysis (definition, levers, failure modes, dynamics, open questions) is on its wiki page.

#### Resources and production
Owns stocks of goods and the recipes that transform them. [Production chains](https://simgrammar.yohei.me/mechanic/production-chain/) is the backbone of city builders, factory games, and colony sims alike; [Storage and buffers](https://simgrammar.yohei.me/mechanic/storage-capacity/), [Spoilage](https://simgrammar.yohei.me/mechanic/spoilage/), and [Byproducts and waste](https://simgrammar.yohei.me/mechanic/byproducts-waste/) decide whether a chain is a puzzle or a ledger. The characteristic failure is the spreadsheet: chains whose only decision is ratio arithmetic. The best implementations make chains spatial ([Conveyor transport](https://simgrammar.yohei.me/mechanic/conveyor-transport/)) or social (who does the work, and in what mood).

| name | games | legibility | emergence potential | authoring cost | compute cost | ai leverage | maturity |
|---|---|---|---|---|---|---|---|
| [Production chains](https://simgrammar.yohei.me/mechanic/production-chain/) | 38 | 3 | 3 | 2 | 2 | 3 | classic |
| [Resource extraction](https://simgrammar.yohei.me/mechanic/resource-extraction/) | 29 | 5 | 2 | 2 | 2 | 1 | classic |
| [Crop cultivation](https://simgrammar.yohei.me/mechanic/crop-cultivation/) | 25 | 4 | 3 | 3 | 2 | 2 | classic |
| [Power grid](https://simgrammar.yohei.me/mechanic/power-grid/) | 20 | 4 | 3 | 1 | 2 | 2 | classic |
| [Storage and buffers](https://simgrammar.yohei.me/mechanic/storage-capacity/) | 19 | 4 | 2 | 1 | 1 | 1 | classic |
| [Hand crafting](https://simgrammar.yohei.me/mechanic/hand-crafting/) | 17 | 4 | 2 | 3 | 1 | 4 | classic |
| [Goods consumption](https://simgrammar.yohei.me/mechanic/goods-consumption/) | 16 | 3 | 3 | 2 | 2 | 2 | classic |
| [Spoilage](https://simgrammar.yohei.me/mechanic/spoilage/) | 10 | 4 | 2 | 2 | 2 | 1 | established |
| [Renewable regrowth](https://simgrammar.yohei.me/mechanic/renewable-regrowth/) | 6 | 3 | 3 | 1 | 2 | 2 | established |
| [Deposit depletion](https://simgrammar.yohei.me/mechanic/deposit-depletion/) | 5 | 4 | 3 | 1 | 1 | 1 | classic |
| [Machine boosting](https://simgrammar.yohei.me/mechanic/machine-boosting/) | 5 | 3 | 2 | 2 | 1 | 2 | established |
| [Quality tiers](https://simgrammar.yohei.me/mechanic/quality-tiers/) | 4 | 3 | 2 | 2 | 1 | 2 | established |
| [Byproducts and waste](https://simgrammar.yohei.me/mechanic/byproducts-waste/) | 3 | 3 | 3 | 2 | 2 | 2 | established |
| [Power allocation](https://simgrammar.yohei.me/mechanic/power-allocation/) | 2 | 4 | 3 | 1 | 1 | 2 | established |


#### Logistics and networks
Owns movement across space or graphs: roads, belts, pipes, rails, transit lines, service reach. These mechanics turn production into geography, and they are where compute and legibility first bind: [Traffic congestion](https://simgrammar.yohei.me/mechanic/traffic-congestion/) is the most visible place a city builder can be wrong, and [Walker service delivery](https://simgrammar.yohei.me/mechanic/walker-service-delivery/) made service coverage legible by putting it on walking bodies. Networks couple to almost everything, so their bugs (pathfinding loops, gridlock) spread to every system they feed.

| name | games | legibility | emergence potential | authoring cost | compute cost | ai leverage | maturity |
|---|---|---|---|---|---|---|---|
| [Fluid pipe networks](https://simgrammar.yohei.me/mechanic/fluid-pipe-network/) | 12 | 3 | 3 | 1 | 3 | 3 | established |
| [Service coverage](https://simgrammar.yohei.me/mechanic/service-coverage/) | 10 | 3 | 3 | 2 | 2 | 2 | classic |
| [Vehicle routes and schedules](https://simgrammar.yohei.me/mechanic/vehicle-route-scheduling/) | 10 | 4 | 3 | 1 | 2 | 2 | classic |
| [Conveyor transport](https://simgrammar.yohei.me/mechanic/conveyor-transport/) | 9 | 4 | 3 | 1 | 3 | 2 | established |
| [Road networks](https://simgrammar.yohei.me/mechanic/road-network/) | 7 | 4 | 3 | 2 | 2 | 2 | classic |
| [Service queues](https://simgrammar.yohei.me/mechanic/service-queues/) | 7 | 4 | 3 | 2 | 2 | 2 | classic |
| [Traffic congestion](https://simgrammar.yohei.me/mechanic/traffic-congestion/) | 6 | 2 | 4 | 1 | 3 | 3 | classic |
| [Hauling jobs](https://simgrammar.yohei.me/mechanic/hauling-jobs/) | 5 | 3 | 3 | 1 | 3 | 2 | classic |
| [Public transit lines](https://simgrammar.yohei.me/mechanic/public-transit/) | 5 | 3 | 3 | 1 | 3 | 3 | established |
| [Rail signaling](https://simgrammar.yohei.me/mechanic/rail-signaling/) | 5 | 2 | 3 | 1 | 2 | 2 | classic |
| [Request-provider logistics](https://simgrammar.yohei.me/mechanic/request-provider-logistics/) | 2 | 3 | 3 | 1 | 3 | 2 | established |
| [Supply lines](https://simgrammar.yohei.me/mechanic/supply-lines/) | 2 | 3 | 3 | 1 | 2 | 2 | established |
| [Travel mode choice](https://simgrammar.yohei.me/mechanic/travel-mode-choice/) | 2 | 2 | 3 | 1 | 3 | 3 | established |
| [Walker service delivery](https://simgrammar.yohei.me/mechanic/walker-service-delivery/) | 2 | 2 | 3 | 2 | 2 | 2 | established |


#### Economy and finance
Owns money, prices, and valuation. Most games use only [Treasury and budget](https://simgrammar.yohei.me/mechanic/budget-treasury/) and [Taxation](https://simgrammar.yohei.me/mechanic/taxation/) as a scorekeeping layer; fewer simulate markets with [Supply-demand pricing](https://simgrammar.yohei.me/mechanic/supply-demand-pricing/), competitors ([Rival firms](https://simgrammar.yohei.me/mechanic/rival-firms/)), or player-made prices ([Player-driven markets](https://simgrammar.yohei.me/mechanic/player-driven-market/)). The characteristic failure is the dominant strategy: a price or loan loophole that converts the economy into an exploit, which is why economies are the first target for automated balancing (§9).

| name | games | legibility | emergence potential | authoring cost | compute cost | ai leverage | maturity |
|---|---|---|---|---|---|---|---|
| [Treasury and budget](https://simgrammar.yohei.me/mechanic/budget-treasury/) | 27 | 4 | 3 | 1 | 1 | 2 | classic |
| [Trade routes](https://simgrammar.yohei.me/mechanic/trade-routes/) | 17 | 3 | 3 | 1 | 2 | 2 | classic |
| [Contracts and orders](https://simgrammar.yohei.me/mechanic/contracts-orders/) | 16 | 4 | 2 | 2 | 1 | 3 | classic |
| [Staff hiring and rosters](https://simgrammar.yohei.me/mechanic/staff-hiring/) | 16 | 4 | 3 | 2 | 1 | 3 | classic |
| [Loans and debt](https://simgrammar.yohei.me/mechanic/loans-debt/) | 13 | 4 | 2 | 1 | 1 | 2 | classic |
| [Taxation](https://simgrammar.yohei.me/mechanic/taxation/) | 13 | 4 | 2 | 1 | 1 | 2 | classic |
| [Supply-demand pricing](https://simgrammar.yohei.me/mechanic/supply-demand-pricing/) | 10 | 4 | 3 | 2 | 2 | 2 | classic |
| [Customer value choice](https://simgrammar.yohei.me/mechanic/customer-value-choice/) | 8 | 3 | 3 | 2 | 2 | 3 | classic |
| [Rival firms](https://simgrammar.yohei.me/mechanic/rival-firms/) | 8 | 3 | 3 | 2 | 2 | 4 | classic |
| [Advertising and awareness](https://simgrammar.yohei.me/mechanic/advertising-awareness/) | 6 | 3 | 2 | 1 | 1 | 3 | classic |
| [Labor market](https://simgrammar.yohei.me/mechanic/labor-market/) | 5 | 3 | 3 | 1 | 2 | 2 | classic |
| [Land value](https://simgrammar.yohei.me/mechanic/land-value/) | 5 | 3 | 3 | 1 | 2 | 2 | classic |
| [Player-driven markets](https://simgrammar.yohei.me/mechanic/player-driven-market/) | 5 | 3 | 4 | 1 | 2 | 3 | established |
| [Auctions](https://simgrammar.yohei.me/mechanic/auctions/) | 4 | 4 | 3 | 1 | 1 | 3 | established |
| [Equity and buyouts](https://simgrammar.yohei.me/mechanic/equity-buyouts/) | 4 | 3 | 3 | 1 | 1 | 2 | established |
| [Negotiation](https://simgrammar.yohei.me/mechanic/negotiation/) | 4 | 3 | 2 | 2 | 1 | 4 | classic |
| [Product development](https://simgrammar.yohei.me/mechanic/product-development/) | 3 | 2 | 2 | 2 | 1 | 4 | established |
| [RCI demand](https://simgrammar.yohei.me/mechanic/rci-demand/) | 3 | 4 | 3 | 1 | 1 | 2 | classic |
| [Delivery-time payment](https://simgrammar.yohei.me/mechanic/delivery-time-payment/) | 2 | 3 | 2 | 2 | 1 | 1 | established |


#### Agents and behavior
Owns individual minds: needs, utilities, moods, memories, skills, schedules. [Needs decay](https://simgrammar.yohei.me/mechanic/needs-decay/) plus [Utility action selection](https://simgrammar.yohei.me/mechanic/utility-action-selection/) is the standard architecture since [The Sims](https://simgrammar.yohei.me/game/the-sims/); [Smart objects](https://simgrammar.yohei.me/mechanic/smart-objects/) moved behavior knowledge into the world so new objects bring new behaviors. Its variety is paid for in animations, thoughts, and dialogue, which is why it is among the families most exposed to language-model techniques (§8).

| name | games | legibility | emergence potential | authoring cost | compute cost | ai leverage | maturity |
|---|---|---|---|---|---|---|---|
| [Agent skills](https://simgrammar.yohei.me/mechanic/agent-skills/) | 33 | 4 | 3 | 2 | 1 | 2 | classic |
| [Needs decay](https://simgrammar.yohei.me/mechanic/needs-decay/) | 30 | 4 | 3 | 2 | 2 | 3 | classic |
| [Personality traits](https://simgrammar.yohei.me/mechanic/personality-traits/) | 25 | 4 | 3 | 3 | 1 | 3 | classic |
| [Utility action selection](https://simgrammar.yohei.me/mechanic/utility-action-selection/) | 18 | 3 | 3 | 2 | 2 | 4 | classic |
| [Memories and thoughts](https://simgrammar.yohei.me/mechanic/memories-thoughts/) | 10 | 4 | 4 | 3 | 2 | 4 | established |
| [Agent pathfinding](https://simgrammar.yohei.me/mechanic/agent-pathfinding/) | 9 | 4 | 3 | 2 | 3 | 2 | classic |
| [Daily schedules](https://simgrammar.yohei.me/mechanic/daily-schedules/) | 8 | 4 | 3 | 2 | 1 | 4 | classic |
| [Mood and breakdowns](https://simgrammar.yohei.me/mechanic/mood-breakdown/) | 8 | 3 | 4 | 3 | 1 | 3 | established |
| [Crowd preferences](https://simgrammar.yohei.me/mechanic/crowd-preferences/) | 6 | 3 | 3 | 2 | 3 | 3 | classic |
| [Work priorities](https://simgrammar.yohei.me/mechanic/work-priorities/) | 6 | 3 | 3 | 1 | 2 | 3 | established |
| [Creature learning](https://simgrammar.yohei.me/mechanic/creature-learning/) | 4 | 2 | 4 | 2 | 2 | 4 | established |
| [Smart objects](https://simgrammar.yohei.me/mechanic/smart-objects/) | 4 | 4 | 3 | 4 | 2 | 3 | classic |
| [Aspirations and wants](https://simgrammar.yohei.me/mechanic/aspiration-wants/) | 3 | 4 | 3 | 3 | 1 | 4 | established |
| [Attribute-driven match engine](https://simgrammar.yohei.me/mechanic/attribute-match-engine/) | 3 | 2 | 3 | 3 | 2 | 3 | classic |
| [Autonomy levels](https://simgrammar.yohei.me/mechanic/autonomy-levels/) | 3 | 4 | 2 | 1 | 1 | 3 | established |
| [Stress accumulation](https://simgrammar.yohei.me/mechanic/stress-accumulation/) | 2 | 3 | 4 | 2 | 1 | 3 | established |


#### Social relations
Owns ties between agents: relationship values, opinion modifiers, reputation, factions, gossip, romance, and conversation. Rule-based social systems are cheap but read as formulaic; [Social exchanges](https://simgrammar.yohei.me/mechanic/social-exchanges/) in [Prom Week](https://simgrammar.yohei.me/game/prom-week/) and [Versu](https://simgrammar.yohei.me/game/versu/) showed richer social logic is possible at high authoring cost, and [Natural-language interaction](https://simgrammar.yohei.me/mechanic/natural-language-interaction/) opened conversation as an input. The characteristic failure is the visible formula: players learn that one compliment always adds a fixed amount.

| name | games | legibility | emergence potential | authoring cost | compute cost | ai leverage | maturity |
|---|---|---|---|---|---|---|---|
| [Reputation](https://simgrammar.yohei.me/mechanic/reputation/) | 22 | 4 | 3 | 2 | 1 | 3 | classic |
| [Relationship values](https://simgrammar.yohei.me/mechanic/relationship-values/) | 21 | 4 | 4 | 2 | 2 | 3 | classic |
| [Faction diplomacy](https://simgrammar.yohei.me/mechanic/faction-diplomacy/) | 15 | 3 | 4 | 2 | 2 | 4 | classic |
| [Natural-language interaction](https://simgrammar.yohei.me/mechanic/natural-language-interaction/) | 11 | 2 | 4 | 3 | 4 | 5 | established |
| [Romance and family](https://simgrammar.yohei.me/mechanic/romance-family/) | 11 | 4 | 4 | 3 | 1 | 4 | classic |
| [Social exchanges](https://simgrammar.yohei.me/mechanic/social-exchanges/) | 7 | 3 | 4 | 4 | 2 | 4 | established |
| [Gossip propagation](https://simgrammar.yohei.me/mechanic/gossip-propagation/) | 3 | 2 | 4 | 2 | 3 | 4 | emerging |
| [Opinion modifiers](https://simgrammar.yohei.me/mechanic/opinion-modifiers/) | 2 | 4 | 3 | 2 | 2 | 3 | established |


#### Population and lineage
Owns birth, death, migration, inheritance, and structure. [Immigration by attractiveness](https://simgrammar.yohei.me/mechanic/immigration-attractiveness/) is the city builder's growth engine; [Population strata](https://simgrammar.yohei.me/mechanic/population-strata/) turns growth into progression; [Trait inheritance](https://simgrammar.yohei.me/mechanic/trait-inheritance/) and [Dynasty succession](https://simgrammar.yohei.me/mechanic/dynasty-succession/) stretch play across generations. These mechanics define the time horizon of a game more than its time model does.

| name | games | legibility | emergence potential | authoring cost | compute cost | ai leverage | maturity |
|---|---|---|---|---|---|---|---|
| [Lifecycle and aging](https://simgrammar.yohei.me/mechanic/lifecycle-aging/) | 22 | 4 | 4 | 3 | 1 | 2 | classic |
| [Population strata](https://simgrammar.yohei.me/mechanic/population-strata/) | 13 | 4 | 3 | 3 | 1 | 2 | established |
| [Trait inheritance](https://simgrammar.yohei.me/mechanic/trait-inheritance/) | 6 | 3 | 4 | 2 | 1 | 3 | established |
| [Culture and religion conversion](https://simgrammar.yohei.me/mechanic/culture-religion-conversion/) | 4 | 3 | 4 | 3 | 2 | 3 | established |
| [Immigration by attractiveness](https://simgrammar.yohei.me/mechanic/immigration-attractiveness/) | 4 | 3 | 3 | 1 | 1 | 2 | classic |
| [Dynasty succession](https://simgrammar.yohei.me/mechanic/dynasty-succession/) | 3 | 3 | 4 | 2 | 1 | 2 | established |
| [Education and workforce](https://simgrammar.yohei.me/mechanic/education-workforce/) | 3 | 3 | 3 | 1 | 1 | 2 | established |
| [Natural selection](https://simgrammar.yohei.me/mechanic/natural-selection/) | 3 | 2 | 5 | 1 | 3 | 3 | established |
| [Off-screen life progression](https://simgrammar.yohei.me/mechanic/offscreen-life-progression/) | 3 | 2 | 3 | 2 | 2 | 4 | established |


#### Governance and policy
Owns rules about rules: policies, laws, elections, interest groups, satisfaction, unrest. Policy menus ([Policy toggles](https://simgrammar.yohei.me/mechanic/policy-toggles/)) are universal; [Policy influence network](https://simgrammar.yohei.me/mechanic/policy-influence-network/) in [Democracy 4](https://simgrammar.yohei.me/game/democracy-4/) made the causal web itself the interface; [Player legislation](https://simgrammar.yohei.me/mechanic/player-legislation/) in [Eco](https://simgrammar.yohei.me/game/eco/) and [A Tale in the Desert](https://simgrammar.yohei.me/game/a-tale-in-the-desert/) let players write rules for each other. The failure is the menu: a fixed list of authored options that no player can extend.

| name | games | legibility | emergence potential | authoring cost | compute cost | ai leverage | maturity |
|---|---|---|---|---|---|---|---|
| [Policy toggles](https://simgrammar.yohei.me/mechanic/policy-toggles/) | 15 | 4 | 2 | 3 | 1 | 3 | classic |
| [Stability and unrest](https://simgrammar.yohei.me/mechanic/stability-unrest/) | 12 | 3 | 4 | 2 | 1 | 3 | classic |
| [Citizen satisfaction](https://simgrammar.yohei.me/mechanic/citizen-satisfaction/) | 10 | 3 | 3 | 2 | 1 | 3 | classic |
| [Elections](https://simgrammar.yohei.me/mechanic/elections/) | 7 | 3 | 3 | 2 | 2 | 4 | established |
| [Political capital](https://simgrammar.yohei.me/mechanic/political-capital/) | 7 | 4 | 2 | 1 | 1 | 2 | established |
| [Interest groups](https://simgrammar.yohei.me/mechanic/interest-groups/) | 6 | 3 | 4 | 3 | 2 | 4 | established |
| [Corruption leakage](https://simgrammar.yohei.me/mechanic/corruption-leakage/) | 4 | 3 | 2 | 1 | 1 | 2 | established |
| [Player legislation](https://simgrammar.yohei.me/mechanic/player-legislation/) | 2 | 3 | 4 | 1 | 1 | 4 | established |
| [Policy influence network](https://simgrammar.yohei.me/mechanic/policy-influence-network/) | 1 | 3 | 3 | 3 | 1 | 4 | emerging |


#### Space and construction
Owns layout: zoning, placement, adjacency, rooms, structure, terrain, and the scoring of player-built designs. [Zoning](https://simgrammar.yohei.me/mechanic/zoning/) is indirect construction; [Building placement](https://simgrammar.yohei.me/mechanic/free-placement/) is direct; [Procedural build assist](https://simgrammar.yohei.me/mechanic/procedural-build-assist/) sits between them, letting rough gestures produce detailed structure. [Design performance rating](https://simgrammar.yohei.me/mechanic/design-performance-rating/) closes the build-test loop in coaster, bridge, and machine builders.

| name | games | legibility | emergence potential | authoring cost | compute cost | ai leverage | maturity |
|---|---|---|---|---|---|---|---|
| [Building placement](https://simgrammar.yohei.me/mechanic/free-placement/) | 75 | 4 | 3 | 3 | 1 | 2 | classic |
| [Modular assembly](https://simgrammar.yohei.me/mechanic/modular-assembly/) | 27 | 3 | 4 | 3 | 3 | 4 | established |
| [Terraforming](https://simgrammar.yohei.me/mechanic/terraforming/) | 19 | 4 | 3 | 1 | 2 | 3 | classic |
| [Decoration and beauty](https://simgrammar.yohei.me/mechanic/decoration-beauty/) | 11 | 3 | 2 | 3 | 2 | 3 | classic |
| [Zoning](https://simgrammar.yohei.me/mechanic/zoning/) | 9 | 3 | 4 | 3 | 2 | 3 | classic |
| [Design performance rating](https://simgrammar.yohei.me/mechanic/design-performance-rating/) | 8 | 3 | 3 | 2 | 2 | 3 | established |
| [Vertical layers](https://simgrammar.yohei.me/mechanic/vertical-layers/) | 8 | 3 | 3 | 2 | 3 | 2 | classic |
| [Room recognition](https://simgrammar.yohei.me/mechanic/room-recognition/) | 6 | 4 | 3 | 2 | 2 | 3 | established |
| [Structural integrity](https://simgrammar.yohei.me/mechanic/structural-integrity/) | 5 | 3 | 4 | 2 | 2 | 3 | established |
| [Track laying](https://simgrammar.yohei.me/mechanic/track-laying/) | 5 | 4 | 3 | 2 | 1 | 2 | classic |
| [Adjacency scoring](https://simgrammar.yohei.me/mechanic/adjacency-scoring/) | 4 | 4 | 2 | 2 | 1 | 2 | established |
| [Procedural build assist](https://simgrammar.yohei.me/mechanic/procedural-build-assist/) | 2 | 4 | 2 | 3 | 2 | 4 | emerging |


#### Physics and materials
Owns continuous dynamics: rigid bodies, vehicles, flight, orbits, fluids, heat, deformation, destruction, material interactions. These are, on average, the most compute-bound mechanics in the taxonomy, and their legibility depends on how closely they match the physical intuitions players bring. The failure is the uncanny edge: a physics model accurate enough to invite intuition but wrong in the cases players probe.

| name | games | legibility | emergence potential | authoring cost | compute cost | ai leverage | maturity |
|---|---|---|---|---|---|---|---|
| [Rigid-body physics](https://simgrammar.yohei.me/mechanic/rigid-body-physics/) | 13 | 4 | 4 | 2 | 3 | 3 | classic |
| [Fluid and gas simulation](https://simgrammar.yohei.me/mechanic/fluid-gas-simulation/) | 11 | 3 | 4 | 1 | 4 | 4 | established |
| [Heat transfer](https://simgrammar.yohei.me/mechanic/heat-transfer/) | 9 | 3 | 4 | 2 | 3 | 2 | established |
| [Vehicle dynamics](https://simgrammar.yohei.me/mechanic/vehicle-dynamics/) | 9 | 3 | 2 | 3 | 2 | 2 | classic |
| [Material interactions](https://simgrammar.yohei.me/mechanic/material-interactions/) | 8 | 4 | 4 | 2 | 2 | 4 | established |
| [Flight aerodynamics](https://simgrammar.yohei.me/mechanic/flight-aerodynamics/) | 5 | 3 | 2 | 3 | 2 | 3 | classic |
| [Projectile ballistics](https://simgrammar.yohei.me/mechanic/projectile-ballistics/) | 4 | 3 | 3 | 3 | 2 | 2 | classic |
| [Falling-sand materials](https://simgrammar.yohei.me/mechanic/falling-sand-materials/) | 2 | 4 | 5 | 2 | 4 | 3 | established |
| [Orbital mechanics](https://simgrammar.yohei.me/mechanic/orbital-mechanics/) | 2 | 3 | 2 | 1 | 2 | 2 | established |
| [Terrain deformation](https://simgrammar.yohei.me/mechanic/terrain-deformation/) | 2 | 4 | 3 | 2 | 3 | 2 | established |
| [Voxel destruction](https://simgrammar.yohei.me/mechanic/voxel-destruction/) | 2 | 4 | 4 | 2 | 4 | 3 | established |
| [Soft-body deformation](https://simgrammar.yohei.me/mechanic/soft-body-deformation/) | 1 | 4 | 3 | 3 | 4 | 3 | experimental |


#### Environment and ecology
Owns the world's own processes: weather, seasons, food webs, habitats, pollution, fire, contagion, water, climate. Environmental mechanics are where simulation games most often lean on real science ([Contagion](https://simgrammar.yohei.me/mechanic/contagion/) follows compartment models; [Food web](https://simgrammar.yohei.me/mechanic/food-web/) follows predator-prey dynamics) and where calibrated learned models can substitute for hand-tuned approximations.

| name | games | legibility | emergence potential | authoring cost | compute cost | ai leverage | maturity |
|---|---|---|---|---|---|---|---|
| [Weather](https://simgrammar.yohei.me/mechanic/weather/) | 27 | 4 | 3 | 3 | 1 | 2 | classic |
| [Day-night cycle](https://simgrammar.yohei.me/mechanic/day-night-cycle/) | 20 | 5 | 2 | 2 | 1 | 2 | classic |
| [Fire spread](https://simgrammar.yohei.me/mechanic/fire-spread/) | 18 | 4 | 4 | 2 | 2 | 2 | classic |
| [Seasons](https://simgrammar.yohei.me/mechanic/seasons/) | 16 | 4 | 2 | 3 | 1 | 2 | classic |
| [Habitat suitability](https://simgrammar.yohei.me/mechanic/habitat-suitability/) | 12 | 4 | 2 | 2 | 1 | 2 | established |
| [Contagion](https://simgrammar.yohei.me/mechanic/contagion/) | 10 | 3 | 4 | 2 | 2 | 3 | established |
| [Pollution spread](https://simgrammar.yohei.me/mechanic/pollution-spread/) | 7 | 3 | 3 | 1 | 2 | 2 | classic |
| [Planetary climate](https://simgrammar.yohei.me/mechanic/planetary-climate/) | 5 | 2 | 3 | 2 | 2 | 3 | established |
| [Food web](https://simgrammar.yohei.me/mechanic/food-web/) | 4 | 2 | 4 | 3 | 2 | 3 | established |
| [Hydrology](https://simgrammar.yohei.me/mechanic/hydrology/) | 4 | 3 | 4 | 1 | 3 | 3 | established |


#### Biology and health
Owns bodies: survival meters, injuries, diagnosis, creature care, husbandry. [Survival meters](https://simgrammar.yohei.me/mechanic/survival-meters/) define a subgenre; [Injury body model](https://simgrammar.yohei.me/mechanic/injury-body-model/) tracks wounds per body part in colony sims; [Creature care](https://simgrammar.yohei.me/mechanic/creature-care/) is the oldest bond between player and simulated being.

| name | games | legibility | emergence potential | authoring cost | compute cost | ai leverage | maturity |
|---|---|---|---|---|---|---|---|
| [Survival meters](https://simgrammar.yohei.me/mechanic/survival-meters/) | 13 | 4 | 3 | 2 | 1 | 2 | classic |
| [Animal husbandry](https://simgrammar.yohei.me/mechanic/animal-husbandry/) | 9 | 4 | 3 | 3 | 2 | 2 | classic |
| [Injury body model](https://simgrammar.yohei.me/mechanic/injury-body-model/) | 7 | 3 | 4 | 2 | 2 | 2 | established |
| [Creature care](https://simgrammar.yohei.me/mechanic/creature-care/) | 6 | 4 | 2 | 4 | 1 | 4 | classic |
| [Diagnosis and treatment](https://simgrammar.yohei.me/mechanic/diagnosis-treatment/) | 3 | 3 | 2 | 3 | 1 | 4 | established |
| [Care-dependent development](https://simgrammar.yohei.me/mechanic/care-dependent-development/) | 2 | 2 | 2 | 4 | 1 | 4 | established |


#### Time and pacing
Owns the clock. [Pause and speed control](https://simgrammar.yohei.me/mechanic/variable-speed/) is near-universal in real-time management games; [Real-time clock](https://simgrammar.yohei.me/mechanic/real-time-clock/) ties play to the calendar; [Daily action budget](https://simgrammar.yohei.me/mechanic/daily-action-budget/) makes days a scarce resource; [Crisis countdown](https://simgrammar.yohei.me/mechanic/crisis-countdown/) turns the future into a deadline. Time mechanics are where multiplayer and persistence constraints bite: a shared world cannot pause.

| name | games | legibility | emergence potential | authoring cost | compute cost | ai leverage | maturity |
|---|---|---|---|---|---|---|---|
| [Pause and speed control](https://simgrammar.yohei.me/mechanic/variable-speed/) | 82 | 5 | 1 | 1 | 1 | 2 | classic |
| [Turn structure](https://simgrammar.yohei.me/mechanic/turn-structure/) | 12 | 5 | 1 | 1 | 1 | 1 | classic |
| [Crisis countdown](https://simgrammar.yohei.me/mechanic/crisis-countdown/) | 10 | 4 | 2 | 3 | 1 | 3 | established |
| [Real-time clock](https://simgrammar.yohei.me/mechanic/real-time-clock/) | 7 | 5 | 2 | 3 | 1 | 2 | classic |
| [Daily action budget](https://simgrammar.yohei.me/mechanic/daily-action-budget/) | 5 | 4 | 2 | 1 | 1 | 1 | classic |
| [Periodic ticks](https://simgrammar.yohei.me/mechanic/periodic-ticks/) | 4 | 4 | 1 | 1 | 2 | 1 | classic |


#### Information and legibility
Owns nothing in the simulation and decides whether anyone can understand it. Overlays, inspectors, tooltips, dashboards, alerts, advisors, forecasts, fog of war, scouting, and comparative histograms. This family is the counterweight to emergence and the most direct beneficiary of language models that can read state and explain it (§8).

| name | games | legibility | emergence potential | authoring cost | compute cost | ai leverage | maturity |
|---|---|---|---|---|---|---|---|
| [Fog of war](https://simgrammar.yohei.me/mechanic/fog-of-war/) | 13 | 4 | 3 | 1 | 2 | 3 | classic |
| [Stats dashboards](https://simgrammar.yohei.me/mechanic/stats-dashboards/) | 7 | 4 | 1 | 1 | 2 | 3 | classic |
| [Advisors](https://simgrammar.yohei.me/mechanic/advisors/) | 6 | 4 | 1 | 3 | 1 | 4 | classic |
| [Agent inspection](https://simgrammar.yohei.me/mechanic/agent-inspection/) | 5 | 4 | 1 | 2 | 1 | 4 | classic |
| [Data overlays](https://simgrammar.yohei.me/mechanic/data-overlays/) | 5 | 4 | 1 | 2 | 2 | 2 | classic |
| [Scouting knowledge](https://simgrammar.yohei.me/mechanic/scouting-knowledge/) | 4 | 3 | 3 | 1 | 2 | 3 | established |
| [Alerts feed](https://simgrammar.yohei.me/mechanic/alerts-feed/) | 3 | 4 | 1 | 2 | 2 | 3 | classic |
| [Causal breakdown tooltips](https://simgrammar.yohei.me/mechanic/causal-tooltips/) | 3 | 4 | 1 | 2 | 1 | 3 | established |
| [Comparative histograms](https://simgrammar.yohei.me/mechanic/comparative-histograms/) | 2 | 4 | 1 | 1 | 1 | 2 | established |
| [Forecasting](https://simgrammar.yohei.me/mechanic/forecasting/) | 2 | 4 | 1 | 1 | 1 | 4 | established |


#### Control and automation
Owns the channel from intent to action: avatars, unit commands, designations, programming, circuits, blueprints, delegation, god powers, and embodied skill. The history of the family is a steady move away from direct control toward specification: from clicking each unit to drawing zones, from wiring logic to writing code, and now toward stating intent in language.

| name | games | legibility | emergence potential | authoring cost | compute cost | ai leverage | maturity |
|---|---|---|---|---|---|---|---|
| [Direct avatar control](https://simgrammar.yohei.me/mechanic/direct-avatar/) | 31 | 5 | 2 | 4 | 2 | 3 | classic |
| [Unit commands](https://simgrammar.yohei.me/mechanic/unit-commands/) | 17 | 4 | 2 | 2 | 2 | 3 | classic |
| [Embodied skill control](https://simgrammar.yohei.me/mechanic/embodied-skill-control/) | 14 | 3 | 3 | 3 | 2 | 3 | classic |
| [Signal circuits](https://simgrammar.yohei.me/mechanic/signal-circuits/) | 12 | 3 | 3 | 1 | 2 | 3 | established |
| [Blueprints](https://simgrammar.yohei.me/mechanic/blueprints/) | 11 | 5 | 2 | 1 | 1 | 4 | established |
| [Player programming](https://simgrammar.yohei.me/mechanic/player-programming/) | 10 | 3 | 3 | 2 | 3 | 4 | established |
| [Delegation to AI managers](https://simgrammar.yohei.me/mechanic/delegation-to-ai/) | 7 | 3 | 3 | 2 | 2 | 4 | established |
| [Designation orders](https://simgrammar.yohei.me/mechanic/designation-orders/) | 5 | 4 | 3 | 1 | 2 | 3 | classic |
| [God powers](https://simgrammar.yohei.me/mechanic/god-powers/) | 5 | 4 | 3 | 3 | 2 | 3 | classic |
| [Execution budget](https://simgrammar.yohei.me/mechanic/execution-budget/) | 4 | 3 | 2 | 1 | 1 | 3 | established |
| [Programming by demonstration](https://simgrammar.yohei.me/mechanic/programming-by-demonstration/) | 2 | 4 | 2 | 2 | 1 | 4 | emerging |


#### Progression and goals
Owns what the player is working toward: tech trees, milestones, scenarios, career ladders, collections. Simulation games are often sandbox-first, and these mechanics supply direction without scripting outcomes.

| name | games | legibility | emergence potential | authoring cost | compute cost | ai leverage | maturity |
|---|---|---|---|---|---|---|---|
| [Tech tree](https://simgrammar.yohei.me/mechanic/tech-tree/) | 43 | 4 | 2 | 3 | 1 | 3 | classic |
| [Scenario objectives](https://simgrammar.yohei.me/mechanic/scenario-objectives/) | 40 | 4 | 2 | 3 | 1 | 3 | classic |
| [Milestone unlocks](https://simgrammar.yohei.me/mechanic/milestone-unlocks/) | 21 | 5 | 1 | 2 | 1 | 2 | established |
| [Career ladder](https://simgrammar.yohei.me/mechanic/career-ladder/) | 12 | 4 | 2 | 3 | 1 | 3 | classic |
| [Collection goals](https://simgrammar.yohei.me/mechanic/collection-goals/) | 7 | 5 | 1 | 3 | 1 | 2 | classic |
| [Megaproject sink](https://simgrammar.yohei.me/mechanic/megaproject-sink/) | 6 | 4 | 2 | 3 | 2 | 2 | established |
| [Dated technology timeline](https://simgrammar.yohei.me/mechanic/dated-tech-timeline/) | 4 | 4 | 2 | 2 | 1 | 2 | classic |
| [Combination discovery](https://simgrammar.yohei.me/mechanic/combination-discovery/) | 2 | 4 | 2 | 3 | 1 | 4 | established |


#### Risk and failure
Owns what goes wrong: disasters, wear, permadeath, threat scaling, crime. Failure mechanics are the main source of stakes, and [Adaptive threat scaling](https://simgrammar.yohei.me/mechanic/adaptive-threat-scaling/) is the genre's most consequential balancing decision: whether growth makes the game easier or harder.

| name | games | legibility | emergence potential | authoring cost | compute cost | ai leverage | maturity |
|---|---|---|---|---|---|---|---|
| [Permadeath](https://simgrammar.yohei.me/mechanic/permadeath/) | 20 | 5 | 3 | 1 | 1 | 2 | classic |
| [Wear and breakdown](https://simgrammar.yohei.me/mechanic/wear-breakdown/) | 20 | 4 | 3 | 2 | 2 | 2 | classic |
| [Random disasters](https://simgrammar.yohei.me/mechanic/random-disasters/) | 17 | 4 | 3 | 3 | 2 | 2 | classic |
| [Adaptive threat scaling](https://simgrammar.yohei.me/mechanic/adaptive-threat-scaling/) | 8 | 2 | 3 | 2 | 1 | 3 | established |
| [Crime and policing](https://simgrammar.yohei.me/mechanic/crime-policing/) | 5 | 3 | 3 | 2 | 2 | 2 | classic |
| [Subsystem damage](https://simgrammar.yohei.me/mechanic/subsystem-damage/) | 5 | 4 | 4 | 2 | 1 | 2 | established |
| [Loss on death](https://simgrammar.yohei.me/mechanic/loss-on-death/) | 4 | 5 | 3 | 1 | 1 | 2 | classic |
| [Board confidence](https://simgrammar.yohei.me/mechanic/board-confidence/) | 3 | 3 | 3 | 2 | 1 | 3 | classic |
| [Stimulus attraction](https://simgrammar.yohei.me/mechanic/stimulus-attraction/) | 2 | 3 | 4 | 1 | 2 | 3 | established |


#### Narrative and generation
Owns what events happen and how they are told: storytellers, dilemma cards, triggered event chains, requests, chronicles, and runtime-generated content. Emergent narrative needs both a director (what happens) and a chronicle (what it meant). This family is bounded by writing budgets, which is why it is a primary target for generative techniques and the place where their risks (inconsistency, tone, disclosure) are most visible.

| name | games | legibility | emergence potential | authoring cost | compute cost | ai leverage | maturity |
|---|---|---|---|---|---|---|---|
| [Triggered event chains](https://simgrammar.yohei.me/mechanic/triggered-event-chains/) | 17 | 3 | 3 | 5 | 2 | 4 | classic |
| [Dilemma cards](https://simgrammar.yohei.me/mechanic/dilemma-cards/) | 7 | 4 | 2 | 5 | 1 | 4 | established |
| [Generative content on demand](https://simgrammar.yohei.me/mechanic/generative-content/) | 7 | 2 | 3 | 2 | 5 | 4 | emerging |
| [Storyteller director](https://simgrammar.yohei.me/mechanic/storyteller-director/) | 3 | 3 | 4 | 3 | 1 | 4 | established |
| [Villager requests](https://simgrammar.yohei.me/mechanic/villager-requests/) | 3 | 5 | 2 | 3 | 1 | 4 | established |
| [History chronicle](https://simgrammar.yohei.me/mechanic/history-chronicle/) | 2 | 4 | 3 | 2 | 2 | 4 | established |


#### World generation
Owns initial conditions: terrain, simulated history, characters. [Simulated history generation](https://simgrammar.yohei.me/mechanic/history-generation/) in [Dwarf Fortress](https://simgrammar.yohei.me/game/dwarf-fortress/) simulates centuries of events before play, so the world has a past before the player arrives.

| name | games | legibility | emergence potential | authoring cost | compute cost | ai leverage | maturity |
|---|---|---|---|---|---|---|---|
| [Procedural terrain](https://simgrammar.yohei.me/mechanic/procedural-terrain/) | 20 | 4 | 3 | 2 | 3 | 4 | classic |
| [Procedural characters](https://simgrammar.yohei.me/mechanic/procedural-characters/) | 6 | 4 | 3 | 3 | 1 | 4 | classic |
| [Real-world data feeds](https://simgrammar.yohei.me/mechanic/real-world-data-feeds/) | 4 | 4 | 2 | 3 | 3 | 4 | established |
| [Simulated history generation](https://simgrammar.yohei.me/mechanic/history-generation/) | 2 | 2 | 5 | 3 | 4 | 4 | established |


#### Multiplayer and persistence
Owns other people: persistent worlds, organizations, content sharing, modding, asynchronous regions. These mechanics turn a simulation into a society of players, and they impose the strictest determinism and fairness constraints on everything else.

| name | games | legibility | emergence potential | authoring cost | compute cost | ai leverage | maturity |
|---|---|---|---|---|---|---|---|
| [Modding API](https://simgrammar.yohei.me/mechanic/modding-api/) | 30 | 3 | 3 | 2 | 2 | 4 | classic |
| [Content sharing](https://simgrammar.yohei.me/mechanic/content-sharing/) | 24 | 5 | 3 | 2 | 2 | 3 | established |
| [Persistent shared world](https://simgrammar.yohei.me/mechanic/persistent-world/) | 7 | 3 | 4 | 3 | 4 | 3 | classic |
| [Player organizations](https://simgrammar.yohei.me/mechanic/player-organizations/) | 5 | 4 | 4 | 1 | 1 | 3 | classic |
| [Asynchronous shared regions](https://simgrammar.yohei.me/mechanic/async-shared-region/) | 4 | 3 | 3 | 2 | 2 | 3 | established |
| [PvP security zones](https://simgrammar.yohei.me/mechanic/pvp-security-zones/) | 2 | 4 | 4 | 1 | 1 | 2 | established |
| [Seasonal world reset](https://simgrammar.yohei.me/mechanic/seasonal-world-reset/) | 2 | 5 | 2 | 2 | 1 | 2 | established |


#### Conflict and defense
Owns violence as a system: raids and operational military simulation. In most simulation games conflict is a stress test of the economy rather than the point.

| name | games | legibility | emergence potential | authoring cost | compute cost | ai leverage | maturity |
|---|---|---|---|---|---|---|---|
| [Raid defense](https://simgrammar.yohei.me/mechanic/raid-defense/) | 14 | 4 | 4 | 3 | 3 | 3 | established |
| [Statistical combat resolution](https://simgrammar.yohei.me/mechanic/stat-combat-resolution/) | 7 | 3 | 3 | 2 | 1 | 2 | classic |
| [Territorial control](https://simgrammar.yohei.me/mechanic/territorial-control/) | 6 | 3 | 4 | 2 | 2 | 2 | classic |
| [War score and peace terms](https://simgrammar.yohei.me/mechanic/war-score-peace/) | 5 | 3 | 3 | 1 | 1 | 3 | established |
| [Military operations](https://simgrammar.yohei.me/mechanic/military-operations/) | 4 | 2 | 4 | 4 | 3 | 3 | established |


#### Operation and procedure
Owns hands-on work: checklists, tool use on surfaces, diagnosis and repair, rule-checking. The job-sim boom of the 2010s and 2020s made procedure itself pleasurable when tool feedback is good.

| name | games | legibility | emergence potential | authoring cost | compute cost | ai leverage | maturity |
|---|---|---|---|---|---|---|---|
| [Procedural checklists](https://simgrammar.yohei.me/mechanic/procedural-checklists/) | 6 | 3 | 2 | 4 | 2 | 3 | established |
| [Surface work tools](https://simgrammar.yohei.me/mechanic/surface-work-tools/) | 3 | 5 | 1 | 3 | 2 | 2 | emerging |
| [Diagnose and repair](https://simgrammar.yohei.me/mechanic/diagnose-repair/) | 2 | 4 | 2 | 4 | 1 | 3 | established |
| [Rule-checking inspection](https://simgrammar.yohei.me/mechanic/rule-checking-inspection/) | 2 | 4 | 2 | 3 | 1 | 4 | established |

## 5. The structure of the design space

### 5.1 What games are made of

The average catalog game uses 11.2 mechanics (median 11). The most widely used is Pause and speed control, present in 47 percent of games. The head of the distribution is interface and structure more than simulation: time controls, placement, progression structures (tech trees, scenarios), then production, skills, avatars, and modding. The table ranks mechanics across families; §4.2 lists them within each family. The figure shows every use at once.


![Every use: the catalog as a grid](figures/viz-matrix.svg)

*Figure: Every use: the catalog as a grid. Each square is one game using one mechanic: 582 core uses (dark) and 1370 supporting uses (light). Rows are grouped into the clusters of §5.4 and columns into mechanic families. Hover to read a cell; reorder rows by release year or columns by first use. Interactive version: https://simgrammar.yohei.me/#fig-matrix*



| name | family | games | core in | earliest | legibility | emergence potential | ai leverage |
|---|---|---|---|---|---|---|---|
| [Pause and speed control](https://simgrammar.yohei.me/mechanic/variable-speed/) | time-pacing | 82 | 1 | 1970 | 5 | 1 | 2 |
| [Building placement](https://simgrammar.yohei.me/mechanic/free-placement/) | space-construction | 75 | 18 | 1970 | 4 | 3 | 2 |
| [Tech tree](https://simgrammar.yohei.me/mechanic/tech-tree/) | progression-goals | 43 | 12 | 1991 | 4 | 2 | 3 |
| [Scenario objectives](https://simgrammar.yohei.me/mechanic/scenario-objectives/) | progression-goals | 40 | 4 | 1989 | 4 | 2 | 3 |
| [Production chains](https://simgrammar.yohei.me/mechanic/production-chain/) | resources-production | 38 | 15 | 1983 | 3 | 3 | 3 |
| [Agent skills](https://simgrammar.yohei.me/mechanic/agent-skills/) | agents-behavior | 33 | 6 | 1993 | 4 | 3 | 2 |
| [Direct avatar control](https://simgrammar.yohei.me/mechanic/direct-avatar/) | control-automation | 31 | 8 | 1983 | 5 | 2 | 3 |
| [Modding API](https://simgrammar.yohei.me/mechanic/modding-api/) | multiplayer-persistence | 30 | 2 | 1995 | 3 | 3 | 4 |
| [Needs decay](https://simgrammar.yohei.me/mechanic/needs-decay/) | agents-behavior | 30 | 17 | 1985 | 4 | 3 | 3 |
| [Resource extraction](https://simgrammar.yohei.me/mechanic/resource-extraction/) | resources-production | 29 | 10 | 1982 | 5 | 2 | 1 |
| [Modular assembly](https://simgrammar.yohei.me/mechanic/modular-assembly/) | space-construction | 27 | 17 | 1993 | 3 | 4 | 4 |
| [Treasury and budget](https://simgrammar.yohei.me/mechanic/budget-treasury/) | economy-finance | 27 | 6 | 1973 | 4 | 3 | 2 |
| [Weather](https://simgrammar.yohei.me/mechanic/weather/) | environment-ecology | 27 | 4 | 1971 | 4 | 3 | 2 |
| [Crop cultivation](https://simgrammar.yohei.me/mechanic/crop-cultivation/) | resources-production | 25 | 8 | 1968 | 4 | 3 | 2 |
| [Personality traits](https://simgrammar.yohei.me/mechanic/personality-traits/) | agents-behavior | 25 | 3 | 1985 | 4 | 3 | 3 |

*Most-used mechanics across all families. Scores are rubric anchors (1-5).*


### 5.2 How the vocabulary grew


![The vocabulary, year by year](figures/viz-strata.svg)

*Figure: The vocabulary, year by year. Cumulative mechanics by the year of their first catalog game, one layer per family, oldest families at the bottom. Labels mark the years that added the most mechanics and the game that introduced most of them. Drag the year control or hover the chart to read what each year added. Interactive version: https://simgrammar.yohei.me/#fig-strata*


68 percent of mechanics appear in at least one catalog game released by 2000, and 59 percent first appear in the 1980s or 1990s (1990s the largest decade). The early vocabulary came from a short list of titles: [SimCity](https://simgrammar.yohei.me/game/simcity-1989/) (zoning, land value, overlays, disasters), [Populous](https://simgrammar.yohei.me/game/populous/) (terraforming as a god power), [Railroad Tycoon](https://simgrammar.yohei.me/game/railroad-tycoon/) and [Transport Tycoon](https://simgrammar.yohei.me/game/transport-tycoon/) (route scheduling and competitors), [Theme Park](https://simgrammar.yohei.me/game/theme-park/) and [Theme Hospital](https://simgrammar.yohei.me/game/theme-hospital/) (crowds with preferences, queues, diagnosis), [Creatures](https://simgrammar.yohei.me/game/creatures/) (learning creatures and genetics), and [The Sims](https://simgrammar.yohei.me/game/the-sims/) (smart objects).


| decade | mechanics |
|---|---|
| 1960s | 6 |
| 1970s | 9 |
| 1980s | 39 |
| 1990s | 79 |
| 2000s | 32 |
| 2010s | 30 |
| 2020s | 4 |

*Mechanics by decade of earliest appearance in the dataset (a lower bound on true origin; dataset is a sample).*


34 mechanics first appear in 2010 or later. They come mainly from four places: factory games (conveyors, request-provider logistics, machine boosting), grand strategy (dynasties, conversion, interest groups), job sims (inspection, repair, surface work), and destructible materials (soft bodies, voxels, terrain deformation).


| family | mechanic | earliest year | earliest game |
|---|---|---|---|
| Conflict & defense | [War score and peace terms](https://simgrammar.yohei.me/mechanic/war-score-peace/) | 2013 | [Europa Universalis IV](https://simgrammar.yohei.me/game/europa-universalis-4/) |
| Control & automation | [Execution budget](https://simgrammar.yohei.me/mechanic/execution-budget/) | 2014 | [Screeps](https://simgrammar.yohei.me/game/screeps/) |
| Control & automation | [Programming by demonstration](https://simgrammar.yohei.me/mechanic/programming-by-demonstration/) | 2019 | [Autonauts](https://simgrammar.yohei.me/game/autonauts/) |
| Economy & finance | [Product development](https://simgrammar.yohei.me/mechanic/product-development/) | 2012 | [Game Dev Tycoon](https://simgrammar.yohei.me/game/game-dev-tycoon/) |
| Governance & policy | [Interest groups](https://simgrammar.yohei.me/mechanic/interest-groups/) | 2013 | [Europa Universalis IV](https://simgrammar.yohei.me/game/europa-universalis-4/) |
| Governance & policy | [Political capital](https://simgrammar.yohei.me/mechanic/political-capital/) | 2013 | [Europa Universalis IV](https://simgrammar.yohei.me/game/europa-universalis-4/) |
| Governance & policy | [Policy influence network](https://simgrammar.yohei.me/mechanic/policy-influence-network/) | 2020 | [Democracy 4](https://simgrammar.yohei.me/game/democracy-4/) |
| Information & legibility | [Comparative histograms](https://simgrammar.yohei.me/mechanic/comparative-histograms/) | 2011 | [SpaceChem](https://simgrammar.yohei.me/game/spacechem/) |
| Information & legibility | [Causal breakdown tooltips](https://simgrammar.yohei.me/mechanic/causal-tooltips/) | 2013 | [Europa Universalis IV](https://simgrammar.yohei.me/game/europa-universalis-4/) |
| Logistics & networks | [Conveyor transport](https://simgrammar.yohei.me/mechanic/conveyor-transport/) | 2013 | [Factorio](https://simgrammar.yohei.me/game/factorio/) |
| Logistics & networks | [Request-provider logistics](https://simgrammar.yohei.me/mechanic/request-provider-logistics/) | 2013 | [Factorio](https://simgrammar.yohei.me/game/factorio/) |
| Logistics & networks | [Travel mode choice](https://simgrammar.yohei.me/mechanic/travel-mode-choice/) | 2015 | [Cities: Skylines](https://simgrammar.yohei.me/game/cities-skylines/) |
| Logistics & networks | [Supply lines](https://simgrammar.yohei.me/mechanic/supply-lines/) | 2016 | [Hearts of Iron IV](https://simgrammar.yohei.me/game/hearts-of-iron-4/) |
| Narrative & generation | [Generative content on demand](https://simgrammar.yohei.me/mechanic/generative-content/) | 2019 | [AI Dungeon](https://simgrammar.yohei.me/game/ai-dungeon/) |
| Operation & procedure | [Rule-checking inspection](https://simgrammar.yohei.me/mechanic/rule-checking-inspection/) | 2013 | [Papers, Please](https://simgrammar.yohei.me/game/papers-please/) |
| Operation & procedure | [Diagnose and repair](https://simgrammar.yohei.me/mechanic/diagnose-repair/) | 2018 | [PC Building Simulator](https://simgrammar.yohei.me/game/pc-building-simulator/) |
| Operation & procedure | [Surface work tools](https://simgrammar.yohei.me/mechanic/surface-work-tools/) | 2018 | [House Flipper](https://simgrammar.yohei.me/game/house-flipper/) |
| Physics & materials | [Soft-body deformation](https://simgrammar.yohei.me/mechanic/soft-body-deformation/) | 2013 | [BeamNG.drive](https://simgrammar.yohei.me/game/beamng-drive/) |
| Physics & materials | [Voxel destruction](https://simgrammar.yohei.me/mechanic/voxel-destruction/) | 2013 | [Space Engineers](https://simgrammar.yohei.me/game/space-engineers/) |
| Physics & materials | [Terrain deformation](https://simgrammar.yohei.me/mechanic/terrain-deformation/) | 2020 | [SnowRunner](https://simgrammar.yohei.me/game/snowrunner/) |
| Population & lineage | [Culture and religion conversion](https://simgrammar.yohei.me/mechanic/culture-religion-conversion/) | 2013 | [Europa Universalis IV](https://simgrammar.yohei.me/game/europa-universalis-4/) |
| Population & lineage | [Dynasty succession](https://simgrammar.yohei.me/mechanic/dynasty-succession/) | 2013 | [Europa Universalis IV](https://simgrammar.yohei.me/game/europa-universalis-4/) |
| Population & lineage | [Education and workforce](https://simgrammar.yohei.me/mechanic/education-workforce/) | 2015 | [Cities: Skylines](https://simgrammar.yohei.me/game/cities-skylines/) |
| Progression & goals | [Combination discovery](https://simgrammar.yohei.me/mechanic/combination-discovery/) | 2019 | [Noita](https://simgrammar.yohei.me/game/noita/) |
| Resources & production | [Power allocation](https://simgrammar.yohei.me/mechanic/power-allocation/) | 2012 | [FTL: Faster Than Light](https://simgrammar.yohei.me/game/ftl/) |
| Resources & production | [Renewable regrowth](https://simgrammar.yohei.me/mechanic/renewable-regrowth/) | 2012 | [Don't Starve](https://simgrammar.yohei.me/game/dont-starve/) |
| Resources & production | [Machine boosting](https://simgrammar.yohei.me/mechanic/machine-boosting/) | 2013 | [Factorio](https://simgrammar.yohei.me/game/factorio/) |
| Resources & production | [Byproducts and waste](https://simgrammar.yohei.me/mechanic/byproducts-waste/) | 2017 | [Oxygen Not Included](https://simgrammar.yohei.me/game/oxygen-not-included/) |
| Risk & failure | [Stimulus attraction](https://simgrammar.yohei.me/mechanic/stimulus-attraction/) | 2011 | [Project Zomboid](https://simgrammar.yohei.me/game/project-zomboid/) |
| Social relations | [Opinion modifiers](https://simgrammar.yohei.me/mechanic/opinion-modifiers/) | 2013 | [Europa Universalis IV](https://simgrammar.yohei.me/game/europa-universalis-4/) |
| Social relations | [Gossip propagation](https://simgrammar.yohei.me/mechanic/gossip-propagation/) | 2023 | [Generative Agents (Smallville)](https://simgrammar.yohei.me/game/generative-agents-smallville/) |
| Space & construction | [Structural integrity](https://simgrammar.yohei.me/mechanic/structural-integrity/) | 2015 | [Poly Bridge](https://simgrammar.yohei.me/game/poly-bridge/) |
| Space & construction | [Procedural build assist](https://simgrammar.yohei.me/mechanic/procedural-build-assist/) | 2020 | [Townscaper](https://simgrammar.yohei.me/game/townscaper/) |
| Time & pacing | [Crisis countdown](https://simgrammar.yohei.me/mechanic/crisis-countdown/) | 2011 | [Project Zomboid](https://simgrammar.yohei.me/game/project-zomboid/) |

*Mechanics whose earliest appearance in the dataset is 2010 or later, grouped by family.*


The dataset is a sample, so these are lower bounds on origin dates, and the pattern partly reflects which early games are canonical.

### 5.3 Which mechanics travel together

Co-occurrence lift measures how much more often two mechanics share a game than independence predicts. The strongest pairs are packages inherited from one lineage: the sports-management trio of match engine, board confidence, and negotiation; the grand-strategy package of war score, territorial control, and conversion; the SimCity core of land value, demand, and traffic; aspirations with smart objects from The Sims; care with learning from virtual pets.


| mechanic a | mechanic b | games | lift | jaccard |
|---|---|---|---|---|
| [Attribute-driven match engine](https://simgrammar.yohei.me/mechanic/attribute-match-engine/) | [Board confidence](https://simgrammar.yohei.me/mechanic/board-confidence/) | 3 | 58 | 1 |
| [Military operations](https://simgrammar.yohei.me/mechanic/military-operations/) | [Projectile ballistics](https://simgrammar.yohei.me/mechanic/projectile-ballistics/) | 4 | 43.5 | 1 |
| [Aspirations and wants](https://simgrammar.yohei.me/mechanic/aspiration-wants/) | [Smart objects](https://simgrammar.yohei.me/mechanic/smart-objects/) | 3 | 43.5 | 0.75 |
| [Attribute-driven match engine](https://simgrammar.yohei.me/mechanic/attribute-match-engine/) | [Negotiation](https://simgrammar.yohei.me/mechanic/negotiation/) | 3 | 43.5 | 0.75 |
| [Board confidence](https://simgrammar.yohei.me/mechanic/board-confidence/) | [Negotiation](https://simgrammar.yohei.me/mechanic/negotiation/) | 3 | 43.5 | 0.75 |
| [Causal breakdown tooltips](https://simgrammar.yohei.me/mechanic/causal-tooltips/) | [Culture and religion conversion](https://simgrammar.yohei.me/mechanic/culture-religion-conversion/) | 3 | 43.5 | 0.75 |
| [Culture and religion conversion](https://simgrammar.yohei.me/mechanic/culture-religion-conversion/) | [War score and peace terms](https://simgrammar.yohei.me/mechanic/war-score-peace/) | 4 | 34.8 | 0.8 |
| [Causal breakdown tooltips](https://simgrammar.yohei.me/mechanic/causal-tooltips/) | [War score and peace terms](https://simgrammar.yohei.me/mechanic/war-score-peace/) | 3 | 34.8 | 0.6 |
| [Land value](https://simgrammar.yohei.me/mechanic/land-value/) | [RCI demand](https://simgrammar.yohei.me/mechanic/rci-demand/) | 3 | 34.8 | 0.6 |
| [Land value](https://simgrammar.yohei.me/mechanic/land-value/) | [Traffic congestion](https://simgrammar.yohei.me/mechanic/traffic-congestion/) | 5 | 29 | 0.833 |
| [Territorial control](https://simgrammar.yohei.me/mechanic/territorial-control/) | [War score and peace terms](https://simgrammar.yohei.me/mechanic/war-score-peace/) | 5 | 29 | 0.833 |
| [Creature care](https://simgrammar.yohei.me/mechanic/creature-care/) | [Creature learning](https://simgrammar.yohei.me/mechanic/creature-learning/) | 4 | 29 | 0.667 |
| [Culture and religion conversion](https://simgrammar.yohei.me/mechanic/culture-religion-conversion/) | [Territorial control](https://simgrammar.yohei.me/mechanic/territorial-control/) | 4 | 29 | 0.667 |
| [Causal breakdown tooltips](https://simgrammar.yohei.me/mechanic/causal-tooltips/) | [Territorial control](https://simgrammar.yohei.me/mechanic/territorial-control/) | 3 | 29 | 0.5 |
| [RCI demand](https://simgrammar.yohei.me/mechanic/rci-demand/) | [Traffic congestion](https://simgrammar.yohei.me/mechanic/traffic-congestion/) | 3 | 29 | 0.5 |
| [Persistent shared world](https://simgrammar.yohei.me/mechanic/persistent-world/) | [Player organizations](https://simgrammar.yohei.me/mechanic/player-organizations/) | 5 | 24.86 | 0.714 |
| [Political capital](https://simgrammar.yohei.me/mechanic/political-capital/) | [War score and peace terms](https://simgrammar.yohei.me/mechanic/war-score-peace/) | 5 | 24.86 | 0.714 |
| [Culture and religion conversion](https://simgrammar.yohei.me/mechanic/culture-religion-conversion/) | [Political capital](https://simgrammar.yohei.me/mechanic/political-capital/) | 4 | 24.86 | 0.571 |
| [Smart objects](https://simgrammar.yohei.me/mechanic/smart-objects/) | [Social exchanges](https://simgrammar.yohei.me/mechanic/social-exchanges/) | 4 | 24.86 | 0.571 |
| [Aspirations and wants](https://simgrammar.yohei.me/mechanic/aspiration-wants/) | [Social exchanges](https://simgrammar.yohei.me/mechanic/social-exchanges/) | 3 | 24.86 | 0.429 |
| [Causal breakdown tooltips](https://simgrammar.yohei.me/mechanic/causal-tooltips/) | [Political capital](https://simgrammar.yohei.me/mechanic/political-capital/) | 3 | 24.86 | 0.429 |
| [Diagnosis and treatment](https://simgrammar.yohei.me/mechanic/diagnosis-treatment/) | [Service queues](https://simgrammar.yohei.me/mechanic/service-queues/) | 3 | 24.86 | 0.429 |
| [Generative content on demand](https://simgrammar.yohei.me/mechanic/generative-content/) | [Gossip propagation](https://simgrammar.yohei.me/mechanic/gossip-propagation/) | 3 | 24.86 | 0.429 |
| [Designation orders](https://simgrammar.yohei.me/mechanic/designation-orders/) | [Room recognition](https://simgrammar.yohei.me/mechanic/room-recognition/) | 4 | 23.2 | 0.571 |
| [Flight aerodynamics](https://simgrammar.yohei.me/mechanic/flight-aerodynamics/) | [Procedural checklists](https://simgrammar.yohei.me/mechanic/procedural-checklists/) | 4 | 23.2 | 0.571 |
| [Equity and buyouts](https://simgrammar.yohei.me/mechanic/equity-buyouts/) | [Rival firms](https://simgrammar.yohei.me/mechanic/rival-firms/) | 4 | 21.75 | 0.5 |
| [Corruption leakage](https://simgrammar.yohei.me/mechanic/corruption-leakage/) | [Territorial control](https://simgrammar.yohei.me/mechanic/territorial-control/) | 3 | 21.75 | 0.429 |
| [Culture and religion conversion](https://simgrammar.yohei.me/mechanic/culture-religion-conversion/) | [Interest groups](https://simgrammar.yohei.me/mechanic/interest-groups/) | 3 | 21.75 | 0.429 |
| [Land value](https://simgrammar.yohei.me/mechanic/land-value/) | [Public transit lines](https://simgrammar.yohei.me/mechanic/public-transit/) | 3 | 20.88 | 0.429 |
| [Rail signaling](https://simgrammar.yohei.me/mechanic/rail-signaling/) | [Track laying](https://simgrammar.yohei.me/mechanic/track-laying/) | 3 | 20.88 | 0.429 |

*Mechanic pairs ranked by lift (observed / expected co-occurrence across games), support >= 3 games.*


27.5 percent of possible mechanic pairs co-occur in at least one game. Most of the combinatorial space is untried, which is the subject of §5.5.

### 5.4 Families of games by what they use

Clustering games by the mechanics they use, ignoring their subgenre labels, produces 16 clusters, 14 of which mix subgenres. Each mechanic is weighted by inverse prevalence, so two games sharing a rare mechanic count as closer than two games sharing a pause button.


![A map of the design space](figures/viz-design-map.svg)

*Figure: A map of the design space. One island per cluster (14 of 16 mix subgenres). Inside an island, lines join games to their nearest neighbours by shared mechanics (inverse-prevalence weighted Jaccard, the measure behind the clustering); bridges join islands whose games are each other's nearest neighbours, wider for more links. Islands sit near the islands they most resemble. Hover a game to see its neighbours; highlight a subgenre to see it spread across islands. Interactive version: https://simgrammar.yohei.me/#fig-design-map*



| cluster | label | size | dominant subgenres | signature mechanics | members |
|---|---|---|---|---|---|
| C01 | Utility action selection + Personality traits | 31 | Management / tycoon (8), Life sim (7) | [Utility action selection](https://simgrammar.yohei.me/mechanic/utility-action-selection/), [Personality traits](https://simgrammar.yohei.me/mechanic/personality-traits/), [Staff hiring and rosters](https://simgrammar.yohei.me/mechanic/staff-hiring/), [Needs decay](https://simgrammar.yohei.me/mechanic/needs-decay/), [Agent skills](https://simgrammar.yohei.me/mechanic/agent-skills/) | [Paralives](https://simgrammar.yohei.me/game/paralives/), [Two Point Hospital](https://simgrammar.yohei.me/game/two-point-hospital/), [The Sims 4](https://simgrammar.yohei.me/game/the-sims-4/), [The Sims](https://simgrammar.yohei.me/game/the-sims/), [The Sims 3](https://simgrammar.yohei.me/game/the-sims-3/), [The Sims 2](https://simgrammar.yohei.me/game/the-sims-2/), [Theme Hospital](https://simgrammar.yohei.me/game/theme-hospital/), [inZOI](https://simgrammar.yohei.me/game/inzoi/), and 23 more |
| C02 | Production chains + Building placement | 25 | City builder (12), Factory / automation (7) | [Production chains](https://simgrammar.yohei.me/mechanic/production-chain/), [Building placement](https://simgrammar.yohei.me/mechanic/free-placement/), [Goods consumption](https://simgrammar.yohei.me/mechanic/goods-consumption/), [Storage and buffers](https://simgrammar.yohei.me/mechanic/storage-capacity/), [Trade routes](https://simgrammar.yohei.me/mechanic/trade-routes/) | [Anno 1800](https://simgrammar.yohei.me/game/anno-1800/), [Anno 117: Pax Romana](https://simgrammar.yohei.me/game/anno-117/), [Satisfactory](https://simgrammar.yohei.me/game/satisfactory/), [Farthest Frontier](https://simgrammar.yohei.me/game/farthest-frontier/), [Workers & Resources: Soviet Republic](https://simgrammar.yohei.me/game/workers-and-resources/), [Manor Lords](https://simgrammar.yohei.me/game/manor-lords/), [Caesar III](https://simgrammar.yohei.me/game/caesar-3/), [Dyson Sphere Program](https://simgrammar.yohei.me/game/dyson-sphere-program/), and 17 more |
| C03 | Embodied skill control + Weather | 14 | Vehicle sim (7), Flight sim (4) | [Embodied skill control](https://simgrammar.yohei.me/mechanic/embodied-skill-control/), [Weather](https://simgrammar.yohei.me/mechanic/weather/), [Vehicle dynamics](https://simgrammar.yohei.me/mechanic/vehicle-dynamics/), [Modding API](https://simgrammar.yohei.me/mechanic/modding-api/), [Procedural checklists](https://simgrammar.yohei.me/mechanic/procedural-checklists/) | [Gran Turismo 7](https://simgrammar.yohei.me/game/gran-turismo-7/), [Microsoft Flight Simulator 2024](https://simgrammar.yohei.me/game/microsoft-flight-simulator-2024/), [DCS World](https://simgrammar.yohei.me/game/dcs-world/), [Gran Turismo](https://simgrammar.yohei.me/game/gran-turismo/), [X-Plane](https://simgrammar.yohei.me/game/x-plane/), [Microsoft Flight Simulator (2020)](https://simgrammar.yohei.me/game/microsoft-flight-simulator-2020/), [iRacing](https://simgrammar.yohei.me/game/iracing/), [Silent Hunter III](https://simgrammar.yohei.me/game/silent-hunter-3/), and 6 more |
| C04 | Policy toggles + Stability and unrest | 13 | City builder (5), Grand strategy (4) | [Policy toggles](https://simgrammar.yohei.me/mechanic/policy-toggles/), [Stability and unrest](https://simgrammar.yohei.me/mechanic/stability-unrest/), [Interest groups](https://simgrammar.yohei.me/mechanic/interest-groups/), [Territorial control](https://simgrammar.yohei.me/mechanic/territorial-control/), [Political capital](https://simgrammar.yohei.me/mechanic/political-capital/) | [Stellaris](https://simgrammar.yohei.me/game/stellaris/), [Europa Universalis IV](https://simgrammar.yohei.me/game/europa-universalis-4/), [Tropico 6](https://simgrammar.yohei.me/game/tropico-6/), [Victoria 3](https://simgrammar.yohei.me/game/victoria-3/), [Hearts of Iron IV](https://simgrammar.yohei.me/game/hearts-of-iron-4/), [Rebel Inc.](https://simgrammar.yohei.me/game/rebel-inc/), [Frostpunk 2](https://simgrammar.yohei.me/game/frostpunk-2/), [Sid Meier's Civilization](https://simgrammar.yohei.me/game/civilization/), and 5 more |
| C05 | Hand crafting + Survival meters | 13 | Survival sim (5), Ecosystem / evolution (2) | [Hand crafting](https://simgrammar.yohei.me/mechanic/hand-crafting/), [Survival meters](https://simgrammar.yohei.me/mechanic/survival-meters/), [Crop cultivation](https://simgrammar.yohei.me/mechanic/crop-cultivation/), [Day-night cycle](https://simgrammar.yohei.me/mechanic/day-night-cycle/), [Animal husbandry](https://simgrammar.yohei.me/mechanic/animal-husbandry/) | [Don't Starve](https://simgrammar.yohei.me/game/dont-starve/), [Subnautica](https://simgrammar.yohei.me/game/subnautica/), [The Long Dark](https://simgrammar.yohei.me/game/the-long-dark/), [Project Zomboid](https://simgrammar.yohei.me/game/project-zomboid/), [Minecraft](https://simgrammar.yohei.me/game/minecraft/), [Valheim](https://simgrammar.yohei.me/game/valheim/), [Animal Crossing: New Horizons](https://simgrammar.yohei.me/game/animal-crossing-new-horizons/), [The Legend of Zelda: Breath of the Wild](https://simgrammar.yohei.me/game/zelda-breath-of-the-wild/), and 5 more |
| C06 | Player programming + Persistent shared world | 11 | Programming sim (6), MMO world (5) | [Player programming](https://simgrammar.yohei.me/mechanic/player-programming/), [Persistent shared world](https://simgrammar.yohei.me/mechanic/persistent-world/), [Execution budget](https://simgrammar.yohei.me/mechanic/execution-budget/), [Player-driven markets](https://simgrammar.yohei.me/mechanic/player-driven-market/), [Player organizations](https://simgrammar.yohei.me/mechanic/player-organizations/) | [Second Life](https://simgrammar.yohei.me/game/second-life/), [Opus Magnum](https://simgrammar.yohei.me/game/opus-magnum/), [Screeps](https://simgrammar.yohei.me/game/screeps/), [SpaceChem](https://simgrammar.yohei.me/game/spacechem/), [EVE Online](https://simgrammar.yohei.me/game/eve-online/), [The Farmer Was Replaced](https://simgrammar.yohei.me/game/the-farmer-was-replaced/), [Bitburner](https://simgrammar.yohei.me/game/bitburner/), [Autonauts](https://simgrammar.yohei.me/game/autonauts/), and 3 more |
| C07 | Rigid-body physics + Signal circuits | 11 | Physics sandbox (4), Construction / engineering (3) | [Rigid-body physics](https://simgrammar.yohei.me/mechanic/rigid-body-physics/), [Signal circuits](https://simgrammar.yohei.me/mechanic/signal-circuits/), [Material interactions](https://simgrammar.yohei.me/mechanic/material-interactions/), [Modular assembly](https://simgrammar.yohei.me/mechanic/modular-assembly/), [Modding API](https://simgrammar.yohei.me/mechanic/modding-api/) | [Besiege](https://simgrammar.yohei.me/game/besiege/), [The Incredible Machine](https://simgrammar.yohei.me/game/the-incredible-machine/), [Garry's Mod](https://simgrammar.yohei.me/game/garrys-mod/), [Space Engineers](https://simgrammar.yohei.me/game/space-engineers/), [Poly Bridge](https://simgrammar.yohei.me/game/poly-bridge/), [Teardown](https://simgrammar.yohei.me/game/teardown/), [Job Simulator](https://simgrammar.yohei.me/game/job-simulator/), [Noita](https://simgrammar.yohei.me/game/noita/), and 3 more |
| C08 | Generative content on demand + Natural-language interaction | 8 | AI-native (6), Social sim (1) | [Generative content on demand](https://simgrammar.yohei.me/mechanic/generative-content/), [Natural-language interaction](https://simgrammar.yohei.me/mechanic/natural-language-interaction/), [Relationship values](https://simgrammar.yohei.me/mechanic/relationship-values/), [Gossip propagation](https://simgrammar.yohei.me/mechanic/gossip-propagation/), [Direct avatar control](https://simgrammar.yohei.me/mechanic/direct-avatar/) | [Whispers from the Star](https://simgrammar.yohei.me/game/whispers-from-the-star/), [Suck Up!](https://simgrammar.yohei.me/game/suck-up/), [AI Dungeon](https://simgrammar.yohei.me/game/ai-dungeon/), [Where Winds Meet](https://simgrammar.yohei.me/game/where-winds-meet/), [Façade](https://simgrammar.yohei.me/game/facade/), [Generative Agents (Smallville)](https://simgrammar.yohei.me/game/generative-agents-smallville/), [Infinite Craft](https://simgrammar.yohei.me/game/infinite-craft/), [Project Sid](https://simgrammar.yohei.me/game/project-sid/) |
| C09 | Traffic congestion + Zoning | 8 | City builder (6), Transport / logistics (1) | [Traffic congestion](https://simgrammar.yohei.me/mechanic/traffic-congestion/), [Zoning](https://simgrammar.yohei.me/mechanic/zoning/), [Service coverage](https://simgrammar.yohei.me/mechanic/service-coverage/), [Land value](https://simgrammar.yohei.me/mechanic/land-value/), [Agent pathfinding](https://simgrammar.yohei.me/mechanic/agent-pathfinding/) | [SimCity 4](https://simgrammar.yohei.me/game/simcity-4/), [Cities: Skylines II](https://simgrammar.yohei.me/game/cities-skylines-2/), [SimCity 2000](https://simgrammar.yohei.me/game/simcity-2000/), [SimCity](https://simgrammar.yohei.me/game/simcity-1989/), [Cities: Skylines](https://simgrammar.yohei.me/game/cities-skylines/), [SimCity (2013)](https://simgrammar.yohei.me/game/simcity-2013/), [SimTower](https://simgrammar.yohei.me/game/simtower/), [Mini Metro](https://simgrammar.yohei.me/game/mini-metro/) |
| C10 | Habitat suitability + Terraforming | 8 | God game (3), Artificial life (2) | [Habitat suitability](https://simgrammar.yohei.me/mechanic/habitat-suitability/), [Terraforming](https://simgrammar.yohei.me/mechanic/terraforming/), [God powers](https://simgrammar.yohei.me/mechanic/god-powers/), [Natural selection](https://simgrammar.yohei.me/mechanic/natural-selection/), [Hydrology](https://simgrammar.yohei.me/mechanic/hydrology/) | [Species: Artificial Life, Real Evolution](https://simgrammar.yohei.me/game/species-alre/), [SimLife](https://simgrammar.yohei.me/game/simlife/), [Populous](https://simgrammar.yohei.me/game/populous/), [SimEarth](https://simgrammar.yohei.me/game/simearth/), [Terra Nil](https://simgrammar.yohei.me/game/terra-nil/), [From Dust](https://simgrammar.yohei.me/game/from-dust/), [Plague Inc.](https://simgrammar.yohei.me/game/plague-inc/), [Timberborn](https://simgrammar.yohei.me/game/timberborn/) |
| C11 | Procedural terrain + Heat transfer | 7 | Space sim (3), 4X strategy (1) | [Procedural terrain](https://simgrammar.yohei.me/mechanic/procedural-terrain/), [Heat transfer](https://simgrammar.yohei.me/mechanic/heat-transfer/), [Orbital mechanics](https://simgrammar.yohei.me/mechanic/orbital-mechanics/), [Modular assembly](https://simgrammar.yohei.me/mechanic/modular-assembly/), [Resource extraction](https://simgrammar.yohei.me/mechanic/resource-extraction/) | [Elite Dangerous](https://simgrammar.yohei.me/game/elite-dangerous/), [Kerbal Space Program](https://simgrammar.yohei.me/game/kerbal-space-program/), [Elite](https://simgrammar.yohei.me/game/elite/), [Spore](https://simgrammar.yohei.me/game/spore/), [Aurora 4X](https://simgrammar.yohei.me/game/aurora-4x/), [Universe Sandbox](https://simgrammar.yohei.me/game/universe-sandbox/), [Islanders](https://simgrammar.yohei.me/game/islanders/) |
| C12 | Turn structure + Random disasters | 6 | Political sim (1), Systemic RPG (1) | [Turn structure](https://simgrammar.yohei.me/mechanic/turn-structure/), [Random disasters](https://simgrammar.yohei.me/mechanic/random-disasters/), [Faction diplomacy](https://simgrammar.yohei.me/mechanic/faction-diplomacy/), [Forecasting](https://simgrammar.yohei.me/mechanic/forecasting/), [Simulated history generation](https://simgrammar.yohei.me/mechanic/history-generation/) | [The Oregon Trail](https://simgrammar.yohei.me/game/oregon-trail/), [Hamurabi](https://simgrammar.yohei.me/game/hamurabi/), [Lemonade Stand](https://simgrammar.yohei.me/game/lemonade-stand/), [Balance of Power](https://simgrammar.yohei.me/game/balance-of-power/), [Conway's Game of Life](https://simgrammar.yohei.me/game/game-of-life/), [Caves of Qud](https://simgrammar.yohei.me/game/caves-of-qud/) |
| C13 | Creature care + Creature learning | 6 | Virtual pet (3), God game (1) | [Creature care](https://simgrammar.yohei.me/mechanic/creature-care/), [Creature learning](https://simgrammar.yohei.me/mechanic/creature-learning/), [Natural-language interaction](https://simgrammar.yohei.me/mechanic/natural-language-interaction/), [Needs decay](https://simgrammar.yohei.me/mechanic/needs-decay/), [Real-time clock](https://simgrammar.yohei.me/mechanic/real-time-clock/) | [Nintendogs](https://simgrammar.yohei.me/game/nintendogs/), [Seaman](https://simgrammar.yohei.me/game/seaman/), [Creatures](https://simgrammar.yohei.me/game/creatures/), [Tamagotchi](https://simgrammar.yohei.me/game/tamagotchi/), [Little Computer People](https://simgrammar.yohei.me/game/little-computer-people/), [Black & White](https://simgrammar.yohei.me/game/black-and-white/) |
| C14 | Triggered event chains + Dilemma cards | 6 | Job sim (2), Political sim (2) | [Triggered event chains](https://simgrammar.yohei.me/mechanic/triggered-event-chains/), [Dilemma cards](https://simgrammar.yohei.me/mechanic/dilemma-cards/), [Rule-checking inspection](https://simgrammar.yohei.me/mechanic/rule-checking-inspection/), [Treasury and budget](https://simgrammar.yohei.me/mechanic/budget-treasury/), [Daily action budget](https://simgrammar.yohei.me/mechanic/daily-action-budget/) | [Papers, Please](https://simgrammar.yohei.me/game/papers-please/), [Suzerain](https://simgrammar.yohei.me/game/suzerain/), [Contraband Police](https://simgrammar.yohei.me/game/contraband-police/), [Reigns](https://simgrammar.yohei.me/game/reigns/), [This War of Mine](https://simgrammar.yohei.me/game/this-war-of-mine/), [Princess Maker 2](https://simgrammar.yohei.me/game/princess-maker-2/) |
| C15 | Surface work tools + Contracts and orders | 5 | Job sim (5) | [Surface work tools](https://simgrammar.yohei.me/mechanic/surface-work-tools/), [Contracts and orders](https://simgrammar.yohei.me/mechanic/contracts-orders/), [Diagnose and repair](https://simgrammar.yohei.me/mechanic/diagnose-repair/), [Auctions](https://simgrammar.yohei.me/mechanic/auctions/), [Direct avatar control](https://simgrammar.yohei.me/mechanic/direct-avatar/) | [House Flipper](https://simgrammar.yohei.me/game/house-flipper/), [PowerWash Simulator](https://simgrammar.yohei.me/game/powerwash-simulator/), [Car Mechanic Simulator 2021](https://simgrammar.yohei.me/game/car-mechanic-simulator-2021/), [PC Building Simulator](https://simgrammar.yohei.me/game/pc-building-simulator/), [Hardspace: Shipbreaker](https://simgrammar.yohei.me/game/hardspace-shipbreaker/) |
| C16 | Procedural build assist + Room recognition | 2 | City builder (2) | [Procedural build assist](https://simgrammar.yohei.me/mechanic/procedural-build-assist/), [Room recognition](https://simgrammar.yohei.me/mechanic/room-recognition/), [Building placement](https://simgrammar.yohei.me/mechanic/free-placement/), [Terraforming](https://simgrammar.yohei.me/mechanic/terraforming/) | [Tiny Glade](https://simgrammar.yohei.me/game/tiny-glade/), [Townscaper](https://simgrammar.yohei.me/game/townscaper/) |

*Games clustered by weighted Jaccard similarity of mechanic sets (average linkage, k=16, core weight 2.0, inverse-prevalence weighting so ubiquitous mechanics do not dominate). Signature mechanics maximize within-cluster share x log-lift. Members are ordered by centrality (mean distance to the rest of the cluster), so the first members are the most typical.*


The clusters read as design families:

- **Minds.** Life sims, colony sims, and agent-driven management share the largest cluster, built on utility action selection, personality, and needs: [The Sims](https://simgrammar.yohei.me/game/the-sims/), [RimWorld](https://simgrammar.yohei.me/game/rimworld/), [Dwarf Fortress](https://simgrammar.yohei.me/game/dwarf-fortress/), [Two Point Hospital](https://simgrammar.yohei.me/game/two-point-hospital/). Virtual pets and trainable creatures form a separate cluster on care and learning: [Creatures](https://simgrammar.yohei.me/game/creatures/), [Tamagotchi](https://simgrammar.yohei.me/game/tamagotchi/), [Black & White](https://simgrammar.yohei.me/game/black-and-white/).
- **Planned economies.** City builders split into two lineages: production chains and placement ([Anno 1800](https://simgrammar.yohei.me/game/anno-1800/), [Factorio](https://simgrammar.yohei.me/game/factorio/), [Manor Lords](https://simgrammar.yohei.me/game/manor-lords/)) and the SimCity line of zoning, land value, and traffic ([SimCity](https://simgrammar.yohei.me/game/simcity-1989/), [Cities: Skylines](https://simgrammar.yohei.me/game/cities-skylines/)). Grand strategy and political city builders cluster on policy and unrest: [Europa Universalis IV](https://simgrammar.yohei.me/game/europa-universalis-4/), [Crusader Kings III](https://simgrammar.yohei.me/game/crusader-kings-3/), [Tropico 6](https://simgrammar.yohei.me/game/tropico-6/), [Frostpunk](https://simgrammar.yohei.me/game/frostpunk/).
- **Build and test.** Physics sandboxes and construction games cluster on rigid bodies and signal circuits: [Besiege](https://simgrammar.yohei.me/game/besiege/), [Teardown](https://simgrammar.yohei.me/game/teardown/), [Poly Bridge](https://simgrammar.yohei.me/game/poly-bridge/). Programming puzzles share a cluster with persistent programmable worlds, since both are about systems the player writes and leaves running: [SpaceChem](https://simgrammar.yohei.me/game/spacechem/), [Screeps](https://simgrammar.yohei.me/game/screeps/), [EVE Online](https://simgrammar.yohei.me/game/eve-online/).
- **Hands-on work.** Job sims form their own cluster on surface tools and contracts, apart from the physics sandboxes: [PowerWash Simulator](https://simgrammar.yohei.me/game/powerwash-simulator/), [Car Mechanic Simulator 2021](https://simgrammar.yohei.me/game/car-mechanic-simulator-2021/), [PC Building Simulator](https://simgrammar.yohei.me/game/pc-building-simulator/). Vehicle and flight sims cluster on embodied skill and weather: [iRacing](https://simgrammar.yohei.me/game/iracing/), [X-Plane](https://simgrammar.yohei.me/game/x-plane/), [DCS World](https://simgrammar.yohei.me/game/dcs-world/).
- **Authored decisions.** Inspection and dilemma games cluster on event chains and dilemma cards across subgenres: [Papers, Please](https://simgrammar.yohei.me/game/papers-please/), [Reigns](https://simgrammar.yohei.me/game/reigns/), [Suzerain](https://simgrammar.yohei.me/game/suzerain/), [This War of Mine](https://simgrammar.yohei.me/game/this-war-of-mine/).
- **Turn reports.** The 1970s text sims ([Hamurabi](https://simgrammar.yohei.me/game/hamurabi/), [The Oregon Trail](https://simgrammar.yohei.me/game/oregon-trail/), [Lemonade Stand](https://simgrammar.yohei.me/game/lemonade-stand/)) form a cluster on turn structure and random events.
- **Generated worlds.** The AI-native titles cluster on generated content and natural-language interaction, apart from the life sims they resemble on the surface: [AI Dungeon](https://simgrammar.yohei.me/game/ai-dungeon/), [Infinite Craft](https://simgrammar.yohei.me/game/infinite-craft/), [Suck Up!](https://simgrammar.yohei.me/game/suck-up/).

These families match the layer profiles in §4.1: minds invest in agents and social coupling; planned economies in stocks, networks, and legibility; build-and-test games in control and continuous substrate; hands-on work and vehicle sims in direct control and physics.

### 5.5 White space

Some mechanics are individually common but rarely combined. The table lists pairs where each mechanic appears in at least eight percent of games, the two belong to different families, neither is a time-and-pacing control, they are not recorded as being in design tension, and they co-occur at most once. The figure lays every pair of common mechanics out as a plan of built and vacant lots.


![Built and vacant lots](figures/viz-vacant-lots.svg)

*Figure: Built and vacant lots. Every pair of the 41 mechanics used by at least 8 percent of games, laid out like a plan: each lot is a pair, darker lots are built more often than chance would predict, dashed lots are white space (different families, no recorded tension, co-occurring at most 1 time), and slashed lots are pairs recorded as being in design tension. Numbers mark the ten largest gaps in the white-space table. Names sit on the diagonal: read a lot by following its row and its column back to the staircase. Interactive version: https://simgrammar.yohei.me/#fig-vacant-lots*



| mechanic a | mechanic b | family a | family b | observed | expected | gap |
|---|---|---|---|---|---|---|
| [Building placement](https://simgrammar.yohei.me/mechanic/free-placement/) | [Triggered event chains](https://simgrammar.yohei.me/mechanic/triggered-event-chains/) | space-construction | narrative-generation | 1 | 7.33 | 6.33 |
| [Embodied skill control](https://simgrammar.yohei.me/mechanic/embodied-skill-control/) | [Building placement](https://simgrammar.yohei.me/mechanic/free-placement/) | control-automation | space-construction | 0 | 6.03 | 6.03 |
| [Lifecycle and aging](https://simgrammar.yohei.me/mechanic/lifecycle-aging/) | [Production chains](https://simgrammar.yohei.me/mechanic/production-chain/) | population-lineage | resources-production | 0 | 4.8 | 4.8 |
| [Permadeath](https://simgrammar.yohei.me/mechanic/permadeath/) | [Scenario objectives](https://simgrammar.yohei.me/mechanic/scenario-objectives/) | risk-failure | progression-goals | 0 | 4.6 | 4.6 |
| [Content sharing](https://simgrammar.yohei.me/mechanic/content-sharing/) | [Production chains](https://simgrammar.yohei.me/mechanic/production-chain/) | multiplayer-persistence | resources-production | 1 | 5.24 | 4.24 |
| [Relationship values](https://simgrammar.yohei.me/mechanic/relationship-values/) | [Tech tree](https://simgrammar.yohei.me/mechanic/tech-tree/) | social-relations | progression-goals | 1 | 5.19 | 4.19 |
| [Content sharing](https://simgrammar.yohei.me/mechanic/content-sharing/) | [Resource extraction](https://simgrammar.yohei.me/mechanic/resource-extraction/) | multiplayer-persistence | resources-production | 0 | 4 | 4 |
| [Hand crafting](https://simgrammar.yohei.me/mechanic/hand-crafting/) | [Scenario objectives](https://simgrammar.yohei.me/mechanic/scenario-objectives/) | resources-production | progression-goals | 0 | 3.91 | 3.91 |
| [Treasury and budget](https://simgrammar.yohei.me/mechanic/budget-treasury/) | [Crop cultivation](https://simgrammar.yohei.me/mechanic/crop-cultivation/) | economy-finance | resources-production | 0 | 3.88 | 3.88 |
| [Treasury and budget](https://simgrammar.yohei.me/mechanic/budget-treasury/) | [Direct avatar control](https://simgrammar.yohei.me/mechanic/direct-avatar/) | economy-finance | control-automation | 1 | 4.81 | 3.81 |
| [Procedural terrain](https://simgrammar.yohei.me/mechanic/procedural-terrain/) | [Scenario objectives](https://simgrammar.yohei.me/mechanic/scenario-objectives/) | world-generation | progression-goals | 1 | 4.6 | 3.6 |
| [Content sharing](https://simgrammar.yohei.me/mechanic/content-sharing/) | [Crop cultivation](https://simgrammar.yohei.me/mechanic/crop-cultivation/) | multiplayer-persistence | resources-production | 0 | 3.45 | 3.45 |
| [Faction diplomacy](https://simgrammar.yohei.me/mechanic/faction-diplomacy/) | [Scenario objectives](https://simgrammar.yohei.me/mechanic/scenario-objectives/) | social-relations | progression-goals | 0 | 3.45 | 3.45 |
| [Permadeath](https://simgrammar.yohei.me/mechanic/permadeath/) | [Production chains](https://simgrammar.yohei.me/mechanic/production-chain/) | risk-failure | resources-production | 1 | 4.37 | 3.37 |
| [Modding API](https://simgrammar.yohei.me/mechanic/modding-api/) | [Terraforming](https://simgrammar.yohei.me/mechanic/terraforming/) | multiplayer-persistence | space-construction | 0 | 3.28 | 3.28 |
| [Modular assembly](https://simgrammar.yohei.me/mechanic/modular-assembly/) | [Relationship values](https://simgrammar.yohei.me/mechanic/relationship-values/) | space-construction | social-relations | 0 | 3.26 | 3.26 |
| [Agent skills](https://simgrammar.yohei.me/mechanic/agent-skills/) | [Random disasters](https://simgrammar.yohei.me/mechanic/random-disasters/) | agents-behavior | risk-failure | 0 | 3.22 | 3.22 |
| [Embodied skill control](https://simgrammar.yohei.me/mechanic/embodied-skill-control/) | [Production chains](https://simgrammar.yohei.me/mechanic/production-chain/) | control-automation | resources-production | 0 | 3.06 | 3.06 |
| [Agent skills](https://simgrammar.yohei.me/mechanic/agent-skills/) | [Goods consumption](https://simgrammar.yohei.me/mechanic/goods-consumption/) | agents-behavior | resources-production | 0 | 3.03 | 3.03 |
| [Direct avatar control](https://simgrammar.yohei.me/mechanic/direct-avatar/) | [Trade routes](https://simgrammar.yohei.me/mechanic/trade-routes/) | control-automation | economy-finance | 0 | 3.03 | 3.03 |
| [Treasury and budget](https://simgrammar.yohei.me/mechanic/budget-treasury/) | [Storage and buffers](https://simgrammar.yohei.me/mechanic/storage-capacity/) | economy-finance | resources-production | 0 | 2.95 | 2.95 |
| [Modding API](https://simgrammar.yohei.me/mechanic/modding-api/) | [Trade routes](https://simgrammar.yohei.me/mechanic/trade-routes/) | multiplayer-persistence | economy-finance | 0 | 2.93 | 2.93 |
| [Scenario objectives](https://simgrammar.yohei.me/mechanic/scenario-objectives/) | [Triggered event chains](https://simgrammar.yohei.me/mechanic/triggered-event-chains/) | progression-goals | narrative-generation | 1 | 3.91 | 2.91 |
| [Modular assembly](https://simgrammar.yohei.me/mechanic/modular-assembly/) | [Personality traits](https://simgrammar.yohei.me/mechanic/personality-traits/) | space-construction | agents-behavior | 1 | 3.88 | 2.88 |
| [Agent skills](https://simgrammar.yohei.me/mechanic/agent-skills/) | [Policy toggles](https://simgrammar.yohei.me/mechanic/policy-toggles/) | agents-behavior | governance-policy | 0 | 2.84 | 2.84 |
| [Utility action selection](https://simgrammar.yohei.me/mechanic/utility-action-selection/) | [Weather](https://simgrammar.yohei.me/mechanic/weather/) | agents-behavior | environment-ecology | 0 | 2.79 | 2.79 |
| [Goods consumption](https://simgrammar.yohei.me/mechanic/goods-consumption/) | [Needs decay](https://simgrammar.yohei.me/mechanic/needs-decay/) | resources-production | agents-behavior | 0 | 2.76 | 2.76 |
| [Treasury and budget](https://simgrammar.yohei.me/mechanic/budget-treasury/) | [Content sharing](https://simgrammar.yohei.me/mechanic/content-sharing/) | economy-finance | multiplayer-persistence | 1 | 3.72 | 2.72 |
| [Production chains](https://simgrammar.yohei.me/mechanic/production-chain/) | [Triggered event chains](https://simgrammar.yohei.me/mechanic/triggered-event-chains/) | resources-production | narrative-generation | 1 | 3.71 | 2.71 |
| [Direct avatar control](https://simgrammar.yohei.me/mechanic/direct-avatar/) | [Policy toggles](https://simgrammar.yohei.me/mechanic/policy-toggles/) | control-automation | governance-policy | 0 | 2.67 | 2.67 |

*Pairs of common mechanics (each in >= 8% of games, different families, not marked as tension, excluding Time & pacing) that co-occur at most 1 time(s). Gap = expected - observed co-occurrence under independence.*


Some pairs are absent because they do not fit: vehicle sims have no use for free building placement. Others point at specific underexplored designs: building placement that triggers authored or generated story events; production chains whose workers age, form families, and are replaced (factory games are populated by machines or faceless workers); research trees driven by relationships between named scientists; production economies whose layouts players publish and remix. Section 9 develops several of these as opportunities.

### 5.6 The legibility frontier

Across all mechanics, legibility and emergence potential are negatively correlated (Spearman ρ = -0.42, p <0.001), and emergence potential is strongly correlated with tuning difficulty (ρ = 0.61, p <0.001). Mechanics that generate unscripted variety are harder to understand and harder to balance. Legibility also falls as compute cost rises (ρ = -0.35, p <0.001): expensive simulation tends to be hidden simulation.

Two caveats bound these numbers. First, every rubric score was assigned by one model rater (claude-opus-5-5) against written anchors, so the correlations describe that rater's reading of design knowledge, not independent expert agreement or player measurement. Second, mechanics in the legibility and time-and-pacing families sit at the bottom of the emergence scale by construction (69 percent score 1), since an overlay or a pause button generates nothing on its own; excluding them leaves the legibility-emergence correlation at ρ = -0.35, weaker but the same sign.

## 6. Five ceilings

Simulation design has been shaped less by imagination than by five constraints. Each one explains a family of conventions, and each one is the target of a different group of techniques in §7.

### 6.1 Compute per tick

A consumer machine must advance the whole simulation many times per second while rendering it. The constraint explains why city builders simulate aggregate populations with a sample of visible agents, why per-particle material simulation ([Falling-sand materials](https://simgrammar.yohei.me/mechanic/falling-sand-materials/), [Fluid and gas simulation](https://simgrammar.yohei.me/mechanic/fluid-gas-simulation/)) appears in 2D or small arenas, why late-game slowdown is a genre-wide complaint, and why [Agent pathfinding](https://simgrammar.yohei.me/mechanic/agent-pathfinding/) and [Traffic congestion](https://simgrammar.yohei.me/mechanic/traffic-congestion/) are the usual bottlenecks. Mechanics scored 4 or 5 on compute cost are the ones whose scale is capped by hardware rather than design.

**Relaxed by:** GPU-parallel and accelerated simulation, learned surrogates for physics and weather, mean-field approximations for large populations, and inference-efficient models for agent decisions.

### 6.2 Authoring cost

Every unit of variety in some mechanics must be made by hand: an animation for each interaction, a line of dialogue for each social exchange, an event for each situation, an asset for each catalog entry. Mechanics with high authoring cost are capped by budgets, and players exhaust them; this is why event decks repeat, why villagers recycle requests, and why social systems in rule-based games read as formulaic. Across mechanics, authoring cost and judged AI leverage have a Spearman correlation of 0.34 (p <0.001): the mechanics most limited by content budgets are, in the rater's judgment, the ones most open to generative techniques. Both scores come from the same model rater (§2.6), so the correlation shows a consistent reading rather than independent confirmation.

**Relaxed by:** constrained language generation for events and dialogue, text-to-3D and neural rendering for assets, learned motion for animation, and procedural generation with learned priors.

### 6.3 Legibility

Players must form a working model of why the simulation did what it did, or they experience the depth as randomness. The rubric scores show the tension (§5.6): the mechanics that generate the most unscripted variety are the hardest to understand.


![Each mechanic placed by rubric legibility (x) and emergence potential (y); area ~ number of games using it. Jitter is deterministic.](figures/legibility-vs-emergence.svg)

*Figure: Each mechanic placed by rubric legibility (x) and emergence potential (y); area ~ number of games using it. Jitter is deterministic.*


Designers have answered with a whole family of mechanics that own no simulation state ([Data overlays](https://simgrammar.yohei.me/mechanic/data-overlays/), [Causal breakdown tooltips](https://simgrammar.yohei.me/mechanic/causal-tooltips/), [Agent inspection](https://simgrammar.yohei.me/mechanic/agent-inspection/), [History chronicle](https://simgrammar.yohei.me/mechanic/history-chronicle/)). Each costs design effort and screen space, and each coupled system a game adds needs one.

**Relaxed by:** language models that read state and event logs and explain causes, forecasting by simulating futures, and learned surrogates that make expensive hidden fields cheap to visualize.

### 6.4 Determinism

Replays, lockstep multiplayer, bug reproduction, competitive leaderboards, and save integrity require that the same inputs produce the same state. [Factorio](https://simgrammar.yohei.me/game/factorio/)'s multiplayer depends on it. Determinism has kept stochastic or learned components out of authoritative game state. Of the 34 techniques here that can run during play, 10 break reproducibility outright, 16 can be made reproducible by seeding, caching, or logging their outputs, and 8 leave it intact (see `determinism_impact`).

**Relaxed by:** recording model outputs as events so replays read the log rather than re-call the model, splitting authoritative symbolic state from non-authoritative generated presentation, and constrained decoding that maps open-ended outputs into typed, validated state changes.

### 6.5 Believability of agents

Rule-driven agents are legible and cheap but shallow: their utilities are visible formulas and their speech is canned. The constraint shapes the genre's preference for many shallow agents ([Crowd preferences](https://simgrammar.yohei.me/mechanic/crowd-preferences/)) or few agents with thick systemic state ([Memories and thoughts](https://simgrammar.yohei.me/mechanic/memories-thoughts/), [Injury body model](https://simgrammar.yohei.me/mechanic/injury-body-model/)) over agents with rich minds.

**Relaxed by:** language-model agents with memory and reflection, models trained to predict human choices, and small local models that make per-agent language affordable.

### 6.6 What the ceilings imply

The five constraints do not move together. Authoring cost is being relaxed fastest, with asset, motion, and language techniques already shipped; compute is being relaxed mostly in rendering, not in simulation. Agent believability is being relaxed at a new cost in determinism and legibility. Legibility shows the widest gap between available technique and use (§8.1): explanation over structured state needs retrieval, constrained generation, and summarization, all of which exist.

## 7. The technique landscape, 2019 to 2026

### 7.1 What is in the set


| Category | Techniques |
|---|---:|
| Generative world model | 6 |
| Neural rendering & 3D generation | 5 |
| Game-theoretic solvers | 4 |
| LLM agents | 4 |
| Procedural content generation | 4 |
| Neural physics & surrogates | 3 |
| Reinforcement learning | 3 |
| Animation & motion | 2 |
| Artificial life research | 2 |
| Automated game design & playtesting | 2 |
| Differentiable & accelerated simulation | 2 |
| LLM narrative & dialogue | 2 |
| Mathematical & algorithmic discovery | 2 |
| Inference efficiency | 1 |
| Multi-agent social simulation | 1 |
| Player modeling | 1 |
| Speech & audio | 1 |


A technique enters the dataset only as a dated, citable result that changes at least one mechanic (CONTRACT.md, I12). Maturity and technology readiness are judged for deployment *in games*, not for AI in general: [Grammar-constrained decoding for valid game actions](https://simgrammar.yohei.me/technique/constrained-decoding/) is routine in software engineering but rare in shipped game runtimes, so it is scored as research for this purpose.


| Maturity in games | Techniques |
|---|---:|
| Research | 22 |
| Shipped (niche) | 12 |
| Prototype | 10 |
| Shipped (mainstream) | 1 |


Of 45 techniques, 1 is shipped as a genre norm, 12 are shipped in at least one commercial game, 10 exist as public prototypes, and 22 are research only. The shipped ones cluster in three places: rendering and assets ([Neural rendering in the graphics pipeline](https://simgrammar.yohei.me/technique/neural-rendering-shaders/), [ML reconstruction of the planet from aerial imagery](https://simgrammar.yohei.me/technique/satellite-world-reconstruction/), [Text- and image-to-3D asset generation](https://simgrammar.yohei.me/technique/text-to-3d-assets/), [Learned kinematic motion synthesis](https://simgrammar.yohei.me/technique/learned-motion-synthesis/)), language characters ([Generative agents (memory stream, reflection, planning)](https://simgrammar.yohei.me/technique/generative-agents/), [On-device small language models for characters](https://simgrammar.yohei.me/technique/on-device-language-models/), [Realtime speech-to-speech and expressive TTS for characters](https://simgrammar.yohei.me/technique/realtime-voice-models/), [LLM game master and narrative director](https://simgrammar.yohei.me/technique/llm-game-master/), [LLM-adjudicated state transitions (LLM as game mechanic)](https://simgrammar.yohei.me/technique/llm-rule-adjudication/)), and older search and learning methods ([Monte Carlo tree search for game AI](https://simgrammar.yohei.me/technique/monte-carlo-tree-search/), [Wave Function Collapse and constraint-based tile generation](https://simgrammar.yohei.me/technique/wave-function-collapse/), [Deep reinforcement learning policies for NPC opponents and navigation](https://simgrammar.yohei.me/technique/deep-rl-npc-policies/), [Agent-based automated playtesting and balancing](https://simgrammar.yohei.me/technique/automated-playtesting/)). The shipped techniques that write into authoritative state are narrow: [LLM-adjudicated state transitions (LLM as game mechanic)](https://simgrammar.yohei.me/technique/llm-rule-adjudication/) stores cached model outputs as [Infinite Craft](https://simgrammar.yohei.me/game/infinite-craft/)'s combination rules, language agents choose actions for characters in [inZOI](https://simgrammar.yohei.me/game/inzoi/) and a few AI-native titles, and search and learned policies drive opponents such as Gran Turismo Sophy in [Gran Turismo 7](https://simgrammar.yohei.me/game/gran-turismo-7/). No learned replacement for physics, fields, or the world itself is deployed in a catalog game.

### 7.2 Adoption and reception

Generative AI has moved from novelty to a measurable share of releases. Disclosures on Steam rose from about a thousand games in April 2024 [[1](#ref-src-totallyhuman-2024-steam-genai-count)] to 7,818 titles by July 2025, about 7 percent of the store, with just under a fifth of 2025 releases disclosing [[2](#ref-src-totallyhuman-2025-steam-genai-count)]; and an estimate in November 2025 put games with disclosures at roughly 8 percent of the store with about 660 million dollars in combined gross [[3](#ref-src-totallyhuman-2025-steam-ai-revenue)]. Most disclosures concern pre-generated visual assets rather than runtime systems. Valve's survey distinguishes pre-generated from live-generated content and requires the latter to describe its guardrails [[4](#ref-src-valve-2026-steamworks-content-survey)].

Developer sentiment moved the other way. In GDC's surveys, 36 percent of respondents reported using generative AI themselves in both 2025 and 2026, while the share who believe it harms the industry rose to 52 percent from 30 percent [[5](#ref-src-gdc-2025-state-of-industry), [6](#ref-src-gdc-2026-state-of-industry)]. Player reception has been mixed in visible cases: [inZOI](https://simgrammar.yohei.me/game/inzoi/) sold strongly at launch and drew negative reviews after announcing generative features [[7](#ref-src-wikipedia-inzoi)]; ARC Raiders was criticized for synthetic voice lines, some of which were later re-recorded by actors [[8](#ref-src-wikipedia-arc-raiders)].

Runtime language characters did ship. On-device small language models power simulated people in inZOI's Smart Zoi and companions in NARAKA's teammate and the PUBG Ally limited beta of June 2026 [[9](#ref-src-nvidia-2025-ace-companions), [10](#ref-src-krafton-2026-pubg-ally-beta)]; [Where Winds Meet](https://simgrammar.yohei.me/game/where-winds-meet/) discloses live NPC text and voice chat [[11](#ref-src-steam-2025-where-winds-meet)]. Audio prices for one leading realtime speech API fell from 100 and 200 dollars per million input and output tokens at launch in October 2024 to 32 and 64 dollars in August 2025, about 68 percent [[12](#ref-src-openai-2024-realtime-api), [13](#ref-src-openai-2025-gpt-realtime)], and specialized text-to-speech vendors price in cents per minute [[14](#ref-src-inworld-2026-tts-1-5)]. Cost limits frame-generating world models: the consumer Genie product grants sixty seconds of play per world, which DeepMind attributed to reaching more users on limited compute [[15](#ref-src-techcrunch-2026-project-genie)].

Among rendering techniques, neural upscaling and frame generation are the one area where learned models are a norm, with hundreds of supported titles [[16](#ref-src-nvidia-2026-dlss-4-5)]. They never touch simulation state, which is why they could spread.

### 7.3 Seven clusters

**Frame-generating world models.** [Diffusion and autoregressive neural game engines](https://simgrammar.yohei.me/technique/diffusion-game-engines/), [Genie foundation world models](https://simgrammar.yohei.me/technique/genie-world-models/), [Muse World and Human Action Model (WHAM)](https://simgrammar.yohei.me/technique/muse-wham/), and [Open real-time interactive video world models](https://simgrammar.yohei.me/technique/open-interactive-video-models/) learn to predict the next frame from recent frames and player input, so the model is the engine. They produce convincing short interactions and fail at what simulation games need most: exact persistent state, long memory, and inspectable causes. Their realistic near-term role is ideation, previsualization, and non-authoritative views (§9).

**3D, rendering, and assets.** [3D Gaussian Splatting](https://simgrammar.yohei.me/technique/gaussian-splatting/), [Prompt-to-persistent 3D world generation](https://simgrammar.yohei.me/technique/generated-3d-worlds/), [Text- and image-to-3D asset generation](https://simgrammar.yohei.me/technique/text-to-3d-assets/), [Neural rendering in the graphics pipeline](https://simgrammar.yohei.me/technique/neural-rendering-shaders/), [Real-time generative restyling of game video](https://simgrammar.yohei.me/technique/real-time-video-restyling/), and [ML reconstruction of the planet from aerial imagery](https://simgrammar.yohei.me/technique/satellite-world-reconstruction/) cut the authoring cost of what the simulation is drawn with, leaving rules untouched. They are the most mature group. Most preserve determinism; [Text- and image-to-3D asset generation](https://simgrammar.yohei.me/technique/text-to-3d-assets/) and [Real-time generative restyling of game video](https://simgrammar.yohei.me/technique/real-time-video-restyling/) are mitigable, since a generated asset or frame must be stored to be reproduced. Their main risks are provenance and reception.

**Motion.** [Learned kinematic motion synthesis](https://simgrammar.yohei.me/technique/learned-motion-synthesis/) has shipped in sports and life games; [Learned physics-based character control](https://simgrammar.yohei.me/technique/physics-based-character-control/) remains research. Both matter to simulation games because canned animation is how most agents' internal states are (poorly) displayed.

**Language agents and dialogue.** [Generative agents (memory stream, reflection, planning)](https://simgrammar.yohei.me/technique/generative-agents/), [Many-agent LLM societies](https://simgrammar.yohei.me/technique/llm-agent-societies/), [LLM models of individual human choice](https://simgrammar.yohei.me/technique/human-behavior-simulation-models/), [On-device small language models for characters](https://simgrammar.yohei.me/technique/on-device-language-models/), [Grammar-constrained decoding for valid game actions](https://simgrammar.yohei.me/technique/constrained-decoding/), [Realtime speech-to-speech and expressive TTS for characters](https://simgrammar.yohei.me/technique/realtime-voice-models/), [LLM game master and narrative director](https://simgrammar.yohei.me/technique/llm-game-master/), [LLM explanation of simulation state](https://simgrammar.yohei.me/technique/llm-explanation-of-state/), and [LLM-adjudicated state transitions (LLM as game mechanic)](https://simgrammar.yohei.me/technique/llm-rule-adjudication/) change who decides what agents do and say, who narrates, and who explains. They relax the authoring and believability ceilings at a cost in consistency. Their determinism cost varies: [Generative agents (memory stream, reflection, planning)](https://simgrammar.yohei.me/technique/generative-agents/), [Many-agent LLM societies](https://simgrammar.yohei.me/technique/llm-agent-societies/), [LLM game master and narrative director](https://simgrammar.yohei.me/technique/llm-game-master/), and [Realtime speech-to-speech and expressive TTS for characters](https://simgrammar.yohei.me/technique/realtime-voice-models/) break reproducibility; [On-device small language models for characters](https://simgrammar.yohei.me/technique/on-device-language-models/) and [LLM-adjudicated state transitions (LLM as game mechanic)](https://simgrammar.yohei.me/technique/llm-rule-adjudication/) are mitigable because a local model can be seeded and a cached rule is replayed rather than regenerated.

**Planning and game theory.** [Monte Carlo tree search for game AI](https://simgrammar.yohei.me/technique/monte-carlo-tree-search/), [Self-play planning with learned models (AlphaZero, MuZero, Dreamer)](https://simgrammar.yohei.me/technique/model-based-planning-muzero/), [Regret minimization and search for imperfect-information games](https://simgrammar.yohei.me/technique/imperfect-information-solvers/), [Language models grounded in strategic planning for negotiation games](https://simgrammar.yohei.me/technique/cicero-strategic-dialogue/), [Deep reinforcement learning policies for NPC opponents and navigation](https://simgrammar.yohei.me/technique/deep-rl-npc-policies/), and [Mean field games and mean-field learning](https://simgrammar.yohei.me/technique/mean-field-games/) produce strong opponents and equilibrium-consistent populations. Their game deployments are few because strength is rarely the design goal; believable and tunable opponents are.

**Design automation.** [Wave Function Collapse and constraint-based tile generation](https://simgrammar.yohei.me/technique/wave-function-collapse/), [Quality-diversity search (MAP-Elites) for content and balance](https://simgrammar.yohei.me/technique/quality-diversity-search/), [Learned level and map generation (PCGRL, MarioGPT, LLM generators)](https://simgrammar.yohei.me/technique/learned-level-generation/), [Automated generation of game rules and mechanics](https://simgrammar.yohei.me/technique/automated-rule-generation/), [Agent-based automated playtesting and balancing](https://simgrammar.yohei.me/technique/automated-playtesting/), [Open-ended co-generation of environments and agents](https://simgrammar.yohei.me/technique/open-ended-environment-generation/), [LLM-written skill libraries (Voyager)](https://simgrammar.yohei.me/technique/voyager-skill-libraries/), [Generalist instructable game agents (SIMA)](https://simgrammar.yohei.me/technique/generalist-game-agents/), and [LLM-guided evolutionary program search](https://simgrammar.yohei.me/technique/alphaevolve-algorithm-discovery/) mostly work on the developer's side: generating content and rules, finding exploits, and estimating difficulty. Used offline they preserve determinism. Some also run during play ([Wave Function Collapse and constraint-based tile generation](https://simgrammar.yohei.me/technique/wave-function-collapse/) in [Townscaper](https://simgrammar.yohei.me/game/townscaper/), agents that play alongside the player). Deterministic algorithms such as wave-function collapse stay reproducible there; learned generators and agents need seeds or logs.

**Simulation science.** [Massively parallel GPU simulation](https://simgrammar.yohei.me/technique/massively-parallel-simulation/), [Differentiable simulation](https://simgrammar.yohei.me/technique/differentiable-simulation/), [Graph network simulators and neural operators](https://simgrammar.yohei.me/technique/graph-network-simulators/), [Subspace neural physics and learned deformers](https://simgrammar.yohei.me/technique/subspace-neural-physics/), [Machine-learned weather forecasting](https://simgrammar.yohei.me/technique/ml-weather-models/), [Neural cellular automata](https://simgrammar.yohei.me/technique/neural-cellular-automata/), [Continuous cellular automata and foundation-model search for artificial life](https://simgrammar.yohei.me/technique/continuous-alife-and-asal/), and [Simulation-based inference for calibrating simulators](https://simgrammar.yohei.me/technique/simulation-based-inference/) come from robotics, physics, climate, and artificial life. They relax the compute ceiling and make calibration possible, and they are the least connected to game development today: an operational ML weather model runs at about a thousandth of the energy of the physics model it complements [[17](#ref-src-ecmwf-2025-aifs-operational)], yet none of these techniques is confirmed at runtime in a catalog game.


### 7.4 Landscape


| technique | category | maturity | trl | horizon | families |
|---|---|---|---|---|---|
| [Neural rendering in the graphics pipeline](https://simgrammar.yohei.me/technique/neural-rendering-shaders/) | neural-rendering-3d | shipped-mainstream | 9 | now | Control & automation (1), Environment & ecology (1), Space & construction (1) |
| [LLM game master and narrative director](https://simgrammar.yohei.me/technique/llm-game-master/) | llm-narrative-dialogue | shipped-niche | 8 | now | Narrative & generation (4), Social relations (1), World generation (1) |
| [Realtime speech-to-speech and expressive TTS for characters](https://simgrammar.yohei.me/technique/realtime-voice-models/) | speech-audio | shipped-niche | 8 | now | Social relations (2), Control & automation (1), World generation (1) |
| [ML reconstruction of the planet from aerial imagery](https://simgrammar.yohei.me/technique/satellite-world-reconstruction/) | procedural-generation | shipped-niche | 8 | now | World generation (2), Control & automation (1) |
| [Wave Function Collapse and constraint-based tile generation](https://simgrammar.yohei.me/technique/wave-function-collapse/) | procedural-generation | shipped-niche | 8 | now | Space & construction (2), World generation (1) |
| [Agent-based automated playtesting and balancing](https://simgrammar.yohei.me/technique/automated-playtesting/) | automated-game-design | shipped-niche | 7 | now | Progression & goals (3), Agents & behavior (1), Conflict & defense (1), Risk & failure (1) |
| [Deep reinforcement learning policies for NPC opponents and navigation](https://simgrammar.yohei.me/technique/deep-rl-npc-policies/) | reinforcement-learning | shipped-niche | 7 | now | Agents & behavior (1), Control & automation (1), Physics & materials (1) |
| [Generative agents (memory stream, reflection, planning)](https://simgrammar.yohei.me/technique/generative-agents/) | llm-agents | shipped-niche | 7 | now | Agents & behavior (4), Social relations (3), Information & legibility (1), Population & lineage (1) |
| [Learned kinematic motion synthesis](https://simgrammar.yohei.me/technique/learned-motion-synthesis/) | animation-motion | shipped-niche | 7 | now | Control & automation (1), Narrative & generation (1) |
| [LLM-adjudicated state transitions (LLM as game mechanic)](https://simgrammar.yohei.me/technique/llm-rule-adjudication/) | generative-world-model | shipped-niche | 7 | now | Progression & goals (2), Narrative & generation (1), Physics & materials (1), Resources & production (1) |
| [Monte Carlo tree search for game AI](https://simgrammar.yohei.me/technique/monte-carlo-tree-search/) | game-theoretic-solvers | shipped-niche | 7 | now | Agents & behavior (1), Conflict & defense (1), Control & automation (1), Economy & finance (1), Social relations (1) |
| [On-device small language models for characters](https://simgrammar.yohei.me/technique/on-device-language-models/) | inference-efficiency | shipped-niche | 7 | now | Agents & behavior (2), Control & automation (1), Information & legibility (1), Social relations (1) |
| [Text- and image-to-3D asset generation](https://simgrammar.yohei.me/technique/text-to-3d-assets/) | neural-rendering-3d | shipped-niche | 7 | now | Space & construction (2), Narrative & generation (1) |
| [Diffusion and autoregressive neural game engines](https://simgrammar.yohei.me/technique/diffusion-game-engines/) | generative-world-model | prototype | 6 | 3-5y | Physics & materials (2), Control & automation (1), Narrative & generation (1), World generation (1) |
| [3D Gaussian Splatting](https://simgrammar.yohei.me/technique/gaussian-splatting/) | neural-rendering-3d | prototype | 6 | 1-2y | Physics & materials (1), Space & construction (1) |
| [Prompt-to-persistent 3D world generation](https://simgrammar.yohei.me/technique/generated-3d-worlds/) | neural-rendering-3d | prototype | 6 | 1-2y | Physics & materials (1), Progression & goals (1), Space & construction (1), World generation (1) |
| [Genie foundation world models](https://simgrammar.yohei.me/technique/genie-world-models/) | generative-world-model | prototype | 6 | 3-5y | Control & automation (2), Narrative & generation (2), Environment & ecology (1), Physics & materials (1), World generation (1) |
| [Muse World and Human Action Model (WHAM)](https://simgrammar.yohei.me/technique/muse-wham/) | generative-world-model | prototype | 6 | 3-5y | Control & automation (1), Narrative & generation (1), Physics & materials (1) |
| [Open real-time interactive video world models](https://simgrammar.yohei.me/technique/open-interactive-video-models/) | generative-world-model | prototype | 6 | 3-5y | Physics & materials (2), Control & automation (1), Multiplayer & persistence (1), Narrative & generation (1), World generation (1) |
| [Real-time generative restyling of game video](https://simgrammar.yohei.me/technique/real-time-video-restyling/) | neural-rendering-3d | prototype | 6 | 1-2y | Narrative & generation (1), Space & construction (1) |
| [Subspace neural physics and learned deformers](https://simgrammar.yohei.me/technique/subspace-neural-physics/) | neural-physics | prototype | 6 | now | Control & automation (1), Physics & materials (1) |
| [Automated generation of game rules and mechanics](https://simgrammar.yohei.me/technique/automated-rule-generation/) | automated-game-design | prototype | 5 | 3-5y | Governance & policy (2), Narrative & generation (1), Progression & goals (1), Time & pacing (1) |
| [LLM explanation of simulation state](https://simgrammar.yohei.me/technique/llm-explanation-of-state/) | llm-narrative-dialogue | prototype | 5 | 1-2y | Information & legibility (4), Narrative & generation (1) |
| [Language models grounded in strategic planning for negotiation games](https://simgrammar.yohei.me/technique/cicero-strategic-dialogue/) | game-theoretic-solvers | research | 5 | 1-2y | Social relations (3), Conflict & defense (1), Economy & finance (1) |
| [Regret minimization and search for imperfect-information games](https://simgrammar.yohei.me/technique/imperfect-information-solvers/) | game-theoretic-solvers | research | 5 | 3-5y | Economy & finance (3), Information & legibility (2), Conflict & defense (1) |
| [Grammar-constrained decoding for valid game actions](https://simgrammar.yohei.me/technique/constrained-decoding/) | llm-agents | research | 4 | now | Narrative & generation (2), Agents & behavior (1), Governance & policy (1), Social relations (1) |
| [Generalist instructable game agents (SIMA)](https://simgrammar.yohei.me/technique/generalist-game-agents/) | llm-agents | research | 4 | 3-5y | Control & automation (3), Progression & goals (1), Social relations (1) |
| [Learned level and map generation (PCGRL, MarioGPT, LLM generators)](https://simgrammar.yohei.me/technique/learned-level-generation/) | procedural-generation | research | 4 | 1-2y | Narrative & generation (1), Progression & goals (1), Risk & failure (1), World generation (1) |
| [Many-agent LLM societies](https://simgrammar.yohei.me/technique/llm-agent-societies/) | multi-agent-social-sim | research | 4 | 3-5y | Governance & policy (3), Economy & finance (2), Multiplayer & persistence (1), Population & lineage (1), Social relations (1) |
| [Massively parallel GPU simulation](https://simgrammar.yohei.me/technique/massively-parallel-simulation/) | differentiable-simulation | research | 4 | 1-2y | Agents & behavior (3), Space & construction (2), Logistics & networks (1), Physics & materials (1), Population & lineage (1) |
| [Self-play planning with learned models (AlphaZero, MuZero, Dreamer)](https://simgrammar.yohei.me/technique/model-based-planning-muzero/) | reinforcement-learning | research | 4 | 3-5y | Agents & behavior (1), Conflict & defense (1), Economy & finance (1), Governance & policy (1), Progression & goals (1) |
| [Neural cellular automata](https://simgrammar.yohei.me/technique/neural-cellular-automata/) | artificial-life-research | research | 4 | 3-5y | Physics & materials (2), Space & construction (1), World generation (1) |
| [Open-ended co-generation of environments and agents](https://simgrammar.yohei.me/technique/open-ended-environment-generation/) | reinforcement-learning | research | 4 | 3-5y | Agents & behavior (1), Narrative & generation (1), Progression & goals (1), Risk & failure (1), World generation (1) |
| [Learned physics-based character control](https://simgrammar.yohei.me/technique/physics-based-character-control/) | animation-motion | research | 4 | 3-5y | Agents & behavior (1), Biology & health (1), Control & automation (1), Physics & materials (1) |
| [Quality-diversity search (MAP-Elites) for content and balance](https://simgrammar.yohei.me/technique/quality-diversity-search/) | procedural-generation | research | 4 | now | Space & construction (2), Economy & finance (1), Progression & goals (1), Resources & production (1), World generation (1) |
| [LLM-written skill libraries (Voyager)](https://simgrammar.yohei.me/technique/voyager-skill-libraries/) | llm-agents | research | 4 | 1-2y | Control & automation (3), Agents & behavior (1), Progression & goals (1) |
| [LLM-guided evolutionary program search](https://simgrammar.yohei.me/technique/alphaevolve-algorithm-discovery/) | math-discovery | research | 3 | 1-2y | Agents & behavior (2), Logistics & networks (2), Control & automation (1), Information & legibility (1) |
| [Continuous cellular automata and foundation-model search for artificial life](https://simgrammar.yohei.me/technique/continuous-alife-and-asal/) | artificial-life-research | research | 3 | 3-5y | Population & lineage (2), Narrative & generation (1) |
| [Differentiable simulation](https://simgrammar.yohei.me/technique/differentiable-simulation/) | differentiable-simulation | research | 3 | 3-5y | Physics & materials (3), Space & construction (2), Environment & ecology (1) |
| [Graph network simulators and neural operators](https://simgrammar.yohei.me/technique/graph-network-simulators/) | neural-physics | research | 3 | 3-5y | Physics & materials (4), Environment & ecology (1), Space & construction (1) |
| [LLM models of individual human choice](https://simgrammar.yohei.me/technique/human-behavior-simulation-models/) | player-modeling | research | 3 | 3-5y | Economy & finance (3), Agents & behavior (2), Governance & policy (2), Logistics & networks (1), Narrative & generation (1) |
| [Mean field games and mean-field learning](https://simgrammar.yohei.me/technique/mean-field-games/) | game-theoretic-solvers | research | 3 | 3-5y | Logistics & networks (3), Agents & behavior (2), Economy & finance (1) |
| [Machine-learned weather forecasting](https://simgrammar.yohei.me/technique/ml-weather-models/) | neural-physics | research | 3 | 3-5y | Environment & ecology (3), Information & legibility (1), Risk & failure (1) |
| [Physical-world foundation models](https://simgrammar.yohei.me/technique/physical-world-foundation-models/) | generative-world-model | research | 3 | 5y-plus | Physics & materials (2), Agents & behavior (1) |
| [Simulation-based inference for calibrating simulators](https://simgrammar.yohei.me/technique/simulation-based-inference/) | math-discovery | research | 3 | 1-2y | Environment & ecology (2), Agents & behavior (1), Economy & finance (1), Logistics & networks (1), Risk & failure (1) |

*Techniques ordered by game-deployment maturity and TRL, with mechanic families they affect.*

## 8. Where the techniques land

### 8.1 How techniques change mechanics

Each `affects` edge records one of seven effects. Across 218 edges the most common effect is *deepens* (74 edges): the technique makes an existing mechanic richer, larger, or more varied without changing its role. Explanation is the rarest effect (5 edges).


| effect | edges |
|---|---|
| deepens | 74 |
| enables-new | 51 |
| replaces-substrate | 33 |
| tunes | 32 |
| cuts-authoring-cost | 13 |
| accelerates | 10 |
| explains | 5 |

*How techniques change mechanics, by effect type.*


The imbalance shows where research effort points. Generating content and replacing substrates (rule-based behavior with language models, numerical physics with learned dynamics) attract most work; explaining a simulation to the person playing it attracts little, although the techniques it needs (retrieval over structured logs, constrained generation, summarization) exist.

### 8.2 Exposure by family

Technique exposure weights each `affects` edge by the technique's maturity in games and by its effect type (weights in `vocab/rubrics.yaml`), then sums over a family's mechanics.


![Where the techniques land](figures/viz-technique-flows.svg)

*Figure: Where the techniques land. Each ribbon follows one technique's edges to one mechanic family, through the kind of change it makes. Darker ribbons come from techniques that have shipped in games. Hover a technique, an effect, or a family to isolate its ribbons; switch the width to weight each edge by maturity and effect, the exposure measure of §8.2. Families with no ribbon: operation & procedure. Interactive version: https://simgrammar.yohei.me/#fig-technique-flows*



| family | mechanics | uses | mean legibility | mean emergence | mean authoring cost | mean ai leverage | technique exposure | mean exposure |
|---|---|---|---|---|---|---|---|---|
| narrative-generation | 6 | 39 | 3.5 | 2.83 | 3.33 | 4 | 8.91 | 1.49 |
| agents-behavior | 16 | 172 | 3.44 | 3.19 | 2.31 | 3.19 | 8.78 | 0.55 |
| control-automation | 11 | 118 | 3.73 | 2.55 | 2 | 3.36 | 8.71 | 0.79 |
| physics-materials | 12 | 68 | 3.5 | 3.33 | 2.17 | 2.75 | 7.43 | 0.62 |
| social-relations | 8 | 92 | 3.25 | 3.75 | 2.5 | 3.75 | 5.99 | 0.75 |
| space-construction | 12 | 179 | 3.5 | 3 | 2.33 | 2.83 | 5.54 | 0.46 |
| world-generation | 4 | 32 | 3.5 | 3.25 | 2.75 | 4 | 5.5 | 1.38 |
| progression-goals | 8 | 135 | 4.25 | 1.75 | 2.75 | 2.62 | 3.7 | 0.46 |
| economy-finance | 19 | 169 | 3.37 | 2.68 | 1.42 | 2.58 | 3.23 | 0.17 |
| information-legibility | 10 | 50 | 3.9 | 1.4 | 1.6 | 3.1 | 3.2 | 0.32 |
| governance-policy | 9 | 64 | 3.22 | 3 | 2 | 3.22 | 2.48 | 0.28 |
| environment-ecology | 10 | 123 | 3.4 | 3.1 | 2.1 | 2.4 | 2.21 | 0.22 |
| population-lineage | 9 | 61 | 3 | 3.67 | 2 | 2.56 | 1.44 | 0.16 |
| conflict-defense | 5 | 36 | 3 | 3.6 | 2.4 | 2.6 | 1.43 | 0.29 |
| logistics-networks | 14 | 84 | 3 | 3.07 | 1.29 | 2.29 | 1.12 | 0.08 |
| risk-failure | 9 | 84 | 3.67 | 3.22 | 1.78 | 2.33 | 0.96 | 0.11 |
| resources-production | 14 | 199 | 3.64 | 2.57 | 1.79 | 1.93 | 0.85 | 0.06 |
| multiplayer-persistence | 7 | 74 | 3.86 | 3.29 | 1.86 | 2.86 | 0.69 | 0.1 |
| biology-health | 6 | 40 | 3.33 | 2.67 | 3 | 3 | 0.25 | 0.04 |
| time-pacing | 6 | 120 | 4.5 | 1.5 | 1.67 | 1.67 | 0.2 | 0.03 |
| operation-procedure | 4 | 13 | 4 | 1.75 | 3.5 | 3 | 0 | 0 |

*Per mechanic family: size, total game uses, mean rubric scores, summed technique exposure (maturity x effect weights from vocab/rubrics.yaml), and exposure per mechanic. Sorted by summed exposure.*


Exposure concentrates in four families: narrative and generation, agents and behavior, control and automation, and physics and materials: the layers where content is expensive to author or where behavior is expensive to compute. Per mechanic, Narrative & generation still leads, so the concentration is not an artifact of family size. Exposure is low across the economic and logistic core of the genre (resources, logistics, economy, population) and lowest of all in operation and procedure. 99 mechanics are affected by no technique in the set, and they account for 51 percent of all game-to-mechanic uses in the catalog. Of the ten most widely used mechanics, 6 have no technique attached.

Current AI research mostly targets what a simulation game shows and says, not the rule-systems most simulation games are built from. That is partly sensible (production chains and budgets are cheap and legible already) and partly a gap: the economic core is where balance work, legibility problems, and authoring of recipes and scenarios consume design time.

### 8.3 Most exposed mechanics


| mechanic | family | technique exposure | technique count | prevalence |
|---|---|---|---|---|
| [Generative content on demand](https://simgrammar.yohei.me/mechanic/generative-content/) | narrative-generation | 5.812 | 13 | 7 |
| [Procedural terrain](https://simgrammar.yohei.me/mechanic/procedural-terrain/) | world-generation | 4.188 | 10 | 20 |
| [Utility action selection](https://simgrammar.yohei.me/mechanic/utility-action-selection/) | agents-behavior | 2.95 | 7 | 18 |
| [Rigid-body physics](https://simgrammar.yohei.me/mechanic/rigid-body-physics/) | physics-materials | 2.788 | 8 | 13 |
| [Direct avatar control](https://simgrammar.yohei.me/mechanic/direct-avatar/) | control-automation | 2.75 | 6 | 31 |
| [Natural-language interaction](https://simgrammar.yohei.me/mechanic/natural-language-interaction/) | social-relations | 2.175 | 6 | 11 |
| [Embodied skill control](https://simgrammar.yohei.me/mechanic/embodied-skill-control/) | control-automation | 1.9 | 4 | 14 |
| [Procedural build assist](https://simgrammar.yohei.me/mechanic/procedural-build-assist/) | space-construction | 1.812 | 4 | 2 |
| [Unit commands](https://simgrammar.yohei.me/mechanic/unit-commands/) | control-automation | 1.562 | 3 | 17 |
| [Vehicle dynamics](https://simgrammar.yohei.me/mechanic/vehicle-dynamics/) | physics-materials | 1.413 | 4 | 9 |
| [Decoration and beauty](https://simgrammar.yohei.me/mechanic/decoration-beauty/) | space-construction | 1.375 | 3 | 11 |
| [Modular assembly](https://simgrammar.yohei.me/mechanic/modular-assembly/) | space-construction | 1.35 | 4 | 27 |
| [Memories and thoughts](https://simgrammar.yohei.me/mechanic/memories-thoughts/) | agents-behavior | 1.312 | 2 | 10 |
| [Social exchanges](https://simgrammar.yohei.me/mechanic/social-exchanges/) | social-relations | 1.312 | 2 | 7 |
| [Scenario objectives](https://simgrammar.yohei.me/mechanic/scenario-objectives/) | progression-goals | 1.3 | 6 | 40 |
| [Agent pathfinding](https://simgrammar.yohei.me/mechanic/agent-pathfinding/) | agents-behavior | 1.25 | 4 | 9 |
| [Rival firms](https://simgrammar.yohei.me/mechanic/rival-firms/) | economy-finance | 1.188 | 4 | 8 |
| [Advisors](https://simgrammar.yohei.me/mechanic/advisors/) | information-legibility | 1.125 | 2 | 6 |
| [Delegation to AI managers](https://simgrammar.yohei.me/mechanic/delegation-to-ai/) | control-automation | 1.062 | 3 | 7 |
| [Storyteller director](https://simgrammar.yohei.me/mechanic/storyteller-director/) | narrative-generation | 1 | 2 | 3 |
| [Player legislation](https://simgrammar.yohei.me/mechanic/player-legislation/) | governance-policy | 1 | 3 | 2 |
| [Material interactions](https://simgrammar.yohei.me/mechanic/material-interactions/) | physics-materials | 0.938 | 2 | 8 |
| [Military operations](https://simgrammar.yohei.me/mechanic/military-operations/) | conflict-defense | 0.938 | 3 | 4 |
| [Soft-body deformation](https://simgrammar.yohei.me/mechanic/soft-body-deformation/) | physics-materials | 0.9 | 4 | 1 |
| [Faction diplomacy](https://simgrammar.yohei.me/mechanic/faction-diplomacy/) | social-relations | 0.812 | 2 | 15 |

*Mechanics most affected by the technique set.*


[Generative content on demand](https://simgrammar.yohei.me/mechanic/generative-content/) and [Procedural terrain](https://simgrammar.yohei.me/mechanic/procedural-terrain/) lead because many techniques generate content or worlds. [Utility action selection](https://simgrammar.yohei.me/mechanic/utility-action-selection/) is next: language models, planners, and learned policies all offer to replace the hand-written scoring at the center of agent behavior. [Rigid-body physics](https://simgrammar.yohei.me/mechanic/rigid-body-physics/) and [Direct avatar control](https://simgrammar.yohei.me/mechanic/direct-avatar/) follow, exposed mainly to frame-generating world models, which replace both with learned prediction and therefore inherit those models' consistency limits.

### 8.4 Judgment versus evidence

Each mechanic carries a judged `ai_leverage` score. It correlates with technique exposure at ρ = 0.53. This is a consistency check, not independent agreement: the same model rater scored leverage, wrote the technique `affects` edges, and judged technique maturity (§2.6). The leverage-gap table lists where they disagree: mechanics judged highly open to AI that no technique in the set yet addresses.


| mechanic | family | ai leverage | technique exposure | prevalence | gap |
|---|---|---|---|---|---|
| [Modding API](https://simgrammar.yohei.me/mechanic/modding-api/) | multiplayer-persistence | 4 | 0 | 30 | 0.8 |
| [Blueprints](https://simgrammar.yohei.me/mechanic/blueprints/) | control-automation | 4 | 0 | 11 | 0.8 |
| [Romance and family](https://simgrammar.yohei.me/mechanic/romance-family/) | social-relations | 4 | 0 | 11 | 0.8 |
| [Creature care](https://simgrammar.yohei.me/mechanic/creature-care/) | biology-health | 4 | 0 | 6 | 0.8 |
| [Diagnosis and treatment](https://simgrammar.yohei.me/mechanic/diagnosis-treatment/) | biology-health | 4 | 0 | 3 | 0.8 |
| [Product development](https://simgrammar.yohei.me/mechanic/product-development/) | economy-finance | 4 | 0 | 3 | 0.8 |
| [Care-dependent development](https://simgrammar.yohei.me/mechanic/care-dependent-development/) | biology-health | 4 | 0 | 2 | 0.8 |
| [Simulated history generation](https://simgrammar.yohei.me/mechanic/history-generation/) | world-generation | 4 | 0 | 2 | 0.8 |
| [Rule-checking inspection](https://simgrammar.yohei.me/mechanic/rule-checking-inspection/) | operation-procedure | 4 | 0 | 2 | 0.8 |
| [Interest groups](https://simgrammar.yohei.me/mechanic/interest-groups/) | governance-policy | 4 | 0.188 | 6 | 0.768 |
| [Fluid and gas simulation](https://simgrammar.yohei.me/mechanic/fluid-gas-simulation/) | physics-materials | 4 | 0.2 | 11 | 0.766 |
| [Dilemma cards](https://simgrammar.yohei.me/mechanic/dilemma-cards/) | narrative-generation | 4 | 0.225 | 7 | 0.761 |
| [Forecasting](https://simgrammar.yohei.me/mechanic/forecasting/) | information-legibility | 4 | 0.25 | 2 | 0.757 |
| [Policy influence network](https://simgrammar.yohei.me/mechanic/policy-influence-network/) | governance-policy | 4 | 0.25 | 1 | 0.757 |
| [History chronicle](https://simgrammar.yohei.me/mechanic/history-chronicle/) | narrative-generation | 4 | 0.375 | 2 | 0.735 |
| [Elections](https://simgrammar.yohei.me/mechanic/elections/) | governance-policy | 4 | 0.438 | 7 | 0.725 |
| [Programming by demonstration](https://simgrammar.yohei.me/mechanic/programming-by-demonstration/) | control-automation | 4 | 0.438 | 2 | 0.725 |
| [Player programming](https://simgrammar.yohei.me/mechanic/player-programming/) | control-automation | 4 | 0.5 | 10 | 0.714 |
| [Real-world data feeds](https://simgrammar.yohei.me/mechanic/real-world-data-feeds/) | world-generation | 4 | 0.562 | 4 | 0.703 |
| [Creature learning](https://simgrammar.yohei.me/mechanic/creature-learning/) | agents-behavior | 4 | 0.625 | 4 | 0.692 |
| [Negotiation](https://simgrammar.yohei.me/mechanic/negotiation/) | economy-finance | 4 | 0.625 | 4 | 0.692 |
| [Hand crafting](https://simgrammar.yohei.me/mechanic/hand-crafting/) | resources-production | 4 | 0.75 | 17 | 0.671 |
| [Triggered event chains](https://simgrammar.yohei.me/mechanic/triggered-event-chains/) | narrative-generation | 4 | 0.75 | 17 | 0.671 |
| [Daily schedules](https://simgrammar.yohei.me/mechanic/daily-schedules/) | agents-behavior | 4 | 0.75 | 8 | 0.671 |
| [Procedural characters](https://simgrammar.yohei.me/mechanic/procedural-characters/) | world-generation | 4 | 0.75 | 6 | 0.671 |

*Mechanics where rater-judged AI leverage outruns the techniques currently linked to them (normalized). High gap = under-researched opportunity or missing technique links. Equal gaps are ordered by prevalence, so more-used mechanics come first.*


Modding interfaces, blueprints, romance and family systems, creature care, diagnosis, product design, history generation, and rule-checking inspection are each judged ready for substantial change, and none has a technique pointed at it in this dataset. Some are covered implicitly by general techniques (code generation for modding, language models for romance dialogue), but none has a cited, game-specific result.

### 8.5 Authoritative state versus presentation

The techniques divide by whether they touch authoritative simulation state. Those that change only presentation have shipped (neural upscaling and frame generation, asset generation, motion synthesis) or reached prototypes (restyling); they preserve determinism or can be made reproducible by storing what they generate. Those that would replace physics, fields, or the world with learned prediction remain prototypes or research in games. The shipped exceptions that reach state are narrow and controlled: cached model outputs as rules ([LLM-adjudicated state transitions (LLM as game mechanic)](https://simgrammar.yohei.me/technique/llm-rule-adjudication/)), language-model characters that choose actions in [inZOI](https://simgrammar.yohei.me/game/inzoi/) ([Generative agents (memory stream, reflection, planning)](https://simgrammar.yohei.me/technique/generative-agents/), [On-device small language models for characters](https://simgrammar.yohei.me/technique/on-device-language-models/)), and opponents ([Deep reinforcement learning policies for NPC opponents and navigation](https://simgrammar.yohei.me/technique/deep-rl-npc-policies/), [Monte Carlo tree search for game AI](https://simgrammar.yohei.me/technique/monte-carlo-tree-search/)). Of these, only the language characters break reproducibility outright. The pattern suggests a design principle that recurs through §9: keep the simulation symbolic, typed, and logged, and let learned models read it, explain it, decorate it, and propose changes to it through validated interfaces.

## 9. Opportunities

### 9.1 Ranking

Each opportunity names the mechanics it reworks, the techniques it depends on, games that partially demonstrate it, a validation experiment, and a falsifiable prediction. Priority is a weighted geometric mean of impact, feasibility, and novelty scored against rubric anchors; the weights favor impact and feasibility so that safe-but-trivial and brilliant-but-impossible ideas both rank below ideas that are useful and buildable.


| opportunity | type | priority | impact | feasibility | novelty | horizon |
|---|---|---|---|---|---|---|
| [Why-query over the simulation log](https://simgrammar.yohei.me/opportunity/causal-why-query/) | legibility-layer | 4.423 | 5 | 4 | 4 | 1-2y |
| [Branch preview of policy futures](https://simgrammar.yohei.me/opportunity/branch-preview-forecasts/) | new-mechanic | 4 | 4 | 4 | 4 | 1-2y |
| [Event-sourced simulation runtime](https://simgrammar.yohei.me/opportunity/event-sourced-sim-runtime/) | infrastructure | 3.776 | 4 | 4 | 3 | 1-2y |
| [Mechanic modding by description](https://simgrammar.yohei.me/opportunity/language-modding/) | authoring-tool | 3.776 | 4 | 4 | 3 | 1-2y |
| [Salience-gated language agents](https://simgrammar.yohei.me/opportunity/salience-gated-llm-agents/) | mechanic-upgrade | 3.776 | 4 | 4 | 3 | now |
| [Bottleneck explainer for production networks](https://simgrammar.yohei.me/opportunity/bottleneck-explainer/) | legibility-layer | 3.587 | 3 | 5 | 3 | now |
| [Placement that tells stories](https://simgrammar.yohei.me/opportunity/placement-that-tells-stories/) | new-mechanic | 3.514 | 3 | 4 | 4 | now |
| [Local-first AI simulation games](https://simgrammar.yohei.me/opportunity/local-first-ai-sims/) | business-model | 3.482 | 4 | 4 | 2 | now |
| [Content-elastic event systems](https://simgrammar.yohei.me/opportunity/content-elastic-events/) | authoring-tool | 3.318 | 3 | 4 | 3 | now |
| [Drama-aware storyteller](https://simgrammar.yohei.me/opportunity/drama-aware-storyteller/) | mechanic-upgrade | 3.318 | 3 | 4 | 3 | now |
| [Explained delegation to AI managers](https://simgrammar.yohei.me/opportunity/explained-delegation/) | mechanic-upgrade | 3.318 | 3 | 4 | 3 | 1-2y |
| [Intent-level orders](https://simgrammar.yohei.me/opportunity/intent-level-orders/) | new-mechanic | 3.318 | 3 | 4 | 3 | now |
| [Learned build assist for cities](https://simgrammar.yohei.me/opportunity/learned-build-assist/) | mechanic-upgrade | 3.318 | 3 | 4 | 3 | now |
| [Learned regional weather](https://simgrammar.yohei.me/opportunity/learned-weather-layer/) | mechanic-upgrade | 3.318 | 3 | 4 | 3 | 1-2y |
| [Factories with a living workforce](https://simgrammar.yohei.me/opportunity/living-workforce-factories/) | new-genre | 3.318 | 3 | 4 | 3 | now |
| [Simulation games as agent benchmarks](https://simgrammar.yohei.me/opportunity/sims-as-agent-benchmarks/) | non-game-transfer | 3.308 | 3 | 5 | 2 | now |
| [Language-agent society terrarium](https://simgrammar.yohei.me/opportunity/llm-society-terrarium/) | new-genre | 3.282 | 4 | 2 | 5 | 3-5y |
| [Automated mechanic discovery](https://simgrammar.yohei.me/opportunity/mechanic-discovery-search/) | authoring-tool | 3.282 | 4 | 2 | 5 | 3-5y |
| [Symbolic simulation, neural rendering](https://simgrammar.yohei.me/opportunity/symbolic-sim-neural-render/) | infrastructure | 3.282 | 4 | 2 | 5 | 3-5y |
| [Agent ambassadors between player worlds](https://simgrammar.yohei.me/opportunity/agent-ambassadors-async/) | new-mechanic | 3.178 | 3 | 3 | 4 | 1-2y |
| [Human-calibrated customers](https://simgrammar.yohei.me/opportunity/human-calibrated-customers/) | mechanic-upgrade | 3.178 | 3 | 3 | 4 | 1-2y |
| [Mean-field crowds and traffic](https://simgrammar.yohei.me/opportunity/mean-field-crowds/) | infrastructure | 3.178 | 3 | 3 | 4 | 3-5y |
| [Natural-language legislation](https://simgrammar.yohei.me/opportunity/natural-language-legislation/) | new-mechanic | 3.178 | 3 | 3 | 4 | 1-2y |
| [Teachable sim companion](https://simgrammar.yohei.me/opportunity/teachable-sim-companion/) | new-mechanic | 3.178 | 3 | 3 | 4 | 1-2y |
| [Learned material surrogates at world scale](https://simgrammar.yohei.me/opportunity/learned-material-surrogates/) | infrastructure | 3.138 | 4 | 2 | 4 | 3-5y |
| [Specification programming games](https://simgrammar.yohei.me/opportunity/specification-programming-games/) | new-genre | 3.062 | 2 | 4 | 5 | now |
| [Generative decoration catalogs](https://simgrammar.yohei.me/opportunity/generative-decoration-catalogs/) | mechanic-upgrade | 3.059 | 3 | 4 | 2 | now |
| [Parallel autobalancing of economies](https://simgrammar.yohei.me/opportunity/parallel-autobalance/) | authoring-tool | 3.059 | 3 | 4 | 2 | now |
| [Simulator instructor coaching](https://simgrammar.yohei.me/opportunity/sim-instructor-coach/) | mechanic-upgrade | 3.059 | 3 | 4 | 2 | now |
| [Negotiating faction AI](https://simgrammar.yohei.me/opportunity/negotiating-faction-ai/) | mechanic-upgrade | 3 | 3 | 3 | 3 | 1-2y |
| [Participatory planning sandboxes](https://simgrammar.yohei.me/opportunity/participatory-planning-sandboxes/) | non-game-transfer | 3 | 3 | 3 | 3 | 1-2y |
| [Trainable creatures revival](https://simgrammar.yohei.me/opportunity/trainable-creatures-revival/) | mechanic-upgrade | 3 | 3 | 3 | 3 | 1-2y |
| [Generated inspection shifts](https://simgrammar.yohei.me/opportunity/generated-inspection-shifts/) | mechanic-upgrade | 2.989 | 2 | 5 | 3 | now |
| [Generated dream and replay views](https://simgrammar.yohei.me/opportunity/dream-replay-layer/) | new-mechanic | 2.769 | 2 | 3 | 5 | 1-2y |
| [Calibrated serious simulations](https://simgrammar.yohei.me/opportunity/calibrated-serious-sims/) | non-game-transfer | 2.764 | 2 | 4 | 3 | 1-2y |
| [Generated recipe graphs](https://simgrammar.yohei.me/opportunity/generated-recipe-graphs/) | authoring-tool | 2.764 | 2 | 4 | 3 | 1-2y |
| [Research by named scientists](https://simgrammar.yohei.me/opportunity/scientists-not-tech-trees/) | mechanic-upgrade | 2.764 | 2 | 4 | 3 | now |
| [Illustrated chronicles](https://simgrammar.yohei.me/opportunity/illustrated-chronicles/) | mechanic-upgrade | 2.756 | 2 | 5 | 2 | now |
| [Quality-diversity scenario libraries](https://simgrammar.yohei.me/opportunity/qd-scenario-libraries/) | authoring-tool | 2.756 | 2 | 5 | 2 | now |
| [Open-ended evolution sandbox](https://simgrammar.yohei.me/opportunity/open-ended-evolution-sandbox/) | new-genre | 2.648 | 2 | 3 | 4 | 1-2y |
| [AI liquidity in player markets](https://simgrammar.yohei.me/opportunity/ai-liquidity-in-player-markets/) | mechanic-upgrade | 2.5 | 2 | 3 | 3 | 1-2y |
| [Learned motion for simulated crowds](https://simgrammar.yohei.me/opportunity/neural-npc-motion/) | mechanic-upgrade | 2.5 | 2 | 3 | 3 | 1-2y |

*Opportunities by composite priority (weighted geometric mean of impact, feasibility, novelty; weights in vocab/rubrics.yaml).*


The highest-ranked opportunity is Why-query over the simulation log. Most of the ideas near the top make existing simulations more legible, cheaper to extend, or more alive with techniques that already work, and none asks a learned model to become the simulation.

### 9.2 Five design principles

The opportunities share a small set of principles, each a response to the ceilings in §6 and the evidence in §8.

1. **Keep the simulation symbolic; let models read, explain, decorate, and propose.** Authoritative state stays typed and deterministic. Learned models sit around it as renderers, narrators, explainers, and proposal generators whose outputs pass through validators ([Symbolic simulation, neural rendering](https://simgrammar.yohei.me/opportunity/symbolic-sim-neural-render/), [Content-elastic event systems](https://simgrammar.yohei.me/opportunity/content-elastic-events/), [Natural-language legislation](https://simgrammar.yohei.me/opportunity/natural-language-legislation/)).
2. **Spend inference on salience.** Most ticks need no model. Calls at moments that matter, cached and logged, buy believability at bounded cost ([Salience-gated language agents](https://simgrammar.yohei.me/opportunity/salience-gated-llm-agents/), [Drama-aware storyteller](https://simgrammar.yohei.me/opportunity/drama-aware-storyteller/), [Local-first AI simulation games](https://simgrammar.yohei.me/opportunity/local-first-ai-sims/)).
3. **Explain before you generate.** Comprehension limits how much coupling players can use (§6.3), and technique research rarely targets it (§8.1). Explanation over logs and sensitivity analysis needs only techniques that already exist ([Why-query over the simulation log](https://simgrammar.yohei.me/opportunity/causal-why-query/), [Bottleneck explainer for production networks](https://simgrammar.yohei.me/opportunity/bottleneck-explainer/), [Branch preview of policy futures](https://simgrammar.yohei.me/opportunity/branch-preview-forecasts/), [Illustrated chronicles](https://simgrammar.yohei.me/opportunity/illustrated-chronicles/)).
4. **Generate offline, verify with agents.** Content, recipes, scenarios, mods, and balance can be generated at design time and checked by automated play before any player sees them ([Parallel autobalancing of economies](https://simgrammar.yohei.me/opportunity/parallel-autobalance/), [Generated recipe graphs](https://simgrammar.yohei.me/opportunity/generated-recipe-graphs/), [Quality-diversity scenario libraries](https://simgrammar.yohei.me/opportunity/qd-scenario-libraries/), [Mechanic modding by description](https://simgrammar.yohei.me/opportunity/language-modding/)).
5. **Log every model call as an event.** Recording outputs restores replay, multiplayer sync, bug reproduction, and auditability, and the same log powers explanation, forecasting, and chronicles ([Event-sourced simulation runtime](https://simgrammar.yohei.me/opportunity/event-sourced-sim-runtime/)).

### 9.3 By the ceiling they relax

**Legibility.** [Why-query over the simulation log](https://simgrammar.yohei.me/opportunity/causal-why-query/) answers why-questions from the event log; [Bottleneck explainer for production networks](https://simgrammar.yohei.me/opportunity/bottleneck-explainer/) points at the binding constraint in production networks, a widely used mechanic with no technique attached; [Branch preview of policy futures](https://simgrammar.yohei.me/opportunity/branch-preview-forecasts/) shows distributions of futures before a decision; [Explained delegation to AI managers](https://simgrammar.yohei.me/opportunity/explained-delegation/) makes delegated subsystems accountable; [Simulator instructor coaching](https://simgrammar.yohei.me/opportunity/sim-instructor-coach/) narrates mistakes in operation sims.

**Authoring cost.** [Content-elastic event systems](https://simgrammar.yohei.me/opportunity/content-elastic-events/) removes the ceiling on event decks; [Generated inspection shifts](https://simgrammar.yohei.me/opportunity/generated-inspection-shifts/) gives rule-checking games endless fair cases; [Generative decoration catalogs](https://simgrammar.yohei.me/opportunity/generative-decoration-catalogs/) and [Learned build assist for cities](https://simgrammar.yohei.me/opportunity/learned-build-assist/) widen creative modes; [Generated recipe graphs](https://simgrammar.yohei.me/opportunity/generated-recipe-graphs/) and [Quality-diversity scenario libraries](https://simgrammar.yohei.me/opportunity/qd-scenario-libraries/) cut the cost of progression content; [Mechanic modding by description](https://simgrammar.yohei.me/opportunity/language-modding/) hands extension to players.

**Agent believability.** [Salience-gated language agents](https://simgrammar.yohei.me/opportunity/salience-gated-llm-agents/) gives colony and life sims specific minds at bounded cost; [Drama-aware storyteller](https://simgrammar.yohei.me/opportunity/drama-aware-storyteller/) picks events for characters' arcs; [Negotiating faction AI](https://simgrammar.yohei.me/opportunity/negotiating-faction-ai/) lets rivals bargain and remember; [Human-calibrated customers](https://simgrammar.yohei.me/opportunity/human-calibrated-customers/) grounds crowds in models of real choice; [Trainable creatures revival](https://simgrammar.yohei.me/opportunity/trainable-creatures-revival/) returns to learned creatures with modern learning; [Learned motion for simulated crowds](https://simgrammar.yohei.me/opportunity/neural-npc-motion/) shows internal state in movement.

**Compute.** [Learned material surrogates at world scale](https://simgrammar.yohei.me/opportunity/learned-material-surrogates/) extends particle-level materials to whole worlds; [Mean-field crowds and traffic](https://simgrammar.yohei.me/opportunity/mean-field-crowds/) lets cities hold equilibrium-consistent populations; [Learned regional weather](https://simgrammar.yohei.me/opportunity/learned-weather-layer/) brings realistic weather at low runtime cost.

**Determinism and infrastructure.** [Event-sourced simulation runtime](https://simgrammar.yohei.me/opportunity/event-sourced-sim-runtime/) and [Local-first AI simulation games](https://simgrammar.yohei.me/opportunity/local-first-ai-sims/) make AI components operable in long-lived, offline, moddable games; [Symbolic simulation, neural rendering](https://simgrammar.yohei.me/opportunity/symbolic-sim-neural-render/) separates what must be exact from what may be generated.

**New forms.** [Language-agent society terrarium](https://simgrammar.yohei.me/opportunity/llm-society-terrarium/) makes watching a language-agent society the game; [Open-ended evolution sandbox](https://simgrammar.yohei.me/opportunity/open-ended-evolution-sandbox/) builds evolution games on continuous artificial life; [Specification programming games](https://simgrammar.yohei.me/opportunity/specification-programming-games/) turns programming puzzles into specification and testing; [Intent-level orders](https://simgrammar.yohei.me/opportunity/intent-level-orders/) and [Teachable sim companion](https://simgrammar.yohei.me/opportunity/teachable-sim-companion/) move control from clicks to intent and demonstration; [Agent ambassadors between player worlds](https://simgrammar.yohei.me/opportunity/agent-ambassadors-async/) links single-player worlds through negotiating envoys; [Generated dream and replay views](https://simgrammar.yohei.me/opportunity/dream-replay-layer/) gives world models a role where drift is a feature; [Factories with a living workforce](https://simgrammar.yohei.me/opportunity/living-workforce-factories/), [Placement that tells stories](https://simgrammar.yohei.me/opportunity/placement-that-tells-stories/), and [Research by named scientists](https://simgrammar.yohei.me/opportunity/scientists-not-tech-trees/) fill white space between common mechanics.

**Beyond entertainment.** [Simulation games as agent benchmarks](https://simgrammar.yohei.me/opportunity/sims-as-agent-benchmarks/) offers simulation games as long-horizon evaluation environments for AI agents; [Participatory planning sandboxes](https://simgrammar.yohei.me/opportunity/participatory-planning-sandboxes/) and [Calibrated serious simulations](https://simgrammar.yohei.me/opportunity/calibrated-serious-sims/) carry calibrated models into planning and education; [Automated mechanic discovery](https://simgrammar.yohei.me/opportunity/mechanic-discovery-search/) uses this taxonomy as a search space for new mechanics.

### 9.4 Where to start, by kind of builder

- **A small studio** should look first at opportunities with feasibility 4 or 5 and horizon "now": legibility layers over an existing simulation, content-elastic events with validators, salience-gated agents on a local model, and offline balancing. Each can ship as a feature of a conventional design.
- **An engine, middleware, or tools company** has the infrastructure opportunities: event-sourced runtimes with model-call logging, constrained interfaces from language to game actions, headless simulation for agent testing, and calibrated surrogate libraries for weather and materials.
- **A research group** has the open problems: symbolic-to-neural rendering with semantic fidelity guarantees, learned material surrogates that conserve mass and energy, automated discovery of mechanics, and evaluation of explanation quality in games.
- **Organizations outside games** can use simulation games as instruments: agent benchmarks, planning sandboxes, and calibrated serious simulations, where the genre's legibility layer is as valuable as its models.

## 10. Risks and open problems

The opportunities in §9 inherit the risks of their techniques. Each technique records its primary risks from a closed vocabulary:


| Risk | Techniques |
|---|---:|
| Controllability | 34 |
| Compute cost | 29 |
| Evaluation difficulty | 24 |
| Consistency / hallucination | 20 |
| Latency | 13 |
| Determinism | 11 |
| IP / provenance | 9 |
| Legibility | 9 |
| Player trust / reception | 9 |
| Content safety | 7 |
| Labor displacement | 7 |


**Consistency.** Language and world models contradict state, forget, and drift. In a simulation game a contradiction is worse than a gap, because players use the simulation's outputs to build mental models. Constrained decoding, typed write-back, and grounding every generated claim in logged state are necessary; none is sufficient for open-ended generation.

**Determinism.** Runtime generation breaks replays, lockstep multiplayer, and bug reproduction unless outputs are recorded and replayed as events. Games that already depend on determinism (competitive leaderboards, large multiplayer factories) should treat model outputs as inputs from an external system, logged at the boundary.

**Cost.** Per-player-hour inference conflicts with one-time purchases and with how long simulation players play. Local models, salience gating, and caching bound cost; frame-generating world models remain far from affordable at the session lengths simulation games require (§7.2).

**Legibility of learned systems.** A learned policy or generated rule can be as opaque as the simulation it replaced. Every learned component that affects state needs an explanation path, or it moves a mechanic down the legibility scale in §5.6.

**Evaluation.** Open-ended outputs are hard to QA. Automated playtesting checks validity and balance, not quality; human evaluation does not scale to generated variety. Simulation games need evaluation methods for generated content analogous to the verification queue in this dataset: sampled, scored against anchors, and logged.

**Player trust and labor.** Reception of generative features has been mixed, and developers' view of generative AI's effect on the industry has turned more negative while reported use held steady (§7.2). Disclosure rules on the largest PC store already distinguish pre-generated from live-generated content [[4](#ref-src-valve-2026-steamworks-content-survey)]. Opportunities that make games more legible or let players author more (explanation, modding by description, intent-level orders) are less exposed to this risk than those that replace authored work.

**Safety and provenance.** Live generation in social simulations needs content guardrails, especially where players can steer characters with language. Asset generation carries training-data and likeness questions. These risks are recorded per technique so they can be filtered and tracked.

**Open research problems** recorded on mechanic and technique pages include: grounding generated explanations in simulation logs with measurable faithfulness; conservation guarantees for learned physics; semantic fidelity for neural rendering of symbolic state; inferring needs and preferences from behavior instead of declaring them; and fair, inspectable AI participants in player economies.

## 11. Predictions and research agenda

Every opportunity carries a falsifiable prediction with a resolve-by date and criteria a stranger could check. The first resolves on 2027-12-31. Because predictions are data, resolving one is a pull request: set the opportunity's status, cite the evidence, and the report and wiki update.


| resolve by | name | prediction |
|---|---|---|
| 2027-12-31 | [Content-elastic event systems](https://simgrammar.yohei.me/opportunity/content-elastic-events/) | A grand strategy, life sim, or narrative management game will ship runtime-generated events constrained by an event schema. |
| 2027-12-31 | [Generated inspection shifts](https://simgrammar.yohei.me/opportunity/generated-inspection-shifts/) | An inspection or bureaucracy job sim will generate documents or applicants at runtime and score the player against an answer key derived from formal rules. |
| 2027-12-31 | [Generative decoration catalogs](https://simgrammar.yohei.me/opportunity/generative-decoration-catalogs/) | A life or management sim other than inZOI will let players generate new placeable 3D objects from text or images. |
| 2027-12-31 | [Illustrated chronicles](https://simgrammar.yohei.me/opportunity/illustrated-chronicles/) | A systemic simulation game will ship an automatic, shareable narrative summary of a run's history generated from its event log. |
| 2027-12-31 | [Local-first AI simulation games](https://simgrammar.yohei.me/opportunity/local-first-ai-sims/) | At least five games with over 1,000 Steam user reviews will use an on-device language model at runtime without requiring an internet connection. |
| 2027-12-31 | [Parallel autobalancing of economies](https://simgrammar.yohei.me/opportunity/parallel-autobalance/) | At least two studios will publicly describe using large-scale agent search to balance a simulation or strategy game's economy before release. |
| 2027-12-31 | [Simulation games as agent benchmarks](https://simgrammar.yohei.me/opportunity/sims-as-agent-benchmarks/) | A simulation game developer or publisher will officially release a headless research API or benchmark for AI agents. |
| 2027-12-31 | [Simulator instructor coaching](https://simgrammar.yohei.me/opportunity/sim-instructor-coach/) | A flight or racing simulator will ship an AI voice instructor that comments on live telemetry. |
| 2027-12-31 | [Why-query over the simulation log](https://simgrammar.yohei.me/opportunity/causal-why-query/) | A widely played simulation or strategy game will let players ask in natural language why something happened in their own game and answer from game state. |
| 2028-06-30 | [Bottleneck explainer for production networks](https://simgrammar.yohei.me/opportunity/bottleneck-explainer/) | A factory or city-building game will ship a feature that names the binding constraint in the player's production network by testing the simulation, not by displaying static ratios. |
| 2028-06-30 | [Branch preview of policy futures](https://simgrammar.yohei.me/opportunity/branch-preview-forecasts/) | A city builder, colony sim, or grand strategy game will show players several simulated stochastic futures of their current game state before a decision. |
| 2028-06-30 | [Drama-aware storyteller](https://simgrammar.yohei.me/opportunity/drama-aware-storyteller/) | A colony sim or survival management game will ship an event director that uses a language model to rank authored events against the current story state. |
| 2028-06-30 | [Intent-level orders](https://simgrammar.yohei.me/opportunity/intent-level-orders/) | A colony or management sim will let players issue standing natural-language orders that compile into its job and priority systems. |
| 2028-06-30 | [Learned build assist for cities](https://simgrammar.yohei.me/opportunity/learned-build-assist/) | A city builder will ship a machine-learned layout generator that turns player strokes into detailed streets or districts. |
| 2028-06-30 | [Mechanic modding by description](https://simgrammar.yohei.me/opportunity/language-modding/) | The developer of a moddable simulation game will ship or officially endorse a tool that builds working mods from natural-language descriptions. |
| 2028-06-30 | [Quality-diversity scenario libraries](https://simgrammar.yohei.me/opportunity/qd-scenario-libraries/) | A simulation or puzzle-sim game will ship a scenario library generated by quality-diversity search. |
| 2028-06-30 | [Specification programming games](https://simgrammar.yohei.me/opportunity/specification-programming-games/) | A programming game will make specifying or testing AI-written code its core loop. |
| 2028-12-31 | [Calibrated serious simulations](https://simgrammar.yohei.me/opportunity/calibrated-serious-sims/) | A playable serious-game or educational simulation will publish posterior-calibrated parameters with fit metrics as part of its release. |
| 2028-12-31 | [Event-sourced simulation runtime](https://simgrammar.yohei.me/opportunity/event-sourced-sim-runtime/) | An engine, middleware vendor, or open-source project will ship an event-log replay and determinism layer designed for games with generative AI components. |
| 2028-12-31 | [Explained delegation to AI managers](https://simgrammar.yohei.me/opportunity/explained-delegation/) | A grand strategy or management game will ship AI managers that learn delegation policy from the individual player's own past decisions. |
| 2028-12-31 | [Generated dream and replay views](https://simgrammar.yohei.me/opportunity/dream-replay-layer/) | A game will use a generative video or world model to show character memories or in-world histories drawn from the simulation's own event log. |
| 2028-12-31 | [Generated recipe graphs](https://simgrammar.yohei.me/opportunity/generated-recipe-graphs/) | A factory or crafting game or overhaul mod will credit algorithmic or model-based generation for its recipe graph or tech tree. |
| 2028-12-31 | [Human-calibrated customers](https://simgrammar.yohei.me/opportunity/human-calibrated-customers/) | A management or tycoon game will state that its customer or citizen preferences come from a model of human behavior learned from data. |
| 2028-12-31 | [Learned regional weather](https://simgrammar.yohei.me/opportunity/learned-weather-layer/) | A farming, flight, or city sim will ship weather generated by a learned emulator rather than scripted states or live forecast feeds. |
| 2028-12-31 | [Natural-language legislation](https://simgrammar.yohei.me/opportunity/natural-language-legislation/) | A political or city-building game will let players enact free-text laws that change simulation parameters. |
| 2028-12-31 | [Placement that tells stories](https://simgrammar.yohei.me/opportunity/placement-that-tells-stories/) | A city builder will advertise placement-triggered narrative events tied to named inhabitants as a core feature. |
| 2028-12-31 | [Salience-gated language agents](https://simgrammar.yohei.me/opportunity/salience-gated-llm-agents/) | At least three colony or life sims with over 1,000 Steam user reviews will call a language model for agents only on salient events rather than per decision. |
| 2028-12-31 | [Teachable sim companion](https://simgrammar.yohei.me/opportunity/teachable-sim-companion/) | An automation or sandbox game will ship an in-game companion that learns reusable skills from player demonstration or instruction. |
| 2029-06-30 | [AI liquidity in player markets](https://simgrammar.yohei.me/opportunity/ai-liquidity-in-player-markets/) | A persistent online game will add AI traders to its player-driven market, with their behavior fitted to observed player trading. |
| 2029-06-30 | [Agent ambassadors between player worlds](https://simgrammar.yohei.me/opportunity/agent-ambassadors-async/) | A game will let each player's AI representative trade or negotiate with other players' worlds while those players are offline. |
| 2029-06-30 | [Learned motion for simulated crowds](https://simgrammar.yohei.me/opportunity/neural-npc-motion/) | A management or colony sim will ship learned physics-based motion for its simulated population. |
| 2029-06-30 | [Negotiating faction AI](https://simgrammar.yohei.me/opportunity/negotiating-faction-ai/) | A grand strategy or 4X game will ship AI opponents that negotiate in free-text or generated-language diplomacy backed by a planner. |
| 2029-06-30 | [Research by named scientists](https://simgrammar.yohei.me/opportunity/scientists-not-tech-trees/) | A strategy or management game will ship research performed by a simulated population of named researchers whose relationships affect outcomes. |
| 2029-06-30 | [Trainable creatures revival](https://simgrammar.yohei.me/opportunity/trainable-creatures-revival/) | A virtual-pet or god game will ship a creature controlled by a learned neural or reinforcement-learning policy that player feedback updates during play. |
| 2029-12-31 | [Factories with a living workforce](https://simgrammar.yohei.me/opportunity/living-workforce-factories/) | A factory or automation game in which workers age, train, and are replaced by a simulated next generation will reach 1,000 Steam user reviews. |
| 2029-12-31 | [Language-agent society terrarium](https://simgrammar.yohei.me/opportunity/llm-society-terrarium/) | A game whose core loop is observing and nudging a society of at least 50 language-model agents will reach 1,000 Steam user reviews. |
| 2029-12-31 | [Learned material surrogates at world scale](https://simgrammar.yohei.me/opportunity/learned-material-surrogates/) | A game will use a learned surrogate model to simulate fluid, gas, or destruction at runtime. |
| 2029-12-31 | [Mean-field crowds and traffic](https://simgrammar.yohei.me/opportunity/mean-field-crowds/) | A city builder will document a mean-field or continuum crowd model as its primary traffic or population simulation. |
| 2029-12-31 | [Open-ended evolution sandbox](https://simgrammar.yohei.me/opportunity/open-ended-evolution-sandbox/) | A game built on a continuous artificial-life substrate (Lenia family or neural cellular automata) will reach 1,000 Steam user reviews. |
| 2029-12-31 | [Participatory planning sandboxes](https://simgrammar.yohei.me/opportunity/participatory-planning-sandboxes/) | A city government will use a game-style calibrated simulation with simulated resident feedback in a formal planning consultation. |
| 2029-12-31 | [Symbolic simulation, neural rendering](https://simgrammar.yohei.me/opportunity/symbolic-sim-neural-render/) | A game will render its primary view with a generative model conditioned on an explicit symbolic game state. |
| 2030-12-31 | [Automated mechanic discovery](https://simgrammar.yohei.me/opportunity/mechanic-discovery-search/) | A commercial game will credit one of its shipped mechanics to an automated rule-discovery system. |

*Each prediction has resolution criteria on its wiki page. A prediction that fails is evidence against the opportunity thesis, not only against its timing.*


### 11.1 Agenda

1. **Instrument a simulation for explanation.** Build the event log with cause links that why-queries, branch previews, and chronicles all need, and measure explanation faithfulness against human audit.
2. **Measure legibility in players, not only in rubrics.** The legibility and emergence scores here are judgments by a single model rater; a shared protocol for measuring how quickly players form correct causal models would let designers compare mechanics empirically.
3. **Connect techniques to the economic core.** Production, logistics, and economy mechanics are the most used and the least targeted by current techniques (§8.2). Balance search, recipe generation, and bottleneck explanation are tractable first steps.
4. **Separate authoritative and generated layers.** Develop and benchmark architectures where learned models render, narrate, or propose, and symbolic state decides.
5. **Extend the dataset.** Add mobile and non-English simulation traditions, score mechanics with a second rater, resolve the verification queue, and record design tensions with evidence from postmortems.

### 11.2 How to extend this report

The report is generated. To add a game, mechanic, technique, or opportunity, follow `AGENTS.md`; tables, counts, figures, rankings, and this section's prediction list update on the next build. To change an argument, edit the prose in `report/src/`; every dataset number in it is a token, so the text cannot fall out of date with the data.

## Appendix A. Game catalog


| name | year | developer | subgenre | time model | sim scale | mechanics | cluster | status |
|---|---|---|---|---|---|---|---|---|
| [Hamurabi](https://simgrammar.yohei.me/game/hamurabi/) | 1968 | Doug Dyment (Digital Equipment Corporation) | city-builder | turn-based | settlement | 6 | C12 | sourced |
| [Conway's Game of Life](https://simgrammar.yohei.me/game/game-of-life/) | 1970 | John Horton Conway | artificial-life | run-on-demand | micro | 3 | C12 | sourced |
| [The Oregon Trail](https://simgrammar.yohei.me/game/oregon-trail/) | 1971 | Don Rawitsch, Bill Heinemann, and Paul Dillenberger; later MECC | survival-sim | turn-based | household | 5 | C12 | sourced |
| [Lemonade Stand](https://simgrammar.yohei.me/game/lemonade-stand/) | 1973 | Bob Jamison (MECC) | business-economic-sim | turn-based | facility | 7 | C12 | sourced |
| [Utopia](https://simgrammar.yohei.me/game/utopia/) | 1982 | Don Daglow (Mattel Electronics) | city-builder | real-time | settlement | 8 | C04 | contested |
| [M.U.L.E.](https://simgrammar.yohei.me/game/mule/) | 1983 | Ozark Softscape | business-economic-sim | turn-based | settlement | 10 | C02 | sourced |
| [Elite](https://simgrammar.yohei.me/game/elite/) | 1984 | David Braben and Ian Bell | space-sim | real-time | interplanetary | 6 | C11 | sourced |
| [Balance of Power](https://simgrammar.yohei.me/game/balance-of-power/) | 1985 | Chris Crawford | political-sim | turn-based | nation | 6 | C12 | sourced |
| [Little Computer People](https://simgrammar.yohei.me/game/little-computer-people/) | 1985 | Activision | life-sim | real-time | individual | 6 | C13 | sourced |
| [Populous](https://simgrammar.yohei.me/game/populous/) | 1989 | Bullfrog Productions | god-game | real-time | region | 5 | C10 | sourced |
| [SimCity](https://simgrammar.yohei.me/game/simcity-1989/) | 1989 | Maxis | city-builder | real-time-pausable | city | 17 | C09 | sourced |
| [Railroad Tycoon](https://simgrammar.yohei.me/game/railroad-tycoon/) | 1990 | MPS Labs (MicroProse) | transport-logistics | real-time-pausable | region | 15 | C02 | sourced |
| [SimEarth](https://simgrammar.yohei.me/game/simearth/) | 1990 | Maxis | god-game | real-time-pausable | planet | 10 | C10 | sourced |
| [Sid Meier's Civilization](https://simgrammar.yohei.me/game/civilization/) | 1991 | MicroProse | 4x-strategy | turn-based | nation | 13 | C04 | sourced |
| [SimAnt](https://simgrammar.yohei.me/game/simant/) | 1991 | Maxis | artificial-life | real-time-pausable | settlement | 10 | C02 | sourced |
| [SimLife](https://simgrammar.yohei.me/game/simlife/) | 1992 | Maxis | artificial-life | real-time-pausable | region | 8 | C10 | sourced |
| [Princess Maker 2](https://simgrammar.yohei.me/game/princess-maker-2/) | 1993 | Gainax | life-sim | turn-based | individual | 9 | C14 | sourced |
| [SimCity 2000](https://simgrammar.yohei.me/game/simcity-2000/) | 1993 | Maxis | city-builder | real-time-pausable | city | 18 | C09 | sourced |
| [The Incredible Machine](https://simgrammar.yohei.me/game/the-incredible-machine/) | 1993 | Jeff Tunnell Productions | construction-engineering | run-on-demand | individual | 6 | C07 | sourced |
| [SimTower](https://simgrammar.yohei.me/game/simtower/) | 1994 | OPeNBooK (Yoot Saito) | management-tycoon | real-time-pausable | facility | 9 | C09 | sourced |
| [Theme Park](https://simgrammar.yohei.me/game/theme-park/) | 1994 | Bullfrog Productions | management-tycoon | real-time-pausable | facility | 14 | C01 | sourced |
| [Transport Tycoon](https://simgrammar.yohei.me/game/transport-tycoon/) | 1994 | Chris Sawyer | transport-logistics | real-time-pausable | region | 18 | C02 | sourced |
| [Capitalism](https://simgrammar.yohei.me/game/capitalism/) | 1995 | Enlight Software | business-economic-sim | real-time-pausable | region | 13 | C01 | sourced |
| [X-Plane](https://simgrammar.yohei.me/game/x-plane/) | 1995 | Laminar Research | flight-sim | real-time-pausable | individual | 8 | C03 | sourced |
| [Creatures](https://simgrammar.yohei.me/game/creatures/) | 1996 | Millennium Interactive / Cyberlife Technology | artificial-life | real-time-pausable | individual | 12 | C13 | sourced |
| [Harvest Moon](https://simgrammar.yohei.me/game/harvest-moon/) | 1996 | Amccus | farming-sim | real-time | facility | 8 | C05 | sourced |
| [Tamagotchi](https://simgrammar.yohei.me/game/tamagotchi/) | 1996 | Bandai | virtual-pet | real-world-clock | individual | 8 | C13 | sourced |
| [Gran Turismo](https://simgrammar.yohei.me/game/gran-turismo/) | 1997 | Polys Entertainment (Polyphony Digital) | vehicle-sim | real-time | individual | 6 | C03 | sourced |
| [Theme Hospital](https://simgrammar.yohei.me/game/theme-hospital/) | 1997 | Bullfrog Productions | management-tycoon | real-time-pausable | facility | 16 | C01 | sourced |
| [Ultima Online](https://simgrammar.yohei.me/game/ultima-online/) | 1997 | Origin Systems | mmo-world | asynchronous-persistent | region | 10 | C06 | sourced |
| [Caesar III](https://simgrammar.yohei.me/game/caesar-3/) | 1998 | Impressions Games | city-builder | real-time-pausable | city | 17 | C02 | sourced |
| [Out of the Park Baseball](https://simgrammar.yohei.me/game/out-of-the-park-baseball/) | 1999 | Out of the Park Developments | sports-management | turn-based | household | 11 | C01 | sourced |
| [Pharaoh](https://simgrammar.yohei.me/game/pharaoh/) | 1999 | Impressions Games | city-builder | real-time-pausable | city | 15 | C02 | sourced |
| [RollerCoaster Tycoon](https://simgrammar.yohei.me/game/rollercoaster-tycoon/) | 1999 | Chris Sawyer Productions | management-tycoon | real-time-pausable | facility | 20 | C01 | sourced |
| [Seaman](https://simgrammar.yohei.me/game/seaman/) | 1999 | Vivarium | virtual-pet | real-world-clock | individual | 8 | C13 | sourced |
| [The Sims](https://simgrammar.yohei.me/game/the-sims/) | 2000 | Maxis | life-sim | real-time-pausable | household | 15 | C01 | sourced |
| [Black & White](https://simgrammar.yohei.me/game/black-and-white/) | 2001 | Lionhead Studios | god-game | real-time | region | 9 | C13 | sourced |
| [Zoo Tycoon](https://simgrammar.yohei.me/game/zoo-tycoon/) | 2001 | Blue Fang Games | management-tycoon | real-time-pausable | facility | 11 | C01 | sourced |
| [A Tale in the Desert](https://simgrammar.yohei.me/game/a-tale-in-the-desert/) | 2003 | eGenesis | mmo-world | asynchronous-persistent | region | 8 | C06 | sourced |
| [EVE Online](https://simgrammar.yohei.me/game/eve-online/) | 2003 | CCP Games | mmo-world | asynchronous-persistent | interplanetary | 12 | C06 | sourced |
| [Second Life](https://simgrammar.yohei.me/game/second-life/) | 2003 | Linden Lab | mmo-world | asynchronous-persistent | region | 8 | C06 | sourced |
| [SimCity 4](https://simgrammar.yohei.me/game/simcity-4/) | 2003 | Maxis | city-builder | real-time-pausable | city | 16 | C09 | sourced |
| [Aurora 4X](https://simgrammar.yohei.me/game/aurora-4x/) | 2004 | Steve Walmsley | 4x-strategy | turn-based | interplanetary | 13 | C11 | sourced |
| [Football Manager](https://simgrammar.yohei.me/game/football-manager/) | 2004 | Sports Interactive | sports-management | turn-based | household | 15 | C01 | sourced |
| [Garry's Mod](https://simgrammar.yohei.me/game/garrys-mod/) | 2004 | Facepunch Studios | physics-sandbox | real-time | individual | 7 | C07 | sourced |
| [The Sims 2](https://simgrammar.yohei.me/game/the-sims-2/) | 2004 | Maxis | life-sim | real-time-pausable | household | 16 | C01 | sourced |
| [Façade](https://simgrammar.yohei.me/game/facade/) | 2005 | Procedural Arts | social-sim | real-time | household | 5 | C08 | sourced |
| [Nintendogs](https://simgrammar.yohei.me/game/nintendogs/) | 2005 | Nintendo EAD | virtual-pet | real-world-clock | individual | 7 | C13 | sourced |
| [Silent Hunter III](https://simgrammar.yohei.me/game/silent-hunter-3/) | 2005 | Ubisoft Bucharest | vehicle-sim | real-time-pausable | individual | 10 | C03 | sourced |
| [Dwarf Fortress](https://simgrammar.yohei.me/game/dwarf-fortress/) | 2006 | Bay 12 Games | colony-sim | real-time-pausable | settlement | 29 | C01 | sourced |
| [Viva Piñata](https://simgrammar.yohei.me/game/viva-pinata/) | 2006 | Rare | ecosystem-evolution | real-time | facility | 9 | C05 | sourced |
| [DCS World](https://simgrammar.yohei.me/game/dcs-world/) | 2008 | Eagle Dynamics | flight-sim | real-time-pausable | individual | 10 | C03 | sourced |
| [Spore](https://simgrammar.yohei.me/game/spore/) | 2008 | Maxis | ecosystem-evolution | real-time-pausable | interplanetary | 8 | C11 | sourced |
| [The Powder Toy](https://simgrammar.yohei.me/game/the-powder-toy/) | 2008 | The Powder Toy contributors | physics-sandbox | real-time-pausable | micro | 9 | C07 | sourced |
| [Universe Sandbox](https://simgrammar.yohei.me/game/universe-sandbox/) | 2008 | Dan Dixon; Giant Army | physics-sandbox | real-time-pausable | interplanetary | 7 | C11 | sourced |
| [iRacing](https://simgrammar.yohei.me/game/iracing/) | 2008 | iRacing Studios (iRacing.com Motorsport Simulations) | vehicle-sim | real-time | individual | 4 | C03 | sourced |
| [Minecraft](https://simgrammar.yohei.me/game/minecraft/) | 2009 | Mojang Studios | sandbox-world | real-time | region | 15 | C05 | sourced |
| [The Sims 3](https://simgrammar.yohei.me/game/the-sims-3/) | 2009 | Maxis Redwood Shores | life-sim | real-time-pausable | household | 18 | C01 | sourced |
| [From Dust](https://simgrammar.yohei.me/game/from-dust/) | 2011 | Ubisoft Montpellier | god-game | real-time | region | 8 | C10 | sourced |
| [Kerbal Space Program](https://simgrammar.yohei.me/game/kerbal-space-program/) | 2011 | Squad | space-sim | real-time-pausable | interplanetary | 15 | C11 | sourced |
| [Project Zomboid](https://simgrammar.yohei.me/game/project-zomboid/) | 2011 | The Indie Stone | survival-sim | real-time-pausable | individual | 18 | C05 | sourced |
| [SpaceChem](https://simgrammar.yohei.me/game/spacechem/) | 2011 | Zachtronics | programming-sim | run-on-demand | micro | 6 | C06 | sourced |
| [Don't Starve](https://simgrammar.yohei.me/game/dont-starve/) | 2012 | Klei Entertainment | survival-sim | real-time | individual | 12 | C05 | sourced |
| [Euro Truck Simulator 2](https://simgrammar.yohei.me/game/euro-truck-simulator-2/) | 2012 | SCS Software | vehicle-sim | real-time | individual | 11 | C03 | sourced |
| [FTL: Faster Than Light](https://simgrammar.yohei.me/game/ftl/) | 2012 | Subset Games | space-sim | real-time-pausable | household | 14 | C01 | sourced |
| [Game Dev Tycoon](https://simgrammar.yohei.me/game/game-dev-tycoon/) | 2012 | Greenheart Games | business-economic-sim | real-time-pausable | facility | 12 | C01 | sourced |
| [Plague Inc.](https://simgrammar.yohei.me/game/plague-inc/) | 2012 | Ndemic Creations | ecosystem-evolution | real-time-pausable | planet | 9 | C10 | sourced |
| [Prison Architect](https://simgrammar.yohei.me/game/prison-architect/) | 2012 | Introversion Software | management-tycoon | real-time-pausable | facility | 17 | C01 | sourced |
| [Prom Week](https://simgrammar.yohei.me/game/prom-week/) | 2012 | UC Santa Cruz Expressive Intelligence Studio | social-sim | turn-based | household | 6 | C01 | sourced |
| [Species: Artificial Life, Real Evolution](https://simgrammar.yohei.me/game/species-alre/) | 2012 | Quasar | artificial-life | real-time-pausable | region | 8 | C10 | sourced |
| [Arma 3](https://simgrammar.yohei.me/game/arma-3/) | 2013 | Bohemia Interactive | wargame | real-time | individual | 10 | C03 | sourced |
| [BeamNG.drive](https://simgrammar.yohei.me/game/beamng-drive/) | 2013 | BeamNG GmbH | vehicle-sim | real-time-pausable | individual | 7 | C03 | sourced |
| [Europa Universalis IV](https://simgrammar.yohei.me/game/europa-universalis-4/) | 2013 | Paradox Development Studio | grand-strategy | real-time-pausable | nation | 20 | C04 | sourced |
| [Factorio](https://simgrammar.yohei.me/game/factorio/) | 2013 | Wube Software | factory-automation | real-time | facility | 28 | C02 | sourced |
| [Kenshi](https://simgrammar.yohei.me/game/kenshi/) | 2013 | Lo-Fi Games | rpg-sim | real-time-pausable | region | 16 | C05 | sourced |
| [Mini Metro](https://simgrammar.yohei.me/game/mini-metro/) | 2013 | Dinosaur Polo Club | transport-logistics | real-time-pausable | city | 5 | C09 | sourced |
| [Papers, Please](https://simgrammar.yohei.me/game/papers-please/) | 2013 | Lucas Pope (3909 LLC) | job-sim | real-time | individual | 7 | C14 | sourced |
| [RimWorld](https://simgrammar.yohei.me/game/rimworld/) | 2013 | Ludeon Studios | colony-sim | real-time-pausable | settlement | 24 | C01 | sourced |
| [SimCity (2013)](https://simgrammar.yohei.me/game/simcity-2013/) | 2013 | Maxis Emeryville | city-builder | real-time-pausable | city | 14 | C09 | sourced |
| [Space Engineers](https://simgrammar.yohei.me/game/space-engineers/) | 2013 | Keen Software House | sandbox-world | real-time | facility | 14 | C07 | sourced |
| [Surgeon Simulator](https://simgrammar.yohei.me/game/surgeon-simulator/) | 2013 | Bossa Studios | medical-sim | real-time | individual | 4 | C07 | sourced |
| [Tomodachi Life](https://simgrammar.yohei.me/game/tomodachi-life/) | 2013 | Nintendo SPD | life-sim | real-world-clock | settlement | 8 | C01 | sourced |
| [Versu](https://simgrammar.yohei.me/game/versu/) | 2013 | Linden Lab | social-sim | turn-based | household | 6 | C01 | sourced |
| [Banished](https://simgrammar.yohei.me/game/banished/) | 2014 | Shining Rock Software | city-builder | real-time-pausable | settlement | 16 | C02 | sourced |
| [Elite Dangerous](https://simgrammar.yohei.me/game/elite-dangerous/) | 2014 | Frontier Developments | space-sim | asynchronous-persistent | interplanetary | 17 | C11 | sourced |
| [Screeps](https://simgrammar.yohei.me/game/screeps/) | 2014 | Screeps, LLC | programming-sim | asynchronous-persistent | region | 12 | C06 | sourced |
| [Subnautica](https://simgrammar.yohei.me/game/subnautica/) | 2014 | Unknown Worlds Entertainment | survival-sim | real-time | individual | 8 | C05 | sourced |
| [The Long Dark](https://simgrammar.yohei.me/game/the-long-dark/) | 2014 | Hinterland Studio | survival-sim | real-time | individual | 9 | C05 | sourced |
| [The Sims 4](https://simgrammar.yohei.me/game/the-sims-4/) | 2014 | Maxis | life-sim | real-time-pausable | household | 19 | C01 | sourced |
| [This War of Mine](https://simgrammar.yohei.me/game/this-war-of-mine/) | 2014 | 11 bit studios | survival-sim | real-time | household | 12 | C14 | sourced |
| [Besiege](https://simgrammar.yohei.me/game/besiege/) | 2015 | Spiderling Studios | construction-engineering | run-on-demand | individual | 8 | C07 | sourced |
| [Big Pharma](https://simgrammar.yohei.me/game/big-pharma/) | 2015 | Twice Circled | factory-automation | real-time-pausable | facility | 10 | C02 | sourced |
| [Caves of Qud](https://simgrammar.yohei.me/game/caves-of-qud/) | 2015 | Freehold Games | rpg-sim | turn-based | individual | 9 | C12 | sourced |
| [Cities: Skylines](https://simgrammar.yohei.me/game/cities-skylines/) | 2015 | Colossal Order | city-builder | real-time-pausable | city | 17 | C09 | sourced |
| [Offworld Trading Company](https://simgrammar.yohei.me/game/offworld-trading-company/) | 2015 | Mohawk Games | business-economic-sim | real-time-pausable | region | 12 | C02 | sourced |
| [Poly Bridge](https://simgrammar.yohei.me/game/poly-bridge/) | 2015 | Dry Cactus | construction-engineering | run-on-demand | facility | 7 | C07 | sourced |
| [Hearts of Iron IV](https://simgrammar.yohei.me/game/hearts-of-iron-4/) | 2016 | Paradox Development Studio | grand-strategy | real-time-pausable | nation | 16 | C04 | sourced |
| [Job Simulator](https://simgrammar.yohei.me/game/job-simulator/) | 2016 | Owlchemy Labs | job-sim | real-time | individual | 3 | C07 | sourced |
| [Motorsport Manager](https://simgrammar.yohei.me/game/motorsport-manager/) | 2016 | Playsport Games | sports-management | real-time-pausable | household | 10 | C01 | sourced |
| [Planet Coaster](https://simgrammar.yohei.me/game/planet-coaster/) | 2016 | Frontier Developments | management-tycoon | real-time-pausable | facility | 17 | C01 | sourced |
| [Reigns](https://simgrammar.yohei.me/game/reigns/) | 2016 | Nerial | political-sim | turn-based | nation | 5 | C14 | sourced |
| [Stardew Valley](https://simgrammar.yohei.me/game/stardew-valley/) | 2016 | ConcernedApe | farming-sim | real-time | facility | 15 | C05 | sourced |
| [Stellaris](https://simgrammar.yohei.me/game/stellaris/) | 2016 | Paradox Development Studio | 4x-strategy | real-time-pausable | interplanetary | 20 | C04 | sourced |
| [Bitburner](https://simgrammar.yohei.me/game/bitburner/) | 2017 | danielyxie and Bitburner contributors | programming-sim | real-world-clock | individual | 8 | C06 | sourced |
| [Kingdoms and Castles](https://simgrammar.yohei.me/game/kingdoms-and-castles/) | 2017 | Lion Shield | city-builder | real-time-pausable | settlement | 16 | C02 | sourced |
| [Mindustry](https://simgrammar.yohei.me/game/mindustry/) | 2017 | Anuke | factory-automation | real-time-pausable | settlement | 16 | C02 | sourced |
| [Opus Magnum](https://simgrammar.yohei.me/game/opus-magnum/) | 2017 | Zachtronics | programming-sim | run-on-demand | micro | 6 | C06 | sourced |
| [Oxygen Not Included](https://simgrammar.yohei.me/game/oxygen-not-included/) | 2017 | Klei Entertainment | colony-sim | real-time-pausable | settlement | 23 | C01 | sourced |
| [Stationeers](https://simgrammar.yohei.me/game/stationeers/) | 2017 | RocketWerkz | survival-sim | real-time | facility | 12 | C07 | sourced |
| [The Legend of Zelda: Breath of the Wild](https://simgrammar.yohei.me/game/zelda-breath-of-the-wild/) | 2017 | Nintendo EPD | sandbox-world | real-time-pausable | region | 10 | C05 | sourced |
| [Eco](https://simgrammar.yohei.me/game/eco/) | 2018 | Strange Loop Games | mmo-world | asynchronous-persistent | planet | 14 | C06 | sourced |
| [Equilinox](https://simgrammar.yohei.me/game/equilinox/) | 2018 | ThinMatrix | ecosystem-evolution | real-time | facility | 8 | C05 | sourced |
| [Frostpunk](https://simgrammar.yohei.me/game/frostpunk/) | 2018 | 11 bit studios | city-builder | real-time-pausable | settlement | 14 | C04 | sourced |
| [House Flipper](https://simgrammar.yohei.me/game/house-flipper/) | 2018 | Empyrean | job-sim | real-time | facility | 7 | C15 | sourced |
| [Jurassic World Evolution](https://simgrammar.yohei.me/game/jurassic-world-evolution/) | 2018 | Frontier Developments | management-tycoon | real-time-pausable | facility | 13 | C02 | sourced |
| [PC Building Simulator](https://simgrammar.yohei.me/game/pc-building-simulator/) | 2018 | Claudiu Kiss and The Irregular Corporation | job-sim | real-time | individual | 6 | C15 | sourced |
| [Project Hospital](https://simgrammar.yohei.me/game/project-hospital/) | 2018 | Oxymoron Games | medical-sim | real-time-pausable | facility | 10 | C01 | sourced |
| [Rebel Inc.](https://simgrammar.yohei.me/game/rebel-inc/) | 2018 | Ndemic Creations | political-sim | real-time-pausable | region | 8 | C04 | sourced |
| [Surviving Mars](https://simgrammar.yohei.me/game/surviving-mars/) | 2018 | Haemimont Games | city-builder | real-time-pausable | settlement | 15 | C02 | sourced |
| [Two Point Hospital](https://simgrammar.yohei.me/game/two-point-hospital/) | 2018 | Two Point Studios | management-tycoon | real-time-pausable | facility | 17 | C01 | sourced |
| [AI Dungeon](https://simgrammar.yohei.me/game/ai-dungeon/) | 2019 | Latitude | ai-native | turn-based | individual | 4 | C08 | sourced |
| [Anno 1800](https://simgrammar.yohei.me/game/anno-1800/) | 2019 | Ubisoft Blue Byte | city-builder | real-time-pausable | region | 13 | C02 | sourced |
| [Autonauts](https://simgrammar.yohei.me/game/autonauts/) | 2019 | Denki | programming-sim | real-time | settlement | 12 | C06 | sourced |
| [Command: Modern Operations](https://simgrammar.yohei.me/game/command-modern-operations/) | 2019 | Warfare Sims | wargame | real-time-pausable | region | 11 | C03 | sourced |
| [Foundation](https://simgrammar.yohei.me/game/foundation/) | 2019 | Polymorph Games | city-builder | real-time-pausable | settlement | 9 | C02 | sourced |
| [Islanders](https://simgrammar.yohei.me/game/islanders/) | 2019 | Grizzly Games | city-builder | turn-based | settlement | 4 | C11 | sourced |
| [Noita](https://simgrammar.yohei.me/game/noita/) | 2019 | Nolla Games | physics-sandbox | real-time | individual | 11 | C07 | sourced |
| [Planet Zoo](https://simgrammar.yohei.me/game/planet-zoo/) | 2019 | Frontier Developments | management-tycoon | real-time-pausable | facility | 15 | C01 | sourced |
| [Satisfactory](https://simgrammar.yohei.me/game/satisfactory/) | 2019 | Coffee Stain Studios | factory-automation | real-time | facility | 18 | C02 | sourced |
| [Tropico 6](https://simgrammar.yohei.me/game/tropico-6/) | 2019 | Limbic Entertainment | city-builder | real-time-pausable | nation | 12 | C04 | sourced |
| [Workers & Resources: Soviet Republic](https://simgrammar.yohei.me/game/workers-and-resources/) | 2019 | 3Division | city-builder | real-time-pausable | region | 15 | C02 | sourced |
| [Animal Crossing: New Horizons](https://simgrammar.yohei.me/game/animal-crossing-new-horizons/) | 2020 | Nintendo EPD | life-sim | real-world-clock | settlement | 13 | C05 | sourced |
| [Crusader Kings III](https://simgrammar.yohei.me/game/crusader-kings-3/) | 2020 | Paradox Development Studio | grand-strategy | real-time-pausable | nation | 20 | C04 | sourced |
| [Democracy 4](https://simgrammar.yohei.me/game/democracy-4/) | 2020 | Positech Games | political-sim | turn-based | nation | 11 | C04 | sourced |
| [Hardspace: Shipbreaker](https://simgrammar.yohei.me/game/hardspace-shipbreaker/) | 2020 | Blackbird Interactive | job-sim | real-time | individual | 7 | C15 | sourced |
| [Microsoft Flight Simulator (2020)](https://simgrammar.yohei.me/game/microsoft-flight-simulator-2020/) | 2020 | Asobo Studio | flight-sim | real-time-pausable | individual | 9 | C03 | sourced |
| [SnowRunner](https://simgrammar.yohei.me/game/snowrunner/) | 2020 | Saber Interactive | vehicle-sim | real-time | individual | 7 | C03 | sourced |
| [Songs of Syx](https://simgrammar.yohei.me/game/songs-of-syx/) | 2020 | Gamatron AB | city-builder | real-time-pausable | city | 11 | C02 | sourced |
| [Space Haven](https://simgrammar.yohei.me/game/space-haven/) | 2020 | Bugbyte | colony-sim | real-time-pausable | household | 17 | C01 | sourced |
| [Suzerain](https://simgrammar.yohei.me/game/suzerain/) | 2020 | Torpor Games | political-sim | turn-based | nation | 6 | C14 | sourced |
| [Teardown](https://simgrammar.yohei.me/game/teardown/) | 2020 | Tuxedo Labs | physics-sandbox | real-time | facility | 8 | C07 | sourced |
| [Townscaper](https://simgrammar.yohei.me/game/townscaper/) | 2020 | Oskar Stålberg | city-builder | turn-based | settlement | 3 | C16 | sourced |
| [Against the Storm](https://simgrammar.yohei.me/game/against-the-storm/) | 2021 | Eremite Games | city-builder | real-time-pausable | settlement | 13 | C04 | sourced |
| [Car Mechanic Simulator 2021](https://simgrammar.yohei.me/game/car-mechanic-simulator-2021/) | 2021 | Red Dot Games | job-sim | real-time | individual | 6 | C15 | sourced |
| [Dyson Sphere Program](https://simgrammar.yohei.me/game/dyson-sphere-program/) | 2021 | Youthcat Studio | factory-automation | real-time | interplanetary | 18 | C02 | sourced |
| [Going Medieval](https://simgrammar.yohei.me/game/going-medieval/) | 2021 | Foxy Voxel | colony-sim | real-time-pausable | settlement | 21 | C01 | sourced |
| [PowerWash Simulator](https://simgrammar.yohei.me/game/powerwash-simulator/) | 2021 | FuturLab | job-sim | real-time | individual | 4 | C15 | sourced |
| [Timberborn](https://simgrammar.yohei.me/game/timberborn/) | 2021 | Mechanistry | city-builder | real-time-pausable | settlement | 13 | C10 | sourced |
| [Valheim](https://simgrammar.yohei.me/game/valheim/) | 2021 | Iron Gate Studio | survival-sim | real-time | individual | 14 | C05 | sourced |
| [Captain of Industry](https://simgrammar.yohei.me/game/captain-of-industry/) | 2022 | MaFi Games | factory-automation | real-time-pausable | settlement | 22 | C02 | sourced |
| [Farthest Frontier](https://simgrammar.yohei.me/game/farthest-frontier/) | 2022 | Crate Entertainment | city-builder | real-time-pausable | settlement | 14 | C02 | sourced |
| [Gran Turismo 7](https://simgrammar.yohei.me/game/gran-turismo-7/) | 2022 | Polyphony Digital | vehicle-sim | real-time | individual | 6 | C03 | sourced |
| [Victoria 3](https://simgrammar.yohei.me/game/victoria-3/) | 2022 | Paradox Development Studio | grand-strategy | real-time-pausable | nation | 19 | C04 | sourced |
| [Big Ambitions](https://simgrammar.yohei.me/game/big-ambitions/) | 2023 | Hovgaard Games | business-economic-sim | real-time-pausable | city | 12 | C01 | sourced |
| [Cities: Skylines II](https://simgrammar.yohei.me/game/cities-skylines-2/) | 2023 | Colossal Order (Iceflake Studios from 2026) | city-builder | real-time-pausable | city | 18 | C09 | sourced |
| [Contraband Police](https://simgrammar.yohei.me/game/contraband-police/) | 2023 | Crazy Rocks Studios | job-sim | real-time | individual | 6 | C14 | sourced |
| [Generative Agents (Smallville)](https://simgrammar.yohei.me/game/generative-agents-smallville/) | 2023 | Stanford University and Google Research | ai-native | run-on-demand | settlement | 7 | C08 | sourced |
| [Suck Up!](https://simgrammar.yohei.me/game/suck-up/) | 2023 | Proxima Enterprises | ai-native | real-time | individual | 6 | C08 | sourced |
| [Terra Nil](https://simgrammar.yohei.me/game/terra-nil/) | 2023 | Free Lives | city-builder | real-time | region | 6 | C10 | sourced |
| [The Farmer Was Replaced](https://simgrammar.yohei.me/game/the-farmer-was-replaced/) | 2023 | Timon Herzog | programming-sim | real-time | facility | 6 | C06 | sourced |
| [Farming Simulator 25](https://simgrammar.yohei.me/game/farming-simulator-25/) | 2024 | Giants Software | farming-sim | real-time-pausable | facility | 14 | C03 | sourced |
| [Frostpunk 2](https://simgrammar.yohei.me/game/frostpunk-2/) | 2024 | 11 bit studios | city-builder | real-time-pausable | city | 11 | C04 | sourced |
| [Infinite Craft](https://simgrammar.yohei.me/game/infinite-craft/) | 2024 | Neal Agarwal | ai-native | turn-based | individual | 3 | C08 | sourced |
| [Manor Lords](https://simgrammar.yohei.me/game/manor-lords/) | 2024 | Slavic Magic | city-builder | real-time-pausable | settlement | 15 | C02 | sourced |
| [Microsoft Flight Simulator 2024](https://simgrammar.yohei.me/game/microsoft-flight-simulator-2024/) | 2024 | Asobo Studio | flight-sim | real-time-pausable | individual | 12 | C03 | sourced |
| [Project Sid](https://simgrammar.yohei.me/game/project-sid/) | 2024 | Altera | ai-native | real-time | settlement | 8 | C08 | sourced |
| [Tiny Glade](https://simgrammar.yohei.me/game/tiny-glade/) | 2024 | Pounce Light | city-builder | real-time | settlement | 3 | C16 | sourced |
| [Where Winds Meet](https://simgrammar.yohei.me/game/where-winds-meet/) | 2024 | Everstone Studio (NetEase Games) | rpg-sim | real-time | individual | 5 | C08 | asserted |
| [shapez 2](https://simgrammar.yohei.me/game/shapez-2/) | 2024 | tobspr Games | factory-automation | real-time | facility | 12 | C02 | sourced |
| [Anno 117: Pax Romana](https://simgrammar.yohei.me/game/anno-117/) | 2025 | Ubisoft Mainz | city-builder | real-time-pausable | region | 13 | C02 | sourced |
| [Schedule I](https://simgrammar.yohei.me/game/schedule-i/) | 2025 | TVGS | business-economic-sim | real-time | city | 11 | C01 | sourced |
| [Whispers from the Star](https://simgrammar.yohei.me/game/whispers-from-the-star/) | 2025 | Anuttacon | ai-native | real-time | individual | 3 | C08 | sourced |
| [inZOI](https://simgrammar.yohei.me/game/inzoi/) | 2025 | inZOI Studio (Krafton) | life-sim | real-time-pausable | household | 17 | C01 | sourced |
| [Paralives](https://simgrammar.yohei.me/game/paralives/) | 2026 | Paralives Studio | life-sim | real-time-pausable | household | 12 | C01 | sourced |


## Appendix B. Technique catalog


| name | category | year | maturity | trl | horizon | determinism impact |
|---|---|---|---|---|---|---|
| [Learned physics-based character control](https://simgrammar.yohei.me/technique/physics-based-character-control/) | animation-motion | 2024 | research | 4 | 3-5y | mitigable |
| [Learned kinematic motion synthesis](https://simgrammar.yohei.me/technique/learned-motion-synthesis/) | animation-motion | 2020 | shipped-niche | 7 | now | preserves |
| [Continuous cellular automata and foundation-model search for artificial life](https://simgrammar.yohei.me/technique/continuous-alife-and-asal/) | artificial-life-research | 2024 | research | 3 | 3-5y | preserves |
| [Neural cellular automata](https://simgrammar.yohei.me/technique/neural-cellular-automata/) | artificial-life-research | 2020 | research | 4 | 3-5y | mitigable |
| [Automated generation of game rules and mechanics](https://simgrammar.yohei.me/technique/automated-rule-generation/) | automated-game-design | 2024 | prototype | 5 | 3-5y | preserves |
| [Agent-based automated playtesting and balancing](https://simgrammar.yohei.me/technique/automated-playtesting/) | automated-game-design | 2018 | shipped-niche | 7 | now | preserves |
| [Massively parallel GPU simulation](https://simgrammar.yohei.me/technique/massively-parallel-simulation/) | differentiable-simulation | 2021 | research | 4 | 1-2y | preserves |
| [Differentiable simulation](https://simgrammar.yohei.me/technique/differentiable-simulation/) | differentiable-simulation | 2020 | research | 3 | 3-5y | preserves |
| [Language models grounded in strategic planning for negotiation games](https://simgrammar.yohei.me/technique/cicero-strategic-dialogue/) | game-theoretic-solvers | 2022 | research | 5 | 1-2y | breaks |
| [Mean field games and mean-field learning](https://simgrammar.yohei.me/technique/mean-field-games/) | game-theoretic-solvers | 2021 | research | 3 | 3-5y | preserves |
| [Regret minimization and search for imperfect-information games](https://simgrammar.yohei.me/technique/imperfect-information-solvers/) | game-theoretic-solvers | 2019 | research | 5 | 3-5y | mitigable |
| [Monte Carlo tree search for game AI](https://simgrammar.yohei.me/technique/monte-carlo-tree-search/) | game-theoretic-solvers | 2006 | shipped-niche | 7 | now | mitigable |
| [Genie foundation world models](https://simgrammar.yohei.me/technique/genie-world-models/) | generative-world-model | 2025 | prototype | 6 | 3-5y | breaks |
| [Muse World and Human Action Model (WHAM)](https://simgrammar.yohei.me/technique/muse-wham/) | generative-world-model | 2025 | prototype | 6 | 3-5y | breaks |
| [Open real-time interactive video world models](https://simgrammar.yohei.me/technique/open-interactive-video-models/) | generative-world-model | 2025 | prototype | 6 | 3-5y | breaks |
| [Physical-world foundation models](https://simgrammar.yohei.me/technique/physical-world-foundation-models/) | generative-world-model | 2025 | research | 3 | 5y-plus | breaks |
| [Diffusion and autoregressive neural game engines](https://simgrammar.yohei.me/technique/diffusion-game-engines/) | generative-world-model | 2024 | prototype | 6 | 3-5y | breaks |
| [LLM-adjudicated state transitions (LLM as game mechanic)](https://simgrammar.yohei.me/technique/llm-rule-adjudication/) | generative-world-model | 2024 | shipped-niche | 7 | now | mitigable |
| [On-device small language models for characters](https://simgrammar.yohei.me/technique/on-device-language-models/) | inference-efficiency | 2025 | shipped-niche | 7 | now | mitigable |
| [Generalist instructable game agents (SIMA)](https://simgrammar.yohei.me/technique/generalist-game-agents/) | llm-agents | 2024 | research | 4 | 3-5y | mitigable |
| [Grammar-constrained decoding for valid game actions](https://simgrammar.yohei.me/technique/constrained-decoding/) | llm-agents | 2024 | research | 4 | now | mitigable |
| [Generative agents (memory stream, reflection, planning)](https://simgrammar.yohei.me/technique/generative-agents/) | llm-agents | 2023 | shipped-niche | 7 | now | breaks |
| [LLM-written skill libraries (Voyager)](https://simgrammar.yohei.me/technique/voyager-skill-libraries/) | llm-agents | 2023 | research | 4 | 1-2y | mitigable |
| [LLM explanation of simulation state](https://simgrammar.yohei.me/technique/llm-explanation-of-state/) | llm-narrative-dialogue | 2023 | prototype | 5 | 1-2y | preserves |
| [LLM game master and narrative director](https://simgrammar.yohei.me/technique/llm-game-master/) | llm-narrative-dialogue | 2019 | shipped-niche | 8 | now | breaks |
| [LLM-guided evolutionary program search](https://simgrammar.yohei.me/technique/alphaevolve-algorithm-discovery/) | math-discovery | 2025 | research | 3 | 1-2y | preserves |
| [Simulation-based inference for calibrating simulators](https://simgrammar.yohei.me/technique/simulation-based-inference/) | math-discovery | 2019 | research | 3 | 1-2y | preserves |
| [Many-agent LLM societies](https://simgrammar.yohei.me/technique/llm-agent-societies/) | multi-agent-social-sim | 2024 | research | 4 | 3-5y | breaks |
| [Machine-learned weather forecasting](https://simgrammar.yohei.me/technique/ml-weather-models/) | neural-physics | 2023 | research | 3 | 3-5y | mitigable |
| [Graph network simulators and neural operators](https://simgrammar.yohei.me/technique/graph-network-simulators/) | neural-physics | 2020 | research | 3 | 3-5y | mitigable |
| [Subspace neural physics and learned deformers](https://simgrammar.yohei.me/technique/subspace-neural-physics/) | neural-physics | 2019 | prototype | 6 | now | preserves |
| [Neural rendering in the graphics pipeline](https://simgrammar.yohei.me/technique/neural-rendering-shaders/) | neural-rendering-3d | 2025 | shipped-mainstream | 9 | now | preserves |
| [Prompt-to-persistent 3D world generation](https://simgrammar.yohei.me/technique/generated-3d-worlds/) | neural-rendering-3d | 2025 | prototype | 6 | 1-2y | preserves |
| [Real-time generative restyling of game video](https://simgrammar.yohei.me/technique/real-time-video-restyling/) | neural-rendering-3d | 2025 | prototype | 6 | 1-2y | mitigable |
| [Text- and image-to-3D asset generation](https://simgrammar.yohei.me/technique/text-to-3d-assets/) | neural-rendering-3d | 2025 | shipped-niche | 7 | now | mitigable |
| [3D Gaussian Splatting](https://simgrammar.yohei.me/technique/gaussian-splatting/) | neural-rendering-3d | 2023 | prototype | 6 | 1-2y | preserves |
| [LLM models of individual human choice](https://simgrammar.yohei.me/technique/human-behavior-simulation-models/) | player-modeling | 2025 | research | 3 | 3-5y | preserves |
| [Learned level and map generation (PCGRL, MarioGPT, LLM generators)](https://simgrammar.yohei.me/technique/learned-level-generation/) | procedural-generation | 2023 | research | 4 | 1-2y | mitigable |
| [ML reconstruction of the planet from aerial imagery](https://simgrammar.yohei.me/technique/satellite-world-reconstruction/) | procedural-generation | 2020 | shipped-niche | 8 | now | preserves |
| [Wave Function Collapse and constraint-based tile generation](https://simgrammar.yohei.me/technique/wave-function-collapse/) | procedural-generation | 2016 | shipped-niche | 8 | now | preserves |
| [Quality-diversity search (MAP-Elites) for content and balance](https://simgrammar.yohei.me/technique/quality-diversity-search/) | procedural-generation | 2015 | research | 4 | now | preserves |
| [Open-ended co-generation of environments and agents](https://simgrammar.yohei.me/technique/open-ended-environment-generation/) | reinforcement-learning | 2024 | research | 4 | 3-5y | mitigable |
| [Deep reinforcement learning policies for NPC opponents and navigation](https://simgrammar.yohei.me/technique/deep-rl-npc-policies/) | reinforcement-learning | 2022 | shipped-niche | 7 | now | mitigable |
| [Self-play planning with learned models (AlphaZero, MuZero, Dreamer)](https://simgrammar.yohei.me/technique/model-based-planning-muzero/) | reinforcement-learning | 2020 | research | 4 | 3-5y | mitigable |
| [Realtime speech-to-speech and expressive TTS for characters](https://simgrammar.yohei.me/technique/realtime-voice-models/) | speech-audio | 2024 | shipped-niche | 8 | now | breaks |


## Appendix C. Using and extending this dataset

- **Cite** a specific version by the `dataset_sha256` in `dist/manifest.json` (also printed on this report's title page).
- **Query** with the CSVs in `dist/tables/`, the graph files in `dist/graph/` (JSON Lines, Cytoscape, GraphML), or `make sqlite` for SQL.
- **Browse** the wiki at `dist/wiki/index.md` or the explorer at `site/index.html`.
- **Contribute** by following `AGENTS.md`: open a run, search before creating, fill entities against the schema, run `make check`. The fastest useful contribution is sourcing an entity from `dist/analysis/verification-queue.csv`.
- **Dispute** a fact by setting `status: contested` with a claim that cites the opposing source; disputes are data, not edits.

## References

<a id="ref-src-totallyhuman-2024-steam-genai-count"></a>[1] Totally Human Media (2024-04-24). *The Surprising Number of Steam Games that Use GenAI*. Totally Human blog https://www.totallyhuman.io/blog/the-surprising-number-of-steam-games-that-use-genai  
<a id="ref-src-totallyhuman-2025-steam-genai-count"></a>[2] Totally Human Media (2025-07-13). *The NEW Surprising Number of Steam Games that Use GenAI*. Totally Human blog https://www.totallyhuman.io/blog/the-surprising-new-number-of-genai-games-on-steam  
<a id="ref-src-totallyhuman-2025-steam-ai-revenue"></a>[3] Totally Human Media (2025-11-06). *Games With AI Disclosures Have Grossed an Estimated $660M on Steam*. Totally Human blog https://www.totallyhuman.io/blog/games-with-ai-disclosures-have-grossed-an-estimated-660m-on-steam  
<a id="ref-src-valve-2026-steamworks-content-survey"></a>[4] Valve (2026). *Steamworks Documentation: Content Survey (generative AI disclosure)*. Steamworks documentation https://partner.steamgames.com/doc/gettingstarted/contentsurvey  
<a id="ref-src-gdc-2025-state-of-industry"></a>[5] Game Developers Conference (2025-01). *GDC 2025 State of the Game Industry: Devs weigh in on layoffs, AI, and more*. gdconf.com https://gdconf.com/article/gdc-2025-state-of-the-game-industry-devs-weigh-in-on-layoffs-ai-and-more/  
<a id="ref-src-gdc-2026-state-of-industry"></a>[6] Game Developers Conference (2026). *GDC 2026 State of the Game Industry reveals impact of layoffs, generative AI, and more*. gdconf.com https://gdconf.com/article/gdc-2026-state-of-the-game-industry-reveals-impact-of-layoffs-generative-ai-and-more/  
<a id="ref-src-wikipedia-inzoi"></a>[7] Wikipedia contributors (2026). *inZOI*. Wikipedia https://en.wikipedia.org/wiki/InZOI  
<a id="ref-src-wikipedia-arc-raiders"></a>[8] Wikipedia contributors (2026). *ARC Raiders*. Wikipedia https://en.wikipedia.org/wiki/ARC_Raiders  
<a id="ref-src-nvidia-2025-ace-companions"></a>[9] NVIDIA (2025). *NVIDIA ACE autonomous game characters: PUBG Ally, inZOI Smart Zoi, NARAKA AI teammate*. GeForce News https://www.nvidia.com/en-us/geforce/news/nvidia-ace-autonomous-ai-companions-pubg-naraka-bladepoint/  
<a id="ref-src-krafton-2026-pubg-ally-beta"></a>[10] KRAFTON (2026-06-16). *KRAFTON Introduces PUBG Ally Beta Test*. KRAFTON press release https://www.krafton.com/en/news/press/krafton-introduces-pubg-ally-beta-test/  
<a id="ref-src-steam-2025-where-winds-meet"></a>[11] Everstone Studio, NetEase Games (2025-11-14). *Where Winds Meet on Steam*. Steam https://store.steampowered.com/app/3564740/Where_Winds_Meet/  
<a id="ref-src-openai-2024-realtime-api"></a>[12] OpenAI (2024-10-01). *Introducing the Realtime API*. OpenAI blog https://openai.com/index/introducing-the-realtime-api/  
<a id="ref-src-openai-2025-gpt-realtime"></a>[13] OpenAI (2025-08-28). *Introducing gpt-realtime*. OpenAI blog https://openai.com/index/introducing-gpt-realtime/  
<a id="ref-src-inworld-2026-tts-1-5"></a>[14] Inworld AI (2026-01-21). *Inworld TTS-1.5: Upgrading the #1 Ranked TTS Model with Production-Grade Latency, Expression and Stability*. Inworld blog https://inworld.ai/blog/introducing-inworld-tts-1-5  
<a id="ref-src-techcrunch-2026-project-genie"></a>[15] Rebecca Bellan (2026-01-29). *I built marshmallow castles in Google's new AI world generator Project Genie*. TechCrunch https://techcrunch.com/2026/01/29/i-built-marshmallow-castles-in-googles-new-ai-world-generator-project-genie  
<a id="ref-src-nvidia-2026-dlss-4-5"></a>[16] NVIDIA (2026-01-06). *NVIDIA DLSS 4.5 Delivers Major Upgrade With 2nd Gen Transformer Model For Super Resolution and 6X Dynamic Multi Frame Generation*. GeForce News https://www.nvidia.com/en-us/geforce/news/dlss-4-5-dynamic-multi-frame-gen-6x-2nd-gen-transformer-super-res/  
<a id="ref-src-ecmwf-2025-aifs-operational"></a>[17] ECMWF (2025-02-25). *ECMWF's AI forecasts become operational*. ECMWF news https://www.ecmwf.int/en/about/media-centre/news/2025/ecmwfs-ai-forecasts-become-operational  
