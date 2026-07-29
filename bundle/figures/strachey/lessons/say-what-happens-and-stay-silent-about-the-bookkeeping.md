---
type: lesson
title: "Say what happens and stay silent about the bookkeeping"
figure: strachey
works: [continuations-a-mathematical-semantics-for-handling-full-jumps]
axes: [cognitive-load, hardware-affinity, verifiability]
subdomains: [programming-languages-and-semantics, formal-methods-and-verification]
tags: [lesson]
---
# Say what happens and stay silent about the bookkeeping

**Lesson:** A specification of what a construct does is a different artifact from an account of how a machine gets it done, and the discipline worth acquiring is the ability to write the first without leaking the second. The continuation treatment makes this concrete by listing exactly what a fragment of program needs in order to have a meaning at all: the bindings in force, the state reached so far, and the computation still owed. Notice what is absent from that list. Nothing about where control currently sits, nothing about where half-finished subexpression results are parked, nothing about frames or registers or return addresses. Those are all real and all necessary on hardware, and none of them belong in the statement of what the program computes.

The reason this holds is that every mechanism you name in a specification becomes a promise. Mention a stack of pending results and you have quietly forbidden an implementation that keeps them elsewhere, or that keeps them nowhere because it fused the computation away. Keep the mechanism out and any strategy that produces the specified outcome is legitimate, which is precisely the freedom an implementer needs in order to fit a machine he can see and you cannot. The same silence buys a second thing: correctness of an implementation becomes a claim you can actually state, because there is now a target independent of the implementation to compare it against, rather than two descriptions of machinery that differ in ways nobody can classify as bug or liberty.

The habit generalises well past language definition. A programmer who has internalised it writes down the observable obligation of a module — what relation holds between what goes in and what comes out, what state it is entitled to have touched — and resists the strong pull toward describing the loop, the buffer, the ordering, the cache that currently produce it. When the pull wins, the incidental becomes contractual, callers start depending on it, and the freedom to reorganise is gone before anyone noticed it was being spent. The distinction being drawn here is ultimately between a function and an algorithm, and between a value and its representation; conflating either pair costs you the ability to change your mind later.

**Source:** [Continuations: A Mathematical Semantics for Handling Full Jumps](../works/continuations-a-mathematical-semantics-for-handling-full-jumps.md) — the closing discussion, where the three arguments to the semantic functions are characterised as the full context a program fragment needs, followed by the explicit observation that run-time organisation is deliberately kept out of view.
