---
type: lesson
title: "Size a change by how much re-understanding it forces, not by how much effort it takes to build"
figure: lehman
works: [on-understanding-laws-evolution-and-conservation-in-the-large-program-life-cycle]
axes: [cognitive-load]
subdomains: [software-engineering-and-architecture]
tags: [lesson]
---
# Size a change by how much re-understanding it forces, not by how much effort it takes to build

**Lesson:** After a system has been stable for a while, everyone touching it — implementers, testers, salespeople, users — has settled into a working familiarity where the thing can be handled without deliberate thought. Its felt complexity has dropped near zero. A batch of change destroys that state for everybody at once, including the people who wrote the change, because each of them worked on only a slice and now has to understand the whole again. The hidden cost of a release is therefore not the cost of building it but the cost of the collective relearning it forces, and that cost is what actually limits how much change a system can take at a time.

The relationship is not linear, and the reason is combinatorial rather than psychological. Changes shipped together must each be understood in the context of all the others, plus the unchanged remainder, plus the system's past and expected uses. Effort to absorb a release therefore grows faster than the release's size — at least quadratically, on the argument here — which produces a threshold rather than a gradient. Below the threshold, integration is unremarkable and familiarity is restored without visible disturbance. Around it, expect slippage, quality problems, and a follow-on release whose only job is cleaning up. Well above it, expect something closer to breakdown, including a system splitting apart under its own weight. And there is no escaping the relearning by testing harder before shipping: until the whole changed system is genuinely in use, some interactions simply have not happened yet, so full exposure is a post-release event by definition.

The capacity that sets the threshold belongs to the average participant, not the best. The strong absorb quickly and pull ahead; the weak fall behind, and their difficulty leaks outward as delays, misread documentation, faults reported that do not exist, and repairs that damage the system, which other people then have to undo. Because the aggregate cost tracks average absorptive capacity, and because hiring tends to reproduce the existing composition of the group, the ceiling cannot be lifted by acquiring a few exceptional people. It moves only if the structure, methodology, and practices that determine how hard the system is to re-understand are changed.

There is a trap on the easy side of the threshold, too. When a modest release goes smoothly, the smoothness itself invites a more ambitious next one, and the pressure for visible productivity pushes releases up toward the threshold until one goes badly. A programmer who understands this stops treating batch size as an ambition to be maximized and starts treating it as a quantity to be held under a measured limit — and reads a proposal calling for several times the usual content as a request to spend the recovery cost later rather than the splitting cost now.

**Source:** [On Understanding Laws, Evolution, and Conservation in the Large-Program Life Cycle](../works/on-understanding-laws-evolution-and-conservation-in-the-large-program-life-cycle.md) — the extended interpretation of the fifth law: the loss and restoration of familiarity around a release, the nonlinear difficulty curve with its threshold region, and the argument that outcomes depend on average rather than exceptional absorptive ability.
