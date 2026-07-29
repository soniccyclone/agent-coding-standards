---
type: work
title: "Über die Bausteine der mathematischen Logik"
figure: schonfinkel
description: Schönfinkel shows that quantified predicate logic can be built from just two primitive combinators (later named S and K), eliminating bound variables from logic entirely by expressing every connective and quantifier as combinator composition. It is the founding paper of combinatory logic, later formalized by Haskell Curry and mirrored independently by Church's lambda calculus. The paper is the historical root of variable-free, point-free functional composition still used in combinator-based language design.
subdomains: [foundations-of-computation, programming-languages-and-semantics]
year: 1924
url: https://gdz.sub.uni-goettingen.de/download/pdf/PPN235181684_0092/LOG_0026.pdf
extraction: complete
survey_pages: 13
survey_text_layer: none
survey_fetch_mb: 0
access: public
host: institutional
tags: [work]
---

# Über die Bausteine der mathematischen Logik

**Venue/year:** Mathematische Annalen, vol. 92, pp. 305-316 (1924)

**Source:** Göttinger Digitalisierungszentrum (GDZ), the digitization center of the SUB Göttingen (Göttingen State and University Library) — direct PDF of the article as digitized from the original Mathematische Annalen volume. Persistent identifier: GDZPPN002270110 (resolvable via http://resolver.sub.uni-goettingen.de/purl?GDZPPN002270110, which redirects to the volume-level viewer). Public domain (author died 1942).

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
- [A smaller basis is a purchase, not a free win](../lessons/a-smaller-basis-is-a-purchase-not-a-free-win.md)
- [Bound names are bookkeeping, not meaning](../lessons/bound-names-are-bookkeeping-not-meaning.md)
- [Widen what a value can be and arity stops mattering](../lessons/widen-what-a-value-can-be-and-arity-stops-mattering.md)
- [Your primitives are the moves your notation cannot make silently](../lessons/your-primitives-are-the-moves-your-notation-cannot-make-silently.md)
