---
type: work
title: "A Lower Bound for the Time to Assure Interactive Consistency"
figure: fischer
description: Proves that any protocol assuring interactive consistency (agreement on each other's inputs) in the presence of m crash-faulty processors needs at least m+1 rounds of communication, regardless of how the protocol is built. Introduces the "chain argument" — a sequence of executions each indistinguishable from the next to some correct process — which became a standard technique for proving round-complexity lower bounds in fault-tolerant distributed computing. Short paper, outsized influence: it set the baseline that later round-efficient Byzantine agreement protocols are measured against.
subdomains: [distributed-systems-and-concurrency]
year: 1982
url: https://groups.csail.mit.edu/tds/papers/Lynch/ipl82.pdf
access: public
host: self-archived
tags: [work]
---

# A Lower Bound for the Time to Assure Interactive Consistency

**Author(s):** with Nancy A. Lynch
**Venue/year:** Information Processing Letters 14(4):183-186, June 1982
**Source:** https://groups.csail.mit.edu/tds/papers/Lynch/ipl82.pdf — self-archived PDF on Nancy Lynch's own paper archive at MIT CSAIL (co-author's site), live and directly downloadable (HTTP 200). Confirmed as the published IPL version against MIT CSAIL TDS group's own bibliography (reflist.html), which lists this exact file for this exact citation (the same page also lists the September 1981 Georgia Tech technical report predecessor, GIT-ICS-81/13, as a separate self-archived scan).

## Lessons
- [Before reasoning about every possible implementation, collapse them into one canonical form](../lessons/collapse-the-space-of-candidates-before-arguing-about-all-of-them.md)
- [Connect the executions nobody can tell apart, then walk the chain to a contradiction](../lessons/connect-the-executions-you-cannot-tell-apart.md)
- [Optimal means nothing until you name the resource, and the winner on one resource can be absurd on another](../lessons/optimal-is-meaningless-until-you-name-the-resource.md)
- [The binding constraint on a distributed component is what its local view cannot tell apart](../lessons/what-cannot-be-distinguished-bounds-what-can-be-decided.md)
