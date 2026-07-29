---
type: lesson
title: "A requirement nobody can point at in the code cannot be reviewed"
figure: reenskaug
works: [the-dci-architecture-a-new-vision-of-object-oriented-programming]
axes: [verifiability, cognitive-load]
subdomains: [software-engineering-and-architecture, programming-environments-and-object-systems]
tags: [lesson]
---
# A requirement nobody can point at in the code cannot be reviewed

Reenskaug and Coplien recall a capability that was lost rather than a technique that was never invented: handing a colleague a statement of what the program should do alongside the program, and having them mark up the disagreements. That works only when the shape of the text follows the shape of the requirement — when an operation described in one paragraph appears in the code as one readable run of steps. It stops working the moment the operation is dispersed, because reviewing dispersed logic means first reconstructing it from fragments, and reconstruction is exactly the activity a reviewer is least reliable at and least willing to do.

What displaced it was a doctrine, and naming the doctrine is the useful part: system-level behavior was supposed to arise from many small local decisions, so writing anything resembling a whole procedure marked you as not understanding objects. The authors treat this as a mythology with a real cost. Emergent behavior is unreviewable behavior. When the correspondence between a stated requirement and an identifiable region of code is gone, so is the cheapest and most effective form of verification anyone has — a second person reading with the specification in hand — and nothing that replaced it covers the same ground.

The design consequence is that traceability is a property to be engineered, not a fortunate accident of good style. If a system operation matters, there should be a place you can open where that operation appears end to end, in terms whose names came from the people who asked for it, and whose steps a reader can compare line by line against what was requested. That such a region can also be exercised in isolation with the participants substituted falls out of the same arrangement, which is why the reviewability argument and the testability argument are the same argument.

A programmer who accepts this stops treating "the logic is spread across the collaborating parts" as sophistication. The question asked of any architecture becomes: for a named requirement, can someone put a finger on the code and read it against the request? If not, every claim about that requirement holding rests on inference rather than inspection.

**Source:** [The DCI Architecture: A New Vision of Object-Oriented Programming](../works/the-dci-architecture-a-new-vision-of-object-oriented-programming.md) — the "Where did we go wrong?" section, with its recollection of reviewing requirements against code with a red pen and its critique of the emergent-behavior mythology, and the later observation that a role-scoped algorithm reads as a near-literal expansion of the requested scenario.
