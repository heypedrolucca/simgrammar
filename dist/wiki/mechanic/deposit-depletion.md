# Deposit depletion

*Mechanic* · `deposit-depletion` · status: **sourced**

Extractable deposits hold finite quantities and run out, forcing expansion, relocation, or substitution.

| field | value |
|---|---|
| aliases | finite resources, resource exhaustion, ore depletion |
| family | Resources & production |
| substrate | Aggregate stocks, Cellular grid |
| math basis | System dynamics / ODEs, Optimization |
| feedback | Balancing (negative) |
| player interface | Observation only, Placement |
| legibility | 4 |
| emergence potential | 3 |
| authoring cost | 1 |
| compute cost | 1 |
| tuning difficulty | 3 |
| ai leverage | 1 |
| maturity | Classic |
| requires | [Resource extraction](../mechanic/resource-extraction.md) |
| core count *(computed)* | 1 |
| earliest game *(computed)* | [Transport Tycoon](../game/transport-tycoon.md) |
| earliest year *(computed)* | 1994 |
| prevalence *(computed)* | 5 |
| prevalence share *(computed)* | 0.029 |
| subgenre spread *(computed)* | 5 |
| technique count *(computed)* | 0 |
| technique exposure *(computed)* | 0.0 |

## Definition

Each deposit holds a remaining quantity that every extraction cycle decrements. At zero the node disappears or the extractor stops; some games instead decay the extraction rate toward a floor. Factorio ore patches store an amount per tile that mining drills consume, while crude oil fields report a yield percentage in which 1% equals 300 pumpjack cycles and depletion stops at a 20% floor. Warcraft and Age of Empires gold mines and The Settlers II mountain mines run dry. Satisfactory is the counterexample: its nodes are infinite and differ only in purity. Inputs: extraction cycles. Outputs: remaining amount, current rate, and an exhaustion event that idles the extractors and any chain they feed.

## Player Experience

A visible timer the player cannot stop. Every mine is temporary, so the player keeps scouting, claiming, and rebuilding at new sites, and judges how much infrastructure a deposit deserves given how long it will last. Losing a key deposit mid-chain creates a scramble to relocate before stocks run out.

## Design Levers

- starting quantity per deposit and its distribution across the map
- whether depletion ends output or decays the rate toward a floor
- efficiency upgrades that change output per unit removed, such as Factorio mining productivity research
- visibility of remaining amounts and warnings before exhaustion
- whether deposits regenerate, can be rediscovered, or have substitutes

## Failure Modes

- Depletion that is too fast makes relocation the whole game and punishes building anything permanent.
- Depletion that is too slow is never felt within a session.
- Hidden remaining amounts cause sudden collapses that read as bugs.
- Infinite nodes or high rate floors remove expansion pressure, so the map stops mattering after the first claims.

## Dynamics

- Pushes expansion outward, which raises defense, logistics, and threat costs at new outposts.
- Creates contested chokepoints in competitive maps as the last deposits run out.
- Drives substitution toward recycling, alternate recipes, or trade once local supply ends.
- Staggers rebuild cycles, giving long games a rhythm of boom at new sites and decline at old ones.

## Open Questions

- Can procedural geology models generate deposits whose size players can estimate from surface signals, turning prospecting into inference?
- What depletion time relative to session length keeps relocation interesting rather than tedious?

## Relations

**requires**

- [Resource extraction](../mechanic/resource-extraction.md)

## Backlinks (computed)

**used by:** [Aurora 4X](../game/aurora-4x.md), [Factorio](../game/factorio.md), [SimCity (2013)](../game/simcity-2013.md), [The Long Dark](../game/the-long-dark.md), [Transport Tycoon](../game/transport-tycoon.md)

## Sources

- [Crude oil](../source/src-factoriowiki-2026-crude-oil.md)
- [Resource node](../source/src-satisfactorywiki-2026-resource-node.md)

---
Provenance: created in run `2026-10-24-taxonomy-m1`.
