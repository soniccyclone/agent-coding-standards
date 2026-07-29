---
type: lesson
title: "Two orthogonal decompositions cannot share one mechanism without both coming out wrong"
figure: reenskaug
works: [the-dci-architecture-a-new-vision-of-object-oriented-programming]
axes: [cognitive-load, expressiveness, primitive-count]
subdomains: [programming-environments-and-object-systems, software-engineering-and-architecture]
tags: [lesson]
---
# Two orthogonal decompositions cannot share one mechanism without both coming out wrong

Reenskaug and Coplien identify a specific structural fault rather than a matter of taste. There are two legitimate ways to carve a program, and they answer to unrelated criteria. One carves by what knowledge belongs together and must be protected behind a boundary. The other carves by how a procedure breaks into steps a reader can hold one at a time. Nothing guarantees these two carvings coincide, and usually they do not, because the steps of an interesting operation range across several holders of knowledge. A language that offers exactly one boundary-making construct forces both carvings through it, and the outcome is decided by which one you privilege.

Both outcomes are bad in predictable ways, and recognizing the symptom is the practical payoff. Privilege the procedural carving and fragments of an operation end up housed in a holder that then has to reach outside itself constantly, showing up as excess coupling. Privilege the knowledge carving and each holder receives only the slivers of the operation that touch its own data, showing up as a swarm of tiny methods that individually mean nothing and collectively hide the operation — while the operation itself exists nowhere as a readable whole. Teams then measure the symptom, tune for the metric that is complaining, and shift the damage to the other side without ever naming the cause.

The resolution is not to pick better boundaries within one mechanism but to notice that a mechanism is missing. Once a second construct exists — one whose boundaries are drawn by the shape of the operation, independent of which data holder ends up executing it — each carving can be made on its own merits, and the two can cross each other freely rather than competing for the same lines. That the two are then fused at run time is an implementation matter; the point is that they are written separately, because they are answering different questions.

A programmer who has internalized this treats an unresolvable coupling-versus-cohesion argument as diagnostic. If tuning one always degrades the other, the two things being traded are not on the same axis and the tool being used to trade them is overloaded. The question shifts from where to draw the line to how many kinds of line the notation lets you draw.

**Source:** [The DCI Architecture: A New Vision of Object-Oriented Programming](../works/the-dci-architecture-a-new-vision-of-object-oriented-programming.md) — the "Where did we go wrong?" and roles sections, which argue that stepwise refinement of an algorithm has no reason to align with the demarcations of the data model, and enumerate what goes wrong when one demarcation mechanism serves both.
