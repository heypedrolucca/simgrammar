# Reputation

*Mechanic* · `reputation` · status: **sourced**

A standing value with a faction or the public changes access, prices, and how others respond.

| field | value |
|---|---|
| aliases | standing, fame, renown |
| family | Social relations |
| substrate | Aggregate stocks, Rule system |
| math basis | System dynamics / ODEs, Game theory |
| feedback | Reinforcing (positive) |
| player interface | Observation only, Choice / cards |
| legibility | 4 |
| emergence potential | 3 |
| authoring cost | 2 |
| compute cost | 1 |
| tuning difficulty | 3 |
| ai leverage | 3 |
| maturity | Classic |
| core count *(computed)* | 5 |
| earliest game *(computed)* | [Elite](../game/elite.md) |
| earliest year *(computed)* | 1984 |
| prevalence *(computed)* | 22 |
| prevalence share *(computed)* | 0.126 |
| subgenre spread *(computed)* | 14 |
| technique count *(computed)* | 1 |
| technique exposure *(computed)* | 0.188 |

## Definition

Owns a scalar or small vector (fame, infamy, honor) for the player or an organization, held per faction or globally, that rises and falls with witnessed or reported acts and often decays toward neutral. Unlike pairwise relationships it is the many-to-one view others hold of one actor, read by rules that gate access (quests, ranks, shops), set prices or acceptance odds, and change NPC reactions. Crusader Kings III tracks character prestige and dynasty renown as standing currencies; Europa Universalis IV diplomatic reputation adds 5 to alliance acceptance per point; RimWorld faction goodwill doubles as reputation by gating trade, caravans, and military aid. Inputs: acts and who observed them. Outputs: modifiers on prices, recruitment, acceptance, aggression, and unlocks.

## Player Experience

The player cultivates a public identity and feels its weight when doors open or close. Reputation makes past choices follow the player into new encounters and creates tension between profitable acts and standing.

## Design Levers

- per-faction versus global scope, and whether there are separate fame and infamy axes
- magnitude per act and whether acts need witnesses or reports
- decay toward neutral and its rate
- threshold tiers and what each unlocks or blocks
- spillover between allied or rival factions

## Failure Modes

- Reputation grinding: repeating cheap acts maxes standing without meaningful choices.
- Global reputation without witnesses means everyone knows everything instantly, which breaks plausibility.
- Tiers that only unlock shops make reputation a currency, not an identity.
- Irreversible collapse locks players out of content with no repair path.

## Dynamics

- Good standing opens trade and quests that further raise standing, a reinforcing loop.
- Opposed factions turn every gain with one into a loss with the other, forcing alignment choices.
- When reputation spreads by gossip, information lag creates windows for crime before word gets out.

## Open Questions

- Can reputation be carried in language-model NPCs' remembered accounts of the player rather than in a number, and still gate content predictably?
- Should reputation be a property of the actor or of each observer's beliefs about the actor?

## Backlinks (computed)

**affected by:** [Language models grounded in strategic planning for negotiation games](../technique/cicero-strategic-dialogue.md)

**involved in:** [Negotiating faction AI](../opportunity/negotiating-faction-ai.md)

**used by:** [Anno 117: Pax Romana](../game/anno-117.md), [Balance of Power](../game/balance-of-power.md), [Bitburner](../game/bitburner.md), [Black & White](../game/black-and-white.md), [Caesar III](../game/caesar-3.md), [Caves of Qud](../game/caves-of-qud.md), [Elite](../game/elite.md), [Elite Dangerous](../game/elite-dangerous.md), [Europa Universalis IV](../game/europa-universalis-4.md), [EVE Online](../game/eve-online.md), [Football Manager](../game/football-manager.md), [Game Dev Tycoon](../game/game-dev-tycoon.md), [Jurassic World Evolution](../game/jurassic-world-evolution.md), [Kenshi](../game/kenshi.md), [Kerbal Space Program](../game/kerbal-space-program.md), [Microsoft Flight Simulator 2024](../game/microsoft-flight-simulator-2024.md), [Planet Zoo](../game/planet-zoo.md), [Space Haven](../game/space-haven.md), [Theme Hospital](../game/theme-hospital.md), [Transport Tycoon](../game/transport-tycoon.md), [Ultima Online](../game/ultima-online.md), [Where Winds Meet](../game/where-winds-meet.md)

## Sources

- [Diplomacy](../source/src-paradoxwikis-2026-eu4-diplomacy.md)
- [Goodwill](../source/src-rimworldwiki-2026-goodwill.md)
- [Crusader Kings III](../source/src-wikipedia-crusader-kings-3.md)

---
Provenance: created in run `2026-10-24-taxonomy-m3`.
