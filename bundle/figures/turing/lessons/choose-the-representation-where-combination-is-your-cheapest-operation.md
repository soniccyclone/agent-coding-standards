---
type: lesson
title: "Choose the representation in which combining results is your executor's cheapest operation"
figure: turing
works: [the-applications-of-probability-to-cryptography]
axes: [hardware-affinity, cognitive-load, primitive-count]
subdomains: [algorithms-and-complexity, foundations-of-computation]
tags: [lesson]
---
# Choose the representation in which combining results is your executor's cheapest operation

**Lesson:** When a computation is built by repeatedly combining many small contributions, the cost of the whole thing is dominated by the cost of the combining step, not by the cost of producing each contribution. So the first design decision is not the algorithm but the number system: pick the encoding under which the combining operator degenerates into whatever your executor already does almost for free. Multiplication of thousands of ratios is intolerable for a room of clerks; the same evidence expressed as logarithms turns the whole accumulation into addition, and addition can be done by eye, by a pencil tally, or by sliding a marked transparency over a printed table and reading off what shows through. The evidence has not changed. Its arithmetic has been relocated to a domain where the executor is strong.

The same move runs in the other direction too: a combinatorial question about how many ways a quantity decomposes into parts can be recast as a question about a coefficient in an expanded polynomial, at which point mechanical algebra replaces enumeration entirely. In both cases the pattern is identical. Identify the operation you will perform an enormous number of times, find a change of representation under which that operation becomes trivial, and pay a one-off cost — building the table, doing the expansion — to buy the transformation. Because the transformation is applied once and the cheap operation is applied constantly, the trade is almost always favorable, and it gets more favorable the larger the problem.

A programmer who believes this stops treating the numeric representation as a detail settled by the type system and starts treating it as the load-bearing design choice. It is why work moves into log space, why probabilities become additive scores, why sets become bitmasks, why coordinates get pre-transformed before a hot loop rather than inside it. The discipline is to ask, before writing the loop, what the loop's inner operation is and whether some encoding makes that operation disappear. The answer usually also collapses the number of distinct primitives the executor has to support, which is a second, quieter win: a procedure expressible entirely in table lookups and additions can be handed to a far dumber machine, or a far more tired human, than one that needs general arithmetic.

**Source:** [The Applications of Probability to Cryptography](../works/the-applications-of-probability-to-cryptography.md) — the introductory section that defines a logarithmic unit of evidence expressly so that long products become sums, together with the worked cipher problems where scoring is reduced to adding tabulated integers read through a marked overlay, and the letter-subtractor section that replaces a counting argument with the coefficients of an expanded polynomial.
