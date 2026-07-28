---
type: work
title: "Reaching Approximate Agreement in the Presence of Faults"
figure: lynch
description: Studies a variant of Byzantine agreement where processes start with arbitrary real-valued inputs and only need to converge to within some bounded distance of each other, rather than reach exact agreement. Gives algorithms that solve this approximate version in both synchronous and asynchronous systems, working by iterated rounds of discarding extreme values and averaging what's left. Notable as a positive result sitting right next to FLP's negative one — exact agreement is impossible to guarantee asynchronously, but approximate agreement is not.
subdomains: [distributed-systems-and-concurrency, algorithms-and-complexity]
year: 1986
url: https://groups.csail.mit.edu/tds/papers/Lynch/jacm86.pdf
extraction: complete
survey_pages: 18
survey_text_layer: full
survey_fetch_mb: 1
access: public
host: institutional
tags: [work]
---

# Reaching Approximate Agreement in the Presence of Faults

**Author(s):** with Danny Dolev, Shlomit S. Pinter, Eugene W. Stark, William E. Weihl
**Venue/year:** Journal of the ACM 33(3), July 1986
**Source:** https://groups.csail.mit.edu/tds/papers/Lynch/jacm86.pdf — hosted on MIT CSAIL's Theory of Distributed Systems group publications page (university-hosted), live and directly downloadable (HTTP 200).

## Lessons
- [Check whether the impossibility is about exactness rather than difficulty, because arbitrarily close is often reachable when equal is not](../lessons/impossibility-often-attaches-to-exactness-not-to-closeness.md)
- [Size a robust aggregate by how far two honest observers' views can diverge, not by how many liars there are](../lessons/size-a-robust-aggregate-by-how-far-two-honest-views-can-diverge.md)
- [Turn "eventually" into a quantity that provably shrinks, and both the deadline and the freedom to stop early follow](../lessons/turn-eventually-into-a-quantity-that-shrinks.md)
