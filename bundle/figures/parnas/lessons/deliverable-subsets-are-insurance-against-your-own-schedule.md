---
type: lesson
title: "A structure of deliverable subsets is insurance against your own schedule"
figure: parnas
works: [designing-software-for-ease-of-extension-and-contraction]
axes: [cognitive-load, verifiability]
subdomains: [software-engineering-and-architecture]
tags: [lesson]
---
# A structure of deliverable subsets is insurance against your own schedule

The case for building a system as a graded series of runnable subsets is normally made in terms of customers: different buyers want different amounts, so make the amounts separable. Parnas adds a second justification that has nothing to do with variety in the market and is probably the more universally applicable of the two. Schedules slip. A project that is late has to decide what to hand over, and the answer depends entirely on a structural property fixed long before anyone knew there would be a delay. If the parts were ordered so that truncating the top leaves something coherent, lateness degrades into a smaller delivery. If they were not, there is nothing to hand over at all, and the complaint that follows is the familiar one: we tried to ship a reduced version and discovered that nothing worked until everything worked.

Notice what this does to the argument about whether the flexibility is worth paying for. The usual objection to designing for subsets is that you are speculating about future customers, and speculation can be wrong. Schedule risk is not speculation. It is a near-certainty on any project of size, so the structure that hedges it is being bought against a risk you already know you carry. That reframes subset structure from an optional generosity toward hypothetical users into ordinary engineering prudence, of the same kind as keeping a system buildable and tested continuously.

The timing consequence is the part that bites. This property cannot be added when it is needed, because by the time you need it you are late, and the work of untangling a system into deliverable layers is precisely the work you have no time for. Flexibility of this kind is not something a project can decide about halfway through; the decision is made, implicitly and irreversibly, in the first structural choices. Which means the question worth asking at the start of a project is not only what the system must do, but what you would be able to give the customer if you ran out of time — and if the honest answer is nothing, that is a design defect visible on day one rather than a scheduling problem discovered on the last day.

**Source:** [Designing Software for Ease of Extension and Contraction](../works/designing-software-for-ease-of-extension-and-contraction.md) — the summation's first point, that identifying usable subsets belongs to the preliminaries of design, that flexibility cannot be an afterthought, and that subsetability provides a fail-soft response to schedule slippage, read against the opening complaint about an early release whose intended subset would not work until everything worked.
