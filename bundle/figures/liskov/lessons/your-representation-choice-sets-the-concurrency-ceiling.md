---
type: lesson
title: "Your representation choice sets the concurrency ceiling, not your concurrency constructs"
figure: liskov
works: [guardians-and-actions]
axes: [parallelizability, expressiveness, cognitive-load]
subdomains: [distributed-systems-and-concurrency, databases-and-data-management, programming-languages-and-semantics]
tags: [lesson]
---
# Your representation choice sets the concurrency ceiling, not your concurrency constructs

**Lesson:** A system can be written entirely out of good concurrency machinery and still serialize almost completely, because the machinery only protects whatever units the data structures present to it. Store a collection of independent things in one general-purpose container and every touch of any one of them contends for the whole container: adding an entry blocks every lookup, appending to one entry blocks reads of its neighbors. The program contains no obvious mistake. The contention was decided when someone picked a container, long before any concurrency was written.

This reframes where to look when a system does not scale. Adding threads, splitting requests, or reaching for a finer-grained lock on the same structure will not help, because the structure itself is the unit. What helps is designing a type whose externally visible behavior still looks indivisible but whose internals permit non-conflicting work to proceed together — an associative structure where distinct keys never interfere, a queue whose ordering promise is about completion rather than arrival. These are not tricks layered on top; they are different abstractions with deliberately weaker guarantees, chosen because the weaker guarantee is all the application actually needed.

Which leads to the second half: indivisibility should be demanded at the abstraction level where it means something, not at the level of the machine words underneath. Insisting the strongest possible ordering hold everywhere is what forces everything into single file. Frequently the application would be perfectly correct with a much looser promise — an existence check that need not stay true for the rest of the operation, a directory that need only converge eventually. Naming that looser promise honestly and building a type that provides exactly it is the legitimate route to concurrency; quietly running without any promise is not.

A programmer who believes this diagnoses a throughput problem by asking what unit the data structure exposes to the coordination layer, and expects the fix to be a different type rather than more threads. When designing, they choose the granularity of the state before choosing how work is divided, and they write down which orderings the application truly requires so that the ones it does not require can be given up on purpose instead of defended out of habit.

**Source:** [Guardians and Actions: Linguistic Support for Robust, Distributed Programs](../works/guardians-and-actions.md) — the remarks following the mail-system example, which trace the lack of concurrency and the deadlocks to the choice of built-in atomic arrays and propose user-defined atomic types with weaker but still indivisible interfaces.
