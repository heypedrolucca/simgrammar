# Simulation games as agent benchmarks

*Opportunity* · `sims-as-agent-benchmarks` · status: **asserted**

Use factory, colony, and economy sims as long-horizon evaluation and training environments for AI agents, with game studios as environment providers.

| field | value |
|---|---|
| opportunity type | Non-game transfer |
| involves | [Production chains](../mechanic/production-chain.md), [Power grid](../mechanic/power-grid.md), [Conveyor transport](../mechanic/conveyor-transport.md), [Scenario objectives](../mechanic/scenario-objectives.md), [Comparative histograms](../mechanic/comparative-histograms.md) |
| applies | [Generalist instructable game agents (SIMA)](../technique/generalist-game-agents.md), [Open-ended co-generation of environments and agents](../technique/open-ended-environment-generation.md), [LLM-written skill libraries (Voyager)](../technique/voyager-skill-libraries.md) |
| precedent | [Factorio](../game/factorio.md), [Minecraft](../game/minecraft.md), [Screeps](../game/screeps.md), [Dwarf Fortress](../game/dwarf-fortress.md) |
| novelty | 2 |
| feasibility | 5 |
| impact | 3 |
| horizon | Now |
| key risks | Benchmarks saturate quickly., Studios may not want agent play to define their game publicly., Engine licensing for research use. |
| falsifiable signal | {'prediction': 'A commercial simulation game developer will officially release a headless research API or benchmark for AI agents.', 'resolve_by': '2027-12-31', 'criteria': 'Official announcement or repository from the developer, not only a community wrapper.'} |
| priority *(computed)* | 3.308 |

## Thesis

AI agents now need environments that test planning over thousands of steps, resource management, and recovery from compounding errors. Simulation games are exactly that, with measurable outcomes (throughput, survival, profit). Minecraft became a research environment through MineDojo and Voyager, and factory games have been proposed as agent benchmarks. Games with headless modes and clean observation APIs can become a licensed research category.

## Design Sketch

A studio ships a headless build with a typed observation and action API, standard scenarios, and leaderboards for agents. Researchers measure long-horizon performance; players watch agent runs as content.

## Key Risks

- Benchmarks saturate quickly.
- Studios may not want agent play to define their game publicly.
- Engine licensing for research use.

## Validation Experiment

Wrap an open-source colony or factory sim with a typed API, define five scenarios with throughput and survival metrics, and evaluate three frontier agents. Success: scores that separate agents and do not saturate within one model generation.

## Falsifiable signal

- **Prediction:** A commercial simulation game developer will officially release a headless research API or benchmark for AI agents.
- **Resolve by:** 2027-12-31
- **Criteria:** Official announcement or repository from the developer, not only a community wrapper.

## Relations

**applies**

- [Generalist instructable game agents (SIMA)](../technique/generalist-game-agents.md)
- [Open-ended co-generation of environments and agents](../technique/open-ended-environment-generation.md)
- [LLM-written skill libraries (Voyager)](../technique/voyager-skill-libraries.md)

**involves**

- [Production chains](../mechanic/production-chain.md)
- [Power grid](../mechanic/power-grid.md)
- [Conveyor transport](../mechanic/conveyor-transport.md)
- [Scenario objectives](../mechanic/scenario-objectives.md)
- [Comparative histograms](../mechanic/comparative-histograms.md)

**precedent**

- [Factorio](../game/factorio.md)
- [Minecraft](../game/minecraft.md)
- [Screeps](../game/screeps.md)
- [Dwarf Fortress](../game/dwarf-fortress.md)

---
Provenance: created in run `2026-10-24-synthesis`.
