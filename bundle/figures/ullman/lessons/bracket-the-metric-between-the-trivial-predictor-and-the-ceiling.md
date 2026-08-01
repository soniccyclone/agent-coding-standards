---
type: lesson
title: "Bracket a metric between the trivial predictor and the ceiling before you spend"
figure: ullman
works: [mining-of-massive-datasets]
axes: [verifiability, cognitive-load]
subdomains: [algorithms-and-complexity, software-engineering-and-architecture]
tags: [lesson]
---
# Bracket a metric between the trivial predictor and the ceiling before you spend

**Lesson:** A percentage improvement target sounds like a specification and is not one, because it says nothing about the range the percentage is measured against. Before committing effort to beating a number, locate two other numbers: what the most stupid available predictor scores, and what the metric would look like if the task were solved as well as it can be. The interval between them is the entire space in which any skill can show up. If a deployed production system sits a few percent above the score you get from averaging two column means, then almost all of its apparent value is baseline, the remaining band is narrow, and a headline goal of beating it by a tenth is a much smaller claim than it appears.

The other end of the bracket is just as informative and gets checked even less often. Translate the metric back into the units of the thing being predicted and ask what the error means physically. A root-mean-square error near one on a five-point scale means the typical prediction is off by a full point, which is most of the usable resolution of the scale. That is a statement about the ceiling: the signal available in the data does not support fine prediction of individual responses, and no method will make it, so a large multi-year effort inside that band buys refinements that are invisible in any single decision the system makes. Knowing this does not mean the work is worthless, but it changes what you are claiming to have achieved and it changes what you would tell someone deciding whether to fund it.

Both numbers are cheap. The trivial predictor is usually a couple of averages and an afternoon. The ceiling is usually available by reading the metric in the units of the domain and asking a practitioner whether that residual matters. Skipping them is how a whole field ends up organised around relative improvements to a quantity whose absolute value nobody has interpreted, and how a benchmark can attract years of talent for gains that live entirely inside the noise of the underlying judgement. The habit to build: whenever someone quotes an improvement, ask what the dumbest thing scores and what perfect would look like, and only then decide whether the gap is worth crossing.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — chapter 9's discussion of the Netflix challenge, which reports that the incumbent system had a root-mean-square error near 0.95 on a one-to-five star scale, that predicting from the average of a user's mean rating and a movie's mean rating came within three percent of it, and that the million-dollar prize required a ten percent relative improvement, finally won after more than three years.
