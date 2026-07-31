---
type: lesson
title: "A requirement that must hold for every interpretation pins down what testing against yours cannot"
figure: scott
works: [data-types-as-lattices]
axes: [verifiability, expressiveness, cognitive-load]
subdomains: [formal-methods-and-verification, programming-languages-and-semantics, foundations-of-computation]
tags: [lesson]
---
# A requirement that must hold for every interpretation pins down what testing against yours cannot

**Lesson:** Scott gives the basic combinators their typing properties — statements of the form "this thing maps things related in one way to things related in another" — and stipulates that the properties must hold for *every* relation, not for some fixed collection of interesting ones. Then he reports something much stronger than the properties themselves: they determine the combinators uniquely. There is exactly one object that behaves correctly under every possible interpretation of the relations, and it is the one you wanted. Behaving correctly for all interpretations, including the ones nobody would ever choose, turns out to be a constraint heavy enough to leave no room.

The mechanism is worth stealing wholesale. Because the requirement is quantified over all interpretations, whoever is reasoning about the object gets to *pick* the interpretation, and picks the most hostile one available — Scott specializes to a relation containing a single pair and nothing else, which collapses the general property immediately into the exact equation he needed. That inverts the usual way of gaining confidence in a component. Exercising it against the interpretations you expect tells you comparatively little, because it can succeed for reasons peculiar to those interpretations; requiring it to work under interpretations carrying no structure at all removes every place a peculiarity could hide. The design consequence: state your requirements over an unrestricted range of instantiations, even ones that seem pathological, because the pathological ones are where the requirement acquires its force.

The paper also models what to do when the pinning-down turns out not to be airtight. Scott states the uniqueness result and then walks it back with precision: for one of the combinators, the typing property alone does not identify it — you must additionally know that it treats its first arguments as functions of the right shape, and only with that clause does the characterization go through. He names the extra condition instead of leaving the headline claim standing. That is the discipline to copy whenever you assert that a specification determines an implementation: go looking for the degenerate things that satisfy the letter of it, and either add the clause that rules them out or downgrade the claim to what you can actually defend.

**Source:** [Data Types as Lattices](../works/data-types-as-lattices.md) — Section 7's functionality theorem, which gives typing properties for the basic combinators holding for all equivalence relations and states that these properties determine the combinators uniquely; the proof sketch that specializes to a one-pair relation to force the defining equation; the exact restatement Scott supplies for the case where the typing property alone does not determine the combinator without an additional condition on how it treats its arguments; and Plotkin's iterator theorem with its analogous proviso.
