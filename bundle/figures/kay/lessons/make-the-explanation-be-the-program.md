---
type: lesson
title: "When a domain already has a picture everyone explains it with, make that picture the program"
figure: kay
works: [steps-toward-the-reinvention-of-programming]
axes: [expressiveness, cognitive-load, verifiability]
subdomains: [programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# When a domain already has a picture everyone explains it with, make that picture the program

**Lesson:** Most established domains have evolved a notation their practitioners actually think in — a diagram, a table, a stylized layout — that appears in every specification and every explanation because it makes the structure immediately visible. The usual treatment is to paste that notation into a comment and then hand-write, underneath it, a mass of arithmetic that means the same thing in a form nobody can read. Two artifacts now exist for one fact, only one of them is checked by the machine, and the readable one is free to drift away from the executed one without anything noticing. The alternative is to teach the language to read the notation directly, so that the clearest human presentation of the structure is literally the definition of it. The offsets and accessors then cannot disagree with the picture, because they are derived from it.

This inverts how syntax is usually valued. Surface form is normally treated as sugar, a convenience layered over the real definition, which is why the effort of supporting a domain's own notation looks unjustifiable. But when the notation is the definition, the surface form is carrying correctness: an error is visible as a wrong picture rather than as a plausible-looking constant, and a reviewer who knows the domain but not the implementation language can still audit it. Getting there requires the ability to define a small notation cheaply enough that it is worth doing for a single structure rather than only for a whole language, which is the practical argument for treating language definition as an ordinary, low-ceremony operation instead of a major undertaking.

The general form of the move is to look for places where a program restates, in a worse medium, something that already exists in a better one. Header layouts drawn in specifications, state tables, grammar productions, protocol exchange diagrams, dimensional formulas: each is a case where the authoritative description is sitting in a document while the code paraphrases it by hand. Consuming the description instead of paraphrasing it removes an entire class of transcription defect and, usefully, makes the program self-documenting in the strong sense — not annotated with an explanation, but consisting of one.

**Source:** [STEPS Toward the Reinvention of Programming](../works/steps-toward-the-reinvention-of-programming.md) — the appendix on the compact network stack, where the bit-field diagrams that specification documents use to depict packet headers are made into a readable notation whose parsing defines the field accessors, so that what looks like documentation is a valid program; and the surrounding argument that treating surface syntax as a first-class part of the programmer's toolset opens alternatives to opaque and error-prone hand-written code.
