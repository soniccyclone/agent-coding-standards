---
type: work
title: "Gaussian Elimination is not Optimal"
figure: strassen
description: Shows how to multiply two 2x2 matrices using seven scalar multiplications instead of the obvious eight, then applies that trick recursively to break the long-assumed n^3 cost of multiplying n x n matrices, yielding roughly n^2.807 arithmetic operations. The same recursive construction carries over to matrix inversion, linear system solving, and determinant computation, all previously believed to require cubic work. The three-page note that founded fast matrix multiplication as a field.
subdomains: [algorithms-and-complexity]
year: 1969
url: https://gdz.sub.uni-goettingen.de/download/pdf/PPN362160546_0013/LOG_0038.pdf
survey_pages: 4
survey_text_layer: none
survey_fetch_mb: 0
access: public
host: institutional
tags: [work]
---

# Gaussian Elimination is not Optimal

**Venue/year:** Numerische Mathematik 13 (1969), 354-356.
**Source:** https://gdz.sub.uni-goettingen.de/download/pdf/PPN362160546_0013/LOG_0038.pdf — direct PDF download from the Göttinger Digitalisierungszentrum (SUB Göttingen), the institutional digitization archive that absorbed DigiZeitschriften's back-catalog of German mathematics journals. Fetched and verified: HTTP 200, application/pdf, 4 pages, author/title metadata confirmed via the volume's IIIF manifest.

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
_(empty — lesson extraction is Phase 4)_
_OCR-HOLD -- no text layer; deferred pending explicit go-ahead_
