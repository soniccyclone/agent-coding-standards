---
type: lesson
title: "Efficiency Is Usually Paid For in Redundancy You Were Not Tracking"
figure: corbato
works: [on-building-systems-that-will-fail]
axes: [verifiability, cognitive-load, hardware-affinity]
subdomains: [operating-systems-and-systems-programming, distributed-systems-and-concurrency, software-engineering-and-architecture]
tags: [lesson]
---
# Efficiency Is Usually Paid For in Redundancy You Were Not Tracking

**Lesson:** Corbató's telephone-network example in the Turing lecture is the cleanest statement of a mechanism that keeps catching mature systems. Replacing copper with fiber was justified entirely on capacity per dollar, and on those terms it was obviously correct. But one fiber carries what thousands of wires carried, so the physical graph gets sparser as it gets cheaper: fewer links, fewer paths between any two points, more traffic behind each one. Nothing in the justification mentioned redundancy, because the redundancy had never been a line item. It was a side effect of the old technology being inefficient. He puts two consequences next to it — a fire in one switching facility cutting service to an enormous number of customers for weeks, a single backhoe in one state stopping the financial exchanges in another — and names the pattern for what it is: efficiency having gotten out in front of robustness.

The reason this is hard rather than merely unfortunate is that the quantity being consumed is invisible on both sides of the trade. Efficiency gains are measurable, immediate, and attributable to whoever delivered them. Failure independence has no reading anywhere; you cannot inspect a running system and see how correlated its failure modes have become, any more than, as he notes elsewhere in the same talk, you can look at a system and see its privacy and security posture. He extends the point to storage: devices became reliable enough that even experienced users stopped genuinely believing in loss, and vendors had every reason not to raise the subject. Reliability high enough to lull is more dangerous than reliability low enough to keep everyone honest, because the belief degrades faster than the hardware.

His prescription is to keep asking what-if against a long, deliberately mixed list — hardware failure, human error, malice, fire, earthquake, media rot, and the slow loss of institutional knowledge about how recovery is supposed to work. He is also honest that this is not easy, because doing it properly means attaching likelihoods to events and reasoning about whether those events are independent, and independence is exactly the thing consolidation quietly destroys. He adds that we have no good shared language for discussing risk at all, which is why the discourse degenerates into misused statistics or into absolutes that cannot be true — an unsaturatable shield, a reactor that cannot overheat.

Someone who has taken this on board treats every consolidation as a change to the failure model and not only to the cost model: merging two services, collapsing two regions to one, replacing several modest components with a single excellent one. Before accepting the efficiency, they ask which correlated failure just became possible and whether anything would reveal it before the day it happens. The habit is not pessimism about the improvement; it is refusing to let a benefit that is easy to measure settle an argument against a cost that is not.

**Source:** [On Building Systems That Will Fail](../works/on-building-systems-that-will-fail.md) — the sources-of-complexity discussion, specifically the passages on rapid technology-driven change in the telephone plant and the two service outages that followed from it, on the false confidence induced by highly reliable storage devices, and on the absence of a usable language for discussing risk.
