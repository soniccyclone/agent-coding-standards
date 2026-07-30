---
type: lesson
title: "Refuse constructs that hide iteration, because counting loops is the only cost model you have"
figure: reynolds
works: [the-craft-of-programming]
axes: [expressiveness, cognitive-load, hardware-affinity]
subdomains: [programming-languages-and-semantics, algorithms-and-complexity]
tags: [lesson]
---
# Refuse constructs that hide iteration, because counting loops is the only cost model you have

**Lesson:** The entire practice of estimating what a program costs rests on one fragile guarantee: that the elementary steps take bounded time, so total cost is a bound on the body multiplied by the number of times around the loop. Notice how much that guarantee is doing. It holds only because no expression and no elementary operation contains an iteration of its own — because the language is low-level enough that nothing hides a loop inside what looks like a single step. The moment some innocuous-looking operation can take time proportional to the size of its data, the multiplication no longer holds and the analysis silently becomes wrong, not approximate. So the property "no construct conceals unbounded work" is not a limitation of a primitive language; it is the precondition of being able to say anything quantitative at all.

That reframes what looks like a gratuitous restriction on expressive power. The language for writing descriptions and the language for writing programs are deliberately different, and the description language is the richer one — it may quantify over sets, speak of whole structures at once, and name things that are not computable. Some of that asymmetry is forced, since no program can evaluate an arbitrary quantified claim. But part of it is chosen: quantification over finite sets *is* computable, and it is still kept out of the executable language, precisely because admitting it would introduce expressions whose evaluation time is unbounded and thereby change the character of the language. Expressive power was declined in exchange for a cost model. That is a trade worth recognizing as a trade rather than as an oversight.

Carry the principle into any system whose performance you intend to reason about. A field access that might trigger a fetch, an equality test that might walk a structure, an implicit conversion that might allocate, a property getter that might query — each is an expression concealing a loop, and each converts a straightforward count of iterations into a guess. The remedy is not to ban convenience but to keep the convenient and the costly lexically distinguishable, so that reading the code tells you where the time can go. When you do accept such a construct, you have not merely accepted some overhead; you have given up the ability to bound the enclosing loop by inspection, and you should know that you paid it.

**Source:** [The Craft of Programming](../works/the-craft-of-programming.md) — Section 1.3.5's timing analysis of the exponentiation variants, which states explicitly that the bounds on initialization and loop body exist only because neither contains an iterative construct and because the language is sufficiently low-level that there are no hidden iterations; together with Section 2.2.5's explanation that quantifiers are excluded from executable logical expressions not only because arbitrary quantified expressions cannot be evaluated but because admitting even finite quantification would introduce expressions with unbounded evaluation times.
