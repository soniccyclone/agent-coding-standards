---
type: lesson
title: "The boundaries between components are inherited, not derived"
figure: stonebraker
works: [one-size-fits-all]
axes: [primitive-count, cognitive-load, hardware-affinity]
subdomains: [software-engineering-and-architecture, databases-and-data-management, operating-systems-and-systems-programming]
tags: [lesson]
---
# The boundaries between components are inherited, not derived

By the time you arrive at a mature field, the set of things a system is "made of" already exists: a store, a transport, an execution container, a loader, a server. These divisions feel principled because everyone builds against them and every vendor sells one. But the divisions were drawn by the order in which problems became urgent and by which products happened to find buyers, not by an analysis of where the seams in the problem actually lie. Treating them as given quietly imports someone else's decade-old assessment of what belongs together.

The cost of an inherited boundary is paid at every crossing, and the crossing rate is set by the workload, not by the architecture diagram. An assembly of three respectable subsystems handles a single unit of work by passing it back and forth across address spaces, reserializing it into each neighbor's preferred shape on the way through. Nothing is wrong with any component; the arrangement is what is wrong, and no amount of optimizing inside the boxes recovers what the boundaries consume. Batching hides the symptom without changing the ratio. The diagnostic question is how many times a single unit of work must cross a boundary before an answer exists — if that number is large, the factoring, not the code, is the defect.

So a programmer who believes this treats the component decomposition as a design variable of the same standing as the algorithms. Rather than asking which existing categories of software to assemble, they ask what services this workload genuinely needs and where those services must share an address space to keep the per-item cost honest. That may collapse three familiar products into one process, which will look immodest — reimplementing pieces of things that already exist — and the justification is precisely that the existing partition was never derived from this problem. The corollary is a healthy expectation of churn: as workloads change, the right factoring changes, and the current one is a snapshot rather than a taxonomy.

**Source:** ["One Size Fits All": An Idea Whose Time Has Come and Gone](../works/one-size-fits-all.md) — the section on factoring, which traces the per-message boundary crossings of the conventional three-tier assembly and then questions whether the standard decomposition of system software into products was ever optimal.
