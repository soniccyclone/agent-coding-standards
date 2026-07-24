---
type: lesson
title: "Handle all computations by ignoring them: reason from the program text, not from imagined executions"
figure: dijkstra
works: [on-the-cruelty-of-really-teaching-computer-science]
axes: [verifiability, cognitive-load]
subdomains: [formal-methods-and-verification]
tags: [lesson]
---
# Handle all computations by ignoring them: reason from the program text, not from imagined executions

**Lesson:** To establish something about every element of an enormous set, arguing element by element is hopeless; the efficient argument works from the set's definition and never mentions an individual member. A program is exactly such a definition: the claim that it meets its specification is a claim about all computations it could evoke, and that set is defined by the text. So the economical way to reason is to work on the text with its proof rules, temporarily ignoring that it can also be run. Execution is one model of the formal system, not its meaning. Mentally simulating runs, tracing this input then that one, is the element-wise argument in disguise, and its cost grows with the very state spaces that made the program worth writing.

The habits that trap people in operational reasoning are linguistic before they are technical. Speaking of code as wanting, knowing, or trying imports an agent that exists and acts in time, and once the metaphor is in place, thinking in terms of behaviors feels mandatory. The same goes for coping with the new by analogy to the familiar: analogies are serviceable across gradual change and treacherous across discontinuities, and the programmable computer is a discontinuity. Even calling a defect a "bug" quietly relocates authorship of the error from the programmer to fate. Cleaning up the vocabulary is not pedantry; it removes the frames that make weak reasoning feel natural.

The working discipline is to treat a program as one half of a conjecture whose other half is its specification, and the programmer's job as settling the conjecture by manipulation of the text. That standard is demanding, and its pedagogical form here is deliberately extreme, but the direction transfers to everyday work: whenever you catch yourself narrating an execution to convince yourself of a property, ask what statement about the text would make the narration unnecessary, and argue that instead.

**Source:** [On the Cruelty of Really Teaching Computer Science](../works/on-the-cruelty-of-really-teaching-computer-science.md) — the domino-covering argument for definition-level over element-level reasoning and its transfer to programs, flanked by the radical-novelty analysis and the case against anthropomorphic vocabulary as the enforcer of operational thinking.
