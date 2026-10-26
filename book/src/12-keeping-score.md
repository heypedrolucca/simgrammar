# Chapter 12. Keeping score

On {{stat:first_prediction_resolves}}, {{stat:n_predictions_first_date}} of the dataset's predictions come due on the same day.{{assert:n_predictions_first_date >= 5}} One of them belongs to the top-ranked bet from chapter 10, the why-query. It reads, in full: a widely played simulation or strategy game will let players ask in natural language why something happened in their own game and answer from game state.

Suppose you are the person who checks it. The prediction's criteria tell you exactly what to look for, and they are narrower than the sentence. The feature must have first shipped after 24 October 2026, so a game that already had one before the dataset was published does not count. The title must have at least 10,000 Steam user reviews, counted on the resolve date. And the release notes or the store page must describe free-text causal questions answered from the player's own save state, which rules out a chatbot that answers from a wiki or general help text.{{assert:field.causal-why-query.falsifiable_signal.resolve_by == first_prediction_resolves}}

You search patch notes and store pages for the year. You find, say, a strategy game that added an advisor you can type questions to. You open its patch notes: the advisor answers questions about game mechanics from the developer's documentation. That fails the last criterion, because the answers do not come from the player's save. You keep looking. If nothing qualifies, the outcome is `refuted`, and the thesis behind the top-ranked bet in the dataset takes a mark against it.

This chapter is about why every bet in the book carries a prediction like that, how the dataset checks them, and what the book will do with the results.

## A bet that can lose

An opportunity without a date cannot be wrong. "AI will make simulation games more legible" will look plausible in any year, whatever happens. Every opportunity in the dataset therefore carries a falsifiable signal: a one-sentence prediction, a resolve-by date, and criteria written so that a stranger with a browser could decide the outcome from public evidence.

The criteria were not always that strict. When an independent reviewer read the first version of the dataset, the predictions used words like "major", "popular", and "peer studio", relied on store rankings, and had no start date, so a feature that already existed could resolve them; one prediction was already true on the day it was written. The fix, recorded in the project's third decision record, set three rules that every prediction now follows. A feature counts only if it first shipped after 24 October 2026. Size is a stated number of Steam user reviews, or a console release. And the evidence must be developer material: patch notes, a store page, documentation, a talk.

All {{stat:n_predictions}} predictions are open today.{{assert:n_predictions_open == n_predictions}} The table lists them by date.

{{table:predictions}}

They come due over four years. {{stat:n_predictions_by_2027}} resolve by the end of 2027, {{stat:n_predictions_by_2028}} by the end of 2028, and the last on {{stat:last_prediction_resolves}}.{{assert:n_predictions_by_2027 < n_predictions_by_2028}}{{assert:last_prediction_resolves == 2030-12-31}} Most of the early dates belong to bets the dataset rates as buildable now. The late ones belong to the long shots of chapter 10, such as a game rendered by a generative model from a symbolic state, or a mechanic credited to automated discovery.

## Reading criteria literally

Most of the work of resolving a prediction is reading its criteria without adding anything to them. Four of the predictions due on {{stat:first_prediction_resolves}} show the kinds of judgment involved.

The local-first prediction counts titles. It resolves `confirmed` if at least five games with more than 1,000 Steam user reviews use an on-device language model at runtime without needing an internet connection, each one's local-model feature first shipped after 24 October 2026, with store pages or documentation confirming that the inference runs locally.{{assert:field.local-first-ai-sims.falsifiable_signal.resolve_by == first_prediction_resolves}} The checker has to establish two facts per title, the date and the offline operation, and a game that falls back to a server when one is available is a judgment call that has to be explained in the resolution's note.

The simulator-instructor prediction excludes things explicitly. It needs a flight or racing simulator with at least 5,000 Steam user reviews or a console release to ship an official AI voice instructor that speaks generated feedback based on the player's live inputs. Third-party apps do not count, however good they are.{{assert:field.sim-instructor-coach.falsifiable_signal.resolve_by == first_prediction_resolves}}

