---
type: work
title: "Early Stopping in Byzantine Agreement"
figure: dolev
description: Distinguishes Eventual Byzantine Agreement (processes can decide at different times) from Simultaneous Byzantine Agreement (all processes must decide in the same round), and shows that protocols don't have to pay for the worst case every time. When the actual number of faults f in a run is below the assumed bound t, agreement can be reached in f+2 rounds rather than the full t+1 worst-case bound. Gives the first round-optimal early-stopping protocols matching a proven lower bound, so termination speed scales with how bad the run actually is rather than how bad it could be.
subdomains: [distributed-systems-and-concurrency]
year: 1990
url: https://courses.csail.mit.edu/6.897/fall04/papers/Dolev/drs.pdf
extraction: complete
access: public
host: third-party-rehost
tags: [work]
---

# Early Stopping in Byzantine Agreement

**Author(s):** with Rüdiger Reischuk and H. Raymond Strong
**Venue/year:** Journal of the ACM 37(4), 1990, pp. 720-741
**Source:** https://courses.csail.mit.edu/6.897/fall04/papers/Dolev/drs.pdf — course-materials mirror on MIT's csail.mit.edu (6.897 distributed algorithms, Fall 2004), live and directly downloadable (HTTP 200, application/pdf). No copy found on Dolev's own HUJI page or elsewhere self-archived; this is a legitimate institutional course mirror, not a redistribution site.

## Lessons
- [A worst-case bound is a statement about the worst case, not a licence to charge for it every time](../lessons/make-the-bill-track-the-run-you-actually-had.md)
- [The exact shape of the agreement you demand is the biggest lever you have, and its price is discontinuous](../lessons/the-shape-of-agreement-you-demand-is-the-largest-lever.md)
- [Optimal is always optimal-within-a-class; state the class, because that is where the next gain lives](../lessons/optimality-is-relative-to-the-class-you-chose.md)
- [What a participant cannot tell apart is the whole argument](../lessons/what-participants-cannot-distinguish-bounds-every-protocol.md)
- [Let the failure budget do the filtering, so no step ever needs to know which inputs were lies](../lessons/build-operators-safe-against-any-budgeted-adversary.md)
