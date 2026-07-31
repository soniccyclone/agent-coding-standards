---
type: work
title: "It's Time to Reconsider Time"
figure: stearns
description: Stearns's 1993 ACM Turing Award lecture (Hartmanis, his co-recipient, gave a separate lecture of his own), revisiting the resource-bounded machine framework of the 1965 founding paper nearly thirty years on. Looks back at how well "time" held up as the field's primary difficulty measure once complexity theory had to reckon with nondeterminism, parallel computation, and structural complexity classes that did not exist when the original hierarchy theorems were proved. A retrospective from one of the field's two founders on what the original formalism got right and where later work pushed past it.
subdomains: [algorithms-and-complexity, foundations-of-computation]
year: 1994
url: http://web.archive.org/web/20120313180620/http://www.cs.albany.edu/~res/turing.pdf
survey_pages: 10
survey_text_layer: full
survey_fetch_mb: 0
access: public
host: self-archived
tags: [work]
extraction: complete
---

# It's Time to Reconsider Time

**Venue/year:** Communications of the ACM 37(11), November 1994, pp. 95-99. 1993 ACM A.M. Turing Award Lecture.
**Source:** http://web.archive.org/web/20120313180620/http://www.cs.albany.edu/~res/turing.pdf — Wayback Machine capture of a PDF Stearns self-archived on his University at Albany faculty page. The live page now returns 404, but this snapshot — matching an earlier 2006 capture by file digest — serves the file directly with HTTP 200.
**Reading note:** `survey_text_layer: full` overstates this PDF's usability. The body prose is set in embedded Type 3 bitmap fonts with a custom encoding and no ToUnicode map, so `pdftotext` returns dense mojibake for it (only the Times-Roman definition and theorem statements extract cleanly). This is a dvips-era artifact, not a scan — the pages render perfectly, so the full text was recovered by reading the ten pages directly as page images. No OCR required.

## Lessons
- [Ask how well the model fits before asking how hard the theorem was](../lessons/ask-how-well-the-model-fits-first.md)
- [A cost measure earns trust by the invariances it turns into theorems](../lessons/invariances-a-measure-must-make-into-theorems.md)
- [What you refuse to charge for decides how finely you can see](../lessons/what-you-refuse-to-charge-for-sets-your-resolution.md)
- [Check which direction your formalism can assert in before setting a goal it cannot state](../lessons/know-which-direction-your-formalism-can-assert.md)
- [Classifying by reduction throws away the one number you wanted, so track the size of the mapping](../lessons/classification-by-reduction-discards-the-magnitude.md)
