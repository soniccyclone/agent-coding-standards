---
type: lesson
title: "Keep history at geometrically decaying resolution"
figure: ullman
works: [mining-of-massive-datasets]
axes: [hardware-affinity, cognitive-load, verifiability]
subdomains: [distributed-systems-and-concurrency, algorithms-and-complexity]
tags: [lesson]
---
# Keep history at geometrically decaying resolution

**Lesson:** Answering questions about arbitrary recent spans of an unbounded stream looks like it requires keeping everything, because the caller may ask about any span. It does not, if you are willing to trade precision at the edges. Summarise the stream in blocks whose sizes double as they age, holding only a bounded number of blocks at each size. Recent history is then described finely, distant history coarsely, and the total number of blocks is logarithmic in the window rather than linear. Since each block holds a fixed-size summary rather than its members, total state is logarithmic too, and it stays that way forever.

The consequence for queries is precise and worth stating rather than glossing. Asked about a span, you take the smallest set of blocks covering it. That set may overshoot, because the oldest block it touches is only partly inside the span and cannot be split — but the overshoot is bounded by the size of that block, which is bounded by the span itself, so you never look at more than about twice what was asked. That is an error bound, not a hope, and it is a design parameter: a finer progression of block sizes shrinks the overshoot toward nothing at the cost of more blocks, so you choose the point on that curve rather than accepting whatever falls out.

The assumption the scheme depends on should be made explicit, because the whole structure is honest only if it holds. Using the overshoot as if it were the requested span presumes the extra material resembles the requested material — that the process is drifting rather than lurching. Under drift the answer is a good approximation; under abrupt change it is contaminated by exactly the stale period you were trying to exclude. So the bucketing parameter and the volatility of the source are coupled, and a system built this way should say what rate of change it assumes.

The generalisable idea is that resolution is a resource you can spend unevenly. Most questions about history are disproportionately about the recent past, and most systems nevertheless store history at uniform resolution and then either truncate it or drown in it. Geometric decay of resolution matches storage to the shape of demand, and it yields a system whose memory footprint does not grow with uptime — which is a much stronger property than a retention policy, because it needs no deletion, no compaction schedule, and no decision about what to discard.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the stream-clustering sections of the clustering chapter, which organise a sliding window into buckets whose sizes form a doubling sequence with a bounded number at each size, yielding logarithmically many buckets, and which note that covering a requested suffix may include up to twice as many points unless a finer bucketing scheme is used to tighten the factor.
