# Vocabulary: time_model

Dominant relation between simulation time and player time.

| id | label | definition |
|---|---|---|
| `real-time` | Real-time | Simulation advances continuously at a fixed rate the player cannot pause in normal play. |
| `real-time-pausable` | Real-time with pause | Continuous time with pause and usually adjustable speed. |
| `turn-based` | Turn-based | Simulation advances in discrete player-triggered turns. |
| `real-world-clock` | Real-world clock | Simulation time is bound to the wall clock and advances while the game is closed. |
| `run-on-demand` | Run on demand | Player builds in a frozen state, then triggers a simulation run (design-then-test). |
| `asynchronous-persistent` | Asynchronous persistent | Shared world advances on servers independent of any one player's session. |
