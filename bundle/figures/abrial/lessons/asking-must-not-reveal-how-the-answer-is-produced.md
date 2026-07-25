---
type: lesson
title: "Asking a question should not reveal whether the answer is stored, computed, or remembered"
figure: abrial
works: [data-semantics]
axes: [expressiveness, hardware-affinity, primitive-count]
subdomains: [databases-and-data-management, programming-environments-and-object-systems]
tags: [lesson]
---
# Asking a question should not reveal whether the answer is stored, computed, or remembered

**Lesson:** There are three ways to answer a question, and a well-built model makes the choice among them invisible at the point of asking. It can know the answer outright, because the fact was recorded. It can derive the answer, by running a rule over other facts. Or it can have derived it earlier and kept the result, answering from that. Abrial's analogy is the memory hierarchy: consulting cache, then main store, then drum, then disk, with a replacement policy deciding what stays near. Human recall works the same way, which is why small sums come back immediately and larger ones get computed. The property worth demanding is that the form of the question is independent of which mechanism supplies the answer, so that a value recorded today and computed tomorrow are indistinguishable to every caller.

This is more than a convenience. It relocates every performance decision to one side of a boundary and every meaning decision to the other, which is what makes the two able to evolve without disturbing each other. Abrial then closes the loop on the implementation side by identifying a small fixed set of standard operations — create, destroy, assert, retract, classify, test, retrieve — and observing that to implement the model at all is precisely to give those operations a physical interpretation. Any interpretation is legal: core memory management, file handling, input/output, or a mixture. The striking illustration is that although the abstract model always defines a relation in both directions as mutually inverse functions, that does not oblige the implementation to maintain both directions as stored structures. One direction can be materialized and the other computed on demand, and nothing above notices. Physical failures at that level surface as ordinary failures at this one.

Two disciplines follow. First, design the interface so that materialization is never implied by the way something is named or accessed; the moment callers can tell a stored field from a derived one, you have leaked the storage plan into the vocabulary and it will never come back out. Second, deliberately pin the mapping to mechanism at a small number of named points rather than scattering it, because a small fixed set of interpretation points is what makes the mapping auditable and replaceable. Abrial is candid that a direct, literal implementation of his own metamodel would have performed dreadfully on the hardware of the time — which is an argument for keeping the abstract description and the physical strategy separately negotiable, not an argument against having the abstract description.

**Source:** [Data Semantics](../works/data-semantics.md) — the introduction's three question-answering mechanisms with the memory-hierarchy comparison and its statement of semantic data independence, together with the implementation section identifying the seven standard programs as the linkage to a physical realization and noting that defining a relation in both directions does not entail a fully inverted store.
