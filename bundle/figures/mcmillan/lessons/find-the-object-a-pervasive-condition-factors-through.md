---
type: lesson
title: "When a condition touches every case, find the one object it factors through"
figure: mcmillan
works: [symbolic-model-checking-10-20-states-and-beyond]
axes: [expressiveness, cognitive-load, primitive-count]
subdomains: [formal-methods-and-verification, programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# When a condition touches every case, find the one object it factors through

A requirement arrives that the specification language cannot express. Here it is fairness: you want to reason only about executions in which certain things keep recurring, and there is no way to say that inside the logic. The paper's response is instructive in two separate ways, and the first is simply that it does not fake it. Rather than encoding a workaround at each site where fairness is wanted, it says outright that the semantics of the logic must be modified — every path quantifier now ranges over a restricted set of executions. The requirement was not expressible, so the interpretation changed and the change was announced. That is the honest option, and it is available far more often than the contortions people substitute for it.

The second is the engineering. A change to the meaning of every quantifier looks like it means reworking every operator, and one of them genuinely does have to be reworked — the one asserting that something holds throughout an infinite execution, which is where recurrence actually interacts with the definition, and which comes out as a fixed point nested inside another fixed point. But having done that one, the authors define a single derived set: the configurations from which some acceptable execution exists at all. Every remaining operator is then the old, unmodified operator applied to its argument narrowed by that set. Three cases; one is hard, and the other two collapse into a conjunction.

The move generalises to any cross-cutting condition that seems to demand touching every branch of a definition, an interpreter, a query planner, or a permission system. Do not thread the condition through each case. Look for a single object the condition factors through — a derived set, a precomputed predicate, a saturated relation — such that each case becomes its unconditional self restricted by that object. Two things follow immediately: the expensive derivation happens once rather than per case, and the number of places that can be wrong drops from many to one.

Finding the object requires attacking in the right order, and the order is counterintuitive. Start with the case where the condition genuinely bites, not the easy ones, because the derived object is almost always something that falls out of solving the hard case. Here the set of configurations admitting an acceptable execution is just the hard operator applied to a trivial argument — it was already constructed, and the remaining work was noticing it could be reused. Solving the easy cases first would have produced a pile of special handling and no shared object at all.

**Source:** [Symbolic Model Checking: 10^20 States and Beyond](../works/symbolic-model-checking-10-20-states-and-beyond.md) — the fairness-constraints section: the statement that the property is not expressible in the logic and the semantics must therefore be modified, the nested fixed-point characterisation of the globally-operator under constraints, and the reduction of the remaining two constrained operators to their unconstrained forms conjoined with the set of states on some fair computation.
