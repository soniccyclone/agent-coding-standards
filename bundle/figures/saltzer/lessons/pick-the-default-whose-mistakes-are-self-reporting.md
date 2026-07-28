---
type: lesson
title: "Pick the default whose mistakes are self-reporting"
figure: saltzer
works: [the-protection-of-information-in-computer-systems]
axes: [verifiability, cognitive-load]
subdomains: [operating-systems-and-systems-programming, software-engineering-and-architecture]
tags: [lesson]
---
# Pick the default whose mistakes are self-reporting

**Lesson:** Two designs can be logically equivalent in the cases their authors
thought about and radically unequal in the cases they forgot. Enumerate the
conditions under which something is allowed, and an omission produces a refusal —
annoying, immediate, and reported by whoever hit it. Enumerate the conditions under
which something is forbidden, and the identical omission produces a silent
permission that nobody notices and nobody reports. Same logic, same amount of code,
same author skill. The difference is entirely in which direction the inevitable gaps
lean, and in a system large enough that some cases will certainly be overlooked, that
direction dominates the outcome.

This generalizes past access control into a way of choosing among any set of
otherwise-equal formulations: prefer the one whose characteristic failure mode is
loud. Frame rules as allow-lists rather than deny-lists. Make the unconfigured state
the inert one. Have a parser reject unrecognized input rather than ignore it. In
each case you are not making errors less likely — you are arranging for the errors
you will make anyway to arrive as complaints instead of as quiet wrongness. A
complaint costs you a support ticket. Quiet wrongness costs you the ability to know
the state of your own system.

The argument also identifies where the reasoning has to be done. A deny-list invites
you to think about the bad cases, which is the wrong direction of thought because the
bad cases are open-ended and adversarial and you cannot finish the list. An
allow-list forces you to say, for each thing you are permitting, why it should be
permitted — a closed question, answerable, and reviewable later by someone who was
not there. The formulation shapes what its author is obliged to justify, and that
obligation is where correctness actually comes from.

**Source:** [The Protection of Information in Computer Systems](../works/the-protection-of-information-in-computer-systems.md)
— the fail-safe-defaults principle in Section I, whose justification turns on the
asymmetry between a mistake in a permission-granting mechanism, which fails toward
refusal and is quickly detected, and a mistake in an exclusion mechanism, which fails
toward access and goes unnoticed in ordinary use.
