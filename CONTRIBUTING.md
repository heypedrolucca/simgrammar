# Contributing to SimGrammar

SimGrammar is a research dataset that people and AI agents extend together. The rules that keep it from drifting are in [`CONTRACT.md`](CONTRACT.md); the step-by-step procedure is in [`AGENTS.md`](AGENTS.md). This page covers how to get work, what review to expect, and the terms of contributing.

Invited to contribute with your own agent? Read [`tasks/humans-with-agents.md`](tasks/humans-with-agents.md) first.

## Find something to do

- **Tasks.** [`tasks/`](tasks/) holds briefs for bounded jobs: cataloguing games, adding verbatim quotes to claims, archiving sources, adding store ids, verifying records, rating scores, resolving predictions. Open issues labeled `task` name a brief and at most 10 records. Comment `claiming` before you start.
- **Errors and disputes.** Use the **Data error** or **Dispute** issue forms. A dispute is recorded, not settled by overwriting (CONTRACT I13).
- **Proposals.** New vocabulary terms, mechanics, schema fields, and rule changes start as a `proposal` in a run file and a **Proposal** issue. A maintainer decides them with an ADR in [`decisions/`](decisions/).

## Make a change

```bash
pip install -r requirements.txt
git config github.user <your-github-handle>   # make pr-check uses it as the PR author
make check                     # green before you start
python scripts/new.py run <slug> --kind <kind> --actor <human|agent> --operator <github-handle> --model <model-id> --purpose "..."
# edit records, following the brief and AGENTS.md
make build && make check       # green before you commit
git commit -s -m "data(games): add three factory games [run:<run-id>]"
```

`dist/` is not committed. CI builds it, checks that the build is deterministic, and the Pages workflow publishes it with the site, so a data PR contains data and a run file only.

A pull request:

- belongs to exactly one run, added in the same PR, and every record it touches names that run in its provenance;
- changes at most 10 records (games, mechanics, techniques, opportunities) and 30 sources;
- never deletes a merged record (deprecate it) and never edits a merged run file.

CI enforces all three (E039) along with every rule in CONTRACT.md §5. It also checks that the PR's run records the current contract version and a recent date, that its operator is the PR author, that no record's `provenance.created` changes, that new ratings come from the PR's run, and that new claims carry a `quote`. The `sources` workflow fetches the sources of the records you touched: it fails when a page holding a source's full text lacks a claim's `quote` or a store id names a different game, and warns, for the reviewer to check by hand, when a source cannot be fetched or only its abstract page can. It blocks merging once it is a required check in branch protection.

## Rules for AI agents and their operators

- **A human operator is accountable for every run.** `operator` is the GitHub handle that opens the PR. The run records the model id and harness truthfully; the independence checks compare them and cannot detect a false entry.
- **Read every source you cite.** A source record means someone opened the work and found the cited content in it. Quotes are copied, never paraphrased, and short (400 characters at most).
- **Independence.** Verifying a record, rating its scores, or resolving a prediction requires a different operator from the run that created it, and a different model when both are agent runs (E035).
- **Calibration.** A run that creates mechanics or adds mechanic ratings first scores the 20-mechanic calibration set and needs within-one agreement of at least 0.8 (E036, `tasks/rate-scores.md`). The reference scores are public, so score it once, from the sheet alone, and record the result.
- **Prose cannot outrun data.** A record whose text states a finding about the dataset carries `assertions` that fail the build when the data stops supporting it (E032). Report prose does the same with `{{assert:...}}` tokens (E029).
- **Say what you did.** The run's `method` describes what was searched, read, and computed, including what failed. Proposals record what the procedure did not allow.

## Review

Paths in [`.github/CODEOWNERS`](.github/CODEOWNERS) need the maintainer's review: the contract and its code, the report and its analysis parameters, mechanics, opportunities, and the calibration set. Games, techniques, sources, and run files merge on green CI plus one maintainer approval.

## Licensing of contributions

By opening a pull request you agree that your contribution is licensed under the repository's licenses ([`LICENSE`](LICENSE)): Apache-2.0 for code, CC BY 4.0 for data, vocabularies, schemas, and text. You certify the [Developer Certificate of Origin 1.1](https://developercertificate.org/) for each commit by signing it off (`git commit -s`, which adds `Signed-off-by: Your Name <email>`); CI checks that every non-merge commit in a PR is signed off. For agent-written commits, the operator signs off.

Quoted excerpts from sources stay the property of their authors and are included as short citations for verification. Do not paste long passages, full tables, or images from sources.

## Conduct

Everyone taking part follows the [Code of Conduct](CODE_OF_CONDUCT.md).
