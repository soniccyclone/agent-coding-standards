---
type: lesson
title: "When a technique 'doesn't work,' suspect the relation between its parts before condemning any one part"
figure: denning
works: [thrashing-its-causes-and-prevention, virtual-memory]
axes: [hardware-affinity, cognitive-load]
subdomains: [operating-systems-and-systems-programming, software-engineering-and-architecture]
tags: [lesson]
---
# When a technique "doesn't work," suspect the relation between its parts before condemning any one part

**Lesson:** Measured paging systems of the late 1960s performed badly, and the field's reaction was to blame the programs: real code, it was argued, simply does not behave in a way paging can exploit, so paging should be abandoned. Denning accepts the measurements and rejects the diagnosis. The collapse is not a property of program behavior, nor of the replacement rule, nor of the machine's configuration. It is a property of the three taken together — how a program's references cluster, what the policy does with that clustering, and how far apart in speed the two storage levels are. Hold two fixed and vary the third and the collapse appears or vanishes. None of them is the culprit alone, which is why every experiment that isolates one of them reaches a confident and wrong conclusion.

This matters as a habit because of what each diagnosis licenses. A failure attributed to a component invites replacing the component, which is normally the most expensive repair available and often the least effective. A failure attributed to a relation invites a cheaper question: which term in the relation is easiest to move? Here two terms were cheap. Bound the offered load so the policy never operates in the regime where programs take memory from each other, and shrink the speed gap by inserting an intermediate storage level between fast memory and the mechanical device. Both leave the mechanism the critics wanted to discard fully intact, and the second one had already been observed to multiply throughput on a real installation.

The survey generalizes the same move. Sorting the subject into machinery and the rules governing the machinery, Denning observes that the field's accumulated disappointments trace to bad rules rather than bad machinery — a claim you cannot even formulate until you have separated the two. A technique that fails under one policy and succeeds under another was never the thing on trial; the argument was about a policy the whole time, and the mechanism was standing in for it.

What a programmer does differently: before ripping out a subsystem that "doesn't scale" or "doesn't work here," enumerate the terms whose interaction produced the symptom, and price the movement of each. The relation usually has one cheap term, and the component everyone wants to delete is usually not it.

**Source:** [Thrashing: Its Causes and Prevention](../works/thrashing-its-causes-and-prevention.md) — the introduction's rebuttal to the proposal that paging be abandoned, replacing "unfavorable program behavior" with a three-way relationship among behavior, algorithm, and hardware configuration, and the two-part remedy that closes the paper. [Virtual Memory](../works/virtual-memory.md) — the introduction's insistence that the observed inadequacies came from the policies rather than the mechanisms.
