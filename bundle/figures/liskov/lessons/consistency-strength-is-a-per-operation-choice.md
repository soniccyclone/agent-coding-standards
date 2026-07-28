---
type: lesson
title: "Consistency strength belongs to the operation, not to the system"
figure: liskov
works: [providing-high-availability-using-lazy-replication]
axes: [parallelizability, expressiveness, verifiability]
subdomains: [distributed-systems-and-concurrency, databases-and-data-management, software-engineering-and-architecture]
tags: [lesson]
---
# Consistency strength belongs to the operation, not to the system

**Lesson:** Ordering guarantees are normally chosen once, for a whole service, and the choice is made by whichever operation has the strictest requirement. One rare administrative action that truly must be globally ordered thereby imposes global ordering on the millions of ordinary actions that did not need it. Every one of them pays coordination cost forever to protect an invariant that concerns a handful of them. Stated that way it is obviously the wrong trade, but it is the default trade, because the guarantee is usually a property of the infrastructure rather than a property of each request.

The alternative is to expose a small set of ordering strengths and require each operation to declare which one it needs, then charge each operation only for what it declared. The strengths form a ladder: at the bottom, respect only the dependencies the caller actually has; in the middle, agree on a common order among a designated subset of operations while still allowing them to interleave with the cheap ones differently at different sites; at the top, an order relative to everything, taking effect before the caller resumes. The message and latency cost climbs steeply up the ladder, which is exactly why the classification matters — and why the design is only a win when the top rungs are used rarely.

The subtler benefit is that the ladder is a design vocabulary, not just a performance knob. Being forced to state an operation's ordering requirement makes you articulate what invariant it protects, which is a question most systems never ask because the infrastructure answered it silently and expensively. The cheap end also turns out to be a superset rather than a weakening: a system in which everything is declared strongly ordered behaves like the conventional design, while still allowing reads to be served from behind and specifying exactly how far behind is acceptable — a knob the conventional design cannot offer at all.

A programmer who believes this stops asking "what consistency model does this system use" and starts asking, per operation, what would actually go wrong under a weaker order. They expect the answer to be "nothing" for the majority, and they expect the minority to be identifiable and specifically defensible. Systems built this way pay for strength where strength is needed and nowhere else, which is the only reason the rare strong operation is affordable at all.

**Source:** [Providing High Availability Using Lazy Replication](../works/providing-high-availability-using-lazy-replication.md) — the introduction and the section on additional operation types, which define three declared ordering categories, tally the message cost of each, and argue that the scheme degenerates to conventional replication if everything is declared strongly ordered.
