## 1. Introduction

A simulation game is a game whose state changes by rules the player did not author and does not fully control. The player builds a road and the traffic is the city's reply; the player sets a tax and the citizens decide whether to stay. Everything distinctive about the form follows from that gap between intent and outcome: the pleasure of watching a system respond, the frustration of not understanding why it did, and the stories players tell about runs no designer scripted.

The genre is old and large. Its lineage runs from text programs on mainframes (a grain-and-population ledger in [[hamurabi]], a wagon party's rations in [[oregon-trail]]) through [[simcity-1989]] and [[the-sims]] to [[dwarf-fortress]], [[factorio]], and [[eve-online]]. Its methods are less visible than its titles. Designers share a working vocabulary (needs meters, production chains, storytellers, overlays) but no common, inspectable map of which rule-systems exist, which games combine them, how each one fails, and which are near their ceilings.

That map matters now because the ceilings are moving. For forty years the depth of a simulation game was bounded by a few constraints: how much compute a consumer machine could spend per tick, how much content a studio could author, how much hidden state a player could understand, how tightly a multiplayer game had to stay deterministic, and how believable a rule-driven agent could be. Results from 2019 to 2026 in learned world models, language-model agents, learned physics, accelerated simulation, automated design, and on-device inference press on each of those constraints, unevenly and with new costs.

This report does four things:

1. **Catalogs** {{count:game}} simulation games across {{stat:n_subgenres}} subgenres, from {{stat:year_min}} to {{stat:year_max}}, and decomposes each into the mechanics it uses ({{count:edge:uses}} typed game-to-mechanic edges, each marked core or supporting, with implementation notes for core mechanics).
2. **Analyzes** {{count:mechanic}} mechanics one at a time: rule-level definition, player experience, design levers, failure modes, dynamics, mathematical basis, and six anchored scores (legibility, emergence potential, authoring cost, compute cost, tuning difficulty, AI leverage).
3. **Maps** {{count:technique}} mathematical, AI, ML, and LLM techniques onto those mechanics through {{stat:n_affects_edges}} typed `affects` edges that say how each technique changes each mechanic (replaces its substrate, deepens it, enables a new form, cuts its authoring cost, explains it, tunes it, or accelerates it).
4. **Synthesizes** {{count:opportunity}} design opportunities, each with a validation experiment a small team could run and a falsifiable prediction with a resolve-by date.

Every number in this document is rendered from the dataset at build time; the dataset hash on the title page identifies the exact version. The report, the wiki, the tables, and the graph are projections of the same YAML files, so a correction to one entity updates all of them.
