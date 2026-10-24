# Stimulus attraction

*Mechanic* · `stimulus-attraction` · status: **sourced**

Player actions emit sound or light stimuli with a radius and decay, and agents that perceive them move toward the source, so managing emissions is part of survival.

| field | value |
|---|---|
| aliases | noise attraction, sound propagation, aggro by noise, hearing and sight perception |
| family | Risk & failure |
| substrate | Agent-based, Cellular grid |
| math basis | Information theory, Probability / statistics |
| feedback | Reinforcing (positive) |
| player interface | Direct manipulation, Observation only |
| legibility | 3 |
| emergence potential | 4 |
| authoring cost | 1 |
| compute cost | 2 |
| tuning difficulty | 3 |
| ai leverage | 3 |
| maturity | Established |
| core count *(computed)* | 1 |
| earliest game *(computed)* | [Project Zomboid](../game/project-zomboid.md) |
| earliest year *(computed)* | 2011 |
| prevalence *(computed)* | 2 |
| prevalence share *(computed)* | 0.011 |
| subgenre spread *(computed)* | 1 |
| technique count *(computed)* | 0 |
| technique exposure *(computed)* | 0.0 |

## Summary

Player actions emit sound or light stimuli with a radius and decay, and agents that perceive them move toward the source, so managing emissions is part of survival.

## Definition

Owns a set of active stimuli, each with a source position, type (sound, light, smell, sight of the player), intensity, radius, and decay time, plus each agent's perception thresholds and current alert target. When an action fires it emits a stimulus sized by the action (gunshot, smashed window, running, a lit fire); each update, agents within range whose perception exceeds the threshold switch to an investigate state and path toward the source, and some propagate the alert to nearby agents so groups follow. Stimuli fade, and agents that find nothing return to idle or wander. Project Zomboid zombies respond to sight and hearing, and loud actions draw them from a distance; This War of Mine shows noise from scavenging actions that can alert people nearby. Unlike fog-of-war, which hides information from the player, this mechanic models what hostile agents perceive about the player; unlike adaptive-threat-scaling, it changes where threats go, not how strong they are.

## Player Experience

Every action has an audience. The player weighs the speed of smashing a window against the zombies it will call, walks instead of running, and uses noise deliberately as a lure. Mistakes are legible and frightening: a gunshot that brings a crowd teaches the rule at once.

## Design Levers

- emission radius and intensity per action, weapon, and tool
- perception thresholds per agent type and modifiers such as weather, time of day, and walls
- stimulus decay time and how long agents investigate before giving up
- alert propagation between agents, which turns individuals into crowds or hordes
- player feedback: visible noise rings, audio cues, or no indication

## Failure Modes

- Invisible emission rules make attacks feel random when players cannot tell what they did to cause them.
- Propagation that is too strong snowballs every mistake into an unwinnable horde.
- Agents that ignore walls and distance when following sound feel omniscient and break stealth.

## Dynamics

- Players lure groups away with distractions such as alarms or thrown objects, turning the rule into a tool.
- Fighting creates noise that draws more enemies, a reinforcing loop that punishes loud tactics.
- Quiet tools and routes become valuable, shaping crafting and travel choices.

## Open Questions

- Can learned agents that reason about what they heard and saw produce searches that feel smarter without becoming omniscient?
- Does visualizing emissions improve player decisions or remove the tension of not knowing what heard you?

## Backlinks (computed)

**used by:** [Project Zomboid](../game/project-zomboid.md), [This War of Mine](../game/this-war-of-mine.md)

## Sources

- [Project Zomboid on Steam](../source/src-steam-2026-project-zomboid.md)

---
Provenance: created in run `2026-10-24-taxonomy-triage-b`.
