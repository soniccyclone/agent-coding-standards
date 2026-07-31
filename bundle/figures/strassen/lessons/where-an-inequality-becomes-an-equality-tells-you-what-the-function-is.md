---
type: lesson
title: "Where an inequality turns into an equality tells you what kind of function you are holding"
figure: strassen
works: [the-asymptotic-spectrum-of-tensors]
axes: [expressiveness, cognitive-load]
subdomains: [algorithms-and-complexity, foundations-of-computation]
tags: [lesson]
---
# Where an inequality turns into an equality tells you what kind of function you are holding

**Lesson:** A cost function on composite objects usually satisfies only inequalities: the cost of a combination is at most the sum, at most the product, never reliably equal. It is tempting to file those inequalities as the sad but complete truth and move on. The productive move is to hunt for the region where each inequality is tight. If the function is merely sub-additive in general but exactly additive whenever the parts are built out of a single generator — every combination of powers of one fixed object gets its cost exactly, additively and multiplicatively — that is not a curiosity. It is a fingerprint. A maximum, taken over some index set, behaves exactly this way: sub-additive across unrelated things because the maximizing index may differ between them, exactly additive on a family where a single index maximizes everything at once. Reading the fingerprint tells you what the function is before you can prove it: not a cost, but the extreme value of a family of costs you have not yet identified.

Once suspected, that hypothesis is testable and it dictates the next move: find the family. Every element of the family must be monotone with respect to the underlying order and must respect combination exactly rather than approximately, so the exactness you observed on the one-generator families is exactly the constraint that pins the candidates down. The mirror observation is worth the same attention: a companion function that is only super-additive in general but again exactly additive on the same one-generator families is a minimum over the same family, and finding the two together is stronger evidence than either alone, because a single family that explains both fingerprints is far more constrained than one explaining one.

Read as method, this is the habit of treating the boundary case of an inequality as the primary evidence rather than an edge case to be noted and dismissed. Anywhere you have a bound and not an identity, ask on which inputs the bound is attained, and what class of function has exactly that pattern of tightness. Answers of the form "it is an extremum of something" are especially likely, because sub- and super-behavior with pockets of exactness is what optimization over a hidden parameter always looks like from outside. The failure of a quantity to be exactly compositional is often the shadow of a parameter you have integrated away without noticing, and locating that parameter is what converts a collection of estimates into a theory.

**Source:** [The Asymptotic Spectrum of Tensors](../works/the-asymptotic-spectrum-of-tensors.md) — the introduction's account of what set the investigation off: asymptotic rank is only subadditive and submultiplicative in general but becomes exactly additive and multiplicative when restricted to nonnegative polynomials in a single fixed element, which the paper reads as the behavior of a maximum functional on a cone of nonnegative continuous functions over a compact space, with asymptotic subrank exhibiting the corresponding minimum behavior; section 3 then confirms both readings.
