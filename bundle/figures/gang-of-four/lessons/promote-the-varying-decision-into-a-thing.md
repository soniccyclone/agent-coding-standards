---
type: lesson
title: "The useful entities in a program are often its verbs, not the nouns of its problem domain"
figure: gang-of-four
works: [design-patterns-abstraction-and-reuse-of-object-oriented-design]
axes: [primitive-count, expressiveness, cognitive-load]
subdomains: [software-engineering-and-architecture, programming-environments-and-object-systems]
tags: [lesson]
---
# The useful entities in a program are often its verbs, not the nouns of its problem domain

**Lesson:** Naive object modeling maps entities in the problem domain onto entities in the program: a trading system gets an Instrument, a drawing editor gets a Shape. The patterns in this catalog do something the authors flag as a distinct mental habit — they promote things that are not domain nouns at all into first-class program entities. An algorithm becomes an object. A traversal order becomes an object. A pending request becomes an object. The responsibility for choosing what to instantiate becomes an object. None of these would ever appear in a requirements document, and the authors are explicit that a purely analysis-driven model will not produce them; they only show up in a design that has moved past the initial model in pursuit of parts that can be recombined.

The mechanical reason this pays is worth stating plainly, because it is a counting argument. Once a varying behavior is a separate object, the alternatives live in their own small units and get selected by handing one over. Once alternatives can be handed over, they can be combined at runtime, which is the difference between choosing a behavior and hard-wiring it. Refuse the promotion and the variation has to be encoded some other way, and there are only two other ways: conditionals sprayed across every site that cares, or a subclass per case. Both scale badly, and the subclass route scales worst — if two independent properties can each be present or absent, static hierarchies want a class per combination, and the class count grows multiplicatively while a composition of independent units grows additively. The authors make this point about attaching decorations to interface components, where inheritance demands a named class for every combination of border and scrollbar and the namespace fills with classes nobody deliberately designed. Additive beats multiplicative, which is a primitive-count argument in the strict sense: fewer irreducible pieces, more reachable configurations.

The reading cost moves the same direction. A behavior gathered into one named object can be understood by reading one place. The same behavior distributed across conditionals must be reassembled in the reader's head from every site that tests the flag, and no site tells you where the others are. The tradeoff is real and runs the other way too — an extra object means an extra hop of indirection, and a reader tracing control flow now steps through a forwarding layer.

A programmer who thinks this way asks, when facing a switch on kind or a family of near-identical subclasses, what concept the branching is standing in for, and considers making that concept an actual object. They read a proliferating class hierarchy as a signal that two independent properties have been fused into one axis and want separating. They stop assuming the program's vocabulary must be borrowed from the domain's.

**Source:** [Design Patterns: Abstraction and Reuse of Object-Oriented Design](../works/design-patterns-abstraction-and-reuse-of-object-oriented-design.md) — the object-jurisdiction discussion arguing composition as the strongest form of reuse, the Wrapper entry's account of combinatorial class growth under inheritance, and the observation that patterns push designers toward concepts absent from the problem domain.
