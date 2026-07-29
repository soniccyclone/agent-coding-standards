---
type: lesson
title: "A live copy can replace a record of the past"
figure: stonebraker
works: [the-end-of-an-architectural-era]
axes: [hardware-affinity, primitive-count, verifiability]
subdomains: [distributed-systems-and-concurrency, databases-and-data-management, operating-systems-and-systems-programming]
tags: [lesson]
---
# A live copy can replace a record of the past

Durability is a requirement about outcomes: work that was acknowledged must survive a failure. It is not a requirement about method, though systems built when a computer was a single machine had only one method available — write an ordered account of everything that happened to slow, non-volatile storage, and replay it after a crash to reconstruct the present from the past. Because that method arrived bundled with the requirement, it is easy to mistake the log for the guarantee itself.

Once an installation keeps more than one machine and keeps them current with each other, the requirement is already satisfied by a second means, and the two means are redundant. Recovery no longer needs a replayable history; a machine coming back can be brought forward from a peer that never stopped. What survives this reasoning is a much smaller thing: the ability to abandon work in progress, which needs to remember only as far back as the operation currently in flight and can therefore live in volatile memory and be discarded at completion. An entire durable, ordered, carefully sequenced subsystem — and all the code that made its ordering fast enough to tolerate — is not optimized but deleted, and something quite different takes its place.

The general shape is worth naming because it recurs far from databases. A guarantee can be met by redundancy across time or by redundancy across space, and which is cheaper is a fact about the hardware you are standing on, not a fact about the guarantee. When durable writes are cheap relative to the network, record history. When the network is fast and machines are plentiful, keep another copy. The same reasoning condemns any redundancy scheme in which the spare does nothing until disaster: if a second machine is going to exist and be kept current anyway, it should be carrying load, because a design that idles half its capacity in exchange for survivability is buying something it could have had while using everything.

The programmer who takes this on separates every guarantee they must provide from the mechanism they inherited for providing it, then asks which of their resources is currently abundant. They also accept the honest cost of the swap — the failure they can now survive is bounded by how independent their copies really are, and a correlated failure that takes the peers together takes the data with them, which is precisely the case a durable history would have covered.

**Source:** [The End of an Architectural Era (It's Time for a Complete Rewrite)](../works/the-end-of-an-architectural-era.md) — the high-availability discussion, which argues that peer-to-peer replicas make a persistent redo log unnecessary while leaving only a transient in-memory undo log, and rejects idle hot-standby configurations on resource grounds.
