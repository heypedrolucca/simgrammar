# Asynchronous shared regions

*Mechanic* · `async-shared-region` · status: **sourced**

Separate players' simulations affect each other asynchronously through shared regions, visits, or exchanges of goods and services.

| field | value |
|---|---|
| aliases | asynchronous multiplayer, region play, shared region |
| family | Multiplayer & persistence |
| substrate | Network / graph, Aggregate stocks |
| math basis | Network flow, Game theory |
| feedback | Both |
| player interface | Parameter, Placement |
| legibility | 3 |
| emergence potential | 3 |
| authoring cost | 2 |
| compute cost | 2 |
| tuning difficulty | 3 |
| ai leverage | 3 |
| maturity | Established |
| core count *(computed)* | 1 |
| earliest game *(computed)* | [Nintendogs](../game/nintendogs.md) |
| earliest year *(computed)* | 2005 |
| prevalence *(computed)* | 4 |
| prevalence share *(computed)* | 0.023 |
| subgenre spread *(computed)* | 4 |
| technique count *(computed)* | 0 |
| technique exposure *(computed)* | 0.0 |

## Definition

Each player runs a local simulation that publishes a small exported state to a server, such as surplus resources, service capacity, pollution, or a snapshot of a town, and periodically imports neighbors' exported state as boundary conditions. Exchanges resolve with delay, so play does not require both players online at once. In SimCity (2013), cities in a region connect by highways, rail, and waterways, trade resources, share services such as garbage collection or health care, see traffic and pollution cross borders, and pool wealth into Great Works such as an arcology; the connection was asynchronous, with brief disruptions tolerated. Animal Crossing island visits and Death Stranding's shared structures are related forms. Inputs: local surpluses and needs. Outputs: imported flows and shared projects.

## Player Experience

The player is part of a neighborhood without coordinating schedules. They specialize, relying on neighbors for what they lack, and notice others' choices arrive as traffic, pollution, or help. Cooperation feels light because commitments are small and delayed.

## Design Levers

- which variables are exported and imported (goods, services, pollution, visitors)
- synchronization interval and conflict resolution
- region size and how neighbors are matched (friends, public, random)
- shared projects that require pooled contributions
- fallback behavior when the server or a neighbor is offline

## Failure Modes

- Server dependence makes single-player play fragile; SimCity (2013) launched with outages and save problems, and an offline mode came later.
- Abandoned neighbor cities leave dependent players short of the services they relied on.
- Small play areas forced by the region design made specialization a necessity rather than a choice, which players criticized.

## Dynamics

- Specialization emerges: one city goes industrial or hosts the hospital and the others import those services.
- Externalities such as pollution and traffic cross borders, creating friction between players who never speak.
- Shared projects create focal points that coordinate otherwise independent players.

## Open Questions

- Can AI-controlled stand-in neighbors, trained on real player cities, keep regions alive when players leave?
- What exchange latency preserves the feeling of a shared region while keeping each player's simulation independent?

## Backlinks (computed)

**involved in:** [Agent ambassadors between player worlds](../opportunity/agent-ambassadors-async.md)

**used by:** [Nintendogs](../game/nintendogs.md), [SimCity (2013)](../game/simcity-2013.md), [Tomodachi Life](../game/tomodachi-life.md), [Viva Piñata](../game/viva-pinata.md)

## Sources

- [SimCity (2013 video game)](../source/src-wikipedia-simcity-2013.md)

---
Provenance: created in run `2026-10-24-taxonomy-m7`; reviewed in `2026-10-24-review-fixes`.
