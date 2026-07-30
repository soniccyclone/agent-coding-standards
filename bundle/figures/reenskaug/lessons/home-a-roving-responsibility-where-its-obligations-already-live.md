---
type: lesson
title: "A responsibility that keeps changing owners belongs to whoever already carries its obligations"
figure: reenskaug
works: [working-with-objects-the-ooram-software-engineering-method]
axes: [cognitive-load]
subdomains: [software-engineering-and-architecture, programming-environments-and-object-systems]
tags: [lesson]
---
# A responsibility that keeps changing owners belongs to whoever already carries its obligations

**Lesson:** One duty in this architecture — coordinating a set of editors and laying them out within a screen region — had moved repeatedly across revisions. It was tried as an extra job for an existing input-handling object, and tried again as a free-standing object outside the display hierarchy entirely. Neither placement stuck. The author names the pattern rather than just reporting the churn: the responsibility was a *rover*, wandering the architecture without settling.

Recognizing that a duty is a rover is the useful diagnostic, and it has a specific meaning. It is not that the design is unfinished or that the team is indecisive. It is evidence that the duty has been characterized by what it does and not by what it is obliged to maintain, and a description of that kind gives no criterion for choosing a home, so each successive placement is decided by whatever felt convenient that month and is dislodged by the next inconvenience. Repeated relocation is therefore a signal about the description, not about the candidates, and more argument between candidates will not converge.

The resolution is to stop asking which object should do the work and ask what obligations the work entails, then hand it to whoever already owes those obligations for other reasons. Here the duty came with two: being answerable for a rectangular region of the screen, and managing a set of subordinate components. Both are exactly the obligations that the display hierarchy's container abstraction already exists to discharge — so the duty belongs to a container, and once placed there it stops moving, because the placement is now derived from the duty's nature rather than from taste. The test is falsifiable in a way the aesthetic question is not: you can enumerate what a responsibility must guarantee and check which existing abstraction already guarantees those things.

Generalized, this is a rule for reading a codebase's history as design evidence. A function or field that has moved three times is telling you something the current arrangement is not: that nobody has yet stated what invariants it is responsible for. Write those down and the correct owner is usually already present in the system, and frequently it is the abstraction that people avoided because giving it one more job felt like bloating it.

**Source:** [Working With Objects: The OOram Software Engineering Method](../works/working-with-objects-the-ooram-software-engineering-method.md) — chapter 9 section 9.6, which calls the Tool object "a rover in our architecture," reports having tried a controller in the role and having tried it as a separate object outside the VisualPart hierarchy, and settles it as a Container on the grounds that it is responsible for an area of the screen and manages a number of components.
