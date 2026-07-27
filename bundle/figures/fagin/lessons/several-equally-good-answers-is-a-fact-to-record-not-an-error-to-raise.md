---
type: lesson
title: "Several equally good answers is a fact to record, not an error to raise"
figure: fagin
works: [on-the-semantics-of-updates-in-databases]
axes: [expressiveness, verifiability]
subdomains: [databases-and-data-management, foundations-of-computation]
tags: [lesson]
---
# Several equally good answers is a fact to record, not an error to raise

**Lesson:** Resolving an ambiguous change by preferring the outcome that disturbs the least usually leaves more than one winner. Prior work in this area treated that as grounds for rejection: if the minimal-disturbance criterion does not single out one successor state, the requested change is declared inadmissible. Fagin, Ullman and Vardi refuse that exit. Their reading is that a tie among minimal outcomes is not a malformed request, it is a genuine and correctly computed conclusion, namely that the new information was insufficient to determine which of several worlds you are now in. The right response is to record exactly that, by taking the new state to be the one whose admissible worlds are the union of the worlds admitted by each tied candidate. Nothing is discarded, nothing is invented, and no user gets told their assertion was illegal for the sin of being incomplete.

Two consequences make this more than a nicety. First, because the state now describes a set of possibilities rather than a single configuration, subsequent changes still work: the object you produced is the same kind of object you started with, so the operation composes with itself. A resolution scheme that reports failure on ties, or that picks a tied candidate arbitrarily, breaks that closure. Second, the paper is honest that the union of the candidates may not be expressible in the language the state is written in, and it identifies the conditions under which expressibility is guaranteed. That is the real cost of the position, and it is a cost worth naming: whether your representation can hold an ambiguous conclusion is a property of the representation, discovered by trying, not something you can assume.

The transferable habit is to distinguish "my inputs did not determine an answer" from "my inputs were invalid," and to build the return type so the first case has somewhere to live. A great deal of defensive code raises errors on situations that are not errors at all, merely underdetermined, and every such raise pushes the ambiguity back onto a caller with even less information than the callee had. Widening the result to admit a set of possibilities is more work than throwing, and it forces the awkward question of whether the type system or data model can even express the widened result. But the alternative silently converts missing information into a false claim of failure, or worse, into an arbitrary choice that later code will read as definite.

**Source:** [On the Semantics of Updates in Databases](../works/on-the-semantics-of-updates-in-databases.md) — the discussion following the definition of minimal change, where a non-unique minimum is reinterpreted as incomplete knowledge and the new state is defined by the union of the tied candidates' models, together with the lemma and theorems establishing when that union is representable.
