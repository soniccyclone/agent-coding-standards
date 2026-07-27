---
type: lesson
title: "Insist that a correctness property hold object by object, or you have bought a global scheduler without noticing"
figure: herlihy
works: [linearizability-a-correctness-condition-for-concurrent-objects]
axes: [verifiability, parallelizability, cognitive-load]
subdomains: [distributed-systems-and-concurrency, formal-methods-and-verification, software-engineering-and-architecture]
tags: [lesson]
---

# Insist that a correctness property hold object by object, or you have bought a global scheduler without noticing

**Lesson:** Composability of a correctness property is not a nice-to-have, it is the property that decides whether a system can be built by independent parts. A property is local when a system satisfies it precisely because each of its components does — no cross-component conditions, no extra proof at the seams. Locality is not automatic and it is not implied by any of the obvious virtues: two well-known consistency notions each admit systems whose every individual object is correct in isolation while the system as a whole is not, and one of them permits a two-object counterexample in which each participant retrieves an item the other inserted, which no sequential run could produce.

The consequences of choosing a non-local property are structural rather than theoretical. If correctness of the whole does not follow from correctness of the parts, then something must coordinate the parts: either a scheduler that sees all objects at once, or a project-wide convention that every object's concurrency-control mechanism be compatible with every other's. The first is a centralization that kills the scalability the concurrency was for; the second is a standing tax on every future implementation choice, and it is easy to violate, since well-known mechanisms are pairwise incompatible in exactly this way. Locality, by contrast, means each object can be implemented, verified, tuned, and replaced by whoever owns it, and scheduling can be entirely decentralized because no one needs a global view.

The habit to take away is to add one question to any evaluation of a consistency model, isolation level, memory model, or module contract: does this compose, and if not, what is the side condition, and who is going to enforce it? Notice also which design decision bought locality here. The condition was deliberately scoped so that the unit of atomicity is a single operation on a single object; the moment atomicity spans multiple objects, locality is gone. That is the real content of the trade between a per-object condition and a transactional one, and it tells you where each belongs: transactions when application invariants genuinely span objects, per-object conditions when concurrency and independent evolution matter more. The scope of atomicity is the scope of the coordination you will have to pay for.

**Source:** [Linearizability: A Correctness Condition for Concurrent Objects](../works/linearizability-a-correctness-condition-for-concurrent-objects.md) — the locality theorem and its proof by contradiction on cycles in the union of per-object orders, the two-queue history showing that sequential consistency and strict serializability are not local, and the discussion of global conventions and incompatible concurrency-control mechanisms.
