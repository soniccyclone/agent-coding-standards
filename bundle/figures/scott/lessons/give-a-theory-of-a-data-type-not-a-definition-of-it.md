---
type: lesson
title: "State what a data type must satisfy instead of defining it as one representation"
figure: scott
works: [a-type-theoretical-alternative-to-iswim-cuch-owhy]
axes: [expressiveness, hardware-affinity, verifiability, cognitive-load]
subdomains: [programming-languages-and-semantics, software-engineering-and-architecture, foundations-of-computation]
tags: [lesson]
---
# State what a data type must satisfy instead of defining it as one representation

**Lesson:** There are two ways to introduce a kind of data into a theory or a system. You can define it — pick a construction out of whatever primitives you already have and declare that the numbers, or the lists, *are* that construction. Or you can give a theory of it — take it as primitive, name its operations, and write down the conditions those operations satisfy, saying nothing about what the values are made of. The second is the one to reach for. Its payoff is that every theorem you prove holds for all representations meeting the conditions, so results are independent of the machine, the encoding, and the choices of whoever implements it. Defining instead forces an arbitrary commitment and then quietly lets consequences of that arbitrary choice leak into everything downstream, where nothing distinguishes them from real consequences.

The reduction-to-definitions habit comes from a foundational instinct — fewer primitives is better, so build everything out of what you already have. That instinct is worth suspecting here, because the reductions tend not to be free. Reducing number to set requires postulating an infinite set to get enough numbers, so the primitive you were avoiding reappears in another costume; reducing function to set is available but so inconvenient that treating sets as a species of function is the better trade. When the reduction merely relocates the assumption, the economy was illusory, and you have paid a representation commitment for nothing.

For working systems this changes where the obligation sits. Under the axiomatic reading, an implementation of a data type owes you a demonstration that its structure satisfies the stated conditions, and that demonstration is a bounded, checkable task; in exchange the implementation is free in every respect the conditions do not mention, which is what allows the representation to be chosen for the machine rather than for the theory. The one place this needs care is where the physical realization cannot satisfy the conditions at all: a finite representation of an unbounded type will fail some axiom at its boundary, and overflow is exactly that failure. Deciding what the axioms say about that boundary is part of the job, not a detail to be discovered later.

**Source:** [A Type-Theoretical Alternative to ISWIM, CUCH, OWHY](../works/a-type-theoretical-alternative-to-iswim-cuch-owhy.md) — Section 1's argument for keeping data types as primitives with a stated structure so that theorems remain machine-independent across representations, its critique of Russell's program of defining number and of the infinite-set postulate needed to rescue it, its preference for Church's functions-over-sets treatment, and the conclusions section, which extends the same axiomatic-over-definitional stance to lists and stores and flags the open question of what to do about overflow.
