---
type: lesson
title: "Separate the structure that is in the system from the structure your model imposes on it"
figure: mcmillan
works: [symbolic-model-checking-an-approach-to-the-state-explosion-problem]
axes: [parallelizability, hardware-affinity, cognitive-load]
subdomains: [distributed-systems-and-concurrency, formal-methods-and-verification, programming-languages-and-semantics]
tags: [lesson]
---
# Separate the structure that is in the system from the structure your model imposes on it

The thesis models the same asynchronous circuit two ways. In one, every component independently decides each round whether to update; in the other, exactly one component updates per round and which one is arbitrary. Both are defensible accounts of "these parts run at unrelated speeds," and on the examples studied both yield exactly the same set of reachable configurations. Yet their costs differ by a whole order of growth, and the explanation has nothing to do with the circuit.

The reason is a correlation manufactured by the second model. If precisely one component moves per round, then after some number of rounds the per-component move counts must sum to that number — so the set of configurations discovered at each round is characterised by a counting condition over otherwise unrelated components. Counting conditions are exactly the shape whose compact representations grow quadratically rather than linearly. The components in the real circuit have no such relationship; the arithmetic tying them together is an artefact of insisting that events be totally ordered. The intermediate results pay for a constraint the system does not have.

This is worth generalising because the mistake it exposes is invisible from inside. Both models are correct, both compute the same answer, and nothing in either one announces that it is smuggling in an accidental invariant. The only way to catch it is to ask, of every structural feature you observe in your intermediate data, whether it reflects the system or your description of the system. The thesis catches it by looking directly at the sizes of the representations produced during the search and reasoning about what shape of function those sizes correspond to — measurement of the internals, not of the outputs.

A programmer who takes this seriously stops treating semantically equivalent formulations as interchangeable and starts asking what each one asserts beyond what was intended. Total orders imposed on genuinely independent events, sequence numbers imposed on unordered work, synchronised clocks imposed on unsynchronised parts — each is a place where a modelling convenience becomes a real cost, and where the cheaper formulation is usually the one that commits to less.

**Source:** [Symbolic Model Checking: An Approach to the State Explosion Problem](../works/symbolic-model-checking-an-approach-to-the-state-explosion-problem.md) — the comparison of simultaneous and interleaving models of asynchronous machines, and the argument explaining why the interleaving formulation induces a counting relationship among independent components.
