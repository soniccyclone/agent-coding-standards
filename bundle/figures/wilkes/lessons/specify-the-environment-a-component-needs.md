---
type: lesson
title: "Specify what a component requires from its environment, not only what it offers, and the call-versus-message choice becomes reversible"
figure: wilkes
works: [cambridge-cap-computer-and-its-operating-system]
axes: [expressiveness, cognitive-load, parallelizability]
subdomains: [software-engineering-and-architecture, distributed-systems-and-concurrency]
tags: [lesson]
---
# Specify what a component requires from its environment, not only what it offers, and the call-versus-message choice becomes reversible

**Lesson:** Most module specifications describe the operations a component provides and leave what it needs implicit — whatever happens to be in scope at the point it is built. Making the requirements explicit and complete, as a first-class part of the specification, changes what can be done with the component afterwards. Once a component's own resources are enumerated rather than assumed, the same component can be instantiated in a different setting by supplying that enumerated list, and the setting can be one it was never written for. Modularity that covers only the code stops at recompilation; modularity that covers the environment reaches structural rearrangement of the running system.

The sharpest instance is that the distinction between calling a service and sending it a message becomes an implementation detail rather than a commitment. To convert one into the other you construct an independent activity with the same enumerated environment the service had when it was called directly, and adjust the calling sequence — nothing about the service's logic is involved. The two organizations are duals, and the reason this is normally invisible is precisely the excess of implicit assumptions about the environment in which code may run. Remove the implicit assumptions and the duality becomes usable rather than merely true.

There is a practical corollary about interface design under this discipline. Structuring both organizations so that their code has the same shape — an initialization phase followed by an unbounded loop that dispatches on a request selector — makes the transformation mechanical rather than a rewrite. And the reason the two forms can be interchanged so cheaply is also why the decision can be deferred: the choice between them is often genuinely arbitrary at design time, depending on load and residency facts you do not have yet, so the right move is to keep it cheap to change rather than to agonize over it early.

**Source:** [The Cambridge CAP Computer and Its Operating System](../works/cambridge-cap-computer-and-its-operating-system.md) — Chapter 5's observation that the descriptor defining a component specifies not only its code and data but the environment it needs to operate correctly, making it unusually easy to substitute a service process for a service procedure by giving the new activity the same environment and changing only the calling sequence, cited as an instance of the duality of operating system structures that is usually obscured by implicit environmental assumptions; and Appendix 2's two near-identical program skeletons for the procedural and message forms, with the note that the choice between them is often arbitrary.
