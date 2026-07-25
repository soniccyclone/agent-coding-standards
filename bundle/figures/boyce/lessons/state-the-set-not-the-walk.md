---
type: lesson
title: "State the set you want, not the walk that finds it"
figure: boyce
works: [sequel-a-structured-english-query-language]
axes: [expressiveness, parallelizability]
subdomains: [databases-and-data-management]
tags: [lesson]
---
# State the set you want, not the walk that finds it

**Lesson:** Describing data element-by-element binds the program to one traversal order and one access strategy; describing it as a set binds the program only to a truth condition. When the written form says which rows qualify rather than how to visit them, the specification stops encoding an execution plan, and everything downstream benefits: the text is shorter and closer to the requirement, maintenance edits change a condition instead of restructuring a loop, and the system is left free to choose — or change — how the answer is actually computed. An unordered, side-effect-free specification is also inherently open to being evaluated in pieces: nothing in it says "one at a time," so nothing in it forbids "all at once."

The deeper habit is treating operations on whole collections as the unit of thought. Set operations compose algebraically — the result of one is a legitimate input to another — whereas loops compose only by interleaving, which entangles their state. A programmer who internalizes this reaches for the whole-collection formulation first, in any language, and treats an explicit iteration as a compilation target: something the machine derives, not something the human writes and maintains. They also recognize the cost asymmetry — the declarative form transfers the burden of finding an efficient strategy from every program author to one system implementor, which is exactly where a hard problem solved once should live.

**Source:** [SEQUEL: A Structured English Query Language](../works/sequel-a-structured-english-query-language.md) — the framing of the procedural-to-declarative evolution in the introduction and the summary's argument for set expressions over row-at-a-time iteration as the source of concision and maintainability.
