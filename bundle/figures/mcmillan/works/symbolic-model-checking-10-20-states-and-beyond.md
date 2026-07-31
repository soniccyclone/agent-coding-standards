---
type: work
title: "Symbolic Model Checking: 10^20 States and Beyond"
figure: mcmillan
description: The paper that introduced symbolic model checking to the field, written with Burch, Clarke, Dill, and Hwang while McMillan was a CMU PhD student. It represents state spaces as Boolean functions over Bryant's Binary Decision Diagrams rather than as explicit lists, and derives efficient decision procedures for CTL model checking, temporal-logic satisfiability, and automata containment from a single mu-calculus model-checking algorithm. Its worked example, a pipeline circuit with roughly 10^20 reachable states, gave the paper its title and demonstrated verification at a scale explicit-state methods of the time could not touch. Not in the Phase 1/2 top-10 list, but added here as the direct precursor and co-founding paper of the symbolic model checking approach that McMillan's thesis and later works built on.
subdomains: [formal-methods-and-verification]
year: 1990
url: https://mcmil.net/pubs/LICS90.pdf
survey_pages: 33
survey_text_layer: ocr
survey_fetch_mb: 0
access: public
host: self-archived
tags: [work]
---

# Symbolic Model Checking: 10^20 States and Beyond

**Author(s):** J. R. Burch, E. M. Clarke, K. L. McMillan, D. L. Dill, L. J. Hwang
**Venue/year:** Proceedings of the Fifth Annual IEEE Symposium on Logic in Computer Science (LICS '90), Philadelphia, June 1990. An extended version appeared in Information and Computation, vol. 98, 1992.
**Source:** https://mcmil.net/pubs/LICS90.pdf — self-archived PDF on McMillan's own site, live and directly downloadable (HTTP 200, title page confirmed: "Symbolic Model Checking: 10^20 States and Beyond," authors J. R. Burch, E. M. Clarke, K. L. McMillan, D. L. Dill, L. J. Hwang).
**Reading copy:** `scratchpad/ocr-text/mcmillan__symbolic-model-checking-10-20-states-and-beyond.txt` — OCR of this paper by tesseract at 300dpi (10,922 words, 33% common-word ratio). Read that file, not the PDF. The PDF *does* have an embedded text layer and `pdftotext` returns ~103k characters from it, but every one of them is garbage: the fonts use a custom encoding with no Unicode map, so the output looks like `!#"%$&')(*'+-,`. A character-count check will therefore call this readable when it is not — see flags H.5. As with any OCR the prose is reliable and the notation is not, so ground lessons in the argument rather than in any formula.

**Frontmatter correction (2026-07-31, Phase 4 bucket 104).** This file carried
`survey_text_layer: full`; that was wrong and cost an extraction attempt. The PDF
downloads cleanly (HTTP 200, 368 KB, 33 pages) but its text layer is unusable in
exactly the way McMillan's thesis PDF is: `pdfinfo` reports the producer as
Aladdin Ghostscript 6.01 converting a DVI file, and `pdffonts` shows the body set
entirely in ~35 embedded Type-3 bitmap fonts with custom encodings and no
ToUnicode map. `pdftotext` in both `-layout` and `-raw` modes therefore returns a
per-font substitution cipher, not text. The flag has been changed to `none` so
future passes route this through the deterministic OCR batch instead of retrying
the fetch.

Alternate readable copies were searched and none is anonymously obtainable:
`cs.cmu.edu/~emc` paths 404; `theory.stanford.edu/~dill` 403; ScienceDirect
(the extended *Information and Computation* 98(2):142-170, 1992 version, which is
what these 33 pages appear to be) 403 bot-gate on both curl and WebFetch;
Unpaywall lists zero OA locations; Semantic Scholar reports only a BRONZE
publisher link back to the gated DOI; the Elsevier text-mining endpoint Crossref
advertises needs an API key (401). archive.org has a DTIC text derivative for the
TCAD94 paper (`DTIC_ADA274375`) and for the thesis (`DTIC_ADA250924`) but nothing
for this one.

## Lessons
_(empty — lesson extraction is Phase 4)_
without rasterising. Blocked on the OCR batch, not on reading effort. Note when
it lands: this paper is the direct precursor of
[the thesis](symbolic-model-checking-an-approach-to-the-state-explosion-problem.md),
which is already `extraction: complete` with seven lessons, so the marginal yield
here is likely small and any lesson must be checked against that set first.
