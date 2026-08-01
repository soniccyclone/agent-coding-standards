---
type: lesson
title: "A cascading merge rule is an increment: read off its radix"
figure: ullman
works: [mining-of-massive-datasets]
axes: [cognitive-load, hardware-affinity, verifiability]
subdomains: [algorithms-and-complexity, operating-systems-and-systems-programming]
tags: [lesson]
---
# A cascading merge rule is an increment: read off its radix

**Lesson:** A structure maintained by the rule "when there are too many components of a given size, combine two of them into one component of the next size up, and repeat if that overflows too" is not merely reminiscent of counting, it is counting. The occupancy of each size class is a digit, the combination step is a carry, and the occasional long chain of merges after a single arrival is the same event as the carry that propagates from a run of nines. Recognising this is not decoration. It hands you the cost analysis immediately: the number of size classes is the number of digits, so worst-case work per arrival is logarithmic, while carries at each position occur geometrically less often, so amortised work is constant. You did not have to invent either bound.

The more valuable thing recognition buys is the design knob, which is otherwise invisible. Allowing one or two components per size is base two. Allowing up to some larger number per size is a higher radix, and the redundancy that comes with permitting more than one representation of the same total is what lets the structure absorb arrivals with fewer cascades and, in schemes where the largest component is the source of uncertainty, what tightens the error. So the parameter that looks like an arbitrary implementation choice — how many of each size are permitted before merging — is the base of a positional number system, and its effect on space, on update cost, and on accuracy can all be derived rather than measured. Someone who has not made the identification will tune that parameter empirically and will not know what else moves when they change it.

The general habit is to check whether the invariant you are maintaining has a counterpart in some well-worn representation before treating it as bespoke. Invariants of the form "at most k of each rank, ranks never decrease, sizes are powers of something" are number representations wearing different clothes, and they turn up in mergeable heaps, log-structured merge trees, level-based compaction, batched rebuilding, and any bucketed summary of a stream. Each of those inherits the same analysis and the same knob.

There is a design principle underneath as well. The invariant that bounds the structure's size and the schedule that governs its update cost are not two decisions but one, and choosing the invariant fixes the schedule whether or not you looked. That is worth knowing before you pick an invariant for space reasons alone and then discover the tail latency it implies. The cascade is where the cost hides: rare, deep, and paid entirely by whichever unlucky arrival triggers it, which is fine if you are averaging and unacceptable if you are quoting a worst case.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the boxed aside in chapter 4 that reads bucket counts in the window-counting algorithm as binary digits and the combination of equal-sized buckets as ripple-carry, together with the following section's relaxation to a larger permitted number of buckets per size as the means of tightening the error bound.
