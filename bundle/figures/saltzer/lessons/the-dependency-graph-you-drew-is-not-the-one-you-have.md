---
type: lesson
title: "The dependency graph you drew is not the one you have"
figure: saltzer
works: [the-multics-kernel-design-project]
axes: [verifiability, cognitive-load, primitive-count]
subdomains: [operating-systems-and-systems-programming, software-engineering-and-architecture, formal-methods-and-verification]
tags: [lesson]
---
# The dependency graph you drew is not the one you have

**Lesson:** Almost every system looks cleanly layered when you stand far enough back,
because the diagram is drawn from the obvious relationships — who contains whom, who
calls whom on the ordinary path. Move closer and cycles appear, and they appear
systematically rather than by sloppiness. The useful definition of dependency is much
wider than the one people draw with: one component depends on another whenever
establishing the first's correctness requires assuming the second's. Under that
definition, a component depends on whatever stores its lookup tables, whatever holds its
own code, whatever provides the address space it runs in, and whatever schedules it —
none of which appear on a call graph, and any of which can point back upward.

The specific trap in low-level software is that a component often participates in
implementing its own execution environment, so it is a client of a service it also
provides. Application code rarely has this problem because the environment comes from
somewhere else entirely; infrastructure has it constantly. Once you accept that the
cycles are structural rather than accidental, the remedy stops being exhortation to be
tidy and becomes an enumeration: list the *categories* of dependency, walk each
component against every category, and record what turns up. Categories catch what
inspection of the call graph never will, particularly dependencies created by shared
writable state, which look like nothing at all in the code.

Why care enough to do this? Because an acyclic structure buys a specific and otherwise
unobtainable property: you can establish correctness one component at a time, each on
top of components already established. A cycle destroys that — the two members can only
be understood together, and in practice "together" grows until it swallows everything
reachable. So acyclicity is not tidiness, it is the precondition for incremental
understanding, and that is why it is worth changing a design, or even a hardware
interface, to obtain it. The typical fix is also worth knowing: cycles in the
supporting categories usually break by introducing a deliberately impoverished lower
object — fixed in number, fixed in size, always present — whose limitations are exactly
what make it safe for anyone to depend on.

**Source:** [The Multics Kernel Design Project](../works/the-multics-kernel-design-project.md)
— the type-extension rationale section with its five categories of intermodule
dependency, and the pair of figures contrasting the apparent near-linear structure of
the file system, memory, and process management code with the actual structure once
every category is accounted for.
