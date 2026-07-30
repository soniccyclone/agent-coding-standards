---
type: work
title: "On the Complexity of Bounded-Variable Queries"
figure: vardi
description: Studies what happens to relational-calculus queries once you cap how many distinct variables a formula may reuse, a restriction motivated by both descriptive complexity (finite-variable logics) and practical query optimization. Vardi ties the complexity of evaluating and comparing such queries to pebble-game characterizations from finite model theory, giving precise bounds that depend on the variable cap rather than on formula size alone. It is a direct example of the finite-model-theory-meets-query-languages approach that is central to his database-theory work.
subdomains: [databases-and-data-management, algorithms-and-complexity]
year: 1995
url: http://www.cs.rice.edu/~vardi/papers/pods95.pdf
survey_pages: 11
survey_text_layer: full
survey_fetch_mb: 0
access: public
host: self-archived
extraction: complete
tags: [work]
---

# On the Complexity of Bounded-Variable Queries

**Venue/year:** PODS 1995 (14th ACM SIGACT-SIGMOD-SIGART Symposium on Principles of Database Systems), pp. 266-276.
**Source:** http://www.cs.rice.edu/~vardi/papers/pods95.pdf — verified live (HTTP 200, application/pdf, ~228KB), self-archived on Vardi's own Rice University papers page.
**Host:** self-archived — author's own site.

## Lessons
- [Find the quantity that actually blows up, then bound it with something checkable in the text](../lessons/find-the-quantity-that-actually-blows-up-then-bound-it-syntactically.md)
- [Length is cheap, simultaneity is not: reuse names to keep the working set narrow](../lessons/length-is-cheap-simultaneity-is-not-reuse-your-names.md)
- [Equal expressive power does not mean equal leverage: techniques attach to structure, not to what is sayable](../lessons/equal-expressive-power-does-not-mean-equal-proof-leverage.md)
- [Replace an inner recomputation with a guess you can check, and a product of costs becomes a sum](../lessons/replace-inner-recomputation-with-a-guess-you-can-check.md)
- [A whole you only ever observe through a few narrow windows can be replaced by the windows, plus the coherence you just gave up](../lessons/replace-an-unobservable-whole-with-its-observations-plus-coherence.md)
- [Finitize one dimension and evaluation stops being computation, becoming recognition](../lessons/finitize-one-dimension-and-evaluation-becomes-recognition.md)
- [When a normalization removes a parameter, find where the cost went before calling it a simplification](../lessons/when-a-normalization-removes-a-parameter-find-where-the-cost-went.md)
