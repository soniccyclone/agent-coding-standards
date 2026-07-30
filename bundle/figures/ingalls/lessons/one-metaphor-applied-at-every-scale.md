---
type: lesson
title: "Pick one metaphor and make it hold at every scale, so the vocabulary learned at the bottom still works at the top"
figure: ingalls
works: [design-principles-behind-smalltalk]
axes: [cognitive-load, primitive-count, expressiveness]
subdomains: [programming-languages-and-semantics, programming-environments-and-object-systems]
tags: [lesson]
---
# Pick one metaphor and make it hold at every scale, so the vocabulary learned at the bottom still works at the top

**Lesson:** The systems that stay comprehensible as they grow are the ones organized around a single structural idea that is applied without exception from the smallest unit to the largest — linked structure, or array, or communicating object, it matters less which than that it is one. The property being bought is scale invariance of understanding: a whole application is looked at the same way as the primitive it is built from, so knowledge acquired at any level transfers everywhere rather than being spent and discarded. In such a system, learning the bottom is most of the work of learning the top.

What makes the discipline hard is that the metaphor must be carried into the places where a locally better fit is available. It is always tempting to model the very smallest things one way because it is efficient and the very largest another way because it is convenient, and each such decision is defensible on its own. Their accumulation is what produces systems where every layer must be learned from scratch and where nothing composes across a boundary. The commitment is only worth making if it is genuinely uniform, which means choosing a metaphor powerful enough to survive being used where it is not the obvious choice — including at the outermost edge, where the system meets its user, since that interaction should be an instance of the same idea rather than a separate mechanism bolted on.

There is a structural reason a single metaphor buys so much, which is that it supplies a general account of what is explicit and what is implicit in any interaction. Each unit publishes a repertoire of things it will respond to, which is what one unit needs to know about another, while everything about its internal state and surrounding context stays unpublished and available to be changed. Because the same account holds at every size, the question "what may I rely on here?" has one answer rather than one per layer, and that single answer is what keeps the interdependencies from multiplying as the system grows.

**Source:** [Design Principles Behind Smalltalk](../works/design-principles-behind-smalltalk.md) — the Uniform Metaphor principle, its examples of Lisp's linked structures and APL's arrays alongside communicating objects, and the accompanying observation that the interaction between the most primitive objects is viewed the same way as the highest-level interaction between the computer and its user, with protocol as the explicit part and local state as the implicit context.
