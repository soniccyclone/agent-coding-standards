---
type: lesson
title: "The size of the source is not the amount you said"
figure: chaitin
works: [an-invitation-to-algorithmic-information-theory, on-the-length-of-programs-for-computing-finite-binary-sequences, the-limits-of-mathematics]
axes: [expressiveness, primitive-count, cognitive-load]
subdomains: [programming-languages-and-semantics, foundations-of-computation]
tags: [lesson]
---
# The size of the source is not the amount you said

**Lesson:** Any notation with syntax is redundant, and the redundancy is exactly what makes it pleasant. Structure in the notation means that not every string of symbols is legal, which means each symbol carries less than its full share of information, which means counting symbols overstates how much has actually been committed to. Chaitin ran into this twice. Early on he found that a machine's own instruction encoding carried information that had nothing to do with its behaviour, since renaming internal states leaves behaviour untouched, and he redesigned the encoding to strip that out before he was willing to count anything. Decades later he stopped trying to measure readable source at all: a program became a readable expression followed by a raw channel of bits that the expression pulls from as it needs them, and the measure is the total of both.

The move is worth generalising. When you want to know how much a design commits you to, measuring the artifact in its convenient notation gives you a number contaminated by the notation's own conventions. The clean version separates the two roles. Let the expressive layer be as redundant as it likes, because that redundancy is buying readability, and put the incompressible decisions somewhere they can be counted honestly. Chaitin's split is unusually literal, but the pattern of a compact interpreter plus a dense payload recurs anywhere a system's real content lives in data rather than code.

For everyday work the lesson is a caution against a family of comfortable metrics. Lines of code, file counts, and expression sizes are notational quantities, and two designs that differ by a factor of three in source size can be identical in what they decide. Ask instead where the choices live. Very often the answer is the configuration, the schema, or the table, which is also where the size measurement should be pointed.

**Source:** [An Invitation to Algorithmic Information Theory](../works/an-invitation-to-algorithmic-information-theory.md) - the passage explaining why measuring expressions in characters is the wrong yardstick and introducing the hybrid of a readable prefix plus raw binary data read on demand. The earlier form of the concern is Part 1 of [On the Length of Programs for Computing Finite Binary Sequences](../works/on-the-length-of-programs-for-computing-finite-binary-sequences.md), where redundancy in the machine's own program table is located and removed. The hybrid measure is set out operationally in [The Limits of Mathematics](../works/the-limits-of-mathematics.md), in the chapter on giving binary data to expressions.
