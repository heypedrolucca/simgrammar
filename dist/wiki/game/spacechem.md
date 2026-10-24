# SpaceChem

*Game* · `spacechem` · status: **sourced**

A programming puzzle game in which the player lays out instruction paths for two waldos in grid reactors that grab, bond, rotate, and split atoms into target molecules, with each solution scored on cycles, reactors, and instructions against global histograms.

| field | value |
|---|---|
| year | 2011 |
| developer | Zachtronics |
| platforms | PC, Mobile |
| subgenre | Programming sim |
| subgenre secondary | Factory / automation |
| sim domain | Computational / abstract, Industrial / logistics |
| player role | Programmer |
| agency model | Programmatic, Design then test |
| time model | Run on demand |
| sim scale | Micro |
| fidelity | Abstract |
| perspective | Top-down / side 2D |
| win structure | Campaign |
| failure model | None |
| narrative mode | Authored |
| multiplayer | Single-player, Async / shared content |
| modding | Content |
| production tier | Indie |
| agent count order | None |
| emergence | 2 |
| influence | 3 |
| boundary case | True |
| influenced by |  |
| cluster *(computed)* | C02 |
| core count *(computed)* | 3 |
| mechanic count *(computed)* | 6 |

## Summary

A programming puzzle game in which the player lays out instruction paths for two waldos in grid reactors that grab, bond, rotate, and split atoms into target molecules, with each solution scored on cycles, reactors, and instructions against global histograms.

## Core Loop

read the input and output molecules -> place waldo paths and instruction icons in a 10x8 reactor -> run and debug collisions -> meet the output quota -> compare cycles, reactors, and instructions on histograms -> optimize or move on

## Design Notes

SpaceChem made the program itself the factory: each 10x8 reactor holds two waldos, red and blue, programmed independently or synchronized by instruction icons laid on the grid, and multiple reactors connect on a planet-surface pipeline so one reactor's output feeds another. Execution is deterministic, so a solution either produces the quota or deadlocks or collides, and success is followed by global histograms of cycles, reactors, and instructions that Zach Barth designed to show where a solution sits without the intimidation of a ranked leaderboard. Each planet ends in a defense level where production must keep pace with an attacker. Barth expanded the manipulator puzzles of his 2008 Flash game The Codex of Alchemical Engineering, and the instruction-grid plus histogram template recurs across Zachtronics' later games. ResearchNet let players share puzzles.

## Relations

**uses**

- [Player programming](../mechanic/player-programming.md) (core): Two waldos per reactor, red and blue, follow player-placed paths and instruction icons that pick up, rotate, drop, bond, and route atoms, programmed independently or synchronized, with deterministic and visible execution.
- [Design performance rating](../mechanic/design-performance-rating.md) (core): A solution passes when it outputs the required molecule quota and is then scored on cycles, number of reactors, and number of instructions used.
- [Comparative histograms](../mechanic/comparative-histograms.md) (core): After completion the player's cycles, reactors, and instructions are plotted on global histograms of other players' solutions, chosen over a ranked leaderboard to avoid discouraging players.
- [Production chains](../mechanic/production-chain.md) (supporting): Reactors placed on a larger planet map pass molecules through pipelines, so later puzzles split a synthesis across several reactors, some limited to tasks such as breaking bonds, with fission and fusion nodes.
- [Scenario objectives](../mechanic/scenario-objectives.md) (supporting): Each puzzle fixes inputs, target outputs, available reactor types, and quotas; defense levels add a time pressure from an attacking enemy.
- [Content sharing](../mechanic/content-sharing.md) (supporting): ResearchNet distributes user-made puzzles that other players download and solve.

## Backlinks (computed)

**influenced:** [Opus Magnum](../game/opus-magnum.md)

**precedent for:** [Automated mechanic discovery](../opportunity/mechanic-discovery-search.md), [Specification programming games](../opportunity/specification-programming-games.md)

## Claims

- Barth's earlier Flash game The Codex of Alchemical Engineering (2008), which is not in this dataset, is the documented precursor of SpaceChem's manipulator puzzles. *(confidence: high)* [[29](../source/src-wikipedia-spacechem.md)]

## Sources

- [SpaceChem](../source/src-wikipedia-spacechem.md)

---
Provenance: created in run `2026-10-24-catalog-gh`.
