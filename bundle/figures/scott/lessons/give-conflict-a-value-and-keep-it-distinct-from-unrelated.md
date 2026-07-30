---
type: lesson
title: "Give conflict its own value, and never confuse conflicting with merely unrelated"
figure: scott
works: [outline-of-a-mathematical-theory-of-computation]
axes: [expressiveness, verifiability, cognitive-load]
subdomains: [programming-languages-and-semantics, databases-and-data-management]
tags: [lesson]
---
# Give conflict its own value, and never confuse conflicting with merely unrelated

**Lesson:** Once values are ordered by how much they tell you, the natural operation on two of them is to combine everything each one asserts. That operation has to produce an answer even when the two disagree, and the honest answer is a distinguished element standing for over-determination: not a perfect value that knows everything, but a saturated one, the state of having been told contradictory things. Reaching it is a real outcome that the value space can name, and combining two values yielding it is exactly the statement that those values are inconsistent. The alternative designs — refusing to combine, raising an error out of band, silently preferring one side — all remove the outcome from the space of values and put it into control flow, where it can no longer be reasoned about with the same algebra as everything else.

The second half of the lesson is a distinction that is easy to lose and expensive to lose: inconsistent is a much stronger relation than incomparable. Two values are incomparable when neither is above the other, which happens all the time between perfectly compatible partial descriptions of different aspects of the same thing. They are inconsistent only when combining them saturates. There is a corresponding notion at the other end — combining down to the empty element says the two share no information at all — and it too is a genuine relation rather than an absence. A system that treats "these are not comparable" as "these are in conflict" will reject merges that should succeed; a system that treats conflict as mere incomparability will accept merges that quietly lose one side. Both errors come from having only an ordering and no algebra.

Generalize this to any setting where partial information from several sources has to be combined: replicated state, configuration layered from multiple files, type inference accumulating constraints, sensor fusion. The design questions are the same three. What is the element that means nothing is known, what is the element that means too much has been claimed, and does combining two inputs land in one of them or somewhere in between. Answering all three gives you a total combining operation, which is what lets merge be associative and order-independent instead of a procedure whose result depends on the sequence of arrivals. Answering only the first — the common case, since undefined values are the ones people notice — leaves conflict handling scattered through the code that calls the merge rather than expressed in the values it merges.

**Source:** [Outline of a Mathematical Theory of Computation](../works/outline-of-a-mathematical-theory-of-computation.md) — the completeness-and-continuity section, which introduces the top element as over-determined rather than perfect, reads the equation that two elements join to the top as saying they are inconsistent, explicitly distinguishes that from the weaker relation of incomparability, and reads the dual equation that two elements meet at the bottom as saying their information does not overlap.
