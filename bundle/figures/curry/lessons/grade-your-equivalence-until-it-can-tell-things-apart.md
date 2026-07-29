---
type: lesson
title: "Grade your notion of sameness until it is sharp enough to show what a rule cannot prove"
figure: curry
works: [grundlagen-der-kombinatorischen-logik]
axes: [verifiability, primitive-count]
subdomains: [foundations-of-computation, formal-methods-and-verification]
tags: [lesson]
---
# Grade your notion of sameness until it is sharp enough to show what a rule cannot prove

**Lesson:** Showing that a rule follows from the others is a search; showing that it does not is a different kind of task, and it cannot be done by failing to find a derivation. What it needs is a property preserved by every rule you keep and violated by the one you are testing. Curry's move is to refuse a single notion of "these two behave the same" and instead build a graded family of them, each obtained by adding one more thing you insist must match: the same set of arguments genuinely consumed, then the same arrangement of them, then the same count of how deep a nested argument had to be disturbed before the arrangement emerged, then the same class of reduction step needed to get there. Four progressively finer readings of one informal word.

With the family in hand the independence arguments become short. Prove that a given group of rules can only ever relate expressions that agree at some coarse grade; then exhibit two expressions that agree at that grade but disagree at the next one and are nevertheless related by the rule under test; conclude that the rule is not a consequence. Curry runs this twice, in opposite directions, to separate two whole classes of his axioms from each other — and the same instrument, pointed the other way, yields the positive results too, since agreement at the finest grade turns out to be necessary and sufficient for provable equality between well-behaved operators. One apparatus, built once, settles derivability and non-derivability together.

The general habit is to invest in the measuring instrument before the argument, and to expect the instrument to be finer than intuition suggested. The auxiliary notions Curry needs to state his grades — which arguments a term essentially uses, which get disturbed during evaluation, which reduction steps happen at the top and which inside a subterm — are not decoration. They exist because coarser vocabulary cannot separate the cases, and inventing them is most of the work. He is also candid about scope: this is the only such investigation in the work, and general consistency and completeness are explicitly out of bounds. A sharp instrument aimed at one question beats a vague ambition aimed at all of them.

For a programmer the transfer is direct. Claims that a feature is redundant, that a configuration knob does nothing, that two code paths are interchangeable, or that an optimization is safe, are all claims about an equivalence — and they are unfalsifiable until someone says which observations count. Defining several equivalences of increasing strictness, and naming which one each claim is made under, converts arguments about redundancy into checkable propositions and usually reveals that different people were using different ones. It also gives the only honest route to "you cannot remove this": here is what everything else preserves, and here is where this one breaks it.

**Source:** [Grundlagen der kombinatorischen Logik](../works/grundlagen-der-kombinatorischen-logik.md) — the opening section of Chapter II's representation chapter, where four senses of equivalence are defined on top of auxiliary notions of essential occurrence, disturbance and kind of reduction step, and the two independence theorems that follow from them, together with the later characterization of provable equality for regular operators.
