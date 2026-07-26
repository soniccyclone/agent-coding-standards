---
type: lesson
title: "Verifiability is a property of the architecture you chose, so pick structures whose guarantees compose"
figure: emerson
works: [model-checking-algorithmic-verification-and-debugging]
axes: [verifiability, parallelizability, cognitive-load]
subdomains: [software-engineering-and-architecture, distributed-systems-and-concurrency, formal-methods-and-verification]
tags: [lesson]
---
# Verifiability is a property of the architecture you chose, so pick structures whose guarantees compose

**Lesson:** After-the-fact checking of a finished system is one strategy for correctness, and the disciplines that computing likes to compare itself to do not rely on it. An electrical engineer does not build a circuit and then search its behavior space; the theory supplies composition laws that make the assembled artifact meet its properties by construction. The gap is not that computing lacks such results — there is a substantial body of them for coordination structures and distributed algorithms — but that they are treated as a separate literature from verification rather than as the thing verification should be steering toward. Between full construction-by-theory and exhaustive after-the-fact search there is a wide space, and the interesting engineering lives in it.

The reason this is a design question rather than a tooling question is that general compositional reasoning does not work. Decomposing a global property into per-component obligations plus assumptions about each component's environment is the standard approach, and synthesizing the assumptions can cost as much as checking the whole system monolithically. A fully general theory of composition would be intractable and of theoretical interest only. What does work is giving up generality in two specific directions: fix the property class, or fix the architecture. Deadlock-freedom composes cheaply under a structural condition on how components interact, and that condition is a property of the arrangement, checkable without exploring behavior. Different property classes need different arguments. Particular topologies, particular scheduling regimes, particular timing disciplines each admit composition rules that no general theory provides.

The conclusion is the one worth carrying: the conditions under which a property composes are conditions on the system's structure, which means they are available at design time as constraints. Verifiability then joins testability as a quality you choose an architecture for, and a composition rule for a restricted class of structures is effectively a construction technique — build it this shape and the property follows from the parts. A programmer who thinks this way asks, before committing to a topology or a synchronization scheme, which global properties will still be checkable component-by-component afterward, and treats an arrangement that forces whole-system reasoning as carrying a permanent cost rather than a one-time one.

**Source:** [Model Checking: Algorithmic Verification and Debugging](../works/model-checking-algorithmic-verification-and-debugging.md) — Sifakis's sections on scalable verification and on moving from after-the-fact verification toward constructivity: the argument against general compositional theories, the proposal to specialize by property class and by architecture, the deadlock-freedom example resting on a structural condition on the interaction graph, and the framing of verifiability conditions as analogous to designing for testability.
