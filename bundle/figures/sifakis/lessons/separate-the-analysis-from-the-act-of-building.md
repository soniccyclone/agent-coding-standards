---
type: lesson
title: "A method that must be practiced while building competes with building; one that runs on the finished artifact does not"
figure: sifakis
works: [turing-lecture-2009]
axes: [cognitive-load, verifiability]
subdomains: [software-engineering-and-architecture, formal-methods-and-verification]
tags: [lesson]
---
# A method that must be practiced while building competes with building; one that runs on the finished artifact does not

**Lesson:** Deriving a program hand in hand with its correctness argument is intellectually the better discipline, and it did not spread. The reason is structural rather than a failure of will: the proof is entangled with the act of construction, so it cannot be automated, cannot be delegated to a different person, and cannot be deferred. Every hour spent on it is an hour not spent producing the artifact, and it is charged to the same person on the same schedule. An analysis that consumes a finished description instead attaches to the process at a seam. One group produces the design, another runs the checks, and the two proceed in parallel rather than in series.

That seam also changes what "done" can mean. When correctness is welded into construction, there is no partial state to ship: either the argument closes or you have nothing. When checking is a separate activity applied to an existing artifact, a project can ship at whatever level of assurance it has reached when the deadline arrives, with the checks it did complete standing as real evidence. That is not as good as a proof, but it is a position a schedule can actually accommodate, and methods that cannot be truncated tend to lose to methods that can.

The lesson for choosing tools is to look past power to placement. Ask where in the workflow a technique attaches, whose time it spends, whether it can be handed to someone who did not write the code, and what it yields if you stop halfway. A weaker guarantee that survives contact with an organization's division of labor will do more good than a stronger one that requires the organization to be rebuilt around it.

**Source:** [Model Checking: Algorithmic Verification and Debugging](../works/turing-lecture-2009.md) — Emerson's analysis of the factors behind model checking's deployment, contrasting the non-automatable nature of proof-carrying development with the separation of system development from verification and debugging.
