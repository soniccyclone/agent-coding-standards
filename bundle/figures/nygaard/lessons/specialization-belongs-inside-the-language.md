---
type: lesson
title: "Make Domain Specialization An Operation In The Language, Then Define Your Own Facilities With It"
figure: nygaard
works: [simula-67-common-base-language]
axes: [expressiveness, primitive-count, cognitive-load]
subdomains: [programming-languages-and-semantics, programming-environments-and-object-systems]
tags: [lesson]
---
# Make Domain Specialization An Operation In The Language, Then Define Your Own Facilities With It

**Lesson:** The report opens with a genuine conflict it refuses to resolve by picking a side. Practitioners want vocabularies fitted to their own field, near enough to how they were trained that they can state a problem directly; the industry cannot absorb an unbounded supply of separate languages. The resolution is to treat specialization as something done inside one standardized language rather than by producing another one: a bundle of domain concepts is packaged as an ordinary declaration, a program is written under that bundle, and the bundle can itself be written under another. A newcomer works with the aggregated concepts and can ignore most of the base; an expert has the whole base available and can add another layer. The chain is open at both ends, so a shop can sit its own vocabulary between the general facilities and its everyday programs.

What gives the claim teeth is that the report applies it to itself. The set handling, the discrete-event simulation apparatus, and the whole input/output system are presented as class declarations written in the language being defined — a program is described as if enclosed by an implicit block whose prefix supplies the standard files. They are predefined, not privileged. This is a load-bearing move rather than a stylistic one: it forces the extension mechanism to be strong enough for real work, since if the layering could not express the standard facilities the specification would have had to describe them by other means and the gap would be visible. It also gives readers the semantics of those facilities as source they can trace, and it leaves room for implementations to choose a different but equivalent internal arrangement.

The habit to take away is twofold and the two halves check each other. Provide one path for making the general thing specific rather than shipping variant products, and then build the things you ship on that path. A programmer following this writes the platform's own conveniences using only what users have, so that any weakness in the extension mechanism hurts the authors first. When something in the standard set has to reach past the public mechanism to work, that is a defect report against the mechanism, not a special case to be granted.

**Source:** [SIMULA 67 Common Base Language](../works/simula-67-common-base-language.md) — the introductory argument about application languages and a general substrate, the prefixing chapters that supply the layering, and the later chapters that define the set-handling, simulation, and input/output facilities as declarations in the language itself.
