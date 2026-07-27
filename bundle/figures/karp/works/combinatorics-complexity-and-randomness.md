---
type: work
title: "Combinatorics, Complexity, and Randomness"
figure: karp
description: Karp's 1985 Turing Award lecture is a first-person retrospective on the emergence of computational complexity theory, tracing his own path from operations research and combinatorial optimization through Cook's theorem, the NP-completeness reductions, and into randomized and probabilistic algorithms. Rather than presenting new results, it's a working researcher's account of how the field's central questions (what makes a problem hard, what randomness buys an algorithm) took shape over roughly 25 years. It's a useful primary source precisely because it's testimony about the field's formative period from someone who did much of the shaping.
subdomains: [algorithms-and-complexity, foundations-of-computation]
year: 1985
url: https://www.cs.umd.edu/~gasarch/COURSES/452/S21/notes/KarpTuringAward.pdf
survey_pages: 12
survey_text_layer: full
survey_fetch_mb: 1
access: public
host: third-party-rehost
tags: [work]
---

# Combinatorics, Complexity, and Randomness

**Venue/year:** 1985 ACM Turing Award Lecture; published in Communications of the ACM 29(2), February 1986, pp. 98-109.
**Source:** https://www.cs.umd.edu/~gasarch/COURSES/452/S21/notes/KarpTuringAward.pdf — full-text copy hosted as course notes on William Gasarch's (University of Maryland CS faculty) course site; third-party rehost. HTTP 200, application/pdf. Verified by decompressing the PDF's text streams directly: extracted text opens "TURING AWARD LECTURE COMBINATORICS, COMPLEXITY, AND RANDOMNESS ... RICHARD M. KARP ... dedicated to the memory of my father, Abraham Louis Karp", confirming this is the actual lecture text. The official ACM Digital Library / cacm.acm.org versions are paywalled (403 on direct access).

## Lessons
- [Every performance claim names an adversary; know which one yours assumed](../lessons/know-which-adversary-your-performance-claim-is-made-against.md)
- [Make your own behavior unpredictable instead of assuming the inputs will be kind](../lessons/be-unpredictable-instead-of-assuming-the-world-is-kind.md)
- [Refinement never repairs a growth rate, and a working demo on small inputs is not evidence](../lessons/refinement-never-repairs-a-growth-rate.md)
- [Weaken the problem on purpose, then prove something exact about the weakened version](../lessons/weaken-the-problem-on-purpose-then-prove-something-about-it.md)

Also contributes to (extracted primarily from *Reducibility Among Combinatorial Problems*):
- [Solve a new problem by translating it into one whose difficulty you already know](../lessons/translate-the-new-problem-into-one-you-already-understand.md)
- [Ask how hard the answer is to check before asking how hard it is to find](../lessons/separate-the-cost-of-checking-from-the-cost-of-finding.md)
- [Route many problems through one universal format instead of building translators between every pair](../lessons/route-everything-through-one-universal-format.md)
