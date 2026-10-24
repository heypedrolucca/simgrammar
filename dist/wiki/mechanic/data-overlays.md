# Data overlays

*Mechanic* · `data-overlays` · status: **asserted**

Map layers visualize hidden variables such as land value, pollution, coverage, or traffic.

| field | value |
|---|---|
| aliases | info views, map modes, data maps, heatmaps |
| family | Information & legibility |
| substrate | UI layer, Cellular grid |
| math basis | Probability / statistics |
| feedback | None |
| player interface | Observation only |
| legibility | 4 |
| emergence potential | 1 |
| authoring cost | 2 |
| compute cost | 2 |
| tuning difficulty | 1 |
| ai leverage | 2 |
| maturity | Classic |
| core count *(computed)* | 0 |
| earliest game *(computed)* | [Balance of Power](../game/balance-of-power.md) |
| earliest year *(computed)* | 1985 |
| prevalence *(computed)* | 5 |
| prevalence share *(computed)* | 0.029 |
| subgenre spread *(computed)* | 5 |
| technique count *(computed)* | 0 |
| technique exposure *(computed)* | 0.0 |

## Definition

A map mode recolors the world by one per-cell, per-building, or per-segment field: land value, pollution concentration, crime, service coverage, traffic volume or speed, power and water connectivity, temperature, gas composition, germs, or political ownership. It owns no simulation state; it samples a field and maps it through a color ramp or categorical palette, sometimes adding glyphs such as flow arrows. Update rule: when active, sample the field each frame or on change and redraw; some games switch an overlay on automatically when the player places a related building. Canonical forms: the data maps of SimCity and SimCity 2000, Cities: Skylines info views, the oxygen, temperature, power, plumbing, decor, and germ overlays of Oxygen Not Included, Factorio's pollution cloud on the map view, and the map modes of Europa Universalis IV.

## Player Experience

A hunch becomes a picture. The player sees the shape of a hidden field, such as a pollution plume or a coverage gap, and responds spatially by moving, adding, or separating buildings. Overlays are the main debugging tool for layout.

## Design Levers

- which fields get an overlay, since exposing a field makes it an optimization target
- continuous gradient versus thresholded bands
- fixed absolute scale versus auto-normalized to the current map range
- automatic display while placing a related building
- instantaneous value versus time-averaged value
- single overlay at a time versus composites, and colorblind-safe palettes

## Failure Modes

- Auto-normalized color ramps make a minor problem look red and a severe one look identical.
- Overlays without legends or units show where something is high but not how high.
- Overlays of fields with hidden formulas, such as land value, show where but not why.
- Red-green ramps are unreadable for many colorblind players.

## Dynamics

- An exposed field becomes a painting target: players lay out coverage grids until no red remains.
- Visible spatial externalities push players toward land-use separation, such as industry far from housing.
- In games with diffusing fields (heat, gas), overlays are how players discover emergent flows they did not intend.

## Open Questions

- Can automated annotation of overlays (this plume originates from these three sources) close the gap between where and why?
- Which fields should stay without an overlay to preserve discovery and uncertainty?

## Relations

**synergy**

- [Pollution spread](../mechanic/pollution-spread.md): Overlays make invisible diffusion fields legible.
- [Traffic congestion](../mechanic/traffic-congestion.md): Traffic overlays turn congestion from a vague complaint into a located problem.
- [Service coverage](../mechanic/service-coverage.md): Coverage overlays show gaps that would otherwise surface only as complaints.
- [Land value](../mechanic/land-value.md): Land value maps are the canonical city-builder overlay.

**tension**

- [Fog of war](../mechanic/fog-of-war.md): Full-information overlays undercut hidden-information play; games must choose what to reveal.

## Backlinks (computed)

**involved in:** [Bottleneck explainer for production networks](../opportunity/bottleneck-explainer.md), [Branch preview of policy futures](../opportunity/branch-preview-forecasts.md), [Participatory planning sandboxes](../opportunity/participatory-planning-sandboxes.md), [Symbolic simulation, neural rendering](../opportunity/symbolic-sim-neural-render.md)

**used by:** [Balance of Power](../game/balance-of-power.md), [Oxygen Not Included](../game/oxygen-not-included.md), [SimCity](../game/simcity-1989.md), [SimEarth](../game/simearth.md), [Universe Sandbox](../game/universe-sandbox.md)

---
Provenance: created in run `2026-10-24-taxonomy-m6`.
