---
type: lesson
title: "Order your assumptions by how the ideas arise, not by logical minimality"
figure: scott
works: [outline-of-a-mathematical-theory-of-computation]
axes: [cognitive-load, verifiability]
subdomains: [formal-methods-and-verification, software-engineering-and-architecture]
tags: [lesson]
---
# Order your assumptions by how the ideas arise, not by logical minimality

**Lesson:** There is a strong pull toward stating a set of assumptions in its irredundant form: drop every condition implied by another, present what remains, and note with satisfaction that nothing is wasted. The cost is that the surviving assumptions are the strong ones, and strong assumptions are the hardest to motivate, because the argument that makes them plausible is the argument for the weaker version they subsume. A reader handed the minimal set gets no account of why any of it should be believed. The alternative is to state the weak condition first with the reasoning that makes it obvious, then discover that it is not quite enough for the applications in view, then strengthen it — and to leave the superseded conditions in place, acknowledged as redundant, because they carry the motivation the final ones cannot.

The redundancy is not sloppiness; it is a record of where each requirement came from. A condition that arrived as "obviously any well-behaved map should do at least this much" and a condition that arrived as "we need this specific closure property to make the limit construction work" have very different standing, and someone later deciding whether a requirement can be relaxed needs to know which kind they are looking at. A flattened minimal list erases exactly that information, which is why minimal axiom sets are pleasant to admire and unpleasant to modify: nothing in the presentation tells you which conditions are load-bearing for what.

The same applies to any specification, interface contract, or set of invariants a system is built on. Present each requirement next to the pressure that produced it, in the order the pressures appeared, and let the strong ones visibly grow out of the weak ones. Then a summary in one sentence, once the reader already has the reasons, is genuinely useful; the mistake is opening with that sentence. And when an assumption exists but its motivating argument cannot be reconstructed, that is worth treating as a defect in its own right — an unmotivated requirement is one nobody can safely change, so it will be preserved by default long after the situation that caused it is gone.

**Source:** [Outline of a Mathematical Theory of Computation](../works/outline-of-a-mathematical-theory-of-computation.md) — the sequence of axioms, each introduced with an informal argument and then strengthened by the next, and the closing remark of the computability section anticipating the objection that two of the axioms are implied by later ones, answered by saying they are given in the order in which the ideas naturally occur, followed by the one-sentence summary of the whole set.
