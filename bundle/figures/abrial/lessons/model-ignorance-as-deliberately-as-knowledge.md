---
type: lesson
title: "A model's silence is not the world's absence; represent what you do not know as carefully as what you do"
figure: abrial
works: [data-semantics]
axes: [expressiveness, verifiability, cognitive-load]
subdomains: [databases-and-data-management, formal-methods-and-verification]
tags: [lesson]
---
# A model's silence is not the world's absence; represent what you do not know as carefully as what you do

**Lesson:** Treat any system that holds facts as a model of an evolving external world which it knows only partially, and take the consequences of that partiality seriously instead of collapsing them. The first consequence is that missing information has at least two meanings which must not share a representation. That a person has no spouse is a fact about the world. That a person is married to someone whose identity is unrecorded is a different fact about the world, and both are different again from the model simply never having been told. Systems that map all three onto one absent value destroy information at the moment of recording it, and no amount of downstream cleverness recovers it.

The second consequence cuts deeper and is easier to miss. If the model's knowledge is partial, then two entries with identical recorded properties are not thereby the same thing — they may be two distinct objects about which the same limited set of facts happens to be known. Identity therefore cannot be inferred from content. It has to be conferred: the model itself issues an internal name at the moment an object enters its field of view, and any externally meaningful designation is a synonym layered on top, never the basis of identity. This is why the recognition problem — deciding whether the thing being told about is one you already know — is not solvable inside the model and must be answered by a procedure outside it. Anyone who has watched a deduplication heuristic silently merge two real customers has met the cost of pretending otherwise.

The third consequence is that the vocabulary for describing what the model knows must include modality. Rules come in kinds — what must be the case, what may be the case, what can be derived from other facts — and those distinctions carry directly into how the world is allowed to change over time. A programmer who takes all this on board designs schemas and specifications with explicit room for the unknown, refuses to overload one sentinel with several meanings, treats identity as something assigned rather than computed, and keeps the necessity of a constraint distinct from the mere permissibility of a value. The reward is that queries and proofs about such a model can be believed, because the model no longer asserts more than it was told.

**Source:** [Data Semantics](../works/data-semantics.md) — the introduction's framing of a data base as a partial model of an evolving reality, its stratification of knowledge into facts, obligatory rules, permissive rules and deduction rules, its argument that identity must be granted by the model rather than derived from known properties, and the later section separating the absence of a relation from an unknown value.
