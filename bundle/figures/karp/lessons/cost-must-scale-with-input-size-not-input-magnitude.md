---
type: lesson
title: "Cost that scales with the magnitude of your numbers rather than the size of your data is exponential in disguise"
figure: karp
works: [theoretical-improvements-in-algorithmic-efficiency-for-network-flow-problems, reducibility-among-combinatorial-problems]
axes: [hardware-affinity, verifiability]
subdomains: [algorithms-and-complexity]
tags: [lesson]
---
# Cost that scales with the magnitude of your numbers rather than the size of your data is exponential in disguise

**Lesson:** There are two different things you might mean by the size of an input, and confusing them is one of the most common ways a design's cost is misjudged. One is how much data there is: how many nodes, how many rows, how many bytes it takes to write down. The other is how large the numbers appearing in the data happen to be. Any cost bound stated in terms of the second is far worse than it looks, because a value written in digits grows exponentially in the number of digits used to write it. The inherited flow method's iteration count was bounded by the magnitude of the answer, which meant that adding a few digits of precision to unchanged inputs could multiply the work enormously while the graph stayed the same size. Karp is explicit that this shows a tendency for the work to grow with the precision the capacities are expressed to, which is the tell.

The two remedies in the paper are both instructive. The first is to eliminate the dependence outright: with the right choice rule the iteration count depends only on the number of nodes, with no reference to the numbers whatsoever, and no need to assume they are even commensurable with each other. When you can get this, take it, because a bound in the shape of the data alone is immune to whatever the values turn out to be in production. The second remedy applies when you cannot: process the numbers digit by digit from the most significant end, so the work depends on how many digits there are rather than on what they add up to. The analogy Karp draws is exact and worth keeping. The relationship between that approach and the original is the relationship between arithmetic that manipulates digits and arithmetic that counts one at a time.

The test this suggests is easy and almost nobody runs it. Hold the shape of your input fixed and scale up only the magnitudes: bigger prices, longer timeouts, larger quantities, more precision. If the runtime moves, your cost is tied to values rather than to structure, and someone will eventually hand you a legitimate input with big numbers in it and take your service down. The same reasoning is why the right question about an algorithm is whether its cost is bounded by the length of the text you would need to write the problem down, and why a procedure that loops once per unit of some quantity is a landmine even when it looks like a simple counted loop.

**Source:** [Theoretical Improvements in Algorithmic Efficiency for Network Flow Problems](../works/theoretical-improvements-in-algorithmic-efficiency-for-network-flow-problems.md) — the contrast between an iteration bound driven by the flow value and one depending only on node count, and the scaling sections whose bound is proportional to the number of binary digits in the capacities, with the arithmetic analogy drawn explicitly. The companion stipulation that integers be encoded in binary rather than unary appears in [Reducibility Among Combinatorial Problems](../works/reducibility-among-combinatorial-problems.md).
