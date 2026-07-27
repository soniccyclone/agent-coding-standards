---
type: lesson
title: "A specification is real only if it is consistent; check that before you try to satisfy it"
figure: hilbert
works: [mathematische-probleme]
axes: [verifiability, primitive-count]
subdomains: [formal-methods-and-verification, foundations-of-computation]
tags: [lesson]
---
# A specification is real only if it is consistent; check that before you try to satisfy it

**Lesson:** Hilbert's second problem carries a definition of existence that is easy to skip past and hard to unlearn once seen: if the properties demanded of a thing lead to a contradiction, the thing does not exist, and if the properties provably never lead to a contradiction in finitely many steps, that non-contradiction is what existence means. Nothing else is required of it — no construction, no intuitive picture, no story about what it really is. He applies this to the continuum directly: it is not the collection of decimal expansions or of laws generating sequences, it is the system whose behavior is fixed by the stated rules, in which exactly the derivable propositions hold and no others.

Read as engineering advice, this says a requirements document is not a wish list, it is a theory, and theories can be inconsistent. Two requirements that cannot both hold do not describe a hard system; they describe no system, and every hour spent implementing against them is wasted before it starts. That makes consistency a property to establish about the spec, prior to and independent of any implementation — the analogue of Hilbert's demand for a direct proof that the arithmetic axioms cannot derive a contradiction. His own remark in the same problem, that the effort to produce such a proof is what forces the axioms to be stated exactly, is the practical payoff: attempting the consistency argument is the most reliable way to discover what your requirements actually say.

The second half of the move is just as useful and more often resisted. If a component is completely characterized by the properties it guarantees, then callers must be written against those properties alone, and any behavior they rely on that is not derivable from them is a bug in the caller even when today's implementation happens to provide it. That is what it means to treat an interface as a definition rather than a description of the current code. Someone who thinks this way writes down the guaranteed relations first, treats them as the whole of the contract, and gets the freedom to replace the implementation entirely — because the specification, not the code, was the thing that existed.

**Source:** [Mathematische Probleme](../works/mathematische-probleme.md) — the second problem on the compatibility of the arithmetic axioms, particularly its identification of freedom from contradiction with mathematical existence and its account of the continuum as constituted by what the axioms derive.
