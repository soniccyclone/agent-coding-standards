---
type: work
title: "NP Is as Easy as Detecting Unique Solutions"
figure: valiant
description: With Vazirani, Valiant shows that merely telling whether a Boolean formula has exactly one satisfying assignment versus none is already, under randomized reductions, as hard as solving SAT itself. The proof uses random pairwise-independent hash functions to isolate a single solution out of a possibly large solution set with non-negligible probability, then leans on that isolation to simulate a general SAT solver. It closed off the hope that NP-hardness is somehow an artifact of instances having wildly varying numbers of solutions.
subdomains: [algorithms-and-complexity]
year: 1986
url: https://www.cs.princeton.edu/courses/archive/fall05/cos528/handouts/NP_is_as.pdf
survey_pages: 10
survey_text_layer: ocr
survey_fetch_mb: 0
extraction: complete
access: public
host: third-party-rehost
tags: [work]
---

# NP Is as Easy as Detecting Unique Solutions

**Author(s):** with Vijay V. Vazirani
**Venue/year:** Theoretical Computer Science, vol. 47 (1986), pp. 85-93 (originally presented at STOC 1985).
**Source:** https://www.cs.princeton.edu/courses/archive/fall05/cos528/handouts/NP_is_as.pdf — scanned copy hosted as a handout on a Princeton COS 528 course archive page; third-party rehost of the original journal paper.
**Reading copy:** `scratchpad/ocr-text/valiant__np-is-as-easy-as-detecting-unique-solutions.txt` — OCR of the scanned original by tesseract at 300dpi. Running prose is reliable; **mathematical and logical notation is not** — turnstiles, implication arrows, subscripts and small-caps headings come through mangled. Ground every lesson in the prose argument and do not transcribe or rely on a formula from this text. Page markers `=== page N ===` correspond to PDF pages.

## Lessons
- [A transformation that preserves the property you are asking about cannot answer the question](../lessons/a-transformation-that-preserves-a-property-cannot-answer-questions-about-it.md)
- [Narrowing a specification to well-behaved inputs buys nothing until you show the hard inputs cannot be smuggled in](../lessons/restricting-a-spec-to-well-behaved-inputs-need-not-make-it-easier.md)
- [When failure is one-sided and checkable, an unknown parameter costs you retries rather than a redesign](../lessons/one-sided-failure-makes-blind-guessing-affordable.md)
- [To manipulate a collection you cannot see, find an operation whose aggregate effect is the same on every collection](../lessons/act-on-a-hidden-set-through-an-operation-with-a-uniform-aggregate-effect.md)
- [Argue about the quantity your operation moves structurally, not the one you happen to care about](../lessons/argue-about-the-quantity-your-operation-moves-structurally.md)
