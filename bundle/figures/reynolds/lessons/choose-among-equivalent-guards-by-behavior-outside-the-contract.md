---
type: lesson
title: "When two guards are equivalent inside the contract, choose by what they do outside it"
figure: reynolds
works: [the-craft-of-programming]
axes: [verifiability, cognitive-load]
subdomains: [software-engineering-and-architecture, formal-methods-and-verification]
tags: [lesson]
---
# When two guards are equivalent inside the contract, choose by what they do outside it

**Lesson:** A correctness argument tells you which tests are interchangeable, and it is easy to read that as saying the choice does not matter. It says the opposite. If the relation you are maintaining already bounds a counter on one side, then testing inequality against the limit and testing strict order against the limit give identical outcomes at every point the argument covers — the proof cannot distinguish them, so the proof is not where the decision gets made. The decision gets made by asking what each version does on the inputs the argument explicitly excludes. Summing an empty range makes this vivid: with the inequality test, a range whose start already exceeds its end sends the loop around forever; with the ordering test, the body never runs, the accumulator keeps its initial value, and that value happens to be the right answer for an empty range. Same proof, same code shape, one of them useless in production.

The general principle is that a precondition marks the region where you promised to be right, not the region where your code will be called. Real callers get boundaries wrong, configurations arrive empty, data sets show up with zero rows. Within the promised region all provably equivalent formulations are equally good, so spend the free choice on grace outside it. This is not the same thing as adding defensive checks: no code is being added, no branch, no cost. You are picking, among formulations you were going to write anyway, the one whose behavior degenerates into the sensible answer rather than into divergence or corruption.

There is a habit to build from this. Whenever an argument tells you that two things do not matter, treat that as a coupon rather than as permission to flip a coin — some other criterion is now free to decide, and if you do not choose deliberately, the compiler or your typing fingers will choose for you. And when you evaluate a formulation's behavior outside the contract, rank the failure modes: silently returning the right answer is best, stopping loudly is acceptable, running forever is the worst outcome available, since a nonterminating loop consumes the resources of everything around it and reports nothing. The asymmetry between those outcomes is usually far larger than any difference the proof was tracking.

**Source:** [The Craft of Programming](../works/the-craft-of-programming.md) — Section 2.2.1's array summation program, where the invariant's range information makes the two candidate while-statement tests equivalent, and the closing observation that for an initial state violating part of the precondition one test causes the program to run forever while the other terminates with the correct result for an empty segment.
