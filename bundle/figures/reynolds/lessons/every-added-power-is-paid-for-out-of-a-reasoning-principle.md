---
type: lesson
title: "Every expressive power you add is paid for out of a reasoning principle, so find out which one before you spend it"
figure: reynolds
works: [types-abstraction-and-parametric-polymorphism]
axes: [expressiveness, verifiability]
subdomains: [programming-languages-and-semantics, formal-methods-and-verification]
tags: [lesson]
---
# Every expressive power you add is paid for out of a reasoning principle, so find out which one before you spend it

**Lesson:** Adding a construct to a language is usually discussed as if the only question were whether it can be given a meaning. The more informative question is which of your existing guarantees stops holding. Extending a well-behaved calculus with general recursion, and with the weakened conditional that recursion forces, is enough to break the central property that implementations agreeing on their abstract types agree everywhere — not weaken it, break it. Recovering the property costs a restriction elsewhere: the correspondences you are permitted to consider must be closed under the limits that recursion introduces, which excludes some correspondences that were previously legitimate. The feature was affordable, but it was not free, and the price was taken out of the reasoning apparatus rather than out of the runtime.

The habit worth forming is to run this accounting deliberately, before the feature ships rather than after a proof mysteriously fails. Ask which theorem was load-bearing, check it against the new construct, and if it fails, look for the smallest restriction on the reasoning side that restores it. Doing the audit in this order also protects you from a subtler failure: the repair often narrows what you may assume in ways that only bite much later, in a proof nobody has written yet, so the restriction needs recording as a standing constraint and not as an incidental step in one argument.

The same audit exposes when the fault lies in the model rather than the feature. If a construct interacts badly with an element of your semantic universe that has no counterpart in the phenomenon you are modelling — an overdefined value with no operational meaning, say — the resulting difficulty is an artifact of over-equipping the model, and it can be settled either by refusing to let that element relate to itself or by choosing a universe that never contained it. Distinguishing the two kinds of breakage matters, because one tells you something real about the feature and the other only tells you that you brought too much apparatus. Symmetrically, the audit can come back clean: a construct that can be defined by translation into what you already have adds no reasoning burden at all, which is the right reason to admit convenient notation freely while keeping the set of genuinely primitive constructs small.

**Source:** [Types, Abstraction, and Parametric Polymorphism](../works/types-abstraction-and-parametric-polymorphism.md) — the section moving from sets to domains, where the fixed-point operator and extended conditional cause the abstraction theorem to fail and completeness of relations is imposed to restore it, including the parenthetical on overdefined elements; together with the remarks that the primitive-operation form of type definition, and later existential type quantification, are definable from the constructs already present.
