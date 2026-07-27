---
type: lesson
title: "Trust only the distinctions that survive a change of machine and a change of representation"
figure: karp
works: [reducibility-among-combinatorial-problems]
axes: [hardware-affinity, primitive-count]
subdomains: [foundations-of-computation, algorithms-and-complexity]
tags: [lesson]
---
# Trust only the distinctions that survive a change of machine and a change of representation

**Lesson:** Before a category is worth reasoning with, it has to be stable under the things you do not control. Karp's development is careful about this in a way that is easy to skim past: the tractability boundary he adopts is drawn where it is drawn largely because it does not move when you change the underlying machine. Swap a single-tape tape-shuffler for a multi-tape one, or for a random-access machine, and the set of problems on the cheap side of the line is unchanged, even though every individual running time changes. Likewise for how you spell your data: represent a graph as an adjacency matrix, an incidence matrix, or a list of node pairs, pick whatever punctuation you like, and membership on the cheap side is unaffected. A distinction with that much invariance is telling you something about the problem. A distinction that flips when you switch machines was telling you about your machine.

The invariance also shows you exactly where it fails, and the exception is the instructive part. Encoding integers in unary rather than binary does change the classification, so the paper stipulates binary. That is not a bookkeeping footnote. It says that one specific representational choice, how much information a symbol of input carries, is genuinely load-bearing, while all the others were noise. Finding the small number of places where representation actually matters is the payoff of testing invariance in the first place.

For a programmer this is a general method for auditing your own abstractions and your own benchmarks. Vary the thing you believe is incidental and see what survives. If a design's advantage evaporates when the allocator changes, the cache size changes, or the serialization format changes, then you discovered a property of that environment and not of your design, and it will not follow you to production. If a property holds across all of those, you have found real structure and can build on it. The reflex is to distrust any measurement or classification you have only ever observed under one machine, one encoding, and one input scale.

**Source:** [Reducibility Among Combinatorial Problems](../works/reducibility-among-combinatorial-problems.md) — the discussion of why the polynomial-time class is unchanged across machine models and across "reasonable" encodings of a domain, together with the explicit carve-out requiring binary rather than unary integers.
