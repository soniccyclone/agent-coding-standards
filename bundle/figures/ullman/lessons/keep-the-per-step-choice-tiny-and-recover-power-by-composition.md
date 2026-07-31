---
type: lesson
title: "Keep the per-step choice tiny and recover power by composition"
figure: ullman
works: [mining-of-massive-datasets]
axes: [primitive-count, expressiveness]
subdomains: [algorithms-and-complexity, programming-languages-and-semantics]
tags: [lesson]
---
# Keep the per-step choice tiny and recover power by composition

**Lesson:** When a procedure has to select the best option at each step, the space of options is a design parameter, and there is a strong pull toward making it rich — allow any predicate, any function, any combination — because a richer space contains better answers. It also contains too many answers to search. An unrestricted space is not merely expensive to search; it is not searchable at all, so the procedure ends up using a heuristic that samples it, and the "best option" is then whatever the heuristic happened to find. Restricting the space to a small, enumerable family reverses that: you can evaluate every candidate and genuinely pick the best, and the guarantee is real rather than nominal.

The objection is that the restricted family cannot express what you need, and the answer is that it does not have to — the *composition* of several restricted steps does. A step that can only compare one quantity against a threshold cannot express a range, but two such steps in sequence can, and three can express something no single richer primitive was going to be designed for. Expressive power moves from the vocabulary of a single step into the structure built from many, which is a much better place for it: the vocabulary stays small enough to search exhaustively, and the structure grows only as far as the evidence supports.

There is a diagnostic benefit too. When each step is one comparison against one quantity, the resulting structure can be read: every decision is a sentence, and a decision that makes no sense is visible as a decision that makes no sense. A single step drawn from a rich family produces an object that must be trusted rather than examined, and rich families are also where the fitting-to-noise happens, since more expressive candidates find more accidental patterns.

The general habit is to be suspicious of the urge to enrich the per-step vocabulary and ask first whether a sequence of poorer steps composes to the same thing. This is the same instinct that favours a small instruction set with composition over a large one with special cases, or a handful of combinators over a large library of bespoke operations: the small vocabulary is what makes exhaustive reasoning — by a search procedure or by a person — possible at all.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the section on designing a decision-tree node in the large-scale-machine-learning chapter, which observes that the test at a node could in principle be any function of the input, that this set of possibilities is essentially infinite, and therefore restricts each node to comparing one numerical feature against a constant or testing membership of one categorical feature in a set — noting that a conjunction of two comparisons in the worked example is obtained by replacing the single node with two nodes each testing one condition.
