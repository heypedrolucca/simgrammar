# Brief: add Wayback snapshots to sources

**Run kind:** `maintenance`. **Limit:** 30 sources per PR.

`W105` counts sources with a `url` and no `archived` snapshot. A snapshot keeps quotes checkable after a page moves or changes.

1. List candidates: `python scripts/check_sources.py --all --suggest-archive` prints the closest existing snapshot for each source, or a save link.
2. For each source, open the snapshot and confirm it shows the content the source was cited for (the snapshot date should be close to `accessed`). If none exists, save the page at `https://web.archive.org/save/<url>` and use the resulting snapshot URL.
3. Set `archived: https://web.archive.org/web/<timestamp>/<url>` (the schema accepts only this form).
4. Append your run to the source's `provenance.reviewed`.

Never change `url` or `accessed` in this task; if the live page no longer supports the citing claims, open a **Dispute** issue instead.
