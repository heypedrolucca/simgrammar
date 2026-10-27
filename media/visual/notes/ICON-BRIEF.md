# Icon brief: SimGrammar visual vocabulary, phase 3

You are drawing one batch of icons for the SimGrammar video series. Each icon is a small SVG file in a strict subset. The build turns it into a dithered two-colour picture: ink on warm paper, or the same drawing in blue when it is the thing the narration is about. This brief has everything you need to work on your own.

## What you own and what you must not touch

- Your batch number N is in your assignment. Your ids are the entries in `icon-worklist.json` with `"batch": N`. The list is also in `batches["N"]` in the same file.
- Write only inside `icons-batch-N/` next to this file:
  - `icons-batch-N/icons/<id>.svg`, one per id;
  - `icons-batch-N/vocab.yaml`, one entry per id (format below);
  - `icons-batch-N/preview/`, which the tool writes;
  - optionally `icons-batch-N/notes.txt`, for anything the coordinator should know about an icon.
- Do not edit, create or delete anything in `/home/claude/simgrammar-visual` or `/home/claude/simgrammar`.
  - No git commands.
  - No `make`.
  - You may read those folders. `media/visual/icons/*.svg` in the worktree holds the 79 existing icons; match their style.
- Do not add ids that are not on your list, and do not draw another batch's ids. If an id cannot be drawn as a generic subject, say so in `notes.txt` and in your hand-back. Do not invent a replacement.

Paths, all under `/tmp/claude-0/-home-claude/a3926534-57b7-5f92-ac72-e47553ebe38a/scratchpad/visual-build/`:

- `ICON-BRIEF.md` (this file)
- `icon-worklist.json`
- `icontool.py`
- `icons-batch-1/`, `icons-batch-2/`, `icons-batch-3/`

## The worklist entry

```json
{"id": "elections", "kind": "mechanic", "ref": "elections", "label": "Elections", "view": "elevation",
 "note": "a ballot box with a folded paper going into the slot. Avoid: any game's art, logo, cover, character, or UI.",
 "batch": 1, "frames_use_it": true}
```

- `kind` is one of mechanic, family, subgenre, technique-category, technique, noun or term.
- `ref` is the dataset id when there is one. For a mechanic, `ref` is the same as `id`.
- `label` is the wording shown beside the icon. You don't draw it.
- `view` is elevation, plan or axonometric (see Views).
- `note` is the subject to draw and what it must not resemble. You can change details, but keep the subject. If you change the subject, record it in `notes.txt`.
- `frames_use_it: true` means a frame in the videos already uses the icon. Draw those first.

To read a definition, look up the id in `/home/claude/simgrammar-visual/dist/entities/mechanics.json` (field `definition`), `techniques.json`, or `/home/claude/simgrammar-visual/vocab/*.yaml`. It helps you pick a picture that says what the thing does.

## The grid

- `viewBox="0 0 48 48"`. One unit is one dither pixel (dpx).
  - Videos draw a dpx at 3 screen px in 16:9 and 4 px in 9:16.
  - Large frames also draw a 48 icon at 72 or 96 dpx. The vector is redrawn at that size, so lines get proportionally thicker and the dither grain stays 1 dpx.
  - Draw for 48. Check the 96 render in the sheet: it must not look crude or empty.
- Coordinates are multiples of 0.5, between 0 and 48.
- Live area is 4 to 44. Standing things sit on a baseline at y = 44, as in `house.svg`, which draws a 1-dpx ground line at y = 44.
- The subject fills the live area: about 36 to 40 dpx in its longer dimension. Frames are getting bigger and fuller, so a small, centred drawing with lots of air reads as weak.

## Tones

Fill and stroke colours name tones. In a browser they preview as flat greys; the build dithers them.

| Hex | Tone | Use |
|---|---|---|
| `#c8c8c2` | 25 % ink | lit faces, light fills |
| `#8c8c86` | 50 % ink | mid faces, secondary parts |
| `#55554f` | 75 % ink | shadow faces, dark parts |
| `#171717` | ink | outlines, small solid parts, doors, windows' dark panes |
| `#fafaf7` | paper (knockout) | an opaque paper fill that covers whatever is under it: windows, a page, the inside of a speech bubble |
| `#a9c2e6` `#6f93cf` `#3a6ab8` `#0550ae` | 25, 50, 75, 100 % accent | only for a part that is always blue, such as a broken link or an injury. Almost no icon needs these. The renderer turns the whole icon blue when it is current. |

- Light comes from the top left: top and left faces are one tone lighter than bottom and right faces.
- Use at least two tones besides the ink outline. A drawing in ink alone reads as a stencil; one that is mostly 75 to 100 % reads as a blot.

## Primitives (the subset)

- The file is a flat list. No `<g>`, `transform`, `<path>`, `<text>`, `style`, `class` or `id` attributes, and no children. An optional `<title>` is ignored.
- Root element: `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48">`. Only xmlns, viewBox, width and height are allowed on it.
- Elements and their allowed attributes:
  - `rect` x y width height [rx]
  - `circle` cx cy r
  - `ellipse` cx cy rx ry
  - `line` x1 y1 x2 y2
  - `polyline` points
  - `polygon` points
  - Any element may also take `fill`, `stroke` and `stroke-width`.
- `rect`, `circle`, `ellipse` and `polygon` must state `fill`, a tone or `none`. `line` and `polyline` cannot be filled.
- Strokes:
  - `stroke-width` is 1, 2 or 3, centred on the geometry as in SVG.
  - A stroke needs a width, and a width needs a stroke.
  - An element must draw something.
- Shapes are drawn in file order, so later shapes cover earlier ones. Draw back to front.

## Drawing rules

