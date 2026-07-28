---
type: lesson
title: "Simplification shows up as fewer paths, not fewer lines"
figure: saltzer
works: [the-multics-kernel-design-project]
axes: [verifiability, cognitive-load, primitive-count]
subdomains: [software-engineering-and-architecture, operating-systems-and-systems-programming]
tags: [lesson]
---
# Simplification shows up as fewer paths, not fewer lines

**Lesson:** Restructuring work is routinely judged by how much code disappeared, and that
measure will usually report failure even when the work succeeded. A component reorganized
around clear ownership of its data tends to keep almost all of its operations — they were
needed before and they are needed now. What changes is the set of circumstances under which
each one can run and the set of other components that can reach into it. The code is the
same size and it is now comprehensible, because the number of distinct situations you must
consider when reasoning about any one part has collapsed. Counting lines cannot see this
at all, so a project that delivers exactly the thing that was wanted looks, by its own
headline metric, disappointing.

The corollary is to pick the measure that tracks the property you care about. If the goal
is that someone can review this and believe it, the quantities worth counting are the ones
that govern review effort: how many entry points cross the boundary, how many components
can reach a given piece of state, how many callers exist for the delicate function, how
many distinct states an operation can be invoked in. Those numbers move independently of
size, sometimes dramatically — moving a mass of code out from behind a boundary can shrink
the volume modestly while cutting the exposed interface by several times as much, and that
second number is the one that determines whether the remainder is understandable.

There is a specific and encouraging observation buried in this too: some code is complex
mostly because of where it lives. Take an algorithm out of the constrained environment that
forced it to be defensive, and it can shrink several-fold while doing the same job — the
complexity belonged to the setting, not the problem. Which means "this code is
irreducibly hairy" should always be tested by asking whether it is hairy where it currently
sits, before concluding that the task itself is hard.

**Source:** [The Multics Kernel Design Project](../works/the-multics-kernel-design-project.md)
— the size-impact section, where the memory-management redesign eliminated paths between
pieces of code rather than the code itself, where removing the dynamic linker cut a small
fraction of the code but a much larger fraction of the user-visible entry points, and where
one relocated algorithm shrank by a factor of four once it was outside the protected region.
