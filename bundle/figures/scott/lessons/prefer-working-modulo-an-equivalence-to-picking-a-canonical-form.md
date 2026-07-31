---
type: lesson
title: "Prefer working modulo an equivalence to picking a canonical representative"
figure: scott
works: [data-types-as-lattices]
axes: [cognitive-load, verifiability, expressiveness]
subdomains: [foundations-of-computation, software-engineering-and-architecture, programming-languages-and-semantics]
tags: [lesson]
---
# Prefer working modulo an equivalence to picking a canonical representative

**Lesson:** Faced with several representations of what is really one thing, the reflex is to nominate a canonical form and normalize everything into it. Scott declines twice in this paper, for two different reasons, and both are worth carrying. The first is the cheap one: where there is genuinely nothing to choose between the candidates, canonicalization is effort spent to produce an arbitrary answer. He frames the alternative as a deliberate act rather than a concession — an equivalence relation makes you blind to certain distinctions, and staying a little blind can cost far less than searching for the most beautiful representative of a class whose members are all equally good. The distinction you refuse to see is one you never have to maintain, propagate, or justify.

The second reason is sharper and much easier to miss. Earlier in the paper he shows that a certain well-behavedness condition can be imposed on any object without changing its structure — for each object there is a normalized version that is structurally indistinguishable from the original — which reads exactly like a licence to assume the condition throughout. He then adds the sentence that undoes the naive reading: the map taking each object to its normalized version is not itself well behaved, not even monotone. So the assumption holds one object at a time and fails uniformly. You may always normalize a thing you are holding; you may not normalize as a step inside a computation, under a limit, or anywhere a construction has to respect the structure. Whenever you find yourself saying "without loss of generality, assume every X is normalized," the question to ask is whether the normalizing map is an operation your framework admits, because if it is not, the assumption is available only at the meta level and every use of it inside the theory is a mistake.

Both moves are trades and neither is free. Scott is explicit that working with quotients instead of plain subsets costs him something concrete — the definitions get harder, and he names the reason as an increase in quantifier complexity, which is to say the properties involved become harder to state and to check. That is the honest accounting. The claim is not that equivalence classes are always the better tool; it is that canonicalization has a price that is usually invisible, being paid in arbitrary decisions and in a normalizing operation nobody checked was legal, while the price of a quotient is visible on the first page and can therefore be weighed.

**Source:** [Data Types as Lattices](../works/data-types-as-lattices.md) — Section 7's opening account of why the total-function theory needs quotients of subsets rather than subsets, including Scott's remark that an equivalence relation makes you blind to certain distinctions and that remaining blind may cost less than choosing among indistinguishable representatives, and his statement that the loss of simplicity comes from increased quantifier complexity; together with Section 4's construction turning a non-strict retract into a strict one with an isomorphic range, and its immediate caveat that the mapping between them is neither continuous nor monotone.
