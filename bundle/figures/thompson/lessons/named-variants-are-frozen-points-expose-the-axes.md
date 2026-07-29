---
type: lesson
title: "Named variants are frozen points in a space; expose the axes instead"
figure: thompson
works: [plan-9-from-bell-labs]
axes: [primitive-count, expressiveness, parallelizability, cognitive-load]
subdomains: [operating-systems-and-systems-programming, distributed-systems-and-concurrency]
tags: [lesson]
---
# Named variants are frozen points in a space; expose the axes instead

When a system needs entities that differ in how much they share, the reflex is to name the useful combinations: a heavyweight kind that shares nothing and a lightweight kind that shares almost everything. Plan 9 declines to do this. It offers one kind of process and one creation call whose argument enumerates, independently, which pieces of the parent's context the child copies, shares, or gets fresh — memory, open files, the naming context, the signal environment. The named variants everyone else ships are recovered as particular settings of those switches, and so are dozens of combinations nobody would have thought to name.

The reason this beats a menu of kinds is that the menu is a claim about which points in the space matter, made before anyone has used the system. That claim is almost always wrong, and it is wrong in a way that cannot be corrected from outside: a caller who wants shared memory but a private naming context has no vocabulary to ask for it, and no amount of library code above the primitive can synthesize a sharing arrangement the primitive cannot express. Factoring into orthogonal switches costs one argument and moves the choice from the designer to the caller, permanently.

The authors also hand over the empirical test for whether a factoring was right, which is more useful than the design advice. Look at the actual call sites. If every caller passes the same combination, the axes you separated were not really independent and you have imposed ceremony for nothing. If it is hard to find two call sites that agree — which is what they report — then the space you exposed is a space people were genuinely spread across, and any fixed menu of kinds would have been serving most of them badly. Variety in observed usage is evidence about the decomposition, not noise to be tidied away behind convenience wrappers.

There is a second move in the same primitive worth stealing: one of the switches controls whether a new entity is created at all, so "make a child that differs from me in these ways" and "change these things about myself" become one operation rather than two. Asking what your operation does when the quantity it varies goes to zero often reveals that a separate operation you already have is the degenerate case of this one.

A programmer who believes this stops enumerating modes. Faced with a request for a second flavor of an existing thing, they ask what dimension the two flavors differ along, expose that dimension, and let the flavors be values — then check the call sites later to see whether the dimension was real.

**Source:** [Plan 9 from Bell Labs](../works/plan-9-from-bell-labs.md) — the parallel programming section, where the paper rejects the two-class process-and-thread split in favor of a single process kind with a resource-sharing bit vector, and cites the diversity of observed call sites as evidence the model is right.
