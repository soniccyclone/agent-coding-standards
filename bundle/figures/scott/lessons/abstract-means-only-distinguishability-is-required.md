---
type: lesson
title: "A representation is abstract exactly when only distinguishability is required of it"
figure: scott
works: [data-types-as-lattices]
axes: [cognitive-load, expressiveness, primitive-count, verifiability]
subdomains: [programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# A representation is abstract exactly when only distinguishability is required of it

**Lesson:** When you have to represent the forms of a language — or a protocol's message kinds, or a command set — the reflex is to start with the concrete marks: keywords, tags, opcodes, discriminator fields. Scott, needing a representation of his own language's expressions in order to treat its meaning function as an ordinary computable object, defines the type of expressions as one alternative per construct and then points out that no special symbols for the constructs are needed at all, because the alternation itself already separates the cases. That is what makes the resulting description abstract, and he gives the criterion in one line: for definitions by recursion it does not matter how the distinctions are made, only that they can be made.

Take that as a test you can apply to any representation you are designing. Could every discriminating mark be replaced by a different one, throughout, with nothing above the layer that reads them needing to change? If yes, everything above that layer depends only on the case structure, which is the thing you actually meant, and it will survive a change of wire format, a re-tagging, a switch of encoding. If no, then something upstream has quietly taken a dependency on the spelling, and that dependency will surface later as a change that should have been local and was not. The word abstract is doing precise work here — it names the property of having committed to distinctions without committing to how they are drawn — rather than functioning as a compliment.

Two consequences worth keeping. First, the case structure of the representation and the case analysis of whatever consumes it should correspond one for one; Scott notes explicitly that his type equation has exactly as many alternatives as his meaning definition has clauses, and that correspondence is a cheap standing check that neither side has grown a case the other does not handle. Second, describing the forms in the same universe as the values, rather than in a separate framework off to the side, means the object that maps forms to meanings is an ordinary inhabitant of that universe — so whatever you already know about the universe applies to it for free, including whether it is computable. A description language that lives outside your system buys nothing you can reason with; one that lives inside it inherits every property you have already established.

**Source:** [Data Types as Lattices](../works/data-types-as-lattices.md) — the end of Section 4, where the abstract syntax of the modified language is given as a recursive type equation with one summand per semantic clause, Scott remarks that no special symbols for successor, application and the rest are needed because separation by cases suffices to make the distinctions and that this is why the syntax is abstract, states that for recursive definitions it does not matter how the distinctions are made so long as they can be made, and observes that treating expressions as a subset of the universal domain avoids dragging in other lattices and makes the meaning function visibly computable.
