---
type: work
title: "Reaching Approximate Agreement in the Presence of Faults"
figure: dolev
description: Relaxes exact agreement to approximate agreement — processes only need to converge to values within some epsilon of each other, not to an identical value. Shows this weaker goal is achievable under Byzantine faults using iterative, averaging-style protocols, and works out the precision and fault-tolerance bounds those protocols can actually hit. Underpins later clock-synchronization and sensor-fusion style convergence protocols that don't need exact consensus.
subdomains: [distributed-systems-and-concurrency, algorithms-and-complexity]
year: 1986
url: https://www.cs.huji.ac.il/~dolev/pubs/p499-dolev.pdf
access: public
host: self-archived
tags: [work]
---

# Reaching Approximate Agreement in the Presence of Faults

**Author(s):** with Nancy A. Lynch, Shlomit S. Pinter, Eugene W. Stark, and William E. Weihl
**Venue/year:** Journal of the ACM 33(3), 1986, pp. 499-516
**Source:** https://www.cs.huji.ac.il/~dolev/pubs/p499-dolev.pdf — self-archived PDF on Dolev's own HUJI publications page, live and directly downloadable (HTTP 200).

## Lessons
- [Having weakened the requirement, solve it directly instead of layering it over the strong primitive](../lessons/solve-the-weak-problem-natively-not-on-top-of-the-strong-one.md)
- [Budget failures happening at once, not failures ever; then rejoining costs nothing](../lessons/budget-simultaneous-failure-not-lifetime-failure.md)
- [Optimal is always optimal-within-a-class; state the class, because that is where the next gain lives](../lessons/optimality-is-relative-to-the-class-you-chose.md)
- [The exact shape of the agreement you demand is the biggest lever you have, and its price is discontinuous](../lessons/the-shape-of-agreement-you-demand-is-the-largest-lever.md)
- [Let the failure budget do the filtering, so no step ever needs to know which inputs were lies](../lessons/build-operators-safe-against-any-budgeted-adversary.md)
