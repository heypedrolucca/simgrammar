# Mechanic modding by description

*Opportunity* · `language-modding` · status: **asserted**

Players describe a rule change in plain language; a model writes the mod against the modding API and automated agents test it before it is shared.

| field | value |
|---|---|
| opportunity type | Authoring tool |
| involves | [Modding API](../mechanic/modding-api.md), [Content sharing](../mechanic/content-sharing.md), [Player programming](../mechanic/player-programming.md) |
| applies | [Automated generation of game rules and mechanics](../technique/automated-rule-generation.md), [Agent-based automated playtesting and balancing](../technique/automated-playtesting.md), [Grammar-constrained decoding for valid game actions](../technique/constrained-decoding.md), [LLM-written skill libraries (Voyager)](../technique/voyager-skill-libraries.md) |
| precedent | [RimWorld](../game/rimworld.md), [Minecraft](../game/minecraft.md), [Garry's Mod](../game/garrys-mod.md), [Factorio](../game/factorio.md), [Cities: Skylines](../game/cities-skylines.md) |
| novelty | 3 |
| feasibility | 4 |
| impact | 4 |
| horizon | 1-2 years |
| key risks | Generated mods with subtle bugs corrupt saves., Security of executing generated code., Flood of low-quality mods drowns curation. |
| falsifiable signal | {'prediction': 'The developer of a moddable simulation game will ship or officially endorse a tool that builds working mods from natural-language descriptions.', 'resolve_by': '2028-06-30', 'criteria': 'Shipped or announced after 2026-10-24 by the developer of a simulation game with at least 10,000 Steam user reviews and an official modding API; the tool outputs mod code or data from text descriptions.'} |
| priority *(computed)* | 3.776 |

## Thesis

Modding is how simulation games stay alive for decades, but scripting mods requires programming skill and engine knowledge. Code-generating models write working code against documented APIs, and automated playtesting agents can smoke-test results. Making 'wolves avoid fire' or 'trains prefer cheaper routes' a sentence rather than a project would enlarge the modding population by orders of magnitude.

## Design Sketch

An in-game mod workshop: the player describes the change, the system proposes a diff to data and scripts, runs a headless test scenario with agents to check for crashes and the intended effect, and shows before and after metrics. The player names and shares the mod; the description, code, and test results travel together.

## Key Risks

- Generated mods with subtle bugs corrupt saves.
- Security of executing generated code.
- Flood of low-quality mods drowns curation.

## Validation Experiment

Collect 100 mod requests from a modding community, generate mods against a documented API, and measure the share that compile, pass a headless scenario, and are judged by the requester to do what they asked. Success: at least 60 percent fully accepted.

## Falsifiable signal

- **Prediction:** The developer of a moddable simulation game will ship or officially endorse a tool that builds working mods from natural-language descriptions.
- **Resolve by:** 2028-06-30
- **Criteria:** Shipped or announced after 2026-10-24 by the developer of a simulation game with at least 10,000 Steam user reviews and an official modding API; the tool outputs mod code or data from text descriptions.

## Relations

**applies**

- [Automated generation of game rules and mechanics](../technique/automated-rule-generation.md)
- [Agent-based automated playtesting and balancing](../technique/automated-playtesting.md)
- [Grammar-constrained decoding for valid game actions](../technique/constrained-decoding.md)
- [LLM-written skill libraries (Voyager)](../technique/voyager-skill-libraries.md)

**involves**

- [Modding API](../mechanic/modding-api.md)
- [Content sharing](../mechanic/content-sharing.md)
- [Player programming](../mechanic/player-programming.md)

**precedent**

- [RimWorld](../game/rimworld.md)
- [Minecraft](../game/minecraft.md)
- [Garry's Mod](../game/garrys-mod.md)
- [Factorio](../game/factorio.md)
- [Cities: Skylines](../game/cities-skylines.md)

---
Provenance: created in run `2026-10-24-synthesis`; reviewed in `2026-10-24-review-fixes`.
