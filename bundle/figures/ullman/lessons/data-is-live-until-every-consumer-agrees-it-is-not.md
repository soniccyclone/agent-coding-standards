---
type: lesson
title: "Data is live until every consumer agrees it is not"
figure: ullman
works: [mining-of-massive-datasets]
axes: [verifiability, cognitive-load, primitive-count]
subdomains: [databases-and-data-management, distributed-systems-and-concurrency]
tags: [lesson]
---
# Data is live until every consumer agrees it is not

**Lesson:** Working out what a computation no longer needs is easy and misleading. A rolling average over the last twenty-four readings plainly has no further use for the twenty-fifth, and the reasoning that establishes this is entirely local to that one computation. The conclusion it licenses is not. Whether the twenty-fifth reading can actually be released depends on every other consumer registered against the same input, and none of them appear anywhere in the reasoning that produced the answer. Discarding is a global decision derived from local evidence, which is exactly the shape of decision that goes wrong when a system grows.

So the discard rule has to live at a layer that can see the whole consumer set, and it has to be derived rather than written down. The derivation is a maximum over the requirements each consumer declares — the longest lookback anyone needs — which means adding a consumer silently changes what may be deleted, and removing one changes it back. Neither event is naturally routed to whoever wrote the eviction code. The engineering move is to make each consumer state its requirement as data, so the retention bound is computed from the current set rather than embedded as a constant that was true when someone last checked. This is the same structure as reference counting: liveness is reachability from the full set of roots, and any scheme that reasons from one root is unsound by construction.

There is a sharper corollary for systems that accept questions they have not seen yet. If arbitrary future queries are permitted, the consumer set is unbounded and the maximum is undefined, so nothing can be safely discarded at all. The only honest resolutions are to bound the questions — publish a window and answer only within it — or to bound the answers, keeping summaries chosen in advance and declining anything outside them. Both are restrictions on the interface, arrived at from a storage argument, which is the useful direction of inference: what you can afford to forget determines what you are permitted to promise, not the other way round.

The failure this prevents is quiet and specific. Someone adds a feature that needs slightly more history than the current retention supports, the data is already gone, and the feature works fine in testing because the test data is fresh. The general habit is to treat any deletion, truncation, downsampling, or column drop as a claim about a set of consumers, and to write the claim down where the set can be checked. A deletion justified by one reader's needs is a deletion justified by nothing.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — chapter 4's discussion of standing queries, where the observation that a reading falling out of a twenty-four-element average will never be needed again is immediately qualified by the parenthetical that some other standing query may still require it.
