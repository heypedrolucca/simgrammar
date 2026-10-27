# SimGrammar video: dithered visual vocabulary

Plan for replacing entity cards with infographic frames built from one set of dithered icons. Written 2026-10-26 against the repo at /home/claude/simgrammar (read only) and the renders in scratchpad/video/final. Proof images are in `proof/`; the scene-by-scene template table is `templates.csv`.

## 1. Summary

1. The 228 Picture lines (177 in episodes, 43 in shorts, 8 in the film's own scenes) sort into 11 content templates plus the existing data figures and title slates. No scene is left without a template; 3 beats inside scenes have none (section 3.3).
2. The four most used templates are compare (37 lines), count (32), chain (29) and anatomy (20). With record, moment, timeline, scale, mockup, formula and toysim they cover 188 of 228 lines; the other 40 stay data figures (26) or slates (14).
3. Today 60% of runtime in episodes and shorts is entity cards (72.6 of 121 minutes), 22% paper figures, 14% title or fallback slates, 4% the catalog grid.
4. The vocabulary that needs pictures is about 415 images: 199 mechanics, 21 families, 25 technique glyphs, 31 subgenre emblems, about 85 scene nouns, about 45 small closed-set terms, and 8 bet plates. Games and bets are drawn as layouts of these, so they need no art of their own.
5. Tier 1 is 60 images. They cover the most frequent nouns (dataset record in 38 of 191 scenes, colonist 30, needs 28, events 26, crowds 25) and the parts of the most-shown games.
6. Look: ink and one accent on Register paper, ordered 8x8 Bayer dither in five tones, 3 px per dither pixel at 16:9 and 4 px at 9:16, 48-dpx icon grid, IBM Plex type kept vector and never dithered.
7. Ordered dither is the only method that survives motion. A 1/255 brightness change flips 0.4% of pixels under Bayer 8x8 and 29% under Floyd-Steinberg, so a fade or build in error diffusion shimmers.
8. Recommended generation: icons authored as code (a small SVG subset) and dithered by a deterministic filter, about 70 agent-hours for the full set at $0. An AI-plate pilot of 30 or fewer images can follow later if the moment template looks too schematic.
9. Pipeline: a new `**Frame.**` line under each Picture names the template and its ids. Icons live in `media/visual/`, are built into `dist/visual/`, and `make check` fails when a Frame names an id without an icon. render.html gets one layout function per template.
10. Effort: about 18 agent-days in four phases. The first reviewable cut is episode 1 plus shorts 1, 4, 5 and 7, after phase 2 (about 6.5 days).

## 2. What the videos show now

Measured by running `scripts/video/timeline.py` over every episode and short (the film is assembled from these):

| On screen | Minutes | Share |
|---|---:|---:|
| Entity cards (game, mechanic, technique, bet) | 72.6 | 60.0% |
| Paper figures (`dist/paper/figures/*.svg`) | 26.7 | 22.0% |
| Title card or fallback slate | 17.2 | 14.2% |
| Catalog grid | 4.5 | 3.7% |

Problems the plan also fixes:

- **Cards come from loose name matching.** `entities.find` matches mechanic aliases case-insensitively, so broad aliases put wrong cards on screen. 35 matches come from five aliases ("research", "shares", "supply", "reports", "event log"), and at least 25 are wrong. Examples: "AI research has touched least" (short 7, first sentence) shows a Tech tree card; "shares a family with M.U.L.E." (03.7) shows Equity and buyouts; "demand above supply" shows Supply lines.
- **Labels break the Register contract.** `render.html` uses `text-transform: uppercase` with letter-spacing on the header, `.kind`, `.lab` and the slate subtitle. web/DESIGN.md rule 3 forbids uppercase anywhere.
- **Fonts come from the network at render time.** `render.html` loads IBM Plex from Google Fonts. If the fetch fails, Chromium falls back silently and the build still passes.
- **Picture lines that describe footage get a card or a slate.** 101 of 228 Picture lines name a game. Without footage, those scenes show the game's card, which states the same facts the narration does.

## 3. Templates

### 3.1 Counts

Every Picture line was read with the Voice line it sits over and given a primary template, plus secondary templates for its later beats (25 lines have more than one beat). The full table is `templates.csv`.

| Template | Shows | Picture lines (primary) | Lines (any beat) | Scenes (primary) | Scenes (any beat) |
|---|---|---:|---:|---:|---:|
| compare | 2 or 3 subjects side by side on the same axes: split screen, before and after, same move in two games | 37 | 41 | 26 | 30 |
| count | a quantity as a picture: unit grid with a lit subset, Venn of two sets and their overlap, ranked bars, piles, a counter | 32 | 33 | 32 | 32 |
| chain | cause and effect: linear chain with signed links, loop, fan-out, a data flow with a gate | 29 | 30 | 23 | 23 |
| data | the existing grid and paper figures, restyled | 26 | 27 | 23 | 24 |
| anatomy | a subject taken apart into labelled parts: game to mechanics, agent to needs, object to what it offers | 20 | 22 | 14 | 15 |
| record | a dataset artefact: entity record, run record, prediction card, file tree, terminal, PR | 17 | 17 | 17 | 17 |
| moment | a game moment as a 2 to 4 panel strip of generic icons with a caption per panel (cold opens) | 14 | 16 | 13 | 15 |
| slate | title card, text card, end card | 14 | 14 | 14 | 14 |
| timeline | things placed on dates: year axis, date tags, a calendar flip, a replay track | 13 | 16 | 13 | 15 |
| scale | a position on an ordinal scale: maturity ladder, the five ceilings, a 1 to 5 rubric, status | 9 | 10 | 8 | 9 |
| mockup | a labelled mock-up of a feature a game lacks (the bets) | 7 | 8 | 7 | 8 |
| formula | a rule as an equation of icons, terms building in order | 6 | 9 | 6 | 9 |
| toysim | the rule itself run by our code on a small grid (water, heat, Life, falling sand), dithered | 4 | 7 | 4 | 6 |
| no template | (section 3.3) | 0 | 3 | 0 | 3 |
| **Total** | | **228** | | 191 scenes, 179 with Picture lines | |

The 12 scenes without Picture lines are the shorts' end cards (slate). The film's 84 minutes reuse episode Picture lines, so templating the episodes covers the film too. Its own 8 lines are data (4), scale (2), timeline (1) and chain (1).

By source: episodes are led by compare 30, count 24, chain 23 and anatomy 16; shorts by count 8, compare 7, data 6 and chain 5.

### 3.2 Template definitions, with a scene from the scripts for each

- **anatomy.** The subject sits in the middle, or in a hero row, and its parts sit in a row above it on a bus line. Each part shows its icon, its name and "n of 177 games" with a bar. Core parts are drawn and supporting parts are counted. Variant *radial*: a hub with weighted spokes. Example: 01.3.0 "RimWorld's core mechanics peel off the screen as labelled cards" (proof frame 1); 05.3.0 and s005.2.0 smart objects (proof frame 3); 02.10.0 Stardew with date tags.
- **chain.** Nodes left to right. Links carry a verb and a sign (+ same direction, − opposite), and loops close below the row. Every node notes its update rule from the record, in mono. Example: 01.8.0 "pollution dragging down land value" (proof frame 2); 01.8.3 Factorio's two opposed loops; 07.3.0 the Infinite Craft cache, hit or miss; 10.10.0 the event log feeding replay, why and fork.
- **compare.** Two columns with the same rows, shared parts in the middle and the parts each game has alone on its side. Example: 03.3.0 Factorio and Anno 1800 share six mechanics; 03.6.0 Papers, Please and Princess Maker 2; 10.1.0 two monitors and two checksums.
- **count.** A unit grid of icons, one per item, lit or grey. Example: s007.2.0 "fourteen labelled tiles, all but two go grey". Venn: 08.6.0 "aging in 23 games, production chains in 38, none both". Ranked bars: 07.8.0. Piles: s008.1.0 (77 vs 17), drawn as uniform game tiles, never covers.
- **timeline.** A year axis with icons dropped on their first catalog year, or a calendar date with cards pinned to it. Example: 02.4.0 mechanic cards drop onto first-use years, plus a faded "outside the catalog" track; 11.1.0 "31 December 2027".
- **scale.** A ladder or ruler with labelled anchors and tokens placed on it. Example: 06.4.0 the technique maturity ladder; 05.3.3 the five ceilings; s004.4.0 legibility 2 of 5.
- **formula.** Icons as terms, building in narration order. Example: s004.2.0 raid points from wealth and colonists; 01.8 crime = 128 − land value + density − police; s002.4.0 250 points a heart, −2 a day.
- **record.** A record set as a mono key and value block, with the field being read in accent. Example: 09.4.0 the bottleneck explainer scrolls field by field; 11.3.0 criteria highlight clause by clause; 12.6.0 a run record.
- **mockup.** A generic game panel drawn from vocab icons inside a dashed frame that always carries the label "mock-up". The renderer refuses to draw this template without the label. Example: 09.5.0 the why button; 09.3.0 the bottleneck view.
- **moment.** 2 to 4 panels, each a small tableau of icons with a one-line mono caption: what happens, then what follows. Example: 01.1.0 raid, funeral, mood under the break line, the cook walks off; 08.1.0 one district, decades, a queue of hearses.
- **toysim.** A 64x36 or 36x64 dpx grid running the rule the narration states, seeded and deterministic, dithered by the same filter. Example: 04.1.0 water filling tile by tile with depth 1 to 7; 04.6.0 the R-pentomino past generation 1000; 01.8.5 heat traded between neighbouring tiles.
- **data.** The catalog grid and the paper figures, kept, with Register labels.
- **slate.** Title and end cards. The blurred figure behind the title becomes the same figure under a 25% Bayer veil.

### 3.3 Beats no template carries

- 06.10.0, second beat: clips from world-model demos ("a DOOM corridor generated frame by frame; a Genie 3 world where a character walks through a wall"). This is third-party footage, and the point is how it looks.
- s006.4.0: "a Project Genie world, with a graphic timer counting down from sixty seconds". The timer is a count; the world needs footage or a stand-in.
- 12.7.0, second beat: "a still of Utopia on the Intellivision". This is a game still.
- Two more need a redraw rather than the source image: 05.8.4 (figures from the Generative Agents paper, becomes a chain of word spreading across a network) and 06.12.0 (GDC survey charts and a Steam review graph, becomes a count from the cited numbers).

## 4. Vocabulary

### 4.1 Inventory

| Set | Images | Notes |
|---|---:|---|
| Mechanics | 199 | 76 are named in narration; 141 including every part of the 19 games taken apart in anatomy scenes; 189 including every part of the 93 games named anywhere |
| Families | 21 | all 21 `mechanic_family` terms are in use |
| Techniques | 25 | 17 category glyphs (`technique_category`) plus 8 techniques the scripts name: llm-game-master (15 scenes), genie-world-models (7), neural-rendering-shaders (4), monte-carlo-tree-search (3), deep-rl-npc-policies (2), on-device-language-models, diffusion-game-engines, wave-function-collapse. The other 37 use their category glyph and a maturity mark |
| Subgenres | 31 | a game is shown as its subgenre emblem plus its name in type (for example, colony sim: hut, person, crops) |
| Scene nouns | about 85 | 103 candidates counted with regexes over all 191 scenes; 80 appear in 5 or more scenes; about 18 merge into a mechanic icon (conveyor belt into conveyor-transport, power into power-grid) |
| Closed sets used on screen | about 45 | effects 7, technique maturity 4, determinism impact 3, horizon 4, status 4, five ceilings 5, six jobs 6, four admission tests 4, rubric scales 2, bet dials 3, builder types 3 |
| Bet plates | 8 | for the bets the scripts stage as mock-ups: bottleneck-explainer, causal-why-query, branch-preview-forecasts, salience-gated-llm-agents, language-modding, event-sourced-sim-runtime, symbolic-sim-neural-render, llm-society-terrarium. The other 35 bets are layouts of their `involves` mechanics plus a technique glyph |
| **Total** | **about 415** | built data has 43 opportunity records; the scripts say 42 bets |

No image is needed for the 177 games. A game is its subgenre emblem, its name, and its parts. This keeps every game-specific picture out of the set.

### 4.2 Order of work: scenes each concept appears in (of 191)

Counts come from regexes over Picture, Voice and On screen text (`work/vocab.py`), so they are approximate. Mechanic counts use the renderer's own matcher, minus the false matches in section 2.

Tier 1, 60 images (the proof made 17 of them):

| Concept | Scenes | Concept | Scenes | Concept | Scenes |
|---|---:|---|---:|---|---:|
| dataset record | 38 | death and grief | 16 | temperature | 13 |
| colonist (person) * | 30 | dice and chance | 16 | crops (crop-cultivation) | 13 |
| needs (needs-decay) * | 28 | hunger | 16 | ship | 13 |
| event (triggered-event-chains) | 26 | factory (industry) * | 16 | wall and turret (raid-defense) | 13 |
| crowd of agents | 25 | water and flood | 15 | calendar | 13 |
| why (question) | 22 | clock and timer | 14 | failed check | 13 |
| money (coins) | 22 | house (residential-zone) * | 14 | conveyor belt (conveyor-transport) | 12 |
| language model | 22 | map overlay | 14 | seed | 12 |
| production chain | 16 | chronicle and history | 14 | placing buildings (free-placement) | 11 |
| screen and monitor | 17 | rendered frame | 14 | mood bar (mood-breakdown) * | 11 |
| tile and cell | 17 | save file | 14 | power-grid | 11 |
| raid | 13 | weather and season | 13 | replay, event log, car | 11 each |

Also in tier 1: the other six RimWorld core parts, pollution-spread and land-value (done in the proof), the four household objects (done), pause (variable-speed, 9 scenes), tech tree (about 6 true scenes), and the emblems for colony sim, city builder, factory automation and life sim. (* = drawn in the proof.)

Tier 2, about 150 images: the remaining named mechanics, the 21 families, the 25 technique glyphs, about 45 more nouns (furnace, road, speech bubble, network, tooltip, thought bubble, aging, statue, diff, wolves and campfire, and so on), and the closed sets.

Tier 3, about 205 images: the 123 mechanics no script names, the 27 remaining subgenres, the 8 bet plates, and the rest of the closed sets. This tier exists for site reuse and for any game's anatomy; the videos need only about 141 mechanics.

### 4.3 Ids

- Mechanic, family, technique-category and subgenre icons use the dataset id (`storyteller-director`, `agents-behavior`, `llm-agents`, `colony-sim`). No dataset field changes.
- Scene nouns get ids in `media/visual/vocab.yaml`, not in `vocab/`, so the dataset's controlled vocabularies stay as they are (AGENTS.md section 7 needs an ADR for new vocab terms).

## 5. Visual language

### 5.1 Palette (Register tokens)

- Paper `#fafaf7`, ink `#171717`, ink-2 `#3d3d38`, muted `#696961`, faint `#97978e`, rules `#dcdcd4` and `#bdbdb4`.
- Accent `#0550ae` marks the element the current sentence is about, and only that element. When a sentence names two parts, both go accent, as in proof frame 1 (storyteller and threat scaling).
- State colours only with a glyph or word: stop `#9a2d25` (breaks reproducibility, a failed assertion, desync), ok `#18794e` (quote found, verified), open `#a96512` (prediction open).
- Series colours `--s1`–`--s4` stay in data figures only.
- Dark variant for text cards (10.9.0 "over a dark background"): paper `#2b2b28`, with the dither drawing paper-coloured dots. The palette is one parameter of the filter.

### 5.2 Dithering

- **Method: ordered, Bayer 8x8.** In `proof/dither-study.png`, a 1/255 brightness change flips 0.21% of pixels (Bayer 4x4), 0.39% (Bayer 8x8), 29.05% (Floyd-Steinberg) and 22.36% (Atkinson). Error diffusion re-flows the whole pattern on any change, which reads as shimmer at 30 fps. Atkinson also blows out highlights. Bayer 8x8 gives more tone steps than 4x4 at the same stability.
- **Five tones for icons**: paper, 25%, 50%, 75%, ink. This is a graphic rule, not a limit of the filter. The full 64 levels are reserved for tonal sources (toysim heat maps, any AI plate).
- **Resolution.** 16:9 uses 3 px per dither pixel (dpx), a 640x360 logical frame. 9:16 uses 4 px per dpx, 270x480. Icons are 48 dpx (144 px at 16:9, 192 px at 9:16); hero subjects are 96 dpx. Sprites go on an 8-dpx grid (24 px or 32 px) so the patterns of neighbouring sprites line up.
- **Compression check.** The 9:16 proof frame, encoded with the pipeline's own x264 settings (crf 20, veryfast, stillimage, 4:2:0), keeps the pattern: mean error 2.3/255 on the refrigerator crop. At crf 32 the 50% checker smears in blocks (3.4/255). Rules: no 50% fill larger than about a twentieth of the frame (use 25% or 75%), keep the accent as outlines and solids, not as sparse dots alone, and upload masters at a high bitrate.
- **Phone.** At 9:16 the 25% dots are 4 px every 8 px. On a 390-pt phone (about 1.08 device px per video px) they read as texture, and at 1x as grey (`proof/study/*-phone-1x.png`). Shapes carry the meaning through 2-dpx outlines (8 px), and tone is secondary.
- **Only pictures are dithered.** Text, arrows, bars, axes and numbers stay vector.

### 5.3 Icon grid and drawing rules (as built in `proof/src/icons.py`)

- 48x48 dpx, live area 4–44, baseline at y = 44 for standing things.
- Outline 2 dpx, interior detail 1 dpx, nothing thinner. Corners square, or radius 2 dpx for appliances.
- Light from the top left. The top and left faces of a volume are one tone lighter than the bottom and right.
- Views: people, objects and buildings in front elevation. Ground, parcels and abstract tokens (die, book) in one fixed 2:1 axonometric. Maps in plan.
- One person glyph: round head, box torso, separate arm and leg bars, no face, hair or clothing detail. Variants by pose and tone only. It must not resemble a game's character: no plumbob-like marker over the head, and no armless round-headed pawn.
- No text, logos or UI chrome inside icons. Labels are set in type next to them.
- One subject per icon. Games, bets and scenes are layouts of icons, never new composite drawings.
- Machine-checkable: coordinates on a 0.5-dpx grid inside the box, stroke widths 1 or 2, tones from the five-level set. This lint is what keeps 415 icons by many authors consistent.

### 5.4 Typography (Register)

- IBM Plex Sans 600 for on-screen statements (50–64 px), 500 for captions (40 px at 16:9, 44–46 px at 9:16), 500 for element labels (26–30 px at 16:9, 36 px at 9:16).
- IBM Plex Mono for labels, counts, ids and source lines, in lowercase: "3 of 177 games", "rimworld, in parts", "advertises Hunger". Names keep their case ("Storyteller director", "Hunger"), per Register rule 3.
- Size floor: 19 px at 16:9 and 21 px at 9:16 for source lines, 22 px and 27 px for anything the viewer must read.
- Every frame carries a source line naming its records and sources ("rules: simcity-1989 record, micropolis source (src-hopkins-2008-micropolis)"), per DESIGN.md's rule on numbers.
- Plex ships in the repo (OFL 1.1) and loads by `@font-face`. render.js asserts `document.fonts.check` before the first screenshot.

### 5.5 Motion

- **Build.** An element appears by Bayer dissolve: its pixels are revealed in matrix order over 8 frames (0.27 s at 30 fps), with no alpha blending, so no grey intermediate tones (`proof/motion-bayer-dissolve.png`). Removal runs the dissolve in reverse.
- **Arrows** draw from tail to head over 0.4 s (stroke-dashoffset), and their sign pops in at the end.
- **Counters** tick in integers to the token value in at most 1 s ("0 to 3 of 177 games"). The grid's year counter works the same way.
- **Current** swaps the sprite to its accent variant. The previous element returns to ink. No glow, scale or bounce.
- **Movement** is integer-dpx translation only (3 or 4 px steps), so patterns never resample. Size changes switch to a pre-rendered 1x or 2x sprite.
- **Timing.** Each element appears when the narration names it. Timeline.py already times each sentence; the match is restricted to the ids the Frame declares, so it cannot go wrong the way the card matcher does.

## 6. How to make the images

| | (a) Icons as code, deterministic dither | (c) Hybrid: (a) plus at most 30 AI plates | (b) AI model for everything, then dither |
|---|---|---|---|
| Rank | **1, recommended** | 2, bounded option after phase 2 | 3 |
| Consistency | Highest: shared primitives, a grid lint, five tones | Icons as (a); plates drift in perspective and detail density, which the dither hides only partly | Medium. Composition, perspective and line weight drift across 415 prompts even with a fixed style prompt; dither unifies tone, not drawing |
| Cost | $0 beyond agent time | (a) plus a few dollars | About 1,700 generations (4 per concept) at a few cents each, plus curation |
| Time for about 415 concepts | About 70 agent-hours (about 10 min per icon with primitives and review; the proof's 17 took about an hour with iteration) | (a) plus 1–2 days | About 20 h of prompting and picking, plus fixes for drift and lookalikes |
| Reproducibility | Byte-identical: the proof rebuilt its 61 PNGs to the same sha256. Fits `make determinism` | Plates are committed PNG sources with provenance; dither is deterministic downstream | Same as (c) for all 415 images: about 20–40 MB of binary sources in git; regenerating later gives different images |
| Rights | Clean: all original drawing of generic subjects | Plates need lookalike review; prompts must never name a game, studio or character | As (c) for every image. Purely AI-generated images may not be copyrightable, so the CC BY grant over them is uncertain |
| Weak point | Pictogram ceiling: a harvester, a docking station or a night street looks schematic | Two drawing systems on screen | Uniformity is the whole brief, and it is the thing this method is worst at |

**What (b) or (c) would need.** This session has no image-generation tool. The restricted ElevenLabs connector here refuses image nodes; its server notes say image generation is in the full ElevenLabs connector, added as a custom connector at https://api.elevenlabs.io/v1/mcp. The alternatives are an API key for a hosted image model, passed to a script by environment variable, or a GPU machine for an open-weights model (this 2-CPU box cannot run one). Either way, DESIGN.md already sets the rules: a `prompts/` template with the skin's image brief, no text in images, and a provenance line per image (generated · prompt id · model · date · seed · treatment). The repo has no `web/prompts/` or `web/skins/` yet, so those would be added first.

## 7. Pipeline

### 7.1 Repo layout

```
media/visual/
  vocab.yaml            one entry per image: id, kind (mechanic|family|technique|technique-category|subgenre|noun|term|plate),
                        ref (dataset id or null), label, aliases (for reveal timing), view (elevation|axonometric|plan),
                        status (draft|approved), run (run id), provenance (drawn | generated: prompt id, model, date, seed)
  icons/<id>.svg        SVG subset only: rect, circle, ellipse, line, polyline, polygon; data-tone="1..4|k"; viewBox 0 0 48 48
  plates/<id>.png       (only if (c) is chosen) committed sources plus <id>.yaml provenance
  fonts/                IBM Plex Sans and Mono, OFL 1.1
scripts/visual/
  raster.py             SVG subset -> tone map (Pillow, 4x supersampling, no antialiasing), as proof/src/dither.py
  dither.py             tone map -> RGBA, Bayer 8x8, palettes (paper, dark)
  build.py              writes dist/visual/icons/<id>@3x.png, @4x.png, .accent, 8-step dissolve sheets, contact sheet
  check.py              coverage, references, grid lint, rights lint (7.3)
```

- `make build` calls `scripts/visual/build.py`, which takes under 10 s for 415 icons. Output stays in gitignored `dist/` and comes under `make determinism`.
- The full set is about 6 MB of PNGs (the proof's 17 icons, in both scales with accent variants, are 252 KB).
- SVG over Python drawing code: diffable, viewable in a browser, reusable on the website, and agents write it well. The rasterizer is ours, so Chromium versions cannot change pixels.
- Licence: `LICENSE` names no path under `media/` except `*.md`. Add `media/visual/` explicitly (decision 5).

### 7.2 How a scene picks its template: ranked

1. **An explicit `**Frame.**` line under each Picture (recommended).** It is machine-readable, reviewed like prose, and can carry `{{derived:}}` tokens and `{{assert:}}` checks, so a frame fails the build when its numbers move. parse.py ignores unknown line kinds, so the current renderer keeps working while Frame lines are added. `templates.csv` is the first draft for all 228.
2. **A side file keyed by picture id**, as `figmap.py` does now. No script edits, but ids are positional (scene.block index) and drift when a scene gains a block.
3. **Inference from Picture text or entity mentions.** This rebuilds the card matcher's false matches, or needs a model at build time, which breaks determinism.

Frame lines for the proof scenes:

```
**Frame.** anatomy game=rimworld parts=core current=storyteller-director,adaptive-threat-scaling
**Frame.** chain label=coupling source=simcity-1989 nodes=industry,pollution-spread,land-value,residential-zone signs=+,-,+ current=land-value
**Frame.** anatomy hub=person spokes=refrigerator:Hunger,bed:Energy,toilet:Bladder,television:Fun weights=illustrative current=refrigerator
```

Others:

```
**Frame.** count venn a=aging-population b=production-chain overlap={{cooccur:...}}      (08.6.0)
**Frame.** mockup bet=causal-why-query subject=colony-sim                                 (09.5.0; label "mock-up" is automatic)
**Frame.** timeline date=2027-12-31 cards=predictions:due                                 (11.1.0)
**Frame.** toysim rule=fluid-flow seed=4 steps=240 show=depth                             (04.1.0)
```

### 7.3 Checks (`make check`)

- Every id in a Frame line exists in `media/visual/vocab.yaml` and has a source file (error). Every `ref` exists in the dataset (error). No orphan icons (error).
- Coverage of mechanics, families, technique categories and subgenres is reported as a warning count until its phase closes, then becomes an error.
- Grid lint on every SVG: coordinates on the 0.5-dpx grid inside 0–48, stroke widths 1 or 2, `data-tone` from the set, only allowed elements (error).
- Rights lint (error):
  - no vocab id or label equals a game id, game name or alias;
  - every icon entry declares `subject: generic`;
  - every `mockup` frame, and every `moment` or `record` frame that draws game UI, renders the label "mock-up". The renderer refuses otherwise, and a check over states.json confirms it.
- New error and warning codes, and the new Frame line kind, go in an ADR (ADR-0006), since CONTRACT.md is the law the validator enforces.

### 7.4 Renderer changes

- **parse.py**: read `**Frame.**` into the preceding picture block.
- **timeline.py**:
  - a picture with a frame emits a `frame` event with the spec resolved against `dist/entities` and `media/visual/vocab.yaml`;
  - element reveal events go at the times the narration names each declared element;
  - voice-matched cards stop while a frame is up (today they stop only while a figure is up), and the main entity moves to a one-line mono chip;
  - add a stoplist for broad aliases ("research", "shares", "supply", "reports", "letters", "graphs", "logistics") in the video matcher only.
- **render.html**:
  - remove uppercase;
  - vendored fonts;
  - a `#frame` stage and `templates.js` with one layout function per template, each with its own 9:16 layout instead of CSS stacking;
  - sprites as `<img>` with `image-rendering: pixelated`, snapped to the 8-dpx grid;
  - arrows in inline SVG;
  - title-card blur becomes a 25% Bayer veil;
  - cards become chips.
- **render.js**: when a state changes `build` or `current`, take the transition stills (8 dissolve steps, 12 arrow steps, counter steps) out of that state's duration, then hold. This adds about 2–3x the screenshots: roughly 1–2 extra minutes per episode, and roughly 20 minutes for the film on this 2-CPU machine.
- **figmap.py**: `FIG` stays for the data template. `CARDS` is retired as Frame lines land.

### 7.5 Phases

| Phase | Work | Agent-days | Reviewable output |
|---|---|---:|---|
| 0 | Decisions below, ADR-0006 (Frame line, `media/visual`, icon licence, check codes) | 0.5 | ADR |
| 1 | `scripts/visual` (raster, dither, build, check), fonts vendored, Register fixes in render.html, Frame parsing, anatomy, chain, compare and count templates, static | 3 | ep1 scenes 3 and 8 re-rendered |
| 2 | Tier 1 (60 images, 17 done), Frame lines for episode 1 and shorts 1, 4, 5, 7 | 3 | 1 episode, 4 shorts |
| 3 | Motion (dissolve, arrows, counters); timeline, scale, formula, record, mockup, moment and toysim templates; tier 2 (about 150 images); Frame lines for all 228 Picture lines | 7 | all 25 videos re-rendered |
| 4 | Tier 3 (about 205 images); site reuse on mechanic, game and bet pages (a DESIGN.md image rule for "drawn" provenance) | 4 | full coverage check turns into an error |
| 5 (optional) | AI-plate pilot: at most 30 moment backdrops through the same filter, kept only if they pass the consistency and lookalike review | 1–2 | pilot sheet |

## 8. Proof (in `proof/`)

| File | Shows |
|---|---|
| `frame-01-anatomy-rimworld-16x9.png` | Episode 1, scene 3. RimWorld's 7 core parts with counts from `dist/entities` (storyteller in 3 of 177 games, needs decay in 30), the storyteller and threat scaling in accent for the caption "The storyteller picks the raid, and spends a threat budget that grows with your wealth.", and a generic colony as the subject |
| `frame-02-chain-pollution-land-value-16x9.png` | Episode 1, scene 8. Industrial zones (+ writes), pollution map (− lowers), land value (+ raises), zone growth. Rule text from the simcity-1989 record and Micropolis notes, the six jobs with "coupling" current, a source line |
| `frame-03-short05-smart-objects-9x16.png` | Short 5, scene 2. A generic person at the hub, refrigerator (Hunger, accent), bed (Energy), toilet (Bladder), television (Fun), with line weight marked illustrative. The finding stays pinned at the top; "smart objects · in 4 of 177 games · first 2000, The Sims" |
| `icons-sheet.png`, `icons/` | 17 icons at 3x and 4x with accent variants; `icons/_preview.png` at 1 dpx |
| `dither-study.png`, `study/` | The four methods, flip rates, and phone previews |
| `motion-bayer-dissolve.png` | Five steps of the build dissolve for three icons |
| `src/` | `dither.py`, `icons.py`, `build_icons.py`, `frames.py` (Playwright), `dither_study.py`, `motion_strip.py`. Every number on the frames is read from `dist/entities` at render time, and the short asserts authoring cost 4 as the script does |

## 9. Risks

- **The pictogram ceiling.** Code-drawn scenes can still read as diagrams. The moment strips and toysim plates are the answer, and the phase-2 review of episode 1's cold open is where to judge it.
- **Script churn.** Frame lines must change when scenes change. Tokens and assertions in Frame lines make stale numbers fail the build. Stale layouts are caught only by review.
- **Lookalikes.** A generic drawing can still evoke a game, such as a green diamond over a head, CP437 smiley dwarves, an RCI bar in green, blue and yellow, or Infinite Craft's emoji tiles. The rights lint covers names, not shapes, so each icon's approval in vocab.yaml (`status: approved`) is a human check.
- **Re-render cost.** About 25 videos on a 2-CPU machine, with a film encode already taking most of it.

## 10. Decisions for Yohei

1. **Generation:** code-first icons (recommended), the hybrid with at most 30 AI plates, or AI for everything? If AI: which provider (needs the full ElevenLabs connector or an image API key) and what budget.
2. **The look:** ink and one accent on Register paper, as proofed, or a duotone, or dark paper for shorts? Dither pixel at 3 px for 16:9 and 4 px for 9:16, or chunkier (4 and 6) for more retro and more compression headroom.
3. **Cold opens:** accept moment strips and toysim plates in place of footage for the 14 cold-open-style lines, or hold those scenes for footage later.
4. **Template selection:** inline `**Frame.**` lines in the scripts (recommended, 228 edits drafted from `templates.csv`), or a side file keyed by picture id.
5. **Icon licence:** CC BY 4.0 like the data (recommended, since icons are artwork), or Apache-2.0 like the code that draws them.
6. **Coverage:** all 199 mechanics (needed for site reuse), or the 141 the videos use.
7. **Entity cards:** drop them for one-line chips under frames, or keep full cards for scenes with no Frame.
8. **The 3 beats with no template** (world-model demo clips, the Project Genie world, the Utopia still): generic labelled stand-ins, ask the rights holders, or cut the beats.
9. **Ship the alias stoplist now**, independent of the rest, so short 7 stops opening on a Tech tree card.
