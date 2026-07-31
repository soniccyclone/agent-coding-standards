---
type: work
title: "Theory and Applications of Trapdoor Functions"
figure: yao
description: Proposes a computational reformulation of Shannon's information theory, defining what it means for information to be "accessible" only through infeasible computation. Uses this framework to build trapdoor-function-based schemes for cryptography, pseudorandom number generation, and abstract complexity theory. One of the founding papers of computational (as opposed to information-theoretic) cryptography.
subdomains: [algorithms-and-complexity]
year: 1982
url: https://www.di.ens.fr/users/phan/secuproofs/yao82.pdf
survey_pages: 12
survey_text_layer: ocr
survey_fetch_mb: 1
access: public
host: third-party-rehost
extraction: complete
tags: [work]
---

# Theory and Applications of Trapdoor Functions

**Venue/year:** 23rd Annual IEEE Symposium on Foundations of Computer Science (FOCS 1982), Chicago, pp. 80-91.
**Source:** https://www.di.ens.fr/users/phan/secuproofs/yao82.pdf — scanned reprint hosted on a cryptography course page at École Normale Supérieure (Duong Hieu Phan's teaching materials). Verified by rendering page 1: title, "Andrew C. Yao, Computer Science Division, University of California, Berkeley," and the 1982 IEEE copyright line are all visible.
**Reading copy:** `scratchpad/ocr-text/yao__theory-and-applications-of-trapdoor-functions.txt` — OCR of the scanned original by tesseract at 300dpi. Running prose is reliable; **mathematical and logical notation is not** — turnstiles, implication arrows, subscripts and small-caps headings come through mangled. Ground every lesson in the prose argument and do not transcribe or rely on a formula from this text. Page markers `=== page N ===` correspond to PDF pages.

## Lessons
- [To rebuild a theory under a resource bound, promote one of its theorems into the new definition](../lessons/promote-a-theorem-into-a-definition-to-relativize-a-theory-to-a-resource-bound.md)
- [Test a new definition by whether the old theory's invariants survive where nothing forces them to](../lessons/test-a-new-definition-by-whether-the-old-invariants-survive-unforced.md)
- [Replace a growing checklist of tests with one quantification over every test the checker could run](../lessons/quantify-over-the-whole-class-of-tests-instead-of-collecting-tests.md)
- [When you generalize a theory, the invariant that breaks is where the new power lives](../lessons/the-symmetry-that-breaks-is-where-the-new-power-lives.md)
- [Assume only a sliver of the guarantee you need, then build the amplifier that makes it total](../lessons/amplify-a-sliver-of-a-guarantee-instead-of-assuming-a-strong-one.md)
- [Hardness is a resource: a proof that something is impossible can be spent to buy a capability elsewhere](../lessons/hardness-is-a-resource-spend-a-lower-bound-to-buy-an-upper-bound.md)
