# Generative decoration catalogs

*Opportunity* · `generative-decoration-catalogs` · status: **asserted**

Let players generate furniture, scenery, and building pieces from text or sketches within a game's style and technical budgets, removing the cap on creative-mode catalogs.

| field | value |
|---|---|
| opportunity type | Mechanic upgrade |
| involves | [Decoration and beauty](../mechanic/decoration-beauty.md), [Building placement](../mechanic/free-placement.md), [Content sharing](../mechanic/content-sharing.md), [Room recognition](../mechanic/room-recognition.md) |
| applies | [Text- and image-to-3D asset generation](../technique/text-to-3d-assets.md), [3D Gaussian Splatting](../technique/gaussian-splatting.md), [Grammar-constrained decoding for valid game actions](../technique/constrained-decoding.md) |
| precedent | [The Sims 4](../game/the-sims-4.md), [Planet Coaster](../game/planet-coaster.md), [inZOI](../game/inzoi.md), [Minecraft](../game/minecraft.md), [Tiny Glade](../game/tiny-glade.md) |
| novelty | 2 |
| feasibility | 4 |
| impact | 3 |
| horizon | Now |
| key risks | Copyright and trademark in generated pieces., Player and press backlash against generated assets., Gameplay tags misassigned to generated objects. |
| falsifiable signal | {'prediction': 'A life or management sim other than inZOI will let players generate new placeable 3D objects from text or images.', 'resolve_by': '2027-12-31', 'criteria': 'Feature first shipped after 2026-10-24 in a life or management sim other than inZOI with at least 5,000 Steam user reviews or a console release; store page or patch notes describe player-facing text-to-3D or image-to-3D object generation inside the game.'} |
| priority *(computed)* | 3.059 |

## Summary

Let players generate furniture, scenery, and building pieces from text or sketches within a game's style and technical budgets, removing the cap on creative-mode catalogs.

## Thesis

Creative-mode sims (The Sims build mode, Planet Coaster scenery, Townscaper-likes) live on catalog breadth, which is bounded by art budgets and DLC schedules. Text-to-3D asset generation reached production use in 2025, and style-constrained pipelines can enforce polygon budgets, collision, and art direction. Generated pieces then feed decoration scores and sharing.

## Design Sketch

A generate button in build mode takes a prompt or sketch, produces three candidates in the game's style, auto-fits collision and placement metadata, and assigns gameplay tags (seating, light, beauty value) from a classifier. Players share pieces with provenance labels.

## Key Risks

- Copyright and trademark in generated pieces.
- Player and press backlash against generated assets.
- Gameplay tags misassigned to generated objects.

## Validation Experiment

Generate 200 decor items from player prompts within a game's style guide; have artists rate style match and check technical budgets. Success: 80 percent pass technical budgets and a majority rated on-style.

## Falsifiable signal

- **Prediction:** A life or management sim other than inZOI will let players generate new placeable 3D objects from text or images.
- **Resolve by:** 2027-12-31
- **Criteria:** Feature first shipped after 2026-10-24 in a life or management sim other than inZOI with at least 5,000 Steam user reviews or a console release; store page or patch notes describe player-facing text-to-3D or image-to-3D object generation inside the game.

## Relations

**applies**

- [Text- and image-to-3D asset generation](../technique/text-to-3d-assets.md)
- [3D Gaussian Splatting](../technique/gaussian-splatting.md)
- [Grammar-constrained decoding for valid game actions](../technique/constrained-decoding.md)

**involves**

- [Decoration and beauty](../mechanic/decoration-beauty.md)
- [Building placement](../mechanic/free-placement.md)
- [Content sharing](../mechanic/content-sharing.md)
- [Room recognition](../mechanic/room-recognition.md)

**precedent**

- [The Sims 4](../game/the-sims-4.md)
- [Planet Coaster](../game/planet-coaster.md)
- [inZOI](../game/inzoi.md)
- [Minecraft](../game/minecraft.md)
- [Tiny Glade](../game/tiny-glade.md)

---
Provenance: created in run `2026-10-24-synthesis`; reviewed in `2026-10-24-review-fixes`.
