---
type: work
title: "Slave Memories and Dynamic Storage Allocation"
figure: wilkes
description: A two-page note proposing that a small, fast core memory sit in front of a larger, slower main memory and be filled automatically as instructions or data are referenced, rather than under explicit programmer control. Wilkes sketches the addressing scheme (comparing a tag against the current block of the slave store) and the replacement problem this creates. This is the paper that put the word "cache" into computing, and the mechanism it describes is the ancestor of every hardware cache built since.
subdomains: [operating-systems-and-systems-programming]
year: 1965
url: https://www.cs.auckland.ac.nz/courses/compsci703s1c/resources/Wilkes.pdf
extraction: complete
survey_pages: 2
survey_text_layer: full
survey_fetch_mb: 0
access: public
host: third-party-rehost
tags: [work]
---

# Slave Memories and Dynamic Storage Allocation

**Venue/year:** IEEE Transactions on Electronic Computers, Vol. EC-14, No. 2, April 1965, pp. 270-271.
**Source:** https://www.cs.auckland.ac.nz/courses/compsci703s1c/resources/Wilkes.pdf — University of Auckland course-materials mirror (also mirrored on other university course pages, e.g. ETH Zurich); content verified by rendering and visually confirming the scanned pages match the published paper.
**Reading copy:** `scratchpad/ocr-text/wilkes__slave-memories-and-dynamic-storage-allocation.txt` — **replaced 2026-07-31 with an embedded publisher text layer; no OCR involved.** The earlier tesseract pass over the Auckland mirror produced unusable garbage, and re-OCR cannot fix it: that PDF embeds the page scan at only 784x1000 pixels for a full two-column journal page, so the body text is a few pixels per line and no rendering resolution recovers it. The IEEE Xplore copy mirrored by ETH Zurich at `https://safari.ethz.ch/digitaltechnik/spring2022/lib/exe/fetch.php?media=wilkes.pdf` carries a genuine text layer (`pdftotext -layout`) plus 600dpi page images, and is the correct source for this work. Prefer it over the `url` above for any future reading.

**A note on reading it:** page 270 is shared with the tail of an unrelated article, so the two-column extraction interleaves Wilkes's summary and introduction with another author's equations. The Wilkes text starts at the byline partway down the page; the stray formulas near the top belong to the preceding paper and are not his.

## Lessons
- [The unit you move data in is a consequence of where the cost sits, so re-derive it whenever a new tier changes the cost shape](../lessons/re-derive-the-transfer-unit-when-the-cost-shape-changes.md)
- [When you cannot predict which data a computation will touch, build the mechanism that lets the touching itself decide](../lessons/let-the-reference-stream-define-the-working-set.md)
- [When you index by a lossy function of a key, store the part you discarded so a hit can be told from a coincidence](../lessons/keep-the-bits-you-discarded-to-index-cheaply.md)
- [What a transparent duplicate of state really costs is the set of freedoms you decline to withdraw from its clients](../lessons/the-freedom-you-decline-to-withdraw-prices-the-duplicate.md)
- [Let claimants collide in one pool with an ownership tag rather than carving the resource up, because partitioning exports an allocation problem upward](../lessons/share-by-tagging-owners-not-by-partitioning.md)
- [Hang deferred reconciliation on a transition the system already makes, and carry the smallest per-entry state that makes deferring safe](../lessons/reconcile-at-a-transition-the-system-already-makes.md)
- [When a cheap check gates an expensive fallback, start both at once and abandon the loser — if abandoning leaves nothing behind](../lessons/issue-the-slow-path-alongside-the-check-if-you-can-abandon-it.md)
- [Give one copy exclusive authority for a bounded interval instead of keeping two copies in step](../lessons/give-one-copy-exclusive-authority-instead-of-keeping-two-in-step.md)
