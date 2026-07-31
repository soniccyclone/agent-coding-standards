---
type: lesson
title: "An estimate that decides what you observe will confirm itself"
figure: ullman
works: [mining-of-massive-datasets]
axes: [verifiability, cognitive-load]
subdomains: [algorithms-and-complexity, software-engineering-and-architecture]
tags: [lesson]
---
# An estimate that decides what you observe will confirm itself

**Lesson:** A system that ranks candidates by an empirical quality estimate, shows only the top ones, and then updates the estimates from what it showed has closed a loop between its belief and its evidence. Whatever the estimate says about a candidate determines how much data that candidate generates, and the data determines the estimate. In that arrangement a low initial value is not a provisional guess to be revised; it is a permanent verdict, because the candidate is never given the exposure that would produce the counter-evidence. The failure is silent — the estimator is unbiased in the narrow sense that it correctly summarises the observations it received, and the observations it received were selected by itself.

The first defence is to notice that initialisation is a policy decision rather than a numerical convenience. Starting everyone at zero is the maximally self-confirming choice; starting everyone optimistic, or reserving a fraction of opportunities for candidates whose estimates are not yet trustworthy, breaks the loop by guaranteeing that each candidate receives enough exposure for its estimate to become an estimate rather than an echo. The cost of that reservation is real and bounded, and it buys the only thing that makes the ranking meaningful in the long run.

The second defence is to separate the effect of the thing being measured from the effect of the treatment your own system applied to it. A candidate's observed success rate confounds its intrinsic quality with the position, timing, and context your policy assigned to it, and if the assignment strongly drives the outcome — as being placed first almost always does — then the raw rate is mostly a measurement of your own ranking, replayed back at you as though it were independent evidence. The correction is to model the treatment explicitly and to score the residual, so that a candidate given the worst slot and doing tolerably is recognised as better than one given the best slot and doing the same. Without that, yesterday's ordering becomes today's justification for the same ordering.

The general form of the check: for any metric that feeds back into the decision that generated it, ask what a genuinely superior candidate would have to do to overtake an incumbent, and confirm there exists a path by which it can accumulate the necessary evidence. If there is no such path, the metric is not measuring quality; it is measuring incumbency, and it will keep doing so no matter how much data accrues.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the advertising chapter's discussion of evaluating ads by click-through, which observes that an ad's position dominates whether it is clicked and that starting every ad at a click probability of zero means it is never shown and so never learned about.
