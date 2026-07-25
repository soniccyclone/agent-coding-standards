---
type: lesson
title: "How precise a specification must be is set by how many independent implementers must agree"
figure: backus
works: [syntax-and-semantics-of-the-proposed-international-algebraic-language]
axes: [verifiability, cognitive-load]
subdomains: [formal-methods-and-verification, programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# How precise a specification must be is set by how many independent implementers must agree

**Lesson:** A notation can have two distinct purposes, and they demand different amounts of rigor. If the goal is only that people can read each other's procedures, an informal description with well-chosen examples does the job, and prose is adequate. If the goal is that the same text runs on machines built by different manufacturers, with translators written by teams that never speak to each other, then two things must be pinned down formally: exactly which sequences of symbols count as legal, and exactly what each legal one means. Absent the first, a text one team's translator accepts another's rejects. Absent the second, both accept it and produce programs that differ in ways that matter. The requirement is not aesthetic and not about proof for its own sake. It is a function of how many independent parties have to reach the same conclusions unaided.

The mechanism behind the failure is worth naming because it does not feel like a failure while it happens. Everything the specification leaves informal still gets decided — by whoever writes the tool, at the moment they hit the ambiguity, according to whatever seemed reasonable that afternoon. The decision is real, it is binding on that implementation's users, and it is invisible to everyone else. Anyone who has built a translator from an informal description has made a large number of these choices without recording them. Multiply by the number of implementations and the portability the whole exercise was for is gone, with the effort already spent.

The practice this implies is to locate the divergence cost before deciding how formal to be. Where multiple independent implementations must agree, or where a wrong assumption is expensive and hard to detect, spend the effort to specify formally, and accept that the formal part will be less pleasant to read than the prose. Where there is one implementation and its behavior is the definition in practice, prose plus examples is honest and cheaper. What is never defensible is wanting the guarantees of the first situation while doing the work appropriate to the second.

**Source:** [The Syntax and Semantics of the Proposed International Algebraic Language](../works/syntax-and-semantics-of-the-proposed-international-algebraic-language.md) — the general part of the formal description, which separates the goal of human communication from the goal of running one program on many machines, states the two precision requirements the second goal imposes, and argues that informality relocates the decisions into each translator's construction.
