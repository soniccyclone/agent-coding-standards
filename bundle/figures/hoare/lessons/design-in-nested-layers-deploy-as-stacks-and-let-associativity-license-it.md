---
type: lesson
title: "Design in nested layers, deploy as two stacks, and let associativity be what licenses the regrouping"
figure: hoare
works: [communicating-sequential-processes-book]
axes: [verifiability, cognitive-load, expressiveness]
subdomains: [distributed-systems-and-concurrency, software-engineering-and-architecture]
tags: [lesson]
---
# Design in nested layers, deploy as two stacks, and let associativity be what licenses the regrouping

**Lesson:** A protocol stack is conceived one way and built another. Conceptually each layer encloses the one beneath it: the innermost pair straddles the raw medium, the next pair treats that entire assembly as its medium, and so on outward. Physically, every sending half sits together at one end and every receiving half at the other. These are two different bracketings of one chain of components, and the reason you are entitled to hold both pictures at once is a law rather than an intuition: the connecting operator is associative, so the grouping is not observable in the result. Absent that law they are not two views of one design, they are two designs, and somebody eventually finds out which one is wrong.

This is worth generalizing, because the pattern recurs constantly and the question it raises is normally answered by hand-waving. The structure that makes a system comprehensible and the structure it has when deployed are routinely different, and whether that difference is safe has a precise answer whenever the composition mechanism has known algebraic properties. Associativity licenses regrouping. Commutativity licenses reordering. A unit element licenses inserting or deleting a do-nothing stage. So the practical instruction is to establish which of these your composition mechanism actually satisfies before relying on rearrangement — and to notice that a mechanism satisfying none of them forbids exactly the rearrangements everyone performs anyway, quietly, on the assumption that it must be fine.

There is a consequence for the design of the mechanism itself, and it is the part that costs something. If you want the freedom to reorganize, nothing in the composition may be able to detect the grouping. No stage may discover how many stages lie beyond it, which particular one it is exchanging with, or how they are bracketed. That is a genuine constraint on interfaces rather than a stylistic preference: every fact a stage can learn about its neighbours' arrangement is a law you have just given up, and with it a class of refactorings. The narrow, uniform, position-independent interface is not tidiness — it is what makes the algebra true, and the algebra is what allows a conceptual layering to be built as a physical stack without a fresh correctness argument every time the deployment changes.

**Source:** [Communicating Sequential Processes](../works/communicating-sequential-processes-book.md) — the buffers and protocols subsection of the pipes section, which presents a multi-layer protocol as transmitter/receiver pairs each nested around the previous layer with the wire innermost, then states that in practice all the transmitters are collected into one at a single end and all the receivers at the other in accordance with the changed bracketing, and that the associativity of the chaining operator is what guarantees the regrouping does not change the system's behaviour; read together with that operator's associativity law given earlier in the same section.
