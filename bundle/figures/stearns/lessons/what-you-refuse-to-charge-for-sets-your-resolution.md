---
type: lesson
title: "What you refuse to charge for decides how finely you can see"
figure: stearns
works: [its-time-to-reconsider-time, hierarchies-of-memory-limited-computations]
axes: [expressiveness, verifiability]
subdomains: [algorithms-and-complexity, foundations-of-computation]
tags: [lesson]
---
# What you refuse to charge for decides how finely you can see

**Lesson:** Every measure has a floor, and the floor is usually not a fact about the world but a consequence of billing yourself for resources you were handed for nothing. Charge a computation for the storage its input occupies and no computation can cost less than the input length, so the entire region below linear becomes a single undifferentiated blur — not because nothing interesting happens there, but because the accounting cannot see it. Stop charging for what is merely given and only charge for what the computation itself consumes, and that blur resolves into a rich structure extending down to logarithmic and even doubly logarithmic cost. One decision about the boundary of the budget, no change to the machinery, and a whole regime becomes discussable.

The general principle is that measurement is not just quantification; it is first a partition of the world into what is inside the budget and what is ambient. That partition is a modeling choice with expressive consequences, and it should be judged by the distinctions it makes available rather than by how completely it accounts for total resource use. Counting everything is more faithful in a trivial bookkeeping sense and strictly less informative, because a large fixed term shared by every case drowns the variable term that distinguishes them. The faithful-looking measure is the useless one.

So when a metric reports that everything across some range behaves identically, treat that as a hypothesis about the metric before accepting it as a fact about the subject. Ask what fixed overhead is being included in every reading, and whether that overhead is something the thing under study actually chose or something it was simply given. Separating the ambient from the incremental is the standard repair, and it tends to reveal not a small correction but an entire stratum of behavior that the old accounting had collapsed to a point. The corresponding warning applies to designing measures in the first place: whatever you decide to include as unavoidable becomes the limit of what you will ever be able to distinguish.

**Source:** [It's Time to Reconsider Time](../works/its-time-to-reconsider-time.md) — the paragraph on the later space-complexity work, where the model-level innovation of charging only for scratch storage and excluding the read-only input is credited with enabling sub-linear classes down to logarithmic and doubly logarithmic bounds. The same decision is made at its origin in [Hierarchies of Memory Limited Computations](../works/hierarchies-of-memory-limited-computations.md) — the introduction states that the input is held separate from the working storage precisely so that costs below linear become expressible, and the paper then exhibits concrete recognition schemes operating at doubly logarithmic cost.
