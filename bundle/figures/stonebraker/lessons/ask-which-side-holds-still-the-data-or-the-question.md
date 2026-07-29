---
type: lesson
title: "Ask which side holds still — the data or the question"
figure: stonebraker
works: [one-size-fits-all]
axes: [expressiveness, hardware-affinity, cognitive-load]
subdomains: [databases-and-data-management, software-engineering-and-architecture]
tags: [lesson]
---
# Ask which side holds still — the data or the question

Every system that answers questions about data has to decide which of the two is resident and which is in motion. The familiar arrangement makes the data resident: you land it, index it, durably commit it, and thereafter the questions arrive and travel across it. The inverse arrangement makes the questions resident: the interrogation is installed once as a standing structure, and the data moves through it, touched as it passes. Both arrangements can express the same computations, so the choice looks like an implementation detail. It is not. It fixes the minimum latency, decides whether durability is on the critical path, determines whether the engine pulls or is pushed, and propagates into the shape of every internal component down to the scheduler.

The reason this matters more than it appears is that the choice is usually inherited rather than made. A design tradition adopts one orientation for good reasons in its original setting — never losing what you were given is a fine reason to store first — and subsequent generations treat that orientation as the definition of the problem rather than as one answer to it. Then a workload arrives whose economics are reversed, where an arriving item is interesting for a moment and irrelevant afterwards, and the inherited orientation charges a durable write for every transient fact. The overhead is not a tuning defect; it is the resident-data assumption being billed per item.

A programmer who has internalized this asks the orientation question explicitly and early, before choosing structures. Given a workload, which population is small and stable — the set of things being asked, or the set of things being asked about? Make that one resident and let the other stream. Notice too that the two orientations do not compose cheaply inside one engine: a runtime that pulls from storage and a runtime that pushes through a standing network differ down to their control flow, so building both means building two systems and admitting it, not adding a mode flag.

**Source:** ["One Size Fits All": An Idea Whose Time Has Come and Gone](../works/one-size-fits-all.md) — the argument distinguishing store-then-query processing from processing that installs the queries and lets arriving messages flow past them, and the claim that an engine committed to one of these looks nothing like an engine committed to the other.
