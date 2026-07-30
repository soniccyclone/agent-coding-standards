---
type: work
title: "The Best Way to Design an Automatic Calculating Machine"
figure: wilkes
description: Discussion remarks from the 1951 Manchester conference arguing that a machine's control unit should be built the same way as its arithmetic unit — out of small, repeated, regular components — rather than as an ad hoc tangle of gates. Wilkes works through a decoding-tree-plus-diode-matrix scheme that turns each machine instruction into a stored sequence of "micro-operations," including conditional branches within that sequence. This is the first published proposal of microprogramming, the technique of implementing an instruction set as an interpreter running on a simpler underlying machine.
subdomains: [operating-systems-and-systems-programming]
year: 1951
url: https://www.cs.princeton.edu/courses/archive/fall10/cos375/BestWay.pdf
extraction: complete
survey_pages: 4
survey_text_layer: ocr
survey_fetch_mb: 0
access: public
host: third-party-rehost
tags: [work]
---

# The Best Way to Design an Automatic Calculating Machine

**Venue/year:** Report of the Manchester University Computer Inaugural Conference, July 1951, pp. 16-18; reprinted in "The Early British Computer Conferences" (Charles Babbage Institute Reprint Series, Vol. 14), pp. 182-184.
**Source:** https://www.cs.princeton.edu/courses/archive/fall10/cos375/BestWay.pdf — Princeton course-materials mirror of the Charles Babbage Institute reprint; content verified by rendering and visually confirming the scanned pages (byline "By M. V. Wilkes, M.A., Ph.D., F.R.A.S.", running head "Manchester University Computer").
**Reading copy:** `scratchpad/ocr-text/wilkes__best-way-to-design-an-automatic-calculating-machine.txt` — OCR of the scanned original by tesseract at 300dpi. Running prose is reliable; **mathematical and logical notation is not** — turnstiles, implication arrows, subscripts and small-caps headings come through mangled. Ground every lesson in the prose argument and do not transcribe or rely on a formula from this text. Page markers `=== page N ===` correspond to PDF pages.

## Lessons
- [When a design problem has unstable solutions, keep reviewing the considerations instead of studying the artifacts](../lessons/when-the-solution-is-unstable-keep-reviewing-the-considerations.md)
- [Define complexity as the interconnection that hides logical structure, not as the amount of stuff](../lessons/define-complexity-as-the-connection-that-hides-structure.md)
- [Put a number on how much extra you would pay for uniformity, so the trade stops being a matter of taste](../lessons/name-the-exchange-rate-you-would-pay-for-uniformity.md)
- [Compare two mechanisms by counting how many of their properties have to be exactly right](../lessons/count-how-many-things-have-to-be-exactly-right.md)
- [Find the corner of the design still being done ad hoc, and recast it as a program over a small set of primitive moves](../lessons/turn-the-ad-hoc-corner-of-a-design-into-a-program.md)
- [Design the principled version first so that every economy you take afterwards has a visible price](../lessons/keep-the-principled-layout-as-the-yardstick-for-every-economy.md)
- [Refuse the optimization that dissolves the analogy your method depends on](../lessons/refuse-the-saving-that-dissolves-the-analogy.md)
- [Ask what your fixed part is a special case of, then price the version where it varies](../lessons/a-fixed-table-is-a-writable-one-with-a-constraint.md)
