---
type: lesson
title: "When you cannot enumerate the variations, take the variation as code"
figure: von-thun
works: [some-simple-programming-in-joy]
axes: [expressiveness, primitive-count]
subdomains: [programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# When you cannot enumerate the variations, take the variation as code

A library author faces a recurring bind. Write a sort keyed on the obvious field and you have covered one case out of unbounded many; write a variant per key and the list never ends, because someone will want to order by the size of a nested component you never imagined. Von Thun states the bind plainly while working through sorting, and then declines both horns. His general sort takes, as an additional argument, the fragment of program that extracts whatever the caller wants to compare on. The fragment is not a callback the sort invokes at a hook point — it is spliced into the comparison position while the sort's own control structure is assembled around it, and the resulting specialised program is what actually runs.

The same move appears everywhere in the paper once you notice it. Exponentiation builds a multiply-by-this-base program out of its own argument and hands it to a repetition combinator. A two-aggregate stepping combinator is defined by constructing the nested inner loop from the second aggregate and the caller's program, then invoking the ordinary one-aggregate version on the result. A general zipping combinator conses the caller's combining program onto a fixed stub to form one of the parameters of a recursion combinator. Deeper nesting of the same technique gives the variants that operate below the top of the stack. Von Thun calls out the technique explicitly as one of the useful things to know about the language.

What distinguishes this from ordinary higher-order programming is that the program-valued argument is a value you edit rather than an opaque thing you call. Because it can be inserted anywhere in a program you are assembling, the extension point does not have to be designed in advance as a hook with a fixed signature and a fixed call site. That is the difference between a library that anticipates its uses and a library that composes with uses nobody anticipated. A programmer who has this available stops trying to predict the axis of variation and instead makes the varying fragment a parameter; a programmer who does not have it should at least recognise that a proliferating family of near-identical entry points is evidence that the variation was misplaced — it belongs in the caller's hands, not in the library's enumeration.

**Source:** [Some Simple Programming in Joy](../works/some-simple-programming-in-joy.md) — the sorting section, where von Thun rejects both a fixed comparison key and a per-key family of sorts in favour of a sort parameterised by an extraction program, together with the paper's repeated construct-then-invoke pattern in the arithmetic and aggregate operators.
