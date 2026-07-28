---
type: lesson
title: "When evaluation would commit too early, turn the computation into a value and pass that instead"
figure: landin
works: [mechanical-evaluation-of-expressions]
axes: [expressiveness, primitive-count, verifiability]
subdomains: [programming-languages-and-semantics, foundations-of-computation]
tags: [lesson]
---
# When evaluation would commit too early, turn the computation into a value and pass that instead

**Lesson:** The obstacle to expressing a conditional in a purely applicative core is that argument positions get evaluated, and the arm not taken may have no value at all. Landin's escape is to stop handing over the arms and hand over functions that would produce them. A function always denotes something — even one whose domain turns out to be empty — so wrapping the risky expression converts a possibly-nonexistent value into a definitely-existing one, and applying the chosen wrapper afterwards recovers exactly the behavior the original notation had. The scaffolding gets tidied further by letting the wrapper take an empty argument list, so nothing arbitrary has to be invented to bind.

The general shape of the move is worth separating from the example. Any time an evaluation strategy is more eager than a construct's intended meaning, the fix is not a new primitive with special evaluation rules but an extra layer of abstraction: quote the work as a function, move it around freely under the ordinary rules, and force it only where the meaning says it should happen. That is why so much later machinery — thunks, lazy fields, callbacks, deferred effects, promise-shaped APIs — is the same trick with different ergonomics. It is also why the trick keeps its power: it buys control over *when* without adding any new notion of what a value is.

The discipline this induces is to treat evaluation order as something you can encode rather than something you must suffer. When a language or a call convention forces work you wanted conditional, ask what would happen if the work were a value. The corollary is worth holding too: every such wrapper is a place where the timing of computation is now under someone's explicit control, so it is also a place where the timing can be got wrong. Cheap to add, but each one moves a decision from the language's rules into your program's, and you own it thereafter.

**Source:** [The Mechanical Evaluation of Expressions](../works/mechanical-evaluation-of-expressions.md) — the treatment of conditional expressions, where an index-selection rendering is rejected and replaced by one that abstracts each arm into a function, then applies the selected one.
