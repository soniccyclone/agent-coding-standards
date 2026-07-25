---
type: lesson
title: "Effort and elapsed time trade only for work whose parts need not agree; where they must agree, coordination grows faster than the division saves"
figure: brooks
works: [mythical-man-month]
axes: [parallelizability, cognitive-load]
subdomains: [software-engineering-and-architecture, distributed-systems-and-concurrency]
tags: [lesson]
---
# Effort and elapsed time trade only for work whose parts need not agree; where they must agree, coordination grows faster than the division saves

**Lesson:** Cost scales with people multiplied by duration. Progress does not, and treating the product of the two as a unit of work smuggles in the assumption that the two factors are interchangeable. They are interchangeable only for tasks that partition with no communication between the parts, which describes harvesting a field and describes almost nothing about constructing a system. When a task cannot be partitioned at all, because each step needs the result of the last, extra hands buy nothing whatever. When it can be partitioned but the pieces must be kept mutually consistent, the coordination effort has to be added to the work, so the trade is always worse than even. Bringing every worker up to speed on the goal, the strategy, and the plan costs effort that scales with headcount and cannot itself be divided, while pairwise reconciliation grows quadratically and joint decisions worse than that.

Once the coordination term dominates, adding people to a project that is already behind pushes the finish date further out. The mechanism is worth tracing rather than accepting as a slogan: newcomers consume the time of the experienced, the work must be repartitioned so some completed effort is discarded, the number of interfaces rises so integration lengthens, and a team of a new size is a different organizational animal rather than the same one scaled. All of that lands in the period when the schedule is already tightest, which is why the response tempts a second application and a third.

The transferable reasoning is a decomposition test applied before staffing, not after. Duration is set by the chain of things that must happen in order; the useful headcount is set by the number of genuinely independent pieces; and those two numbers together define the schedules that exist. You can always spend more months with fewer people, and you can never buy months with people. This is the same analysis one applies to parallel execution, where speedup is bounded by the serial fraction and eaten further by communication, and the isomorphism is not a metaphor: in both cases the question is how much hidden agreement the pieces require. Systems whose parts must share mutable assumptions resist division whether the workers are processors or people.

**Source:** [The Mythical Man-Month](../works/mythical-man-month.md) — the title chapter, which works through the partitionable, unpartitionable, and communication-bearing cases and then traces the staffing of a late project step by step to the law now carrying the author's name.
