---
type: lesson
title: "Two accounts agreeing is evidence in proportion to how far apart they are"
figure: scott
works: [data-types-as-lattices]
axes: [primitive-count, expressiveness, verifiability]
subdomains: [foundations-of-computation, formal-methods-and-verification]
tags: [lesson]
---
# Two accounts agreeing is evidence in proportion to how far apart they are

**Lesson:** The standard argument that a definition captures an informal notion is that several independently proposed definitions turned out equivalent. The argument is sound in form and is routinely applied without checking the quantity it depends on: how far apart the definitions actually were. If two formalisms are near neighbors — if the translation between them is a short exercise in encoding, a few tricks with pairing functions and indices — then their agreement is close to a restatement and carries little weight about the informal notion either of them was supposed to capture. The evidential content lives entirely in the distance covered, and that distance has to be assessed on its own, not inferred from the fact that the proof took effort to find the first time.

Scott makes this case against a specific piece of received reasoning. The equivalence of definability in a small function calculus with partial recursiveness is usually cited as strong support for the thesis identifying effective calculability with those notions, on the grounds that two widely different and equally natural definitions coincided. His objection is that the divergence is not wide at all: the calculus reduces to elementary operations on enumerable sets of integers, the equivalence proofs are all easy, and the pleasant surprise that a great deal can be defined with very few primitives cuts the wrong way as evidence, since what you want is agreement with a *stronger* framework rather than a weaker one. What would count is a definition that is natural on its own terms and whose equivalence is not a mechanical coding exercise; frameworks that are obviously more inclusive make a better witness than ones that are obviously more austere.

Applied outside foundations, this is a rule about corroboration generally. Two implementations that agree tell you little if one was derived from the other or both descend from the same design; two tests that pass tell you little if they exercise the same path with different literals. Independence is the whole of the evidence, and it is a property you have to argue for explicitly, because agreement looks the same whether it was earned or inherited. The corollary is a preference worth holding: when you get to choose a second account to check against, pick the one that is most unlike the first, even at the cost of a harder comparison.

**Source:** [Data Types as Lattices](../works/data-types-as-lattices.md) — the discussion following the definability theorem in Section 2, which quotes Church's footnote arguing that the equivalence of two widely different and equally natural definitions strengthens the case for the thesis, and replies that the reduction of the calculus to enumeration-operator theory shows the divergence is not wide, that the equivalence proofs are all easy, that greater definability from fewer primitives is the wrong direction for evidence, and that Post systems or first-order theories would be better witnesses because they are more obviously inclusive.
