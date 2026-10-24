# History chronicle

*Mechanic* · `history-chronicle` · status: **sourced**

The game records significant simulation events into a structured history that players can browse and other systems can reference.

| field | value |
|---|---|
| aliases | legends, event log, tales |
| family | Narrative & generation |
| substrate | Rule system, UI layer |
| math basis | Information theory |
| feedback | None |
| player interface | Observation only |
| legibility | 4 |
| emergence potential | 3 |
| authoring cost | 2 |
| compute cost | 2 |
| tuning difficulty | 1 |
| ai leverage | 4 |
| maturity | Established |
| core count *(computed)* | 1 |
| earliest game *(computed)* | [Out of the Park Baseball](../game/out-of-the-park-baseball.md) |
| earliest year *(computed)* | 1999 |
| prevalence *(computed)* | 2 |
| prevalence share *(computed)* | 0.011 |
| subgenre spread *(computed)* | 2 |
| technique count *(computed)* | 1 |
| technique exposure *(computed)* | 0.375 |

## Definition

A recorder subscribes to simulation events, filters them by significance, and stores structured records (actor, action, target, place, time, cause) indexed by entity. Browsers present the records as biographies, site histories, and timelines; some games feed records back into play. Dwarf Fortress Legends mode lists historical figures, sites, artifacts, written works, regions, and civilizations, with Chronicles by Age, records the player's own fortress and adventurer achievements, and exports XML that can reach about a gigabyte for long histories. RimWorld records tales that its art system uses to describe what a sculpture depicts. Inputs: the event stream. Outputs: a queryable archive, generated descriptions, and knowledge that agents or items can carry.

## Player Experience

Looking back over a run turns scattered events into a story. Players browse to find out who caused what, discover that a minor figure had a long history, and retell their runs to others. When chronicles feed art or rumors, players see their own history reflected inside the world.

## Design Levers

- significance filter: which event types and thresholds get recorded
- record granularity and causal links between records
- retention policy and summarization as the archive grows
- presentation: raw log, templated prose, timeline, or map
- feedback paths: art, books, rumors, or agent knowledge drawn from the archive
- export formats for external tools

## Failure Modes

- Recording everything floods the archive with trivial entries and very large files.
- Templated, tabular text is dry, so most players never open the browser.
- Records without causal links list events but do not explain why they happened.

## Dynamics

- Players reconstruct and embellish stories from sparse records, and communities share them as written retellings.
- Fed back into the world, records let artworks, books, and rumors reference real past events.
- Third-party legends viewers and map tools grow around exported data.

## Open Questions

- Can language models turn structured event logs into faithful narrative summaries that do not invent causes?
- Which significance measures best predict the events players later retell?

## Relations

**synergy**

- [Storyteller director](../mechanic/storyteller-director.md): Directed incidents become chronicle entries, so pacing produces a retellable history.
- [Simulated history generation](../mechanic/history-generation.md): Pre-play generated history populates the same archive that records play (Dwarf Fortress legends).

## Backlinks (computed)

**affected by:** [LLM explanation of simulation state](../technique/llm-explanation-of-state.md)

**involved in:** [Why-query over the simulation log](../opportunity/causal-why-query.md), [Drama-aware storyteller](../opportunity/drama-aware-storyteller.md), [Generated dream and replay views](../opportunity/dream-replay-layer.md), [Event-sourced simulation runtime](../opportunity/event-sourced-sim-runtime.md), [Illustrated chronicles](../opportunity/illustrated-chronicles.md), [Language-agent society terrarium](../opportunity/llm-society-terrarium.md), [Placement that tells stories](../opportunity/placement-that-tells-stories.md)

**used by:** [Dwarf Fortress](../game/dwarf-fortress.md), [Out of the Park Baseball](../game/out-of-the-park-baseball.md)

## Sources

- [Legends](../source/src-dfwiki-2026-legends.md)
- [Dwarf Fortress](../source/src-wikipedia-dwarf-fortress.md)

---
Provenance: created in run `2026-10-24-taxonomy-m7`.
