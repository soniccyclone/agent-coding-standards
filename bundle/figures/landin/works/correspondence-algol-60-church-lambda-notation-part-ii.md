---
type: work
title: "A Correspondence Between ALGOL 60 and Church's Lambda-Notation: Part II"
figure: landin
description: The second half of the ALGOL-60-to-lambda-calculus translation, extending Part I's applicative core to cover ALGOL's imperative features — assignment, jumps, and blocks with side effects. Landin has to stretch the purely applicative framework to accommodate state and control flow, and the seams in that effort foreshadow later work (including his own "A Generalization of Jumps and Labels") on giving imperative control constructs a functional account. Together the two parts are the founding proof-of-concept that a mainstream imperative language reduces to a lambda-calculus core.
subdomains: [programming-languages-and-semantics, foundations-of-computation]
year: 1965
url: https://web.archive.org/web/20250316005026/https://dl.acm.org/doi/pdf/10.1145/363791.363804
survey_pages: 8
survey_text_layer: full
survey_fetch_mb: 1
access: public
host: institutional
tags: [work]
---

# A Correspondence Between ALGOL 60 and Church's Lambda-Notation: Part II

**Venue/year:** Communications of the ACM 8(3), March 1965, pp. 158-167.
**Source:** https://web.archive.org/web/20250316005026/https://dl.acm.org/doi/pdf/10.1145/363791.363804 — Wayback Machine snapshot of the ACM Digital Library's own PDF for this DOI. Verified: the archived file is a genuine PDF (not an error page) whose embedded metadata reads Author "P. J. Landin", Title "A correspondence between ALGOL 60 and Church's Lambda-notations", Subject "Commun. ACM 1965.8:158-167". The live dl.acm.org page returns HTTP 403 to automated fetches (bot-blocking), but CACM's own site states it "is now a fully Open Access publication," and the Wayback capture shows the DL served the full PDF with no paywall as of March 2025 — used here per the Wayback-fallback rule for a stale/blocked live link to a public work.

## Lessons
- [Specify the direction in which the mapping is a function: define the object, generate its representations, and let the spread of representations define what carries no information](../lessons/generate-the-representations-from-the-object.md)
- [Translating a system into a general framework is a diagnostic instrument: the context you must thread names its irregularities, the freedom left over names its missing generalizations](../lessons/translation-is-a-diagnostic-instrument.md)
- [Write the specification in the formalism it specifies, and optimize it for its readers rather than for its output](../lessons/write-the-specification-in-the-thing-it-specifies.md)
