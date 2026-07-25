---
type: lesson
title: "Let shape decide compatibility, and seal by hiding whatever invariant the shape fails to express"
figure: cardelli
works: [structural-subtyping-and-the-notion-of-power-type, a-semantics-of-multiple-inheritance]
axes: [expressiveness, cognitive-load, verifiability]
subdomains: [programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# Let shape decide compatibility, and seal by hiding whatever invariant the shape fails to express

**Lesson:** There are two ways to decide whether one description is usable where another was expected. Either the two are related because somebody declared them to be, or they are related because of what they are made of. Declared relationships have a hidden dependency on the moment of declaration: the relation exists only inside the process, session, or compilation that performed it, and a description's meaning is tied to when it was generated. Structural relationships have no such dependency, which is what allows a value to be written down, stored, sent to another address space, and read back somewhere that never saw the original declaration and still agrees about what it is. It also delivers relatedness to several unrelated expectations at once for free, without a hierarchy someone has to design in advance, since having the required parts is not an exclusive property.

The standard objection is that unrelated things can match by accident. The reply is precise and worth internalizing as a general rule: accidental matching only causes harm when a value carries an obligation that its shape does not express. If everything true of the value is visible in its structure, a stranger who satisfies the structure is not an impostor, it is another legitimate instance. If the value maintains a promise that the structure cannot state, then no naming discipline was really protecting that promise either, and the correct response is to make the representation unavailable rather than to make the name unique. That gives an actionable test for any data design: for each invariant, ask whether it is visible in the shape, and if it is not, hide the representation behind operations. Naming as a protection mechanism is the answer to a question nobody asked.

The cost is real and specific. When compatibility follows shape, the vocabulary of labels becomes globally significant, and organizing a hierarchy means choosing names with care; conveniences for declaring intended relationships can be layered back on as notation, but they should be understood as notation rather than as the ground of the relation.

**Source:** [Structural Subtyping and the Notion of Power Type](../works/structural-subtyping-and-the-notion-of-power-type.md) — the introduction's case for structural over declared matching, with persistence across sessions given as the main advantage, and the discussion of accidental matching that reduces the problem to invariants absent from the structure. Also [A Semantics of Multiple Inheritance](../works/a-semantics-of-multiple-inheritance.md) — the inheritance idioms section, where the relation is observed to depend only on the shape of objects and to need no declaration.
