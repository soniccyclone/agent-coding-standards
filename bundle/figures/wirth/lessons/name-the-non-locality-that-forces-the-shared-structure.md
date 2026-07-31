---
type: lesson
title: "Name the exact non-locality that forces a shared structure"
figure: wirth
works: [project-oberon]
axes: [cognitive-load, verifiability, primitive-count]
subdomains: [programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# Name the exact non-locality that forces a shared structure

**Lesson:** A design in which every part can be understood from what it contains is enormously easier to work with than one where understanding any part requires knowing something recorded elsewhere. So the arrival of a shared, long-lived structure — consulted from everywhere, mutated over time, holding facts nobody local can see — deserves a specific justification rather than the usual drift into one. The justification takes a particular form: there is a piece of information that is established in one place and needed in another, the two places are not related by containment or by argument-passing, and no amount of rearrangement makes them so. That is a non-locality, and it is the only thing that earns a shared structure.

Insisting on naming it pays off in three ways. It tells you the structure's minimum contents — exactly the facts that cross the gap, and nothing that happened to be convenient to store alongside them. It tells you the structure's lifetime, which is the interval between the establishing event and the last consultation, and lets you say what should be true of it at the boundaries. And it lets you check the claim: if you cannot describe the crossing concretely, the structure is not answering a non-locality, it is a place where state accumulated because there was somewhere to put it. Most objectionable global state fails this test, and the failure is easy to see once the question is asked in this form.

The corollary is that everything not forced across the gap should stay local, and the design should read that way. Where the greater part of a system genuinely can be handled with only what is in front of it, that regularity is worth protecting deliberately, because it is what makes the parts independently comprehensible and independently testable. The exception then stands out as an exception, is documented as one, and can be examined on its own terms — including the question of whether a change to the surrounding conventions could remove it. A shared structure introduced with its motivating non-locality recorded next to it remains reviewable for as long as the system lives; one introduced silently becomes a fixture whose contents nobody dares reduce, because nobody can any longer say what any given field is for.

**Source:** [Project Oberon](../works/project-oberon.md) — section 12.1's treatment of context dependence, which observes that when a construct's translation depends only on its own semantic rule and on attributes of its immediate components the construct is context-free, that the language adheres to this rule with the significant exception of declarations, since a declaration attaches permanent properties to an identifier which are invisible when parsing a statement containing it because the declaration is not part of the statement, so the meaning of identifiers is inherently context-dependent; and the statement that this context dependence due to declarations is the immediate reason for the global structure representing declared identifiers and their attributes, which grows while declarations are processed and is searched while expressions and statements are processed.
