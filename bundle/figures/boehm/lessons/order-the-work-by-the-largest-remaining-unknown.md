---
type: lesson
title: "Let the largest remaining unknown choose what you build next"
figure: boehm
works: [a-spiral-model-of-software-development-and-enhancement]
axes: [verifiability, cognitive-load]
subdomains: [software-engineering-and-architecture]
tags: [lesson]
---
# Let the largest remaining unknown choose what you build next

**Lesson:** Any way of organizing work is answering two questions over and over: what do we do next, and how long do we keep doing it. Most answers are inherited as a fixed sequence, which quietly assumes that the order of activities is a property of the activity list rather than of the particular thing being built. Boehm's reframing is that the order should be derived, each time, from where the ignorance currently sits. If nobody knows whether the interaction model is acceptable to its users, then the next artifact should be whatever cheaply produces evidence about that; if nobody knows whether the chosen component can carry the load, the next artifact is a measurement. The activity that resolves the most dangerous uncertainty per unit of cost wins, and the same list of activities can therefore come out in radically different orders on two projects that look superficially alike.

This works because uncertainty, not code volume, is what actually kills a build. Committing to structure while a decision is still unresolved means either building on a guess or building machinery whose only purpose is to hedge. Choosing the next step by residual unknowns converts the whole effort into a chain of small refutable claims, each one narrowing the space in which a catastrophic surprise can still be hiding. The corollary is one people resist: the top-level claim is itself refutable. The premise is that some situation would be improved by building this thing, and every cycle tests that premise. If the premise fails, stopping is a correct outcome of the process, not a failure of it. That single move turns cancellation from an embarrassment into a result the method is designed to produce.

The other half is that each cycle has to end somewhere visible. Boehm closes every pass with a review whose purpose is not inspection of the artifacts but confirmation that the parties who have to live with the next commitment actually agree to it. Otherwise an iterative process degenerates into perpetual motion, since there is always another unknown worth chasing.

A programmer who works this way stops asking "which phase are we in" and starts asking "what is the most expensive thing we are currently guessing about, and what is the cheapest experiment that would settle it." They build spikes, benchmarks, and throwaway prototypes without apology, because those are instruments rather than deliverables. They treat an unexamined assumption sitting in the plan as more alarming than an unwritten module, and they are willing to argue for killing work they have already invested in when the evidence comes back negative.

**Source:** [A Spiral Model of Software Development and Enhancement](../works/a-spiral-model-of-software-development-and-enhancement.md) — the description of a single cycle (objectives, alternatives, constraints, then risk evaluation choosing the next step) together with the discussion of how the process starts and terminates, where the whole effort is cast as a hypothesis under continuing test and each cycle ends in a commitment review.
