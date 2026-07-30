---
type: work
title: "Toward a Mathematical Semantics for Computer Languages"
figure: scott
description: The founding paper of denotational semantics, written jointly with Christopher Strachey. It argues that a program's meaning should be given as a mathematical function from states to states, independent of any particular machine, and works through how recursive commands and variable environments fit into that scheme. The paper's closing sections sketch the function-space problem that Scott would spend the next several years solving with domain theory.
subdomains: [programming-languages-and-semantics, foundations-of-computation]
year: 1971
url: https://www.cs.cmu.edu/~crary/819-f09/Scott71.pdf
survey_pages: 28
survey_text_layer: ocr
survey_fetch_mb: 8
access: public
host: third-party-rehost
tags: [work]
---

# Toward a Mathematical Semantics for Computer Languages

**Author(s):** Dana Scott and Christopher Strachey
**Venue/year:** Proceedings of the Symposium on Computers and Automata, Polytechnic Institute of Brooklyn, April 1971, pp. 19-46 (originally Oxford PRG Technical Monograph PRG-6, August 1971).
**Source:** https://www.cs.cmu.edu/~crary/819-f09/Scott71.pdf — scanned copy hosted on a CMU graduate course page (course-mirror rehost); verified against the CMU/CiteSeerX access flag already noted in the figure stub. Title page confirmed by direct render.
**Reading copy:** `scratchpad/ocr-text/scott__toward-a-mathematical-semantics-for-computer-languages.txt` — OCR of the scanned original by tesseract at 300dpi. Running prose is reliable; **mathematical and logical notation is not** — turnstiles, implication arrows, subscripts and small-caps headings come through mangled. Ground every lesson in the prose argument and do not transcribe or rely on a formula from this text. Page markers `=== page N ===` correspond to PDF pages.

## Lessons
- [Give each construct a meaning of its own instead of explaining the whole by translating it away](../lessons/define-meaning-clause-by-clause-not-by-translation.md)
- [Keep the notation and the thing it denotes apart, because equivalence is a question about meanings](../lessons/keep-the-notation-and-the-thing-it-denotes-apart.md)
- [Separate the fixed skeleton from the pluggable primitives, so one account covers a whole class of models](../lessons/parameterize-over-a-class-of-models-not-one.md)
