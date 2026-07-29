---
type: lesson
title: "Roles are the invariant; how many objects carry them is a sizing decision"
figure: reenskaug
works: [mvc-its-past-and-present]
axes: [primitive-count, cognitive-load, expressiveness]
subdomains: [software-engineering-and-architecture, programming-environments-and-object-systems]
tags: [lesson]
---
# Roles are the invariant; how many objects carry them is a sizing decision

A decomposition that names distinct responsibilities is often mistaken for a decomposition that mandates distinct components. Reenskaug, revisiting his own most-copied structure twenty-four years later, is explicit that the responsibilities are the durable content and the component count is not: for something as small as a scrollbar one object reasonably carries all of them, for a menu two of them fuse because they are too tightly coupled to profit from a seam, and only in genuinely complex cases does each responsibility deserve its own object. The design tells you which questions must have answers, not how many files to create.

The reason this distinction gets lost is that responsibilities are invisible in code while objects are not. A reader can count classes; nobody can count responsibilities without understanding the design. So a structure originally offered as an analysis of forces hardens into a template, and teams end up paying for seams that carry no traffic — indirection, ceremony, and files whose whole content is forwarding — in order to look compliant with a picture. The cost is real and it is charged against the same budget that comprehension draws on.

Recasting the whole thing as a pattern language rather than an architecture is the corrective move, and the choice of form matters as much as the content. A pattern carries its context and the forces pushing each way, which means it also carries the conditions under which you should not apply it; a diagram of boxes carries none of that. Presenting a structure as composable patterns invites the reader to assemble the subset their situation calls for, and makes "I applied two of the eleven" a coherent thing to say instead of a confession.

A programmer who holds this reads every canonical architecture as a list of concerns to allocate, and allocates them by measured pressure — how independently the concerns actually vary, how much traffic crosses the proposed seam — rather than by fidelity to the diagram. And when publishing a structure of their own, they publish the forces alongside it, because a structure without its forces will be applied where it does not belong.

**Source:** [The Model-View-Controller (MVC): Its Past and Present](../works/mvc-its-past-and-present.md) — the framing of the whole talk as a draft pattern language of composable patterns, and specifically the forces listed under the input/output separation pattern, which enumerate the cases where one or two objects should play all the roles.
