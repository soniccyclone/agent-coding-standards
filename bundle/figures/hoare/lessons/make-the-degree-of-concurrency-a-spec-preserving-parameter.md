---
type: lesson
title: "Make the degree of concurrency a parameter that leaves the specification unchanged"
figure: hoare
works: [communicating-sequential-processes-book]
axes: [parallelizability, hardware-affinity, verifiability]
subdomains: [operating-systems-and-systems-programming, distributed-systems-and-concurrency]
tags: [lesson]
---
# Make the degree of concurrency a parameter that leaves the specification unchanged

**Lesson:** A system running one activity at a time and the same system running four should differ in one operator, not in their specifications. That is achievable, and the way to achieve it is to arrange that every resource an activity touches is a per-activity stand-in rather than the shared article itself. Activities then have nothing in common to interfere over, running several is simply interleaving several copies, and the logical description of the assembly is exactly what it was for one. The degree of concurrency becomes a dial affecting throughput and nothing else — which means it can be turned during operation, or tuned per deployment, without any of the reasoning being redone.

This is the real content of the observation that time-sharing one processor and genuinely running on several have the same logical effect. If the degree is a parameter with no semantic consequence, then the physical arrangement realizing it has no semantic consequence either, since both are ways of producing the same interleaving. The value of that is easy to underrate: correctness arguments, tests, operational intuition and incident analysis all carry across a hardware change that is normally treated as a rewrite with its own risk register. It also means the question "is this bug a concurrency bug" acquires a sharp answer, because a defect reproducible at degree one is not one.

The property is not free, and knowing what pays for it is what makes it actionable. Every point at which two activities would share something real has to be moved behind a stand-in, and the stand-ins must be available in unlimited number even though the real articles behind them are not. That is the whole of the work, it is done once, and it is exactly the work people skip when they add concurrency by starting more threads. The diagnostic runs in reverse and is worth using as a design check: if raising the degree of concurrency forces you to change a specification or revisit an argument, then something real is still being shared directly, and the place where the argument had to change is precisely where the trouble will be.

**Source:** [Communicating Sequential Processes](../works/communicating-sequential-processes-book.md) — the operating systems section of the shared resources chapter, which builds up from a system running one job at a time, through spooling systems supplying an unbounded number of virtual card readers and line printers over a small number of actual ones, to the observation that since no communication is required between jobs, simple interleaving is the appropriate sharing method — the technique called multiprogramming, or multiprocessing when more than one actual processor is used — with the remark that the logical effects of the two are the same, and the final system defined as four interleaved copies of the single-job batch process carrying the same logical specification as the one-job version.
