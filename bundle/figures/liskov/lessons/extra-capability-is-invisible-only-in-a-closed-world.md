---
type: lesson
title: "Extra capability is invisible only in a closed world"
figure: liskov
works: [a-behavioral-notion-of-subtyping]
axes: [verifiability, parallelizability, cognitive-load]
subdomains: [programming-languages-and-semantics, distributed-systems-and-concurrency, formal-methods-and-verification]
tags: [lesson]
---
# Extra capability is invisible only in a closed world

**Lesson:** The comfortable story about specialization is that added abilities cost nothing: a client that only knows the general type will never invoke the specialized extras, so whatever those extras do is that client's business to ignore. The story holds exactly as long as the object has one reference and one reasoner. Introduce a second name for the same object, or a second party who found it in a shared namespace, and the extras become fully observable to someone who never called them — because they change the object, and the change shows up the next time the first party looks. Nothing was called by that first party and yet its conclusions were falsified.

This is why reasoning about substitutability has to be conducted in the pessimistic setting rather than the tidy one. The tidy setting assumes each object is reached by one path, examined by one program, in one uninterrupted stretch of time. Real object universes are the opposite: objects outlive the code that created them, several parties reach them concurrently or at unrelated moments, and a specialized capability installed by one party is a mutation source for every other. Under those conditions the properties worth protecting are not merely per-call agreements about what a single operation does, but agreements across the whole sequence of an object's states — what can never change, and what can only change in one direction. Those are the promises an unseen extra capability quietly breaks.

Two ways out are both instructive. One states the across-time promises explicitly in the description, so a specialization must show its own promises imply the general one's, and the extras are constrained just by having to fit. The other demands that every added capability be accounted for as something achievable by composing the abilities the general type already published; if it can be so explained, it introduces no surprise, because whatever state it reaches was reachable anyway. Both amount to the same insight: an addition is safe only when it is not really new in what it can do to the object, merely new in how conveniently it does it.

A programmer who believes this stops treating "the base-type client won't call it" as a defense of an added mutator, and starts asking what across-time property that mutator destroys for anyone else holding the object. The design habit that follows is to write down the invariants and the permitted directions of change as part of the type's public meaning, not as folklore in the implementation, because that is precisely the material a shared, aliased, long-lived object universe puts at risk.

**Source:** [A Behavioral Notion of Subtyping](../works/a-behavioral-notion-of-subtyping.md) — the motivation section's treatment of aliasing and of objects shared through a persistent object store, and the two mechanisms it develops for constraining methods that a supertype never declared.
