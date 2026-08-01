---
type: lesson
title: "The outputs you ship are exactly the ones you never scored"
figure: ullman
works: [mining-of-massive-datasets]
axes: [verifiability, expressiveness]
subdomains: [algorithms-and-complexity, formal-methods-and-verification]
tags: [lesson]
---
# The outputs you ship are exactly the ones you never scored

**Lesson:** There is a family of systems whose objective function is arithmetically incapable of mentioning the thing they are for. Fit a compact model so that it reproduces the observations you have, summing error only over cells where an observation exists, and every term in that sum concerns a value you already knew. The cells you are actually going to act on contribute nothing to the score, cannot contribute, and will never be checked against anything. This is not a flaw to be engineered away, it is the shape of the problem: if you could evaluate the outputs you care about you would not need to predict them. But it should be said plainly, because a low error number invites everyone to believe the outputs have been validated, and none of them have.

What carries the weight from the scored region to the unscored one is not the quality of the fit. It is the structural restriction you imposed. A model with as many free parameters as there are observations can reproduce the observations exactly and say nothing whatsoever about anything else. The claim only becomes meaningful when the parameters are far fewer than the observations, because then agreeing with what you saw is evidence that the model found real regularity rather than transcribed the data, and the same regularity is what generates the values you never saw. The restriction is the entire argument. So the number to report next to your error is the ratio of observations to free parameters, and the design question that matters most is how tight the restriction can be made while still fitting.

Two habits follow. First, be suspicious of any improvement that came from enlarging the model, since it moves you toward the regime where fitting is free and extrapolation is worthless, and the error number will happily improve the whole way down. Second, notice that a convenient property of scoring only observed cells is that missing data needs no invention: absent entries simply contribute no term, so nothing has to be imputed, defaulted, or flagged. That is a much better handling of absence than filling it with a stand-in value, and it generalises. When you can define an objective purely over what you have, missingness stops being a special case in the code and becomes a fact about which terms exist.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — chapter 9's dimensionality-reduction section, where the error between the product of two thin factor matrices and the utility matrix is summed only over non-blank entries, blank entries drop out of the derivative when optimizing a single element, the predicted values are read from precisely those blank positions, and the running example is chosen as the smallest case in which the known entries outnumber the entries of the two factors.
