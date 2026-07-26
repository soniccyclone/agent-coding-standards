---
type: work
title: "Paths, Trees, and Flowers"
figure: edmonds
description: Edmonds gives a matching algorithm for general (non-bipartite) graphs that runs in polynomial time, handling odd cycles by "shrinking" them into single pseudo-vertices (the "blossom" technique) so the tree-growing search for augmenting paths stays efficient. Along the way he generalizes König's theorem on bipartite matching-cover duality to arbitrary graphs. Section 2's "Digression" is the paper's real bombshell: it explicitly proposes polynomial ("good") versus exponential growth as the dividing line for tractability, years before the P/NP vocabulary existed.
subdomains: [algorithms-and-complexity]
year: 1965
url: https://www.cambridge.org/core/services/aop-cambridge-core/content/view/08B492B72322C4130AE800C0610E0E21/S0008414X00039419a.pdf/paths-trees-and-flowers.pdf
access: public
host: institutional
tags: [work]
---

# Paths, Trees, and Flowers

**Venue/year:** Canadian Journal of Mathematics 17, 1965, pp. 449-467. DOI: 10.4153/CJM-1965-045-4.
**Source:** https://www.cambridge.org/core/services/aop-cambridge-core/content/view/08B492B72322C4130AE800C0610E0E21/S0008414X00039419a.pdf/paths-trees-and-flowers.pdf — direct PDF from Cambridge University Press (the journal's official publisher), served without a login/paywall gate on this asset path even though the HTML landing page shows a subscription banner. Verified by fetching and reading the full 19-page PDF: opens "PATHS, TREES, AND FLOWERS / JACK EDMONDS", matches the published pagination (449-467), and includes the "Received November 22, 1963" note and NBS/Princeton affiliation. A secondary NIST commemorative essay of the same title (nvlpubs.nist.gov/nistpubs/sp958-lide/140-144.pdf, referenced in the Phase 1/2 stub) turned out to be a historical write-up *about* this paper by Christoph Witzgall, not the paper itself, and its URL is dead besides (confirmed via Wayback); it was not used as the source.

## Lessons
- [Whether an affordable method exists at all is a claim you can prove or refute, so state it and pick a cost measure that cannot be gamed](../lessons/prove-that-an-affordable-method-exists.md)
- [When one shape of input defeats your method, collapse that shape into a single opaque object and work in the world where it cannot occur](../lessons/contract-the-obstruction-instead-of-special-casing-it.md)
- [Design so that the method's inability to improve the answer is itself the proof the answer is best, checkable without rerunning the method](../lessons/make-failure-hand-you-the-proof.md)
- [Efficiency comes from never re-examining the same evidence: build a structure that accumulates what you learn instead of a search that retries combinations](../lessons/spend-each-piece-of-evidence-once.md)
- [Find out which of your method's choices are incidental and which fix the answer, because the incidental ones are freedom you have already paid for](../lessons/separate-what-the-run-chooses-from-what-the-problem-determines.md)
- [Look for a description of your feasible set in a language that already has machinery, so the hard condition dissolves instead of being enforced](../lessons/trade-a-discreteness-condition-for-the-right-continuous-description.md)
