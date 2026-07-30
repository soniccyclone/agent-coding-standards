---
type: lesson
title: "The checks you ship are the only checks you have, and every failure must be explicable in the user's own vocabulary"
figure: hoare
works: [hints-on-programming-language-design]
axes: [verifiability, cognitive-load]
subdomains: [programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# The checks you ship are the only checks you have, and every failure must be explicable in the user's own vocabulary

**Lesson:** A recurring and comfortable design position is that safety checking belongs to a special diagnostic mode — a checking build, a debug configuration, an instrumented run — which is turned off for production. Take that arrangement apart and the argument for it disappears. It gives you two artifacts instead of one, which are unlikely to be equally trustworthy, and which cannot be guaranteed to agree on the very inputs where agreement matters most: a subtly wrong program. When they disagree, nothing in the setup helps you locate the discrepancy, because the discrepancy is between two implementations rather than inside one program. The checked version costs more time and more space, so the largest and most difficult cases — the ones that most need checking — are the ones that cannot afford it. And the whole scheme applies its strictest scrutiny to runs whose results nobody trusts, then withdraws that scrutiny for the runs whose results are acted upon and where a wrong answer is expensive. Build the guarantee into the single thing you ship, and the awkward question of which mode you are in never arises.

The companion requirement is about the vocabulary of failure. Some errors genuinely cannot be caught before running; those must be cheap to detect at run time. What must never happen is a program error that produces an effect only describable in terms of the layer underneath — hardware behavior, allocator internals, whatever the implementation happens to do this week. An effect that cannot be explained within the abstraction's own terms is not a diagnosable error but a leak, and it forces every user of the abstraction to reason at two levels simultaneously in order to reason at all. The property to design for is that a program's every observable behavior, including its misbehavior, has an account in the language the programmer wrote it in.

Both halves rest on a prior condition that is usually left implicit: the tool itself must be reliable enough that a user attributes surprising behavior to their own work by default. The moment that confidence is gone, every debugging session forks into a second investigation about whether the tool is at fault, and the cost of that fork dwarfs whatever was saved by shipping a tool that was fast to build.

**Source:** [Hints on Programming Language Design](../works/hints-on-programming-language-design.md) — the treatment of security as a design criterion in the Principles and Security discussion sections, including the argument against relying on a separate checkout compiler and the requirement that no error yield implementation-dependent effects.
