## Run

- Run id: `log/runs/<id>.yaml` (exactly one new run per PR)
- Issue: closes #
- Brief: `tasks/<brief>.md` (if any)
- Change class (CONTRACT §3): data / prose / analysis / calibration / vocabulary / rubric / schema / rule
- ADR (required for vocabulary, rubric, calibration, schema, rule): `decisions/ADR-XXXX-...md`

## What changed

<!-- Records added or edited, by id. No counts here; the build reports them. -->

## Checks

- [ ] `make check` is green locally
- [ ] At most 10 records and 30 sources; every changed record names this PR's run in its provenance
- [ ] Every source I cite, I opened and read; every `quote` is copied verbatim
- [ ] I did not verify, rate, or resolve work from my own operator or model
- [ ] I searched with `scripts/find.py` before creating records
- [ ] Proposals I could not act on are in the run file
- [ ] I read the diff, then signed off every commit (`git rebase --signoff origin/main`, or `git commit -s` without an agent)
