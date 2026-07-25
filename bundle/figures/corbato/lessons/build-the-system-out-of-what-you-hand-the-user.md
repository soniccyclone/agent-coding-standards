---
type: lesson
title: "Build the System Out of What You Hand the User"
figure: corbato
works: [introduction-and-overview-of-the-multics-system, multics-the-first-seven-years]
axes: [primitive-count, cognitive-load, verifiability]
subdomains: [operating-systems-and-systems-programming, programming-environments-and-object-systems, software-engineering-and-architecture]
tags: [lesson]
---
# Build the System Out of What You Hand the User

**Lesson:** Multics was designed so that the operating system is written against the same facilities as the programs running on top of it. One calling sequence for everything. The same segmented virtual memory, with paging that does not distinguish supervisor pages from user pages. The same protection descriptors, arranged so that most supervisor modules run without access to privileged instructions. Corbató states the consequence bluntly: the line between system code and user code stops being architectural and becomes a question of who maintains it and what the access rules say. The seven-years paper carries the idea further out — operators, hardware maintainers and administrators turn out to be ordinary accounts holding unusual access rights, and the payoff reported is a large reduction in special-purpose control software.

Two things follow, and both are structural rather than aesthetic. First, a ceiling disappears. Because the supervisor is not a special region of memory with a fixed budget, there is no intrinsic limit on how large or capable it can become, which matters over a system's whole life as services accumulate. Second, and more important, a mechanism you are willing to build your own kernel out of is a mechanism whose defects you will find, because you are the heaviest user of it. The inverse is where the trouble lives: a privileged internal path exists outside the traffic that would exercise it, so its bugs sit undisturbed, and its existence quietly licenses the next special case.

A programmer who has absorbed this refuses to maintain a second, inward-facing version of a facility, and reads a request for an internal-only path as evidence that the public one is wrong. The test is uncomfortable and that is the point: if the interface you offer is not good enough to implement the system in, you have shipped something you would not use.

**Source:** [Introduction and Overview of the Multics System](../works/introduction-and-overview-of-the-multics-system.md) — the software design features section, where the single calling sequence, the shared paging treatment and the absence of a supervisor size limit are presented together, plus the descriptor discussion under hardware features. The seven-years paper's treatment of programmers, administrators, operators and maintainers as one uniform class of user is the mature version.
