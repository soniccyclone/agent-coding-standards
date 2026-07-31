---
type: work
title: "Should Tables Be Sorted?"
figure: yao
description: Studies the lower bound on the number of probes needed to answer membership queries ("is x in S?") against a stored table, comparing sorted-table binary search against hash-table and other schemes. Shows that in a general model covering common table implementations, roughly log(n) probes are unavoidable in the worst case, which motivated later work on the cell-probe model. A foundational paper in the complexity theory of data structures.
subdomains: [algorithms-and-complexity, databases-and-data-management]
year: 1981
url: https://www.cs.umd.edu/users/gasarch/COURSES/858/S13/tables.pdf
survey_pages: 14
survey_text_layer: full
survey_fetch_mb: 0
access: public
host: third-party-rehost
extraction: complete
tags: [work]
---

# Should Tables Be Sorted?

**Author(s):** Andrew Chi-Chih Yao
**Venue/year:** Journal of the ACM, Vol. 28, No. 3, July 1981, pp. 615-628.
**Source:** https://www.cs.umd.edu/users/gasarch/COURSES/858/S13/tables.pdf — course materials page at University of Maryland (William Gasarch's complexity theory course), a standard academic rehost. Verified by rendering page 1: title, "Andrew Chi-Chih Yao, Stanford University," and the JACM 1981 copyright line are all visible.

## Lessons
- [Permission to store a function of your data is a different power from permission to store the data](../lessons/storing-a-function-of-your-data-is-a-different-power-than-storing-it.md)
- [You cannot analyze an arbitrary implementation, so force it onto inputs where it must behave uniformly](../lessons/force-an-arbitrary-opponent-into-a-case-you-already-understand.md)
- [Argue in the smallest model that makes the reasoning legible, then widen it until every rival design is inside](../lessons/prove-it-in-the-small-model-then-widen-until-the-rivals-are-inside.md)
- [When both extremes of a parameter are easy for opposite reasons, the hard case is the middle](../lessons/when-both-extremes-are-easy-the-difficulty-lives-in-the-middle.md)
- [A guarantee that only switches on past every real input is not an answer yet — invert it into a reach question](../lessons/a-guarantee-that-starts-past-every-real-input-is-not-yet-an-answer.md)
- [In a construction that is already at the limit, the ugly exception is load-bearing — delete it and watch it fail](../lessons/in-an-extremal-construction-the-ugly-exception-is-load-bearing.md)
- [Say which question your fast path actually answers, because the cheap one and the useful one are rarely the same](../lessons/say-which-question-your-fast-path-actually-answers.md)
- [To get a claim that outlives the hardware, let the machine-dependent quantity diverge instead of fixing a plausible value](../lessons/let-the-machine-dependent-quantity-diverge-instead-of-picking-a-plausible-value.md)
