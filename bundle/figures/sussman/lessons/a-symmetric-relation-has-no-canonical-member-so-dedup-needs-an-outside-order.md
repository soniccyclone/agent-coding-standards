---
type: lesson
title: "A symmetric relation has no preferred side, so removing the duplicate requires an order the relation does not contain"
figure: sussman
works: [structure-and-interpretation-of-computer-programs]
axes: [expressiveness, cognitive-load]
subdomains: [algorithms-and-complexity, programming-languages-and-semantics]
tags: [lesson]
---
# A symmetric relation has no preferred side, so removing the duplicate requires an order the relation does not contain

**Lesson:** Describe a relation whose defining condition treats its two participants identically, and every fact it yields will be yielded twice, once with the participants in each arrangement. This is not a defect in the description. It is the description being exactly right: you said the condition holds between these two things, the condition genuinely does not care which is written first, and so both writings are true and both get reported. The duplication is the correct output of a correct specification, which is why staring at the rule looking for the bug is unproductive.

What you actually want when you want each pair once is a representative — a rule for choosing one arrangement of each unordered pair and rejecting the other. And nothing in the relation can supply that rule, because supplying it means distinguishing the participants, which the relation's whole content is that you cannot. The choice therefore has to be imported from somewhere outside: an ordering on the participants that has nothing to do with the relation itself, applied as an additional condition so that only the arrangement respecting the order survives. Names, identifiers, insertion sequence, addresses — the source does not matter and is generally arbitrary, and the arbitrariness is not a compromise, it is the only available answer.

The generalization is worth carrying around, because this shape recurs far from logic programming. Deduplicating unordered pairs, canonicalizing sets represented as sequences, choosing a leader among symmetric peers, picking a direction for an undirected edge, breaking a tie between equally-ranked candidates: in every case, the thing being asked for is a canonical representative of an equivalence class whose defining property is that its members are indistinguishable in the terms the system uses. That is not obtainable from those terms. So the design question is never "how do I make the system prefer one" but "what additional, external total order am I willing to introduce, and is it stable" — because if the imported order is not stable across runs, the canonical form is not canonical and you have converted a duplication bug into a nondeterminism bug.

There is also a diagnostic in the pattern. Output arriving in pairs that differ only by an exchange of roles is a reliable sign that a relation you thought was directional is actually symmetric, and that any downstream code treating the two positions as meaningfully different is wrong. It is worth chasing the doubling to its source rather than filtering it, because the filter hides the fact that the two positions were never distinguishable, and that fact usually matters somewhere else too.

**Source:** [Structure and Interpretation of Computer Programs](../works/structure-and-interpretation-of-computer-programs.md) — chapter 4 section 4.4.1, Exercise 4.60, which observes that querying the neighbour relation with both participants left open lists every neighbouring pair twice, once in each arrangement, asks why this happens, and asks whether there is a way to obtain a list in which each pair appears only once; read against the definition of that relation earlier in the same section, whose body compares the two participants' towns in a way that is indifferent to which is named first and adds only a non-identity clause, not an ordering.
