---
type: lesson
title: "An operation that names two abstractions at once forces their representations to be chosen together"
figure: reynolds
works: [the-craft-of-programming]
axes: [cognitive-load, hardware-affinity]
subdomains: [software-engineering-and-architecture, algorithms-and-complexity]
tags: [lesson]
---
# An operation that names two abstractions at once forces their representations to be chosen together

**Lesson:** Write a step that combines a whole aggregate with another whole aggregate and you have created a hidden dependency between two decisions that otherwise had nothing to do with each other. To make that one step efficient, whoever chooses how the first thing is stored must already know how the second thing is stored, because the cost of merging them depends on both layouts at once. Nothing in the problem demanded this; it came in with the notation. The tell is that the step's cost function has two free variables in it, and neither of the two people who would naturally own those variables can evaluate it alone.

The repair is to replace the bulk step with a traversal of one aggregate performing an elementary step on the other. Now there are two independent obligations: implement the elementary step, which involves only the first layout, and implement the traversal, which involves only the second. Each can be settled by whoever knows the most about that side, in either order, without negotiation. This matters most exactly where you would expect — at the edges of a program, where one of the two things is produced by somebody upstream and the other is consumed by somebody downstream. A bulk operation joining an input to an output silently couples two teams' storage decisions through a line of code that mentions neither of them.

Two honesty requirements come with the technique. First, breaking a bulk operation into elements genuinely forfeits implementations that only exist at bulk scale — merging two sorted representations, unioning two bitmaps word at a time — so you are trading a class of optimizations for independence, and you should know you are making that trade rather than discover it later. Second, the argument for the rewrite is a heuristic, not a derivation. It tells you the shape of the design space and which decisions can be taken apart; it does not tell you that the decomposed version is the fastest program available. A systematic method for constructing programs is not a method for finding optimal ones, and the moment you start treating it as one it will quietly hand you a worse program with a cleaner provenance.

**Source:** [The Craft of Programming](../works/the-craft-of-programming.md) — Section 5.1.2, where the abstract reachability program's step that unions the successor set of a node into the accumulating result is replaced by an iteration over that successor set adding one node at a time, on the stated grounds that leaving the union in place would force the representation of the result set and the representation of the successor function to be chosen jointly, which is intolerable when one is an input and the other an output; together with the accompanying admission that this replacement excludes some implementations of the union and is only a heuristic argument, since data representation structuring is a systematic way of constructing programs rather than a guarantee of optimal design choices.
