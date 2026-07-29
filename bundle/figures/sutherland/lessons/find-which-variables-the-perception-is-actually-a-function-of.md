---
type: lesson
title: "Find which variables the result is actually a function of, and stop measuring the rest"
figure: sutherland
works: [a-head-mounted-three-dimensional-display]
axes: [cognitive-load, hardware-affinity, primitive-count]
subdomains: [programming-environments-and-object-systems, software-engineering-and-architecture]
tags: [lesson]
---
# Find which variables the result is actually a function of, and stop measuring the rest

A system that must convince a human of something is easy to over-build, because every physical cue seems mandatory. The corrective move is to ask, for each input you were planning to sense, whether the output you compute is genuinely a function of it. Sutherland's display had to produce a picture, and the picture's geometry depends on where the viewing optics sit, not on where the eyeballs behind them happen to be pointed. So eye rotation — the hardest quantity in the whole apparatus to acquire — drops out of the design entirely, not as a compromise but as a consequence. He also ranks the cues that remain: motion-coupled perspective change carries more of the illusion than binocular disparity does, so the motion path gets the custom hardware and the money.

The reasoning generalizes past graphics because the same trap appears wherever a program models something rich. You start listing everything true about the domain, then build machinery to observe all of it, and the cost lands on the parts that were never in the output's dependency set. Working the other direction — write down what the computed answer depends on, then sense exactly that — usually deletes whole subsystems. It also tells you where to spend: the dependencies are not equally weighted, and the one with the steepest influence deserves the expensive implementation while the others get whatever is cheap.

A programmer who has internalized this treats a requirements list as a set of hypotheses about dependency rather than a set of obligations. Before adding a sensor, a field, a configuration input, or a tracked piece of state, they trace whether any output actually varies with it. When something does not appear in that trace, its physical or conceptual reality is beside the point — it is not part of the system. And when several inputs do appear, they measure which one dominates before committing engineering to any of them, because uniform effort across unequal contributors is how a project runs out of budget on the parts nobody notices.

**Source:** [A Head-Mounted Three Dimensional Display](../works/a-head-mounted-three-dimensional-display.md) — the introduction, where Sutherland explains why eye rotation is deliberately not sensed and why kinetic depth outranks stereo presentation, and the closing results, where user response is used to check that ranking after the fact.
