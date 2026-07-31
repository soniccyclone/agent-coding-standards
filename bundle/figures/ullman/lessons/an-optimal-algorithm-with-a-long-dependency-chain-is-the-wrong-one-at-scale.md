---
type: lesson
title: "An optimal algorithm with a long dependency chain is the wrong one at scale"
figure: ullman
works: [mining-of-massive-datasets]
axes: [parallelizability, hardware-affinity]
subdomains: [distributed-systems-and-concurrency, algorithms-and-complexity]
tags: [lesson]
---
# An optimal algorithm with a long dependency chain is the wrong one at scale

**Lesson:** The best-known algorithm for a problem is often best in a model with one processor and uniform memory access, and that superiority can be inseparable from a structure that cannot be spread across machines. Depth-first traversal is the classic case: it is elegant, linear, and provably optimal, and its correctness depends on visiting things in an order determined by everything visited before, which is a dependency chain as long as the input. You cannot cut that chain without changing the algorithm into a different one. So the choice on a cluster is not between the optimal algorithm and a worse one; it is between an algorithm that does not run and one that does.

What replaces it usually looks embarrassing by sequential standards — repeated passes, redundant work, randomisation, an approximate or partial answer. But those properties are what makes it decomposable, and total work is the wrong figure of merit once the constraint is coordination. An approach that does several times the arithmetic in a handful of independent, wide steps beats an approach that does the minimum arithmetic in a chain of dependent ones, and the crossover is not far out. Accepting a worse constant, or even a worse exponent, in exchange for shallow dependencies is the routine trade, not an exceptional one.

The habit this argues for is reading algorithms for their dependency structure alongside their complexity. The question is not only how much work there is but how much of it must happen after some other part. Complexity notation hides this completely: two procedures with identical bounds can have depth proportional to the input and depth proportional to its logarithm, and nothing in the notation distinguishes them. Making a habit of asking "what must finish before what" turns a lot of algorithm selection from lore into analysis.

There is a corollary about where to spend design effort. If the sequential method is unusable, do not try to parallelise it — its structure is the problem, and incremental restructuring tends to preserve the chain while adding synchronisation. Go back to the specification and look for a different characterisation of the answer, one defined by properties that can be checked locally and combined, rather than by the order in which a single traversal would discover them.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the graph-reduction section of the social-network chapter, which notes that the linear-time algorithm for finding strongly connected components is inherently sequential because it is built on depth-first search and therefore ill-suited to large graphs, and instead adopts a randomised scheme using two reachability computations per randomly chosen node.
