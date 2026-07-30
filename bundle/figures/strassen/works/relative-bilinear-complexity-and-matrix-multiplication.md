---
type: work
title: "Relative Bilinear Complexity and Matrix Multiplication"
figure: strassen
description: Develops a theory of bilinear complexity measured relative to a chosen reference bilinear map rather than in absolute terms, giving a framework for comparing how "hard" one bilinear problem is against another. Uses this relative viewpoint to derive new upper bounds on the exponent of matrix multiplication by relating matrix multiplication to other structured tensors. A technical, foundational step toward the degeneration and border-rank arguments that dominate later work on the matrix multiplication exponent.
subdomains: [algorithms-and-complexity]
year: 1987
url: https://gdz.sub.uni-goettingen.de/download/pdf/PPN243919689_0375_0376/LOG_0024.pdf
survey_pages: 39
survey_text_layer: ocr
survey_fetch_mb: 4
access: public
host: institutional
tags: [work]
---

# Relative Bilinear Complexity and Matrix Multiplication

**Venue/year:** Journal für die reine und angewandte Mathematik (Crelle's Journal), vol. 375/376 (1987), 406-443.
**Source:** https://gdz.sub.uni-goettingen.de/download/pdf/PPN243919689_0375_0376/LOG_0024.pdf — direct PDF download from the Göttinger Digitalisierungszentrum (SUB Göttingen), which digitizes Crelle's Journal's historical volumes. Fetched and verified: HTTP 200, application/pdf, 39 pages, author/title metadata confirmed via the volume's IIIF manifest. (The publisher-of-record copy at De Gruyter is paywalled; this GDZ scan is the public copy.)
**Reading copy:** `scratchpad/ocr-text/strassen__relative-bilinear-complexity-and-matrix-multiplication.txt` — OCR of the scanned original by tesseract at 300dpi. Running prose is reliable; **mathematical and logical notation is not** — turnstiles, implication arrows, subscripts and small-caps headings come through mangled. Ground every lesson in the prose argument and do not transcribe or rely on a formula from this text. Page markers `=== page N ===` correspond to PDF pages.

**Text-layer correction (2026-07-29): GDZ cover-only.** This is a
Göttingen Digitalisierungszentrum scan whose *only* embedded text is the
library's own German cover sheet. Article pages yield exactly zero characters
under `pdftotext -layout` and `-raw`, and `pdffonts` shows the sole embedded
font belongs to the cover. It was previously recorded `partial`, which was
actively misleading — that reads as "some of the article extracts" when in fact
none of it does; my survey had measured the cover boilerplate. GDZ exposes no
ALTO/OCR derivative for these items either (the IIIF manifest 404s), so the
host-provided-text channel is genuinely unavailable rather than unattempted.
This work needs the deterministic OCR batch.

## Lessons
- [When a quantity only matters up to a bounded factor, replace its operational definition with an algebraic one](../lessons/swap-the-operational-definition-for-an-invariant-that-is-robust-to-constants.md)
- [Make the comparison relation the primitive object, and let the numeric measures fall out as extremes of it](../lessons/make-the-comparison-relation-primitive-and-let-the-numbers-fall-out.md)
- [Turn the question around: besides what an object costs to build, ask what can be extracted from it](../lessons/turn-the-question-around-ask-what-can-be-extracted.md)
- [Find the equivalent condition that survives outside the friendly case, then make it the definition](../lessons/find-the-equivalent-condition-that-survives-outside-the-friendly-case.md)
- [Let a solution be approximate when the error is repaid by scale](../lessons/let-a-solution-be-approximate-when-the-error-is-repaid-by-scale.md)
- [Keep several equivalent encodings of the same object, and switch to whichever exposes the structure you need](../lessons/keep-several-equivalent-encodings-and-switch-to-whichever-exposes-the-structure.md)
