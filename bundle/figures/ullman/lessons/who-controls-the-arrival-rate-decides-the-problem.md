---
type: lesson
title: "Who controls the arrival rate decides what problem you are solving"
figure: ullman
works: [mining-of-massive-datasets]
axes: [hardware-affinity, verifiability, cognitive-load]
subdomains: [distributed-systems-and-concurrency, databases-and-data-management]
tags: [lesson]
---
# Who controls the arrival rate decides what problem you are solving

**Lesson:** Two systems can hold identical data, answer identical questions, and still be entirely different engineering problems, and the variable that separates them is not volume or schema but who sets the pace. A system that pulls its input decides when the next record appears; if it is behind, it simply reads more slowly, and no amount of slowness can make an answer wrong. A system whose input is pushed at a rate chosen elsewhere has lost that freedom before a line of code is written. Falling behind is now a correctness event, not a latency event, because the material you did not process in time is gone. That single difference is what forces approximate summaries, bounded working memory, and one-pass algorithms — none of which are needed by a system holding its own clock, however large its data.

The practical consequence is that "we will make it faster" is not a response to a rate mismatch. Being faster buys headroom against the average, and the thing that kills you is the burst, whose size is a property of the producer. The genuine responses are all semantic: buffer and accept a bounded delay, drop and accept a defined loss, or summarise and accept a bounded error. Each of those is a promise to the consumer about what the answer means, so the choice belongs in the specification rather than in the operations runbook, and it should be made before the first overload rather than during it. A system that has not chosen will still exhibit one of the three behaviours; it will just be whichever one the runtime happens to produce, usually the least useful.

The question generalises well beyond data pipelines because the same asymmetry appears everywhere two components meet. Polling versus interrupts, cron versus webhooks, a queue you drain versus a socket that fills, a batch job versus a user-triggered request path: in each pair, one side can be slow without being wrong and the other cannot. Worth asking of any interface you are about to define, since it is far cheaper to keep the clock than to reclaim it later — an interface that hands the caller control of the rate is very hard to convert into one that does not, because by then every caller depends on the freedom you gave away.

It also reframes what capacity planning is for. Under pull, capacity determines throughput and the risk of getting it wrong is a slow system. Under push, capacity determines fidelity, and the risk of getting it wrong is silently answering questions from partial data. The second failure does not surface as a queue growing or a dashboard reddening; it surfaces as numbers that look fine and are not. That argues for instrumenting the loss itself — counting what was dropped or approximated — as a first-class output of the system rather than as a debugging aid, because it is the only signal that distinguishes the two regimes from outside.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — chapter 4's opening description of a data-stream-management system, which identifies the defining difference from a database system as the fact that the rate of arrival is not under the system's control, so that unlike a database reading from disk at its own pace it must worry about data being lost while queries execute.
