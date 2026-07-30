---
type: lesson
title: "When your notion of correspondence stops working at higher order, weaken the notion rather than shrink the language"
figure: reynolds
works: [types-abstraction-and-parametric-polymorphism]
axes: [expressiveness, verifiability, primitive-count]
subdomains: [programming-languages-and-semantics, foundations-of-computation]
tags: [lesson]
---
# When your notion of correspondence stops working at higher order, weaken the notion rather than shrink the language

**Lesson:** The standard way to say that two implementations of an abstraction agree is to exhibit a structure-preserving map from one to the other: translate the inputs, apply the second implementation's operation, and you land where translating the first implementation's output would have put you. That formulation is quietly first-order. The moment an operation takes another operation as an argument, the translation between the two representations no longer induces a translation between their operation spaces — it induces only a looser correspondence, one that says which pairs of operations belong together without picking out a unique partner for each. Faced with that, there are two moves available: forbid the higher-order operations so the old machinery keeps working, or keep the operations and adopt the looser notion as primary. The second is the productive one, and the general shape of the lesson is that a preservation concept which breaks on a feature you actually want is the thing to generalize, not the feature.

What makes the weakening pay off is that the loose notion composes where the strict one did not. Fix an arbitrary correspondence at each abstract type, and every compound type gets one for free by a rule that is forced rather than invented: two functions correspond when they carry corresponding arguments to corresponding results, two aggregates when their components correspond. Because that rule is defined for arbitrary correspondences, it survives arbitrarily deep nesting of function types, which is exactly where the map-based version died. The pattern recurs far from types: whenever a notion of "same behavior" refuses to lift through a construction, check whether you were demanding uniqueness — a one-to-one translation — where mere relatedness would have sufficed.

Two further returns come from having made the weaker notion primary. First, the earlier strict notion does not disappear; it reappears as a special case, since a translation pair is just a particular correspondence, and results proved about correspondences immediately specialize to it. Second, the same slack lets you accommodate settings the strict version could not reach at all — non-injective conversions, partial information orderings, several implementations related simultaneously rather than two — by varying what you plug in rather than reproving anything. Generality bought by weakening a definition tends to be cheap in exactly this way, whereas generality bought by adding cases to a definition is not.

**Source:** [Types, Abstraction, and Parametric Polymorphism](../works/types-abstraction-and-parametric-polymorphism.md) — the argument that the algebraic view of abstract types is intrinsically first-order because a homomorphism induces only a relation, not a function, between operation spaces; the induced relational rules for function and product types; and the later sections showing the representation theorem and the multi-implementation generalizations falling out as instances.
