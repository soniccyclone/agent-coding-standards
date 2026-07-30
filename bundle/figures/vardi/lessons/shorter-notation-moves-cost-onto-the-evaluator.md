---
type: lesson
title: "Shorter notation moves cost onto the evaluator; it does not remove it"
figure: vardi
works: [the-complexity-of-relational-query-languages]
axes: [expressiveness, cognitive-load, primitive-count]
subdomains: [databases-and-data-management, programming-languages-and-semantics]
tags: [lesson]
---
# Shorter notation moves cost onto the evaluator; it does not remove it

**Lesson:** Adding abbreviations to a notation — a repetition shorthand, a compact numeral form, any construct that lets one symbol stand for what previously took many — changes nothing about which computations the language can describe, and yet it can raise the cost of evaluating a text of a given length by an entire exponential. Nothing was added to the semantics; the same set of behaviours is still expressible. What changed is the exchange rate between characters written and work implied. A measurement indexed on program length therefore reacts violently to sugar, while a measurement indexed on data size does not react at all: one figure is a property of the syntax, the other of the meaning.

Read that as a conservation law rather than a curiosity. Compression on the authoring side is not free efficiency; it is a transfer of effort from the person writing to the machine unfolding, and the transfer is measurable. This is the honest way to argue about syntactic sugar, macros, defaults, and derived operators. They are worth it when the effort moved is effort a human was spending badly and a machine spends well, and the argument against them is never "it is only sugar" — sugar with a bad exchange rate is exactly how a notation acquires expressions whose cost is invisible at the point of writing.

The practical discipline is to ask, of any convenience feature, what it does to the ratio between a program's visible size and its implied work. Features that keep the ratio bounded are genuinely free; features that let a linear amount of text conjure an exponential amount of unfolding have installed a trap where a reader's intuition about size no longer predicts cost. And when comparing two notations for the same semantics, the comparison is only meaningful if the translation between them preserves size within a constant factor — an equivalence proof that permits blowup settles the question of expressive power while saying nothing about the cost question people usually care about.

**Source:** [The Complexity of Relational Query Languages](../works/the-complexity-of-relational-query-languages.md) — the concluding remarks on "squeezing" expressions with shorthands like exponentiation and binary notation, which raise expression complexity while leaving data complexity fixed; and the algebra-to-calculus equivalence, whose usefulness depends on the translation being size-linear in both directions.
