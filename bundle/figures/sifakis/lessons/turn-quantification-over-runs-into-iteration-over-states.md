---
type: lesson
title: "A definition that ranges over all executions becomes computable once you restate it one step at a time"
figure: sifakis
works: [cesar-1982]
axes: [verifiability, cognitive-load]
subdomains: [formal-methods-and-verification, algorithms-and-complexity]
tags: [lesson]
---
# A definition that ranges over all executions becomes computable once you restate it one step at a time

**Lesson:** The meanings of the interesting temporal claims are given by quantifying over execution sequences, which are unbounded in number and length, so the definitions look like nothing a machine could evaluate. The bridge is to notice that each of them satisfies a recurrence in terms of a single step: a state has the property either directly or because of what holds at its immediate neighbours. That recurrence is a monotonic map on sets of states, and its solutions are fixed points. Because the map only ever grows or only ever shrinks its argument, iterating from the empty set or from everything converges on the one you want, in a number of rounds bounded by the size of the state space. Quantification over runs becomes a loop over sets.

The move worth internalizing is the change of variable, from a statement about paths to a statement about a set closed under taking predecessors. Everything downstream depends on it: the whole engine reduces to computing which states can step into a given set, applying that operator repeatedly, and testing for stability. Two things have to be true for the reduction to work, and they are worth checking explicitly whenever you attempt it — the operator must be monotone, and the domain must be well enough behaved that the iteration terminates. Neither is automatic, and reaching for iteration without them yields a procedure that quietly does not converge.

This pattern shows up far beyond temporal logic — reachability, dataflow analysis, constraint propagation, and type inference all wear it — and recognizing it is what turns a semantic definition into an implementation. When you meet a specification phrased over infinite objects, the first question to ask is whether membership in the answer set can be characterized locally, in terms of one transition and the answer itself.

**Source:** [Specification and Verification of Concurrent Systems in CESAR](../works/cesar-1982.md) — section 4.1's characterization of the temporal operators as fixed points of predicate transformers built from the one-step predecessor operator, and section 4.2's description of computing them by iteration.
