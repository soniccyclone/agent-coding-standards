---
type: lesson
title: "Turn a find-the-best solver into a find-them-all solver by subtraction"
figure: ullman
works: [mining-of-massive-datasets]
axes: [primitive-count, cognitive-load]
subdomains: [algorithms-and-complexity]
tags: [lesson]
---
# Turn a find-the-best solver into a find-them-all solver by subtraction

**Lesson:** You often have a cheap iterative method that finds only the single dominant thing — the largest component, the strongest signal, the most influential contributor — and a requirement for the whole ranked list. The exact general method exists and costs far more, sometimes prohibitively so. Before paying for it, check whether the dominant thing can be *removed* from the problem: construct a modified instance in which the found item's contribution is exactly cancelled and everything else is untouched. If so, running the cheap method again on the modified instance yields the second item, and the whole list falls out of repeated application of a solver that only ever does one job.

The construction has to be verified in two directions and both are easy to forget. The thing you removed must genuinely be gone — applying the method to the modified instance must not rediscover it — and everything you did not remove must be genuinely unchanged, with the same status in the modified instance as in the original. Only when both hold is the second run answering the question you think it is. Skipping the second check is the common error, because a subtraction that visibly kills the target often perturbs the rest as a side effect, and then the second answer is about a problem you did not intend to pose.

What makes this worth reaching for is the shape of what it buys. One simple, well-understood primitive plus a subtraction step replaces a large piece of specialised machinery, and you get the results one at a time in decreasing order of importance — so you can stop as soon as you have enough, rather than computing the full decomposition and discarding most of it. That incrementality is frequently the real prize, since these lists are usually truncated anyway.

The costs are equally specific. Errors from each extraction are baked into the instance the next extraction sees, so accuracy degrades down the list in a way a one-shot exact method would not suffer. And each item is found under the condition that all previous ones have been removed, so the later items are answers to increasingly constrained questions. Both are acceptable when you want the leading few and unacceptable when you want the full list to equal precision — which is exactly the criterion for deciding whether to use this or pay for the general method.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the power-iteration section of the dimensionality-reduction chapter, which finds the principal eigenpair by repeated normalised multiplication, then forms a modified matrix by subtracting the outer product of the found eigenvector scaled by its eigenvalue, and verifies both that the found eigenvector becomes an eigenvector of the new matrix with eigenvalue zero and that every other eigenpair of the original matrix survives unchanged.
