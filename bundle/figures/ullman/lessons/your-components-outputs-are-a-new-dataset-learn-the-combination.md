---
type: lesson
title: "Your components' outputs are a new dataset — learn the combination"
figure: ullman
works: [mining-of-massive-datasets]
axes: [expressiveness, parallelizability]
subdomains: [software-engineering-and-architecture, algorithms-and-complexity]
tags: [lesson]
---
# Your components' outputs are a new dataset — learn the combination

**Lesson:** When several independent procedures produce opinions about the same question, the combination rule is nearly always chosen by fiat: take the majority, take the average, take the first that answers. Those are defensible defaults and they discard information. Each component has a characteristic reliability — one is good on some region of the input and hopeless elsewhere, another has the opposite profile, a third is mostly redundant with the first — and a fixed rule treats them all as interchangeable. The information needed to do better is already in hand: run every component on the cases whose answers you know, and record the vector of opinions alongside the correct answer. That is a dataset, in exactly the form the same fitting machinery consumes, and fitting to it yields a combination rule tuned to the components' actual strengths.

The reframing worth internalising is that the components' outputs form a legitimate representation of the input in their own right — usually a far shorter one than the original — and that the composition step is not plumbing but a modelling problem of the same kind as the components solve. Once seen that way, everything you know about the inner problem applies to the outer one: it needs its own held-out evidence, it can overfit, and it can be as simple or as elaborate as the amount of that evidence supports.

This also changes what makes a good component. If the combination is learned, individual components no longer need to be good; they need to be *differently wrong*. A collection of shallow, deliberately restricted procedures, each looking at a different slice of the input, will often beat one elaborate procedure, because their errors are uncorrelated and the combination can cancel them. That in turn makes the whole thing cheaper: many small components can be built independently and in parallel, where the single elaborate one is a long serial construction.

The general habit is to look at any place where multiple signals get reduced to one decision — health checks, ranking signals, fraud rules, retry heuristics — and notice that the reduction rule is a parameter nobody fitted. If you have historical outcomes, you have what you need to fit it, and the gain from weighting existing signals correctly is often larger than the gain from adding another signal.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the decision-forest section and the accompanying ensemble-methods box in the large-scale-machine-learning chapter, which build many trees each restricted to a few levels and randomly chosen features, note that they collectively outperform any single deep tree and can be constructed in parallel, and then form a new training set whose feature vector is the vector of the trees' outputs on each original example, to be fitted by a perceptron or support-vector machine so the trees' opinions are weighted optimally.
