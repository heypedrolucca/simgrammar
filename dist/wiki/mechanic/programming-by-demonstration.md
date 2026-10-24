# Programming by demonstration

*Mechanic* · `programming-by-demonstration` · status: **sourced**

An agent or vehicle learns a routine by recording the player performing it, and the recording becomes a replayable, sometimes editable, program.

| field | value |
|---|---|
| aliases | teach by example, record and replay, macro recording |
| family | Control & automation |
| substrate | Player-authored logic, Agent-based |
| math basis | Computation theory |
| feedback | Reinforcing (positive) |
| player interface | Direct manipulation, Programming |
| legibility | 4 |
| emergence potential | 2 |
| authoring cost | 2 |
| compute cost | 1 |
| tuning difficulty | 2 |
| ai leverage | 4 |
| maturity | Emerging |
| core count *(computed)* | 1 |
| earliest game *(computed)* | [Autonauts](../game/autonauts.md) |
| earliest year *(computed)* | 2019 |
| prevalence *(computed)* | 2 |
| prevalence share *(computed)* | 0.011 |
| subgenre spread *(computed)* | 2 |
| technique count *(computed)* | 2 |
| technique exposure *(computed)* | 0.438 |

## Definition

Owns a recording session (the agent being taught and the sequence of player actions or positions captured so far) and the resulting routine. While recording, each player action is generalized into a step that names an action and a target class or place rather than one specific object; the agent then replays the routine, often in a loop, and the player may edit it. Autonauts bots watch the player perform a task and record it as blocks in a Scratch-style visual language, which the player wraps in repeat loops and conditions, and the bot's head caps program length. Satisfactory trucks and tractors repeat a route the player records by driving it once, stopping at truck stations. Unlike player-programming, the player does not write code to create the routine; unlike blueprints, which snapshot a spatial layout, a recording captures a sequence over time. Inputs: player actions while recording and later edits. Outputs: an autonomous routine, and its failures when the world no longer matches the recording.

## Player Experience

Teaching instead of coding. The player shows a bot how to chop a tree or drives a delivery once, then watches it repeat the job, which makes automation approachable for players who have never programmed. The surprise comes when the routine generalizes the wrong thing, such as returning to a spot where the resource is already gone.

## Design Levers

- how actions are generalized: exact positions, nearest object of a type, or named areas
- whether recordings become editable programs with loops and conditions or stay opaque replays
- program length caps and how agent upgrades raise them
- recovery behavior when a step fails: skip, wait, or stop
- whether one recording can be copied to many agents

## Failure Modes

- Over-literal recording replays positions after the world has changed, so routines break silently.
- Opaque replays with no editing force players to re-record a whole routine for one small change.
- Recorded vehicle routes drift or collide when terrain or traffic differs from the recording run.

## Dynamics

- Each taught agent frees player time to teach the next, so automation grows quickly once the first routine works.
- Players pick up programming concepts such as loops and conditions by editing what they demonstrated.
- Fleets of copied routines amplify any flaw in the original recording.

## Open Questions

- Can learned imitation policies generalize a single demonstration to new layouts while staying predictable and editable?
- Does editing a demonstrated routine teach programming better than writing code from a blank page?

## Backlinks (computed)

**affected by:** [Generalist instructable game agents (SIMA)](../technique/generalist-game-agents.md), [LLM-written skill libraries (Voyager)](../technique/voyager-skill-libraries.md)

**used by:** [Autonauts](../game/autonauts.md), [Satisfactory](../game/satisfactory.md)

## Sources

- [Autonauts](../source/src-steam-2026-autonauts.md)
- [OUT NOW: Autonauts (Denki)](../source/src-scottishgames-2019-autonauts-out-now.md)
- [Bots](../source/src-autonautswiki-2026-bots.md)

---
Provenance: created in run `2026-10-24-taxonomy-triage-b`.
