---
type: lesson
title: "Pose the question as a ratio between rival explanations so the term you cannot compute cancels"
figure: turing
works: [the-applications-of-probability-to-cryptography]
axes: [verifiability, cognitive-load, primitive-count]
subdomains: [algorithms-and-complexity, foundations-of-computation]
tags: [lesson]
---
# Pose the question as a ratio between rival explanations so the term you cannot compute cancels

**Lesson:** There is a recurring shape to hard quantitative problems: the thing you want is blocked behind a factor that is either enormously expensive to evaluate or has no closed form at all. Asking "how likely is this explanation?" in absolute terms drags in the whole space of alternatives and a normalizing quantity you cannot write down. Asking instead "how much better is this explanation than that one?" leaves you with a quotient in which the blocking factor appears identically in numerator and denominator and simply disappears. The unanswerable question was never the one you needed; the answerable relative question drives the same decision, because decisions are always choices between options rather than assignments of absolute merit.

This is worth internalizing as a design reflex, not a trick, because the cancelling term is often the part you could not have computed even in principle. When the shared factor is a combinatorial count over configurations, or the total measure of an open-ended space of possibilities, the comparative formulation is the only formulation that terminates. It also composes: once results are expressed as ratios, independent pieces of evidence multiply, and a long accumulation of small comparisons becomes a single running score. There is a real cost, and it should be stated rather than glossed. Comparing two named explanations silently assumes those two are the only candidates, and the space of explanations is never closed — so the discipline that comes with the technique is to keep asking what third explanation would also have produced this evidence, since the arithmetic will never volunteer it.

The programming version shows up whenever you are tempted to compute an absolute quantity in order to rank things. Scoring, ranking, plan selection in a query optimizer, choosing between candidate parses or candidate repairs — in every case the expensive normalizing work is wasted, because the ordering survives dropping any factor common to all candidates. A programmer who thinks this way asks, before writing the expensive part, whether it will be identical across everything being compared. If it will, that code should not exist. What replaces it is a comparison function and an explicit list of the rival hypotheses being entertained, which is both cheaper and more honest about the assumption being made.

**Source:** [The Applications of Probability to Cryptography](../works/the-applications-of-probability-to-cryptography.md) — the factor principle in the introduction and its use in the theory of repeats, where an intractable count of possible patterns appears on both sides of the comparison and drops out, together with the introduction's warning that framing the problem as two rival possibilities is itself an approximation.
