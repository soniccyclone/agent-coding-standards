---
type: lesson
title: "Rank candidate methods by how they grow, then cut what still will not fit"
figure: sutherland
works: [a-head-mounted-three-dimensional-display]
axes: [hardware-affinity, cognitive-load, verifiability]
subdomains: [algorithms-and-complexity, software-engineering-and-architecture]
tags: [lesson]
---
# Rank candidate methods by how they grow, then cut what still will not fit

When Sutherland surveyed the published approaches to the hardest subproblem his display faced, he sorted them by a single criterion that had nothing to do with the quality of the pictures they produced: the rate at which their cost climbed as the scene got more complicated. Most of the field's methods worked, and worked well on the examples their authors chose. He set nearly all of them aside anyway, because their cost rose roughly with the square of complexity, which makes them permanently unsuitable for a system that must finish before the next refresh no matter what the scene contains. Only the two whose growth left room for a real-time future stayed on the shortlist. Present output quality is a snapshot; the growth rate is the thing that decides whether a method has a future in your system at all.

That criterion earns its authority from a structural fact: a demonstration is always run at a size someone chose, while a shipped system runs at whatever size reality hands it. Any comparison done at the demonstration size measures the constant factors and hides the exponent, and the exponent is what determines the outcome at the size that matters. Ranking by growth also has the pleasant property of being cheap to establish and hard to fool — you can often reason it out from the shape of the method before writing a line of code, whereas ranking by observed quality requires implementations you do not yet have.

The second half of the move is more uncomfortable and matters more. Having narrowed to the plausible candidates, Sutherland concluded that none of them was within his reach yet, said so plainly, and shipped the version of the system that omitted the capability entirely — objects you can see through, rather than objects that occlude one another. He did not ship a version that attempted the hard thing and missed its deadline sometimes, and he did not let the unsolved subproblem hold the rest of the system hostage. The unsolved part was named, bounded, and excluded, which left everything else free to be finished and used.

A programmer with this instinct evaluates candidate designs by asking how the cost behaves as the input grows before asking how good the results look, and treats a quadratic method as disqualified in a latency-bounded path rather than as a starting point to optimize. Just as importantly, they are willing to cut a capability out of scope, honestly and visibly, when its best available implementation does not fit the system's real constraints. An excluded feature is a known limitation. A feature that is present but sometimes blows the deadline is an unknown one, and it contaminates confidence in everything shipped beside it.

**Source:** [A Head-Mounted Three Dimensional Display](../works/a-head-mounted-three-dimensional-display.md) — the introduction's survey of occlusion methods, where scaling behavior rather than picture quality decides the shortlist, followed by the explicit decision to display transparent line figures instead.
