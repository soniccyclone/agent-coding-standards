---
type: lesson
title: "Building it is the experiment that tells you whether your separation of concerns was real"
figure: reenskaug
works: [working-with-objects-the-ooram-software-engineering-method]
axes: [verifiability, cognitive-load]
subdomains: [software-engineering-and-architecture]
tags: [lesson]
---
# Building it is the experiment that tells you whether your separation of concerns was real

**Lesson:** A decomposition always looks clean while it is still a diagram, because the diagram is where you decide what to leave out. The claim it makes — that these concerns are genuinely independent — is not testable at the level it is drawn. It becomes testable at exactly one moment: when you build the thing and find out how many places the supposedly separate parts have to know about each other. If assembling the details forces you back to reconsider the whole, that is not an implementation difficulty. It is the decomposition being falsified, and the diagram was wrong when you drew it.

This gives implementation a role most process models deny it. In a design-then-build sequence, discovering a design flaw during construction counts as expensive rework and something to be prevented by designing harder. In the view here it is the *point* of construction: the acid test that separation of concerns has to pass, with a clear pass condition — the parts interact at a few controlled places you can name — and a clear failure signal, which is having to reason about everything at once again.

There is a second, humbler version of the same idea that cuts deeper. Simple abstract descriptions are excellent at answering the questions you pose to them, and completely silent about whether you posed the right questions. Concerns you were sure were central sometimes evaporate under close examination, and things you dismissed as trivial turn out to be where the difficulty actually lives — and no amount of staring at the abstraction reveals which is which, because the abstraction was built from the same misjudgement. Only carrying the solution all the way to something that runs establishes that your original questions were the right ones. A programmer who takes this seriously stops treating an elegant model as an achievement in itself and starts treating it as a hypothesis with a scheduled experiment.

**Source:** [Working With Objects: The OOram Software Engineering Method](../works/working-with-objects-the-ooram-software-engineering-method.md) — chapter 4's introduction, which names the implementation stage the acid test of separation of concern and says something is suspicious about the models if the whole must be reconsidered while filling in details; and its later counter-examples section, where the author reports that simple models may hide the fact that the most critical questions were never found.
