---
type: lesson
title: "Choose the grain of your operators and you choose who owns performance"
figure: date
works: [an-introduction-to-database-systems, databases-types-and-the-relational-model-the-third-manifesto]
axes: [hardware-affinity, parallelizability, cognitive-load]
subdomains: [databases-and-data-management, software-engineering-and-architecture, programming-languages-and-semantics]
tags: [lesson]
---
# Choose the grain of your operators and you choose who owns performance

**Lesson:** Date's sharpest pedagogical device is a comparison of two programs that do the same thing: one statement that names the desired outcome, next to some forty lines of position-keeping, chain-following, and manual bookkeeping that achieve it in a system whose operators work one record at a time. The lesson he draws is not that the short version is nicer. It is that the granularity of the operator set determines who is responsible for choosing an access strategy. If the operators consume and produce whole collections, the request carries no traversal plan, so the system is free to pick one, revise it as data volumes and available structures change, and vary it between two executions of identical code. If the operators consume one record at a time, the traversal plan is in the caller's source text, and it is frozen there.

This is why he rules out one-at-a-time access rather than merely discouraging it, and why he is careful to note that the ban is about the interface and not about the eventual need to iterate. Programs do sometimes need to walk results in order, for display or printing. His response is to make the crossing explicit: convert the collection into an ordered array in one operation, then iterate the array with the ordinary constructs of the host language. Ordering and stepwise access are legitimate needs of the environment, and pushing them out to a declared boundary keeps them from contaminating the model, while giving the implementation the freedom to fill the array lazily. The same reasoning applies to modifications, which are defined in terms of assigning a whole collection, with single-record forms admitted only as shorthand for a collection of one.

Date is honest that the usual label for this style is unsatisfactory, since being procedural is a matter of degree rather than a binary property. What he claims instead is a difference in level of abstraction, and he attributes the productivity gains of the whole approach specifically to that raise in level. The consequence for machine sympathy is the part usually missed: expressions that specify no order of visitation are exactly the ones an engine can reorder, restructure, split across storage units, or evaluate with whatever access structures happen to exist, since none of that can invalidate an answer that was never phrased as a sequence of steps.

A programmer holding this position designs interfaces around whole-collection operations and treats any per-item call across an expensive boundary as a design defect rather than a performance detail, since it hard-codes a plan into the caller. When iteration is genuinely required, they mark the point where the declarative world ends and the stepwise one begins, and keep that point as far out as they can.

**Source:** [An Introduction to Database Systems](../works/an-introduction-to-database-systems.md) — the optimization section of the introductory relational chapter, whose side-by-side comparison of a single declarative statement against hand-written navigation code motivates the argument that the system rather than the user should choose the access strategy, together with the surrounding treatment of set-level operators. Also [Databases, Types, and the Relational Model: The Third Manifesto](../works/databases-types-and-the-relational-model-the-third-manifesto.md), whose proscription against record-at-a-time operations states the rule directly and offers the load-into-an-array construction as the sanctioned way to iterate.
