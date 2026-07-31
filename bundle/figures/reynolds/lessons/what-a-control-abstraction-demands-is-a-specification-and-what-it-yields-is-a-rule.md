---
type: lesson
title: "A control abstraction demands a specification of its behaviour argument and yields the inference rule for the construct"
figure: reynolds
works: [the-craft-of-programming]
axes: [expressiveness, verifiability]
subdomains: [programming-languages-and-semantics, formal-methods-and-verification]
tags: [lesson]
---
# A control abstraction demands a specification of its behaviour argument and yields the inference rule for the construct

**Lesson:** When a component takes behaviour as an argument, the condition it imposes on that argument is not a constraint on a value — it is a specification: under these circumstances, running the supplied behaviour must achieve that. This is the piece people miss when they try to document such a component. They write down what the argument must *be* and find themselves unable to say anything useful, because the argument can be anything; what matters is what the argument must *do*, and saying that requires putting a claim about a foreign fragment into the interface. Get that right and the rest of the reasoning falls out easily. Get it wrong and the component is undocumentable.

The reward for doing it is that the component's contract turns out to be exactly the rule a language designer would have written for the construct if it had been built in. A repetition abstraction, specified honestly, states that if the supplied body preserves a relation under the supplied condition, then invoking the abstraction preserves that relation and establishes the condition — which is the loop rule, in the language, as an ordinary consequence of a declaration. This is what it means for control flow to be library code rather than syntax: not merely that you can write the shape, but that using it comes with reasoning power indistinguishable from a primitive's.

The one difference, and it is worth being precise about, is scope of validity. The built-in construct's rule is true everywhere; the abstraction's rule is true only where the declaration is in effect, because it is a fact about a particular meaning of a particular name rather than about the language. That is a smaller distinction than it looks, and it points at the real design question: whether the extra construct is worth being in the language at all, given that a declaration plus its contract buys you the same inferences over the region where you would actually use it. It also tells you what the argument's specification is doing structurally — it is the premise of the rule you are manufacturing, so choosing what to demand of the behaviour parameter is choosing what rule your abstraction will offer.

**Source:** [The Craft of Programming](../works/the-craft-of-programming.md) — Section 3.3.10's first example, the repetition procedure taking a statement parameter and a condition, where the parameter assumption is itself a specification of the supplied statement rather than a non-interference or good-variable condition, described as the key to reasoning about the procedure; the derivation of the resulting procedure assumptions by the loop axiom, with the pre- and postconditions promoted to ghost parameters of assertion type; and the closing observation that the result is similar to the axiom one would give about a repeat statement if the language provided one, except that it is not universal since it holds only in environments where the identifier has an appropriate meaning.
