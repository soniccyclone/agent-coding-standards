---
type: lesson
title: "A distributed algorithm can only depend on what its participants can actually tell apart"
figure: lynch
works: [impossibility-of-distributed-consensus-with-one-faulty-process]
axes: [parallelizability, verifiability, hardware-affinity]
subdomains: [distributed-systems-and-concurrency, formal-methods-and-verification]
tags: [lesson]
---
# A distributed algorithm can only depend on what its participants can actually tell apart

**Lesson:** Two facts do the real work in the classic consensus impossibility argument, and both are about the limits of local knowledge rather than about consensus. The first is that steps taken by disjoint sets of processes commute: if two groups act without exchanging information, running one group then the other, or the reverse, lands the system in the same place. The second is that a process that has stopped is locally indistinguishable from a process that is merely slow, because nothing in an asynchronous model lets you observe absence of activity. Together these say that a correct algorithm cannot be built on any distinction its participants are physically incapable of drawing. Any design that quietly relies on "we would have heard from them by now" has smuggled in a global observer that does not exist.

The commutativity point is the more generative of the two. It is the formal statement of why concurrency is hard in a specific way: independent activity does not merely interleave arbitrarily, it produces genuinely identical futures from different pasts, so no amount of local bookkeeping can recover the order in which things happened. The consequence runs in both directions. It is a constraint, because it caps what any protocol can conclude. It is also a tool, because it lets you collapse enormous families of interleavings into a single case during a proof, which is the only reason such proofs are finishable at all.

The practical discipline this induces is to write down, for each participant, exactly what it can observe, and then refuse to let any line of the algorithm branch on anything else. Timeouts, failure detectors, and heartbeats then reveal themselves for what they are: not detection mechanisms, but assumptions being added to the model, which have to be paid for and justified rather than assumed. A programmer who works this way treats every "the node must be down" in a design document as an unproven premise and goes looking for what grants it.

**Source:** [Impossibility of Distributed Consensus with One Faulty Process](../works/impossibility-of-distributed-consensus-with-one-faulty-process.md) — the commutativity lemma about schedules over disjoint process sets, together with the stated modeling assumption that process death is unannounced and undetectable.
