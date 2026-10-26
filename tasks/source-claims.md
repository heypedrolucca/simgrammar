# Brief: add verbatim quotes to claims

**Run kind:** `maintenance` (or `catalog` when you are adding the claim). **Limit:** 10 records per PR.

A claim's `quote` is the shortest verbatim passage (10 to 400 characters) from its first listed source that supports the claim. `locator` says where the passage is. The `sources` workflow fetches the source (its `archived` snapshot first) and fails the PR if the quote is not there, so copy the text; never paraphrase.

Adding quotes is not verification. It needs no independence (E035), so any operator may quote any record. It never changes `status`. Verifying a record is `verify-record.md`.

1. Take the records the issue lists and find their claims with no `quote`: `claims` on games, mechanics and opportunities, and `key_results` on techniques.
2. Open the first source of each claim. The source that counts is the one the record cites, at the url, DOI or arXiv id in its source file.
   - **A DOI-only paper** you can read only as a copy (an author's PDF, a university repository): quote from the copy only if it is the same version. Name the copy's url in your run's `method`. CI reaches only the DOI landing page and will warn, so say so in the PR.
   - **A regional or mirror page** (a `/gb/` copy of a `/us/` article): do not quote it unless it is the url the source cites.
3. Decide what the quote must support.
   - **The claim goes further than its source:** do not quote. Leave it and propose a rewording in your run's `proposals`, with the quote that would support the reworded claim.
   - **The claim bundles several facts:** quote the passage that supports its most specific checkable part (a number, a name, a result). Propose splitting the claim if another part has no support.
   - **The claim states an absence** ("no source found", "not documented"): no quote can support it. Propose moving it to `limitations` or `notes`.
   - **The evidence is in a code file**, and the source is the repository root: CI fetches only the root page. Propose a file-level source rather than quoting.
4. Paste the passage as `quote`. The checker normalizes typography (curly quotes, dashes, spacing) but not words. Avoid passages with LaTeX, footnote markers, or inline citations, which differ between a page's HTML and its PDF, and leave off a trailing period.
5. Set `locator` in one of these forms:
   - `Abstract`
   - `Section 3, Method`
   - `p. 12`
   - `README, Installation`
   - `Article body`
   - `00:14:32` (a timestamp in a video)
6. Append your run to `provenance.reviewed` on each record you quoted or re-checked. Name every claim you left unquoted, and why, in your run's `method`.

**If your web tool summarizes pages**, as many agent fetch tools do, it may return only short verbatim fragments. Ask it whether your exact passage appears on the page before you use the passage. A quote stitched from fragments is a guess until CI finds it.

Archiving sources is a separate task (`archive-sources.md`); do not archive here. Paywalled or PDF-only sources cannot be fetched by CI, so the checker warns and a reviewer checks by hand. Say so in the PR.

**Done when:** every claim on the listed records has a quote, or is named in your run's `method` with the reason and, where useful, a proposal. `make check` and `make pr-check` are green. The `sources` workflow either finds each quote or flags it for review.
