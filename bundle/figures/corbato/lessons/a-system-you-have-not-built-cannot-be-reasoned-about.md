---
type: lesson
title: "A System You Have Not Built Cannot Be Reasoned About"
figure: corbato
works: [multics-the-first-seven-years, an-experimental-time-sharing-system]
axes: [verifiability, cognitive-load]
subdomains: [software-engineering-and-architecture, operating-systems-and-systems-programming]
tags: [lesson]
---
# A System You Have Not Built Cannot Be Reasoned About

**Lesson:** The most valuable admission in the Multics retrospective is that as modules were merged into larger aggregates, the actual performance of the execution paths through the software differed grossly from what everyone had expected, and an entire unplanned phase of redesign became necessary. The authors are explicit that this was not a coding-quality problem; the programmers were good. The knowledge simply did not exist yet. Their conclusion is that when a design breaks genuinely new conceptual ground, its behavior cannot be deduced in advance and has to be obtained by running it. They also close the escape hatch: simulation does not rescue you here, because constructing a model simple enough to be cheaper than the system requires the understanding you were trying to acquire in the first place.

What they do with that conclusion is the interesting part. They reframe the first working version of a module as its first complete specification, and recommend that it get a design review before it gets debugged. Design iteration stops being an embarrassment to be minimized and becomes a scheduled activity to be budgeted, on the grounds that any system too large for one person to hold in detail will require it. They report the corroborating evidence honestly, including modules that were functionally right and performed badly, were kept in service for months anyway because everything else needed something to stand on, and then were replaced by a structurally simpler version that ran an order of magnitude faster.

The 1962 CTSS paper had already staked out the same epistemology from the other end, arguing that the point of building a prototype on inadequate contemporary hardware was that the problems of this kind of system had to be met in a running form before anyone could sensibly design the next generation. A programmer who believes this treats a plan's confidence as unrelated to its accuracy, ships the ugly running version specifically in order to learn from it, and reserves suspicion for any performance or behavior claim about a system nobody has yet operated.

**Source:** [Multics: The First Seven Years](../works/multics-the-first-seven-years.md) — the software-development history section on the unanticipated design iteration phase, including the two restated principles about module versions and periodic redesign, and the implementation-experience discussion of the variable-size storage allocation replacement. The 1962 paper's conclusion makes the prototype-as-instrument argument directly.
