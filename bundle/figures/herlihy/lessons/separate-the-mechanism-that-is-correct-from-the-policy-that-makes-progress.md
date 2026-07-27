---
type: lesson
title: "Separate the part that must be correct from the part that must be tuned, and let only the tuned part be replaceable"
figure: herlihy
works: [software-transactional-memory-for-dynamic-sized-data-structures]
axes: [verifiability, parallelizability, cognitive-load]
subdomains: [distributed-systems-and-concurrency, software-engineering-and-architecture]
tags: [lesson]
---

# Separate the part that must be correct from the part that must be tuned, and let only the tuned part be replaceable

**Lesson:** Two very different kinds of question get tangled together in concurrent code. Whether an interleaving can produce a state the data type does not admit is a question with a proof; whether two contending participants will keep knocking each other down forever is a question about timing, scheduling, machine size, and workload, and it has no proof — only measurements that change when the deployment changes. Building both into one algorithm means every attempt to improve the second forces a re-audit of the first, which is why sophisticated contention behavior rarely gets built at all. The move that unlocks it is to cut the system along that seam: the core mechanism detects conflicts and recovers from them and is proved once, and every decision about who should yield is delegated to a module that can be swapped without the proof being touched.

What makes such a split real rather than decorative is that the interface between the two carries almost no correctness weight. Here the policy module is consulted at exactly the moment one participant has determined it is about to destroy another's work, and it answers a single question: do it now, or wait. The only obligation placed on any policy is a liveness triviality — a participant that keeps asking must eventually be allowed to proceed, otherwise two of them can refuse each other forever and reinvent deadlock at the policy layer. Beyond that the policy may consult anything at all: elapsed time, thread priorities, what the operating system knows about preemption, hints from the programmer. Those inputs are precisely the ones that formal work on non-blocking algorithms had no way to use, and making them the property of a replaceable module is what lets them be used at all.

The practical result is measured and blunt: with the most naive possible policy the system stalls immediately under any real concurrency, and with a barely less naive one it beats a lock. The mechanism was identical in both. That is the strongest possible evidence for the split, because it shows that the thing determining whether the system works is the thing you can iterate on cheaply without endangering correctness. A programmer who thinks this way asks, of every system component: which of my invariants are provable and which are empirical? Then puts a hard boundary between them, keeps the provable side small and stable, and makes the empirical side something a future engineer can replace on the evidence of a benchmark rather than on the strength of a proof they will not attempt.

**Source:** [Software Transactional Memory for Dynamic-Sized Data Structures](../works/software-transactional-memory-for-dynamic-sized-data-structures.md) — the contention-management section, which states the deliberately weak correctness requirement on any policy module, its consultation point at detected conflict, and the argument that scheduling and environment knowledge belongs there; together with the experiments comparing an always-abort policy against a backoff policy over the same mechanism.
