---
type: lesson
title: "Measure input size by what it takes to write the input down, including the precision of its numbers, or your cost bound is fiction"
figure: edmonds
works: [optimum-branchings, theoretical-improvements-in-algorithmic-efficiency-for-network-flow-problems]
axes: [hardware-affinity, verifiability]
subdomains: [algorithms-and-complexity, foundations-of-computation]
tags: [lesson]
---
# Measure input size by what it takes to write the input down, including the precision of its numbers, or your cost bound is fiction

**Lesson:** When a problem is stated over a structure — a graph, a table, a document tree — the obvious size measure is a count of structural parts, and the obvious measure is often wrong. Edmonds insists that for a weighted problem the number of significant digits in the weights has to enter the size measure alongside the number of elements, because the method's work genuinely depends on it. This is not pedantry about units. A bound stated purely in structural terms while the real cost tracks the magnitude of the data describes an algorithm nobody has, and the discrepancy shows up as a small input that runs forever.

The flow paper demonstrates the failure concretely and then repairs it. A textbook method for maximum flow is correct on integer capacities and terminates, with a bound equal to the value of the final flow; a four-node network with one unit-capacity arc and the rest set to some large integer forces that bound to be attained, so the running time is proportional to a number written in the input rather than to the input's length. Push further and the failure becomes qualitative: with capacities that are not commensurable, the sequence of improvements need not terminate at all and can converge to a non-answer. The authors' comment on the practical significance is the honest one, that finite-precision arithmetic makes the non-termination moot, and that the real message is the trend it exposes, since the number of steps grows with the precision to which the data is written.

What follows for design is a discipline about what your cost claims are quantified over. State bounds in terms of the encoded length of the input, and check separately whether a bound depends on the values in the data, on their precision, or on neither. The three cases have different consequences: a bound independent of the data is a property of your method, a bound that grows with precision is a property of your arithmetic, and a bound that grows with magnitude means you are effectively counting. The flow paper's two refinements are graded exactly this way, one giving a bound in the node count alone regardless of commensurability, the other giving a better bound in a useful range but only for integer capacities and only as a function of the flow value. Reporting which kind of bound you have is as much a part of the result as the bound itself.

**Source:** [Optimum Branchings](../works/optimum-branchings.md) — the section defining a polynomially bounded method and immediately observing that the digit count of the weights must be figured into the size measure for this problem. Also [Theoretical Improvements in Algorithmic Efficiency for Network Flow Problems](../works/theoretical-improvements-in-algorithmic-efficiency-for-network-flow-problems.md) — the worked pathological network in the opening section, the discussion of non-terminating behaviour under incommensurable capacities, and the contrast drawn between a bound in the node count alone and a bound depending on capacities.
