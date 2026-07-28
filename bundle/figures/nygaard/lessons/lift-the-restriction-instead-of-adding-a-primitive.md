---
type: lesson
title: "Find The Arbitrary Restriction On What You Already Have"
figure: nygaard
works: [simula-67-common-base-language]
axes: [primitive-count, expressiveness, cognitive-load]
subdomains: [programming-languages-and-semantics, programming-environments-and-object-systems]
tags: [lesson]
---
# Find The Arbitrary Restriction On What You Already Have

**Lesson:** The object in Simula 67 was not invented; it was released. The report's opening reasoning starts from a construct already present in the language it extends — a lexical region that pairs data declarations with actions, exists in the text as a pattern, and materializes as an instance when entered. Two accidental limits made that construct useless as a modelling unit: instances had to nest strictly inside one another, and an instance died when control left it. Remove those limits, add a way to name an instance from outside, and the same construct becomes a class whose instances can coexist, be arranged in whatever structure the problem suggests, and act in interleaved bursts rather than one continuous run. The declaration syntax barely changes; what changes is which constraints are enforced.

That route matters for a reason the report states directly: the constraint driving the whole design is what a person can hold in mind at once, and the situation is worse when several people must reason about the same program. Every new orthogonal primitive spends part of that budget. A lifted restriction spends almost none, because the reader already knows the construct's rules and only has to unlearn a prohibition. This is also why the resulting mechanism stayed general enough to serve modelling, extension, and later object-oriented programming at large: it inherited the block's existing account of naming, scope, and locality instead of inventing a parallel one.

A programmer who has internalized this treats "we need a new construct" as a hypothesis to be attacked rather than a conclusion. The first question is which existing construct in the system is already almost the right shape, and what rule currently prevents it from being used that way — a lifetime tied to a stack frame, a cardinality fixed at one, an ordering imposed for implementation convenience. Very often the rule was never load-bearing; it was inherited from the first use case. Removing it yields a smaller total system than adding beside it, and every reader who understood the old construct gets the new capability for free.

**Source:** [SIMULA 67 Common Base Language](../works/simula-67-common-base-language.md) — the introductory sections that motivate the language from decomposition and the limits of human concentration, then derive the class and the object from the block-instance notion before the formal definition begins.
