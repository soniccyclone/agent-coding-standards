---
type: work
title: "Slave Memories and Dynamic Storage Allocation"
figure: wilkes
description: A two-page note proposing that a small, fast core memory sit in front of a larger, slower main memory and be filled automatically as instructions or data are referenced, rather than under explicit programmer control. Wilkes sketches the addressing scheme (comparing a tag against the current block of the slave store) and the replacement problem this creates. This is the paper that put the word "cache" into computing, and the mechanism it describes is the ancestor of every hardware cache built since.
subdomains: [operating-systems-and-systems-programming]
year: 1965
url: https://www.cs.auckland.ac.nz/courses/compsci703s1c/resources/Wilkes.pdf
survey_pages: 2
survey_text_layer: ocr
survey_fetch_mb: 0
access: public
host: third-party-rehost
tags: [work]
---

# Slave Memories and Dynamic Storage Allocation

**Venue/year:** IEEE Transactions on Electronic Computers, Vol. EC-14, No. 2, April 1965, pp. 270-271.
**Source:** https://www.cs.auckland.ac.nz/courses/compsci703s1c/resources/Wilkes.pdf — University of Auckland course-materials mirror (also mirrored on other university course pages, e.g. ETH Zurich); content verified by rendering and visually confirming the scanned pages match the published paper.
**Reading copy:** `scratchpad/ocr-text/wilkes__slave-memories-and-dynamic-storage-allocation.txt` — OCR of the scanned original by tesseract at 300dpi. Running prose is reliable; **mathematical and logical notation is not** — turnstiles, implication arrows, subscripts and small-caps headings come through mangled. Ground every lesson in the prose argument and do not transcribe or rely on a formula from this text. Page markers `=== page N ===` correspond to PDF pages.

## Lessons
- [The unit you move data in is a consequence of where the cost sits, so re-derive it whenever a new tier changes the cost shape](../lessons/re-derive-the-transfer-unit-when-the-cost-shape-changes.md)
- [When you cannot predict which data a computation will touch, build the mechanism that lets the touching itself decide](../lessons/let-the-reference-stream-define-the-working-set.md)
- [When you index by a lossy function of a key, store the part you discarded so a hit can be told from a coincidence](../lessons/keep-the-bits-you-discarded-to-index-cheaply.md)
- [What a transparent duplicate of state really costs is the set of freedoms you decline to withdraw from its clients](../lessons/the-freedom-you-decline-to-withdraw-prices-the-duplicate.md)
- [Let claimants collide in one pool with an ownership tag rather than carving the resource up, because partitioning exports an allocation problem upward](../lessons/share-by-tagging-owners-not-by-partitioning.md)
