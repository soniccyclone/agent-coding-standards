---
type: lesson
title: "Who is allowed to reuse what is a structural decision, not a local one"
figure: parnas
works: [designing-software-for-ease-of-extension-and-contraction]
axes: [cognitive-load, verifiability]
subdomains: [software-engineering-and-architecture, operating-systems-and-systems-programming]
tags: [lesson]
---
# Who is allowed to reuse what is a structural decision, not a local one

Reuse is taught as an unqualified good and is therefore delegated downward: a programmer who notices an existing routine that would serve calls it, and is praised for not duplicating effort. The aggregate outcome is not obvious from any one such decision. Every unremarkable, locally correct choice adds an edge to the dependency graph, and nobody is looking at the graph. Parnas names the endpoint precisely — a system in which nothing works until everything works — and it arrives without anyone having made a decision they would defend as wrong.

The illustration is worth holding onto because it is exactly the kind of reuse that sounds most sensible. A scheduler needs somewhere to keep its data, the system already has a file system, and having the scheduler write its own storage code looks like waste. Take the shortcut and the file system must be present and correct before any scheduling can happen at all, which forecloses every configuration that wanted a system without files — and forecloses the bring-up sequence during development, where the ability to run a scheduler before a file system exists is exactly what you want. That last point matters even when no customer ever asks for the reduced configuration: the subsets you can run are the states you can test in.

So the size of the system and the interdependence of the system pull against each other, and the resolution is not a preference but a placement of authority. Which components may rely on which is a property of the design as a whole; it cannot be inferred from any local view, so it cannot be left to whoever is writing the code at the time. It must be decided deliberately, alongside the decomposition into callable pieces rather than after it, since each constrains the other. And once you are pricing the trade rather than following a slogan, some duplicated effort turns out to be the cheaper purchase — the cost of writing a small routine twice is bounded and known, while the cost of a system that cannot be brought up in pieces is neither.

**Source:** [Designing Software for Ease of Extension and Contraction](../works/designing-software-for-ease-of-extension-and-contraction.md) — the discussion of loops in the uses relation arising from leaving usage decisions to individual programmers, the scheduler-and-file-system example including its remark about development and testing, and the note that the division into callable subprograms must proceed in parallel with the uses decisions.
