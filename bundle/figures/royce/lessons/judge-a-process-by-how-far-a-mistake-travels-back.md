---
type: lesson
title: "Judge a structure by how far a mistake has to travel back"
figure: royce
works: [managing-the-development-of-large-software-systems]
axes: [cognitive-load, verifiability]
subdomains: [software-engineering-and-architecture]
tags: [lesson]
---
# Judge a structure by how far a mistake has to travel back

**Lesson:** Royce's phased scheme rests on one assumption that he states openly rather than smuggling in: correction is local. Each step is expected to iterate with the steps immediately adjacent to it and rarely with distant ones. That locality, not the ordering itself, is where the value sits. If a discovery only ever pushes you one step back, there is always a recent, consistent baseline to return to, and almost all completed work survives the correction. The ordering of activities is incidental; the reach of the feedback is the property doing the work.

His diagnosis of failure is the same claim negated. When the first execution comes at the end, a discovery there can invalidate the requirements that justified every decision in between, so the nearest consistent state is the origin and the intervening work is not salvageable. He puts a figure on what that costs, roughly a doubling of schedule or budget. The failure mode is not that mistakes happened, it is that the structure placed the detector for an entire class of mistakes as far as possible from where those mistakes were made.

The generalization reaches well past project methodology. Any layered arrangement, a build pipeline, a module stack, a type discipline, a deployment path, can be characterized by the distance between where a class of error is introduced and where it becomes visible, and by how much intervening work its correction destroys. A structure where errors surface one layer from their origin is cheap to be wrong in, which means it is cheap to explore in. A structure that only reveals a class of error at the far end is expensive to be wrong in no matter how orderly its layers look drawn on a page.

So the design question stops being "what is the right sequence of activities" and becomes "for each class of mistake I can expect to make, where does it become visible, and what does its correction cost me." A programmer who thinks this way spends effort shortening detection distance rather than on the hope of not making the mistake: fast local checks over end-to-end ones, invariants asserted where state is created rather than where it is finally consumed, boundaries drawn so that a wrong guess about one side does not propagate into the other.

**Source:** [Managing the Development of Large Software Systems](../works/managing-the-development-of-large-software-systems.md) — the contrast between the hoped-for iteration confined to successive phases and the actual case where iteration reaches back across the whole sequence, including the estimate of what that reach costs.
