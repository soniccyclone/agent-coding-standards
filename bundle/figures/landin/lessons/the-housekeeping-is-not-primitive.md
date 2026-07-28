---
type: lesson
title: "Most of what a language seems to need is housekeeping derivable from a handful of primitives; count the basis before adding to it"
figure: landin
works: [mechanical-evaluation-of-expressions]
axes: [primitive-count, expressiveness]
subdomains: [foundations-of-computation, programming-languages-and-semantics]
tags: [lesson]
---
# Most of what a language seems to need is housekeeping derivable from a handful of primitives; count the basis before adding to it

**Lesson:** Landin turns the usual question inside out. Instead of asking how a given notation can be analyzed into applications and abstractions, he asks how much can be reached starting from a small stock of given constants using only those two ways of building. The answer he reports is uncomfortably small: about half a dozen objects — the means to test a list for emptiness, take its head and tail, denote the empty one, extend one, choose between alternatives, and take a fixed point — suffice, together with application and abstraction, to carry the load that sequencing, subscripting and copying carry in a conventional language, and that narrative prose carries in informal mathematics. Recursion needs no statement form; iteration needs no loop construct; selection needs no control keyword. They are consequences, not ingredients.

The reason this matters is that it separates two things that ordinary language design conflates. What a formalism is *about* is fixed entirely by which primitives you admit; the names chosen for them and the rules for writing expressions do not touch it, except in the sad case where the writing rules make some expressions unwritable and so silently shrink the subject matter. Everything customarily filed under syntax, and a good part of what gets filed under semantics, therefore turns out to be a question about text and not about the computational universe at all. Once you see the split, the interesting comparison between two languages is not their surface but their basis — and two languages that agree on the basis differ only in convenience, however unlike they look.

The practical discipline is to keep a running count of what is truly irreducible in whatever you are building, and to demand of every proposed addition that it not be derivable from what is already there. Most requests for a new construct are requests for a shorthand, and shorthands belong in the layer above the basis where they cost nothing structural. The converse discipline is just as important: notice when a feature genuinely enlarges the basis, because that is the moment your system starts being about something new, and every reasoning tool built on the old basis has to be re-examined. Landin is careful to flag the honest limit here, too — showing that the housekeeping is derivable is not the same as showing that programming this way is practical, and he declines to claim the latter.

**Source:** [The Mechanical Evaluation of Expressions](../works/mechanical-evaluation-of-expressions.md) — the section that inverts the analysis to ask what a small set of constants can construct, and the concluding discussion separating subject matter fixed by primitives from the conventions of written representation.
