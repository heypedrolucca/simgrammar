# Mini Metro

*Game* · `mini-metro` · status: **sourced**

A minimalist subway-design game where the player draws and redraws lines between shape-coded stations under a weekly ration of trains and tunnels until a station overcrowds.

| field | value |
|---|---|
| year | 2013 |
| year full release | 2015 |
| developer | Dinosaur Polo Club |
| platforms | PC, Mobile, Handheld, Console, Web |
| subgenre | Transport / logistics |
| sim domain | Urban, Industrial / logistics |
| player role | Planner / mayor |
| agency model | Zoning / placement |
| time model | Real-time with pause |
| sim scale | City |
| fidelity | Abstract |
| perspective | Top-down / side 2D |
| win structure | Score / ranking |
| failure model | Hard restart |
| narrative mode | None |
| multiplayer | Single-player |
| modding | None |
| production tier | Indie |
| agent count order | ~100 |
| emergence | 2 |
| influence | 2 |
| cluster *(computed)* | C12 |
| core count *(computed)* | 2 |
| mechanic count *(computed)* | 5 |

## Summary

A minimalist subway-design game where the player draws and redraws lines between shape-coded stations under a weekly ration of trains and tunnels until a station overcrowds.

## Core Loop

new stations appear -> draw or reroute lines -> trains carry shape-matched passengers -> weekly grant of new assets -> demand outgrows capacity -> a station overcrowds and the run ends

## Design Notes

Mini Metro abstracts a metro network into station shapes, passengers drawn as the shape of the station type they want to reach, and a scarce inventory of lines, locomotives, tunnels, and bridges. New stations keep appearing while supply arrives only as a weekly grant, so the player keeps redrawing a network that is always under capacity. Failure is local and visible: a station over its limit (typically six passengers) for long enough ends the run. Modes vary the rules: Extreme fixes lines once placed, Endless removes overcrowding, and Creative is a sandbox.

## Relations

**uses**

- [Public transit lines](../mechanic/public-transit.md) (core): The player draws colored lines between stations and assigns trains that load and unload automatically; ridership is the score.
- [Service queues](../mechanic/service-queues.md) (core): Passengers wait at stations with limited capacity, typically six; interchanges raise capacity and loading speed, and a station overcrowded too long ends the game.
- [Agent pathfinding](../mechanic/agent-pathfinding.md) (supporting): Passengers ride to any station of their target shape, transferring between lines when needed.
- [Periodic ticks](../mechanic/periodic-ticks.md) (supporting): Each in-game week grants extra rolling stock and a choice of assets such as tunnels, bridges, new lines, or interchanges.
- [Pause and speed control](../mechanic/variable-speed.md) (supporting): Time can be paused to reroute lines or move trains.

## Sources

- [Mini Metro (video game)](../source/src-wikipedia-mini-metro.md)

---
Provenance: created in run `2026-10-24-catalog-ge`.
