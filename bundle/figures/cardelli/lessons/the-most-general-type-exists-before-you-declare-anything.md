---
type: lesson
title: "There is a most general truth about what your code accepts, and declarations can only narrow it"
figure: cardelli
works: [basic-polymorphic-typechecking]
axes: [expressiveness, cognitive-load, verifiability]
subdomains: [programming-languages-and-semantics]
tags: [lesson]
---
# There is a most general truth about what your code accepts, and declarations can only narrow it

**Lesson:** It is tempting to think of a declared interface as the thing that makes code applicable to certain inputs. The order is the reverse. A piece of code, considered as text, already constrains what it can be applied to, and under the right conditions those constraints have a unique most general solution. That solution exists whether or not anybody wrote it down, it can be computed, and a declaration can only be equal to it or stricter than it. Annotation is therefore an act of restriction and communication, not of creation. Attempting to declare something more general than the code supports is not permission, it is a claim the code fails to honour.

Two practical consequences follow. First, the widest applicability of a routine is a fact you can discover rather than an aspiration you have to design toward, which changes how you read unannotated code: the general case is recoverable, and if the inferred generality is narrower than you expected the surprise is information about a dependency you did not realize you had introduced. Second, the ability to omit annotations altogether is not a separate convenience feature bolted on for interactive use; it is a by-product of the machinery that searched for the most general solution in the first place. A design that pursues maximal reuse honestly gets terseness free, which is why a language can feel as unceremonious as an untyped one while retaining full static discipline.

The uniqueness has preconditions worth respecting. It holds for a carefully chosen space of descriptions, and richer spaces lose it, so the existence of a best answer is a property you preserve by restraint rather than something you can assume. Where the space is enlarged, discovery gives way to negotiation and annotations start carrying real content again.

A programmer who believes this reads annotations as constraints rather than definitions, expects to be told the general fact about their own code and to be corrected by it, and treats a required annotation as evidence about the limits of the description language rather than as an inherent cost of static checking.

**Source:** [Basic Polymorphic Typechecking](../works/basic-polymorphic-typechecking.md) — the pragmatic motivation and historical sections, which trace the principal-type property and its consequence that inference finds the best type independently of declarations, with declarations able only to reduce generality.
