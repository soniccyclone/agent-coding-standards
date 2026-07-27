---
type: lesson
title: "A negative result gets its reach from how little it demands and how much it permits"
figure: fischer
works: [impossibility-of-distributed-consensus-with-one-faulty-process, easy-impossibility-proofs-for-distributed-consensus-problems]
axes: [verifiability, primitive-count]
subdomains: [formal-methods-and-verification, distributed-systems-and-concurrency]
tags: [lesson]
---

# A negative result gets its reach from how little it demands and how much it permits

**Lesson:** Positive and negative claims are strengthened in opposite directions, and confusing the two is a common way to waste effort. To make an algorithm impressive you weaken what it needs from its environment. To make an impossibility impressive you do the reverse: hand the hypothetical implementation every convenience you can think of, and simultaneously shrink the goal to the least ambitious version anyone would still call success. If the goal is unreachable even then, it is unreachable under every stronger goal and every stingier environment, which is to say in every real system.

Both moves are visible in how the asynchronous consensus result is set up. The environment is generous: messages are never lost, corrupted, or duplicated, they are delivered exactly once, participants never lie or behave maliciously, only one of them may ever stop, and a participant may broadcast atomically to everyone at once. Internal storage is unbounded and the number of internal states may be infinite, so no computational limit is doing any work. The goal, meanwhile, is reduced to almost nothing: only one participant needs to ever announce an answer, announcements must not contradict each other, and both answers must be possible for some starting inputs. Nobody would ship a protocol satisfying only that. Because the negative result lands there, it lands on everything above it, and the folklore belief that every commit protocol has a window in which one slow participant can hang the whole thing stops being folklore.

The same discipline applied to a family of agreement problems shows why the reach matters more than the difficulty. Restating known bounds over a model that fixes almost nothing, where the objects exchanged between components are left abstract and state sets are not even required to be finite or effectively computable, produced not just shorter proofs but strictly stronger theorems, including a connectivity bound that had not been established before and a much more general treatment of clock synchronization. Generality was not a stylistic bonus; it was the mechanism by which new results appeared.

A programmer who thinks this way is careful about what a benchmark or a failure report proves. Demonstrating that one implementation cannot meet a requirement says nothing; demonstrating that no implementation can, under assumptions more forgiving than production, ends the search. The corollary is a habit of stripping requirements down before declaring them impossible, because a requirement that is impossible only in its most ambitious form is usually a requirement that was stated carelessly.

**Source:** [Impossibility of Distributed Consensus with One Faulty Process](../works/impossibility-of-distributed-consensus-with-one-faulty-process.md) — the introduction's inventory of what the model gives away for free and the deliberately minimal correctness conditions attached to the consensus problem. Also [Easy Impossibility Proofs for Distributed Consensus Problems](../works/easy-impossibility-proofs-for-distributed-consensus-problems.md), whose model section refuses to fix the nature of component behaviors at all and whose conclusion reports generality as the source of the strengthened results.
