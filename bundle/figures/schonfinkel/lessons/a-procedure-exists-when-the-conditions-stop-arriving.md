---
type: lesson
title: "A procedure exists when the conditions stop arriving"
figure: schonfinkel
works: [entscheidungsproblem-der-mathematischen-logik]
axes: [verifiability, cognitive-load]
subdomains: [formal-methods-and-verification, foundations-of-computation, algorithms-and-complexity]
tags: [lesson]
---
# A procedure exists when the conditions stop arriving

The treatment of the hard case generates an unbounded sequence of requirements. For each number of individuals there is a corresponding condition on the formula, one per length, and the formula is valid over a domain of a given size exactly when all conditions up to that length hold. Left there, the account is an infinite conjunction and decides nothing. The authors then show the conditions are not independent: a longer one implies the shorter ones obtained by collapsing repeated individuals, so the early members of the sequence are consequences of later ones, and past a small starting point the whole family reduces to a finite generating set. The final page states plainly what made the method work — from a certain domain size onward, determined by the formula's quantifier type and its count of function symbols, no further condition arises.

That is the general criterion for whether a procedure exists at all, stated in terms you can check. A problem approached by accumulating necessary conditions is decidable when the accumulation saturates, and undecidable, or at least unsolved by that route, when it does not. So the interesting question is never how many conditions you have collected but whether the sequence has a fixed point, and where. Detecting saturation requires exactly what the paper supplies: an implication ordering on the conditions, so you can show that beyond some index every new member is entailed by ones already present.

The authors then do the thing that makes the result trustworthy, which is to name the limit of their own method. Saturation is confined to special formula types. There are formulas — already with only four leading quantifiers — that hold over every finite domain and fail over an infinite one, and for those the sequence of finite conditions never closes, so no amount of finite work settles them. That is where the decision problem meets the foundations of mathematics, and they say so and stop rather than gesturing at an extension. A published boundary is worth more than a published hope, because the next person can aim at it.

The habit transfers directly to iterative analyses. Abstract interpretation, dataflow fixpoints, constraint propagation, and invariant inference all run the same loop of deriving new conditions from old, and in every case the question that decides whether you have an algorithm is whether the lattice of conditions has finite height or the iteration is guaranteed to stabilize. Building such a loop without knowing which of those holds is building something that either terminates by luck or hangs on the case you did not test. And when you find that your particular construction saturates only for a restricted class of inputs, that restriction is the actual result — publish it as the boundary, not as an implementation detail.

**Source:** [Zum Entscheidungsproblem der mathematischen Logik](../works/entscheidungsproblem-der-mathematischen-logik.md) — section 4's family of cyclic-disjunction conditions indexed by length, the demonstration that longer conditions entail shorter ones so that finitely many suffice, and the concluding paragraph attributing the method's success to no new condition appearing past a computable domain size while noting formulas valid on all finite domains but not on infinite ones.
