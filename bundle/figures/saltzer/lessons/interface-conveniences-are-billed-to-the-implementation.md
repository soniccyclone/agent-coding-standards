---
type: lesson
title: "Interface conveniences are billed to the implementation"
figure: saltzer
works: [the-multics-kernel-design-project]
axes: [expressiveness, cognitive-load, hardware-affinity, primitive-count]
subdomains: [operating-systems-and-systems-programming, software-engineering-and-architecture]
tags: [lesson]
---
# Interface conveniences are billed to the implementation

**Lesson:** A large share of a system's internal complexity traces back to a very small
number of promises made at its surface, and the promises rarely look expensive when made.
Let a limit be attached anywhere in a hierarchy and reattached at will, and something deep
in the system must now search upward at the worst possible moment to find which limit
applies. Charge only for what is physically stored, and the component that reclaims space
must inspect the contents of everything it reclaims, and reading can now cause writing —
which quietly breaches a containment property that had nothing to do with billing. Let a
name be resolved without regard to whether the path to it is visible, and either a large
apparatus moves inside the trusted region or the interface has to lie in a carefully
constructed way to avoid confirming what exists.

Recognizing this changes what you do when you find complexity. The reflex is to absorb it
— refactor the tangle, encapsulate it, admit it as the price of the feature. The better
move is to walk back to the promise that generated it and renegotiate. Often a barely
perceptible narrowing of the promise collapses the internal mess: constrain when the limit
may be reattached and the frantic upward search becomes a fact fixed once and carried
along. The user-visible difference is a restriction almost nobody exercises. The internal
difference is a whole category of coupling gone. That trade is available far more often
than people look for it, because the surface and the interior are usually owned by
different people at different times, and nobody is holding both ends of the ledger.

The same reasoning runs downward as well as upward. Complexity that seems inherent to
software sometimes dissolves against a tiny change in the substrate: have the machine
distinguish two conditions it currently reports as one, and a component stops needing to
reinterpret its neighbor's data structures to tell them apart. So when a mass of internal
complexity is found, there are two directions to push and both should be tried before
accepting it — up to the promise that demanded it, and down to the platform that failed to
distinguish something. And when neither renegotiation is available, that is worth knowing
explicitly: the semantics you have chosen genuinely cost this much, which is a decision
rather than an accident.

**Source:** [The Multics Kernel Design Project](../works/the-multics-kernel-design-project.md)
— the section on complex implementations arising from simple semantics, which works through
dynamically reassignable storage quotas, a variable versus fixed number of processes, the
interaction of naming with per-object access control, and charging for physically occupied
storage, alongside the conclusion that small hardware adjustments and small semantic
variations both make large differences to internal complexity.
