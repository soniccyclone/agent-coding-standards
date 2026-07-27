---
type: lesson
title: "A specification must fix what the implementation is allowed to know, and when"
figure: pnueli
works: [on-the-synthesis-of-a-reactive-module]
axes: [expressiveness, verifiability, hardware-affinity]
subdomains: [formal-methods-and-verification, distributed-systems-and-concurrency]
tags: [lesson]
---

# A specification must fix what the implementation is allowed to know, and when

**Lesson:** Ordinary logical quantification records that one thing depends on another, and nothing at all about the moment at which the dependence is resolved. For a computation that reads everything, thinks, and then answers, that omission costs nothing, because there is exactly one moment and all the input is available at it. Stretch the same notation over an ongoing interaction and the omission becomes fatal: saying that for every input stream some output stream makes the requirement hold permits the chosen output at the earliest instant to have been computed from input values that had not arrived yet. The witness is a function of the entire history including its future, and no mechanism is that. There is a sharp, checkable example of the failure: demand that the very first thing a component emits report whether any input it will ever receive is going to be true. As a relation between two streams this is unimpeachable and demonstrably satisfiable. As a thing to build it requires foresight, which is not on offer.

What this reveals is that adequacy of a formalism is relative to the question asked of it. A notation can be entirely suitable for describing what a system does and simultaneously unsuitable for asking whether that behavior can be achieved, because achievability depends on a structure the notation never had to represent: the order in which information becomes available. Two requirements can pin down the identical relation between inputs and outputs and differ completely in whether anything can meet them, purely because of who knows what at which point. Any formalism used to settle buildability therefore has to force each committed output to be a function of the strictly prior input, and if the formalism cannot express that restriction, it must be extended until it can rather than trusted anyway.

This is the specification-level shadow of a physical constraint, which is why it generalizes far past temporal logic. Every design in which a decision must be committed before the evidence justifying it arrives has the same shape: cache eviction, scheduling, speculative execution, streaming aggregation, a distributed participant that must act on a stale view, a user interface that must render before the fetch returns. In each case the tempting analysis is done with the whole trace laid out flat, from which position the right choice is obvious, and the obviousness is an artifact of standing outside time.

The habit to acquire is to separate the relation you want from the causal budget under which it must be produced, and to state both. When reviewing an argument that a design works, locate the moment of each decision and check that every quantity the argument leans on had already arrived at that moment. When the check fails, the design is not merely imprecise, it is impossible, and the impossibility is not repairable by better code. The available repairs are structural: delay the commitment, weaken the requirement to allow a bounded lag, or accept an approximation and make the error budget explicit.

**Source:** [On the Synthesis of a Reactive Module](../works/on-the-synthesis-of-a-reactive-module.md) — the part of the implementability section that rejects the naive quantified formula as a buildability criterion, using the requirement whose first output must anticipate all later inputs, and the accompanying observation that a program's definition permits its output to rest only on inputs already seen.
