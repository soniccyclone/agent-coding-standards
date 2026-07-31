---
type: work
title: "The Asymptotic Spectrum of Tensors"
figure: strassen
description: Introduces the "asymptotic spectrum" of tensors, a duality-theoretic framework (in the spirit of a Positivstellensatz for tensor degeneration) that characterizes the asymptotic rank of a tensor as a maximum over a space of spectral points rather than something computed directly. Built specifically to attack the exponent of matrix multiplication by giving a structural handle on which tensors can and cannot be degenerated into matrix multiplication tensors. The theoretical backbone later reused and extended by asymptotic-spectrum approaches to bounding the matrix multiplication exponent.
subdomains: [algorithms-and-complexity]
year: 1988
url: https://gdz.sub.uni-goettingen.de/download/pdf/PPN243919689_0384/LOG_0008.pdf
survey_pages: 52
survey_text_layer: ocr
survey_fetch_mb: 3
access: public
host: institutional
extraction: complete
tags: [work]
---

# The Asymptotic Spectrum of Tensors

**Venue/year:** Journal für die reine und angewandte Mathematik (Crelle's Journal), vol. 384 (1988), 102-152.
**Source:** https://gdz.sub.uni-goettingen.de/download/pdf/PPN243919689_0384/LOG_0008.pdf — direct PDF download from the Göttinger Digitalisierungszentrum (SUB Göttingen). Fetched and verified: HTTP 200, application/pdf, 52 pages, author/title metadata confirmed via the volume's IIIF manifest.
**Reading copy:** `scratchpad/ocr-text/strassen__the-asymptotic-spectrum-of-tensors.txt` — OCR of the scanned original by tesseract at 300dpi. Running prose is reliable; **mathematical and logical notation is not** — turnstiles, implication arrows, subscripts and small-caps headings come through mangled. Ground every lesson in the prose argument and do not transcribe or rely on a formula from this text. Page markers `=== page N ===` correspond to PDF pages.

Note: the Phase 1/2 stub listed this as "The Asymptotic Spectrum of Tensors and the Exponent of Matrix Multiplication (1988, FOCS)" — that conflates two related items. The actual FOCS extended abstract ("...and the Exponent of Matrix Multiplication") ran in FOCS 1986 (IEEE SFCS '86, pp. 49-54, DOI 10.1109/SFCS.1986.52) and sits behind the IEEE Xplore paywall with no public copy found. The full journal treatment, titled simply "The Asymptotic Spectrum of Tensors," appeared in Crelle's Journal in 1988 and is the version linked here.

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
- [One number cannot represent an order; a family of numbers can represent it exactly](../lessons/one-number-cannot-represent-an-order-a-family-of-numbers-can.md)
- [Where an inequality turns into an equality tells you what kind of function you are holding](../lessons/where-an-inequality-becomes-an-equality-tells-you-what-the-function-is.md)
- [Pass to the asymptotic version of a relation: distinctions you could not settle dissolve, and the algebra you needed appears](../lessons/pass-to-the-asymptotic-version-and-the-unresolvable-distinctions-dissolve.md)
- [Isolate the axioms your argument actually used, then find out whose theory you have landed in](../lessons/isolate-the-axioms-your-argument-used-and-find-whose-theory-you-are-in.md)
- [Treat a pile of separate bounds as constraints on one unknown object, and track the object instead](../lessons/treat-a-pile-of-bounds-as-constraints-on-one-unknown-object.md)
- [Aim at the weakest property that still yields your conclusions, and find out first whether a general proof could exist](../lessons/aim-at-the-weakest-property-that-still-yields-your-conclusions.md)
