---
type: lesson
title: "Choose an encoding by the law you need it to satisfy, not by which one looks natural"
figure: scott
works: [data-types-as-lattices]
axes: [expressiveness, verifiability, cognitive-load]
subdomains: [programming-languages-and-semantics, foundations-of-computation, software-engineering-and-architecture]
tags: [lesson]
---
# Choose an encoding by the law you need it to satisfy, not by which one looks natural

**Lesson:** Scott spends a whole section building on one encoding of pairs, and then, when the setting shifts to a different class of operations, throws it away. His reason is exact rather than aesthetic: under the new constraints the old pairing fails to satisfy a particular identity, and the replacement is picked precisely because it does. He does the same thing one paragraph earlier with the encoding of truth values, noting that the natural definition does not have the property now required and adopting a modified one for the duration. In both cases the discarded version is described as the natural one, and in both cases naturalness turns out to be no defense.

That is the point worth internalizing. An encoding is natural relative to some purpose — it was chosen because it made the operations in play at the time come out cleanly, and it wears the label because nobody has changed the operations since. When the operations change, the naturalness expires silently. Nothing warns you; the encoding continues to look canonical and continues to be the one anyone would write down first. So the reliable procedure is inverted from the usual one: write down the identities the representation must satisfy — the equations consumers will actually lean on — before choosing it, and design backwards to something that satisfies them. Picking the obvious representation first and discovering afterward which laws it lacks is the same work in a worse order, done after code has been written against it.

The second half of the move is equally worth copying: he does not go back and unify. The earlier encoding remains correct for the earlier section's purposes, the new one holds for this section's, and each is stated where it applies. Two encodings of the same concept coexisting with explicitly different regions of validity is a legitimate outcome rather than a failure of taste. What is not legitimate is leaving the reason unrecorded — because an unexplained switch from the obvious representation to a stranger one is exactly the thing a later reader will helpfully simplify back, taking the law with it.

**Source:** [Data Types as Lattices](../works/data-types-as-lattices.md) — the opening of Section 5, where Scott notes that the natural definition of the boolean retract does not yield a closure operation and adopts a modified definition for the section, then replaces the earlier pairing function because it leads to projections rather than closures, giving the new one together with its inverses and stating that its main advantage is an identity that does not hold for the other pairing functions.
