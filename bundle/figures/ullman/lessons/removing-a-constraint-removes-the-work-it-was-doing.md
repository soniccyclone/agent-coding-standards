---
type: lesson
title: "Removing a constraint removes the work the constraint was silently doing"
figure: ullman
works: [mining-of-massive-datasets]
axes: [cognitive-load, expressiveness]
subdomains: [software-engineering-and-architecture, databases-and-data-management]
tags: [lesson]
---
# Removing a constraint removes the work the constraint was silently doing

**Lesson:** A limit on capacity forces a selection, and the selection is usually performed by some mechanism nobody thinks of as a component of the system, because it never had to be built — it was implied by the shortage. When the shortage disappears, the selection disappears with it, and the resulting system is not the old system plus more options. It is the old system with a function removed, and the function has to be rebuilt, deliberately, from nothing. Teams that lift a constraint and expect strict improvement are routinely blindsided by this, because the missing capability has no name, no owner, and no line in the design that says it was ever there.

The shape recurs. A shortage of display space forced a ranking by aggregate popularity, and the ranking was free. Remove the shortage and everything is available, which means nothing is presented, which means the vast majority of the inventory is unreachable in practice — not because it is hidden but because nobody knows it exists to ask for. Worse, the selection that the shortage used to perform was crude but adequate for its purpose, so its replacement must be substantially better than crude to be worth the change: the abundant system with no curation is genuinely worse than the scarce system with popularity ordering.

There is a compensating opportunity, and it is the reason the trade is usually still worth making. The mechanism implied by a shortage is necessarily one-size-fits-all — a shared resource has to be allocated by aggregate criteria, since it cannot be arranged differently for each requester. Its deliberate replacement is under no such obligation. Once you are building the selection anyway, it can be per-requester, and a per-requester selection over the whole inventory can reach things the aggregate ranking would never have surfaced for anyone. The economics of the change come entirely from that: the value is not in offering more, it is in offering different things to different people, which was structurally impossible before.

Generalise the question rather than the example. Whenever a limit is about to be relaxed — memory, latency budget, schema rigidity, review capacity, a rate limit, a headcount cap — ask what decisions that limit was making on your behalf, who will make them afterwards, and whether the replacement is being funded. The limit was load-bearing and nobody documented it.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the long-tail section of the recommendation-systems chapter, which contrasts physical outlets whose shelf space forces them to stock only aggregate favourites against on-line ones that can carry everything, and argues that carrying everything is precisely what forces the on-line outlet to recommend to individuals, since users cannot be shown all items and cannot be expected to have heard of the ones they would like.
