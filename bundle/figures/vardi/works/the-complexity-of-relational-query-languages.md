---
type: work
title: "The Complexity of Relational Query Languages"
figure: vardi
description: Shows that how hard a relational query is to answer depends heavily on whether you hold the query fixed and vary the database, or vary both together — the query-fixed case (data complexity) is far cheaper than the combined case, which Vardi pins down as complete for standard complexity classes like PSPACE for relational calculus. That data/combined complexity split became a standard lens for talking about how expressive a query language can afford to be. The Phase 1 pass attributed this to "Chandra and Vardi" — DBLP shows it is solely authored by Vardi; the STOC 1982 volume also contains a related but separate paper by Chandra and Harel, which is likely the source of the mix-up.
subdomains: [databases-and-data-management, algorithms-and-complexity]
year: 1982
url: http://www.cs.rice.edu/~vardi/papers/stoc82.pdf
survey_pages: 10
survey_text_layer: ocr
survey_fetch_mb: 0
access: public
host: self-archived
extraction: complete
tags: [work]
---

# The Complexity of Relational Query Languages

**Venue/year:** STOC 1982 (14th Annual ACM Symposium on Theory of Computing), Extended Abstract.
**Source:** http://www.cs.rice.edu/~vardi/papers/stoc82.pdf — verified live (HTTP 200, application/pdf, ~590KB), self-archived on Vardi's own Rice University papers page.
**Reading copy:** `scratchpad/ocr-text/vardi__the-complexity-of-relational-query-languages.txt` — OCR of the scanned original by tesseract at 300dpi. Running prose is reliable; **mathematical and logical notation is not** — turnstiles, implication arrows, subscripts and small-caps headings come through mangled. Ground every lesson in the prose argument and do not transcribe or rely on a formula from this text. Page markers `=== page N ===` correspond to PDF pages.
**Host:** self-archived — author's own site.

## Lessons
- [Name which input you are holding fixed before you quote a cost](../lessons/name-which-input-you-are-holding-fixed-before-you-quote-a-cost.md)
- [Shorter notation moves cost onto the evaluator; it does not remove it](../lessons/shorter-notation-moves-cost-onto-the-evaluator.md)
- [Earn each new construct with a thing the old language cannot say, and price it before adding it](../lessons/earn-each-new-construct-with-a-thing-the-old-language-cannot-say.md)
- [A language blind to arrangement cannot count, so hand it the arrangement deliberately](../lessons/a-language-blind-to-arrangement-cannot-count.md)
- [When two opposed styles measure identically, the choice between them is ergonomic](../lessons/when-two-opposed-styles-measure-identically-the-choice-is-ergonomic.md)
- [Measure the smallest yes-or-no question, then check the reduction back is faithful](../lessons/measure-the-smallest-decidable-question-then-check-the-reduction-is-faithful.md)
