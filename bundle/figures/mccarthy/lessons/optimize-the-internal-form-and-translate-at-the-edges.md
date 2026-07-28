---
type: lesson
title: "Shape the internal representation for the transformations you will perform, and push human-facing notation out to the boundary"
figure: mccarthy
works: [history-of-lisp]
axes: [expressiveness, cognitive-load, primitive-count]
subdomains: [programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# Shape the internal representation for the transformations you will perform, and push human-facing notation out to the boundary

**Lesson:** There is a persistent temptation to make a system's working representation resemble the way people write the subject matter down. Infix arithmetic, conventional mathematical layout, the printed form of a formula: all of these carry the comfort of familiarity, and a system that stores them directly seems to save a translation step. McCarthy's account argues the saving is illusory and the cost is structural. Customary notations treat different operators in syntactically different ways, so a program that computes over them must dispatch on notational irregularity before it can get at meaning. A representation that instead puts the operator where the code needs to look first, uniformly, makes every substantive operation — deduction, algebraic simplification, differentiation — a straightforward recursion. If humans need the familiar form, you write a translator at the edge, once.

He credits this choice, rather than any performance or theory advantage, with the language's survival against the symbolic-computation systems of the same era, which computed over approximations of printed layout. The comparison he reaches for is that of binary against decimal machines, and he judges the gap larger. The reason it widens with program size is that notational irregularity does not compose: every new operation over the representation re-pays the parsing cost, so a small program absorbs it and a large one drowns in it. Uniformity, by contrast, is a fixed cost paid once at the boundary.

The conclusion of the retrospective adds a claim McCarthy presents as almost embarrassing. The feature nearly everyone including him regarded as a defect — that programs are stored in the same undecorated nested-list form as data, with no pleasant syntax of their own — is plausibly the reason the language outlived its intended replacements. A uniform, syntax-free internal form is a target other systems can compile into. Proposed successors that adopted a conventional algebraic surface syntax gained readability and lost the property of being something higher-level systems could emit, and with it lost their reason to exist. Being a good compilation target is a durability property, and it is bought precisely by refusing to make the internal form pretty.

A programmer who takes this seriously separates the representation their code manipulates from the representation their users read, and resists the reflex to unify them. They accept boundary translators as a normal cost. They evaluate an internal format by asking how many distinct shapes a traversal has to handle, not by whether it looks like the domain. And when designing something intended to be built upon, they treat the absence of privileged syntax as a feature, because whatever is easy to generate mechanically is what other tools will be able to target.

**Source:** [History of Lisp](../works/history-of-lisp.md) — the prehistory section's argument for giving up familiar infix notation internally and writing translation programs when external notation is wanted, and the conclusions, which credit the language's longevity partly to its programs being ordinary data with no syntax of their own, contrasting it with successors that adopted conventional syntax and left nothing to compile into.
