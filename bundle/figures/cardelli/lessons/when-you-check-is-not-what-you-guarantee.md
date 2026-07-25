---
type: lesson
title: "Separate the guarantee you require from the moment you establish it, and pick the moment per boundary"
figure: cardelli
works: [a-language-with-distributed-scope, on-understanding-types-data-abstraction-and-polymorphism]
axes: [verifiability, expressiveness]
subdomains: [programming-languages-and-semantics, distributed-systems-and-concurrency]
tags: [lesson]
---
# Separate the guarantee you require from the moment you establish it, and pick the moment per boundary

**Lesson:** Debates about checking collapse two questions that should be asked separately. The first is what must never happen: an operation applied to something it cannot handle, producing arbitrary behaviour instead of a clean failure. The second is when you find out: during construction, or at the moment of use. The property worth insisting on is the first, and it can be had either way. Establishing it entirely before execution is better where it is available, since it costs nothing at run time and rules out whole categories of fault early. But a system that checks late and refuses to proceed on a violation still delivers the property, while a system that checks early on paper and has holes in its rules does not.

Separating the two questions lets the answer differ per boundary, which matters most where boundaries are expensive. Committing to complete prior checking across a distributed system means every participant must agree in advance about the descriptions of everything they exchange, which is a coupling between independently deployed parts and a source of compatibility problems that has nothing to do with the correctness of any one program. Deciding at the point of use instead purchases independence, and the guarantee is retained by making violations produce clean, propagated errors rather than undefined behaviour. That choice also has a second-order benefit worth noticing: a design that keeps the value space heterogeneous, so that nothing quietly stands in for something of another kind, stays compatible with prior checking later even if it does not perform it now, which keeps the option open rather than foreclosing it.

The general habit is to write down the invariant first and the enforcement schedule second, and to justify the schedule by the boundary it sits on rather than by allegiance to a school. Systems that reason the other way, starting from when they want to check, end up either weakening the invariant to fit the schedule or paying coupling costs they never intended.

**Source:** [A Language with Distributed Scope](../works/a-language-with-distributed-scope.md) — the language overview's account of a design without prior checking whose run-time discipline is nonetheless strong, with clean errors propagated across sites, and its note that heterogeneity plus strict scoping keeps the design amenable to prior checking. Also [On Understanding Types, Data Abstraction, and Polymorphism](../works/on-understanding-types-data-abstraction-and-polymorphism.md) — the early section distinguishing checking before execution from the weaker requirement of consistency however established, and recommending the strong property always with the early schedule where possible.
