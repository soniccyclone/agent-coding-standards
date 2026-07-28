---
type: work
title: "The Mechanical Evaluation of Expressions"
figure: landin
description: Landin specifies an abstract machine — the SECD machine, named for its four registers: stack, environment, control, and dump — that evaluates lambda-calculus-style expressions step by step. It is the first operational (as opposed to purely mathematical) account of how a functional expression actually gets computed, and it fixed the vocabulary of environments, closures, and control stacks that essentially every later functional-language implementation still uses. Landin frames it explicitly as a way to make expression evaluation mechanical and precise enough to run on real hardware.
subdomains: [programming-languages-and-semantics, foundations-of-computation]
year: 1964
url: https://www.cs.cmu.edu/afs/cs/user/crary/www/819-f09/Landin64.pdf
extraction: complete
survey_pages: 13
survey_text_layer: full
survey_fetch_mb: 1
access: public
host: third-party-rehost
tags: [work]
---

# The Mechanical Evaluation of Expressions

**Venue/year:** The Computer Journal 6(4), January 1964, pp. 308-320.
**Source:** https://www.cs.cmu.edu/afs/cs/user/crary/www/819-f09/Landin64.pdf — course-materials mirror on Karl Crary's "Classic Papers in Programming Languages and Logic" (CMU 15-819, Fall 2009) page, same course page that hosts "The Next 700 Programming Languages." Confirmed via decompressed PDF content containing "SECD," the machine this paper introduces.

## Lessons
- [To understand a computation mechanically, turn everything implicit about it into named parts of an explicit state](../lessons/make-the-implicit-context-of-execution-into-explicit-data.md)
- [Define a data shape by the questions it can answer, not by how it is written or stored](../lessons/structure-is-the-questions-a-thing-answers.md)
- [Any translation between notations is easy; only one that preserves meaning counts, so state that test before you start](../lessons/a-translation-is-cheap-a-meaning-preserving-one-is-not.md)
- [When evaluation would commit too early, turn the computation into a value and pass that instead](../lessons/wrap-what-must-not-happen-yet-into-a-value.md)
- [Most of what a language seems to need is housekeeping derivable from a handful of primitives; count the basis before adding to it](../lessons/the-housekeeping-is-not-primitive.md)
