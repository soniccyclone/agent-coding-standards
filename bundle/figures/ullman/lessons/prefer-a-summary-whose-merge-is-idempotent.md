---
type: lesson
title: "Prefer a summary whose merge is idempotent"
figure: ullman
works: [mining-of-massive-datasets]
axes: [parallelizability, verifiability]
subdomains: [distributed-systems-and-concurrency, algorithms-and-complexity]
tags: [lesson]
---
# Prefer a summary whose merge is idempotent

**Lesson:** Counting distinct things is expensive for one reason: you must remember what you have already seen in order to tell whether the next item is new. Everything about that requirement is bad at scale — the memory grows with the answer, the check is a lookup against shared state, and the order in which contributions arrive determines what gets counted. But the requirement is not intrinsic to the question; it is intrinsic to counting by incrementing. If you replace the counter with a summary whose merge operation is idempotent — combining a value with itself leaves it unchanged, so absorbing the same contribution twice is the same as absorbing it once — the entire problem evaporates. There is no need to know whether you have seen something before, because seeing it again does nothing.

The properties this unlocks are worth listing because they are what people usually try to build with locks and bookkeeping. Contributions can be applied in any order and the result is the same, so a computation can stream its input from wherever it happens to be, in whatever order the storage layer prefers, and never revisit it. Partial results from independent workers combine by the same operation that absorbs a single contribution, so there is one code path and no separate reduction logic. Retries and replays are free, since re-applying a contribution cannot corrupt anything — which means failure recovery needs no exactly-once machinery. And propagating a summary through a structure becomes a matter of repeatedly taking the merge of neighbours until nothing changes, with the fixpoint independent of the schedule.

The cost is that idempotent summaries are generally approximate, and the approximation lives in a specific place. A single such summary is noisy; the usual remedy is to keep many independent ones and combine their estimates with a rule chosen to suppress outliers rather than average them. That is a real accuracy loss, and the trade is stated plainly: you give up exactness and gain order-independence, mergeability, bounded memory, and replay safety. For a question asked over a population too large to enumerate, that is almost always the right side of the trade, and the space saving is dramatic — a handful of bytes per entity where the exact answer needed a set.

The general prompt is to ask, of any aggregate you are maintaining, what its combining operation is and whether applying the same input twice is harmless. If it is not, you have implicitly signed up for deduplication, ordering guarantees, and exactly-once delivery somewhere in the system. Choosing a different summary is often much cheaper than building those.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the approximate-neighbourhood-function section of the social-network chapter, which stores per-node maximum hash tail lengths in place of the reachable sets themselves, grows the radius by taking the larger of a node's value and its successors', explicitly observes that it does not matter whether a node is reached through one successor or many, notes that arcs may therefore be processed in any order and streamed from disk one block at a time, and combines many hash functions by averaging within groups and taking the median.
