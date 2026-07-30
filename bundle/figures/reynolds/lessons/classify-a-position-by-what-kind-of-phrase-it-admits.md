---
type: lesson
title: "Classify an interface position by what kind of phrase it admits, not by what kind of value flows through it"
figure: reynolds
works: [the-craft-of-programming]
axes: [verifiability, expressiveness, cognitive-load]
subdomains: [programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# Classify an interface position by what kind of phrase it admits, not by what kind of value flows through it

**Lesson:** There are two independent classifications running through any interface and they are easy to conflate. One says what kind of *value* is involved — a whole number, a truth value, a record. The other says what kind of *thing* may appear in the position — something that can be evaluated, something that can be assigned to, something that itself takes arguments. The second classification is the one that determines whether a substitution even makes sense. A position that only ever gets read will accept a constant or a computed expression; a position that gets written must have something with an identity behind it, and supplying a constant there produces nonsense. Knowing that both positions carry whole numbers tells you nothing about this. Record both, and record them separately.

The cost of conflating them is precisely measurable: errors that a checker could have caught before the program ever ran instead surface during execution, possibly long after the code has been written, tested and believed correct, and the machinery needed to catch them at run time slows down every call that was fine. That is the shape of the failure, and it is worth naming as a design mistake rather than an inconvenience — the loss is not "some errors get through" but "the whole class moves from cheap detection to expensive detection." Whenever you design a way to pass things around, ask which mismatches your notation makes impossible to express, and treat every mismatch it permits as a defect you have chosen to pay for later.

The encouraging half is what to do when you cannot change the checker. The information can be added as a rigorously observed annotation — a comment in a fixed format, applied uniformly, obeying stated rules — and used as though it were enforced. You lose mechanical guarantee and keep the discipline, which is most of the value, because the discipline is what makes the intent reviewable and makes the eventual mechanical version a formality. This is the general shape of retrofitting a missing static check onto a system you do not control: define the classification precisely, write it down everywhere it applies, and follow it as strictly as a compiler would. The annotation is not a substitute for the check so much as a specification of the check somebody can later implement.

**Source:** [The Craft of Programming](../works/the-craft-of-programming.md) — Section 3.1.2 on specifiers and phrase types, which distinguishes phrase types describing sets of phrases from data types describing sets of values, shows a procedure whose parameter is assigned to and therefore cannot accept a constant or compound expression, calls the inability to catch this before execution the most serious design mistake in the language because it postpones detection from compilation to execution and degrades efficiency, and then retrofits adequate specifiers as formally prescribed comments used exactly as if the compiler enforced them.
