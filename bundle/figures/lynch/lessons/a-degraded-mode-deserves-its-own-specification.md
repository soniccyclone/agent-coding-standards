---
type: lesson
title: "A degraded mode is not the absence of a guarantee, it is a guarantee you have not bothered to write down"
figure: lynch
works: [brewers-conjecture-and-the-feasibility-of-consistent-available-partition-tolerant-web-services]
axes: [verifiability, expressiveness, cognitive-load]
subdomains: [distributed-systems-and-concurrency, databases-and-data-management, formal-methods-and-verification]
tags: [lesson]
---
# A degraded mode is not the absence of a guarantee, it is a guarantee you have not bothered to write down

Once a property is proven unachievable, the usual response is to declare it dropped and let the fallback behavior be whatever the code happens to do. That is where systems rot. Notice how cheap the "pick any two" corner cases are once you look at them: a service that ignores every request satisfies consistency and partition tolerance; a service that eternally returns its initial value satisfies availability and partition tolerance. Both are theorems and both are worthless. The tradeoff framing is satisfied by garbage, which is proof that the framing is not where the engineering content lives. The content lives in what you promise *instead*, and in whether that promise is stated precisely enough that someone could catch you violating it.

Doing this well means writing a weaker condition with the same rigor you would have given the strong one. The move demonstrated here keeps the shape of the strong property — an ordering of operations that respects real-time precedence — and then relaxes precisely one clause: precedence is only enforced across pairs of operations separated by a long enough stretch of healthy network. Everything else stays. Reads still return some value that was genuinely written rather than an arbitrary one; per-node request order is still respected; runs without loss are still fully consistent. And crucially the relaxation is *quantified*: a parameter names how long after a partition heals before ordering is owed again. "Eventually consistent" as a slogan promises nothing; a bound on the reconvergence interval is a claim you can build against, test against, and be wrong about.

The habit this teaches is to treat every fallback path as a specification obligation rather than an exception handler. When a programmer decides that under partition a replica will serve stale data, the work is not finished at that decision — it starts there. How stale? Stale relative to what ordering? Which invariants still hold on the stale value? How long until the system owes freshness again? Systems that skip these questions are not making a tradeoff; they are declining to have a contract in the exact regime where clients most need one, since the degraded path is by definition the one that runs when things are already going badly.

**Source:** [Brewer's Conjecture and the Feasibility of Consistent, Available, Partition-Tolerant Web Services](../works/brewers-conjecture-and-the-feasibility-of-consistent-available-partition-tolerant-web-services.md) — this thinking is in the section on weaker consistency conditions, where the trivially-correct two-out-of-three constructions are dismissed and replaced with a formally defined, time-parameterized relaxation of atomicity plus a proof that a modified centralized protocol meets it.
