---
type: lesson
title: "Display the active interpreter at the point of interaction"
figure: wirth
works: [project-oberon]
axes: [cognitive-load, verifiability]
subdomains: [programming-environments-and-object-systems, software-engineering-and-architecture]
tags: [lesson]
---
# Display the active interpreter at the point of interaction

**Lesson:** Dispatching an input to whichever component currently owns the location it arrived at is a clean mechanism and it creates a specific hazard: the meaning of an action now depends on a selection the actor did not make and cannot see. The same gesture in two adjacent regions does two different things, and nothing in the gesture says which. The remedy is not to remove the context-dependence, which is what makes the arrangement useful, but to make the selection continuously visible — and to put the display of it on the very thing the actor is already looking at, which is the pointer or the input focus itself. Changing its appearance when the owning interpreter changes converts an invisible dispatch into a fact the actor cannot miss, and it costs nothing at the moment of action because the feedback was already there before the action began.

This matters more, not less, as composition gets richer. Where regions of different kinds sit side by side as peers, an actor might keep track of them by position alone. Once regions of one kind can be nested inside regions of another — a drawing embedded in a document, a terminal embedded in a panel — position is no longer a reliable cue for the actor, because the boundaries no longer align with anything visually prominent. The pointer's appearance is then the only cheap channel that reports the truth of the dispatch, and it should be treated as part of the interpreter's contract: a component that claims inputs in a region owes a distinct appearance while it holds them.

The general principle survives outside interactive systems. Any time behaviour is selected by an implicit ambient context — the current working directory, the active configuration profile, the environment a command will run against — the selection should be rendered where the operator's attention already is, continuously, rather than being available on request. Feedback that must be asked for is not feedback; it is a query that nobody makes precisely when they most need the answer, because they do not know that the context is not what they assume.

**Source:** [Project Oberon](../works/project-oberon.md) — section 13.8.2's frame handler, which on receiving a track message with no key depressed simply draws the cursor, using a crosshair rather than the regular arrow so as to provide immediate visual feedback that mouse actions are now interpreted by the graphics handler rather than, say, a text handler, and the observation that such feedback is helpful when graphic frames appear not only in menu viewers but as subframes of a more highly structured document frame.
