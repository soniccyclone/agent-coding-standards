---
type: lesson
title: "The bookkeeping a mechanism needs is a cost of the mechanism, not of the problem"
figure: herlihy
works: [transactional-memory-architectural-support-for-lock-free-data-structures]
axes: [primitive-count, hardware-affinity]
subdomains: [distributed-systems-and-concurrency, operating-systems-and-systems-programming]
tags: [lesson]
---

# The bookkeeping a mechanism needs is a cost of the mechanism, not of the problem

**Lesson:** Compare two ways of incrementing a shared counter by counting only the operations that actually reach shared memory. The mutual-exclusion version reads a guard word, writes it to claim it, reads the counter, writes the counter, and writes the guard word again to release it: three of those five accesses concern a word that is not part of the data and exists only because the coordination scheme requires somewhere to record whose turn it is. The optimistic version reads and writes the counter and then asks a local question about whether anything intervened. The performance gap that shows up under contention is not subtle tuning; it is a direct consequence of one scheme carrying auxiliary state on the hot path and the other not. And the auxiliary state is not intrinsic to the problem of incrementing a counter — it is rent paid to the mechanism.

The deeper observation is where that rent comes from. A word-wide conditional-update instruction applied straight to a single-word datum needs no guard at all, and measurably wins. The moment the datum spans more than one word, that same instruction can no longer be applied to the datum itself, so it gets used to build a guard word instead, and all the bookkeeping traffic reappears. The auxiliary state is therefore an artifact of a mismatch between the width of the available primitive and the width of the thing being updated — the indirection exists to bridge a gap in the primitive, and it disappears if the primitive is generalized along the dimension where its restriction was arbitrary rather than fundamental. That is a much better diagnosis than "locks are slow," because it tells you what to change.

For a programmer the transferable move is to itemize, for any coordination scheme, which of its memory touches are the work and which are the protocol, and then to ask what would have to be true of the primitive for the protocol touches to go away. Very often the answer is that the primitive is narrower, coarser, or more single-shot than the data it is guarding, and the extra state is compensating for that. This also sharpens how to read a benchmark: a scheme can lose not because its logic is worse but because it maintains more shared state, and that is an argument about mechanism design, not about the algorithm on top.

**Source:** [Transactional Memory: Architectural Support for Lock-Free Data Structures](../works/transactional-memory-architectural-support-for-lock-free-data-structures.md) — the counting-benchmark discussion enumerating the shared references each scheme requires per increment and attributing the difference to the absence of an explicit lock variable, together with the observation that the single-word conditional-update primitive only wins where the object fits in one word.
