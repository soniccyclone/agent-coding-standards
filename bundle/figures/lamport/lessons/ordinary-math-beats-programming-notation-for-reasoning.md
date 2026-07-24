---
type: lesson
title: "For describing and reasoning about systems, ordinary mathematics beats programming notation"
figure: lamport
works: [the-temporal-logic-of-actions, specifying-systems]
axes: [primitive-count, expressiveness, cognitive-load]
subdomains: [formal-methods-and-verification, programming-languages-and-semantics]
tags: [lesson]
---

# For describing and reasoning about systems, ordinary mathematics beats programming notation

**Lesson:** Programming languages feel simpler than logic because they are familiar, but the familiarity hides real semantic weight. Assignment is a more complicated concept than equality: equality obeys algebraic laws you can calculate with, while assignment drags in locations, aliasing, and evaluation order — complications languages must carry because they exist to be compiled efficiently, not to be reasoned about. Describing a step of computation as a plain boolean relation between old and new state (primed and unprimed variables in one formula) recovers all of algebra as a reasoning tool. The formalism needed on top of everyday mathematics turns out to be astonishingly small: a handful of added operators suffices to describe concurrent systems, and the temptation to import programming constructs into the description language evaporates on contact — what a specifier actually needs is a robust notation for mathematics, including mathematics in the large, since real system descriptions are twenty-page formulas and mathematicians only ever built tools for twenty-line ones.

There is a load-bearing corollary about where reasoning effort should live: almost all of it should be ordinary, nontemporal mathematics. In a well-factored verification, temporal reasoning is a thin glue layer, and the bulk of every proof is manipulation of predicates and relations that any mathematically literate person can check. A formalism is practical exactly to the degree that it minimizes its exotic part and maximizes the part where centuries of mathematical technique apply. The same instinct favors abstract descriptions over executable ones: reasoning about a one-page abstract algorithm is feasible, reasoning about its five-thousand-line realization is not, and correctness secured at the abstract level is what makes the realization trustworthy.

A programmer who takes this seriously reaches for a state relation, a set, or a function where habit would reach for pseudocode; treats "can I calculate with this notation?" as the test of a good description; and resists enriching a specification language with features, on the grounds that every construct beyond ordinary math is a construct that ordinary math can no longer help you reason about.

**Source:** [The Temporal Logic of Actions](../works/the-temporal-logic-of-actions.md) — the opening "logic versus programming" argument (equality versus assignment, toy languages as dangerously misleading, why languages are necessarily complicated), and the design of TLA as familiar math plus three operators with temporal reasoning minimized. [Specifying Systems](../works/specifying-systems.md) — the account of setting out to design an abstract programming language atop the logic and discovering no programming constructs were needed, only notation for mathematics in the large.
