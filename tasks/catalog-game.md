# Brief: add or complete games

**Run kind:** `catalog`. **Limit:** 10 games per PR, plus their sources.

Read first: `AGENTS.md` §3 (game inclusion test) and §4, `schema/game.schema.json`, and `data/games/rimworld.yaml` as the depth to match.

1. Search before you add: `python scripts/find.py "<title>" --type game`. If it exists, improve it instead.
2. Scaffold: `python scripts/new.py game <id> --run <run-id>`. Fill every field from the vocabularies; quote numeric-looking terms (`agent_count_order: "10"`).
3. Verify `year` (first public release, early access included), `year_full_release`, `developer`, and `platforms` against a primary source (store page, official site) and cite it. Wikipedia alone keeps the game at `sourced`, never `verified` (E034).
4. Decompose the game into existing mechanics only (`python scripts/find.py --list mechanic`), typically 6 to 14. Mark `core` only for identity-defining mechanics and give each core entry a `note` naming how this game implements it. A missing rule-system becomes a `new-mechanic` proposal in your run, never a forced fit.
5. Two mechanics follow fields exactly (E033): a `real-time-pausable` game tags `variable-speed`; a `scripting` or `total-conversion` game tags `modding-api`. Choose the field term that is true, then tag accordingly.
6. Add `store_ids` when you can confirm them (see `store-ids.md`), and a `quote` on each claim (see `source-claims.md`).
7. Score `emergence` and `influence` by anchor text; between two anchors take the lower.

Done when `make check` is green and every game names your run in `provenance.created`.
