---
type: lesson
title: "A synchronization barrier can be what pays for batching"
figure: ullman
works: [mining-of-massive-datasets]
axes: [parallelizability, hardware-affinity, cognitive-load]
subdomains: [distributed-systems-and-concurrency, algorithms-and-complexity]
tags: [lesson]
---
# A synchronization barrier can be what pays for batching

**Lesson:** Barriers have a bad reputation, and the reasoning behind it is sound as far as it goes: a barrier forces every participant to wait for the slowest, so it converts a spread of finishing times into a shared cost and rules out overlap. That accounting is incomplete, because it only prices what the barrier prevents. What a barrier *enables* is knowing that a well-defined batch of outgoing work has accumulated and that nothing more will be added to it. Anything whose cost is per-invocation rather than per-byte — a network round trip, a syscall, a transaction, an API call with a rate limit — becomes dramatically cheaper once you can amortise it over a batch, and the barrier is what makes the batch a definite object rather than a guess about how long to wait.

The situation where this matters is easy to recognise once you look for it: an algorithm that is entirely correct and entirely reasonable in operation count, but which emits one small message per discovered fact. Nobody has made a complexity error. The problem is that the analysis counted facts and the machine charges per send, and at scale a per-send constant of even a fraction of a millisecond makes the algorithm unimplementable rather than slow. The repair is not to discover fewer facts. It is to restructure the computation into rounds in which every participant does its local work, and only then does the system collect all the pending communications between each pair of participants and ship them as one.

The general habit is to ask, of any cost you are about to incur, whether it scales with the amount of data or with the number of times you touch the boundary. If it is the latter, the design question stops being "how do I make each call faster" and becomes "what is the largest well-defined group of calls I can accumulate before crossing, and what tells me the group is complete." Very often the honest answer to the second half is a barrier — and paying the barrier's straggler cost to collapse a million crossings into a few thousand is not a compromise, it is the point. The corollary is that in this style, the round is the unit of everything: it is also where you place progress reporting, checkpoints, and termination checks, because it is the only moment the system has a consistent global picture.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the chapter on cluster programming systems, in its treatment of bulk-synchronous graph processing, where computation is organised into supersteps specifically so that all messages passing between two managing tasks can be bundled into one transmission, and the accompanying observation that sending each newly discovered shortest-path fact individually would be unrealistic on a large graph.
