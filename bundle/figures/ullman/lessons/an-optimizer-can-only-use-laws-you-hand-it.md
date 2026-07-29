---
type: lesson
title: "An optimizer can only exploit the laws you hand it in advance"
figure: ullman
works: [a-comparison-between-deductive-and-object-oriented-database-systems]
axes: [expressiveness, verifiability, primitive-count, cognitive-load]
subdomains: [databases-and-data-management, programming-languages-and-semantics, programming-environments-and-object-systems]
tags: [lesson]
---
# An optimizer can only exploit the laws you hand it in advance

Writing at a high level of abstraction is not the same as writing something a machine can rearrange. Ullman's argument turns on a distinction most people collapse: a language can let you say "combine these three collections" very briefly and still give the system no grounds for choosing a good order to do it in. The freedom to reorder comes from knowing that the combining operation obeys particular laws — that it associates, that it commutes, that a filter can slide inside it. Those laws are not in the code that implements the operation. They are a separate piece of knowledge, and either the system was told them up front or nobody knows them.

This is why "raise the abstraction level" fails as a strategy on its own. If a user can define a new combining operation with a body written in a general-purpose language, the system faces the problem of deciding whether an arbitrary procedure is associative — a question nothing available can answer for arbitrary code. So the system must evaluate that operation exactly in the order written, which means every performance decision is back in the programmer's hands, which is precisely what the high-level notation was supposed to buy. The abstraction was raised and the leverage was lost.

The consequence is uncomfortable and worth sitting with: the operations you want optimized must come from a fixed, closed vocabulary whose algebraic properties are part of the system's design, not part of user code. The moment you let the vocabulary grow arbitrarily, the growable part becomes an opaque region the optimizer walks around. Ullman's blunt reading of this is that an extensible high-level language, once you freeze the operations enough to optimize them, has simply become a data model with a fixed algebra — which was the thing it claimed to improve on.

A programmer who takes this seriously separates two questions that usually get asked as one. First: what do I want to be able to express? Second: what rewriting freedom do I want the system to have? Answering the second demands committing to a small operator set with stated laws, and accepting that anything outside it will run as literally written. That reframes plugin points, user-defined functions, and custom aggregates as deliberate optimization barriers rather than free extensibility, and it explains why so many systems end up with a small blessed core surrounded by a slow escape hatch.

**Source:** [A Comparison Between Deductive and Object-Oriented Database Systems](../works/a-comparison-between-deductive-and-object-oriented-database-systems.md) — the section on declarativeness and methods, where Ullman works through a three-way combination whose evaluation order matters by orders of magnitude and asks what the system would need to know to pick between the orders.
