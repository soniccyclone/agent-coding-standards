---
type: lesson
title: "Price every feature by what its absence would cost, in a unit that lets the prices add up"
figure: ungar
works: [design-and-evaluation-of-a-high-performance-smalltalk-system]
axes: [primitive-count, hardware-affinity, verifiability]
subdomains: [operating-systems-and-systems-programming, software-engineering-and-architecture]
tags: [lesson]
---
# Price every feature by what its absence would cost, in a unit that lets the prices add up

**Lesson:** "Does this feature help?" is nearly unanswerable and always answered yes, because every feature helps something. The productive reformulation is subtractive: if this were not here, what would the system have to do instead, and what would that cost on real workloads? That question has a number attached. It forces you to write down the substitute implementation, count what it costs at the frequency the case actually occurs, and produce a figure. Two features can then be compared, and — this is the part that makes the method work — the figures can be summed, so you can price a whole subset of the design at once and ask what a stripped version would really give up.

Doing this honestly is uncomfortable, because it finds that a substantial fraction of what you built earns nothing. The pattern is consistent enough to name: a feature is clever, it makes one operation dramatically faster, it cost real design time, and it does not move the aggregate at all, because real programs do not spend their time in the operation it accelerated. Every ingredient of that pattern feels like success while you are building. Only the subtractive measurement separates the ones that carry weight from the ones that merely impressed their designer. And the ranking has a second use: it tells you what to add. If a feature you never built would have saved more than four you did build put together, that comparison is only visible when everything is denominated in the same unit.

The discipline that follows is to build the substitution analysis into the design process rather than doing it once at the end for a paper. Before adding anything, describe the workaround you would need without it, estimate the frequency of the case from measurements of real workloads rather than from a microbenchmark you chose, and multiply. If the product is small, you have learned something cheaply. It also means being willing to publish your own losers: a design report that lists which of its ideas failed is far more useful to the next designer than one that explains why each idea was good.

**Source:** [The Design and Evaluation of a High-Performance Smalltalk System](../works/design-and-evaluation-of-a-high-performance-smalltalk-system.md) — the architecture evaluation chapter and its supporting appendix, which score every hardware feature by the simulated slowdown and code growth its omission would cause, then reorder the whole feature list by that measure and separate the ones that pull their weight from the ones that do not.
