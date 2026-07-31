---
type: lesson
title: "Break a retry tie with an identifier you already have"
figure: wirth
works: [project-oberon]
axes: [parallelizability, hardware-affinity, primitive-count]
subdomains: [distributed-systems-and-concurrency, operating-systems-and-systems-programming]
tags: [lesson]
---
# Break a retry tie with an identifier you already have

**Lesson:** Identical participants running identical code fail identically. If two of them want the same resource, find it busy, wait the same interval and try again, they will collide again, and the retry loop that was supposed to resolve the contention becomes the thing that perpetuates it. The defect is not in the waiting; it is that the wait is a constant, and a constant is the same on every machine. Any retry policy shared verbatim by every contender is a synchroniser: it takes participants that happened to collide once and locks them into colliding forever, with the added cruelty that the more precisely the machines are matched the more reliably the deadlock holds.

The fix is to make the interval a function of something that is already distinct per participant, and the crucial word is *already*. Systems in this position usually have a unique identifier lying around for some unrelated reason — an address, a slot number, a hardware setting made at installation — and deriving the delay from it costs one arithmetic operation and introduces no new state, no new configuration, and nothing to keep consistent. The alternative, generating a random offset, works too and is the standard answer, but it requires a source of randomness at exactly the layer where you least want a dependency, and it makes the behaviour irreproducible in a way that is hostile to debugging. When a deterministic distinguisher is already present, prefer it; it gives the same effect with strictly less machinery, and identical inputs still produce identical runs.

Look also at what the tie-break buys and what it does not. Staggering the retries makes collision recoverable, not impossible — simultaneity can still happen on the first attempt, and if the medium does not report collisions the damage may only be detectable later, by whoever checks the result's integrity. So a staggered retry is one half of a design whose other half is a downstream check that notices corrupted outcomes; without that check, the stagger merely makes the failure rare enough to be mysterious. And the derived-delay approach carries a fairness consequence that should be chosen deliberately rather than discovered: if the delay rises with the identifier, low-numbered participants systematically win, which is fine when the population is small and known and quite bad when it is not.

**Source:** [Project Oberon](../works/project-oberon.md) — the third comment following the network driver listing in section 9.3, which describes verifying that the line is free by testing the hunt bit before sending, polling again after a delay if the line is busy, with the delay influenced by the station's own address so that all stations have slightly different delays, and the accompanying observation that actual collisions can only be detected by the receiver through the redundancy check at the end of the packet.
