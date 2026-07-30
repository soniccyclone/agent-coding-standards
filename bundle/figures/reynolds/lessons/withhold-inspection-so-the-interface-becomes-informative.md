---
type: lesson
title: "Withhold the ability to inspect, and the interface starts telling you what the implementation must do"
figure: reynolds
works: [types-abstraction-and-parametric-polymorphism]
axes: [verifiability, expressiveness, primitive-count]
subdomains: [programming-languages-and-semantics, formal-methods-and-verification]
tags: [lesson]
---
# Withhold the ability to inspect, and the interface starts telling you what the implementation must do

**Lesson:** A generic operation can be generic in two very different ways. It can be uniform — doing one thing, blind to which type it happens to be working over — or it can be a bundle of unrelated behaviors selected by inspecting the type it was handed, adding when given numbers, disjoining when given truth values, composing when given functions. Both satisfy the same signature, and only the first supports any reasoning from the signature alone. The design move that separates them is not a check added to the type system but a capability deliberately left out of the language: provide no way to branch on a type, and the ad hoc variety becomes inexpressible rather than merely discouraged. Restraint at the level of what can be written is what converts a signature from documentation into a theorem.

The payoff is that the interface begins constraining behavior without anyone reading the implementation. Because a uniform operation cannot notice which representation it was instantiated at, it must carry corresponding inputs to corresponding outputs for *every* correspondence between representations, and the freedom to choose that correspondence adversarially squeezes the space of possible behaviors hard. This is the same mechanism that makes an opaque type definition opaque, viewed from the other end: hiding a representation behind operations and writing an operation that cannot ask about its type parameter are two faces of one property, so one argument covers both instead of each needing its own justification.

Pushed far enough, the squeeze becomes total, and this is the part with practical consequences beyond verification. Certain interfaces are so tightly constrained by uniformity that the collection of things satisfying them is forced, up to isomorphism, to be a familiar data structure — the interface consuming a value plus a way to step it is exactly the natural numbers, and an interface that accepts a combining operation and a starting point is exactly finite sequences. When that happens the concrete representation is redundant: the abstract interface is not a view onto the data, it *is* the data. A designer who notices this stops asking what representation to choose for a structure and asks instead what the smallest uniform interface is that pins it down, which is how a language ends up with fewer primitives rather than more.

**Source:** [Types, Abstraction, and Parametric Polymorphism](../works/types-abstraction-and-parametric-polymorphism.md) — the parametric-versus-ad-hoc distinction and the remark that the language deliberately provides no way to branch on types; the section deriving type opacity from the abstraction theorem; and the results in the polymorphism-semantics section showing certain low-order polymorphic types isomorphic to truth values, the natural numbers, and finite sequences.
