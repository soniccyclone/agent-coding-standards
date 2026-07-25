---
type: lesson
title: "Whether a thing can be shared is decided entirely by whether it remembers its context"
figure: gang-of-four
works: [design-patterns-abstraction-and-reuse-of-object-oriented-design]
axes: [parallelizability, hardware-affinity]
subdomains: [software-engineering-and-architecture, distributed-systems-and-concurrency]
tags: [lesson]
---
# Whether a thing can be shared is decided entirely by whether it remembers its context

**Lesson:** Two places in this catalog make the same structural claim from different directions, and together they identify a single property as the gatekeeper of sharing. The fine-grained-sharing pattern states the condition outright: an object may be shared among many users only if it holds no state that depends on the particular use. Anything it needs about the caller's situation has to arrive as an argument at the moment of the call rather than living inside it. The behavior-as-object pattern arrives at the same rule as implementation advice — such an object should not carry state between invocations, precisely so that one instance can serve many contexts. Neither passage is really about sharing as an optimization. Both are identifying context-dependence as the thing that makes an instance non-replicable, and its absence as the thing that makes replication free.

Why this generalizes past the two patterns: state that encodes context is what creates a private relationship between an object and one user, and a private relationship is exactly what prevents a second user from safely holding the same reference. Push that state out to the call site and the object stops having a relationship with anyone. Then one instance can serve arbitrarily many callers, and — the part that matters beyond memory footprint — those callers do not need to coordinate with each other, because there is nothing in the shared object for them to race over. Independent execution stops being something you engineer with locks and becomes a property that follows from the shape of the thing. The same reasoning is why the paper can note that sharing makes consistency automatic: there is one copy, so there is no synchronization problem to have.

The physical side is not incidental either. The authors reach this design because programs that create objects in enormous quantities must account for the per-object cost, and sharing rather than duplicating is what makes fine-grained objects affordable at all. That is a hardware-level argument about how much memory the representation actually occupies and how much of it stays resident, and it is the reason the abstraction level a designer wants and the granularity a machine can afford can be reconciled instead of traded off.

A programmer who has absorbed this reads every field on an object as a question — is this intrinsic to what the object is, or is it a memory of who last used it? Fields of the second kind are the ones that force per-user copies, block safe concurrent use, and multiply memory. Moving them outward is a single structural change that improves footprint, contention, and reasoning at once, which is why "make this stateless" is so often the highest-leverage move available.

**Source:** [Design Patterns: Abstraction and Reuse of Object-Oriented Design](../works/design-patterns-abstraction-and-reuse-of-object-oriented-design.md) — the structural-object discussion of fine-grained object sharing and its stated precondition, alongside the implementation note in the Strategy entry on avoiding retained state across calls.
