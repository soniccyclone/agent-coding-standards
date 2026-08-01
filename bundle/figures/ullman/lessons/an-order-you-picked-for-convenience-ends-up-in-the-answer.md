---
type: lesson
title: "An order you picked for convenience ends up inside the answer"
figure: ullman
works: [mining-of-massive-datasets]
axes: [verifiability, cognitive-load, expressiveness]
subdomains: [algorithms-and-complexity, databases-and-data-management]
tags: [lesson]
---
# An order you picked for convenience ends up inside the answer

**Lesson:** A procedure that applies several corrections, or fits several parameters, has to do them in some sequence, and the sequence is almost always chosen for implementation convenience: rows before columns, left to right, whatever the loop happened to iterate over. That choice looks like scaffolding. It frequently is not. If the operations do not commute, the sequence is a modelling assumption that nobody wrote down and nobody can defend, and it will be visible in the output. Two adjustments that each remove a per-group offset are the cleanest case: subtract the row offsets and then the column offsets and you get one result, reverse the order and you get another, because the second subtraction operates on data the first has already changed. Nothing in the problem says which is right.

There are two honest exits, and both are cheap. The first is to symmetrise: instead of applying one correction and then the other, construct a single adjustment that treats them evenly, such as removing half of each offset at once. That removes the choice rather than making it, which is the better outcome whenever no principled ordering exists. The second is to measure the disagreement and show it is small, which converts an unexamined assumption into a bounded one. Note the asymmetry in how much these cost you if skipped: an ordering artefact does not announce itself, it just sits in every downstream number as a small unexplained bias, and it is nearly impossible to find later because nobody thinks to look at the loop.

The same hazard appears in a different disguise when parameters are fitted one at a time to a shared residual. Solving exactly for one coordinate while holding the rest fixed is attractive because it has a closed form and needs no step size, but exactness is precisely the problem: the coordinate visited first absorbs all the structure the data will let it absorb, including structure that other coordinates would have explained equally well. Whatever you happened to optimise first ends up carrying an outsized share of the fit, and the resulting model encodes your traversal order as though it were a belief about the domain. Moving each parameter only part of the way toward its locally optimal value breaks that. The full step is greedy in an ordering you invented; the partial step lets every parameter compete for the same evidence across successive rounds. Whenever a result depends on a sequence, either justify the sequence or make the result stop depending on it.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — chapter 9's preprocessing and overfitting discussions in the UV-decomposition section: the note that subtracting user averages then item averages need not agree with the reverse order, the third option of subtracting half the sum of both averages, and the recommendation to avoid favouring the first components optimised by moving each element only a fraction of the way toward its computed optimum.
