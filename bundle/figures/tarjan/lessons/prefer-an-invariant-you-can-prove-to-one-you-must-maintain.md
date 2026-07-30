---
type: lesson
title: "Prefer an invariant you can prove about your rules to one you have to store and enforce"
figure: tarjan
works: [fibonacci-heaps-and-their-uses-in-improved-network-optimization-algorithms]
axes: [verifiability, cognitive-load, primitive-count]
subdomains: [algorithms-and-complexity]
tags: [lesson]
---
# Prefer an invariant you can prove about your rules to one you have to store and enforce

**Lesson:** The conventional way to keep a structure efficient is to name a shape it must always have, record enough per-node bookkeeping to detect violations, and repair after every modification. Fredman and Tarjan take the opposite stance and say so directly: they place no explicit constraint on the number or the shape of the trees in the structure. Whatever regularity it has is *implicit in the operations* — a consequence of the fact that trees are only ever combined and severed in particular ways. The property their entire cost analysis depends on, that a node's subtree is exponentially large in the number of children it has, is never checked and never enforced at runtime. It is a theorem about the manipulation rules, established once on paper by an argument about the order in which children were attached and how many can subsequently be lost.

Moving an invariant from the code into the proof changes what the code costs and what it can be trusted to do, and both directions of that trade deserve to be stated. The code gets smaller and faster: no shape to validate, no rebalancing pass, no branch-heavy repair logic, and the freedom to leave the structure temporarily ragged means the common operations touch almost nothing. What you give up is per-operation predictability — an individual operation may do an unbounded amount of work, and only the total over a sequence is bounded — and you give up the ability to detect corruption locally, because there is no longer a stored condition that a consistency check could compare against. That second cost is the one people underestimate. An explicitly maintained invariant is also an assertion you can test; a derived one is only as good as the argument, and if the argument has a hole nothing in the system will notice.

The generalizable move is to ask, for every consistency condition you are about to store and police, whether it instead *follows* from restricting how the state may be changed. If the only ways to modify the state are a small set of operations, and each operation provably preserves the property, then the property needs no representation. This is why narrowing the mutation surface pays off twice: it is the same discipline that lets you claim an invariant without checking it. And when the answer is no — when an operation genuinely can break the property — the interesting question is not how to detect the breakage but how much breakage the argument can absorb before the cost analysis fails, which is the subject the next design decision in this paper turns on.

**Source:** [Fibonacci Heaps and Their Uses in Improved Network Optimization Algorithms](../works/fibonacci-heaps-and-their-uses-in-improved-network-optimization-algorithms.md) — the statement introducing the structure that no explicit constraints are placed on the number or structure of its trees and that the only constraints are implicit in how the trees are manipulated, together with the lemma and corollary that derive the exponential-size-per-rank property from the linking and cutting rules rather than from any stored condition.
