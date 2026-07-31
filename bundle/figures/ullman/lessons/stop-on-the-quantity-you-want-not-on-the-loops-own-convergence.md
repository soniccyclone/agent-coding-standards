---
type: lesson
title: "Stop on the quantity you want, not on the loop's own convergence"
figure: ullman
works: [mining-of-massive-datasets]
axes: [verifiability, cognitive-load]
subdomains: [algorithms-and-complexity, software-engineering-and-architecture]
tags: [lesson]
---
# Stop on the quantity you want, not on the loop's own convergence

**Lesson:** Iterative procedures are usually specified as "repeat until settled," which quietly assumes two things: that settling will happen, and that settling is what you wanted. Both fail routinely. If the input does not admit a solution of the form the procedure is searching for, the procedure does not fail — it cycles, indefinitely, through states that look exactly like progress. And detecting the cycle is generally infeasible, since it would require remembering every state visited and the period may be astronomically long. So the loop has a non-terminating case that it cannot recognise from the inside, which means an external bound is not a safety net bolted on afterwards but a required part of the specification.

The deeper point is the second assumption. Even when the procedure does settle, settling means it has perfectly accommodated the evidence it was shown — which is a statement about the sample, not about the population. If the sample admits an exact accommodation and the population does not, then running to convergence is running past the point of usefulness and into fitting the sample's peculiarities. The quantity being driven to zero is not the quantity you care about; it is a proxy that coincides with it early and diverges from it late.

That argues for stopping criteria of a different kind. A fixed budget is crude but honest, and bounds the cost. A plateau in the error on the data you are fitting says the procedure has stopped learning from it, which is cheap to check but still measures the proxy. The one that actually addresses the problem is to evaluate, after each round, on evidence the procedure is not fitting, and stop when *that* stops improving — because it is a direct measurement of the thing you want, and it turns over rather than monotonically decreasing, so it has an interior optimum you can detect.

The habit worth carrying: for every loop that runs to a fixed point, ask what happens when no fixed point exists, and ask whether the fixed point is the outcome you wanted or merely the outcome the loop is built to find. Those two questions catch a large fraction of the ways iterative procedures go wrong, and both are answerable at design time.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the convergence-of-perceptrons section, which notes that on non-separable data the algorithm eventually repeats a weight vector and loops forever, that detecting this by remembering previous vectors is infeasible and the period would be impractically long anyway, that the training set may be separable while the full dataset is not, and which then lists termination after a fixed number of rounds, termination when the misclassification count stops changing, and termination when the error on a withheld set stops changing.
