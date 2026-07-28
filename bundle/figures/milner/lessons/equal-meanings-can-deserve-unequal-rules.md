---
type: lesson
title: "Constructs with identical meaning can deserve unequal rules"
figure: milner
works: [a-theory-of-type-polymorphism-in-programming]
axes: [expressiveness, verifiability, cognitive-load]
subdomains: [programming-languages-and-semantics, formal-methods-and-verification]
tags: [lesson]
---
# Constructs with identical meaning can deserve unequal rules

**Lesson:** There is a strong instinct that a static discipline should respect the semantics: if two program forms compute the same thing, an analysis that accepts one and rejects the other looks incoherent, and the honest fix is to desugar the derived form and treat both alike. This paper does the opposite on purpose. A local binding and the immediate application of an abstraction to an argument are shown to have the same meaning under the semantics, and are then given deliberately different typing rules — the binding form is allowed to be used at several different types within its scope, the abstraction form is not. The result is a discipline that accepts programs whose semantic equals it rejects.

The justification is that a static discipline is not a description of meaning; it is an approximation, and approximations are permitted to be finer than the equivalence relation the semantics induces. What distinguishes the two forms is not what they compute but what is known at the point of analysis. In the binding form the thing being bound is present, so its full generality can be measured and then used differently at each occurrence. An abstraction, in general, appears with no argument in sight, and must therefore be checked once under an assumption that covers every future argument uniformly. Same meaning, different available information, so different affordable precision.

The rest of the design follows this same instinct about locating a restriction correctly. Generality may only be exploited for those parts of a binding's description that are independent of the enclosing parameters, because a locally defined function that closes over a parameter is genuinely tied to that parameter and pretending otherwise yields an unsound over-general description. The paper notes that in practice the distinction almost never bites — nearly always everything or nothing is independent — and that no simple syntactic rule separates the exceptions, then declines to impose a cruder rule anyway. Drawing the line at the semantically real fault rather than at the convenient common case is what makes the guarantee provable at all.

A designer who accepts this stops treating desugaring as a free move. Rewriting a surface form into a core form loses whatever the surface form told you about context, and if the analysis was exploiting that context, the rewrite silently costs expressiveness. Sugar can be load-bearing.

**Source:** [A Theory of Type Polymorphism in Programming](../works/a-theory-of-type-polymorphism-in-programming.md) — the observation accompanying the semantic equations that the local binding and the applied abstraction denote the same value yet are typed differently, together with the tagging example that motivates restricting which parts of a description may be re-instantiated.
