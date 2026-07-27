---
type: lesson
title: "Wherever a method says choose any, you have a family of algorithms and you will get its worst member"
figure: karp
works: [theoretical-improvements-in-algorithmic-efficiency-for-network-flow-problems]
axes: [verifiability, cognitive-load]
subdomains: [algorithms-and-complexity, software-engineering-and-architecture]
tags: [lesson]
---
# Wherever a method says choose any, you have a family of algorithms and you will get its worst member

**Lesson:** The classical method Edmonds and Karp start from is stated with a hole in it: repeatedly find some improving path and improve along it. Correctness does not depend on which path you pick, so the textbook presentation leaves the choice free, and that freedom looks like generosity. It is actually where every bad behavior lives. On a network with a handful of connections, a perverse alternation of choices turns work proportional to a small graph into work proportional to the numeric size of the capacities. Loosen the numbers to arbitrary reals and there are choice sequences that never finish at all, converging on an answer that is not even the right one. None of this is visible in the method's statement, because the statement is not one algorithm. It is a large family of algorithms sharing a correctness proof and nothing else.

The repair is to make the free choice a specified rule, and Karp's version has a detail that is worth more than the theorem it supports: pick the improving path with fewest steps, and the iteration count falls to a polynomial in the number of nodes with no dependence on the numbers at all. What is delicious is that this rule is what you get for free if you happen to expand candidates in the order you first discovered them, which is the most natural way anyone would code the search. So the good behavior was always available by accident, which explains both why practitioners rarely hit the pathology and why nobody had noticed the guarantee. Correctness resting on an accident of iteration order is exactly the sort of thing a later refactor destroys silently, since no test fails and the specification never mentioned it.

The habit is to treat every unspecified choice in a design as a variable you own, not a detail you get to ignore. Which candidate does the loop take first? What order does the queue drain in? Which of several valid plans does the optimizer emit? If the answer is "whatever falls out," then your system's performance is an emergent property of code nobody is guarding, and the assumption that the emergent behavior is the good one is untested. Write the rule down, state what it buys, and put the reason next to it, so that the next person who reorders the loop for tidiness discovers they are changing a guarantee.

**Source:** [Theoretical Improvements in Algorithmic Efficiency for Network Flow Problems](../works/theoretical-improvements-in-algorithmic-efficiency-for-network-flow-problems.md) — the first section's demonstration that the inherited labeling method degrades catastrophically under an unlucky sequence of path choices, together with the observation that the shortest-path selection rule which fixes it is simple enough to appear in an implementation unintentionally.
