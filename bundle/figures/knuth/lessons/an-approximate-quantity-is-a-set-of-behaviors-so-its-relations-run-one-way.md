---
type: lesson
title: "An approximate quantity is a set of behaviors, so relations over it legitimately run one way only"
figure: knuth
works: [big-omicron-and-big-omega-and-big-theta]
axes: [verifiability, cognitive-load, expressiveness]
subdomains: [algorithms-and-complexity, formal-methods-and-verification]
tags: [lesson]
---
# An approximate quantity is a set of behaviors, so relations over it legitimately run one way only

**Lesson:** The pivotal definitional choice in this letter is easy to skim past: the growth-rate symbols are defined to denote *sets* of functions, not "some unspecified function with a property." Knuth credits the improvement to a suggestion he received and says plainly it is the right way to define the notation, replacing what he had originally published. The consequence is that arithmetic written with these symbols is arithmetic on sets — adding two of them means forming all the pairwise sums — and the familiar equals sign appearing in such formulas is not equality at all but containment. Which is why the well-known asymmetry follows: a tight expression sits inside a loose one, never the reverse, and the direction you may read the statement in is fixed by which side is the smaller set.

The reasoning generalizes past asymptotics. Any time you write about a quantity you only know approximately — a bound, an interval, a range of acceptable outcomes, a type that admits many values, a specification that permits many implementations — the object you are manipulating is a set of possibilities, and the relation you can establish between two such objects is refinement, not identity. Refinement has a direction. Treating it as symmetric is the standard way to derive nonsense from correct premises: you prove a program satisfies a loose contract, then read the contract backward as a description of the program. Knuth's set-valued reading makes the asymmetry structural rather than a caveat you must remember.

Notice what he then declines to do about it. Several people wanted the equals sign banned in this context, since it means something other than equality. He keeps it, on the grounds that the usage is long-established, universally understood by its readers, and does not in practice mislead the people who use it. That is not laziness; it is a claim about where the risk actually lives. A notation whose surface form overstates its formal strength is safe exactly when its community shares an accurate model of what it means, and dangerous when it does not — and the paper's own opening shows what the dangerous case looks like, since the abuse he set out to correct was a case where the shared model had genuinely broken down. The judgment being modeled is that you tolerate a notational compromise in proportion to how reliably readers decode it, and you fix the notation when they stop.

A programmer who takes this on board writes bounds and contracts in a form that makes the permitted direction of inference explicit, and stops reading specifications as descriptions. The upper bound you proved is a claim about the worst case only; it authorizes no statement about how the code typically behaves, and any argument that quietly reverses the inclusion is broken no matter how plausible its conclusion.

**Source:** [Big Omicron and Big Omega and Big Theta](../works/big-omicron-and-big-omega-and-big-theta.md) — the passage defining the notations as sets of functions rather than individual functions, and the ensuing defence of one-way equalities against critics who wanted the equals sign disallowed.
