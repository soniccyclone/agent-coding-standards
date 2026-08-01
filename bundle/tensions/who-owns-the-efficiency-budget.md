---
type: tension
title: "Who owns the efficiency budget an abstraction spends"
figures: [wilkes, hoare]
lessons: [wilkes/the-efficiency-objection-is-usually-valid-and-usually-loses, hoare/dont-pre-spend-your-users-efficiency-budget]
status: resolved-by-llm
tags: [tension]
---
# Who owns the efficiency budget an abstraction spends

## The decision
You are building a tool that raises the level at which other people work, and the mediated version costs a large multiple of the hand-built one in both time and space. The clarity or capability gain is real; nobody disputes the measurement. Do you ship it anyway, or does the multiple itself veto the design?

## Wilkes: the machine cost is real, correctly measured, and still not the deciding number
[Learn to recognize the efficiency objection that is valid and still loses](../figures/wilkes/lessons/the-efficiency-objection-is-usually-valid-and-usually-loses.md) says the objection recurs unchanged at every level and is normally correct on its own terms. Wilkes's move is not to deny the arithmetic but to point out that the two sides are counting different resources, one of which the entire industry is organized to make cheaper and one of which does not grow at all. When an abstraction trades machine capacity for the number of people able to attempt the work and the size of what any one of them can attempt, the trade runs toward the resource that stays scarce. He does not treat this as a licence: the exchange has to actually happen, and an advocate who claims the abstraction is free rather than conceding the cost and disputing its weight destroys their own credibility.

## Hoare: the budget belongs to whoever is closest to the problem, and a large multiple is taken, not spent
[Don't pre-spend your users' efficiency budget](../figures/hoare/lessons/dont-pre-spend-your-users-efficiency-budget.md) grants that every abstraction has slack and that trading ten or twenty percent for clarity or safety is ordinary engineering. What he refuses is the scale. A factor of two or ten is not a design choice the builder is entitled to make, because the person who can see which parts of a program deserve the spending is the person writing that program, not the person writing the tool. When the budget is consumed before the user arrives, the user's response is to obscure their own structure to claw the headroom back, which is the exact opposite of what the abstraction was supposed to buy. His constructive half matters here: make the plain translation non-wasteful, and make the notation expressive enough that the improvements users care about can be stated rather than hoped for.

## Resolution
**LLM DECISION — Nathan may overturn.**

The deciding property is not the size of the multiple but whether the cost is opt-out-able at the granularity where a program actually needs the performance. Where a user who finds the abstraction too expensive in one specific place can recover the speed there, locally, without abandoning the abstraction everywhere, Wilkes governs and the objection loses at any magnitude. Where the multiple is a uniform, unavoidable tax on every operation of every program regardless of whether that operation needed the abstraction, Hoare governs and the multiple is theft.

This is what makes Wilkes's historical cases come out the way they did. Fortran did not take the assembler away; the inner loop could still be hand-coded and linked in. Time sharing did not remove the option of booking the machine for a run that needed it. In both cases the multiple was paid by default and refusable in the specific place a program could not afford it, so the users who needed the old performance kept it and everybody else got the capability. Hoare's ten-to-twenty-percent line is best read as a proxy for the same property rather than as an independent threshold: at that size nobody needs an escape hatch, so the question of who holds the budget never arises. Past it the question becomes live, and his answer is not that the cost is too large in the abstract but that a cost this large has to be steerable by the person who can see the program.

Read that way the two lessons converge on the same requirement from opposite directions. Wilkes's guard, that the abstraction must genuinely convert scarce human effort into abundant machine effort rather than being an overhead that buys nothing, is a claim about the trade being real. Hoare's demand, that the notation be expressive enough for users to state the improvements they care about, is the mechanism that keeps the trade refusable where it turns out not to be worth it. Ship the multiple, concede the measurement in public, and leave a usable path back down. A builder who does all three has not taken anything.

The practical test a designer can apply: name the place a user would go if your abstraction turned out to cost too much in their hot path, and check that the path exists, is documented, and does not require abandoning the rest of the system. If you cannot name it, you have taken the budget rather than spent it, and Hoare's objection stands regardless of how good the trade looks on average.

**Strongest counter-argument:** the escape hatch is usually a fiction. Hoare could grant every word above and answer that in practice the local drop-down does not exist in usable form, and pointing at it is how builders launder a uniform tax as a refusable one. Writing one procedure in assembly against a compiler's calling convention, suppressing collection for one object graph, disabling bounds checks in one loop, each of these is nominally available and in practice attempted by almost nobody, because the escape is priced in expertise the user does not have and the abstraction's own invariants usually break when you leave it. If the hatch is real only on paper, the uniformity test collapses into Wilkes's position by default, and Hoare's blunt magnitude threshold is the only guard that actually binds. Overturning this resolution means holding that an escape hatch counts only when it is demonstrably used, which would move the burden of proof onto the builder and put the ten-to-twenty-percent line back in force for everyone who cannot show usage.

Related: [substrate cost as given or as revisable](substrate-cost-as-given-or-as-revisable.md) asks the same allocation question about costs a designer expects the hardware to absorb later.
