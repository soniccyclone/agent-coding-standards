---
type: lesson
title: "Find the support of a change and evaluate only that"
figure: ullman
works: [mining-of-massive-datasets]
axes: [hardware-affinity, parallelizability]
subdomains: [algorithms-and-complexity, software-engineering-and-architecture]
tags: [lesson]
---
# Find the support of a change and evaluate only that

**Lesson:** Iterative procedures are typically written as: adjust something, then recompute the objective. When the objective is a sum over the entire system and the adjustment touched one component, that recomputation is almost entirely the recomputation of terms that did not move. Nothing is wrong with the answer, and the cost per step is the size of the whole system when the honest cost of the step is the size of what the change could possibly have affected. For structures where each component interacts with a handful of others, that ratio is not a constant factor — it is the difference between a step costing the total number of interactions and a step costing one component's local degree, which is the difference between a method that runs and a method that does not.

Getting this requires a specific piece of analysis that is easy to skip: identify, for each parameter you can adjust, the exact set of terms in the objective whose value depends on it. That set is the support of the change. Everything outside it is constant across the step and contributes nothing to a comparison between before and after, so it can be omitted entirely rather than computed and cancelled. Note the framing — you are not computing the objective more cleverly, you are computing a *difference*, and differences over a sum only need the terms that differ.

Two conditions make this legitimate and both are worth confirming rather than assuming. The objective must decompose into terms with identifiable dependencies, which is a property of how you wrote it and can sometimes be arranged by rewriting. And the terms must not be coupled through some shared normalisation — a denominator summed over everything reintroduces global dependence and quietly destroys the locality, which is a good reason to prefer formulations without one when a choice exists.

The habit generalises well beyond optimisation loops, because the pattern "small change, full recomputation" is everywhere: rebuilding a whole index after one insert, re-deriving a whole layout after one element moves, revalidating an entire configuration after one field changes. In each case the question is the same — what is the set of things this change could possibly have invalidated — and in each case the answer is what separates a system that scales with the size of the edit from one that scales with the size of the world.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the closing observation of the continuous-membership section in the overlapping-communities chapter, that when the strength parameters of a single node are adjusted, the only terms of the log-likelihood whose values change are those involving that node and a node adjacent to it, so most of the expression can be skipped at each gradient step because a node's degree is typically far smaller than the number of edges.
