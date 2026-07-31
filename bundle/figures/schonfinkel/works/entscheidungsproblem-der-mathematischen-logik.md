---
type: work
title: "Zum Entscheidungsproblem der mathematischen Logik"
figure: schonfinkel
description: Co-authored with Paul Bernays, this paper isolates special cases of Hilbert's decision problem (Entscheidungsproblem) for first-order logic that admit a decision procedure. It identifies what is now called the Bernays-Schönfinkel class - prenex formulas with an exists-forall quantifier prefix and no function symbols - and proves satisfiability decidable via a finite-model bound. That fragment underlies "effectively propositional" reasoning and remains a core decidable class exploited by modern automated theorem provers and SMT solvers.
subdomains: [foundations-of-computation, formal-methods-and-verification]
year: 1928
url: https://gdz.sub.uni-goettingen.de/download/pdf/PPN235181684_0099/LOG_0022.pdf
survey_pages: 32
survey_text_layer: ocr
survey_fetch_mb: 2
access: public
host: institutional
tags: [work]
---

# Zum Entscheidungsproblem der mathematischen Logik

**Author(s):** Paul Bernays, Moses Schönfinkel

**Venue/year:** Mathematische Annalen, vol. 99, pp. 342-372 (1928)

**Source:** Göttinger Digitalisierungszentrum (GDZ), the digitization center of the SUB Göttingen (Göttingen State and University Library) — direct PDF of the article as digitized from the original Mathematische Annalen volume. Persistent identifier: GDZPPN002272393 (resolvable via http://resolver.sub.uni-goettingen.de/purl?GDZPPN002272393, which redirects to the volume-level viewer). Also present as part of the full-volume scan on Internet Archive (https://archive.org/details/sim_mathematische-annalen_1928_99). Public domain (both authors died more than 70 years ago).
**Reading copy:** `scratchpad/ocr-text/schonfinkel__entscheidungsproblem-der-mathematischen-logik.txt` — OCR of the scanned original by tesseract at 300dpi. **This paper is in German** and was recognised with English language data, so umlauts and eszett are systematically mangled (u-umlaut appears as "ii", o-umlaut as "e" or "i", and eszett as a registered-trademark glyph -- e.g. "fiir" is fuer, "da(R)" is dass, "Pridikate" is Praedikate). The German prose is fully comprehensible through this; read past the diacritics. Running prose is reliable; **mathematical and logical notation is not** — turnstiles, implication arrows, subscripts and small-caps headings come through mangled. Ground every lesson in the prose argument and do not transcribe or rely on a formula from this text. Page markers `=== page N ===` correspond to PDF pages.

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
- [A family of checks is not a check until the family is bounded](../lessons/a-family-of-checks-is-not-a-check-until-the-family-is-bounded.md)
- [What you cannot distinguish, you do not have to keep](../lessons/what-you-cannot-distinguish-you-do-not-have-to-keep.md)
