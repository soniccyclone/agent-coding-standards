---
type: lesson
title: "One new construct can turn meaning from a fact into a choice you must justify"
figure: ullman
works: [assigning-an-appropriate-meaning-to-database-logic-with-negation]
axes: [expressiveness, verifiability, cognitive-load]
subdomains: [databases-and-data-management, programming-languages-and-semantics, formal-methods-and-verification]
tags: [lesson]
---
# One new construct can turn meaning from a fact into a choice you must justify

There is a comfortable regime in language design where meaning is not up for
debate. Rules without negation have exactly one minimal reading, everyone agrees
it is the reading, and a designer never has to argue for it. Ullman's survey is a
record of what happens when you cross out of that regime by adding a single
capability. Permit a rule to depend on something *not* holding, and the guarantee
of a unique intended reading evaporates: the same rules over the same data now
satisfy several equally consistent readings, some of which assert conclusions
supported by nothing at all. Nothing became ambiguous in the syntax. What was lost
was a mathematical property the old fragment had been silently providing.

The instructive part is what cannot rescue you. The traditional logical answer —
take only what follows from the rules and nothing more, the common part of all
consistent readings — is well defined and turns out to be the wrong answer, in the
plain sense that it is not what the person who wrote the rules meant. So the field
had to abandon the classical reading and build something new: an explicit theory
of which reading to prefer, along with a reinterpretation in which the direction
of an implication carries weight it does not carry in classical logic. The
criterion for that theory is not internal consistency, which the bad readings also
have, but agreement with what a competent author expects. Formal respectability
and being right are different tests, and only the second one matters here.

For anyone designing a notation — a query language, a configuration format, a
build system, a policy or effect language — the transferable move is to know which
property of your restricted fragment is buying you unambiguous meaning, and to
treat any feature that breaks it as a semantics project rather than a feature
request. Defaults, overrides, exclusions, absence tests and cancellation rules are
all this same feature in disguise: each one is a way for a specification to depend
on something *not* being present, and each one can admit self-supporting readings
where a specification appears to justify itself. The discipline is to write down
your preference rule, state it as deliberately chosen rather than inherited from
logic, and validate it against cases where users have firm expectations — because
once several readings are consistent, no amount of formal machinery will pick the
intended one for you.

**Source:** [Assigning an Appropriate Meaning to Database Logic with Negation](../works/assigning-an-appropriate-meaning-to-database-logic-with-negation.md) — the motivation and model-selection sections, which contrast the unique reading of negation-free rules with the multiple minimal readings of the two-bus-line monopoly example, and explain why the field replaced classical negation with a preference theory over models.
