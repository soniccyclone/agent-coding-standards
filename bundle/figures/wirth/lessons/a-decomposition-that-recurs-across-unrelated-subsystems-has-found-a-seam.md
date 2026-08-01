---
type: lesson
title: "A decomposition that recurs across unrelated subsystems has found a seam"
figure: wirth
works: [project-oberon]
axes: [cognitive-load, primitive-count]
subdomains: [software-engineering-and-architecture, programming-environments-and-object-systems]
tags: [lesson]
---
# A decomposition that recurs across unrelated subsystems has found a seam

**Lesson:** Any single subsystem can be cut into layers a dozen defensible ways, and arguing about which cut is right from inside that subsystem produces taste, not evidence. The evidence arrives when a second subsystem, built for entirely different content by a different route, turns out to want the same cut. If the stack that emerged for handling text — the abstract data structure, the machinery that renders it into a rectangular region, the machinery that attaches such a region to a window, and the thin layer that parses a command line and dispatches — is also the stack that emerges for handling drawings, then the layers are not an arrangement of the text problem. They are the boundaries between concerns that vary independently in this environment, and the repetition is the proof.

Two things follow from noticing it, and the second is the one usually skipped. First, the recurrence should be written down as the environment's standard shape, because a third subsystem then starts from a specification instead of from a blank page, and its author's effort goes into the content rather than into rediscovering the seam. Second — and this is what makes the template useful rather than dogmatic — every deviation from it becomes a decision that must be stated and justified rather than a silent difference. Merging two of the layers because the code that would occupy one of them is too small to be worth a module boundary is a legitimate deviation; so is threading an extra parameter through the layers because this subsystem's data refers to shared resources that text does not have. Both are worth a sentence each. What the template buys is not conformity but the ability to see a departure as a departure.

The failure mode on the other side is worth naming too: a decomposition scheme applied past the point where each part carries its own weight. Following a layering rule down to modules containing three procedures is atomization, and it costs interface surface, indirection and reader effort to buy a separation nobody will ever exercise. The rule that generates the layers is a claim about which concerns move independently; where two adjacent concerns in a particular subsystem demonstrably do not move independently, the boundary between them is ceremony. Keep the scheme, note the merge, move on.

**Source:** [Project Oberon](../works/project-oberon.md) — section 13.3's presentation of the four-module hierarchy found most appropriate in the Oberon system (base type and abstract data structure, frame handler, viewer handler, command scanner), tabulated side by side for the Draw system (Graphics, GraphicFrames, MenuViewers, Draw) and the Text system (Texts, TextFrames, MenuViewers, Edit); together with the enumerated reasons the Draw system deviates from the ideal scheme — the wish to avoid atomization into tiny modules, which merges the basic object types into the base module, and the context of fonts and libraries carried as an extra parameter by the reading and writing procedures.
