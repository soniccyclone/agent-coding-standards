---
type: work
title: "An Algebraic Model for Combinatorial Problems"
figure: stearns
description: With Harry B. Hunt III, introduces the generalized satisfiability problem (GSP) model, an algebraic alternative to the usual language-recognition framing of combinatorial problems — an instance becomes a set of variables and terms combined over a commutative semiring rather than a string to accept or reject. Shows the model is expressive enough to capture satisfiability variants, 0/1-linear programming, nonserial optimization, and a wide range of graph problems in a structure-preserving way. Gives a single algebraic framework for classifying the complexity of many combinatorial problems that previously needed separate, problem-specific reductions.
subdomains: [algorithms-and-complexity]
year: 1996
url: http://web.archive.org/web/20120313180518/http://www.cs.albany.edu/~res/gsp.pdf
survey_pages: 40
survey_text_layer: full
survey_fetch_mb: 0
access: public
host: self-archived
tags: [work]
extraction: complete
---

# An Algebraic Model for Combinatorial Problems

**Author(s):** Harry B. Hunt III (co-author)
**Venue/year:** SIAM Journal on Computing 25(2), April 1996, pp. 448-476.
**Source:** http://web.archive.org/web/20120313180518/http://www.cs.albany.edu/~res/gsp.pdf — Wayback Machine capture of a PDF Stearns self-archived on his University at Albany faculty page. The live page now returns 404, but this snapshot — and two earlier snapshots from 2006, all with an identical file digest — serve the file directly with HTTP 200.
**Reading note:** `survey_text_layer: full` overstates this PDF's usability, the same way it does for [It's Time to Reconsider Time](its-time-to-reconsider-time.md). The body prose is set in embedded Type 3 bitmap fonts with a custom encoding and no ToUnicode map, so `pdftotext` returns dense mojibake (only the Times-Roman theorem and definition statements come through). It is a dvips-era artifact, not a scan — the pages render perfectly, so the full 40 pages were recovered by reading them directly as page images in five batches. No OCR required. Note the PDF is 40 pages (the author's own preprint, with the appendix of five algorithms and two figures) rather than the 29-page journal pagination.

## Lessons
- [Let the proof tell you what the interface is: the abstraction is exactly the laws the argument consumed](../lessons/let-the-proof-tell-you-what-the-interface-is.md)
- [Change the interpretation, not the algorithm, and absorb variants instead of building parallel theories](../lessons/change-the-interpretation-not-the-algorithm.md)
- [Make cost depend on the instance in front of you, and pick a representation that keeps its structure visible](../lessons/cost-should-depend-on-the-instance-not-its-class.md)
- [Expressibility is not leverage: judge an encoding by what structure survives it, and name where it fails](../lessons/expressibility-is-not-leverage.md)
- [Existence can be enough: price finding the certificate against using it before demanding one](../lessons/existence-can-be-enough-price-the-search-for-the-certificate.md)
- [Compute from the description, not from what it expands to, and return the answer in description form](../lessons/compute-from-the-description-not-the-expansion.md)
