---
type: lesson
title: "Optimize any monotone transform of your objective"
figure: ullman
works: [mining-of-massive-datasets]
axes: [hardware-affinity, cognitive-load]
subdomains: [algorithms-and-complexity, programming-languages-and-semantics]
tags: [lesson]
---
# Optimize any monotone transform of your objective

**Lesson:** A question of the form "which configuration scores best" does not depend on the scale the score is expressed in — only on the order. That means you are free to replace the objective with any strictly increasing function of it and get the identical answer, and it is worth developing the habit of asking, every time you write down a scoring function, which transform of it would be nicer to work with. This is not a micro-optimisation; it routinely changes an expression from unusable to usable, and it costs nothing because the invariant you need is order, not value.

Two payoffs recur. The structural one: a transform can convert the operation combining your terms into a cheaper or better-behaved one — products into sums being the standard example — which turns a deeply nested expression into a flat accumulation you can differentiate term by term, evaluate incrementally, distribute across machines, and read. The numerical one: scores built by multiplying many small quantities underflow, and the underflowed value is not merely imprecise but exactly zero, so it destroys the comparison entirely rather than degrading it. Working in the transformed space keeps every quantity in a range the machine represents well, and turns error accumulation from multiplicative into additive.

The discipline that keeps this safe is remembering what the transform does and does not preserve. The ranking survives, and so does the location of the optimum. Absolute magnitudes do not, differences do not mean what they meant, and anything downstream that treats the score as a quantity rather than a rank — averaging it, thresholding it against a number chosen in the original units, reporting it — has to be revisited. Transform for the search, and convert back only at the boundary where a human or another system consumes the number, if it needs converting at all.

The same reasoning generalises past logarithms. Dropping constant factors and constant addends, squaring to remove a square root, negating to turn a minimisation into a maximisation, comparing on a monotone proxy that is cheaper to compute than the real quantity — all of these are the same move: identify the weakest property of the objective your question actually depends on, then exploit every freedom that property leaves you.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the log-likelihood sidebar in the overlapping-communities chapter, noting that products become sums and that summing is less prone to rounding error than multiplying many tiny numbers, together with the following section's use of the identity between maximising a function and maximising its logarithm to simplify the affiliation model's likelihood expression before applying gradient descent.
