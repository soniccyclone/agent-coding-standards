---
type: lesson
title: "Trade repeated work for the absence of state: abandon and retry instead of recursing"
figure: wilkes
works: [cambridge-cap-computer-and-its-operating-system]
axes: [cognitive-load, verifiability, primitive-count]
subdomains: [operating-systems-and-systems-programming, algorithms-and-complexity]
tags: [lesson]
---
# Trade repeated work for the absence of state: abandon and retry instead of recursing

**Lesson:** When resolving one thing requires first resolving another of the same kind, the obvious implementation is recursion, and in constrained settings recursion is exactly what you cannot afford — it needs a stack, the stack needs a bound, the bound needs justification, and the whole apparatus has to survive failures partway down. There is an alternative that costs more total work and removes the state entirely: on discovering a missing prerequisite, abandon the attempt in progress completely, start a fresh attempt aimed at the prerequisite, and repeat as often as necessary. Each abandonment throws away work, and each completed attempt resolves one thing permanently. Retry the original operation from the beginning as many times as it takes.

This terminates for a reason worth internalizing, because it is not obvious from the code: every attempt that runs to completion makes one unit of irreversible progress, and progress is monotone, so the number of attempts is bounded by the number of things that could be missing even though no attempt knows anything about the others. Correctness comes from the monotonicity of the progress measure rather than from any plan or bookkeeping, which is why the mechanism needs no memory of what it has already done. The cost is duplicated effort in the worst case; the gain is that the mechanism is stateless, has no depth limit, and is trivially safe to interrupt at any point since an abandoned attempt leaves nothing behind.

The pattern generalizes to anything with a dependency chain and a hard constraint against keeping state: resolvers, loaders, initialization sequences, distributed protocols where a participant cannot hold a partial transaction. The design question to ask when recursion looks necessary is whether the operation can be made idempotent and restartable from scratch, and whether each successful pass leaves a permanent improvement. If both hold, the recursion can be replaced by a loop that knows nothing, and every bound and every failure path disappears with it.

**Source:** [The Cambridge CAP Computer and Its Operating System](../works/cambridge-cap-computer-and-its-operating-system.md) — Chapter 1's description of the capability loading cycle, which notes that making the microprogram work recursively would be awkward and instead abandons the current cycle whenever a needed prerequisite is itself missing, initiates a new cycle for that prerequisite, continues abandoning and initiating as long as necessary, and retries the original instruction repeatedly until all required entries have been loaded.
