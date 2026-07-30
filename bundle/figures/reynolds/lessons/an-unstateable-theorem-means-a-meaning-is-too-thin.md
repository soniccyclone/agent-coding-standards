---
type: lesson
title: "A theorem you cannot even state is telling you some construct's meaning is too thin"
figure: reynolds
works: [towards-a-theory-of-type-structure]
axes: [verifiability, expressiveness]
subdomains: [programming-languages-and-semantics, foundations-of-computation]
tags: [lesson]
---
# A theorem you cannot even state is telling you some construct's meaning is too thin

**Lesson:** There is a distinct and valuable kind of failure that comes before any attempt at proof: writing down the property you want and finding that one of its clauses does not denote anything. The instance here is exact. The desired guarantee says that programs evaluated under corresponding implementations produce corresponding results, where the correspondence used is the one belonging to the relevant type. But correspondences had been supplied only for the atomic type names, so the phrase "the correspondence belonging to this type" is undefined the moment the type is compound. The instinct to patch this by supplying correspondences for compound types directly is wrong, and the reason is worth internalizing: once you have fixed how two implementations correspond at the base types, the correspondence at any type built from them is not yours to choose. It is already determined. A definition that lets you choose it is admitting configurations that cannot arise.

The correct diagnosis is that the meaning assigned to type expressions was too thin all along. It had been treated as a function taking an assignment of implementations to base names and yielding an implementation — enough to say what a type denotes, not enough to say how two denotations correspond. Enriching it so that it also carries assignments of correspondences to correspondences makes the theorem statable, and the enrichment is not an add-on: the same construction on type expressions has to act coherently on both, so that building a compound type and then relating the results agrees with relating the parts and then building. The general move is to notice that an entity's meaning has two jobs — saying what it produces, and saying how it transports relationships between things it produces — and that a semantics giving only the first will not support any theorem about variation.

Two habits follow. When a property resists formalization, resist the urge to weaken the property; check first whether some construct's meaning is impoverished, because enriching a meaning usually leaves you with the strong property intact, whereas weakening the property is permanent. And when you do enrich, insist on the coherence conditions rather than treating them as pedantry — they are what make the extension forced rather than invented, and an extension that is forced cannot be got wrong in a way that only shows up three proofs later.

**Source:** [Towards a Theory of Type Structure](../works/towards-a-theory-of-type-structure.md) — the representation-theorem section, where the preliminary statement is shown to have a serious flaw because representations are assigned only to type variables and cannot be assigned arbitrarily to compound type expressions, together with the conclusion that the meaning of type expressions had been underestimated and must map assignments of representations into representations, and the following section's requirement that this extension respect the composition and identity laws.
