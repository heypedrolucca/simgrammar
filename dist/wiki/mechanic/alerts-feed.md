# Alerts feed

*Mechanic* · `alerts-feed` · status: **asserted**

A notification layer surfaces discrete events and threshold crossings with severity and a link to their location.

| field | value |
|---|---|
| aliases | notifications, letters, announcements, event log |
| family | Information & legibility |
| substrate | UI layer, Rule system |
| math basis | Information theory |
| feedback | None |
| player interface | Observation only |
| legibility | 4 |
| emergence potential | 1 |
| authoring cost | 2 |
| compute cost | 2 |
| tuning difficulty | 2 |
| ai leverage | 3 |
| maturity | Classic |
| core count *(computed)* | 0 |
| earliest game *(computed)* | [Balance of Power](../game/balance-of-power.md) |
| earliest year *(computed)* | 1985 |
| prevalence *(computed)* | 3 |
| prevalence share *(computed)* | 0.017 |
| subgenre spread *(computed)* | 3 |
| technique count *(computed)* | 0 |
| technique exposure *(computed)* | 0.0 |

## Definition

The feed subscribes to simulation events (raid arrived, agent died, contract completed) and to condition predicates over state (food below a threshold, building unpowered, storage full, entity damaged). It owns a list of active alerts, each with type, severity, timestamp, a deduplication key, a location or entity link, and a lifetime. Each tick it adds an alert on the rising edge of a predicate or on an event, merges alerts with the same key, removes condition alerts when the condition clears, and expires event alerts after a timeout or dismissal. Optional rules pause the game or drop speed on chosen types. Canonical forms: RimWorld's severity-colored event letters plus a persistent condition list (low food, colonist needs rescue), Factorio alerts for entities under attack or destroyed, trains out of fuel, and ghosts lacking construction materials, problem icons over buildings and the Chirper feed in Cities: Skylines, Dwarf Fortress announcements, and the Football Manager inbox.

## Player Experience

In a system too large to watch, the feed decides where the player looks. The player triages, jumps the camera to the alert, and learns to dread specific alert types. Auto-pause on alerts turns real-time play into a series of decision points.

## Design Levers

- event alerts versus persistent condition alerts that clear themselves
- severity tiers, color, and sound per alert type
- auto-pause or speed-drop rules per alert type
- aggregation: one alert for many identical problems versus one per entity
- persistence until dismissed versus until the condition clears
- click-through to location and player-side filtering
- in-fiction framing (social posts, letters) versus neutral system text

## Failure Modes

- Alert fatigue: frequent low-value alerts bury the one that matters, and players miss a fatal problem.
- In-fiction feeds read as noise; many Cities: Skylines players hid the Chirper feed with mods.
- Predicates near a threshold, such as power just at capacity, flicker and spam add and remove cycles.
- Alerts that report symptoms (no goods) rather than causes send players to fix the wrong thing.

## Dynamics

- The alert set encodes what the designer considers a problem, so players optimize to keep icons off rather than toward their own goals.
- With auto-pause, alert density sets the effective pacing of a real-time game.
- Paired with an event director, alerts announcing incident arrival create a recognizable beat structure of calm, alarm, and response.

## Open Questions

- Can a learned salience model rank and merge alerts by predicted consequence so the feed stays useful at megabase or metropolis scale?
- Do natural-language digests of many alerts help players more than icons, or do they slow reaction time?

## Backlinks (computed)

**involved in:** [Why-query over the simulation log](../opportunity/causal-why-query.md)

**used by:** [Balance of Power](../game/balance-of-power.md), [Plague Inc.](../game/plague-inc.md), [Tamagotchi](../game/tamagotchi.md)

---
Provenance: created in run `2026-10-24-taxonomy-m6`.
