---
type: lesson
title: "A general layer earns its generality by naming what it does not define and by keeping control around what fills the gap"
figure: dahl
works: [class-and-subclass-declarations, simula-67-common-base-language]
axes: [expressiveness, cognitive-load, verifiability]
subdomains: [programming-environments-and-object-systems, software-engineering-and-architecture]
tags: [lesson]
---
# A general layer earns its generality by naming what it does not define and by keeping control around what fills the gap

**Lesson:** Two small mechanisms in the class declaration together produce something much larger than either. The first lets a general declaration list identifiers it will use but does not define, to be supplied by a more specific declaration further down the chain; the reference resolves to whatever the innermost applicable specialization provides. The second lets the general body mark a position inside itself where the specific body's statements are to be inserted, so the general text can run setup before that point and cleanup after it. Names deferred downward, control retained upward. With both, a general layer can be a complete, executable, self-consistent piece of program that nevertheless contains holes only its specializations close.

This inverts the ordinary direction of a library call and it is the reason the arrangement is worth the machinery. In the calling direction, the specific code drives and the general code is a passive resource, which means every specialization must remember the protocol: initialize first, clean up after, do these steps in this order. In the inverted direction the general code owns the protocol and the specialization supplies only the part that genuinely varies. Protocol errors stop being possible for the specialization to make, because it never had the opportunity. That is a real verifiability gain and not merely a stylistic one: the invariants of the general layer are established and restored by the general layer's own text, so its correctness argument does not have to quantify over specializations that do not exist yet.

The mechanism was also chosen against a more powerful alternative on cost grounds, which is part of the lesson. Full call-by-name would have covered these uses and more, and it was rejected because implementing it with both security and efficiency was judged out of proportion to the gain, and because the storage it forces to stay alive would be invisible to the programmer creating it. Deferred names anchored to declaration sites give most of the capability with static structure, checkable matching between what is specified and what is supplied, and no space cost at all when nothing has been supplied. Restricting a general mechanism until its cost is both small and visible is usually a better move than shipping the general version and hoping.

A programmer who has internalized this designs the general layer first as a runnable thing with named gaps, rather than as a collection of helpers the specific code is trusted to call in the right order. The diagnostic: if the documentation of a base layer has to explain a sequence the subclass must follow, the base layer failed to keep control and the sequence should have been expressed as structure instead of as prose.

**Source:** [Class and Subclass Declarations](../works/class-and-subclass-declarations.md) — the extensions section, where the split class body places the specific statements inside the general one, and the virtual-quantities subsection, which motivates deferred identifiers explicitly as the affordable replacement for unrestricted call-by-name; Dahl's answers in the appended discussion press the cost argument further. Also [SIMULA 67 Common Base Language](../works/simula-67-common-base-language.md), whose class-declaration chapter gives both mechanisms their reference definitions, including the innermost-matching rule for deferred quantities.
