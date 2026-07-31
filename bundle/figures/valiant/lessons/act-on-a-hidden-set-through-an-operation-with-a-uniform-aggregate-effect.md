---
type: lesson
title: "To manipulate a collection you cannot see, find an operation whose aggregate effect is the same on every collection"
figure: valiant
works: [np-is-as-easy-as-detecting-unique-solutions]
axes: [expressiveness, cognitive-load, primitive-count]
subdomains: [algorithms-and-complexity, foundations-of-computation]
tags: [lesson]
---
# To manipulate a collection you cannot see, find an operation whose aggregate effect is the same on every collection

**Lesson:** Sometimes the object you need to reshape is not available for inspection: you know it exists, you know it lives inside some large space, and finding even one of its members is the very thing you are trying to do. The instinct is to reach for per-element control — remove each member with some probability, address them one at a time — and this instinct fails on a resource argument, because there may be exponentially many members and you can only afford to make polynomially many choices. The way out is to stop trying to name elements and instead look for a single cheap operation, drawn at random from a small family, whose effect on an *arbitrary* subset is predictable in aggregate. If a random member of the family reliably keeps about half of whatever set you point it at, you can iterate it to shrink the hidden set to a single element without ever having learned anything about the set.

The properties that make such a family useful are worth stating separately, because they are what you go shopping for. The effect must be uniform over inputs — the guarantee holds for every subset, not for subsets you have modelled, since the whole point is that the subset is unknown. The operation must be describable in few bits, so the randomness stays affordable. And it must be expressible as a constraint you can conjoin onto your existing representation, rather than as a post-hoc filter, so that the shrunken set is again an instance of the same problem you started with and the machinery can be applied again. In the classic instance all three come from linear functionals over a two-element field: a random one splits any set of vectors into near-halves, costs one vector to name, and turns into a parity constraint that the original formula language can already express.

The habit generalizes past this construction. When you cannot enumerate, ask what operations have distribution-free behavior on the thing you cannot enumerate — hashing to buckets, random projection, sampling by a rule rather than by a list. Each replaces knowledge of the object with a guarantee that holds regardless of the object. Two cautions come with it. First, the aggregate guarantee is not a per-element guarantee: you have not controlled who survives, only how many, and any argument that secretly needs a particular element to survive is unsound. Second, verify that the operation composes — iterating it must leave you in the same setting, or you have a one-shot trick rather than a mechanism.

**Source:** [NP Is as Easy as Detecting Unique Solutions](../works/np-is-as-easy-as-detecting-unique-solutions.md) — the discussion in section 2 rejecting independent per-solution removal as unaffordable with polynomially many random choices and adopting random inner products over the two-element field instead, the observation that a random such constraint splits an arbitrary solution set into roughly equal halves, and the lemma showing the constraint can be folded back into a formula of the same kind in linear time with a bijection on solutions.
