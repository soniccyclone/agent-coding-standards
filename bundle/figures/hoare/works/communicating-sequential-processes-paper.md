---
type: work
title: "Communicating Sequential Processes"
figure: hoare
description: The original CACM paper introducing CSP, proposing that input and output be treated as primitive operations and that parallel composition of guarded, communicating processes be a basic program-structuring method rather than an afterthought bolted onto sequential languages. Introduces the core notation for processes, guarded alternation, and synchronized communication that the later book expands into a full theory. Precedes and motivates the more mathematically developed 1985 book of the same name.
subdomains: [distributed-systems-and-concurrency]
year: 1978
url: http://www.cs.cmu.edu/~crary/819-f09/Hoare78.pdf
survey_pages: 12
survey_text_layer: full
survey_fetch_mb: 1
access: public
host: third-party-rehost
tags: [work]
---

# Communicating Sequential Processes

**Author(s):** C. A. R. Hoare
**Venue/year:** Communications of the ACM 21(8), August 1978, pp. 666-677.
**Source:** http://www.cs.cmu.edu/~crary/819-f09/Hoare78.pdf — course-reading mirror hosted by Karl Crary for a CMU graduate course (819, Fall 2009). The original Phase 1 pass flagged this as paywalled/uncertain (ACM Digital Library gates the canonical copy); PDF metadata on this mirror confirms it directly: Title "Communicating sequential processes", Author "C. A. R. Hoare", Subject "http://doi.acm.org/10.1145/359576.359585", CreationDate 1978-08-02.

## Lessons
- [Test a candidate primitive by re-deriving the constructs it should replace, then keep them anyway](../lessons/re-derive-the-constructs-to-test-a-primitive-then-keep-them.md)
- [Never let correctness rest on a courtesy the implementation was never obliged to provide](../lessons/never-let-correctness-rest-on-a-courtesy.md)
- [When two candidate primitives can each define the other, the tiebreak has to come from outside the algebra](../lessons/interderivable-features-need-a-tiebreak-from-outside.md)
- [Define an unbounded facility as the limit of bounded ones, so no run needs semantics the bounded language lacks](../lessons/define-the-unbounded-case-as-the-limit-of-bounded-ones.md)
- [Prove a construct is missing with a closure property, not with an appeal to symmetry](../lessons/prove-a-construct-is-missing-with-a-closure-property.md)
- [Rate a convenience by what retreating from it would cost, and ship the restrictive version first](../lessons/rate-a-convenience-by-the-cost-of-retreating-from-it.md)
