---
type: lesson
title: "Solve a new problem by translating it into one whose difficulty you already know"
figure: karp
works: [reducibility-among-combinatorial-problems, combinatorics-complexity-and-randomness]
axes: [cognitive-load, primitive-count]
subdomains: [algorithms-and-complexity, foundations-of-computation]
tags: [lesson]
---
# Solve a new problem by translating it into one whose difficulty you already know

**Lesson:** The default reflex when handed an unfamiliar problem is to attack it directly: study its structure, invent a method, tune the method. There is a cheaper and more powerful move available first, which is to look for a cheap, mechanical translation from the new problem into an old one. If you can convert every instance of the new problem into an instance of the old one so that the answers agree, and the conversion itself costs little, then you have inherited everything anyone knows about the old problem for free. Any method for the old problem becomes a method for the new one. Any proof that the old problem is hard becomes a proof that the new one is at least as hard.

What makes this more than a trick is that the translations compose and travel in both directions. Chained together, a handful of individually unremarkable translations connect problems that look nothing alike at the surface: covering a graph's edges, packing disjoint sets, coloring nodes, routing a tour, choosing which jobs to run, splitting a list of numbers into two equal halves. The vocabulary of each problem is domain-specific accident; the structure underneath is shared, and translation is the instrument that exposes the sharing. A field where nobody builds translations accumulates a pile of unrelated special cases. A field where everybody does accumulates a map.

The habit this installs in a working programmer is to spend the first hour on recognition rather than invention. Before writing a solver, ask what canonical problem the thing in front of you is a costume for, because if it is scheduling with side conditions, or a covering problem, or a flow problem, then decades of other people's work already applies and your job shrinks to writing the encoder and the decoder. The same reflex protects you in the other direction: when you notice that solving your ticket would also solve something famously unsolved, you have learned that no amount of cleverness on your part is the missing ingredient, and the right response is to change the requirement rather than keep grinding.

**Source:** [Reducibility Among Combinatorial Problems](../works/reducibility-among-combinatorial-problems.md) — the paper's definition of a cheap-to-compute mapping between problems and the long chain of such mappings, presented as a directed figure, that links satisfiability to twenty-one apparently unrelated combinatorial problems.
