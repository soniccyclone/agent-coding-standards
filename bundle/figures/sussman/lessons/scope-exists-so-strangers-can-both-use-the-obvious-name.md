---
type: lesson
title: "Scope exists so that strangers can both use the obvious name"
figure: sussman
works: [structure-and-interpretation-of-computer-programs]
axes: [cognitive-load, primitive-count]
subdomains: [software-engineering-and-architecture, programming-languages-and-semantics]
tags: [lesson]
---
# Scope exists so that strangers can both use the obvious name

**Lesson:** A working square-root routine decomposes into a handful of helpers with names like *improve* and *good-enough?*. Left at the top level, those names are correct, well chosen, and a genuine problem — not because they are wrong here, but because they are the names every other successive-approximation routine would also want. Any second author building a numerical library hits the collision immediately, and the resolution is either ugly prefixing or a coordination conversation that scales with the number of authors.

The point worth extracting is that this is a different argument for scope than the one usually given. The familiar justification is correctness: limit what can be touched so it cannot be corrupted. The argument here is about *naming capacity in a shared namespace with independent authors*. Without nesting, the obvious name for a common idea is a scarce global resource, and it goes to whoever writes first. That pressure shows up as names nobody would choose in isolation, and as the quiet reluctance to factor out a helper at all because naming it means claiming territory.

So the design goal is that several successive-approximation routines can coexist, each holding a private helper called the obvious thing. Once that is possible, decomposition stops carrying a social cost and the natural decomposition of a problem can be written down as it is, rather than as the global namespace permits.

The generalization is that any namespace shared by parties who do not talk to each other will exhibit this, and the symptom is diagnostic: when you see systematically awkward names — repeated prefixes, module names embedded in identifiers, numeric suffixes — you are looking at the absence of a scoping mechanism rather than at bad taste. The remedy is a boundary inside which the obvious name is available again, and the measure of whether your language, module system or schema has enough of them is whether two independent teams can both use the word their domain actually uses.

**Source:** [Structure and Interpretation of Computer Programs](../works/structure-and-interpretation-of-computer-programs.md) — chapter 1 section 1.1.8 on internal definitions and block structure, which observes that only `sqrt` matters to a user while its helpers merely clutter their minds, that those helpers cannot be defined by any other program because `sqrt` needs them, that the problem is especially severe when large systems are built by many separate programmers — with the example of a numerical library in which many procedures would want auxiliaries named `good-enough?` and `improve` — and resolves it by allowing definitions internal to a procedure so each successive approximation keeps its own private versions.
