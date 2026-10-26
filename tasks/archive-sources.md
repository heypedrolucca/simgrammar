# Brief: add Wayback snapshots to sources

**Run kind:** `maintenance`. **Limit:** 30 sources per PR (sources count separately from the 10-record limit).

`W105` counts sources with a `url` and no `archived` snapshot (`python scripts/validate.py --warnings` prints it; `python scripts/make_tasks.py --brief archive-sources` lists them in batches). A snapshot keeps quotes checkable after a page moves or changes.

**You need network access to archive.org.** Some cloud agent sandboxes block it or gate it behind a permission prompt. If your agent cannot reach `https://archive.org/wayback/available`, stop, comment on the issue, and do not open a PR.

1. Look up the issue's sources: `python scripts/check_sources.py --ids <id>,<id>,... --suggest-archive`. For each one it prints the closest existing snapshot with its date next to the source's `accessed` date, or a save link. (The API returns `http://` snapshot urls; the script rewrites them to `https://`, which the schema requires.)
2. Open each snapshot and confirm it shows the content the source was cited for: the passage a claim quotes, or the facts the citing records state. Which snapshot to use:
   - **Taken on or after `accessed`:** use it.
   - **Older than `accessed`:** use it only if it shows the cited content. Otherwise save a fresh one.
   - **None, or none shows the content:** save the page at `https://web.archive.org/save/<url>` and use the snapshot it creates.
   - **Raw files and PDFs** (`raw.githubusercontent.com`, a direct `.pdf`): use the `id_` form, `https://web.archive.org/web/<timestamp>id_/<url>`, which serves the original bytes.
   - **Paywalled or login-only pages** (a publisher chapter, say): the snapshot will show the same wall. Archive it anyway if it captures the landing page with the citation details. Note in `method` that the full text is not in the snapshot.
3. Set `archived:` to the snapshot url. The schema accepts `https://web.archive.org/web/<timestamp>/<url>` and the `id_` form, and E034 rejects a snapshot of a different url.
4. Append your run to `provenance.reviewed` on each source you archived, and only on those. A source you looked up but could not archive stays untouched; name it, and why, in your run's `method`.

Never change `url` or `accessed` in this task. If the live page no longer supports the citing claims, open a **Dispute** issue instead.

**Done when:** every listed source you could archive has an `archived` snapshot of its own url and names your run in `provenance.reviewed`; the rest are listed in your run's `method`; `make check` and `make pr-check` are green. If you archived none, see the AGENTS.md rule on runs that change nothing.
