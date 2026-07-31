---
type: lesson
title: "Inherently serial usually means nobody looked for the regrouping"
figure: ullman
works: [mining-of-massive-datasets]
axes: [parallelizability, cognitive-load]
subdomains: [algorithms-and-complexity, distributed-systems-and-concurrency]
tags: [lesson]
---
# Inherently serial usually means nobody looked for the regrouping

**Lesson:** A computation defined as "each result depends on the one before it" reads as unparallelisable, and the reading is usually wrong. The definition describes one way to produce the results, not the dependency structure of the results themselves. When the accumulation is over an associative operation, results can be regrouped: compute the two halves independently, and then repair the second half by applying the first half's total to every one of its entries at once. Repairing everything at once is a single parallel step, the two halves were independent, and recursing gives a depth logarithmic in the input where the sequential reading suggested depth equal to the input.

The property that licenses this is associativity, and it is worth checking rather than feeling. If the combining operation is associative, the grouping of the operations is free, and freedom of grouping is exactly what allows an independent subproblem to be solved before the value flowing into it is known. Commutativity is not required and is a separate question — order can be preserved while grouping is rearranged, which is what makes the technique applicable to genuinely ordered computations like running totals, running maxima, and scan-like traversals over sequences.

The economics deserve stating because they are not free. The parallel version performs more total operations than the sequential one, since the repair step touches entries that the sequential version handled implicitly. You are trading additional work for reduced depth, which is the same trade behind every latency-oriented restructuring, and it pays exactly when you have idle capacity and a deadline. On one processor the sequential version is better and always will be.

The habit worth building is a suspicion of the phrase "inherently serial." Sometimes it is true — the dependency is genuine and the operation has no algebraic structure to exploit. Very often it describes a formulation rather than a problem, and the test is a specific question with a yes-or-no answer: is the combining operation associative? If it is, a logarithmic-depth version exists, whether or not you have seen it written down.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the parallel-design section of the decision-tree chapter, which notes that the accumulated sums needed at each candidate split appear to be inherently serial, then gives the divide-and-conquer construction: compute accumulated sums for each half in parallel, add the left half's final sum to every entry of the right half in one parallel step, and observe that this yields all the sums in a number of parallel steps one more than the base-two logarithm of the list length.
