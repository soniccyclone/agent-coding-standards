---
type: work
title: "Über die mehrfache Rekursion"
figure: peter
description: Extends Péter's analysis of recursion schemes to "multiple recursion" — definitions involving several variables recursing simultaneously — examining how such schemes relate in strength to ordinary primitive recursion and to Ackermann's generalized recursion. It is part of her 1930s program of mapping the landscape of recursion types by relative strength, work that fed directly into the systematic treatment she later gave in her 1951 book Rekursive Funktionen. Note: the figure's Phase 1/2 stub dated this paper 1950, but that appears to conflate it with a different, later paper on the same theme ("Zusammenhang der mehrfachen und transfiniten Rekursionen," Journal of Symbolic Logic 15(4), 1950); the Mathematische Annalen paper verified here is 1936.
subdomains: [foundations-of-computation]
year: 1936
url: https://gdz.sub.uni-goettingen.de/download/pdf/PPN235181684_0113/LOG_0035.pdf
extraction: complete
survey_pages: 40
survey_text_layer: none
survey_fetch_mb: 1
access: public
host: institutional
tags: [work]
---

# Über die mehrfache Rekursion

**Venue/year:** Mathematische Annalen, Bd. 113 (1936), pp. 489-527.
**Source:** https://gdz.sub.uni-goettingen.de/download/pdf/PPN235181684_0113/LOG_0035.pdf — direct per-article PDF served by the Göttinger Digitalisierungszentrum (GDZ), the digitization center of the SUB Göttingen (Göttingen State and University Library), from its public digitized run of Mathematische Annalen. Confirmed via the volume's METS metadata (article ID GDZPPN002278820, logical structure LOG_0035, 39 pages, author "Péter, R."), spanning physical pages 494-532 of the volume. No paywall or login. Volume-level viewer: https://gdz.sub.uni-goettingen.de/id/PPN235181684_0113

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
- [The order you impose on the domain is the real definition of a recursion](../lessons/the-order-you-impose-on-the-domain-is-the-definition.md)
- [What one level cannot define, the level above defines easily](../lessons/what-one-level-cannot-define-the-level-above-defines-easily.md)
- [To prove one level stronger than another, make it enumerate the weaker one](../lessons/separate-two-levels-of-power-by-making-the-higher-enumerate-the-lower.md)
- [Swap a construction for a checkable record plus a search you can guarantee](../lessons/swap-a-construction-for-a-checkable-record-and-a-guarded-search.md)
