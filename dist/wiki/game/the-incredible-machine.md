# The Incredible Machine

*Game* · `the-incredible-machine` · status: **sourced**

A Rube Goldberg puzzle game in which the player places supplied parts such as balls, ropes, pulleys, belts, and animals into a level so that a deterministic physics run completes a simple goal.

| field | value |
|---|---|
| aliases | TIM |
| year | 1993 |
| developer | Jeff Tunnell Productions |
| platforms | PC, Console |
| subgenre | Construction / engineering |
| sim domain | Physical / mechanical |
| player role | Engineer / designer |
| agency model | Design then test |
| time model | Run on demand |
| sim scale | Individual |
| fidelity | Stylized |
| perspective | Top-down / side 2D |
| win structure | Scenario goals |
| failure model | Soft / recoverable |
| narrative mode | None |
| multiplayer | Single-player |
| modding | Content |
| production tier | AA |
| agent count order | None |
| emergence | 2 |
| influence | 3 |
| cluster *(computed)* | C07 |
| core count *(computed)* | 3 |
| mechanic count *(computed)* | 6 |

## Summary

A Rube Goldberg puzzle game in which the player places supplied parts such as balls, ropes, pulleys, belts, and animals into a level so that a deterministic physics run completes a simple goal.

## Core Loop

read the puzzle goal -> place the supplied parts among fixed objects -> start the machine -> watch the chain reaction -> adjust positions until the goal triggers

## Design Notes

Each puzzle fixes some objects in a side-view scene and hands the player a small inventory of parts; the solution is a chain reaction where each part triggers the next, such as a ball dropping on a seesaw that frees a mouse that runs toward cheese. The physics engine models gravity and air pressure as global settings and has no random number generator, so a design behaves the same on every run and solutions are verifiable. A freeform mode exposes all parts so players can make puzzles for others.

## Relations

**uses**

- [Modular assembly](../mechanic/modular-assembly.md) (core): Levels supply a limited inventory of parts such as balls, ropes, pulleys, belts, electrical generators, cats, and mice that the player places among fixed objects; parts act on each other by contact, rope, or belt.
- [Rigid-body physics](../mechanic/rigid-body-physics.md) (core): A deterministic 2D physics engine with no random number generator moves balls, seesaws, and falling objects under level-set gravity and air pressure, so the same design always gives the same run.
- [Scenario objectives](../mechanic/scenario-objectives.md) (core): Each puzzle states one simple goal, such as moving an object to a target, that must be met with only the parts provided.
- [Material interactions](../mechanic/material-interactions.md) (supporting): Some parts react to others by fixed rules, such as a mouse running toward cheese.
- [Signal circuits](../mechanic/signal-circuits.md) (supporting): Electrical generators driven by other parts power electrical devices in the contraption.
- [Content sharing](../mechanic/content-sharing.md) (supporting): Freeform mode saves player-built puzzles, using any part, for others to solve.

## Sources

- [The Incredible Machine](../source/src-wikipedia-the-incredible-machine.md)

---
Provenance: created in run `2026-10-24-catalog-gg`.
