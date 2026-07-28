---
type: lesson
title: "When a cost cannot be derived or afforded, sample it: one weighted traversal estimates a structure you can never build"
figure: knuth
works: [estimating-the-efficiency-of-backtrack-programs]
axes: [verifiability, cognitive-load]
subdomains: [algorithms-and-complexity, formal-methods-and-verification]
tags: [lesson]
---
# When a cost cannot be derived or afforded, sample it: one weighted traversal estimates a structure you can never build

**Lesson:** The situation this paper opens in is one every programmer eventually meets and few handle well. A search program's running time depends entirely on how much of its space gets cut away by tests along the way, and how much gets cut away depends on the data in ways nobody can see by reading the code. Knuth describes waiting overnight on such a program before working out that it would have needed a span of time longer than recorded history, and notes that the sensitivity runs in both directions and without any correlation to effort: a change that looks trivial can buy three orders of magnitude, and a change that looks like a serious improvement can make things ten times worse. So the usual two options are both unavailable. You cannot derive the cost, because it depends on structure you have no closed form for, and you cannot measure it by running the thing, because running it to completion is the very expense you were trying to predict.

The third option is to sample. Walk one path down the search space at random, and at each step record how many alternatives were available. Multiply those branching counts together as you descend, and use the running product to weight the cost you observe locally — because the reciprocal of that product is exactly the probability that this particular walk visited that particular position, so weighting by its inverse compensates for everything you did not look at. The expectation of what you compute is then the true total, and Knuth proves it twice, once by summing over positions and once by recursion on subtrees. The move worth extracting is the general one: an aggregate over an enormous structure can be estimated from a single traversal, provided you weight what you see by how unlikely you were to see it. Nothing is materialized. No part of the structure needs to exist, be stored, or be enumerated.

What makes this more than a statistical trick is the conditions under which it works. The estimator needs almost no understanding of the problem — the pruning tests can be as intricate as you like, and the method never inspects them, only counts how many options they left standing. That is precisely why it applies where analysis fails: analysis needs to model the tests, sampling only needs to run them. It is also cheap enough to do by hand, and Knuth means that literally, recommending you do a few walks with dice before writing any code, because the process of doing it teaches you where the branching actually lives and suggests the data structures and pruning refinements you will want.

A programmer who takes this seriously changes what they do at the start of an expensive project rather than at the end. Instead of building the search and then discovering its cost, they build the cheap unbiased probe first — a partial walk, instrumented for branching factor — and get an order-of-magnitude answer before committing. The same reasoning covers query planning, crawl sizing, test-space exploration, and any workload whose total is a sum over a space too large to enumerate: measure a random path, weight by its improbability, and you have a defensible estimate of the whole.

**Source:** [Estimating the Efficiency of Backtrack Programs](../works/estimating-the-efficiency-of-backtrack-programs.md) — the motivating discussion of unpredictable search cost, the estimation algorithm that accumulates a product of branching counts along one random descent, and the two proofs that its expectation equals the true total cost.
