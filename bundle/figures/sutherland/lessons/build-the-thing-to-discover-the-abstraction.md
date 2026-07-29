---
type: lesson
title: "Build the thing to discover the abstraction the old medium hid from you"
figure: sutherland
works: [sketchpad-a-man-machine-graphical-communication-system-thesis]
axes: [cognitive-load, expressiveness]
subdomains: [software-engineering-and-architecture, programming-environments-and-object-systems]
tags: [lesson]
---
# Build the thing to discover the abstraction the old medium hid from you

When you set out to put an established human practice onto a machine, your
model of that practice is the enemy. Decades of doing it the old way have
installed assumptions so deep they do not present themselves as assumptions —
they present themselves as what the activity *is*. Sutherland's account of this
is unusually direct: he argues that without a running system his thinking would
have stayed captive to a lifetime of drawing on paper, and that the properties
that turned out to matter most were not accuracy or speed but the ability to
rearrange without erasing, which paper simply cannot offer and therefore never
suggests. The working artifact is not a demonstration of the idea; it is the
instrument that finds the idea.

The corollary he draws about generality is harder to swallow. He describes
three successive systems, records that the general structure which made the
final one extensible arrived late, states plainly that he had to stumble to be
convinced, and admits he had been told the right answer earlier by people who
saw it before he did. He does not conclude that planning would have worked. He
concludes that a builder should either grasp generality immediately or have the
nerve to keep stumbling until they reach it. That is a claim about where design
knowledge lives: the argument for the general structure is not persuasive in the
abstract, only in the presence of the specific pain the specific structure
caused.

Two working habits follow. First, when the goal is discovery rather than
delivery, mechanize the practice early and crudely and then use it enough to
develop taste — Sutherland logged roughly a hundred hours of actual drawing
before drawing conclusions, and it is the accumulated use, not the code, that
produced the insight. Second, treat a rewrite prompted by a newly visible
abstraction as success rather than waste, and be suspicious of a design that has
never been revised, because it probably encodes the old medium's habits
untouched. What this does *not* license is generality invented in advance of
evidence: the abstractions he kept were the ones some concrete failure had
argued for.

**Source:** [Sketchpad: A Man-Machine Graphical Communication System (PhD Thesis)](../works/sketchpad-a-man-machine-graphical-communication-system-thesis.md) — the opening rationale for implementing rather than theorizing about a drawing system, and the first-person history chapter recounting three generations of the system and the late arrival of its general structure.
