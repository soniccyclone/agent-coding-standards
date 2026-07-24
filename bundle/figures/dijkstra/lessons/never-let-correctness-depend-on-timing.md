---
type: lesson
title: "Make cooperating processes correct under every speed ratio, because timing assumptions are hidden coupling"
figure: dijkstra
works: [cooperating-sequential-processes, solution-of-a-problem-in-concurrent-programming-control, the-structure-of-the-the-multiprogramming-system]
axes: [parallelizability, verifiability, hardware-affinity]
subdomains: [distributed-systems-and-concurrency, operating-systems-and-systems-programming]
tags: [lesson]
---
# Make cooperating processes correct under every speed ratio, because timing assumptions are hidden coupling

**Lesson:** The defining property of a sequential process is the order of its steps, not their pace; nothing about the process changes if you observe it with a stopwatch. Take that seriously and a design rule follows: a set of cooperating processes must be correct under every possible assignment of speeds, including speeds that vary and speeds that drop to zero outside the agreed synchronization points. Assuming anything about relative pace is a form of implicit communication between processes, and like all hidden coupling it produces an unstable equilibrium: replace a device with a faster model, reprogram one component, and a "working" system silently loses the property it never actually had.

The discipline pays in reasoning power. When cooperation rests only on explicit synchronization, the whole ensemble can be verified by discrete logic, ordering arguments that need no clocks, no probabilities, and no expectations about the scheduler. It also pays in portability of the deepest kind: the same argument covers one processor time-slicing many processes and many processors running them in parallel, because the design never mentioned the number or speed of processors in the first place. The distinction between multiprogramming and multiprocessing becomes an implementation detail below the level at which correctness lives.

Believing this changes how one reads a concurrent design. Any correctness story that includes "by then it will have finished" or "this window is too short to matter" is not a proof but a bet against future hardware. The reviewer's question is always: does the argument survive an adversary who may pause any process indefinitely at any point outside its synchronization primitives, and run any other arbitrarily fast? If not, the coupling is still there, just unpaid.

**Source:** [Cooperating Sequential Processes](../works/cooperating-sequential-processes.md) — the opening sections, which found the whole treatment on refusing speed-ratio assumptions and defend that refusal as economy rather than pedantry. Also [Solution of a Problem in Concurrent Programming Control](../works/solution-of-a-problem-in-concurrent-programming-control.md) — the problem statement makes speed-independence and stop-tolerance explicit admission criteria for any solution. Also [The Structure of the 'THE'-Multiprogramming System](../works/the-structure-of-the-the-multiprogramming-system.md) — the processor-allocation discussion, where a society of explicitly synchronized processes with undefined speed ratios is what makes the system independent of its processor count.
