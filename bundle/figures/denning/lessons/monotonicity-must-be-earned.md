---
type: lesson
title: "More resource can make things worse; only a structural property forbids it"
figure: denning
works: [virtual-memory]
axes: [verifiability, cognitive-load]
subdomains: [operating-systems-and-systems-programming, algorithms-and-complexity]
tags: [lesson]
---
# More resource can make things worse; only a structural property forbids it

**Lesson:** Everyone assumes that giving a system more of the resource it is short of cannot hurt. Denning's survey reports that for one of the most widely deployed replacement rules this is simply false: there exist access sequences on which the rule, given a larger memory, faults more often than it did with a smaller one. The assumption was never a theorem. It was an intuition that happened to hold for the rules people had examined, and the counterexample shows that "monotone in the resource" is a property some designs have and others lack, not a law of the domain.

What makes the episode worth learning from is the shape of the fix. The remedy is not a patch to the offending rule or a special case for the pathological sequence; it is the identification of a structural condition that decides the question for a whole class at once. Call a rule well-behaved when the set it retains at any size is always contained in the set it would retain at the next size up. That single containment requirement forces monotonicity immediately, and the argument is two lines: if an item is present in the smaller configuration it is present in the larger one, so every hit in the small case is a hit in the large case, so the larger resource cannot produce more misses. The rule that misbehaves is exactly the one that fails containment, because what it retains depends on arrival order rather than on any nested notion of usefulness. Notice the economy — one property, proved once, settles an unbounded family of designs and does so without examining any individual rule's mechanics.

The habit this teaches is to name the invariants your intuitions are secretly leaning on, then check whether the design supplies them. "More memory can only help," "a larger batch can only be more efficient," "raising the timeout can only reduce failures," "adding a replica can only improve availability" — each of these is a monotonicity claim, each is false for some plausible implementation, and each is knowable in advance from structure rather than discoverable later from a confusing incident report. Ask what containment or ordering property would make the claim follow, and then ask whether the mechanism has it.

There is a payoff beyond avoiding surprises, and it is the reason this class of rules became the object of study rather than a footnote. Designs with the containment property are tractable to analyze: their behavior at all resource sizes can be characterized from a single pass over the access sequence, which is what makes their trade curves measurable at all. A structural property adopted for correctness turned out to be the same property that made the whole family analyzable — the usual relationship between a construct's discipline and how much you can prove about it.

**Source:** [Virtual Memory](../works/virtual-memory.md) — the replacement-algorithm section's account of the anomalous non-decreasing fault curve for order-of-arrival replacement, followed by the definition of the well-behaved class via memory-state containment across sizes, the short proof that containment implies monotonicity, and the remark that this class contains the reasonable rules and is unusually easy to analyze.
