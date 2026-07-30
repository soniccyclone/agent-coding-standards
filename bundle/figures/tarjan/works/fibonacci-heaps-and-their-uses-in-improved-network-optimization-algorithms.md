---
type: work
title: "Fibonacci Heaps and Their Uses in Improved Network Optimization Algorithms"
figure: tarjan
description: Develops the Fibonacci heap, a priority-queue structure built from a loose forest of trees rather than a single balanced shape, supporting decrease-key and insert in O(1) amortized time and extract-min in O(log n) amortized time. That combination directly improved the asymptotic running time of network-optimization algorithms that call decrease-key repeatedly, most notably Dijkstra's shortest-path algorithm and algorithms for minimum spanning trees. It's a textbook case of amortized analysis unlocking a better worst-case bound for algorithms built on top of the structure.
subdomains: [algorithms-and-complexity]
year: 1987
url: https://www.cs.princeton.edu/courses/archive/fall03/cs528/handouts/fibonacci%20heaps.pdf
survey_pages: 20
survey_text_layer: ocr
survey_fetch_mb: 2
access: public
host: third-party-rehost
extraction: complete
tags: [work]
---

# Fibonacci Heaps and Their Uses in Improved Network Optimization Algorithms

**Author(s):** Michael L. Fredman, Robert E. Tarjan
**Venue/year:** Journal of the ACM 34(3), 1987, pp. 596-615.
**Source:** https://www.cs.princeton.edu/courses/archive/fall03/cs528/handouts/fibonacci%20heaps.pdf — live page, hosted as course reading material for a Princeton graduate algorithms course (CS528); a scanned copy, image-based with no extractable text layer, so identification rests on the file's title, path, and consistent cross-referencing to this exact paper across independent searches.
**Reading copy:** `scratchpad/ocr-text/tarjan__fibonacci-heaps-and-their-uses-in-improved-network-optimization-algorithms.txt` — OCR of the scanned original by tesseract at 300dpi. Running prose is reliable; **mathematical and logical notation is not** — turnstiles, implication arrows, subscripts and small-caps headings come through mangled. Ground every lesson in the prose argument and do not transcribe or rely on a formula from this text. Page markers `=== page N ===` correspond to PDF pages.

## Lessons
- [Optimize for the caller's operation mix, and let an abstract operation set spread the gain](../lessons/optimize-for-the-callers-operation-mix-not-per-operation-symmetry.md)
- [Prefer an invariant you can prove about your rules to one you have to store and enforce](../lessons/prefer-an-invariant-you-can-prove-to-one-you-must-maintain.md)
- [Tolerate a bounded amount of damage before repairing, and let the accounting pick the threshold](../lessons/let-the-accounting-choose-the-repair-threshold.md)
- [Size each round to the unavoidable floor, then reduce the whole analysis to counting rounds](../lessons/size-each-round-to-the-unavoidable-floor-then-count-rounds.md)
- [A lower bound on your method is not a lower bound on the problem; find what it solves incidentally](../lessons/a-lower-bound-on-your-method-is-not-a-lower-bound-on-the-problem.md)
- [Know which machine your claim needs, and don't let a convenience strengthen the assumption](../lessons/know-which-machine-your-claim-needs.md)
