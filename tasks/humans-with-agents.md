# For invited contributors who work through an AI agent

You direct an agent; the agent does most of the reading and typing; you are accountable for what it submits. This page is the human half of that arrangement. The agent's half is `AGENTS.md`, which every common agent reads on its own.

## What you can do that the maintainer's agents cannot

Most records were created by runs operated by the maintainer. The independence rule (E035) means only a different operator can verify those records, rate their scores, or resolve their predictions. Those three jobs are why you were invited.

| Job | Brief | Why it needs you |
|---|---|---|
| Verify records | `tasks/verify-record.md` | A record becomes `verified` only when someone other than its creator checks it against a primary source |
| Rate scores | `tasks/rate-scores.md` | Every rubric score so far is one model's reading; a second, calibrated rater turns it into measured agreement |
| Resolve predictions | `tasks/resolve-prediction.md` | A bet cannot be judged by the run that made it |
| Review each other's PRs | `CONTRIBUTING.md` | Games, techniques, and sources merge on green CI plus one approval, which can be yours |

You can also take any other task (catalogue games, quote claims, archive sources, add store ids).

## Setup, about 15 minutes

```bash
git clone https://github.com/yoheinakajima/simgrammar && cd simgrammar
pip install -r requirements.txt
git config github.user <your-github-handle>
make hooks                                   # runs the validator before every commit
make check                                   # green before you start
```

Your agent finds its instructions without help: Claude Code reads `CLAUDE.md`, Codex and most others read `AGENTS.md`, Cursor reads `.cursorrules`, Gemini reads `GEMINI.md`, and GitHub Copilot reads `.github/copilot-instructions.md`. All of them point to `AGENTS.md`.

You have write access to the repository, but `main` is protected: you work on a branch, open a pull request, and it merges when the checks pass and someone approves it. Paths the maintainer owns (`.github/CODEOWNERS`) also need the maintainer's approval.

## Handing a task to your agent

Pick an issue labelled `task`, comment `claiming`, and give your agent something like this:

```
You are contributing to SimGrammar on my behalf. I am <your-github-handle>, the operator; record your
exact model id and harness in the run. Read CLAUDE.md (or AGENTS.md) and follow it. Task: issue #<n>,
<paste the issue body>. Open one run of the kind the issue names, do only what the issue lists,
quote every claim you add verbatim from a source you actually opened, run `make check` and
`make pr-check`, and commit on a branch named task/<brief>-<your-handle> with `git commit -s`.
Then stop and give me: the files you changed, every source you opened, and anything you could not verify.
```

## Before you open the pull request

You sign off every commit (`git commit -s`), which certifies the Developer Certificate of Origin for the work. Check these five things yourself; they are the ones CI cannot fully check.

1. **The diff is what the issue asked for.** No unrelated records, at most 10 records and 30 sources.
2. **Open two or three of the cited sources yourself.** Confirm each says what the claim says. CI checks that quotes appear in their sources; it cannot check that a quote supports the claim.
3. **Status changes are earned.** `verified` only after a real check against a non-wiki source; a disagreement becomes `contested` with both sides, never an overwrite.
4. **The run file is honest.** Operator is you, the model id is the agent's real one, and `method` says what was opened and what failed.
5. **`make check` and `make pr-check` are green.** The second needs network access to check quotes; if your machine has it, so will CI.

Open the PR from your own account (the operator must be the PR author) and link the issue.

## Calibrating before you rate

Whoever produces the scores calibrates: if your agent rates, your agent's run carries the calibration; if you rate by hand, yours does, with `--actor human`. Score the sheet once, from the sheet alone, before reading stored scores (`tasks/rate-scores.md`). The reference scores are public, so the procedure is only as blind as you keep it.

## A first week

| Day | Do | Brief |
|---|---|---|
| 1 | Set up, run `make check`, read `CONTRACT.md` sections 1 and 2 | this page |
| 2 | Review one open pull request from another contributor or agent, using the checklist above | `CONTRIBUTING.md` |
| 3 | Claim one `verify-record` issue and take it to a merged PR | `tasks/verify-record.md` |
| 4 | Calibrate, then claim one `rate-scores` issue | `tasks/rate-scores.md` |
| 5 | Write down what slowed you or your agent down, as an issue | `tasks/README.md` |

Disagree with a record, a rule, or another contributor? Open a **Dispute**, **Data error**, or **Proposal** issue. Disagreement is data here (CONTRACT I13), not something to settle by editing over each other.
