---
type: lesson
title: "Design into the shape where local checks certify global properties"
figure: fagin
works: [on-the-desirability-of-acyclic-database-schemes]
axes: [verifiability, cognitive-load, parallelizability]
subdomains: [algorithms-and-complexity, databases-and-data-management, distributed-systems-and-concurrency]
tags: [lesson]
---
# Design into the shape where local checks certify global properties

**Lesson:** Deciding whether a collection of tables can all be slices of one consistent whole is NP-complete in general. Checking that each pair of them agrees on the columns they share is trivial. Pairwise agreement obviously follows from global coherence, and just as obviously does not imply it: the paper's three-table example, each pair matching perfectly while no single whole reproduces them, is the smallest possible demonstration. The interesting content is that this gap closes exactly when the schema has a particular shape, and closes for every possible data set over such a schema. Under that shape the cheap local check is not an approximation of the expensive global one. It is the same check.

That reframes what a structural restriction is for. The reflex on meeting an intractable problem is to look for a heuristic, or a good-enough approximation, or an amortized trick. The move here is to look instead for the class of inputs on which a local, decomposable test is provably equivalent to the global property, and then to arrange your design to live in that class. The authors are explicit that this is advice and not just theory: designers should know about the property and aim for it, and they report a conjecture that the well-behaved shape covers most situations that arise in practice anyway. Restricting the design space costs less than the general-case complexity does.

Local-to-global equivalence also happens to be what makes distributed operation cheap, which is not a coincidence. A test that decomposes into independent pairwise checks needs no global coordination, and the same structural condition guarantees the existence of a pruning program that reaches a coherent state by exchanging only projections between sites. When a global invariant can be certified by checks that touch two components at a time, verification, parallelism, and communication cost all improve together, because they were all being blocked by the same thing.

The transferable habit is to treat "the general case is expensive" as an unfinished sentence. The useful next question is which restriction on the shape of the input makes a local test sufficient, whether real designs can be pushed into that shape, and what the restriction costs in expressiveness. Programmers hit this constantly and usually answer it by accident: acyclic dependency graphs, tree-shaped ownership, partitioned keys, and hierarchies without back-edges are all instances of buying a cheap global guarantee by giving up structural freedom nobody was using.

**Source:** [On the Desirability of Acyclic Database Schemes](../works/on-the-desirability-of-acyclic-database-schemes.md) — the condition equating pairwise with global consistency, the three-table counterexample showing they differ in general, the noted NP-completeness of the unrestricted problem, and the introduction's argument that designers should aim for the well-behaved class.
