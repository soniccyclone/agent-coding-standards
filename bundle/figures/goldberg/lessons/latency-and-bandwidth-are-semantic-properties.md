---
type: lesson
title: "Treat response time and bandwidth as properties of what can be thought, not as performance numbers to tune later"
figure: goldberg
works: [personal-dynamic-media]
axes: [hardware-affinity, cognitive-load]
subdomains: [programming-environments-and-object-systems, operating-systems-and-systems-programming]
tags: [lesson]
---
# Treat response time and bandwidth as properties of what can be thought, not as performance numbers to tune later

**Lesson:** Most engineering cultures file latency and throughput under optimization: get the behavior right, then make it fast. This work inverts that ordering by arguing that for a system a person thinks *through*, the delay between action and consequence is part of the system's meaning. The instrument analogy makes the point without needing measurements — an instrument that sounded a second after you played it would not be a slow instrument, it would be a different and largely useless one, because the tight loop between intent, act, and perception is the mechanism by which skill and exploration happen at all. The same holds for a medium of thought: if the feedback arrives after the thought has moved on, whole classes of work (adjusting an animation while watching it move, hearing a composition while writing it) are not merely inconvenient but unavailable.

Bandwidth gets the same treatment. The claim is that the sensory quality of a medium is inseparable from what it communicates, so a low-resolution channel does not deliver a degraded version of the same content — it delivers different, poorer content. The observation the authors report is telling in an unflattering way: the population with the *least* professional need, children, turned out to demand the most capability, because their existing media (real paint, real instruments, color television) had already set a floor that a shared, thin, wire-frame channel fell below. Adults tolerated the thin channel because they had learned to; that tolerance is an accommodation to a limitation, not evidence that the limitation was acceptable.

The consequence is architectural, and this work follows it all the way down to the hardware. If response and resolution are semantic requirements rather than nice-to-haves, then a design that shares one large machine among many people is not a cheaper version of the right answer — it is the wrong answer, because the property being sacrificed is the one that mattered. Given a choice between building a shared resource hundreds of times larger and giving each person a machine of their own, they took the second, and did so on grounds of what the medium had to feel like rather than on cost or utilization. Notice what this rules out: you cannot recover the property later by tuning, because the allocation decision has already fixed the ceiling.

A programmer who takes this seriously writes the interaction budget into the requirements next to the functional behavior, and treats a violation of it as a defect rather than a backlog item. It also changes how architectural options are compared — utilization efficiency, the metric that favors sharing, is measuring the machine's convenience rather than the user's thinking, and should lose to a latency requirement rather than be traded against it.

**Source:** [Personal Dynamic Media](../works/personal-dynamic-media.md) — the design-requirements discussion that sets out sensory-rate input and output and the absence of any perceptible gap between cause and effect as hard goals, then derives from them the rejection of timesharing in favor of a machine per person; reinforced by the later remark about what a thin shared channel actually communicates.
