# Brief: add store ids to games

**Run kind:** `catalog`. **Limit:** 10 games per PR.

`store_ids` lets other datasets (platforms, themes, sales, reviews) join on SimGrammar's games without copying them. Fields:
- `steam`: integer app id from `store.steampowered.com/app/<id>`.
- `igdb`: slug from `igdb.com/games/<slug>`.
- `wikidata`: item id such as `Q12345`.

Each id points at the game the record describes. Use these rules to decide whether a store entry is that game:

- **Same game, later edition: use it.** Covers a paid Steam release of a game first released free, or a 1.0 release after early access. Examples: Dwarf Fortress (free 2006 build, Steam 2022), Garry's Mod (2004 mod, Steam 2006), Factorio (2013 alpha, Steam 2020). Use it when the record's `design_notes` describe that edition.
- **Remaster, sequel, bundle, or expansion: a different game.** Leave the field out.
- **Series records** (the record covers yearly editions, like `football-manager`): no store id; one id would name one edition.
- **Not on the store** (Minecraft is not sold on Steam): leave the field out.
- **Developer renamed or acquired** (the store shows a new studio name): keep the id if the game is the same. Note the rename in your run's `method`; do not edit the record's developer in this task.

1. Open each store page or item and confirm it is the record's game by the rules above. Add only ids you opened yourself; an id seen only in a search listing is not confirmed.
2. Wikidata and IGDB often cannot be opened by agent web tools. If yours cannot, add the Steam id only and list the game in `method` as "Wikidata/IGDB not checked"; a human with a browser picks it up. On IGDB, a `--1`-style suffix marks a second game with the same name (often a remake), so check the release year on the page. CI checks IGDB slugs for format only, so the reviewer opens each one.
3. Do not add the store page as a source: store ids carry no evidence field. Your run's `method` names each page you opened and what it showed (title, developer, release date).
4. The `sources` workflow resolves Steam and Wikidata ids and fails when the store's name does not match the game's `name` or an alias (sequels are treated as mismatches). If the store uses another name for the same game, add it to `aliases`.
5. Put `store_ids` where the schema lists it (before `claims` and `sources`). Append your run to `provenance.reviewed` on each game you changed, and only those. A game you checked and left without an id goes in `method`, not in `reviewed`.

**Done when:** each listed game has every store id you could confirm; games you could not confirm are named in `method` with the reason; `make check` and `make pr-check` are green; the `sources` workflow resolves every id to the right game.
