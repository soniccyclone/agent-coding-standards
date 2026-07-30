---
type: lesson
title: "Finitize one dimension and evaluation stops being computation, becoming recognition"
figure: vardi
works: [on-the-complexity-of-bounded-variable-queries]
axes: [parallelizability, cognitive-load, expressiveness]
subdomains: [foundations-of-computation, algorithms-and-complexity]
tags: [lesson]
---
# Finitize one dimension and evaluation stops being computation, becoming recognition

**Lesson:** Hold the data fixed and cap the width of intermediate results, and something qualitative happens: there are now only finitely many values any subexpression can possibly denote. At that point the expression is no longer a recipe to be executed against an unbounded world; it is a term over a finite algebra, and evaluating it is a fold up its own tree where each node consults a finite composition table. The number of distinct results does not grow with the input, so nothing has to be carried between nodes except which of the finitely many results this subtree produced.

The payoff is that the problem changes fields. A syntax-directed fold with finite state is a recognition problem, and recognition of well-bracketed structure is one of the most thoroughly settled questions there is — with bounds far below anything the original framing suggested, and, because a fold over a tree has no sequential dependency between siblings, bounds that are parallel rather than merely small. Vardi gets his sharpest result here not by inventing an algorithm but by exhibiting the correspondence and then citing decades-old work on bracket languages. That is the move worth stealing: after you finitize a dimension, go looking for which already-solved class your problem has fallen into, because the change of category is the whole point.

The general habit is to notice which quantity in a cost estimate is actually unbounded, and ask what becomes finite if you pin it. When a value domain becomes finite, interpreters become table lookups, analyses become abstract interpretations that terminate by construction, caches become total, and equality of two expressions becomes decidable by evaluation rather than by proof. Deliberate finitization — bounded integers instead of arbitrary ones, an enumerated set of states instead of an open one, a closed set of message kinds instead of extensible payloads — is not just a simplification for its own sake. It is what moves a design from the class of things you reason about informally into the class of things a machine can settle.

**Source:** [On the Complexity of Bounded-Variable Queries](../works/on-the-complexity-of-bounded-variable-queries.md) — the expression-complexity section for first-order queries, which observes that a fixed database admits only finitely many relations of bounded arity, recasts a query as an expression over that finite algebra, reduces evaluation to membership in a parenthesis language built with one nonterminal per possible relation value, and inherits both the logspace/alternating-logtime upper bound and the matching hardness from the classical results on those languages.
