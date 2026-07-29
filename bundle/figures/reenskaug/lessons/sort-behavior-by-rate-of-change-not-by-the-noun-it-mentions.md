---
type: lesson
title: "Sort behavior by what it drags in, not by the noun it mentions"
figure: reenskaug
works: [the-dci-architecture-a-new-vision-of-object-oriented-programming]
axes: [cognitive-load, primitive-count]
subdomains: [software-engineering-and-architecture, programming-environments-and-object-systems]
tags: [lesson]
---
# Sort behavior by what it drags in, not by the noun it mentions

Two operations can both be about the same entity and still belong to entirely different strata of a system. Reenskaug and Coplien work the distinction on a deliberately mundane pair: adjusting a balance versus performing a withdrawal. The first is constitutive — an account that cannot do it is not an account, and the operation needs nothing beyond the entity's own data. The second sounds equally like an account operation and in fact drags in atomicity, failure handling, an audit obligation, a person at a screen, and rules that come from outside the entity entirely. Grouping them because they share a grammatical subject is a category error that no naming convention will fix.

The workable test is what an operation pulls into scope. If implementing it requires knowledge of processes, participants, and policies that live beyond the entity, the operation is about the system's purpose rather than the entity's nature, and housing it inside the entity imports all of that knowledge across a boundary that existed to keep it out. The two strata also move at different speeds: notions of the domain's essential entities are comparatively durable, while the operations people want to perform grow and mutate for as long as the software is in service. Mixing strata therefore guarantees that the durable code is edited constantly for reasons that have nothing to do with it.

There is a corollary that reads as heresy against a decade of object advice: the entities should be kept deliberately unintelligent. Resisting the urge to make them capable is not laziness but boundary maintenance, and the usual argument against it — that a rich interface designed carefully up front will not need to change — fails on arithmetic, since whatever operations you know about at the start are a small fraction of those the system will accumulate.

A programmer holding this asks of every method not "is this about X?" but "what does this need to know?" — and moves anything whose answer reaches past the entity into a construct that is allowed to know those things. The stable core stays small and boring by design, which is what lets it stay stable.

**Source:** [The DCI Architecture: A New Vision of Object-Oriented Programming](../works/the-dci-architecture-a-new-vision-of-object-oriented-programming.md) — the data section's contrast between two operations on a savings account, and the argument that follows about separating stable structure from changing behavior and keeping domain classes deliberately dumb.
