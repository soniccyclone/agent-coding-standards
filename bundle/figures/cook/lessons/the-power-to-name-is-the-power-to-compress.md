---
type: lesson
title: "The ability to name an intermediate result is not convenience, it is the difference between linear and exponential size"
figure: cook
works: [the-relative-efficiency-of-propositional-proof-systems]
axes: [expressiveness, cognitive-load, primitive-count]
subdomains: [programming-languages-and-semantics, formal-methods-and-verification]
tags: [lesson]
---
# The ability to name an intermediate result is not convenience, it is the difference between linear and exponential size

**Lesson:** Consider a construction that proceeds by repeatedly substituting a compound expression for a variable, each pass replacing a symbol with something three times its size. The number of passes may be perfectly modest, and the number of steps may stay polynomial, yet the expressions being manipulated blow up exponentially because every pass re-expands everything the previous pass built. Now add one facility: the right to introduce a fresh symbol standing for a compound expression, with a definition recorded once. The same construction proceeds with the same step count, but each expression stays small, because iterated structure is referenced rather than reproduced. Nothing about what is expressible changed. Only the size did, and it changed by an exponential.

The precise shape of the win is instructive because it is narrow. Abbreviation buys almost nothing in step count; a construction using defined symbols can be unfolded back into one that avoids them at the cost of only a modest additive increase in the number of steps, and that unfolding is exactly where the exponential size reappears. So the facility purchases compression of repeated substructure and nothing else. Once you have it, a much stronger guarantee becomes available: no intermediate expression need be more than a constant multiple of the size of the final result, which turns the whole intermediate landscape from something that could explode into something bounded by the thing you set out to establish. It also washes out surface choices that would otherwise matter, so systems differing in their base vocabulary become interchangeable once all of them can name.

This is the same phenomenon that makes a shared graph exponentially smaller than the tree it unfolds to, that makes let-binding and common subexpression elimination structural rather than cosmetic, and that separates memoized recursion from naive recursion. In each case the operation being avoided is duplication of structure under repeated substitution, and the mechanism avoiding it is a name. Whether a formalism permits naming is therefore a load-bearing question about it, not a question of taste, and asking it early is how you find out whether a representation will scale before you commit to it.

There is a second, quieter lesson in how the cost of a translation depends on the order of operations rather than only on what is being translated. Eliminating nested uses of a derived rule one at a time can double the size at every level and produce exponential growth, while eliminating all of them simultaneously stays cheap. Two encodings of the same semantic content can differ enormously in cost, so when a translation looks expensive, suspect the schedule before concluding the target lacks the power.

**Source:** [The Relative Efficiency of Propositional Proof Systems](../works/the-relative-efficiency-of-propositional-proof-systems.md) — the section motivating extended systems, where the pigeonhole argument is carried out first with iterated substitution and then again with defined atoms; the proposition showing step count is barely reduced by the extension; the theorem bounding all intermediate formula sizes by a constant multiple of the target; and the earlier discussion of simultaneous versus sequential elimination of the deduction rule.
