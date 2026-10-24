# Persistent shared world

*Mechanic* · `persistent-world` · status: **sourced**

A server-side world keeps running and keeps its state for many players, whether or not any one player is logged in.

| field | value |
|---|---|
| aliases | MMO world, single-shard world, living world |
| family | Multiplayer & persistence |
| substrate | Agent-based, Rule system |
| math basis | Game theory, System dynamics / ODEs |
| feedback | Reinforcing (positive) |
| player interface | Direct manipulation, Orders |
| legibility | 3 |
| emergence potential | 4 |
| authoring cost | 3 |
| compute cost | 4 |
| tuning difficulty | 5 |
| ai leverage | 3 |
| maturity | Classic |
| core count *(computed)* | 6 |
| earliest game *(computed)* | [Ultima Online](../game/ultima-online.md) |
| earliest year *(computed)* | 1997 |
| prevalence *(computed)* | 7 |
| prevalence share *(computed)* | 0.04 |
| subgenre spread *(computed)* | 4 |
| technique count *(computed)* | 1 |
| technique exposure *(computed)* | 0.188 |

## Definition

Authoritative world state lives on servers that advance it continuously in real time; clients submit actions and receive updates, and changes such as built structures, market orders, territory, and destroyed assets persist for everyone. Design choices are shard topology and what the world does while a player is away. Eve Online runs one universe on the Tranquility server rather than parallel copies, takes it offline daily for maintenance, trains character skills in real time while players are logged out, and slows the server clock in crowded systems (time dilation) so large fights stay simulated; the Bloodbath of B-R5RB ran 21 hours. Ultima Online (1997), A Tale in the Desert, Second Life, and Eco are other persistent worlds. Inputs: concurrent player actions and world rules. Outputs: shared, durable state and history.

## Player Experience

Actions matter to strangers, and the world changes while the player sleeps. Players log in to see what happened, plan around other time zones, and take part in events, such as wars or market crashes, that no single player or designer controlled.

## Design Levers

- shard topology: one universe, many parallel shards, or instanced zones
- offline progression: what continues for absent players (skills, production, decay)
- persistence scope: which changes are permanent versus reset
- server tick rate and overload handling such as time dilation or queues
- world resets, seasons, or wipes
- rules for asset loss and protection of offline players

## Failure Modes

- Early arrivals accumulate wealth and territory, and new players find no room to matter.
- Load spikes in popular locations degrade simulation for everyone present.
- Abandoned structures and items clutter the world without decay rules.
- The world dies when concurrency falls below what its systems assume.

## Dynamics

- Player-driven economies, wars, and politics emerge because consequences persist and accumulate.
- Time-zone coverage becomes a strategic resource for groups that hold territory.
- Persistent history makes notable events into community lore and news.

## Open Questions

- Can AI agents that stand in for absent players keep a persistent world active at low concurrency without dominating it?
- What offline progression rules keep a persistent world fair to players with little play time?

## Relations

**synergy**

- [Player-driven markets](../mechanic/player-driven-market.md): A persistent world lets player markets accumulate history, monopolies, and scams (EVE Online).
- [Player legislation](../mechanic/player-legislation.md): Laws only matter where the world persists long enough to need governance (Eco, A Tale in the Desert).

**tension**

- [Pause and speed control](../mechanic/variable-speed.md): A shared persistent world cannot be paused or sped up by one player.

## Backlinks (computed)

**affected by:** [Many-agent LLM societies](../technique/llm-agent-societies.md)

**involved in:** [AI liquidity in player markets](../opportunity/ai-liquidity-in-player-markets.md), [Event-sourced simulation runtime](../opportunity/event-sourced-sim-runtime.md), [Language-agent society terrarium](../opportunity/llm-society-terrarium.md)

**required by:** [Seasonal world reset](../mechanic/seasonal-world-reset.md)

**used by:** [A Tale in the Desert](../game/a-tale-in-the-desert.md), [Elite Dangerous](../game/elite-dangerous.md), [EVE Online](../game/eve-online.md), [Minecraft](../game/minecraft.md), [Screeps](../game/screeps.md), [Second Life](../game/second-life.md), [Ultima Online](../game/ultima-online.md)

## Sources

- [Eve Online](../source/src-wikipedia-eve-online.md)

---
Provenance: created in run `2026-10-24-taxonomy-m7`.
