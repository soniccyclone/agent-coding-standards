---
type: lesson
title: "A smaller basis is a purchase, not a free win"
figure: schonfinkel
works: [bausteine-der-mathematischen-logik]
axes: [primitive-count, cognitive-load, expressiveness]
subdomains: [foundations-of-computation, programming-languages-and-semantics]
tags: [lesson]
---
# A smaller basis is a purchase, not a free win

Shrinking the set of undefined starting notions is a real goal, distinct from shrinking the set of axioms, and Schönfinkel opens by insisting on it: hunt for the notions from which every other notion in the field can be built. But he attaches a price tag in the same breath. Once you select primitives for generative reach, you must lower your expectation that each one be individually intuitive. The two demands — small basis, obvious basis — pull against each other, and the honest move is to name which one you are sacrificing rather than pretending a minimal basis is simply better.

The paper then supplies the counterweight, which is the part usually forgotten. Having driven the reduction down to three signs, he observes that a single sign suffices if you introduce an operator that merely dispatches on which of the others it is handed. Formally the count drops to one. He rejects it anyway, calling the arrangement plainly arbitrary and of scarcely any real significance. The reduction was achieved by encoding a tag, not by finding structure, and a tag explains nothing. He does accept a different one-level saving in the same section, because there the sign disappears for a reason internal to the calculus rather than by fiat.

So the number of primitives is a diagnostic, not the objective. A basis earns its smallness when the remaining pieces recombine to reach everything by their own composition behavior, and when the collapse tells you something you did not already know. A basis reached by folding distinctions into a discriminator has the same headline count and none of the content. The two cases look identical if you are only counting.

A programmer who holds this reads any claim of minimality by asking what did the work. Fewer built-in forms in a language, fewer opcodes, fewer core abstractions: each is worth having only if the survivors compose to cover the removed cases, and only if the resulting programs are still explicable. Otherwise you have relocated the complexity into a dispatch table and made the system harder to reason about while improving a metric nobody should have been optimizing directly. Correspondingly, when a genuine reduction does cost intelligibility at the small scale, that is an acceptable bill — provided you noticed you were paying it.

**Source:** [Über die Bausteine der mathematischen Logik](../works/bausteine-der-mathematischen-logik.md) — the opening section's framing of the axiomatic method as minimizing undefined concepts and its warning about the resulting loss of simplicity, together with the final section's construction and immediate dismissal of a single-symbol basis.
