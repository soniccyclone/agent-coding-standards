---
type: lesson
title: "Study the extremes to find out which of your assumptions are local"
figure: strachey
works: [the-varieties-of-programming-language]
axes: [expressiveness, cognitive-load]
subdomains: [programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# Study the extremes to find out which of your assumptions are local

**Lesson:** A designer's sense of what is reasonable is calibrated by whatever they have been exposed to, and exposure is usually narrow — one machine, one language family, one house style. The trouble is that a locally-formed sense of reasonableness is indistinguishable from a universal one when viewed from the inside. Nothing in your own experience will announce which of your assumptions are consequences of the problem and which are consequences of your equipment. So you have to go looking, and the productive place to look is not at the systems near yours but at the ones far out at the edges of the design space — the purists, the extremists, the designs your colleagues would call unusable.

The value of an extreme design is not that you should copy it. Most of them are impractical, and that is fine. Their value is diagnostic: an extreme case takes one variable and pushes it until the consequences become impossible to miss, which reveals that it *was* a variable. Every feature of your own tools that survives contact with a genuinely alien design is probably load-bearing; every feature that turns out to be simply absent over there, with the system still functioning, was a choice someone made and you inherited without noticing. Working purely with moderate, familiar examples cannot produce this information, because moderate examples share your blind spots.

Abstract formulas alone do not do it either. A theory of the design space tells you what is possible in principle; a handful of concrete extreme specimens tells you what the possibilities actually feel like and where they bite. The productive method runs both: general machinery for describing the space, then specific outliers to keep the machinery honest and to correct for the exaggerations that abstraction encourages. A programmer who works this way deliberately spends time in systems built on premises they reject, and treats the discomfort as the measurement rather than as a verdict on the other design.

**Source:** [The Varieties of Programming Language](../works/the-varieties-of-programming-language.md) — the preface's defence of choosing extreme language designs as its concrete examples, warning that a sense of what is sane in programming is too easily shaped by familiarity with a single machine.
