---
type: lesson
title: "The fastest route to a working model of a system is being forced to explain its failures"
figure: cutler
works: [oral-history-of-david-cutler]
axes: [cognitive-load, verifiability, hardware-affinity]
subdomains: [operating-systems-and-systems-programming, software-engineering-and-architecture]
tags: [lesson]
---
# The fastest route to a working model of a system is being forced to explain its failures

**Lesson:** Reading a system to understand it produces a shallow model, because nothing forces you to distinguish the parts you actually understand from the parts you have merely accepted. Being handed a stack of crash dumps and told to find the cause inverts that. You cannot explain why a system broke without first constructing an account of how it works, and every gap in that account announces itself immediately as a place where the trace goes cold. Comprehension arrives as a byproduct of a diagnostic obligation you cannot discharge any other way. The person who does this for a while ends up with the most reliable mental model in the building, which is why the assignment nobody wants is often the fastest apprenticeship available.

The discipline has a second, harsher half. Chasing a fault backwards through a system teaches you that the fault need not live at the layer you are searching. A defect can sit below the floor of your abstraction entirely — in the machine's timing, in a synchronizer that occasionally settles into an undecided state, in an assumption about clocks that the hardware never actually honored. A programmer who has spent months failing to find a bug in software that was never in the software carries that possibility permanently. It changes how long you are willing to keep torturing your own code before you start questioning what is underneath it, and it makes "the abstraction is lying to me" a live hypothesis rather than an excuse.

What follows practically is a preference for investigations that start from evidence rather than from theory. Collect the failures, look for the pattern across many of them rather than reasoning about one, and take seriously the possibility that the pattern's period or shape is telling you something about the physical machine rather than the program. It also argues against a common instinct: when a system is unreliable and nobody knows why, the useful response is not to make more changes but to build the account of how it works well enough that the absence in that account becomes visible.

**Source:** [Oral History of David Cutler](../works/oral-history-of-david-cutler.md) — the account of his first serious systems work, spent working through mainframe crash dumps to find why an operating system failed so often, and the much later discovery that the real cause was a hardware-level timing problem no amount of software inspection could have surfaced.
