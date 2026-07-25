---
type: lesson
title: "When a formalism feels almost right, check whether its primitive was borrowed from the mechanism you were escaping"
figure: abrial
works: [data-semantics]
axes: [primitive-count, expressiveness]
subdomains: [databases-and-data-management, programming-languages-and-semantics]
tags: [lesson]
---
# When a formalism feels almost right, check whether its primitive was borrowed from the mechanism you were escaping

**Lesson:** The complaint that opens this work is that supposedly logical descriptions of data were still being shaped, often without their authors noticing, by the storage and retrieval hardware of the day. The relational model was the recognized cure. Abrial's move is to apply the same suspicion one level further and ask whether the n-ary relation is itself residue of the mechanism: a tuple with named columns is a record with fields, and a schema of such things is a file layout wearing mathematics. So he drops to a smaller primitive — a link between two objects, expressed as a pair of mutually inverse access functions with declared minimum and maximum cardinalities — and asks whether anything is lost.

Nothing is, and several things are gained. Facts that seem to need three or four participants are handled by promoting the fact itself to an object: an invitation, a purchase, an order becomes a thing that exists, with binary links to its participants. That reification is not a workaround, it is a discovery, because such facts genuinely have identity and can acquire further properties later, which a tuple cannot without a schema change. Constraints that were previously extra apparatus become statements about the two access functions' cardinalities. Inversion becomes an operator rather than a design decision. And the model gains the ability to describe itself, since a category is just another category and the whole structure can be expressed in its own terms — the sharpest available test that a primitive basis is actually complete.

The generalizable habit is to distrust the sense that a formalism is nearly right. That feeling usually means the formalism liberated you from one mechanism while quietly retaining its shape, and the remaining awkwardness is where the borrowed structure is showing through. The diagnostic questions are concrete: can this formalism describe itself, or does it need a second language to talk about its own schemas? Does adding a participant to a fact require restructuring, or merely another link? Are the constraints expressible in the same vocabulary as the data, or do they live in an annex? Each awkward answer points at a primitive that has not been decomposed far enough. The reward for pushing down is not economy for its own sake but that the things which used to be special cases stop being special.

**Source:** [Data Semantics](../works/data-semantics.md) — the foreword's complaint about physical mechanisms shaping logical models, and the early sections arguing that binary connections are a more primitive level of description than n-ary relations, with multi-participant facts reified as objects and constraints expressed as access-function cardinalities.
