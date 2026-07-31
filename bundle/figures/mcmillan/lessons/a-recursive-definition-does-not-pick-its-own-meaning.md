---
type: lesson
title: "A recursive definition does not pick its own meaning — you do"
figure: mcmillan
works: [symbolic-model-checking-10-20-states-and-beyond]
axes: [verifiability, expressiveness, cognitive-load]
subdomains: [formal-methods-and-verification, programming-languages-and-semantics, foundations-of-computation]
tags: [lesson]
---
# A recursive definition does not pick its own meaning — you do

The two interesting temporal operators in this paper are derived the same way. Write the identity that expresses the operator one step at a time — "holds forever along some path" means "holds now, and holds forever along some path starting at a successor"; "holds until" unfolds just as neatly — and then notice that the operator satisfies it. Having written the unfolding you might think you have defined the operator. You have not. That equation has many solutions. The always-style operator is the *largest* of them and the until-style operator is the *smallest*, and the two are genuinely different sets: the gap between them is exactly the configurations that can go around a loop forever without the obligation ever coming due.

That gap is the whole content of the choice. An unfolding identity describes a single step, so it is structurally incapable of saying whether an execution that unfolds forever and never delivers counts as satisfying the definition. Naming the least solution says it does not — every member has to be reached by finitely many unfoldings, so the obligation must actually be discharged. Naming the greatest says it does — perpetual deferral is a legitimate way to satisfy the equation. Both readings are faithful to the identity. Only one is what you meant, and the identity will not tell you which.

Two consequences follow that are worth carrying anywhere. The first is that a self-referential specification should be treated as two decisions written down as one, and the second decision is the one people forget: it is where safety separates from liveness, where a well-founded relation separates from a merely consistent one, where an optimistic analysis separates from a pessimistic one. The second is that the extremes only exist under a condition, and that condition is worth enforcing syntactically rather than trusting authors to respect. The calculus here demands that the recursive variable appear only under an even number of negations — a check a compiler can run — and that mechanical check is what licenses the whole solve-by-iteration strategy, since the extreme solutions are then reachable by starting at the empty or full relation and applying the body until nothing changes.

Programmers hit this far more often than they notice, and usually resolve it by accident. Initialising a dataflow lattice at bottom rather than top, choosing whether a cyclic reference is an error or a fixed point, deciding whether a mutually recursive type is inhabited only by finite values or by infinite ones, choosing whether a rule engine's closure includes self-supporting conclusions — each is the same fork, and in each the two answers agree on every terminating case and disagree exactly on the pathological one. The habit to build is to notice when a definition refers to itself, write down what the perpetually-deferring case ought to mean, and pick the extreme accordingly instead of letting the evaluation order pick for you.

**Source:** [Symbolic Model Checking: 10^20 States and Beyond](../works/symbolic-model-checking-10-20-states-and-beyond.md) — the derivation of the branching-time operators from their unfolding identities as greatest and least fixed points respectively, the formal monotonicity restriction imposed on the calculus so those extremes exist, and the theorem relating the greatest solution to the least by exactly the cycle-reaching states.
