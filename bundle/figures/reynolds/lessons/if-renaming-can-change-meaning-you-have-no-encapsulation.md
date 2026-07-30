---
type: lesson
title: "If renaming a component's internal names can change what it means, you have no encapsulation"
figure: reynolds
works: [the-craft-of-programming]
axes: [cognitive-load, expressiveness, verifiability]
subdomains: [programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# If renaming a component's internal names can change what it means, you have no encapsulation

**Lesson:** There is a single question that decides whether a naming construct genuinely hides anything: can you consistently rename everything it binds, choosing fresh names, without changing what the construct means? If yes, then a user of the component never has to know which names it uses internally, and the component's author never has to worry about which names the user has already spent. If no, then the internal names are part of the interface — an invisible part, unlisted anywhere, discovered only by collision. Treat invariance under renaming as the acid test of a binding mechanism rather than as a technicality of the semantics, because everything one usually says about encapsulation follows from it or fails with it.

The failure mode is worth understanding precisely, because it is not that a rename produces a syntax error. It is that the rename silently converts free occurrences into bound ones. Pick as the new internal name something that already occurs freely inside the region, and every one of those occurrences now refers to the local thing instead of the outer thing; the component still compiles, still runs, and now computes something else. That is why the property has to be stated as invariance of meaning and checked against the actual capture condition — you may rename to anything that does not already occur in the scope, and to nothing else. The same restriction is why substitution has to be defined carefully rather than as textual replacement, and why the careful definition is worth its complexity.

The unhappy part is that widely used systems fail this test, and they fail it not in simple cases but in the intricate ones involving procedures — which is to say, exactly where a programmer's attention is already fully committed and a name-capture bug will not be noticed. So the test is worth running against any mechanism that introduces names into a region: template expansion, macro systems, shell and configuration interpolation, dependency injection by name, dynamically scoped bindings. Ask whether a caller could break a component by choosing an unlucky identifier. If the answer is yes, then the component's documentation is obliged to publish its internal vocabulary, and the abstraction you thought you had is a convention held in place by luck.

**Source:** [The Craft of Programming](../works/the-craft-of-programming.md) — Section 1.5.2 on binding and alpha conversion, which names invariance under renaming of bound identifiers as the fundamental property of identifier binding in a well-designed language, works the example in which replacing a bound identifier by one occurring free in its scope changes the meaning, and observes that the property's failure in several popular languages arises in situations involving procedures and is a rich source of error.
