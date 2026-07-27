---
type: lesson
title: "Push the world's uncertainty out to the seams so that every leaf module is fully specified"
figure: lehman
works: [programs-life-cycles-and-laws-of-software-evolution]
axes: [verifiability, parallelizability, cognitive-load]
subdomains: [software-engineering-and-architecture, formal-methods-and-verification]
tags: [lesson]
---
# Push the world's uncertainty out to the seams so that every leaf module is fully specified

**Lesson:** A system whose worth is judged by the world cannot be proved correct as a whole, but that is a statement about the whole, not about its parts. Decomposition can be carried far enough that every remaining piece has a complete specification — which means the approximations, arbitrary criteria, and guesses about the world all end up expressed in the specifications and interfaces rather than smuggled into the interior of the code. Wherever a judgment about an uncertain world has been made, it is visible at a boundary as a stated assumption, and everything inside the boundary is once again a matter of satisfying a specification and can be reasoned about accordingly.

This is a design target with real force. It says nobody should begin writing a module before their task has been delimited by a specification their finished work can be checked against, and it says that when a module turns out to be wrong the repair sequence is to fix the specification first and then produce code that satisfies the corrected one — not to adjust the code and leave the specification stale. It also relocates the hardest engineering: the interesting judgment calls are in the partitioning and the interface definitions, because that is where the irreducible imprecision has been deliberately parked.

The dividend is that the parts stop needing to know about each other. A decomposition where each module is a specified transformation from inputs to outputs is a dataflow structure, and modules connected only through their declared interfaces can be executed independently, distributed onto separate machines, or replaced individually. Localizing change and enabling parallel execution turn out to be the same structural property viewed from two directions, both consequences of having made the interfaces the complete story of what a module owes its neighbors.

A programmer working this way resists two opposite temptations: treating a system as unspecifiable because its overall value is a human judgment, and pretending the whole thing can be pinned down formally. The move is to admit exactly where the world leaks in, name it at a seam, and then insist on precision everywhere else.

**Source:** [Programs, Life Cycles, and Laws of Software Evolution](../works/programs-life-cycles-and-laws-of-software-evolution.md) — the section on program structures and structural elements, which postulates that a real-world program can always be partitioned until every module is specification-derived, and draws out the interface, dataflow, and distribution consequences.
