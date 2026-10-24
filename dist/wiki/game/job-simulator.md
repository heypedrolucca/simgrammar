# Job Simulator

*Game* · `job-simulator` · status: **sourced**

A room-scale VR comedy set in a museum run by robots, where the player performs parodied office, kitchen, store, and garage tasks by grabbing and manipulating physics objects.

| field | value |
|---|---|
| aliases | Job Simulator: The 2050 Archives |
| year | 2016 |
| developer | Owlchemy Labs |
| platforms | PC, Console, VR |
| subgenre | Job sim |
| subgenre secondary | Physics sandbox |
| sim domain | Occupational, Physical / mechanical |
| player role | Worker |
| agency model | Direct avatar |
| time model | Real-time |
| sim scale | Individual |
| fidelity | Abstract |
| perspective | First-person |
| win structure | Completion |
| failure model | None |
| narrative mode | Authored |
| multiplayer | Single-player |
| modding | None |
| production tier | Indie |
| agent count order | None |
| emergence | 2 |
| influence | 2 |
| boundary case | True |
| cluster *(computed)* | C07 |
| core count *(computed)* | 2 |
| mechanic count *(computed)* | 3 |

## Summary

A room-scale VR comedy set in a museum run by robots, where the player performs parodied office, kitchen, store, and garage tasks by grabbing and manipulating physics objects.

## Core Loop

job bot gives a task -> grab and manipulate objects with tracked hands -> appliances and props react physically -> task completes -> next task until the job ends

## Design Notes

Included as a boundary case for its interaction model: nearly every object within reach is a physics object that can be picked up, thrown, or combined, and fixed appliances expose buttons, levers, and dials. Tasks are authored and loose, so variety comes from physical improvisation such as choosing pizza toppings or tire styles rather than from a modeled occupation. After all four jobs, modifiers alter the physics.

## Relations

**uses**

- [Rigid-body physics](../mechanic/rigid-body-physics.md) (core): Most objects within reach can be picked up and manipulated with tracked controllers, fixed appliances expose buttons, levers, and dials, and post-game modifiers change the physics.
- [Direct avatar control](../mechanic/direct-avatar.md) (core): The player's tracked head and hands are the avatar at a room-scale workstation; a smaller human mode adjusts reach.
- [Scenario objectives](../mechanic/scenario-objectives.md) (supporting): Four jobs (Office Worker, Gourmet Chef, Store Clerk, Auto Mechanic) each run a sequence of task requests from job bots.

## Sources

- [Job Simulator](../source/src-wikipedia-job-simulator.md)

---
Provenance: created in run `2026-10-24-catalog-gf`.