- Outlines are 2-dpx ink. Interior detail is 1 dpx in ink or 75 %. A 3-dpx stroke is for one bold mark, such as the question mark in `question.svg` or a magnifier handle.
- Never put text in an icon: no letters, digits, currency signs or arrows made of characters. Labels are set in type beside the icon.
- **Views:**
  - Elevation (front view) is for people, objects, buildings and machines.
  - Plan (top view) is for maps, roads, routes and pitches.
  - Axonometric 2:1 (2 across for every 1 up) is for ground, parcels and tokens such as a die or a book lying flat.
- **The person glyph** is shared across all batches. Copy the coordinates from `media/visual/icons/person.svg` and scale or move them.
  - It has a round head, a box torso, and separate arm and leg bars.
  - It has no face, hair or clothing detail.
  - For a small figure in a group, scale the whole glyph and keep its proportions. A 16-dpx-tall figure is the smallest that reads.
- **Shared motifs.** Reuse these exactly so the set reads as one family:
  - The speech bubble is a rounded rect (rx 3) with a paper fill (`#fafaf7`), a 2-dpx ink outline, and a small triangular tail at the bottom left. Text inside is 1-dpx lines in 50 %.
  - The magnifier is a circle with a 2-dpx ink outline, a 25 % or paper fill, and a 3-dpx ink handle at 45° toward the bottom right.
  - Coins, gears, a house, a factory, a clock, a person, a document or record, and a rendered frame already exist. They are `coins.svg`, `gear.svg`, `house.svg`, `factory.svg`, `clock.svg`, `person.svg`, `dataset-record.svg` and `rendered-frame.svg` in `media/visual/icons/`. When your subject includes one of them, redraw it the same way at your scale.
  - The "learned model" motif is `language-model.svg`: a box with a small layered network. Batch 3 uses it for AI technique categories and techniques. A "chip outline" is a square with a 2-dpx outline and three 1-dpx pins on each side.
- **Distinct silhouettes.** Two icons in the same frame must be told apart at a glance at phone size.
  - The lint warns when a silhouette overlaps an existing icon by more than 75 %.
  - Family emblems and subgenre emblems are shown beside mechanic icons, so they must not look like a mechanic icon of the same subject.
- **Rights.** Draw generic subjects only. Nothing may copy or evoke a specific game's art, logo, cover, characters, mascot, tileset or UI. For example:
  - no diamond marker over a head;
  - no armless round-headed pawn;
  - no pixel-perfect creeper-like face;
  - no well-known game's robot, logo shape or HUD.
  - No real-world brand, flag, religious symbol, or AI lab or product logo either. A technique is drawn by what it does, not by who makes it.

## The vocab fragment

`icons-batch-N/vocab.yaml`:

```yaml
icons:
  - {id: elections, kind: mechanic}
  - {id: microphone, kind: noun, label: Microphone, aliases: [mic]}
  - {id: status-verified, kind: term, label: Verified}
```

- One entry per SVG, with the keys `id`, `kind`, and for a noun or term `label`, plus optional `aliases`.
  - `kind` and `label` come from the worklist entry.
  - Mechanics, families, subgenres, technique categories and techniques take no label; the dataset supplies it.
- `aliases` are optional, lower-case, everyday words for the subject, which the renderer matches in the narration to move the highlight.
  - Leave them out unless the subject has an obvious short name; the coordinator adds narration aliases when merging.
  - An alias must never be a game's name and must not repeat an existing icon's id, label or alias. The lint checks both.
- No other keys. Don't add `run`; the coordinator records the run when merging.

## Tools

Run from any directory with `python3`. PIL, numpy and PyYAML are installed. The tool reads the worktree and never writes to it.

```sh
T=/tmp/claude-0/-home-claude/a3926534-57b7-5f92-ac72-e47553ebe38a/scratchpad/visual-build/icontool.py
python3 $T lint  --batch N              # subset errors, ownership, vocab entries, game names, aliases; style warnings
python3 $T check --batch N              # the repository's own E041 check (scripts/visual/check.py) with your batch merged in
python3 $T sheet --batch N              # icons-batch-N/preview/sheet-N.png
python3 $T sheet --batch N --only a,b   # a sheet of just those ids
python3 $T show  icons-batch-N/icons/<id>.svg   # one icon at 8x with a tone count, to icons-batch-N/preview/<id>.png
```

- **The sheet.** Each row of `sheet-N.png` shows the icon in ink at 3x, in accent at 3x, drawn at 96 dpx, and at phone size, which is how it reads on a phone held at arm's length. The top row shows eight existing icons for comparison.
- **Look at the sheet.** Open the PNG with your image-reading tool after every few icons. Judge three things:
  - Does the subject read at phone size?
  - Is it distinct from its neighbours?
  - Does its weight match the reference row?
- **What the commands check:**
  - `lint` covers everything E041 checks, plus things E041 cannot know: whether the id is yours, missing files, and style warnings (small subject, weak outline, one tone, blot, too many shapes, near-duplicate drawings, accent tones). The near-duplicate test compares full-ink pixels only, so box-shaped subjects with different contents do not match.
  - `check` runs the real repository check on a scratch copy, so a clean `check` means the merge will pass E041.

## Done means

1. Every id in your batch has an SVG and a vocab entry.
2. `lint` reports 0 errors, and `check` reports 0 E041 errors.
3. Every lint warning is fixed or explained in `notes.txt`, one line per id.
4. You have looked at the full `sheet-N.png`.

Draw the `frames_use_it: true` ids first. If you run out of time, hand back what is drawn and list the rest.

## Hand-back

Report to your caller:

- the count drawn out of the count assigned;
- the final `lint` and `check` summary lines;
- the path to `sheet-N.png`;
- any id whose subject you changed or could not draw generically, and why.

Don't paste the SVGs; the coordinator reads the folder.
