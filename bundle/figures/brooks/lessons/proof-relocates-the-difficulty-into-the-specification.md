---
type: lesson
title: "Proof relocates the difficulty rather than removing it: agreeing with a specification is worth little until the specification is the hard part you have debugged"
figure: brooks
works: [no-silver-bullet]
axes: [verifiability, cognitive-load]
subdomains: [formal-methods-and-verification, software-engineering-and-architecture]
tags: [lesson]
---
# Proof relocates the difficulty rather than removing it: agreeing with a specification is worth little until the specification is the hard part you have debugged

**Lesson:** A verified program is one shown to agree with a statement of what it should do. That is genuinely valuable, and for a small number of artifacts where failure is intolerable it is worth almost any cost. But it establishes a relation between two descriptions, and it says nothing about whether the second description is the one you wanted. Since the labour of arriving at a complete, consistent, and correct statement of intent is precisely where the difficulty of building systems concentrates, a technique that presupposes such a statement has assumed away the problem it appeared to solve. Much of the real work of building a system consists of finding out that the specification was wrong.

Two further limits follow from taking proof seriously rather than dismissively. Proofs are themselves artifacts made by people and can be mistaken, so verification reduces the testing burden instead of abolishing it. And the effort involved is large enough that only a handful of substantial programs have ever been carried through, which means the technique's reach is set by economics as much as by theory. None of this argues against formal reasoning. It argues against a particular hope: that pushing correctness upstream into a proof obligation removes rather than repositions the intellectual work.

The habit this produces is to treat the specification as the primary object of scepticism. Before asking whether the code matches the spec, ask what evidence exists that the spec matches the need, and arrange for that evidence to arrive early and from outside the team that wrote it. It also produces a clear-eyed view of where formal methods pay best: components with small, sharply bounded interfaces and consequences severe enough to justify the cost, sitting inside a larger system whose requirements are still being discovered by use. Verifiability is a property worth designing for, and it is also a property whose value is capped by the quality of the statement being verified against.

**Source:** [No Silver Bullet: Essence and Accidents of Software Engineering](../works/no-silver-bullet.md) — the survey section's assessment of program verification as a candidate breakthrough, which grants the technique's power for particular kernels while arguing that the residual difficulty sits in reaching a complete and consistent statement of what is wanted.
