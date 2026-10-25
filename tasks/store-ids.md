# Brief: add store ids to games

**Run kind:** `catalog`. **Limit:** 10 games per PR.

`store_ids` lets other datasets (platforms, themes, sales, reviews) join on SimGrammar's games without copying them. Fields: `steam` (integer app id from `store.steampowered.com/app/<id>`), `igdb` (slug from `igdb.com/games/<slug>`), `wikidata` (item id such as `Q12345`).

1. Find the exact edition the record describes (first release year, developer). A remaster, sequel, or bundle is a different id; leave the field out rather than guess.
2. Add only ids you opened and confirmed. The `sources` workflow resolves Steam and Wikidata ids and fails when the store's name does not match the game's `name` or an alias (sequels are treated as mismatches). If the store uses another name, add it to `aliases`.
3. Append your run to each game's `provenance.reviewed`.
