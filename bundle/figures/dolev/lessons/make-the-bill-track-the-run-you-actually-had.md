---
type: lesson
title: "A worst-case bound is a statement about the worst case, not a licence to charge for it every time"
figure: dolev
works: [early-stopping-in-byzantine-agreement]
axes: [parallelizability, hardware-affinity, verifiability]
subdomains: [distributed-systems-and-concurrency, algorithms-and-complexity]
tags: [lesson]
---
# A worst-case bound is a statement about the worst case, not a licence to charge for it every time

**Lesson:** Once a lower bound is proved in terms of a tolerance parameter, the usual next step is to build something that always pays it and call the matter settled. That conflates two different quantities: how much adversity the system is prepared for, and how much adversity this particular run contained. They are independent, and the second is almost always much smaller. The question worth asking is whether a construction can be made whose cost is a function of what actually happened rather than of what was provisioned for, so a quiet run finishes quickly and only a genuinely hostile run pays the full bill. Framed that way, the interesting theorem is not a constant but a function of the observed fault pattern, and the interesting engineering target is a protocol that meets that function pointwise.

Two results have to be established to make this real, and they cut in opposite directions. On the positive side, when the requirement permits it, cost can be made to track the number of failures that actually occurred, plus a small constant, rather than the number provisioned for; and the matching lower bound proves nothing better is available, so the adaptivity is complete rather than opportunistic. On the negative side, some requirements admit no adaptivity whatsoever. Demanding that every participant act at the same moment forces the full provisioned cost even in runs where absolutely nothing went wrong, and that holds even against the tamest failures imaginable. So adaptivity is not a technique you can always apply; whether it is available at all is decided by the shape of the specification, and that check has to come first.

The transferable habit is to keep the provisioning parameter and the observed-adversity parameter separate in your head and in your cost claims. Any system sized for a rare worst case — retry budgets, quorum waits, timeout ladders, reconciliation passes — is a candidate for the question "does this pay worst case even when nothing is wrong?" A surprising amount of software does, because the worst-case bound got compiled into a constant somewhere early and nobody revisited it. And there is a subtler distinction the same analysis forces into the open: knowing the answer and being finished are different events, since a participant may be able to name its output well before it is permitted to stop talking. Cost accounting that stops at the first of those two moments understates what the protocol actually costs.

**Source:** [Early Stopping in Byzantine Agreement](../works/early-stopping-in-byzantine-agreement.md) — the question posed in the introduction of whether the round count can shrink when actual failures fall below the provisioned bound, the negative answer for the simultaneous variant even in failure-free runs, the positive bound expressed as a function of the actual failure count, the matching algorithm, and the paper's insistence on counting rounds until participants stop rather than until they know their output.
