---
type: lesson
title: "Front an expensive test with a cheap one that is allowed to be wrong in only one direction"
figure: sussman
works: [structure-and-interpretation-of-computer-programs]
axes: [hardware-affinity, cognitive-load]
subdomains: [algorithms-and-complexity, software-engineering-and-architecture]
tags: [lesson]
---
# Front an expensive test with a cheap one that is allowed to be wrong in only one direction

**Lesson:** When a costly decision has to be made against every member of a large collection, the reflex is to make the decision cheaper. The more productive move is usually to leave it alone and put something in front of it: a much cheaper test that is permitted to be wrong, but only in the safe direction. It may admit things the real test would reject; it must never reject anything the real test would accept. Under that one-sided guarantee the composition is exactly as correct as the expensive test alone, because everything surviving the cheap test is still checked properly and everything eliminated was genuinely eliminable. Correctness is unaffected by how good the approximation is; only cost is. That decoupling is what makes the technique safe to apply aggressively — a mediocre prefilter costs you nothing but its own execution.

The design of such a filter is a search for a necessary condition that is easy to evaluate: some coarse feature of the candidate which must agree if the full test is to succeed. A tag, a length, a bounding region, a hash of the discriminating part, a range. The art is in choosing a feature discriminating enough to reject most of the collection, and no more, since precision beyond that point costs evaluation time without buying correctness.

The second and larger step is to notice that the cheap test's answer depends only on the candidate, not on the query. Anything depending only on the stored side can be computed when the item is stored rather than when it is searched for, and organized so that the filtering happens by lookup rather than by evaluation — the candidates whose coarse feature could possibly match are found directly, and the rest are never touched at all. This is the point at which the technique stops being a constant-factor improvement and becomes an asymptotic one, and it is a specific instance of a general habit: for every per-query computation, ask which of its inputs were already known at insertion time, and move that part backwards in time.

What makes this worth stating as a principle rather than an optimization is that it inverts a common instinct. Faced with a slow scan, people reach for a faster comparison or a parallel scan, both of which preserve the shape of doing work proportional to the collection. The one-sided prefilter changes the shape, and it does so without touching the expensive test, which usually cannot be made cheaper because it is doing something genuinely necessary. Leave the hard thing hard, and spend your effort on not calling it.

**Source:** [Structure and Interpretation of Computer Programs](../works/structure-and-interpretation-of-computer-programs.md) — chapter 4 section 4.4.2, the footnote to the stream-of-frames discussion, which observes that matching is generally very expensive so one would like to avoid applying the full matcher to every element of the data base, describes the usual arrangement as breaking the process into a fast coarse match followed by the final match with the coarse match reducing the data base to a small candidate set, notes that with care some of the coarse-matching work can be performed when the data base is constructed rather than when candidates are selected, identifies this as indexing, remarks that a vast technology is built around such schemes, and points forward to the simple-minded version of the optimization in the chapter's own implementation.
