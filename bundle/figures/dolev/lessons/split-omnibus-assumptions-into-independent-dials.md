---
type: lesson
title: "An omnibus assumption hides several independent dials; separate them before believing anything proved about it"
figure: dolev
works: [on-the-minimal-synchronism-needed-for-distributed-consensus]
axes: [verifiability, primitive-count, hardware-affinity]
subdomains: [distributed-systems-and-concurrency, formal-methods-and-verification]
tags: [lesson]
---
# An omnibus assumption hides several independent dials; separate them before believing anything proved about it

**Lesson:** Words like asynchronous, atomic, and reliable name bundles, not properties. A famous impossibility result had established that agreement among processes cannot survive even one failure without timing guarantees, and the profession absorbed it as a fact about a single condition. Reading the proof closely shows it consumes three separate freedoms at once: that a participant may pause arbitrarily long, that a message may take arbitrarily long, and that messages may arrive out of the order they were sent. Nothing forces those to travel together. Pull them apart into independently settable dials and the single fact splits into a map, and the map is more useful and more surprising than the fact. The negative result gets stronger along one dial — even participants marching in perfect lockstep cannot tolerate one failure if delivery time and delivery order are both free — while along the others it collapses entirely, since bounding delivery time alone, or fixing delivery order alone, suffices to tolerate any number of failures.

Two of the dials turn out not to be about time at all, and those are the ones a working programmer is most likely to have discarded as implementation detail. Whether a participant can reach everyone in one indivisible step or only one peer at a time is one dial. Whether receiving and then sending constitutes a single indivisible step, or two steps with an unbounded gap between them, is another. Both are decisive: split the receive from the send and a construction that tolerated every failure stops tolerating even one; narrow reach from everyone to one peer and the ceiling drops from everyone to a single failure. Granularity of atomicity is not a modelling convenience, it is a purchasable resource with a price attached, and the price is measured in how much failure the system can absorb.

The other thing the map shows is that the surface between possible and impossible is not a gradient. There are settings from which flipping any single dial the wrong way drops tolerance from everything to one or two, with nothing in between. That shape is why arguing about protocols before pinning down assumptions is wasted effort: the assumptions, not the ingenuity, are selecting the feasible region, and they select it in jumps.

So when handed an impossibility claim, the first move is to ask which conjuncts of its model the proof actually spent, because the claim is only as broad as the weakest conjunct it needed. And when writing a specification, refuse to let one adjective stand for a bundle. Enumerate what is separately guaranteed — a delivery deadline, an ordering guarantee, a clock-drift bound, a fan-out, a boundary around an indivisible step — because each is separately obtainable, separately costly, and you may need only one of them. Teams that write asynchronous or atomic as a single word cannot tell which guarantee they are relying on, and therefore cannot tell what a configuration change has just taken away.

**Source:** [On the Minimal Synchronism Needed for Distributed Consensus](../works/on-the-minimal-synchronism-needed-for-distributed-consensus.md) — the introduction's decomposition of the earlier impossibility proof into the distinct freedoms it uses, the resulting list of five independent system parameters, the exhaustive table of maximum tolerance over all their settings, and the identification of the minimal favourable settings from which any single downgrade is fatal.
