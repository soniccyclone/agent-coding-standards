---
type: lesson
title: "Check whether your theory covers the region where the cost actually is"
figure: boehm
works: [software-engineering-1976]
axes: [verifiability]
subdomains: [software-engineering-and-architecture, foundations-of-computation]
tags: [lesson]
---
# Check whether your theory covers the region where the cost actually is

**Lesson:** A field's theory tends to grow where theory is easy to make, not where the difficulty is. Boehm's audit of his own discipline draws the line bluntly. The rigorous results available to him covered one region: detailed design and coding of systems-level programs, done by capable specialists, in a setting where economics can be ignored. Meanwhile the money and the failures lived in a different region: figuring out what to build, structuring it, testing it, and modifying it for years afterward, done by ordinary staff, under hard cost and schedule pressure. Two regions, and almost all the intellectual machinery pointed at the smaller one. His verdict is that a discipline whose foundations do not reach its own dominant cost centers has not yet earned the name it has given itself.

The mechanism behind this misalignment is not laziness, it is selection by tractability. The problems that admit clean formal treatment are the ones where inputs are well-defined, human judgment is absent, and the objective is a single crisp property. Every one of those conditions fails in the region where the cost is. So the field drifts toward the provable, and the drift is invisible from the inside because progress is real, publishable, and locally satisfying. Boehm's point is that the risk of working the harder region is higher and the payoff is much larger, and that solving it would feed back into neighboring engineering disciplines struggling with the same class of large-system problems.

The transferable habit is a periodic audit: take the place where your effort and your failures actually accumulate, and ask honestly what fraction of your tools, abstractions, and mental models address it. A type system that guarantees a property that has never broken for you, while the recurring outages come from unclear ownership of state across a boundary, is a well-built tool aimed away from the target. Coverage, not sophistication, is the metric.

A programmer who thinks this way keeps an honest inventory of where their own time and defects go, and treats a mismatch between that inventory and their toolkit as the thing to fix. They are also less impressed by rigor per se, asking first what region a result covers before asking how strong it is.

**Source:** [Software Engineering](../works/software-engineering-1976.md) — the concluding section and its side-by-side comparison with hardware engineering, which partitions the field into the region existing scientific principles cover and the region where the pressing problems live, then argues the field's reluctance to attack the second is both understandable and costly.
