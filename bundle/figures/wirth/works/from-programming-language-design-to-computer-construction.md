---
type: work
title: "From Programming Language Design to Computer Construction"
figure: wirth
description: Wirth's 1984 Turing Award lecture, tracing a single throughline from ALGOL W and Pascal through Modula-2 to the Lilith personal workstation he built to run it — the argument being that language design, compiler construction, and hardware design are one continuous engineering problem rather than three separate specialties handed off between different people. He draws out the recurring principles behind his own projects: economy of concepts, and building things small enough that one person can understand the whole. Not in the original candidate list but added here as a Phase 3 seminal-works addition — it is the Turing Award lecture underpinning the "why a candidate" case and is self-archived in full.
subdomains: [programming-languages-and-semantics, software-engineering-and-architecture]
year: 1985
url: https://people.inf.ethz.ch/wirth/Articles/TuringAward.pdf
survey_pages: 6
survey_text_layer: ocr
survey_fetch_mb: 2
access: public
host: self-archived
extraction: complete
tags: [work]
---

# From Programming Language Design to Computer Construction

**Venue/year:** ACM Turing Award Lecture; Communications of the ACM 28(2), February 1985, pp. 159-164.
**Source:** https://people.inf.ethz.ch/wirth/Articles/TuringAward.pdf — live PDF, self-archived on Niklaus Wirth's ETH Zurich personal page.
**Reading copy:** `scratchpad/ocr-text/wirth__from-programming-language-design-to-computer-construction.txt` — OCR of the scanned original by tesseract at 300dpi. Running prose is reliable; **mathematical and logical notation is not** — turnstiles, implication arrows, subscripts and small-caps headings come through mangled. Ground every lesson in the prose argument and do not transcribe or rely on a formula from this text. Page markers `=== page N ===` correspond to PDF pages.

## Lessons
- [Bootstrap every tool into its own next use, so your mistakes come back to you first](../lessons/bootstrap-every-tool-into-its-own-next-use.md)
- [Sort every design question into essential or ephemeral, and never let an ephemeral one perturb the core](../lessons/decide-what-is-essential-before-what-is-convenient.md)
- [Keep tools commensurate with the product, and read the tool you need as a measurement of your design](../lessons/keep-your-tools-commensurate-with-the-product.md)
- [Mismatch across a layer boundary is a permanent tax, and the lower layer is the one you cannot revise](../lessons/mismatch-across-a-layer-boundary-is-a-permanent-tax.md)
- [Bound an ambitious project with a few axioms, and expect them to contradict the fashion](../lessons/bound-a-project-with-axioms-chosen-against-the-fashion.md)
- [Unify the substrate of one system, not the demands of every user](../lessons/unify-the-substrate-of-one-system-not-the-needs-of-every-user.md)