The decoration-catalog prediction excludes a specific game. It asks for a life or management sim other than [[inzoi|inZOI]] to let players generate new placeable 3D objects from text or images inside the game, because inZOI already did so before the window opened.{{assert:field.generative-decoration-catalogs.falsifiable_signal.resolve_by == first_prediction_resolves}}

The autobalance prediction counts studios. It needs talks, technical blogs, or papers from staff of two different studios, each naming a commercial title with at least 1,000 Steam user reviews and describing automated agent play at scale used to balance its economy.{{assert:field.parallel-autobalance.falsifiable_signal.resolve_by == first_prediction_resolves}} This one can fail because a studio uses the practice without describing it in public. The resolution would record that as `refuted` all the same, and the note would say what was searched.

## Who may resolve one

A prediction is resolved by a pull request, like any other change to the dataset. The procedure is a short brief in the repository. The resolver reads the criteria, finds the evidence, creates source records for it, and adds a resolution to the prediction: an outcome, the date it was checked, the run that checked it, the sources, and a note saying which title met which criterion or which criterion failed.

In the record, a resolution is a few lines of data:

```yaml
resolution:
  outcome: confirmed        # confirmed | refuted | ambiguous | withdrawn
  date: '2028-01-04'        # the day it was checked
  run: 2028-01-04-resolve-why-query
  evidence: [src-...]       # required unless withdrawn
  note: Which title met which criterion, and how it was checked.
```

The outcomes come from a closed list: `confirmed`, `refuted`, `ambiguous`, or `withdrawn`. The validator enforces when each may be used. A prediction can be `refuted` only after its resolve-by date has passed, so nobody can declare a bet lost early. It can be `withdrawn` only before the date, so nobody can withdraw a bet after seeing that it lost. Every outcome except a withdrawal must cite evidence. A prediction that passes its date with no resolution is listed by a warning every time the dataset is built.

The resolver also has to be someone else. All {{stat:n_predictions}} predictions were written in a single synthesis run by an agent running one model under the dataset's maintainer, and the independence rule says a resolution must come from a run with a different operator and, when both runs are agents, a different model. The person who made the bet cannot settle it, and neither can another copy of the model that wrote it. The rule is the same one that governs verifying records and rating scores, and chapter 13 explains how the build checks it.

A refuted prediction counts against the opportunity's thesis as well as its timing. The brief asks resolvers not to edit the thesis in the same pull request. If a bet loses, the record keeps the losing argument next to the evidence that it lost, and any rewrite has to come later, in its own change, where a reader can see what changed and why.

## What the scoreboard will show

Nothing has been checked yet. The first {{stat:n_predictions_first_date}} predictions come due on {{stat:first_prediction_resolves}}, and the scoreboard will start to say something only after that.

It can show several things once it does. The simplest is a count: how many of the bets the dataset ranked highest came true, against how many of the ones it ranked lowest. If the priority scores in chapter 10 mean anything, confirmations should cluster near the top of the table. They may not. A cluster of refutations among the legibility bets would say that the argument running through this book, that explanation is the cheapest and most neglected use of current techniques, was wrong about what studios would build, even if it was right about what players need.

The predictions also test the dataset's maturity scores. Chapter 7 classified each technique as research, prototype, shipped in a niche, or shipped as a norm. A prediction that depends on a research-stage technique and still resolves `confirmed` by its date is evidence that the maturity scale ran behind the field.

The book will report the results. Each edition names the version of the dataset it was built from, and a new edition follows when predictions resolve or the catalog grows substantially. Every number in this chapter is a token, so an edition built after the first resolutions will print different counts, and the sentences asserting that all predictions are open will fail the build until someone rewrites them.

## Exercise: resolve one early

Pick a prediction from the table whose date is more than a year away.

1. Read its criteria and list every fact a resolver would need to establish, each as a yes-or-no question.
2. Search for evidence today. For each question, note whether you found an answer and where.
3. Decide what the outcome would be if the date were today. If any question is open, say what evidence would close it.
4. Write the note you would attach to the resolution, in two sentences, so that someone who never saw your search could check it.

Step 1 usually turns up a question the criteria leave open, and a question like that is grounds for a proposal to sharpen the prediction before it comes due. The rules that would carry such a proposal, from the run that records it to the review it needs, are the subject of chapter 13.
