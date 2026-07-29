---
type: lesson
title: "Cutting constructs relocates the cost into the environment rather than erasing it"
figure: ungar
works: [self-the-power-of-simplicity]
axes: [primitive-count, cognitive-load, expressiveness]
subdomains: [programming-languages-and-semantics, programming-environments-and-object-systems]
tags: [lesson]
---
# Cutting constructs relocates the cost into the environment rather than erasing it

Every distinct construct in a notation does double duty. It provides a capability, and it also *announces* something about the program that uses it — a class declaration says "this is a category of thing," a variable declaration says "this is stored, not computed," a scope keyword says "this name lives here and nowhere else." When you collapse several constructs into one, you keep all the capabilities but you lose all the announcements. The program becomes representable with less machinery and simultaneously less self-describing, because there is no longer a syntactic difference between two situations a reader needs to tell apart.

This is the tension a designer must own rather than argue away. A system with one kind of relationship instead of two is genuinely easier to explain and reason about at the mechanism level, and that gain is real. But structure does not stop existing just because the notation stopped labeling it; the intent that used to live in the choice of construct now lives only in convention, naming, and the shape of the object graph. The cost has not been paid off, it has been moved — out of the language definition and into whatever helps a person navigate a running system.

The practical consequence is that a minimalist language is a *bet on its environment*, and that bet has to be honored deliberately. If you remove the declarations that told a reader which objects exist to be shared and which exist to be used, you owe the reader something else that answers the same question: browsers, structural conventions, navigational aids, tooling that reconstructs the categories the syntax no longer records. A programmer who believes this stops treating "fewer concepts" as a complete argument. Reducing primitive count is a claim you can only cash by naming where the displaced explanatory burden went, and building the thing that carries it.

The corollary cuts both ways. When you are tempted to *add* a construct, ask whether you want the capability or the announcement. If you only want the announcement, a convention plus a tool may be the cheaper purchase, since it costs nothing in the semantics. If a single mechanism already covers the capability, adding a second one to signal intent means paying language complexity for a documentation problem.

**Source:** [Self: The Power of Simplicity](../works/self-the-power-of-simplicity.md) — the concluding section, which states plainly that shrinking the variety of constructs also shrinks the variety of cues to a system's structure, and the earlier admission that a classless system's flexibility poses a challenge the programming environment must answer.
