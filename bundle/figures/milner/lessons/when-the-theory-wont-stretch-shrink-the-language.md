---
type: lesson
title: "When the theory will not stretch, shrink the language and publish the boundary"
figure: milner
works: [a-theory-of-type-polymorphism-in-programming]
axes: [expressiveness, verifiability]
subdomains: [programming-languages-and-semantics, formal-methods-and-verification]
tags: [lesson]
---
# When the theory will not stretch, shrink the language and publish the boundary

**Lesson:** Every design eventually reaches a feature whose interaction with an existing guarantee cannot be justified. Here it is the collision between reusing a general description at several types and having mutable state hidden inside a closure: a function with a private accumulator can be handed values of one kind and then another, and the accumulator ends up holding a mixture that its description says is impossible. Two honest responses are identified — refuse to treat that description as reusable, or forbid the offending assignment pattern outright — and one is chosen for the actual language. The response that is not taken, and this is the point, is to keep the feature and quietly weaken what the guarantee is claimed to mean.

The same discipline appears in the pure fragment. Self-application is not expressible, so the fixed-point combinator built from it is rejected, and a primitive recursion form is provided instead. A higher-order function that would need its argument to be usable at two different types is rejected too. The paper names both, states that this is the main limitation, and observes that removing it would require explicit type parameters and thus confronting the question of what the types of types are — a problem it deliberately declines, wanting to see how far one gets while avoiding it. The scope was bounded on purpose, and the boundary was written down where users can see it.

The reason this is the right instinct is that a guarantee is only as valuable as its weakest documented case. A system that accepts more programs but can no longer say precisely what acceptance implies has traded something measurable for something rhetorical, and everyone downstream who optimized on the strength of the old guarantee is now wrong without knowing it. Restricting the language keeps the implication crisp; the cost lands visibly, on the programs you must rewrite, rather than invisibly, on assumptions that no longer hold.

Someone who works this way treats "the analysis cannot justify this construct" as information about the construct, not as an obstacle to route around. They keep a list of what their system deliberately cannot do and why, and they publish it. That list is what makes the guarantee trustworthy, and its absence is the clearest sign that a claimed guarantee has been eroded by accretion.

**Source:** [A Theory of Type Polymorphism in Programming](../works/a-theory-of-type-polymorphism-in-programming.md) — the extensions section's analysis of hidden assignable state inside procedures and the restriction adopted for the real language, together with the earlier passage listing untypable expressions and the decision to avoid explicit type parameters.
