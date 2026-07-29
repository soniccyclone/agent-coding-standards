---
type: lesson
title: "Keep the mechanism breaking and the mechanism being wrong as two different failure classes"
figure: turing
works: [computing-machinery-and-intelligence]
axes: [verifiability, cognitive-load]
subdomains: [foundations-of-computation, software-engineering-and-architecture]
tags: [lesson]
---
# Keep the mechanism breaking and the mechanism being wrong as two different failure classes

There are two unrelated things that get called the same thing when a system disappoints you. In one, the physical apparatus departs from what it was built to do — a component degrades, a signal is corrupted, the realized machine and the specified machine come apart. In the other, the apparatus does exactly what it was built to do and the meaning attached to its output is false. The first kind is impossible by construction in an idealized machine, because an idealized machine is a mathematical object with no separate body to fail. The second kind is always possible, and is not a defect in the apparatus at all: any procedure that reaches conclusions by generalizing from evidence will sometimes reach false ones, and this is a property of the procedure's licence rather than of its wiring.

The distinction matters because the two classes have disjoint remedies and disjoint verification stories. You attack the first with redundancy, checksums, monitoring, and by narrowing the gap between the specification and the implementation. You attack the second by changing what the system is licensed to conclude — the inference rules, the priors, the confidence thresholds — and no amount of hardware reliability touches it. Conflating them produces two characteristic wastes: chasing a hardware ghost when the logic was simply entitled to be wrong, and patching the logic when the real story was a flaky component. A useful diagnostic is that a fault in the apparatus tends to show up as an output that is not even a plausible member of the output class, whereas a wrong conclusion is well-formed and merely false.

A programmer who holds this distinction firmly writes error taxonomies with a bright line through the middle: invariant violations that mean "this code cannot be running correctly, stop" versus results that mean "the model was applied faithfully and disagrees with reality." The first should abort loudly; the second should be recorded, scored, and fed back. It also changes what you claim in a design document. Saying a component is correct is a statement about the first class only; it is not a promise the component's answers are true, and a system whose answers must be true needs an argument the correctness proof cannot supply.

**Source:** [Computing Machinery and Intelligence](../works/computing-machinery-and-intelligence.md) — inside the reply to the objection that machines are incapable of error, where the paper splits mistakes into a mechanical-departure kind and a false-assertion kind and shows the objection only holds for one of them.
