---
type: lesson
title: "An interface is factored correctly when a program can stand in for the user"
figure: reenskaug
works: [models-views-controllers]
axes: [verifiability, expressiveness, cognitive-load]
subdomains: [programming-environments-and-object-systems, software-engineering-and-architecture]
tags: [lesson]
---
# An interface is factored correctly when a program can stand in for the user

Most advice about separating presentation from input is unfalsifiable: you can always claim a layering is clean because "clean" has no test attached. There is a test. Take any sequence of things a person could do — point, type, choose from a menu, drag — and ask whether you could write an ordinary procedure that produces exactly the same effect by sending messages to the presentation objects, with no human present and no synthetic events. If you can, the boundary is real. If you cannot, some behavior is trapped inside the input handling, reachable only by a hand on a mouse, and no amount of naming discipline will get it out.

The reason this works as a criterion is that it converts a matter of taste into a reachability question about the message vocabulary. Behavior stuck behind a gesture is behavior with exactly one caller, and one caller that cannot be invoked by a program at that. It cannot be tested without driving the interface, cannot be scripted, cannot be replayed, cannot be reached by a different input device, and cannot be reused by a second interaction that wants the same effect for a different reason. All of those symptoms have the same cause and the same cure, so the test finds them all at once instead of one bug report at a time.

Believing this changes the order in which you build. You define the vocabulary of things that can be done to the presentation first, treating the human as merely one possible source of those messages, and only then attach input to it. Two constraints follow, and both cost something up front. The presentation must never listen for keystrokes or pointer events on its own, or the vocabulary is bypassed. And the input side must never add anything the presentation cannot express — the moment a coordinator starts drawing its own decorations across several views, there is visible behavior with no name in the vocabulary, and the substitution test fails again from the other direction.

**Source:** [Models-Views-Controllers](../works/models-views-controllers.md) — stated as a design rule in the note's controller section, alongside the paired prohibitions that a view must not know about user input and that a controller must not add presentation of its own.
