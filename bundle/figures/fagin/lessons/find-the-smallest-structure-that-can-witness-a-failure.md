---
type: lesson
title: "Find the smallest structure that can witness a failure, and reason only there"
figure: fagin
works: [functional-dependencies-in-a-relational-database-and-propositional-logic]
axes: [verifiability, cognitive-load]
subdomains: [foundations-of-computation, formal-methods-and-verification, databases-and-data-management]
tags: [lesson]
---
# Find the smallest structure that can witness a failure, and reason only there

**Lesson:** A dependency of the classical kind is violated by a pair of records that agree in one place and disagree in another. Nothing else in the structure participates in the violation. Fagin turns that observation into a proof strategy: if a counterexample exists at all, then throwing away every record except the two that disagree leaves a counterexample. So the entire question can be settled inside structures with exactly two records. And a two-record structure is nothing more than a choice, for each column, of whether the two records agree there, which is to say it is a truth assignment. The semantic collapse and the logical correspondence turn out to be the same fact seen twice.

This is a move worth having in reach whenever you face reasoning over an unbounded space of states. Ask what the minimum evidence of failure looks like. If violations are always witnessed by a bounded fragment, then quantifying over all structures collapses to quantifying over structures of bounded size, and an infinite semantic question becomes a finite combinatorial one. The bound is what does the work, and it comes from the shape of the property rather than from cleverness about the search. Properties whose violations require arbitrarily large witnesses do not admit this collapse, and knowing which camp your property is in tells you whether exhaustive checking is even on the table.

Fagin also proves his main equivalence twice, once by showing a set of axioms is strong enough to derive every consequence and once by this minimal-witness route. The two proofs are not redundant. The first yields a proof system you can mechanize; the second yields the two-record collapse and the reusable interpretation of column-agreement as truth. When a single result has two independent derivations, each derivation typically leaves behind a different tool. For a programmer the analogue is direct: the smallest input that can exhibit a bug bounds the size of test cases you need, bounds the size of a model an exhaustive checker must explore, and is usually the fastest route to understanding why the bug exists at all.

**Source:** [Functional Dependencies in a Relational Database and Propositional Logic](../works/functional-dependencies-in-a-relational-database-and-propositional-logic.md) — the semantic proof of the equivalence theorem, which restricts attention to two-record structures and establishes the correspondence between column agreement and truth assignment, alongside the separate syntactic proof given earlier.
