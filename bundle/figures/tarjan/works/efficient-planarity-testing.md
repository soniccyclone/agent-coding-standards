---
type: work
title: "Efficient Planarity Testing"
figure: tarjan
description: Gives a linear-time algorithm for deciding whether an arbitrary graph can be drawn in the plane without edge crossings, built as an iterative reformulation of the earlier Auslander-Parter path-addition method on top of a depth-first-search traversal. Before this result the best known planarity tests ran in superlinear time, so pairing DFS with a careful path-embedding order was what got the problem down to O(V). It stands alongside the 1972 DFS paper as a second demonstration of depth-first search unlocking a linear bound on a problem that previously resisted one.
subdomains: [algorithms-and-complexity]
year: 1974
url: https://web.archive.org/web/20221226115810/https://ecommons.cornell.edu/bitstream/handle/1813/6011/73-165.pdf
survey_pages: 57
survey_text_layer: ocr
survey_fetch_mb: 2
access: public
host: institutional
extraction: complete
tags: [work]
---

# Efficient Planarity Testing

**Author(s):** John Hopcroft, Robert E. Tarjan
**Venue/year:** Cornell University Department of Computer Science technical report TR 73-165, April 1973; journal version in Journal of the ACM 21(4), 1974, pp. 549-568.
**Source:** https://web.archive.org/web/20221226115810/https://ecommons.cornell.edu/bitstream/handle/1813/6011/73-165.pdf — Wayback Machine snapshot (Dec 2022) of the Cornell eCommons technical-report repository copy; the live eCommons URL currently returns HTTP 202 to automated fetches, so the archived snapshot is used as the stable public link. Item metadata on the eCommons record page (also confirmed via a separate Wayback snapshot) lists the title as "Efficient Planarity Testing," handle 1813/6011.
**Reading copy:** `scratchpad/ocr-text/tarjan__efficient-planarity-testing.txt` — OCR of the scanned original by tesseract at 300dpi. Running prose is reliable; **mathematical and logical notation is not** — turnstiles, implication arrows, subscripts and small-caps headings come through mangled. Ground every lesson in the prose argument and do not transcribe or rely on a formula from this text. Page markers `=== page N ===` correspond to PDF pages.

## Lessons
- [Decide a property by trying to build the thing, not by searching for the forbidden shape](../lessons/decide-by-attempting-to-construct-not-by-searching-for-the-forbidden-shape.md)
- [Make the unit of work the set of decisions that are forced to move together](../lessons/make-the-unit-of-work-the-set-of-decisions-that-move-together.md)
- [Order the work so the items nest, and the bookkeeping collapses to a stack](../lessons/order-the-work-so-it-nests-and-a-stack-is-enough.md)
- [Give a subcomputation its own view of shared mutable state with a boundary marker and a proof that the older entries cannot matter](../lessons/scope-shared-mutable-state-with-a-marker-and-an-irrelevance-proof.md)
- [Extract the constraint graph, and a yes/no procedure starts producing the witness](../lessons/extract-the-constraint-graph-so-the-decision-yields-a-witness.md)
- [Narrow the input in cheap front passes so the core algorithm may assume more, and the bound simplifies with it](../lessons/narrow-the-input-before-you-start-so-the-core-can-assume-more.md)
- [Fit the measurement to the shape you claimed, and find out which resource actually binds](../lessons/fit-the-measurement-to-the-claimed-shape-and-find-which-resource-binds.md)
- [Get the bound first, then spend a separate revision buying the simplicity back](../lessons/get-the-bound-first-then-spend-a-separate-revision-buying-simplicity.md)
