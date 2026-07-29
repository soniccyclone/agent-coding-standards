---
type: lesson
title: "Put the variety in the composable layer"
figure: strachey
works: [the-main-features-of-cpl]
axes: [expressiveness, primitive-count, cognitive-load]
subdomains: [programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# Put the variety in the composable layer

**Lesson:** A language, or any system with a layered notation, usually has one layer whose pieces nest freely inside each other and another whose pieces only sit in sequence. Growth can go into either layer, and the choice decides how the system ages. Add a new sequential form and you have added a thing that must be learned, matched against every other sequential form, and given its own rules for how it interacts with the rest. Add a new kind of nestable piece and you have added something that combines with everything already there for free, because composition was the layer's job from the start.

CPL's designers took the second route deliberately: keep the stock of command forms very small and let the expression grammar carry the language's richness, so that new capability arrives as new things that can appear anywhere a value can appear. The same instinct shows up in how they handled arrays. Rather than treating the shape of an array as something a declaration pronounces, they made building one an ordinary call that yields an array as a value — and that single move bought them ragged, non-rectangular structures that no declaration syntax was ever going to express, without any new statement form at all.

The rule of thumb is that a feature which can only be reached by writing a particular statement has been welded to one position in the program, while a feature that produces a value has been placed in general circulation. So when the pressure to extend arrives, ask which layer the extension can live in before asking what it should look like. If a capability is only available through a dedicated form of statement, that is usually a sign it was put in the wrong layer, and the cost shows up later as the special cases needed to let it interact with everything else.

A programmer who believes this stops reaching for new syntax as the default response to a missing capability. They look first for a way to express the thing as a value produced by ordinary machinery, and they treat a growing list of statement forms — or of configuration blocks, or of framework lifecycle hooks — as evidence that variety has been accumulating in the layer that cannot compose it.

**Source:** [The Main Features of CPL](../works/the-main-features-of-cpl.md) — the design goal stated at the end of the section on program structure, that the language's power comes from many kinds of expression combined within very few basic command forms, and the section on arrays, where storage creation is made a function yielding an array expression rather than part of a declaration.
