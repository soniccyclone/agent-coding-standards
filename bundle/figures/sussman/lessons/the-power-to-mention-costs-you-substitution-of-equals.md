---
type: lesson
title: "The power to mention your own expressions costs you the right to substitute equals for equals"
figure: sussman
works: [structure-and-interpretation-of-computer-programs]
axes: [expressiveness, verifiability]
subdomains: [programming-languages-and-semantics, foundations-of-computation]
tags: [lesson]
---
# The power to mention your own expressions costs you the right to substitute equals for equals

**Lesson:** Adding a way to treat an expression as an object rather than as something to evaluate is the single most leveraged feature in the book — it is what makes a program able to build and transform other programs, and everything the later interpreter chapters do rests on it. The authors introduce it and immediately flag the bill: it wrecks the ability to reason about the language in simple terms, because it destroys the principle that equal things may be swapped for one another.

The reason is worth getting exactly right, because the failure is not a bug in any implementation. Three is one plus two, and a program computing with either gets the same answer. But the *word* "three" is not the *phrase* "one plus two" — they are different objects, and any operation that inspects the object can tell. So the moment a language can hold onto expressions instead of only their values, two things that are equal as values stop being interchangeable in every context. The classic sharpened form is about knowledge: from "the evening star is Venus" you may derive "the morning star is Venus," since they name the same body; but from "John knows the evening star is Venus" you may derive nothing about what John knows of the morning star. The equality still holds. What fails is the licence to rewrite inside a context that is sensitive to how the thing was named.

The general shape: every mechanism that lets code inspect the form of something — quotation, reflection, macros, an AST-walking framework, a rule engine matching on syntax, a logging decorator that prints its argument's source, memoization keyed on an expression rather than a value — creates a region of the program where value-equality no longer authorizes substitution. Inside that region, refactorings that are unconditionally safe elsewhere (inline this constant, hoist this subexpression, replace this call with its result) become claims requiring separate proof. This is why such features feel disproportionately dangerous relative to their size: they do not add a construct so much as revoke a law that all your other reasoning silently assumed.

The practical discipline follows from that. Treat the introduction of any form-inspecting capability as drawing a boundary, and know which side of it you are on. Outside, reason equationally and refactor freely. Inside, reason about the exact objects. Trouble comes from code that pretends the boundary is not there — a supposedly pure helper that happens to reflect on its argument, or an optimizer that rewrites expressions in a language whose users can quote them. The feature is worth its price often enough that it is the foundation of the rest of the book; the mistake is to take the power without noticing which reasoning principle you just gave up in exchange.

**Source:** [Structure and Interpretation of Computer Programs](../works/structure-and-interpretation-of-computer-programs.md) - chapter 2 section 2.3.1's footnote on quotation, which states that allowing quotation in a language wreaks havoc with reasoning about the language in simple terms because it destroys the notion that equals can be substituted for equals, gives the three / one-plus-two contrast, notes that quotation is powerful precisely because it lets expressions manipulate other expressions as when writing an interpreter in Chapter 4, and works the evening-star/morning-star example through the "John knows that" context to show where the inference fails.
