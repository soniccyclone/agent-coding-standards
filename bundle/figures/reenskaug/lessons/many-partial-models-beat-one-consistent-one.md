---
type: lesson
title: "Let a system hold several partial models of the same reality rather than one consistent one"
figure: reenskaug
works: [thing-model-view-editor]
axes: [cognitive-load, expressiveness]
subdomains: [programming-environments-and-object-systems, software-engineering-and-architecture]
tags: [lesson]
---
# Let a system hold several partial models of the same reality rather than one consistent one

Most design instinct runs toward a single canonical representation: one schema, one object graph, one truth for each entity in the world. The competing move is to admit that a thing worth modelling — a building project, a chip, an argument — is approached by its users through several unrelated ways of thinking, and that each of those ways of thinking deserves its own representation in the machine. The scheduling view of a project and the cost view of the same project are not two slices of one grand model; they are separate abstractions that happen to be about the same subject matter, and forcing them into one structure buys unity at the cost of distorting both.

What makes this more than a preference is the accompanying claim about consistency. Perfect agreement between coexisting models is not merely expensive to implement, it is organizationally corrosive: the machinery required to keep every representation reconciled at every moment imposes a bureaucracy on the humans feeding it, and the rigidity of that bureaucracy is a worse defect than the small disagreements it eliminates. The correct target is that the whole family of models be a reasonably faithful account of the subject, not that any pair of them agree on trivia. Consistency becomes a resource to be spent where it matters instead of an invariant asserted everywhere.

A programmer who takes this seriously stops treating divergence between representations as automatically a bug to be engineered away, and starts asking which divergences actually cost something. It changes what gets built: instead of one heavyweight model with adapters hanging off it, a set of independently intelligible models, each shaped by a way its users already think, each cheap enough to add that a new way of thinking about the domain does not require renegotiating the existing ones. The cognitive win is that no one ever has to hold the union of all perspectives in mind to reason about one of them.

**Source:** [Thing-Model-View-Editor: An Example from a Planning System](../works/thing-model-view-editor.md) — the argument sits in the definition-and-comments treatment of Model, where the note works through why one subject admits many abstractions and then explicitly rejects total consistency between the resulting models as unattainable and undesirable.
