---
type: lesson
title: "Expressibility is not leverage: judge an encoding by what structure survives it, and name where it fails"
figure: stearns
works: [an-algebraic-model-for-combinatorial-problems]
axes: [expressiveness, cognitive-load]
subdomains: [algorithms-and-complexity, software-engineering-and-architecture]
tags: [lesson]
---
# Expressibility is not leverage: judge an encoding by what structure survives it, and name where it fails

**Lesson:** A sufficiently general framework can encode nearly anything, and the demonstration that it can is worth almost nothing. What the framework buys you is conditional on the encoding letting it inherit the structure of the original object — one variable per part of the input, one relation per connection between parts, so that the framework's incidence pattern simply *is* the input's. When that inheritance holds, structural results about the input transfer to the encoded problem automatically and the framework's whole apparatus becomes available. When it does not, the encoding is still formally valid and still solves the problem, but the structure has been shredded in translation and there is nothing to exploit. The value of a representation falls off as the domains it invents become more contrived, and it is entirely possible to produce a technically correct encoding of something that yields no benefit whatsoever.

Two consequences follow, and both cut against the reflex to focus on algorithms. First, the load-bearing decision in applying any general framework is the choice of representation, not the choice of method — the whole difference between leverage and futility is made before an algorithm is selected, and it is made by whoever decides what maps to what. Second, structure is a sufficient route to tractability, not a necessary one, and not a universal one: there exist problems that stay hard on inputs with the simplest possible structure, which proves the framework's leverage depends on the problem's semantics and not merely on the shape of its input. Anyone selling structural methods as a general answer to hardness is overselling, and the counterexamples are not exotic.

The third consequence is about intellectual honesty in framework design. Whether a particular awkward encoding should count as being within the framework has no formal answer — the criterion that matters, whether the encoding is natural enough to preserve the structure you wanted, is a judgement rather than a theorem. The right thing to do is say so plainly: state that the boundary is a matter of taste, describe the direction in which encodings degrade, and give examples on both sides. That is more useful to a reader than a manufactured formal criterion, because a reader deciding whether to apply the framework needs to know how to judge their own case, and the honest description of a soft boundary equips them to do that while a crisp fake one does not.

**Source:** [An Algebraic Model for Combinatorial Problems](../works/an-algebraic-model-for-combinatorial-problems.md) — the graph-problems section, which states the sufficient condition as the model inheriting the input graph's structure, works through the natural and less natural encodings of the same problem, notes that value diminishes as the invented domains become more contrived, and gives a problem that remains hard on inputs of the simplest possible structure; together with the earlier admission in the introduction that exactly which problems should count as instances of the model is a non-mathematical question and a matter of taste.
