---
type: lesson
title: "Refuse to decide what nobody asked you to decide"
figure: mcmillan
works: [symbolic-model-checking-an-approach-to-the-state-explosion-problem]
axes: [parallelizability, primitive-count, cognitive-load]
subdomains: [distributed-systems-and-concurrency, algorithms-and-complexity, formal-methods-and-verification]
tags: [lesson]
---
# Refuse to decide what nobody asked you to decide

The thesis closes with a second, unrelated attack on the same problem, and its premise is a diagnosis: for asynchronous control logic, the blowup comes almost entirely from enumerating orderings among events that have no relationship to each other. If two things are independent, then "A then B" and "B then A" are two entries in your search where the honest answer is one fact — that both happened. Every such pair multiplies the work while adding nothing.

So the alternative representation simply declines to order them. Behaviour is unrolled into an acyclic structure carrying only genuine dependency, and a possible partial run is any downward-closed, conflict-free subset of it. Independent events sit side by side with no relative order because none was ever established. The thesis connects this explicitly to least-commitment strategies in planning, and draws the distinction sharply: you can search the space of the problem — the configurations — or the space of solutions, and here the second space is dramatically smaller because the first one was inflated by bookkeeping.

Two details make the technique work and both are instructive. Termination comes from a cutoff criterion: stop extending past any event whose history already leads to a configuration you have represented by a smaller history, since anything reachable beyond it is reachable by a shorter route. That is a completeness argument about a pruning rule, not a heuristic, and it is what licenses the truncation. The other detail is a warning: the structure never overcommits, so it never needs to backtrack — whereas planners that greedily narrow the solution space are fast but must undo their guesses, and are therefore unfit when the goal is to exhaust the space rather than find one answer. Committing early and committing never are different engineering positions, and which is right depends on whether you need one solution or all of them.

The thesis is also careful about where this wins. It only helps when the explosion really is ordering bookkeeping; it says nothing about a system whose difficulty lies in the values it computes. And it notes that some competing partial-order methods fail on exactly these circuits because they depend on statically identifying events that cannot be disturbed, and in speed-independent logic there are none. A technique's applicability condition is part of the technique.

The transferable instinct: when work is exploding, check whether you are enumerating distinctions the question does not care about. Ordering independent events, naming anonymous things, sequencing concurrent ones — each is a commitment you may be able to simply not make, and declining to make it is often a bigger win than making it faster.

**Source:** [Symbolic Model Checking: An Approach to the State Explosion Problem](../works/symbolic-model-checking-an-approach-to-the-state-explosion-problem.md) — the final technical chapter on unfolding a net into a partially ordered structure, including the cutoff-point termination argument and the comparison with least-commitment planning.
