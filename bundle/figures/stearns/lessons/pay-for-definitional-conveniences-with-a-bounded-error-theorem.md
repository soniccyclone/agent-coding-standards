---
type: lesson
title: "Pay for every convenience in a definition with a theorem bounding what it cost you"
figure: stearns
works: [on-the-computational-complexity-of-algorithms]
axes: [verifiability, primitive-count]
subdomains: [foundations-of-computation, formal-methods-and-verification]
tags: [lesson]
---
# Pay for every convenience in a definition with a theorem bounding what it cost you

**Lesson:** Definitions accumulate conveniences: a relaxation that makes the proofs go smoothly, a permission that avoids an irritating special case. Each one is a debt, because each one is a place where a sceptic can say the results are artifacts of the setup rather than facts about the subject. The debt is dischargeable, and the way to discharge it is not to argue that the convenience is harmless but to prove how much it is worth. Allowing a bounded amount of output per step rather than exactly one digit is such a convenience; the honest treatment is a run of results showing that under the strict convention the whole theory shifts by at most an arbitrarily small proportion, so that the tiniest increase in speed erases the distinction entirely. Now the convenience is not defended, it is priced, and the sceptic's objection has a number attached to it.

The same discipline applies to guard conditions. A definition usually needs a side condition to exclude degenerate cases, and there is a temptation to pick a round, comfortable one. The better practice is to derive the condition from the degeneracy it is meant to exclude and then prove it is exactly tight — show that below the threshold the object is necessarily empty and that at or above it the object is necessarily nonempty. A guard derived this way carries information: it tells the reader what would go wrong and where the boundary genuinely is. A guard chosen for tidiness tells them only that you wanted to avoid thinking about something, and it leaves open whether the interesting cases were excluded along with the degenerate ones.

Both habits transfer directly to specifications, APIs and data models, where the equivalent conveniences are the permissive field, the tolerated duplicate, the accepted denormalisation. The rule is the same in each case: state the convenience explicitly rather than letting it hide in the schema, then bound its consequence — how far the permissive version can diverge from the strict one, and under what added assumption they coincide. Conveniences with stated bounds are engineering. Conveniences without them are the mechanism by which a design's guarantees quietly become approximate, and the drift is undetectable precisely because nobody ever wrote down what was given away.

**Source:** [On the Computational Complexity of Algorithms](../works/on-the-computational-complexity-of-algorithms.md) — the definition of the complexity classes together with its two side conditions: the derivation showing that the growth-rate guard is exactly the boundary between an empty and a nonempty class in both directions, and the sequence of corollaries establishing that the allowance of several output digits per square changes the theory by at most an arbitrary epsilon and is wiped out by the slightest increase in operation speed.
