# PvP security zones

*Mechanic* · `pvp-security-zones` · status: **sourced**

A shared world is divided into zones whose rules set whether players may attack each other and what an aggressor pays, such as NPC police response or lost standing.

| field | value |
|---|---|
| aliases | security status, safe zones, PvP rulesets by region, high-sec and null-sec |
| family | Multiplayer & persistence |
| substrate | Rule system, Network / graph |
| math basis | Mechanism design / auctions, Game theory |
| feedback | Balancing (negative) |
| player interface | Direct manipulation, Observation only |
| legibility | 4 |
| emergence potential | 4 |
| authoring cost | 1 |
| compute cost | 1 |
| tuning difficulty | 4 |
| ai leverage | 2 |
| maturity | Established |
| core count *(computed)* | 1 |
| earliest game *(computed)* | [Ultima Online](../game/ultima-online.md) |
| earliest year *(computed)* | 1997 |
| prevalence *(computed)* | 2 |
| prevalence share *(computed)* | 0.011 |
| subgenre spread *(computed)* | 1 |
| technique count *(computed)* | 0 |
| technique exposure *(computed)* | 0.0 |

## Summary

A shared world is divided into zones whose rules set whether players may attack each other and what an aggressor pays, such as NPC police response or lost standing.

## Definition

Owns a security rating or ruleset per zone (star system, region, server facet) and each player's standing, such as security status or criminal flags. When one player attacks another, the zone's rules decide whether the attack is allowed, whether NPC enforcers respond and how fast, and how much standing the attacker loses; standing then limits where the attacker can travel safely. EVE Online rates each system from 1.0 to -1.0, with the CONCORD police destroying unprovoked aggressors in high-security space while low- and null-security space leaves fights to players, and the most profitable activities sit in the less secure zones. Ultima Online split its world in 2000 into Trammel, where player-versus-player combat is consensual, and Felucca, where it is open. Unlike persistent-world, which owns continuity of the shared world, this mechanic owns the spatial rules for aggression inside it.

## Player Experience

The player chooses a risk level by choosing where to go. Safe zones let new and cautious players work and trade; dangerous zones promise better rewards and real fights. Crossing a border with valuable cargo is a decision, and an attacker in safe space knows the police are coming.

## Design Levers

- number of security tiers and how rewards scale with risk across them
- enforcement: instant destruction, delayed police response, flags that make the aggressor attackable, or none
- standing penalties for aggression and how they recover
- whether players can choose a ruleset at entry, as with separate facets
- map layout of tiers, including chokepoints between safe and dangerous space

## Failure Modes

- Safe zones that cover everything valuable empty the dangerous zones, and the player-versus-player design withers.
- Delayed enforcement allows suicide attacks on rich targets in safe space when the loot exceeds the attacker's loss.
- Offering a consensual ruleset beside an open one lets most players choose safety, which can leave the open ruleset thinly populated; Ultima Online's Felucca after the Trammel split is the usual example.

## Dynamics

- Gate camps form at chokepoints where safe space meets dangerous space.
- Players stage risky ventures from safe hubs, creating hub-and-frontier geography in the economy.
- Groups organize escorts, scouts, and intelligence networks to operate in dangerous zones.

## Open Questions

- Could AI enforcers that respond to context, rather than fixed rules, curb exploits such as suicide attacks without blocking legitimate play?
- What reward gradient across tiers keeps both safe and dangerous zones populated?

## Backlinks (computed)

**used by:** [EVE Online](../game/eve-online.md), [Ultima Online](../game/ultima-online.md)

## Sources

- [Ultima Online](../source/src-wikipedia-ultima-online.md)
- [Eve Online](../source/src-wikipedia-eve-online.md)

---
Provenance: created in run `2026-10-24-taxonomy-triage-b`.
