# Brief: add verbatim quotes to claims

**Run kind:** `verification` (or `catalog` when you are adding the claim). **Limit:** 10 records per PR.

A claim's `quote` is the shortest verbatim passage (10 to 400 characters) from its first listed source that supports the claim; `locator` says where it is (page, section heading, timestamp). The `sources` workflow fetches the source (its `archived` snapshot first) and fails the PR if the quote is not there, so copy, do not paraphrase.

1. Pick records whose claims have no `quote` (issue lists them).
2. Open the first source of each claim. If it no longer supports the claim, do not quote it: either cite a source that does, or set the record to `contested` with a `disputes` note (I13).
3. Paste the passage as `quote`. Typography (curly quotes, dashes, spacing) is normalized by the checker; words are not.
4. If the source has no `archived` snapshot, add one (see `archive-sources.md`) so the quote stays checkable after the page changes.
5. Append your run to each record's `provenance.reviewed`.

Paywalled or PDF sources cannot be fetched by CI; the checker warns and a reviewer checks by hand. Say so in the PR.
