---
type: lesson
title: "A correspondence established operation by operation never has to be executed"
figure: jones
works: [software-development-a-rigorous-approach]
axes: [verifiability, hardware-affinity, cognitive-load]
subdomains: [formal-methods-and-verification, software-engineering-and-architecture]
tags: [lesson]
---
# A correspondence established operation by operation never has to be executed

**Lesson:** People who meet the idea of relating a machine-shaped structure back to an idealized one often assume there is a translation happening somewhere at runtime — that something has to convert back and forth so the abstract account stays true. Nothing of the kind occurs, and understanding why is what makes abstraction free rather than expensive.

The reasoning is short. Show, for each individual operation, that performing the concrete version and then interpreting the result gives the same thing as interpreting first and performing the abstract version. Now put two of them one after the other. The state left behind by the first concrete operation is already a legitimate starting state for the second concrete operation — that is what the first obligation established — so there is no point at which the abstract counterpart needs to exist. Interpreting after the first step and re-finding a concrete state for the second would be a detour producing nothing. Control stays entirely with the concrete operations, joined by whatever the language uses to join things, and the correspondence rides along untouched. Where an operation reports an answer rather than changing state, even the notional interpretation disappears: the answer produced concretely simply is the answer, in the same type, with nothing to convert.

Two things follow that are worth holding onto. First, the correspondence is an artifact of reasoning, not of execution. It exists so that you can talk about the system in the terms you designed it in; the running program never mentions it. This is the sense in which a good abstraction costs nothing — not that the compiler optimized it away, but that it was never there to optimize. Second, and more general: proving a property pointwise over a set of primitives buys you that property over every composition of them, without any further work, provided the composition operators are the ones you assumed. That is what makes local obligations worth their price. You check a fixed, small number of things, and you get a guarantee over an unbounded set of programs — which is a far better trade than any amount of checking assembled programs one at a time.

**Source:** [Software Development: A Rigorous Approach](../works/software-development-a-rigorous-approach.md) — chapter 11's "Refinement of Operations" section, in the discussion of collections of operations: the observation that since the language's constructs link operations together, if the individual operations model those of an abstraction then so does their combination; the specific argument that once a representation of an initial state has been processed by one modelling operation the resulting state is already usable by the next, so applying the retrieve function and finding another corresponding state is superfluous and control can be given entirely to the operations of the representation linked by the sequencing constructs of the programming language; and the accompanying note that when a final interrogating operation delivers a value in another data type, the answers are identical and need no relating at all.
