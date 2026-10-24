# Habitat suitability

*Mechanic* · `habitat-suitability` · status: **asserted**

Species or crops thrive only where conditions such as terrain, temperature, water, and cover match their needs, scored per location.

| field | value |
|---|---|
| aliases | biome requirements, habitat requirements, fertility |
| family | Environment & ecology |
| substrate | Cellular grid, Rule system |
| math basis | Utility / decision theory, Population dynamics |
| feedback | None |
| player interface | Placement, Observation only |
| legibility | 4 |
| emergence potential | 2 |
| authoring cost | 2 |
| compute cost | 1 |
| tuning difficulty | 2 |
| ai leverage | 2 |
| maturity | Established |
| open questions | Can species distribution models learned from ecological data generate plausible, varied requirement profiles for procedurally generated species? |
| core count *(computed)* | 4 |
| earliest game *(computed)* | [Populous](../game/populous.md) |
| earliest year *(computed)* | 1989 |
| prevalence *(computed)* | 12 |
| prevalence share *(computed)* | 0.069 |
| subgenre spread *(computed)* | 7 |
| technique count *(computed)* | 0 |
| technique exposure *(computed)* | 0.0 |

## Definition

Owns a preference profile per species or crop (acceptable ranges or targets for terrain type, temperature, humidity, water, foliage, space, and company) and computes a suitability score for each tile, region, or enclosure by comparing local conditions to the profile, often as a weighted sum or as the worst single factor. The score gates where things can be placed or survive and scales growth, yield, welfare, or breeding. Zoo Tycoon and Planet Zoo grade each enclosure on terrain mix, foliage, area, and biome for each animal; Anno 1800 gives each island fertilities that decide which crops it can farm; Viva Pinata spawns a species only when the garden meets its requirements. Inputs are terrain and climate state; outputs are a scalar per location used by other systems.

## Player Experience

Matching puzzles on the map. The player reads a species' or crop's profile, then sculpts terrain, plants foliage, or picks locations until the indicator turns green. Unmet requirements show up as unhappy animals or missing harvests, so the player iterates on the place rather than on the creature.

## Design Levers

- number of factors in the profile and how narrow each acceptable range is
- combination rule: weighted average, product, or worst single factor
- hard gate on placement versus soft multiplier on growth or welfare
- how the score is shown: checklist, percentage, overlay, or only through outcomes
- whether conditions change at runtime through seasons, climate, or terraforming

## Failure Modes

- Checklists with exact percentages become form-filling once the player knows the threshold values.
- Averaging factors lets a perfect score on one factor hide a fatal mismatch on another.
- Static suitability makes each location solved once, removing reasons to revisit it.

## Dynamics

- Different profiles force specialization by location, which drives trade between regions or islands.
- Coupled with climate or seasons, suitable areas move and populations must migrate or be relocated.
- Players terraform to manufacture suitability, creating demand for terrain tools and materials.

## Open Questions

- Can species distribution models learned from ecological data generate plausible, varied requirement profiles for procedurally generated species?

## Relations

**synergy**

- [Terraforming](../mechanic/terraforming.md): Terrain edits change biome conditions, letting the player engineer habitats (Terra Nil, Equilinox).

## Backlinks (computed)

**involved in:** [Open-ended evolution sandbox](../opportunity/open-ended-evolution-sandbox.md)

**used by:** [Aurora 4X](../game/aurora-4x.md), [Equilinox](../game/equilinox.md), [Plague Inc.](../game/plague-inc.md), [Planet Zoo](../game/planet-zoo.md), [Populous](../game/populous.md), [Seaman](../game/seaman.md), [SimEarth](../game/simearth.md), [SimLife](../game/simlife.md), [Species: Artificial Life, Real Evolution](../game/species-alre.md), [Terra Nil](../game/terra-nil.md), [Viva Piñata](../game/viva-pinata.md), [Zoo Tycoon](../game/zoo-tycoon.md)

---
Provenance: created in run `2026-10-24-taxonomy-m5`.
