---
type: work
title: "Scheme: An Interpreter for Extended Lambda Calculus"
figure: sussman
description: The founding document of Scheme, written up as an AI Memo rather than a formal paper. It specifies a small Lisp dialect built around lexical scoping and full closures, gives an interpreter for it, and uses that interpreter to work out how tail-recursive iteration and continuation-passing style actually behave under the hood. The design choice at its center — unify functions and control state so that closures and continuations fall out of the same mechanism — set the template for every later "minimal Lisp" language.
subdomains: [programming-languages-and-semantics]
year: 1975
url: https://web.archive.org/web/20260405051522/https://dspace.mit.edu/bitstream/handle/1721.1/5794/AIM-349.pdf
survey_pages: 43
survey_text_layer: ocr
survey_fetch_mb: 2
access: public
host: institutional
extraction: complete
tags: [work]
---

# Scheme: An Interpreter for Extended Lambda Calculus

**Author(s):** Gerald Jay Sussman and Guy L. Steele Jr.
**Venue/year:** MIT AI Memo 349, December 1975.
**Source:** https://web.archive.org/web/20260405051522/https://dspace.mit.edu/bitstream/handle/1721.1/5794/AIM-349.pdf — Wayback Machine snapshot (April 2026) of the bitstream PDF from MIT's DSpace institutional repository (handle 1721.1/5794). The live dspace.mit.edu host currently returns bot-challenge responses (HTTP 202, empty body) to automated fetches, so the Wayback snapshot of the original institutional file is used per the self-archived/institutional-snapshot fallback policy.
**Reading copy:** `scratchpad/ocr-text/sussman__scheme-an-interpreter-for-extended-lambda-calculus.txt` — OCR of the scanned original by tesseract at 300dpi. Running prose is reliable; **mathematical and logical notation is not** — turnstiles, implication arrows, subscripts and small-caps headings come through mangled. Ground every lesson in the prose argument and do not transcribe or rely on a formula from this text. Page markers `=== page N ===` correspond to PDF pages.

## Lessons
- [When you cannot tell whether two ideas differ, implement both in one substrate and see whether the artifacts coincide](../lessons/build-it-to-find-out-whether-two-ideas-are-the-same.md)
- [Classify a process by what accumulates as it runs, not by what the source text looks like](../lessons/classify-a-process-by-what-accumulates-not-by-how-it-looks.md)
- [Never implement a mechanism out of the host's version of that same mechanism, or you inherit every limit the host imposed on it](../lessons/never-build-a-mechanism-out-of-the-hosts-version-of-itself.md)
- [A model whose basic move is copying has no vocabulary for identity, so anything that depends on sharing is not hard in it but unsayable](../lessons/a-model-that-copies-can-never-talk-about-sharing.md)
- [Deferred work is retained state, so a demand-driven discipline cannot express a loop no matter how the loop is written](../lessons/deferred-work-is-retained-state.md)
- [When a cost is believed to grow with runtime behaviour, look for the semantic rule that pins it to a static property of the text](../lessons/find-the-static-bound-hiding-inside-a-supposedly-dynamic-cost.md)
- [Encode a new ambient mode inside a mechanism you already have, then audit the laws it just inherited](../lessons/give-a-new-mode-to-an-existing-mechanism-and-audit-what-it-inherits.md)
- [Check whether a clever encoding is secretly parasitic on the evaluation rule you were about to change](../lessons/an-encoding-can-be-parasitic-on-the-rule-you-are-replacing.md)
