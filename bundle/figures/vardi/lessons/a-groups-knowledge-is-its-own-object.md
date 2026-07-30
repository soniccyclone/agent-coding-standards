---
type: lesson
title: "A group's knowledge is its own object, above and below the sum of its members'"
figure: vardi
works: [reasoning-about-knowledge]
axes: [expressiveness, verifiability, parallelizability]
subdomains: [distributed-systems-and-concurrency, formal-methods-and-verification]
tags: [lesson]
---
# A group's knowledge is its own object, above and below the sum of its members'

**Lesson:** The state of what a collection of participants knows is not recoverable from a list of what each one knows. It extends in two directions at once, and both are needed to reason about anything a group does jointly. Downward from the sum: pool the members' information — intersect their sets of remaining possibilities rather than union their conclusions — and the group can pin down facts that no individual member knows, because each member's uncertainty is cut away by another's certainty. Upward from the sum: everyone knowing a fact is weaker than everyone knowing that everyone knows it, which is weaker again than the next level, and the whole infinite tower is distinct all the way up.

The upward direction has a consequence that reliably surprises people: announcing something every single member already knows can change what the group is able to do. Vardi's worked puzzle is the sharpest demonstration available — without the redundant-seeming announcement the participants can never draw the conclusion, no matter how long they interrogate each other, and with it they can. The announcement adds nothing to any individual's stock of facts and everything to the group's, because it lifts the group past the level of the tower where its reasoning was stuck. So an audit that measures information delivered per recipient will score such a message at zero, and be wrong about its effect.

For system design the practical content is this. Whenever a decision must be taken jointly and simultaneously — commit or abort, cut over or roll back, act or wait — the relevant precondition is a property of the group, and neither "each node knows" nor "each node has been told that each node knows" is that property. Meanwhile, whenever you need to know what a system can in principle determine, compute it from the intersection of the components' uncertainties, not from what any component can report. The two directions answer different questions: what could be jointly derived, and what can be jointly relied upon.

**Source:** [Reasoning About Knowledge](../works/reasoning-about-knowledge.md) — chapter one's introduction of common knowledge as the infinite tower and of distributed knowledge as what a pooled observer would know, with the example of two people who jointly determine a fact neither knows; the muddy children analysis showing that with a given number of muddy children the tower holds to one level below what is needed, so the father's individually redundant announcement is what enables the conclusion, and that without it the group's state of knowledge never changes; and chapter two's definitions, where pooling is intersection of possibility sets and the traffic-light example shows why knowing the rules is insufficient without knowing that others know them.
