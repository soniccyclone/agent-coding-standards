---
type: work
title: "The Complexity of Theorem Proving Procedures"
figure: cook
description: Introduces what became known as the Cook-Levin theorem, showing that Boolean satisfiability (SAT) is at least as hard as any problem solvable by a nondeterministic polynomial-time Turing machine, and that several other combinatorial problems reduce to it in polynomial time. The paper is the founding document of NP-completeness: it defines polynomial-time reducibility as the tool for comparing problem difficulty and identifies SAT as the first problem proven complete for the class. Nearly every later intractability result traces its reduction chain back to this construction.
subdomains: [algorithms-and-complexity]
year: 1971
url: http://www.cs.toronto.edu/~sacook/homepage/1971.pdf
access: public
host: self-archived
tags: [work]
---

# The Complexity of Theorem Proving Procedures

**Venue/year:** Proceedings of the Third Annual ACM Symposium on Theory of Computing (STOC), May 1971, pp. 151-158.
**Source:** http://www.cs.toronto.edu/~sacook/homepage/1971.pdf — scanned PDF self-archived on Cook's University of Toronto homepage (verified HTTP 200); a retyped version by Tim Rohls is also linked from the same page at http://4mhz.de/cook.html.

## Lessons
- [When you cannot measure a problem's cost, measure the cheap translations between problems instead](../lessons/compare-difficulty-by-translation-not-measurement.md)
- [A whole execution can be reified as one static constraint object, and then attacked with tools that cannot touch running programs](../lessons/turn-a-computation-into-a-static-object-you-can-solve.md)
- [Performance on examples cannot rank competing implementations — define a cost measure parameterized on the dimension that actually drives the work](../lessons/benchmarks-cannot-rank-implementations-a-cost-measure-can.md)
- [Before grinding harder, check whether your technique could ever reach the conclusion](../lessons/audit-whether-your-technique-can-reach-the-conclusion.md)
