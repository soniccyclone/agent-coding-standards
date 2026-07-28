---
type: lesson
title: "Organizational boundaries decide which designs are thinkable, not just which are shippable"
figure: ritchie
works: [evolution-of-the-unix-time-sharing-system]
axes: [cognitive-load, expressiveness]
subdomains: [software-engineering-and-architecture, operating-systems-and-systems-programming]
tags: [lesson]
---
# Organizational boundaries decide which designs are thinkable, not just which are shippable

**Lesson:** Ritchie tells a story against himself that is more valuable than most design advice. The redirection notation everybody associates with Unix required no invention at all: the system he had been working on previously already had general, dynamically retargetable I/O streams, and he and his colleagues used the clumsy incantation for redirecting output to a file constantly. Folding it into the command language would have been trivial there. Nobody did, and his explanation is not technical. The I/O system was maintained at one site and the command interpreter at another, so the people who felt the pain daily regarded the interpreter as somebody else's program and never considered touching it, while the people who owned the interpreter had no reason to know the pain existed. When both pieces sat under one person's control, the idea surfaced and took about an hour.

The claim is stronger than the usual observation that systems mirror the communication structure of the organizations that build them. Those boundaries did not merely make the change hard to negotiate; they made the change hard to *conceive*, because seeing it requires holding the awkward mechanism and the notation that could absorb it in the same head at the same time. A boundary that separates two components separates the two problems they jointly cause, and the joint problem then belongs to nobody. Ritchie's phrasing about the other team's program is the tell: ownership had become an epistemic limit, not just a permission limit.

The rest of the paper keeps supplying the same shape from the other direction. A file system design worked out on a blackboard by three people, a process-control scheme designed and implemented in a couple of days, a message facility retired when it stopped earning its keep — small enough scope that the whole thing could be reconsidered at once, repeatedly.

A programmer who believes this reads recurring friction between two components as evidence about the org chart and not only about the code. When a workaround has been performed by hand a thousand times without anyone proposing to remove it, they suspect the fix spans an ownership line and go looking for who would have to see both sides at once. They also treat boundaries as a real design cost when drawing them: every seam that separates people is a class of improvement that will not be imagined.

**Source:** [The Evolution of the Unix Time-sharing System](../works/evolution-of-the-unix-time-sharing-system.md) — the section on I/O redirection, where Ritchie speculates that the split between the group maintaining the I/O system and the group maintaining the shell is why the notation was never invented in the earlier system.
