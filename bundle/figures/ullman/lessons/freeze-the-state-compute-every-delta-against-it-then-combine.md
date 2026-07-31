---
type: lesson
title: "Freeze the state, compute every delta against it, then combine"
figure: ullman
works: [mining-of-massive-datasets]
axes: [parallelizability, hardware-affinity]
subdomains: [distributed-systems-and-concurrency, algorithms-and-complexity]
tags: [lesson]
---
# Freeze the state, compute every delta against it, then combine

**Lesson:** A great many procedures are sequential for one reason only: they carry a piece of state that each step reads and writes, so step two must wait for step one to finish updating it. That is a genuine dependency and it cannot be wished away — but it can be *approximated* away when the per-step changes are small. Hold the state fixed for a whole batch of items. Compute, independently and in parallel, the change each item would have proposed against that fixed state. Then combine all the proposed changes into one new state and repeat. Nothing in the batch waits for anything else in it.

The result is not identical to the sequential run, and being clear-eyed about that matters. Each item was evaluated against a slightly stale state — the state as of the start of the batch rather than as of that item's turn. When the increments are small, the staleness is small, and the trajectory the batched version follows stays close to the sequential one, arriving at a comparable place. When the increments are large, or the batch is enormous, the two diverge and the batched version can oscillate or fail to settle. The step size and the batch size are therefore coupled parameters, not independent ones, and treating them as independent is how these schemes go wrong.

Two structural details make it practical. The proposed changes should be emitted as sparse contributions keyed by which part of the state they touch, so that combining them is an independent aggregation per part rather than a merge of full copies — which is what lets the combine step parallelise too. And the same items can be reused in the next batch rather than requiring fresh ones, because the state has moved and their contribution against the new state is different; re-examining evidence you have already seen is productive, not wasteful, once the thing you are evaluating it against has changed.

The general recognition is worth keeping: when told that a process is inherently sequential, ask whether it is sequential because each step *needs* the previous result or merely because each step *reads* it. If the second, and the reads are of something that moves slowly, a batch of steps can share one snapshot and the whole thing parallelises with a bounded loss of fidelity. That is one of the few reliable routes from a serial algorithm to a distributed one.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the parallel-implementation section of the perceptron chapter and the accompanying "key trick to obtain parallelism" box: fixing the weight vector across a batch, having each worker emit a keyed increment for each nonzero component of each misclassified example, summing the increments per component to form the new state, repeating until convergence, and reusing the same training data on later rounds because its effect differs once the state has changed.
