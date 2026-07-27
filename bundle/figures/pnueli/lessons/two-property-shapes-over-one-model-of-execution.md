---
type: lesson
title: "Two shapes of property over one model of execution beats a proof theory per paradigm"
figure: pnueli
works: [the-temporal-logic-of-programs]
axes: [primitive-count, verifiability, parallelizability]
subdomains: [formal-methods-and-verification, distributed-systems-and-concurrency]
tags: [lesson]
---

# Two shapes of property over one model of execution beats a proof theory per paradigm

**Lesson:** When sequential and concurrent programs are treated as different kinds of thing, each gets its own correctness vocabulary and its own proof machinery, and the two bodies of technique drift apart with no way to tell which of their differences are essential. The consolidating move is to find the model both are instances of and work there. Take a program to be nothing but a set of states, a relation saying which states may follow which, and a starting point; a run is any chain the relation permits. Sequential determinism is then a choice of how to structure a state — one control position plus data. Concurrency is the same structure with several control positions and a nondeterministic choice of whose turn it is. Nothing about the proof principles has to be reinvented for the second case; only the transition relation is spelled out differently.

On top of that single model, remarkably few property shapes are needed. Partial correctness, absence of arithmetic and indexing faults, mutual exclusion, and freedom from deadlock are all one shape: a predicate true of every reachable state. Termination, accessibility of a critical section, and responsiveness to requests are all a second shape: a situation that must be followed by another. Two shapes, and the sequential/concurrent divide turns out not to be a divide in the properties at all — it shows up only in how expensive the reasoning gets. That is the real dividend of unification: it tells you which apparent differences between programming worlds are substance and which were artifacts of studying them separately.

The transferable habit is to resist per-paradigm vocabulary. When you find yourself with one set of correctness ideas for single-threaded code, another for concurrent code, and a third for distributed code, look for the model they are all special cases of and re-ask what the properties actually are. Usually you find the same two questions — what must always hold, what must eventually happen — and discover that the third of your three vocabularies was mostly notation. It also cuts the other way as a design check: a construct whose correctness cannot be phrased as an invariant plus an eventuality over its runs is a construct you do not yet understand.

**Source:** [The Temporal Logic of Programs](../works/the-temporal-logic-of-programs.md) — the framing of a program as a discrete dynamic system with sequential and concurrent programs obtained by structuring the state, and the catalogue showing partial correctness, clean execution, mutual exclusion, and deadlock freedom all reduced to invariance while total correctness, accessibility, and responsiveness reduce to eventuality.
