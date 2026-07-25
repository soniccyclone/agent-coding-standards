---
type: lesson
title: "Write down what must be decided before deciding how to decide it, and let the algorithm be answerable to that statement"
figure: cardelli
works: [basic-polymorphic-typechecking, structural-subtyping-and-the-notion-of-power-type, a-semantics-of-multiple-inheritance]
axes: [verifiability, cognitive-load]
subdomains: [formal-methods-and-verification, programming-languages-and-semantics]
tags: [lesson]
---
# Write down what must be decided before deciding how to decide it, and let the algorithm be answerable to that statement

**Lesson:** An analysis pass explained as a walk over a data structure is nearly impossible to evaluate. You cannot tell which of its behaviours are essential and which are artefacts of traversal order, whether two implementations agree, or what it would mean for it to be wrong. The alternative is to state the analysis first as a set of rules saying what conclusions follow from what premises, with no commitment to order or representation, and only then write code that searches for derivations. The rule set is smaller, it outlives the implementation technology, and it gives the code something to be correct with respect to. A pleasant side effect is that the natural presentation of the algorithm becomes the rule set plus a search strategy, which is far easier to teach than a walk with accumulated state.

This layering supports a chain of accountability that no single artefact could provide. The rules are held answerable to a meaning, so that anything derivable is true of the values involved; the implementation is held answerable to the rules, so that anything it accepts was derivable. Composing the two gives the property actually wanted, which is that accepted programs cannot fail in the ways the analysis was built to exclude. It also legitimizes a deliberate gap: an implementation may be strictly more conservative than the rules permit, rejecting things that are technically derivable but always useless in practice, and because the two artefacts are separate this can be a documented choice rather than an unexplained quirk. Completeness with respect to the rules is then something you knowingly forgo, not something you accidentally lack.

The separation also reveals which properties are structural rather than incidental. If the outcome of the analysis is independent of the order in which constraints are discovered, that fact belongs to the rule system, and knowing it frees the implementation to pick whatever traversal is cheapest. Without the rule system there is nowhere to state such a property, let alone prove it, and every performance change becomes a risk to correctness.

A practitioner who works this way separates the specification of a check from its schedule, states the meaning the specification answers to, and treats deviations of the implementation as recorded decisions. The alternative, which is a checker whose only definition is its code, leaves you unable to distinguish a bug from a design.

**Source:** [Basic Polymorphic Typechecking](../works/basic-polymorphic-typechecking.md) — the digression on models, inference systems, and algorithms, which argues that the system is more fundamental than any procedure implementing it, together with the two presentations of the same check as a constraint system and as a bottom-up synthesis. Also [Structural Subtyping and the Notion of Power Type](../works/structural-subtyping-and-the-notion-of-power-type.md) — the note that its rules deliberately specify a superset of what a checker should do, being easier to understand and less dependent on implementation technology. Also [A Semantics of Multiple Inheritance](../works/a-semantics-of-multiple-inheritance.md) — the layered soundness argument from algorithm to inference system to semantics, and the explicit decision to make the algorithm stricter than the system.
