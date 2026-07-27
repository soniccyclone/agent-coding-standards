---
type: lesson
title: "Design for the laziness you actually observe: make the safe variant cheaper to type than the unsafe one"
figure: steele
works: [common-lisp-the-language-2nd-edition]
axes: [verifiability, cognitive-load, expressiveness]
subdomains: [software-engineering-and-architecture, programming-languages-and-semantics]
tags: [lesson]
---
# Design for the laziness you actually observe: make the safe variant cheaper to type than the unsafe one

**Lesson:** The specification includes several dispatching constructs that differ from their ordinary counterparts only in what happens when no branch applies: one signals an unrecoverable error, another signals a recoverable one that lets the user supply a replacement value and retry. The rationale for including them is refreshingly unflattering to everyone involved. Users could write these themselves out of existing pieces. The reason they are in the language anyway is that programmers demonstrably do not add the catch-all branch, even when they will readily agree that omitting it will hurt them later — and that if the catch-all can be obtained by adding a single character to the construct's name, they might actually do it. The design is calibrated not to what a disciplined programmer would do but to what an observed population does under time pressure.

This inverts the usual framing of a safety feature. Normally safety is presented as something the programmer must choose to invest in, with the unsafe form as the default because it is shorter. Here the cost differential is deliberately engineered to be one keystroke, which is small enough to fall below the threshold at which people economise. The insight generalises: whether a safety measure gets used is largely a function of its marginal cost at the moment of writing, and that cost is something a designer controls. If the safe path is more verbose, it loses. If it is the same length or shorter, it wins — regardless of what anybody believes about discipline.

The rationale gives a second, independent reason for shipping these rather than leaving them to users, and it is the stronger one. The recoverable variant is genuinely hard to implement correctly, so leaving it to users guarantees a population of subtly wrong private versions; and an implementation with its own debugger integration can do a better job than any portable reconstruction could. That is the same argument the document makes elsewhere for putting a fiddly invariant inside a mechanism rather than documenting it: when correct use requires care that most people will not take, the care belongs in the shared implementation. Combining the two reasons gives a general test for whether a convenience belongs in a core: is it easy to get subtly wrong, and does its absence cause people to skip a check they would endorse in principle?

A programmer who thinks this way stops treating "the user should just remember to..." as a design. They count keystrokes on the safe path versus the unsafe one and treat any deficit as a bug: exhaustiveness checks that must be opted into, resource cleanup that requires more code than leaking, timeouts that are optional parameters rather than required ones. Where the deficit cannot be removed, they at least stop being surprised that the safe form goes unused.

**Source:** [Common Lisp the Language, 2nd Edition](../works/common-lisp-the-language-2nd-edition.md) — the rationale accompanying the exhaustive case-analysis constructs in the errors chapter, which argues both from observed programmer behaviour about omitted catch-all clauses and from the difficulty of implementing the recoverable variant correctly.
