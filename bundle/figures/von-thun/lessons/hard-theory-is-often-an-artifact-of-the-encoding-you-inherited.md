---
type: lesson
title: "Hard theory is often an artifact of the encoding you inherited"
figure: von-thun
works: [recursion-theory-and-joy]
axes: [cognitive-load, verifiability]
subdomains: [foundations-of-computation, programming-languages-and-semantics]
tags: [lesson]
---
# Hard theory is often an artifact of the encoding you inherited

Computability theory acquired its reputation for forbidding proofs partly by accident of history. Its classical formalisms cannot manipulate their own descriptions, so before a formalism can say anything about itself, programs must be pushed through an arithmetic encoding, every syntactic operation must be mirrored by an arithmetic one, and the resulting proofs carry the weight of the translation rather than the weight of the idea. Von Thun's move is to redo the standard results in a setting where programs are already ordinary values, and to observe what happens: the parameterisation theorem collapses to a single list-building operation, diagonalisation to a two-word program, the recursion theorem to a short chain of rewrites, and Rice's theorem to a page of algebra. He goes as far as suggesting the field would have looked qualitatively less intimidating had a program-as-data language existed decades earlier.

The generalisable claim is that difficulty has two components which practitioners routinely confuse: difficulty belonging to the subject, and difficulty imported by the representation the subject was first expressed in. The second kind is invisible from inside, because everyone learns the encoding along with the content and comes to experience the encoding's overhead as the content's depth. It only becomes visible when someone re-expresses the same results in a representation that does not require the translation, and the results turn out to be short.

What a programmer does differently is treat sustained difficulty as a diagnostic about representation rather than a fact about the problem. When proofs about your system are unbearable, when tests need elaborate scaffolding to say simple things, when reasoning about your own configuration or schema or build requires a parallel vocabulary that mirrors the real one — the ceremony is a measurement of the gap between what you are reasoning about and what your notation can hold directly. Closing that gap is usually a bigger win than getting better at the ceremony, and it is a different kind of work: change what the system can represent about itself, and whole classes of argument stop needing to be constructed at all.

**Source:** [Recursion Theory and Joy](../works/recursion-theory-and-joy.md) — the discussion of why classical formalisms need arithmetic encodings of their own specifications, and the sequence of classical theorems restated afterwards where the encoding step is simply absent.
