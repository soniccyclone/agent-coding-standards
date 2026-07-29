---
type: lesson
title: "Escalate mechanism on measured failure, not on its possibility"
figure: stonebraker
works: [the-end-of-an-architectural-era]
axes: [parallelizability, verifiability, cognitive-load]
subdomains: [distributed-systems-and-concurrency, databases-and-data-management, software-engineering-and-architecture]
tags: [lesson]
---
# Escalate mechanism on measured failure, not on its possibility

There is a habitual conflation between something being possible and something being frequent, and it is expensive. A conflict between two concurrent operations is possible in almost any system; that possibility is what motivates a protective mechanism, and the mechanism then runs on every operation regardless of how often the bad case actually occurs. The cost structure is inverted: the rare event dictates the price of the common one.

The alternative is to arrange the system as a ladder of increasingly defensive strategies, each of which is correct, and to let an observed statistic decide which rung you stand on. Begin at the rung that assumes nothing goes wrong. Watch the rate at which reality contradicts that assumption. When the rate crosses a threshold, move up to a strategy that spends more — a small delay to order arrivals, then full bookkeeping of what each operation read and wrote — and move back down when the pressure subsides. Nothing about this weakens the guarantee; every rung produces the same outcomes. What varies is only how much work is done to obtain them.

Two conditions make this work, and both deserve to be checked rather than assumed. The first is that the failure being counted must be cheap to absorb: if the optimistic rung's failure mode is a retry, escalation is a performance decision, but if its failure mode is corruption, there is no ladder, only a bug. The second is that the frequency must genuinely be low, and low for a structural reason rather than by luck. Notice that contention in a well-built application is usually low because its authors already went and removed the contention — the statistic is low because someone made it low, which is exactly why designing for the common case is defensible rather than reckless.

Someone who internalizes this stops asking "can this go wrong?" as the sole input to a design and starts asking "how often, and what does it cost me when it does, versus what does the guard cost me when it doesn't?" They instrument the bad case before building elaborate machinery to prevent it, and they accept the real price of the approach: more modes in the system, a transition policy to get wrong, and behavior under load that is harder to predict than a system that always pays the same toll.

**Source:** [The End of an Architectural Era (It's Time for a Complete Rewrite)](../works/the-end-of-an-architectural-era.md) — the transaction-management section, where a monitor watching the abort rate promotes the engine from running with no controls, to inserting a bounded delay for ordering, to full optimistic read/write-set tracking.
