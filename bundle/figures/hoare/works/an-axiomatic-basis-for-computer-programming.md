---
type: work
title: "An Axiomatic Basis for Computer Programming"
figure: hoare
description: Formalizes Floyd's inductive-assertion method into a deductive proof system for imperative programs, built around the triple P{Q}R meaning "if P holds before Q executes and Q terminates, R holds after." Gives axioms and inference rules for assignment, composition, and conditionals, plus a rule of consequence for strengthening/weakening. The paper's notation and style became the namesake formalism for the entire axiomatic-semantics subfield.
subdomains: [formal-methods-and-verification]
year: 1969
url: http://www.cs.cmu.edu/~crary/819-f09/Hoare69.pdf
survey_pages: 6
survey_text_layer: ocr
extraction: complete
survey_fetch_mb: 2
access: public
host: third-party-rehost
tags: [work]
---

# An Axiomatic Basis for Computer Programming

**Venue/year:** Communications of the ACM 12(10), October 1969, pp. 576-580.
**Source:** http://www.cs.cmu.edu/~crary/819-f09/Hoare69.pdf — course-reading mirror hosted by Karl Crary for a CMU graduate course (819, Fall 2009); PDF metadata confirms title "An Axiomatic Basis for Computer Programming" and author "C. A. R. Hoare".
**Reading copy:** `scratchpad/ocr-text/hoare__an-axiomatic-basis-for-computer-programming.txt` — OCR of the scanned original by tesseract at 300dpi. Running prose is reliable; **mathematical and logical notation is not** — turnstiles, implication arrows, subscripts and small-caps headings come through mangled. Ground every lesson in the prose argument and do not transcribe or rely on a formula from this text. Page markers `=== page N ===` correspond to PDF pages.

## Lessons
- [Underspecify on purpose: a specification should name the choices it refuses to make](../lessons/underspecify-on-purpose-and-make-the-choice-explicit.md)
- [Let the rule for reasoning about a construct be its definition, and let the rule's ugliness be its grade](../lessons/let-the-reasoning-rule-be-the-definition-and-the-grade.md)
- [Scope a guarantee to what you can actually discharge, and push the residue somewhere it can be detected](../lessons/scope-the-guarantee-and-name-the-residue.md)
- [A component's stated contract is simultaneously its documentation, its proof obligation, and its licence to be replaced](../lessons/a-components-contract-is-its-documentation-and-its-replacement-license.md)
