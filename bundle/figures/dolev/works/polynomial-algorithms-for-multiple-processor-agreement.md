---
type: work
title: "Polynomial Algorithms for Multiple Processor Agreement"
figure: dolev
description: Gives a Byzantine agreement protocol built on digital signatures (authenticated messages) that runs in polynomial time and message complexity, in contrast to the earlier oral-message protocols of Lamport, Shostak, and Pease whose cost grew exponentially in the number of faults tolerated. Matches the t+1 round lower bound for agreement under t faults. Became the standard template — the "Dolev-Strong protocol" — for essentially all later authenticated Byzantine agreement work.
subdomains: [distributed-systems-and-concurrency, algorithms-and-complexity]
year: 1982
url: https://www.cs.huji.ac.il/~dolev/pubs/p401-dolev.pdf
access: public
host: self-archived
tags: [work]
---

# Polynomial Algorithms for Multiple Processor Agreement

**Author(s):** with H. Raymond Strong
**Venue/year:** 14th ACM Symposium on Theory of Computing (STOC), May 1982, pp. 401-407
**Source:** https://www.cs.huji.ac.il/~dolev/pubs/p401-dolev.pdf — self-archived PDF on Dolev's own HUJI publications page, live and directly downloadable (HTTP 200).

## Lessons
- [A tight bound on one resource says nothing about the resource that decides feasibility](../lessons/count-the-resource-the-machine-actually-spends.md)
- [A mechanism you depend on is a bundle of properties; name them and you may not need the mechanism](../lessons/name-the-properties-a-mechanism-buys-then-rebuild-them.md)
- [What a participant cannot tell apart is the whole argument](../lessons/what-participants-cannot-distinguish-bounds-every-protocol.md)
- [You will never learn who failed; scope correctness to a budget instead](../lessons/correctness-holds-inside-a-fault-budget.md)
- [Let the failure budget do the filtering, so no step ever needs to know which inputs were lies](../lessons/build-operators-safe-against-any-budgeted-adversary.md)
