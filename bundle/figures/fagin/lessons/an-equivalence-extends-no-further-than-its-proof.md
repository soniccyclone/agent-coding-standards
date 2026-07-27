---
type: lesson
title: "An equivalence extends no further than its proof, so attack the obvious next step"
figure: fagin
works: [functional-dependencies-in-a-relational-database-and-propositional-logic, multivalued-dependencies-and-a-new-normal-form-for-relational-databases]
axes: [verifiability]
subdomains: [formal-methods-and-verification, foundations-of-computation, databases-and-data-management]
tags: [lesson]
---
# An equivalence extends no further than its proof, so attack the obvious next step

**Lesson:** Having established that dependency entailment and logical entailment coincide, the natural next question is whether the correspondence survives one small generalization: instead of asking whether a single statement follows, ask whether at least one of two statements must follow. Fagin shows this fails, with a three-record counterexample small enough to check by eye. In the logical world, a disjunction can be forced without either branch being forced, because a truth assignment must fall on one side or the other. In the data world it cannot, and the reason is structural rather than incidental: there exists a single structure exhibiting exactly the entailed dependencies and no others, so if a disjunction is entailed, that structure settles which branch. The two domains agree on individual statements and diverge on disjunctions of them.

The same shape recurs in his work on the more general dependency, where dropping a technical disjointness restriction, an apparently harmless tidying-up, destroys transitivity. In both cases the generalization looked so mild that few people would have bothered to check it, and Fagin says as much: those who find the original result obvious will find the extension only slightly less obvious, and it is false.

The operating rule this suggests is to treat every proved equivalence as having a boundary and to go looking for it immediately, before anyone builds on the result. A correspondence is a contract about specific claims; extrapolating past the contract is how a correct theorem becomes an incorrect assumption three papers later. The productive way to find the boundary is to take the smallest step past what was proved and try hard to break it, because the failures cluster right at the edge, where they are least expected and least often tested. Programmers meet this constantly with laws that hold for single operations and fail for compositions, or that hold for one element and fail for collections, and the reliable defence is to prove or refute each extension rather than let it inherit credibility from its neighbour.

**Source:** [Functional Dependencies in a Relational Database and Propositional Logic](../works/functional-dependencies-in-a-relational-database-and-propositional-logic.md) — the section presenting a counterexample to the disjunctive extension of the equivalence theorem, and the pair of contrasting theorems about when a disjunction can be entailed without either branch being. Also [Multivalued Dependencies and a New Normal Form](../works/multivalued-dependencies-and-a-new-normal-form-for-relational-databases.md), whose section on relaxing the disjointness requirement shows transitivity failing under the modified definition.
