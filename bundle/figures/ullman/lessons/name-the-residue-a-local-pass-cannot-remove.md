---
type: lesson
title: "When you push a global operation earlier, name the residue it cannot remove"
figure: ullman
works: [mining-of-massive-datasets]
axes: [verifiability, parallelizability, cognitive-load]
subdomains: [distributed-systems-and-concurrency, algorithms-and-complexity]
tags: [lesson]
---
# When you push a global operation earlier, name the residue it cannot remove

**Lesson:** A useful and dangerous move in pipeline design is to run a late, global operation early and locally — deduplicate inside each producer instead of only at the collector, pre-sum inside each partition, filter before shipping. The move is licensed when the operation can be applied to arbitrary subsets and combined afterwards without changing the result, and its payoff is real: less data crosses the expensive boundary, and the crossing is usually the dominant cost. The danger is the slide from "I applied it early" to "it is done." Local deduplication removes duplicates that happened to land in the same producer and leaves untouched two identical items produced in different places. Local summation gets you partial sums, not sums. The early pass is volume reduction; it is not the answer.

So the discipline is to say out loud, at the moment you add the early pass, what is *left over* — the precise class of discrepancy that survives it — and to confirm that a later stage still handles that class in full. If you can state the residue, the optimisation is safe and you know why. If you cannot, you have not proven the pass is legitimate, you have only assumed it, and the way that failure presents is uniquely nasty: results are correct on small inputs, correct in tests where everything lands in one partition, and quietly wrong at scale, where the wrongness is proportional to how well the system parallelised. Better throughput makes the bug worse.

Once framed this way the criterion for pushing work earlier stops being folklore. You are asking whether the operation is one whose global result can be assembled from results on the pieces, which is a property of the operation's algebra and not of your data or your framework. Sums and maxima and set unions qualify; averages do not without carrying a count alongside; medians and exact distinct counts do not at all. Rather than memorising which is which, get in the habit of asking what a partial result even means for the operation in question. If a partial result is a valid input to the same operation, you can push it early. If it is a different kind of object, you cannot, and pretending otherwise is where the silent corruption lives.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the MapReduce chapter's treatment of combiners for associative and commutative reducers, together with the projection algorithm, which notes that a local combiner eliminates duplicates within one map task but that the global duplicate-elimination step is still required for identical tuples arising in different tasks.
