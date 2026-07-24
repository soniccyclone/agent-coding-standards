---
type: lesson
title: "Reason about concurrent programs through invariants over states, never by enumerating interleavings"
figure: lamport
works: [proving-the-correctness-of-multiprocess-programs, the-part-time-parliament]
axes: [verifiability, cognitive-load]
subdomains: [formal-methods-and-verification, distributed-systems-and-concurrency]
tags: [lesson]
---

# Reason about concurrent programs through invariants over states, never by enumerating interleavings

**Lesson:** The natural way to convince yourself a concurrent program works is to walk through the ways its processes can interleave. This method is doomed: the number of execution sequences explodes, intuition samples only the few orderings a human imagines, and an algorithm as short as a mutual-exclusion loop can hide behavior that only a hostile scheduler exposes. The alternative that scales is assertional: attach a predicate to each control point, and prove one thing — that every atomic step of every process preserves the assertions. Correctness stops being a claim about all possible histories and becomes a claim about a single relation between consecutive states, checked node by node.

The structural insight that makes this practical for concurrency is interference: a process's local assertions can be invalidated by other processes' steps, so each assertion must be shown monotone (undisturbed) under everyone else's actions. Crucially, this checking can be organized so proof effort grows roughly linearly with program size rather than quadratically, and the proof can be designed together with the program by stepwise refinement, each subroutine carrying its assertions from the start. A proof bolted on afterwards reconstructs design rationale; a proof grown with the design records it.

A programmer who believes this treats "I traced through the cases" as no evidence at all for concurrent code, and asks instead: what predicate is always true, and does every action preserve it? The same shape carries from shared-memory programs to message-passing protocols, where the entire correctness argument for a consensus algorithm compresses into one conjunction of invariants, each conjunct owned by a variable, each action checked against each conjunct. Finding the invariant takes creative effort; checking it is mechanical. That division of labor, human insight for the invariant and drudgery for the checking, is exactly what makes machine-assisted verification feasible.

**Source:** [Proving the Correctness of Multiprocess Programs](../works/proving-the-correctness-of-multiprocess-programs.md) — the generalization of inductive assertions to multiple processes via interpretations, consistency, and monotonicity; the discussion of why exhaustive case analysis of the bakery algorithm proved hopeless; and the hierarchical design-with-proof methodology. [The Part-Time Parliament](../works/the-part-time-parliament.md) — the appendix's consistency proof, which reduces the protocol's correctness to an invariant conjunction preserved by every action.
