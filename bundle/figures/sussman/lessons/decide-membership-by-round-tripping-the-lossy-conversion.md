---
type: lesson
title: "Decide whether a value really belongs to the simpler type by round-tripping the lossy conversion"
figure: sussman
works: [structure-and-interpretation-of-computer-programs]
axes: [verifiability, expressiveness]
subdomains: [software-engineering-and-architecture, formal-methods-and-verification]
tags: [lesson]
---
# Decide whether a value really belongs to the simpler type by round-tripping the lossy conversion

**Lesson:** Converting a value to a richer type is always safe; the reverse is not, and the reason is that the answer depends on the value rather than the type. A complex number with zero imaginary part is an ordinary number wearing extra structure; one with a nonzero imaginary part is not, and no fact about the type distinguishes them. The test the authors propose is to define the lossy conversion anyway — throw away the extra structure — then convert straight back up and ask whether you have what you started with. If yes, the discarded part carried nothing, and the value may be demoted. If no, it cannot.

What makes this worth extracting is the shape of the argument rather than the arithmetic. You want to know whether some information is redundant. Rather than reason about what the information means, you construct the operation that destroys it, undo that operation, and compare. The redundancy question becomes an equality question on values you can actually compute. That is a much easier thing to get right than a predicate written from first principles, and it stays right when the representations change, because it is defined in terms of the conversions rather than in terms of anybody's model of them.

The same instrument answers a second question people usually treat separately: whether a pair of conversions are honest inverses at all. A round trip that fails on values it should preserve is not telling you about that value; it is telling you your conversions disagree. So the test does double duty — as a runtime decision procedure for individual values and as a property to check across the whole conversion layer. It is worth deliberately conflating the two, because a demotion rule and an invertibility law are the same equation read in two directions.

The applications are everywhere a narrowing conversion exists: deciding whether a floating-point value is exactly an integer, whether a serialized record can use the compact form, whether a general query can be answered by the specialized index, whether a Unicode string fits an older encoding, whether a lossy compression was in fact lossless for this input. In every case the alternative — a hand-written predicate that tries to characterize the safe inputs directly — is a restatement of the conversion's semantics maintained separately from the conversion, which is precisely the kind of duplicated knowledge that drifts. Derive the predicate from the operation instead of asserting it alongside.

**Source:** [Structure and Interpretation of Computer Programs](../works/structure-and-interpretation-of-computer-programs.md) - chapter 2 section 2.5.2's discussion of lowering a data object in the tower of types, which notes that adding two complex numbers should ideally yield an integer rather than an integer plus zero times i and that the trick is to distinguish objects that can be lowered from those that cannot; and Exercise 2.85, which sets out the plan of defining a generic project operation that pushes an object down the tower, and deciding that a value can be dropped exactly when projecting it and raising the result back yields something equal to the original, then using a generic equality predicate and repeated dropping to simplify results inside apply-generic.
