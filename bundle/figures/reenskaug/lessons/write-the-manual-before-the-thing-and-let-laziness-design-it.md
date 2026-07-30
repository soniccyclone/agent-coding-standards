---
type: lesson
title: "Write the consumer's instructions before you build the thing, and let your laziness simplify the interface"
figure: reenskaug
works: [working-with-objects-the-ooram-software-engineering-method]
axes: [cognitive-load, expressiveness]
subdomains: [software-engineering-and-architecture]
tags: [lesson]
---
# Write the consumer's instructions before you build the thing, and let your laziness simplify the interface

**Lesson:** Documentation normally comes last, which guarantees it describes whatever got built. Invert the order — write the instructions a consumer will follow *before* designing the thing — and something useful happens to the design rather than to the document. Every awkwardness in the interface now has to be written down and defended in prose, by you, before it exists and while it is still free to change. Anything genuinely hard to explain becomes visible as effort you are about to spend on yourself.

The mechanism is unusually honest about human nature: the reason this works is that nobody wants to write a long, intricate explanation, so an author drafting instructions first will unconsciously push the design toward something that is short to describe. Ordinary laziness, which is a design hazard in most orderings, becomes the enforcement mechanism in this one. You are not relying on discipline; you are arranging things so the path of least effort points at simplicity.

There is a sharp diagnostic that goes with it, and it doubles as a way to audit anything already built: take the manual for a piece of software you use and mark every sentence that could not possibly have been written before the program existed. Those sentences are the accidents — behaviour that emerged from implementation decisions rather than from anyone's intent, now permanent because it shipped. A high proportion of them means the interface was discovered rather than designed. The same test applied to your own draft, before building, tells you which parts of your plan you do not yet actually understand.

**Source:** [Working With Objects: The OOram Software Engineering Method](../works/working-with-objects-the-ooram-software-engineering-method.md) — chapter 5's procedure for creating a framework, which places documenting it as a pattern *before* design and implementation, justifies this by noting a successful framework must be easy to understand and safe to use and that in-born laziness will therefore keep the consumer interface simple, and offers the exercise of highlighting manual sentences that could not have been written before the program.
