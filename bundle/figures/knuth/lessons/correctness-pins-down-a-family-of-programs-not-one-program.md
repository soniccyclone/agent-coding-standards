---
type: lesson
title: "Correctness pins down a family of programs, not one program — cost is the free parameter you then choose"
figure: knuth
works: [estimating-the-efficiency-of-backtrack-programs]
axes: [verifiability, cognitive-load]
subdomains: [algorithms-and-complexity, formal-methods-and-verification]
tags: [lesson]
---
# Correctness pins down a family of programs, not one program — cost is the free parameter you then choose

**Lesson:** When Knuth abstracts backtracking away from the puzzle he opened with, the whole technique reduces to one requirement. You are looking for sequences satisfying some target condition, and to search efficiently you invent conditions on partial sequences — tests you can apply before the sequence is complete. The only thing these partial conditions must satisfy is that holding at any stage is implied by holding at the next stage, so that failing a partial test rules out every possible completion. That single implication is what makes early abandonment sound. Any collection of partial conditions with that property yields a correct search, and the argument for correctness is a short induction that does not depend on which conditions you picked.

The consequence is the interesting part: the requirement does not determine the program. It bounds a family, and the family is enormous, with the two ends explicitly visible. Take the partial conditions to be vacuously true and you have exhaustive enumeration of every candidate — correct, and useless. Take them to be the strongest possible thing, true exactly when some completion exists, and the search visits almost nothing — also correct, and equally useless, because deciding that condition at each step is the original problem again. Every practical algorithm lives strictly between these, and moving along the continuum shifts cost between two accounts that never both go down: stronger tests mean fewer positions examined and more work per position. Knuth notes that in his simple example the right point is obvious, and in general it is not.

This is a different mental model of program design from the one most people carry. The usual model is that you write a program and then, separately, try to make it faster. The model here is that correctness is a constraint that carves out a space, and design consists of locating yourself inside that space along the axis the constraint left free. It makes the trade-off explicit and it makes it enumerable, which is why the estimation technique in the same paper matters so much: given a family parameterized by pruning strength, you now have a cheap way to price several members before implementing any of them, which is otherwise impossible because the two accounts move in opposite directions and no amount of reasoning tells you which dominates.

The pattern recurs far outside search. A validation check placed earlier costs more per item and rejects more before downstream expense; a cache admission policy that thinks harder stores fewer useless things; a type system that demands more of you rules out more programs. In each case there is a soundness condition that many designs satisfy, and a continuum of how much you compute up front to avoid computing later — and in each case the mistake is to treat the design you first wrote as the algorithm rather than as one arbitrary point in a space you never explored.

**Source:** [Estimating the Efficiency of Backtrack Programs](../works/estimating-the-efficiency-of-backtrack-programs.md) — the section generalizing the technique, which states the implication condition the partial properties must satisfy, observes that it fails to determine them uniquely, and works out the weakest and strongest admissible choices and what each degenerates into.
