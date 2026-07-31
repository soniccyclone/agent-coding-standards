---
type: lesson
title: "The properties you can compute from an artifact are not the ones that matter about it"
figure: ullman
works: [mining-of-massive-datasets]
axes: [expressiveness, cognitive-load]
subdomains: [databases-and-data-management, software-engineering-and-architecture]
tags: [lesson]
---
# The properties you can compute from an artifact are not the ones that matter about it

**Lesson:** Given an artifact in a machine-readable encoding, it is always possible to compute statistics over the encoding, and it is tempting to treat those statistics as its description because they are cheap, objective, and available. They are usually descriptions of the encoding rather than of the artifact. Nobody chooses among pictures by their average colour. The attributes people actually discriminate on — what the thing is about, where it was taken, what it is for — are not recoverable from the representation by any straightforward measurement, and building on the measurable ones produces a system that works flawlessly on a dimension nobody cares about.

Once that is admitted, the useful question becomes where the meaningful attributes can come from, and there are only three answers. They may already exist as separate structured records maintained for other reasons, in which case the work is acquisition and joining, not analysis. They may be extractable from the artifact by a procedure that reconstructs something semantic rather than superficial — picking out the terms whose presence is disproportionate rather than merely frequent, for instance, so the description reflects what distinguishes this item rather than what all items share. Or they may only be obtainable from people, which turns a computation problem into a participation problem with an entirely different cost structure and failure mode.

The third path has properties worth knowing before choosing it. Human-supplied descriptions arrive only if enough people are motivated to supply them, and the motivation has to come from somewhere — a use they already wanted, or a mechanism that makes the supplying itself worthwhile. They are individually unreliable, so the design must depend on volume, with enough independent contributions per item that mistakes and mischief are outvoted rather than believed. That means coverage is inherently uneven: popular items are richly described and everything else is bare, which is the opposite of the distribution you need if the point of the system is to surface obscure items.

The general instruction is to separate the question "what can I compute about this object" from "what do people distinguish these objects by," answer the second one first from the domain, and only then ask which of the three acquisition paths can supply it. Skipping straight to what is computable is how systems end up with a mathematically impeccable notion of similarity that no user recognises.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the content-based sections of the recommendation-systems chapter, which contrast readily available structured attributes with document features derived by scoring terms for disproportionate occurrence, and then treat images as the case where pixel statistics reveal nothing anyone selects on, so descriptions must be solicited from users — with the caveat that this only works when enough people bother and enough tags accumulate to dilute the wrong ones.
