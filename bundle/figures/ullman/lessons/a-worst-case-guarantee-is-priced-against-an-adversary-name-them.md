---
type: lesson
title: "A worst-case guarantee is priced against an adversary — say who it is before you pay for it"
figure: ullman
works: [mining-of-massive-datasets]
axes: [verifiability, cognitive-load, hardware-affinity]
subdomains: [algorithms-and-complexity, distributed-systems-and-concurrency]
tags: [lesson]
---
# A worst-case guarantee is priced against an adversary — say who it is before you pay for it

**Lesson:** A guaranteed-fraction result is always a statement about the nastiest input the design permits, which means it is implicitly a statement about someone choosing that input. The guarantee costs something: to be safe against a pathological arrival order, the procedure must hold back, spread its commitments, and decline to exploit regularities it can see. That conservatism is paid on every ordinary input, and it is worth paying exactly to the extent that a party capable of constructing the pathological input exists and has a motive. So the design question is not "worst case or average case" as a matter of temperament; it is the concrete question of who controls the input, and what they gain from hurting you.

When the answer is that nobody controls it — arrivals come from an enormous, uncoordinated population whose aggregate behaviour is stable and independently measurable — you can spend the guarantee to buy performance. Feeding a historical model of what is coming into the decision rule lets the procedure stop hedging against futures it has good reason to believe will not occur, and it will do better on the traffic that actually arrives. This is a real trade with a real exposure, and the honest way to make it is to state the exposure: if the population's behaviour shifts, or someone acquires the ability to steer it, the procedure degrades to something with no bound at all. Written down, that is a monitorable risk. Left implicit, it is the postmortem.

The same reasoning runs the other way and is the more common error. Systems that face genuine adversaries — anything where a participant profits from your misallocation — get built on average-case reasoning because the average case is what the dashboards show, and the adversary's whole job is to be absent from the historical distribution you fit. There, the conservatism is not overhead; it is the product.

The second half of this is knowing when to stop. Some problems have a ceiling: a proof that no procedure of the permitted kind can guarantee better than a certain fraction, no matter how clever. Once your procedure attains that ceiling, further ingenuity within the stated problem is provably wasted, and every remaining improvement must come from changing the statement — obtaining information the original formulation denied you, relaxing what counts as an admissible input, or accepting a weaker form of guarantee. Impossibility results are therefore not bad news; they redirect effort from the algorithm to the assumptions, which is where the remaining gains actually live.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the closing observations of the advertising chapter, which note that no on-line procedure for the problem as stated can exceed the ratio the generalised Balance algorithm attains, and then propose using historical query frequencies to relax its hedging, conceding that this degrades the result against an adversary who can control the arrival sequence while arguing that search traffic is too voluminous and unsteered for such an adversary to exist.
