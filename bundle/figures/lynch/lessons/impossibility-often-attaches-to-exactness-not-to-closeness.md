---
type: lesson
title: "Check whether the impossibility is about exactness rather than difficulty, because arbitrarily close is often reachable when equal is not"
figure: lynch
works: [reaching-approximate-agreement-in-the-presence-of-faults]
axes: [expressiveness, verifiability]
subdomains: [distributed-systems-and-concurrency, algorithms-and-complexity, formal-methods-and-verification]
tags: [lesson]
---
# Check whether the impossibility is about exactness rather than difficulty, because arbitrarily close is often reachable when equal is not

Impossibility results get filed mentally as statements about difficulty: this problem is too hard for this setting, so aim lower. Sometimes that is wrong in an interesting way. The barrier may sit not on the hard part of the requirement but on its *exactness* — on the demand for an identity rather than a proximity. Guaranteed-terminating exact agreement among unreliable asynchronous participants is unattainable. Agreement to within a tolerance you get to choose, however small, is attainable, with a guaranteed halt and no probabilistic escape hatch. Both requirements ask participants to end up in the same place; only one of them insists that "same" means *equal*, and that insistence is the whole obstruction.

The reason this is not a cheat is worth sitting with. A process of successive refinement can shrink the spread of honest values by a constant factor every round forever, and it will never make that spread zero. Every finite tolerance is met after a computable number of rounds; the limit is met at no round at all. So a requirement quantified as "for every tolerance there exists an algorithm" lives on the achievable side of the line while the seemingly infinitesimally stronger "there exists an algorithm meeting tolerance zero" lives on the impossible side. The gap between them is not small in engineering terms even though it is small in numeric terms, and noticing which side of it your actual need falls on is often the whole design decision.

The habit worth forming is to interrogate exactness whenever you hit a wall. Ask what your requirement is really for. Sensors being reconciled, clocks being brought into step, replicas converging on an estimate — none of these callers care about bit-identity; they care about a bound they can budget for. Conversely, if you truly do need identity (which value gets committed, which participant holds the lock), no amount of convergence substitutes, and you should stop looking for one. The mistake to avoid in both directions is inheriting an exactness requirement you never examined, either paying for consensus where a tolerance would do or convincing yourself that convergence is nearly as good as a decision when the caller will break unless the answers match.

**Source:** [Reaching Approximate Agreement in the Presence of Faults](../works/reaching-approximate-agreement-in-the-presence-of-faults.md) — this framing is set up in the problem statement, where agreement is redefined as ending within a preassigned tolerance while validity is kept intact, and the paper repeatedly positions its asynchronous algorithm as the counterpoint to the impossibility of guaranteed-terminating exact agreement.
