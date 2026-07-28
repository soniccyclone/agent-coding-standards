---
type: lesson
title: "Keep the distinctions your implementation collapses"
figure: liskov
works: [data-abstraction-and-hierarchy]
axes: [cognitive-load, verifiability]
subdomains: [software-engineering-and-architecture, programming-environments-and-object-systems, programming-languages-and-semantics]
tags: [lesson]
---
# Keep the distinctions your implementation collapses

**Lesson:** Designs are not discovered whole. An abstraction shows up early with a partial set of operations, and each subsequent piece of the program that uses it demands a bit more, so what began as one idea accretes into something broader. The tempting move is to keep merging: there is one abstraction, it now does more, everybody talks to the same thing. The merge is cheap at the time and expensive later, because it erases the record of which client needed which part.

Treating each accretion as a distinct refinement — the same idea plus what this new client required — buys something concrete. When a later investigation shows a mistake in the newer, wider version, only the clients that asked for the wider version have to be reexamined; the clients that only ever needed the original are provably unaffected. That is not a stylistic preference, it is a smaller blast radius, and it is available only if the distinction was recorded when it was made. As a side effect the layers become a chronology of decisions, so a defect discovered late can be traced to the point where the reasoning went wrong instead of being diffused across one large description.

The important twist is that the distinction is worth keeping even when it never appears in the code. It is frequently more convenient to implement the accreted result as a single module rather than a stack of them, and that is fine — the layering was doing its work at the level of descriptions, not modules. Collapsing at build time still leaves you able to answer "who depended on this part" from the design record. Insisting that every conceptual layer become a physical one is a separate, usually unprofitable decision, and conflating the two is what makes people abandon the layering entirely.

A programmer who believes this keeps a written trail of which requirement introduced which capability, and resists the urge to fold that trail into the code's shape or to discard it because the code did not need it. When a change lands, the first question is which layer it touches, because that determines who must be rechecked — and an answer exists only because someone declined to merge.

**Source:** [Data Abstraction and Hierarchy](../works/data-abstraction-and-hierarchy.md) — the incremental-design section, where refining a type as successive subtypes limits which using modules must be reexamined after a change, and remains useful even when the final design is implemented as one module.
