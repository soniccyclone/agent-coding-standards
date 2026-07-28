---
type: work
title: "The Text Editor sam"
figure: pike
description: Describes sam, Pike's earlier multi-file editor for bitmap displays, which pairs a mouse-driven cut-and-paste interface with a textual command language built from composable regular expressions (structural regular expressions). Edits are logged as atomic transactions against the file, treating the buffer like a small transactional database and giving the editor a clean general undo mechanism as a side effect rather than a bolted-on feature. Sam's split-process design (a display process talking a low-bandwidth protocol to an editing process) and its command language directly prefigure Acme and Plan 9's file-server style interfaces.
subdomains: [programming-environments-and-object-systems]
year: 1987
url: https://research.swtch.com/sam.pdf
extraction: complete
survey_pages: 30
survey_text_layer: full
survey_fetch_mb: 0
access: public
host: third-party-rehost
tags: [work]
---

# The Text Editor sam

**Venue/year:** Software: Practice and Experience 17(11), November 1987, pp. 813-845.
**Source:** https://research.swtch.com/sam.pdf — live page, hosted by Russ Cox (longtime Go team member, maintainer of a well-known personal archive of Plan 9 and Bell Labs papers) — not the publisher, not Pike's own site. A second independent copy (OCR scan of the same published paper) is mirrored at the Internet Archive: https://archive.org/details/text-editor-sam. Original publisher (Wiley) copy is paywalled; resolves the `uncertain` flag from the Phase 1/2 stub.
**Host:** third-party-rehost.

## Lessons
- [Compose the selection, apply the change once](../lessons/compose-the-selection-apply-the-change-once.md)
- [Write down the change before you make it](../lessons/write-down-the-change-before-you-make-it.md)
- [The loop you write silently chooses the data's shape](../lessons/the-loop-you-write-silently-chooses-the-datas-shape.md)
- [Extensibility is what you add when the core is too slow](../lessons/extensibility-is-what-you-add-when-the-core-is-too-slow.md)
- [Both ends modelling what the other knows beats asking](../lessons/both-ends-modelling-what-the-other-knows-beats-asking.md)
