---
type: lesson
title: "When the queries outlive the data, index the queries instead"
figure: ullman
works: [mining-of-massive-datasets]
axes: [expressiveness, parallelizability, hardware-affinity]
subdomains: [databases-and-data-management, distributed-systems-and-concurrency]
tags: [lesson]
---
# When the queries outlive the data, index the queries instead

**Lesson:** The default architecture of retrieval is that data is durable and questions are ephemeral: you accumulate a corpus, build an index over it, and each arriving question is answered by consulting that index. A whole family of problems inverts the lifetimes. The questions are the long-lived objects — standing interests, alert subscriptions, bids on terms, filters someone registered months ago — while the data streams past and is gone. Applying the default architecture there produces the worst of both worlds: you store everything so the standing questions can be re-run, and you re-run all of them periodically anyway, paying repeatedly for answers that were mostly unchanged.

The inversion is to build the index over the questions and stream the data through it. Each arriving item is decomposed into its features, and those features are looked up against a structure keyed by what the registered questions are waiting for; the item's cost is then proportional to the questions it actually touches rather than to how many exist. This scales in the direction that matters, because the population of questions grows into the hundreds of millions while any single item is small, and it removes the need to retain the data at all once it has been passed by. It also changes what "adding a query" means operationally: registration becomes a write into a live index rather than a new job on a schedule.

The representation that makes this work is worth extracting on its own. A question that requires several conditions to hold simultaneously becomes a small state machine: it sits in a table keyed by the next condition it is waiting for, and each time an arriving item satisfies that condition the question advances and is re-filed under the following one. Completed questions fall out as matches. The elegance is that no question is ever fully evaluated against an item that will not match it — a question that never clears its first condition costs one failed lookup.

The remaining design freedom is the order of the conditions, and the right choice is the most selective first. Ordering the conditions so that the rarest gates entry means very few questions are ever promoted into the partially-satisfied state, which keeps that working set small enough to stay resident and cuts the work at every subsequent step. Ordering by anything convenient instead — alphabetical, insertion order, whatever the schema suggests — admits enormous numbers of questions into partial progress that will die a step later. The lesson generalises to any conjunctive filter evaluated at volume: put the discriminating test where it can prevent work, not where it reads well.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the implementation sections of the advertising chapter, on matching very large numbers of word-set bids against arriving documents, including the pair of hash tables holding untouched and partially matched bids keyed on the next needed word, and the argument for ordering the words of both bids and documents rarest-first to keep the partial table small.
