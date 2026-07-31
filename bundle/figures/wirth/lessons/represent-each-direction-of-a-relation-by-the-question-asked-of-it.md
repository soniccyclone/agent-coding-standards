---
type: lesson
title: "Represent each direction of a relation by the question asked of it, not by symmetry"
figure: wirth
works: [algorithms-and-data-structures]
axes: [hardware-affinity, cognitive-load]
subdomains: [algorithms-and-complexity, databases-and-data-management]
tags: [lesson]
---
# Represent each direction of a relation by the question asked of it, not by symmetry

**Lesson:** A binary relation looks symmetric on paper, and the reflex is to store it symmetrically: a list of what each thing points to and a list of what points at each thing. That reflex is usually wasteful, because the two directions are almost never subjected to the same question. Ask what each direction is actually used for. If one direction is enumerated — you need to visit every partner and do something to each — then a list is the right representation, because enumeration is exactly what a list supports. If the other direction is only ever interrogated for a summary property, such as whether any partners remain, then the list of partners is not what you need; the summary is. Storing a count instead of a collection makes the interrogation constant-time, and makes the update that changes the answer a single arithmetic step rather than a search-and-remove.

The general move is to let the query pattern, not the shape of the mathematics, decide the shape of the storage. Two consequences follow that are worth holding onto. First, the resulting representation will be asymmetric even though the relation is not, and that asymmetry is a feature to be documented rather than an inconsistency to be tidied up — someone will eventually want to clean it into symmetry, and the cleanup silently converts a constant-time test into a scan. Second, a summary is only admissible when every operation that could change its value goes through code you control; the count is correct only because the sole way a partner disappears is the step that decrements it. When you replace a collection with an aggregate over it, you are asserting that all mutations funnel through one place, and that assertion has to be true.

The same reasoning governs whether to keep a structure at all past its useful life. Once a preparatory phase has finished with the linkage it built, the fields that implemented that linkage are free, and reusing them to build the next phase's linkage costs nothing and keeps each element to one record. This is only safe because the earlier structure is genuinely dead, so it is a claim about phase ordering, and it should be stated as such rather than left as a coincidence in the field names. Representations that change role between phases are a standard and legitimate technique; the discipline is that each phase's invariant on the shared field is written down, since the type system will not distinguish the two uses.

**Source:** [Algorithms and Data Structures](../works/algorithms-and-data-structures.md) — section 4.3.3's topological sort, where the choice of representation is stated to be determined by the operations to be performed and particularly by the selection of elements with zero predecessors, and each item is accordingly given a key, a linked list of its successors, and a count of its predecessors rather than a list of them; together with the same section's reuse of the leader chain's link field to build the chain of zero-predecessor elements, justified by the observation that the original chain of leaders will afterwards no longer be needed, and described as an operation of replacing one chain by another that occurs frequently in list processing.
