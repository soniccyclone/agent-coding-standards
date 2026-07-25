---
type: lesson
title: "Allocate the scarce resource before detailed work spends it for you"
figure: royce
works: [managing-the-development-of-large-software-systems]
axes: [hardware-affinity, cognitive-load]
subdomains: [software-engineering-and-architecture]
tags: [lesson]
---
# Allocate the scarce resource before detailed work spends it for you

**Lesson:** Royce's first corrective is to do a whole-program design before the detailed analysis rather than after it, and he grants the obvious objection immediately: the designer is working from nearly nothing and the design will be partly wrong. His reply is that this misses what the exercise is for. Being provisionally wrong about the global shape costs less than being locally right with no global budget in force. Once execution time, storage, data flow and interfaces have been divided up, everyone doing detailed work operates inside a fixed envelope, and any request for more of a scarce resource becomes visibly a request to take that resource away from someone else. Accuracy is not the point. Making a shared constraint zero-sum, and making each participant feel it, is the point.

The reason this holds is that locally reasonable decisions about a shared finite resource do not compose. Every analyst who needs slightly more memory or slightly more time to implement their equations properly is individually justified. The sum of those justified requests is infeasible, and under a late-design order the infeasibility only becomes apparent once everyone has already committed detailed work to their own local optimum. An early allocation, even a crude one, converts an invisible aggregate into a negotiation that individual participants can perceive and resolve while resolution is still cheap.

There is a second thing the early pass buys: if the total resources available are simply insufficient, or the operating concept is wrong at the root, that becomes knowable before the expensive detailed work exists to be discarded. A budget is a cheap feasibility test as well as a coordination device.

The habit this produces is fixing the envelope before writing the parts that consume it. Decide the latency budget, the memory ceiling, the allowed number of round trips, the shape of the interfaces, in advance and in the open, expecting the first numbers to be wrong and expecting to revise them against measurement later. The early allocation's job is to surface the conflicts that would otherwise be discovered by summation at the end.

**Source:** [Managing the Development of Large Software Systems](../works/managing-the-development-of-large-software-systems.md) — the "program design comes first" corrective, including its answer to the criticism that designing before analysis means designing in a vacuum, and the mechanism by which constraints are imposed on the analysts so they feel the trade.
