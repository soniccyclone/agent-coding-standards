---
type: work
title: "Literate Programming"
figure: knuth
description: Makes the case for writing programs primarily as documents addressed to human readers, with the machine-executable form derived from that document rather than the other way around — source order should follow the logic of exposition, not the order a compiler needs. Introduces WEB, a system combining a Pascal-like language with TeX-based typesetting, letting a program be "woven" into readable documentation and "tangled" into compilable code from a single source. The paper argues this reordering of priorities produces programs that are easier to verify and maintain, and it seeded a whole family of later literate-programming tools.
subdomains: [software-engineering-and-architecture]
year: 1984
url: http://www.literateprogramming.com/knuthweb.pdf
extraction: complete
survey_pages: 15
survey_text_layer: full
survey_fetch_mb: 0
access: public
host: third-party-rehost
tags: [work]
---

# Literate Programming

**Venue/year:** The Computer Journal 27(2), 1984, pp. 97-111
**Source:** http://www.literateprogramming.com/knuthweb.pdf — third-party rehost (literateprogramming.com, a dedicated literate-programming/CWEB resource site hosting a "PDF Articles" collection), live PDF, verified HTTP 200. The Oxford Academic/ACM original is paywalled.

## Lessons
- [The order a program should be presented in is a discoverable property of the problem, not a choice between top-down and bottom-up](../lessons/expository-order-is-the-real-structure-not-top-down-or-bottom-up.md)
- [Agreement between a program and its explanation has to be structural, because discipline does not hold it](../lessons/consistency-between-code-and-explanation-must-be-structural.md)
- [Explaining a program is a coverage check on your own understanding, and understanding is where the bugs are](../lessons/explaining-a-program-is-a-verification-pass-over-your-own-understanding.md)
- [Relative size in source text is read as a statement of purpose, so the notation ends up rewriting your design decisions](../lessons/visual-proportion-reads-as-importance-so-layout-deforms-design.md)
- [Before generalizing a primitive, check whether composing the restricted one already covers every use you actually saw](../lessons/restrict-the-primitive-and-check-whether-composition-already-covers-the-gap.md)
- [Give the axis of local variation its own artifact, and edits along the two axes stop colliding](../lessons/make-the-axis-of-local-variation-a-separate-artifact.md)
