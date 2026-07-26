---
type: lesson
title: "Correctness is bought at the point of authorship, and its price scales with depth"
figure: cutler
works: [oral-history-of-david-cutler]
axes: [verifiability, cognitive-load]
subdomains: [operating-systems-and-systems-programming, software-engineering-and-architecture]
tags: [lesson]
---
# Correctness is bought at the point of authorship, and its price scales with depth

**Lesson:** Testing is a filter, not a source of correctness. A defect that leaves the
author's hands acquires cost from every subsequent stage it passes through: it consumes
someone else's debugging time, it interacts with code written on the assumption that it
works, and by the time it is reported the person best positioned to reason about it has
lost the context. The practice this argues for is treating the moment of writing as the
primary verification step, working through the paths a routine can take, including the
error paths, until you believe you can argue it is correct, and only then running it. The
run confirms the argument; it is not where the argument gets made.

The second half is the leverage claim, which is what makes this an architectural
principle rather than a personal habit. Correctness effort should not be distributed
uniformly across a system, because a defect's blast radius is a function of its depth in
the dependency graph. A wrong assumption in a low-level allocator or synchronization
primitive is inherited by every layer that builds on it, and each layer's own reasoning
becomes unsound in ways its authors cannot see. Consequently, quality cannot be mandated
from the top of an organization onto the bottom; it has to be strongest at the bottom,
because that is where a single mistake multiplies. The corollary is that the deeper you
are working, the more of the verification burden is yours specifically, and the less any
downstream process can compensate.

The practice that operationalizes both halves is arranging matters so the author cannot
avoid their own defects. Building a system on top of the system you are building means
every crash lands on the people who caused it, immediately, in the middle of their own
work. That structural arrangement does more for defect rates than any exhortation,
because it converts a distant abstract cost into a present concrete one. The same logic
explains why an outstanding known defect is worth dropping other work to fix: its cost is
still small and still local, and both of those properties decay with time.

A programmer who believes this reads their own new code adversarially before running it,
treats a bug in their own module as an interrupt rather than a queue entry, and expects
to spend disproportionately more care per line the further down the stack they are
working.

**Source:** [Oral History of David Cutler](../works/oral-history-of-david-cutler.md) — the
discussion of mentally executing new code along all its paths before running it, the
argument that quality has to be built in from the lowest level rather than legislated
downward because low-level mistakes have high leverage upward, and the account of
developing an operating system on the machine running that operating system so the team
absorbed its own failures directly.
