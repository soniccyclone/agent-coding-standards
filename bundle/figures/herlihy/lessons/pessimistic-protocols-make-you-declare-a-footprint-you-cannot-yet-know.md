---
type: lesson
title: "Pessimistic protocols make you declare a footprint you do not yet know, and the concurrency you lose is the state-dependent kind"
figure: herlihy
works: [transactional-memory-architectural-support-for-lock-free-data-structures]
axes: [parallelizability, expressiveness, cognitive-load]
subdomains: [distributed-systems-and-concurrency, operating-systems-and-systems-programming]
tags: [lesson]
---

# Pessimistic protocols make you declare a footprint you do not yet know, and the concurrency you lose is the state-dependent kind

**Lesson:** Reserving resources before touching them has a structural requirement that gets overlooked: you must know what you are going to touch before you have computed it. Whenever the set of locations an operation modifies depends on values it has yet to read, the requirement is unsatisfiable, and the programmer resolves it the only way available — by reserving a superset, usually the whole structure. That is where the parallelism goes. Consider a queue held by two end pointers where an operation at one end normally leaves the other alone, so opposite-end operations could in principle run simultaneously; but in the boundary case where the queue is empty, both ends must move together. Neither participant can tell which case it is in until it has read a pointer, and by then the pessimistic discipline has already required it to have decided. Reserving one end and then discovering you need the other in an order the opposite participant reverses is precisely the classic deadlock, so the workable version reserves everything and the available parallelism is thrown away in every state — to pay for one state that is rare.

Detecting conflict after the fact inverts the dependency. The operation reads, computes, and only then asks whether anything it depended on moved; the footprint it declares is the footprint it actually had, discovered rather than predicted. The concurrency you get is then a function of the runtime state instead of a static over-approximation of it, which means the common case runs at its true cost and only the genuinely conflicting case pays. This is not a marginal effect. The class of concurrency that pessimistic reservation cannot express at all is exactly the class in which the interaction between two operations depends on data, and that class contains most interesting shared structures: which nodes a tree rebalance touches, whether an insertion splits, whether an operation at one boundary interacts with the other.

What changes for a programmer who internalizes this is the diagnostic reflex when a structure fails to scale. The question stops being "is my locking too coarse?" and becomes "am I forced to name what I touch before I know it?" If yes, no amount of finer-grained reservation fixes it, because the granularity is not the problem — the ordering between deciding and knowing is. Either restructure so the footprint is computable in advance, or switch to a discipline that validates afterwards and retries. And note the cost side honestly: the optimistic version buys expressible state-dependent parallelism in exchange for wasted work when conflicts do occur, which is a good trade only when conflicts are the exception.

**Source:** [Transactional Memory: Architectural Support for Lock-Free Data Structures](../works/transactional-memory-architectural-support-for-lock-free-data-structures.md) — the doubly-linked-list benchmark's analysis of why enqueuers and dequeuers cannot lock their own end without risking deadlock on the empty-queue case, forcing a single coarse lock, alongside the introduction's remark that deadlock avoidance is awkward when the object set is not known in advance.
