---
type: lesson
title: "An optimality proof is scoped to the shape you quantified over"
figure: ullman
works: [mining-of-massive-datasets]
axes: [verifiability, parallelizability]
subdomains: [algorithms-and-complexity, distributed-systems-and-concurrency]
tags: [lesson]
---
# An optimality proof is scoped to the shape you quantified over

**Lesson:** A matching lower bound is the strongest result available about a design: it says your construction cannot be improved, and it lets you stop optimising with a reason rather than from fatigue. It is also the result most often overread. The bound was proved by quantifying over some class of candidate designs, and that class was fixed by structural assumptions you probably made without noticing — that the computation happens in one round, that the workers do not talk to each other, that the intermediate results are never written down. Everything outside that class is untouched by the proof. So when a bound tells you a design is optimal, the operative question is not "how do I beat it" but "which of my assumptions defined the class, and what happens if I drop one".

The concrete instance is worth internalising because it inverts the usual instinct. A single-round distributed matrix product has a lower bound on data movement that the natural blocked algorithm meets exactly, so within one round the matter is settled. Running the same computation in two rounds — partial products in the first, summed in the second — moves strictly less data at the same per-worker capacity, and the improvement is large rather than marginal. No contradiction: the two-round algorithm was never a member of the class the bound quantified over. This directly contradicts the reflex that fewer coordination steps must be cheaper, which is exactly why the reflex is worth distrusting. The extra round can pay for itself because it lets you keep an intermediate in a form that has to be shipped once instead of a form that has to be replicated.

The habit that falls out of this is to treat each structural assumption as a knob rather than as the ground. Write down what you assumed about the shape of the computation — the number of phases, whether state persists between them, whether outputs are materialised or streamed — and price the alternative for each. Most of the time the assumption is the right one and you have lost ten minutes. Occasionally the whole bound evaporates, and the gain is not the few percent that further optimisation inside the class would have yielded. The same discipline protects you in the other direction: when you prove a bound of your own, state the class explicitly in the claim, because a bound quoted without its scope will be believed in situations it says nothing about.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the complexity-theory chapter's case study of matrix multiplication, where the replication-rate lower bound derived for one-pass algorithms is met by the band-partitioned algorithm and then beaten by the two-pass algorithm that partitions both matrices into squares, computes partial sums in the first pass and aggregates them in the second, with the second pass's communication working out to half the first's.
