---
type: lesson
title: "Define a relation by how wrong it currently is, not by how to fix it"
figure: sutherland
works: [sketchpad-a-man-machine-graphical-communication-system-thesis]
axes: [expressiveness, verifiability, primitive-count]
subdomains: [programming-environments-and-object-systems, programming-languages-and-semantics]
tags: [lesson]
---
# Define a relation by how wrong it currently is, not by how to fix it

When you want a system to maintain a relationship among values, the tempting
specification is a repair procedure: given this relationship and these values,
here is how to move them into compliance. That specification is expensive to
write, different for every relationship, and quietly encodes assumptions about
which value gets moved. The cheaper and stronger specification is a
measurement: given these values, how far is the relationship from holding?
Nothing about repair, nothing about direction — just a scalar that is zero when
satisfied and grows as the values drift.

Two things fall out of the inversion. First, authoring gets trivial: a relation
demanding two positions share a coordinate is expressed as their difference,
and anything else computable is equally admissible, including relations that
depend on time or on state outside the model. Second, and more important, the
repair machinery becomes universal — one solver drives every relation down
toward zero, so relations compose without knowing about each other. Sutherland
learned this the hard way: his first attempt specified each relation by the
locus along which it would be satisfied, which needed bespoke work per relation
and, worse, was unstable, because a repair step could inject energy instead of
removing it. Measuring error instead of prescribing correction made monotone
decrease a property of the framework rather than a hope about each contributor.

The inversion does impose an obligation the procedural version hides: the
measurements must be commensurable. If one relation reports error on a wildly
different scale than another, the solver will chase the loud one and starve the
quiet one, and a relation that removes several degrees of freedom must report
one measurement per degree rather than a single lumped distance. So the design
work moves from writing repair logic to calibrating a shared notion of
badness — a smaller, more inspectable job that pays off across every relation
added later. A programmer who has absorbed this reaches for a residual and a
generic solver where they would previously have written a cascade of update
rules, and treats "which relation wins" as a property of the metric rather than
of the order the code happens to run in.

**Source:** [Sketchpad: A Man-Machine Graphical Communication System (PhD Thesis)](../works/sketchpad-a-man-machine-graphical-communication-system-thesis.md) — the constraint-satisfaction chapter, particularly the account of abandoning per-relation solution loci for error-computing routines, and the balance and degrees-of-freedom requirements imposed on those routines.
