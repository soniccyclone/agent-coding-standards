---
type: lesson
title: "Without a timing assumption, slow and dead are the same observation"
figure: fischer
works: [impossibility-of-distributed-consensus-with-one-faulty-process]
axes: [parallelizability, hardware-affinity]
subdomains: [distributed-systems-and-concurrency]
tags: [lesson]
---

# Without a timing assumption, slow and dead are the same observation

**Lesson:** Failure detection is not a service you can implement; it is an assumption you have to buy. If nothing bounds how long a step or a delivery may take, then a participant that has stopped forever and one that is merely between two very slow moments produce literally identical evidence at every observer, for all time. Every mechanism that appears to detect failure — a timeout, a heartbeat gap, a lease expiry — is not observing failure at all. It is asserting a bound on delay and then treating a violation of that bound as death. The bound comes from somewhere physical: a clock, a known network, an operator's judgment about tail latency. It is not derivable from the protocol.

Once that is clear, the reason waiting for agreement can hang forever stops being mysterious. A protocol that must not decide wrongly cannot commit while an unheard-from participant might still speak, and it cannot ever conclude that the participant will not speak. So it waits, and the interval in which one unreachable participant stalls everyone is not an implementation defect in any particular commit protocol — it is a property every such protocol must have. The corresponding design move is to stop hunting for the protocol that has no such interval and start choosing, explicitly, which extra assumption you are willing to pay for: bounded delay for some stretch of the run, synchronized-enough clocks, randomization that gives termination with probability one rather than with certainty, or a weaker agreement requirement.

The engineering consequence is that a distributed design should carry its timing and failure assumptions as first-class, written-down parameters, in the same way an embedded design carries voltage and clock tolerances. Systems whose availability story rests on undocumented timeouts have made the purchase without recording the price, which is why they fail in ways their authors describe as impossible: the assumption was real, it was just never stated, so nobody checked whether the deployment still satisfied it.

**Source:** [Impossibility of Distributed Consensus with One Faulty Process](../works/impossibility-of-distributed-consensus-with-one-faulty-process.md) — the model's explicit refusal of relative process speeds, synchronized clocks, and death detection; the closing remarks on needing refined timing models or probabilistic termination; and the companion protocol for participants that are dead before the run starts, which shows how narrow the escape is.
