---
type: lesson
title: "The unit you move data in is a consequence of where the cost sits, so re-derive it whenever a new tier changes the cost shape"
figure: wilkes
works: [slave-memories-and-dynamic-storage-allocation]
axes: [hardware-affinity, cognitive-load]
subdomains: [operating-systems-and-systems-programming, algorithms-and-complexity]
tags: [lesson]
---
# The unit you move data in is a consequence of where the cost sits, so re-derive it whenever a new tier changes the cost shape

**Lesson:** Every tiered storage arrangement carries a transfer granularity, and that granularity is almost never chosen on its merits — it is inherited from whatever tier the practice grew up around. When the slower party charges a large fixed price per transfer and a negligible price per additional word, moving data in big chunks is not a heuristic, it is arithmetic: the fixed cost has to be amortized over something, so you amortize it over as many words as you can plausibly justify wanting. Block transfer, prefetch windows, page-in, batch reads from a queue — all of them are the same derivation run against the same cost shape.

The trap is that the derivation is invisible once the practice becomes habit, so it survives into settings where its premise is gone. Insert a tier where both sides are true random access and the fixed per-transfer cost drops out of the equation entirely; the arithmetic that recommended chunking now recommends the opposite, because every word moved beyond the one actually wanted is unamortized waste with nothing to spread it over. The correct granularity collapses to a single item, and a design that keeps moving blocks is paying a tax justified by a constraint that no longer exists. The same reversal happens on the way to any tier whose cost is per-request rather than per-byte, or per-byte rather than per-request: same structure, opposite conclusion.

The discipline this asks for is to keep the cost model attached to the policy rather than only the policy. Write down, next to any batching or chunking decision, the two numbers it was derived from — the fixed cost of initiating a transfer and the marginal cost of one more unit — because those numbers are what a future reader needs in order to know whether the decision still holds. When a new layer lands in the hierarchy, the question is not whether to tune the block size but whether the ratio that produced a block size at all is still what it was.

**Source:** [Slave Memories and Dynamic Storage Allocation](../works/slave-memories-and-dynamic-storage-allocation.md) — the introduction's contrast between core backed by drum or tape, where moving information in blocks is described as the natural and efficient thing to do, and a fast core memory backed by a large slow core memory, where both levels are genuinely random access with no latency and the time spent transferring words the program never touches is simply wasted.
