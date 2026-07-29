---
type: lesson
title: "A discipline is worth exactly what it forbids"
figure: reenskaug
works: [the-common-sense-of-object-oriented-programming]
axes: [verifiability, cognitive-load, expressiveness]
subdomains: [programming-environments-and-object-systems, software-engineering-and-architecture]
tags: [lesson]
---
# A discipline is worth exactly what it forbids

Reenskaug frames the target with three nested sets. Almost all programs a machine could run are junk. A tiny fraction of those work. A tiny fraction of the ones that work are also transparent enough that a second person can read them and be convinced there is nothing wrong. That third set is the one worth aiming at, and the crucial structural point is that reaching it means giving up programs from the second set — programs that run, pass their tests, and are perfectly correct. A paradigm is therefore not a collection of things you may now do. It is a collection of things you may no longer do, and its value is measured by what it rules out.

The concrete instance in this report shows how the trade actually pays. Runtime networks of collaborating objects can in principle take any shape, and while that freedom is unrestricted no static text can describe them. So the freedom is revoked: all executions of a given system operation are required to produce networks of one shape. That single prohibition is what makes a fixed, readable description of an ephemeral runtime phenomenon possible at all. The same trade recurs wherever a static artifact is supposed to tell the truth about a dynamic one — you get the description by outlawing the variation the description cannot express, not by making the description cleverer.

Reenskaug is unusually honest about the felt experience of accepting such a bargain, using the abolition of unrestricted jumps as the precedent: at the time it looked like the removal of the very thing that gave programming its power, it was genuinely depressing, the adjustment was painful, and some years later he noticed he had stopped missing it entirely. That trajectory is worth expecting in advance, because the moment of loss is when a discipline gets abandoned, and the loss is real rather than imagined.

A programmer who holds this evaluates a proposed practice by asking what it makes impossible and whether that impossibility buys a property worth having, rather than by asking what it enables. It also inverts the usual reflex about restrictive tools: the complaint that a discipline rejects a program you know to be fine is a description of the mechanism working, not an argument against it.

**Source:** [The Common Sense of Object Oriented Programming](../works/the-common-sense-of-object-oriented-programming.md) — the introduction's nested-sets argument about programs that are useful versus programs whose correctness is evident, the constraint that all networks realizing one system operation share a topology, and the closing recollection about giving up unrestricted jumps.
