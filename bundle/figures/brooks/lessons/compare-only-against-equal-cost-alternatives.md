---
type: lesson
title: "A design is only good relative to alternatives costing the same, and the metric that decides belongs at the level of the user's result, not the component's"
figure: brooks
works: [architecture-of-the-ibm-system-360, mythical-man-month]
axes: [hardware-affinity, cognitive-load]
subdomains: [operating-systems-and-systems-programming, software-engineering-and-architecture]
tags: [lesson]
---
# A design is only good relative to alternatives costing the same, and the metric that decides belongs at the level of the user's result, not the component's

**Lesson:** Goodness is not a property a design has by itself. It is a comparison, and the comparison is only meaningful between candidates that consume the same resources. Absolute complaints — this consumes too much memory, this is slower than it could be — carry no information until the resources are held fixed and the question becomes what else that budget could have bought. A large share of a machine's storage spent on the software that manages it is not extravagance or thrift; it is a placement decision, defensible exactly insofar as the storage does more for the user there than it would have done as additional capacity or additional processing elsewhere. Cost is never zero, so the only real question is where a fixed cost has been put.

The companion move is choosing what to measure. The natural metrics are the local ones, because they belong to the component and can be read off it: operations per unit time, bytes occupied, instructions executed. Those are the wrong ones, and being locally optimal on them can make the whole worse — the recorded case is a set of components each honouring its own space budget by fragmenting itself into pieces fetched on demand, every one of them within target while the assembled system thrashed and the compiler crawled. What actually matters is the rate at which the user gets answers, measured over the whole apparatus including the humans and the turnaround. A metric at that level makes some strange-looking trades obviously correct: accepting a handicap on one component because the systemic saving elsewhere is larger, or spending decoding time to avoid touching slow storage, or paying storage to buy speed across a range so wide that the trade remains favourable throughout it.

Holding both ideas at once changes how proposals get argued. A cost is not an objection; it is half of a ratio whose other half must be produced. A component's local excellence is not a defence; someone has to show the effect at the level where value is realised. And a team measured only on local targets will optimise itself into a system nobody wants, each member honestly meeting the number they were given — so the choice of what to measure is itself a design decision, made early, with the same care as the interfaces.

**Source:** [Architecture of the IBM System/360](../works/architecture-of-the-ibm-system-360.md) — the efficient-performance section, which fixes the measure as performance against other designs of equal cost and justifies accepting the compatibility handicap by the larger saving it buys, together with the design-objectives passage relocating the measure of an information system's value from machine-level rates to delivered results; also [The Mythical Man-Month](../works/mythical-man-month.md), whose chapter on space as a cost makes the same argument about resident software occupying memory, and reports the budgeting failure in which locally compliant components produced a system-level collapse.
