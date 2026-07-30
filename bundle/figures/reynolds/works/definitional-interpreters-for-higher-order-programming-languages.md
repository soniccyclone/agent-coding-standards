---
type: work
title: "Definitional Interpreters for Higher-Order Programming Languages"
figure: reynolds
description: Argues that the clearest way to give a language semantics is to write an interpreter for it in a simpler host language, rather than reach directly for denotational mathematics. Along the way it names and analyzes continuation-passing style and introduces defunctionalization as a technique for eliminating higher-order functions from an interpreter. Its 1998 reprint added a retrospective in which Reynolds traces how these ideas anticipated later work in compiler construction and semantics.
subdomains: [programming-languages-and-semantics]
year: 1972
url: https://homepages.inf.ed.ac.uk/wadler/papers/papers-we-love/papers-we-love.pdf
survey_pages: 45
survey_text_layer: ocr
survey_fetch_mb: 4
access: public
host: third-party-rehost
extraction: complete
tags: [work]
---

# Definitional Interpreters for Higher-Order Programming Languages

**Venue/year:** Proceedings of the ACM Annual Conference, 1972, pp. 717-740; reprinted with a retrospective in Higher-Order and Symbolic Computation 11(4), 1998, pp. 363-397.
**Source:** https://homepages.inf.ed.ac.uk/wadler/papers/papers-we-love/papers-we-love.pdf — live PDF (HTTP 200), hosted on Philip Wadler's University of Edinburgh homepage as the text for a "Papers We Love" talk on this paper. Reynolds also self-archived DVI/PostScript copies (`defint.ps.gz`) at https://www.cs.cmu.edu/afs/cs/user/jcr/ftp/, also live, but no self-archived PDF exists there.
**Reading copy:** `scratchpad/ocr-text/reynolds__definitional-interpreters-for-higher-order-programming-languages.txt` — OCR of the scanned original by tesseract at 300dpi. Running prose is reliable; **mathematical and logical notation is not** — turnstiles, implication arrows, subscripts and small-caps headings come through mangled. Ground every lesson in the prose argument and do not transcribe or rely on a formula from this text. Page markers `=== page N ===` correspond to PDF pages.
**Host:** third-party-rehost — Wadler's own academic page, not Reynolds's site or the original publisher.
**Read for extraction:** the reading copy above is Wadler's *talk slides*, which reproduce only fragments of the paper (abstract, the classification table, the six interpreters) and not its argument. Phase 4 extraction was instead done from Reynolds's own self-archived PostScript, `https://www.cs.cmu.edu/afs/cs/user/jcr/ftp/defint.ps.gz` — dvips output of `revdefint.dvi`, i.e. the complete 37-page 1998 Kluwer reprint, converted with `ps2pdf` + `pdftotext`. That file does *not* contain the separately published "Definitional Interpreters Revisited" retrospective (HOSC 11(4):355-361), so the retrospective remains unmined.

## Lessons
- [An explanation that uses the feature it explains transmits your misunderstandings intact](../lessons/explain-a-thing-in-a-weaker-medium-than-itself.md)
- [A function is a tagged record of its free variables plus one dispatcher, and the conversion is mechanical](../lessons/a-function-and-a-tagged-record-with-a-dispatcher-are-the-same-thing.md)
- [To stop depending on a choice your host made, find the discipline that makes the choice irrelevant](../lessons/adopt-the-discipline-that-makes-your-hosts-choices-irrelevant.md)
- [When a precise definition answers questions your description never asked, believe the definition](../lessons/when-the-definition-outruns-your-intention-believe-the-definition.md)
- [Thread an effect explicitly and it will tell you what it acts on and who is exempt](../lessons/make-an-effect-explicit-and-it-tells-you-what-it-acts-on.md)
