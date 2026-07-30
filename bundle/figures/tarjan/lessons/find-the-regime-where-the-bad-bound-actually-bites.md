---
type: lesson
title: "Find the regime where the bad bound actually bites, because outside it the cheap analysis holds"
figure: tarjan
works: [efficiency-of-a-good-but-not-linear-set-union-algorithm]
axes: [hardware-affinity, cognitive-load]
subdomains: [algorithms-and-complexity]
tags: [lesson]
---
# Find the regime where the bad bound actually bites, because outside it the cheap analysis holds

**Lesson:** The headline result is a superlinear worst case, and the natural reading is that the structure is superlinear and you should worry about it. Tarjan immediately narrows that. Because the bound is expressed in two independently varying quantities — how many groups get merged and how many lookups are performed — you can ask what happens when they are far apart, and the answer is that the extra factor disappears: if either count sufficiently dominates the other, the total is plainly linear. The pathology exists only when the two counts are of comparable size, and the matching lower bound is proved precisely in that regime. So the honest summary is not "this is superlinear" but "this is linear except in a specific balance of the workload, where it is superlinear by a factor almost nobody will measure."

Getting into the habit of asking that question changes how worst-case results inform decisions. A bound is a function of parameters, and a bound's bad behaviour usually lives in some region of parameter space rather than everywhere. Locating the region and comparing it against where your actual workload sits is often the entire decision, and it takes far less effort than either improving the algorithm or replacing it. The failure this prevents is common in both directions: engineers who reject a good structure on the strength of a worst case their workload can never reach, and engineers who adopt one whose worst case is exactly the regime their traffic occupies. Neither can tell which they are, because neither did the substitution.

There is a corollary about how to state bounds so this reasoning is possible at all. If the analysis had collapsed the two counts into a single notion of input size, the regime structure would have been invisible — you cannot ask what happens when the counts diverge if the notation has already assumed they don't. Keeping distinct parameters distinct through the analysis, resisting the urge to simplify by assuming they are proportional, is what preserves the ability to answer the question a practitioner actually has. Simplifications made for the writer's convenience destroy exactly the information the reader needs to apply the result.

**Source:** [Efficiency of a Good But Not Linear Set Union Algorithm](../works/efficiency-of-a-good-but-not-linear-set-union-algorithm.md) — the bound stated in terms of separate find and union counts, the observation following it that when one count dominates the other by a sufficient factor the total is linear, the conclusion that the worst case occurs when the two counts are approximately equal, and the lower-bound section proving tightness in precisely that balanced regime.
