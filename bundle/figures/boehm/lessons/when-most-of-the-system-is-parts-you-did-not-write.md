---
type: lesson
title: "When most of the system is parts you did not write, integration is the engineering"
figure: boehm
works: [a-view-of-20th-and-21st-century-software-engineering]
axes: [verifiability, cognitive-load]
subdomains: [software-engineering-and-architecture, programming-environments-and-object-systems]
tags: [lesson]
---
# When most of the system is parts you did not write, integration is the engineering

**Lesson:** The largest productivity gains Boehm can find across decades did not come from writing code faster. They came from not writing it: infrastructure that arrives already built, families of related products sharing a deliberately designed common core, components acquired rather than authored. He tracks the consequence honestly, including the part practitioners resist. If most of a system is assembled from external parts, then the dominant skills are assessment, adaptation, and integration, and the claim that the job is fundamentally about programming becomes decreasingly true for most application work.

The shift changes where risk lives, and this is the part worth generalizing. An acquired component is opaque, so you cannot reason about its interior and cannot fix its defects; it evolves on someone else's schedule and for someone else's reasons, so your system inherits a stream of changes you did not choose; support for any given release expires, so standing still is not an option either. Components differentiated to compete with each other are often mutually incompatible for exactly that reason. Consequently dependability stops being a property you establish about your code and becomes a property of the assembly plus its refresh cadence, and keeping a large collection of independently evolving parts simultaneously current becomes a permanent activity rather than a project phase. Boehm gives the cautionary case of a system delivered with a large fraction of its acquired components already unsupported.

He also notes the counter-move that pays: investment in a domain model good enough that the resulting structure has strong internal cohesion and weak coupling across boundaries, which is what makes a family of products cheap to build and evolve. The cost of that investment shows up immediately as slower first delivery and pays back on the later members of the family. And he warns that the measurement of productivity itself has to change: counting newly written lines makes an era of massive reuse look stagnant, when the honest denominator is how much capability an organization has in service.

A programmer who believes this treats dependency selection as an architectural decision with a maintenance tail rather than a convenience, budgets for continuous currency rather than one-time integration, keeps the boundary against each external part narrow enough that replacing it stays possible, and measures their own leverage by capability delivered rather than by volume authored.

**Source:** [A View of 20th and 21st Century Software Engineering](../works/a-view-of-20th-and-21st-century-software-engineering.md) — the 1980s reuse discussion including the product-line investment payoff, and the 2000s section on acquired, open source, and legacy components: their opacity, vendor-driven evolution, synchronized-refresh burden, the resulting reprioritization of skills, and the argument for changing how productivity is counted.
