---
type: lesson
title: "Model only the part of the program the claim can see"
figure: clarke
works: [design-and-synthesis-of-synchronization-skeletons-using-branching-time-temporal-logic, automatic-verification-of-finite-state-concurrent-systems-using-temporal-logic-specifications]
axes: [cognitive-load, verifiability]
subdomains: [formal-methods-and-verification, distributed-systems-and-concurrency]
tags: [lesson]
---
# Model only the part of the program the claim can see

**Lesson:** Before any algorithm can help you, something has to decide what the program *is* for the purpose of the question being asked. The founding insight here is that for coordination properties, a process is adequately described by a graph whose nodes are regions of code and whose arcs carry the conditions under which the process may move between them. What happens inside a region is deliberately left uninterpreted. Whether the critical section increments a counter or rewrites a database is invisible to the claim that two processes are never inside their critical sections at once, so it should be invisible to the model. Transitions within a region are not recorded at all.

This is a discipline about what to look at, and it is upstream of every efficiency argument. It works because properties come with an implicit dependency footprint: the set of program facts whose alteration could flip the property's truth value. Anything outside that footprint is free to be erased, and erasing it is not an approximation but a change of subject that preserves the answer exactly. Notice also the empirical observation that made the move safe rather than presumptuous: solutions to synchronization problems in the literature were already being published in this reduced form. The abstraction was not imposed on practice, it was recovered from how practitioners already thought.

The payoff compounds. Once the model contains only coordination states, it is finite, usually small, and the propositional fragment of a temporal logic suffices to talk about it. Everything downstream — decidability, cheap checking, the whole apparatus — is a consequence of having drawn the boundary in the right place first. Conversely, a model that faithfully retains detail the property cannot observe will be both intractable and no more trustworthy.

A programmer who internalizes this treats "what is the smallest thing I can reason about that still answers my question" as the first design step in any correctness argument, review, or test plan. The habit generalizes well beyond formal methods: it is the difference between a review that traces the one invariant at stake through the code and a review that reads everything with uniform attention and notices nothing.

**Source:** [Design and Synthesis of Synchronization Skeletons Using Branching Time Temporal Logic](../works/design-and-synthesis-of-synchronization-skeletons-using-branching-time-temporal-logic.md) — the introduction and the model-of-computation section, where the skeleton is defined as the program with synchronization-irrelevant detail suppressed and code regions left uninterpreted; the 1986 paper repeats the discipline when it builds the two-process mutual exclusion graph and states that moves within a region are not represented.
