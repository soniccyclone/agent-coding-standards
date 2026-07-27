---
type: lesson
title: "An arbitrary distinction in your constraint vocabulary is a defect in the vocabulary"
figure: fagin
works: [multivalued-dependencies-and-a-new-normal-form-for-relational-databases]
axes: [expressiveness, primitive-count]
subdomains: [databases-and-data-management]
tags: [lesson]
---
# An arbitrary distinction in your constraint vocabulary is a defect in the vocabulary

**Lesson:** The received vocabulary for describing data could say that one thing determines exactly one other thing, and had no way at all to say that one thing determines a whole set of other things independently of everything else present. That gap produced a strange asymmetry: a person's employer-assigned pay was expressible as a fact about them, while the person's children were not, even though both are equally facts about that person. Fagin's move was to read the asymmetry as evidence that the vocabulary was cut in the wrong place, and to define a weaker constraint whose special case (when the determined set is always a singleton) recovers the original one. The old notion did not have to be discarded; it was demoted to a corner of the new one.

The general principle is that when a formalism forces you to treat two structurally similar situations differently, and you cannot state a reason for the difference that lives in the problem rather than in the notation, the notation is imposing the difference. The test is cheap to apply: describe the awkward case in plain language and see whether the awkwardness survives translation. If a competent person describing the domain would use the same sentence shape for both cases, and your formalism needs two shapes, the formalism has an extra distinction that costs you expressiveness and buys nothing.

What follows from this in practice is a discipline about generalizing downward instead of adding sideways. The tempting response to an inexpressible case is a second, parallel construct with its own rules and its own interactions with everything already there. The better response is to look for the single weaker construct that has the existing one as a degenerate instance, because then the count of independent ideas does not grow and every result already proved about the old construct becomes a special case rather than a thing to re-derive. A programmer who believes this treats each new special-case mechanism in a codebase as a suspicion that some earlier abstraction was drawn too narrowly.

**Source:** [Multivalued Dependencies and a New Normal Form for Relational Databases](../works/multivalued-dependencies-and-a-new-normal-form-for-relational-databases.md) — the introductory comparison of the new dependency against the older single-valued one, including the response to the objection that a person "has" a set of things exactly as they "have" a single thing, and the proposition establishing the older notion as a special case of the new.
