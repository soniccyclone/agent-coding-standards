---
type: lesson
title: "Mark every hole in a definition deliberately, and say who is obliged to fill it"
figure: naur
works: [revised-report-on-the-algorithmic-language-algol-60]
axes: [verifiability, hardware-affinity]
subdomains: [programming-languages-and-semantics, formal-methods-and-verification]
tags: [lesson]
---
# Mark every hole in a definition deliberately, and say who is obliged to fill it

**Lesson:** A definition that tries to settle everything will settle some things wrongly; a definition that quietly settles nothing is useless. The way out is to treat incompleteness as a first-class construct. Say precisely which outcomes you decline to fix, then state, once and globally, what it means that you declined: that a description using those features is not yet a full description of a process, and becomes one only when the missing pieces — the arithmetic actually used, its precision, the behaviour in each case you left open — are supplied alongside it. That single clause converts scattered vagueness into a well-formed obligation held by an identifiable party.

Arithmetic on approximated reals is the archetype. You cannot pin it down without picking a machine, and picking a machine would make the definition useless everywhere else, so you say outright that no exact arithmetic is prescribed and that different implementations may compute the same expression differently. Then comes the move that saves it: managing the consequences of that freedom is declared to be part of the process being described, not a wart on the description of it. The obligation is pushed into the program, where the programmer has the numerical knowledge to discharge it, and it must be discharged in the notation itself rather than in a side agreement with an implementer. Similarly, when a body of code is written outside the language, the report simply declares that its rules lie outside its own scope rather than pretending to govern it.

Two refinements keep this from becoming an excuse. Where a total definition is cheap, give one instead of a hole: an out-of-range branch selection could have been left undefined, but defining it to do nothing costs a line and removes a trap. And where an undefined value is really undefined, say so at the exact place a reader would otherwise assume otherwise — the loop variable after normal exhaustion, a variable's value on re-entering a block, exponentiation at the degenerate cases. The discipline underneath is the one the report puts on its own title page by quotation: what can be said at all can be said clearly, and about the rest one is obliged to keep quiet rather than improvise. Silence that is marked as silence is information. Silence that reads as coverage is a defect that no implementation test will find, because every implementation will look correct against it.

**Source:** [Revised Report on the Algorithmic Language ALGOL 60](../works/revised-report-on-the-algorithmic-language-algol-60.md) — the footnote to section 1 stating the global interpretation of unspecified precision and undefined outcomes, section 3.3.6 on the arithmetic of real quantities, the undefined cases in 3.3.4.3, 4.6.5 and 4.6.6, the defined degradation of a jump through an out-of-range switch designator in 4.3.5, the exclusions in 4.7.8 and 5.4.6, and the Wittgenstein epigraph heading the description of the reference language.
