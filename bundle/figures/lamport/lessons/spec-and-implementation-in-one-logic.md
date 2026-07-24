---
type: lesson
title: "Put the system and its specification in one formalism, so 'implements' becomes implication"
figure: lamport
works: [the-temporal-logic-of-actions, specifying-systems]
axes: [verifiability, expressiveness, primitive-count]
subdomains: [formal-methods-and-verification]
tags: [lesson]
---

# Put the system and its specification in one formalism, so 'implements' becomes implication

**Lesson:** When specifications live in one notation and implementations in another, the relation between them ("this satisfies that") needs its own ad hoc theory, and every level of a design hierarchy needs a fresh bridge. The dissolving move is to represent both as formulas in the same logic, each describing its set of allowed behaviors. Then "the algorithm satisfies the property" and "the low-level design implements the high-level one" are both the same statement — one formula implies the other — and refinement through any number of abstraction levels is just a chain of implications, checkable with ordinary logical machinery. Composition gets the same treatment: running two components together is the conjunction of their formulas, which only works if a formula constrains its own variables and leaves the rest of the universe alone.

Making implication actually hold across abstraction levels forces a discipline that is valuable in itself: a specification must not distinguish granularities it does not care about. A description of a system must permit steps that leave its variables unchanged, because a finer-grained implementation will take many steps invisible at the coarse level; a spec that forbade them could never be implemented by anything more detailed than itself. Building this stuttering-invariance in from the start is what keeps abstraction boundaries real — the coarse description genuinely does not know or care how many micro-steps realize one of its actions.

The payoff shows up in how a designer thinks. There is no longer a specification language over here and a modeling language over there; there is one semantic universe (behaviors, i.e. state sequences) and everything — property, protocol, hardware description — denotes a set of them. Questions like "does the cache protocol implement the memory?" stop being philosophical and become proof obligations with a standard shape: exhibit the substitution (a refinement mapping) under which the detailed formula implies the abstract one. A single relation, implication, carries the entire vertical structure of a design.

**Source:** [The Temporal Logic of Actions](../works/the-temporal-logic-of-actions.md) — the opening thesis that algorithm and property are formulas in one logic with correctness as implication, the stuttering-steps argument via the two-clock example, and parallel composition as conjunction. [Specifying Systems](../works/specifying-systems.md) — the same semantics carried into an engineering-scale language, with behaviors as state sequences over the variables of an entire universe and theorems of the form spec-implies-property.
