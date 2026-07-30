---
type: lesson
title: "When two communities have separate words for the same idea, prove the coincidence and then use whichever wording is shorter"
figure: sifakis
works: [property-preserving-abstractions-1995]
axes: [expressiveness, cognitive-load, primitive-count]
subdomains: [formal-methods-and-verification, programming-languages-and-semantics, foundations-of-computation]
tags: [lesson]
---
# When two communities have separate words for the same idea, prove the coincidence and then use whichever wording is shorter

**Lesson:** Two research lines had each built a notion of "abstraction" for programs and had built it out of different material. One started from lattices of properties and defined an abstraction as a pair of functions moving between a concrete property lattice and a coarser one, subject to an adjointness condition. The other started from sets of states and defined an abstraction as a relation between concrete and abstract states under which the abstract machine can mimic the concrete one. The two definitions do not resemble each other — different carriers, different primitive notion, different intuition about what abstraction *is*. Sifakis and co-authors show they define the same thing, and the proof is constructive in both directions: from any relation between state sets you can manufacture the adjoint pair, and from any adjoint pair you can recover a unique relation.

The productive part is what happens after the theorem. Having established the identity, they explicitly refuse to standardize on one presentation. Some results are far easier to state when the abstraction is a relation — anything about mimicking, about totality, about composing relations. Others are far easier when it is a pair of functions — anything about images of property sets, about distributing over unions, about monotonicity. So they keep both notations in play and choose per result. This is only legitimate because the equivalence was proved once; without it, alternating vocabularies would be equivocation. With it, the alternation costs nothing and each theorem gets its cheapest proof.

The habit to steal is the response to a suspected duplicate concept. The reflex options are both bad: pick a winner and force everyone to translate, or build an adapter layer that keeps two things separate forever and adds a third thing to maintain. The third option is to spend the effort on an equivalence proof, which is a one-time cost that permanently licenses free movement between the two views. The signal that this is worth doing is when each community's results feel awkward when restated in the other's terms — awkwardness in translation is usually evidence that both notations are carrying real information about different aspects of one object, not evidence that one of them is wrong.

**Source:** [Property Preserving Abstractions for the Verification of Concurrent Systems](../works/property-preserving-abstractions-1995.md) — section 3.2's two propositions establishing that simulation parameterized by a Galois connection and simulation parameterized by a state relation induce each other, and the closing remark of that section declining to distinguish between them in the rest of the paper.
