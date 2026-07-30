---
type: lesson
title: "Define a construction only on the shapes where it is clean, then reach the general case by embedding"
figure: strassen
works: [gaussian-elimination-is-not-optimal]
axes: [cognitive-load, expressiveness]
subdomains: [algorithms-and-complexity, software-engineering-and-architecture]
tags: [lesson]
---
# Define a construction only on the shapes where it is clean, then reach the general case by embedding

**Lesson:** A recursive method usually has a family of inputs on which it is exact and beautiful — sizes that split evenly all the way down — and the temptation is to complicate the method until it also handles the ragged sizes directly. That is the wrong repair. Keep the construction defined precisely where its induction is clean, and handle everything else outside it, by mapping an arbitrary input into the nearest well-shaped one, running the clean method, and reading the answer back out. The generality then costs one lemma about the embedding instead of a special case threaded through every level of a recursion, and the recursion's correctness argument stays the short one you can still follow.

The reason this is not merely tidier is that the price is provably bounded. Rounding an input up to the next convenient shape inflates it by at most a constant factor, and a constant factor is invisible to the growth law the whole construction exists to improve. So the accounting is: the messy part is confined to a wrapper whose cost is analyzed once and is asymptotically free, and the part that carries the actual result never has to mention it. Deciding what belongs inside the elegant core and what belongs in the adapter around it is a real design decision, and the criterion is whether the accommodation changes the growth law or only the constant.

The failure mode to recognize is a construction that has been generalized into incoherence — every level handling the odd case, the induction now over a statement nobody wants to read, and the central idea no longer visible in the code that implements it. When a method resists a shape of input, the first question is not how to teach it that shape but whether the shape can be manufactured away at bounded cost before the method is ever entered. Restricting a method's domain and then widening the domain by a cheap transformation is very often stronger than widening the method.

**Source:** [Gaussian Elimination is not Optimal](../works/gaussian-elimination-is-not-optimal.md) — the derivation of the general-order bound, where matrices of arbitrary order are embedded into matrices of the doubling-friendly order the recursive algorithm is defined on, and the resulting inflation is absorbed into the constant by choosing the recursion depth and block size appropriately.
