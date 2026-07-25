---
type: lesson
title: "Work in the narrow band where a formalism is both reasonable-about and runnable"
figure: chaitin
works: [an-invitation-to-algorithmic-information-theory, the-limits-of-mathematics]
axes: [expressiveness, cognitive-load, verifiability]
subdomains: [programming-languages-and-semantics, programming-environments-and-object-systems]
tags: [lesson]
---
# Work in the narrow band where a formalism is both reasonable-about and runnable

**Lesson:** Chaitin needed a notation he could prove theorems about and also finish real programs in, and he is explicit that most candidates fail one side or the other. The most primitive formalisms are beautiful to reason about and unusable in practice at any interesting scale. Low-level implementation languages run fast and become incomprehensible to their own author within days of being written. He settled on a stripped functional notation sitting in the overlap, small enough that its semantics can be stated and argued about, expressive enough that a few hundred lines of it does something substantial. He also wrote the same interpreter three times in three different host languages and judged the results by how the code read afterwards, which is a measurement, not a preference.

The general claim is that the choice of notation bounds which projects you can complete. It is not a matter of style downstream of the real decisions, it is one of the real decisions, made first and constraining everything after. Chaitin's earlier version of the language was cute and unusable for teaching, and the redesign that made it ordinary is what made the whole enterprise transmissible to anyone else.

The way to make the choice is to name what you must do with the artifact. Reason about it formally, hand it to a stranger, run it fast, evolve it under pressure: very few notations serve two of those well and almost none serve three. So decide which one you are sacrificing rather than discovering the sacrifice later. And note the asymmetry Chaitin found in practice: cleverness in a low-level notation buys speed and costs comprehension immediately, while restraint in a simple notation costs speed and keeps the artifact discussable for years.

**Source:** [An Invitation to Algorithmic Information Theory](../works/an-invitation-to-algorithmic-information-theory.md) - the passages explaining why a minimal combinatory formalism is unusable and a low-level one is incomprehensible, and comparing the three implementations of his interpreter by readability. The redesign of the language toward ordinariness for the sake of other people is described in the same lecture and in the language chapter of [The Limits of Mathematics](../works/the-limits-of-mathematics.md).
