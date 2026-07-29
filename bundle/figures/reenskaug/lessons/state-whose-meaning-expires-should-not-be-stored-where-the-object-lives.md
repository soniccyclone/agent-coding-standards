---
type: lesson
title: "State whose meaning expires with the operation must not be stored where the object lives"
figure: reenskaug
works: [the-common-sense-of-object-oriented-programming]
axes: [cognitive-load, verifiability, primitive-count]
subdomains: [programming-environments-and-object-systems, software-engineering-and-architecture]
tags: [lesson]
---
# State whose meaning expires with the operation must not be stored where the object lives

Reenskaug does a controlled experiment on himself: the same program, twice, with the same executed logic, differing only in how the code is filed. The measurable difference lands on the long-lived classes, and it lands hardest on their fields. In the conventional arrangement each domain class grows extra fields — precomputed orderings, running maxima, working collections — whose meaning exists only while one particular operation is in progress. Between operations they hold stale or meaningless values, and nothing in the class says so. The declaration outlives the meaning.

This is a more diagnostic symptom than excess code volume, because the lifetime mismatch has consequences a reader cannot see. Anyone reasoning about the class must now consider states that never occur in practice; anyone changing the operation must edit the durable class to do it, so the stable core churns for reasons unrelated to the domain; and two operations that both want scratch space are silently coupled through fields neither declared. Reenskaug notes the follow-on precisely: the layout algorithm those caches served is weak and likely to be replaced, and in one arrangement that replacement means editing a domain class, while in the other it is confined to the operation.

The corrective is to give an operation a place of its own that exists while it runs and disappears when it finishes, and to put its working state there. What remains in the entity is then only what is true of the entity whenever anyone looks. The scratch space stops being a permanent property that happens to be meaningless most of the time and becomes a local variable with a wider scope, which is what it always was.

A programmer who has absorbed this reads new fields on a long-lived type with suspicion and asks what value each one holds when nothing in particular is happening. A field with no honest answer to that question is misplaced, and the fix is not a comment explaining when it is valid but a home whose lifetime matches the value's.

**Source:** [The Common Sense of Object Oriented Programming](../works/the-common-sense-of-object-oriented-programming.md) — the side-by-side comparison of the two planning-program implementations, where the conventional version's model and view classes acquire fields that are meaningful only during one operation, and the accompanying line-count and coupling comparison.
