---
type: lesson
title: "An update rule that can only demote needs a separate discovery path"
figure: ullman
works: [mining-of-massive-datasets]
axes: [expressiveness, cognitive-load, verifiability]
subdomains: [distributed-systems-and-concurrency, software-engineering-and-architecture]
tags: [lesson]
---
# An update rule that can only demote needs a separate discovery path

**Lesson:** Many incremental maintenance schemes are structurally one-directional without anyone noticing. They track a set of currently-interesting things, update those things' standing on each new observation, and drop anything whose standing falls below a bar. That machinery is complete for removal and incapable of addition, because a candidate not already being tracked accumulates no evidence, and a single observation cannot lift an untracked thing over a bar set well above what one observation contributes. The set can therefore only shrink. Left alone, such a system converges to emptiness while appearing to be maintaining itself, and the symptom — gradually going stale — looks like a tuning problem rather than a missing component.

Once you see the asymmetry, the fix follows directly and should be designed in from the start rather than bolted on: promotion is a different mechanism from maintenance, with a different trigger and a different cost. The usual shape is a periodic batch that reconsiders the full population from scratch and injects newly qualifying candidates into the tracked set with an appropriate starting standing. Getting that starting value right is its own small problem, since a new entrant given the minimum will be dropped immediately and one given too much will outlive its evidence; the honest approach is to convert its batch-measured strength into the incremental scheme's units so that it enters where it would have been had it been tracked all along.

There is a cheaper partial alternative worth knowing, which is to admit candidates speculatively rather than by full recomputation, but to be selective about which ones. Admitting everything is impossible when the candidate space is combinatorial, and admitting at random wastes almost all of the tracking budget. Admitting the immediate neighbours of things already qualifying is the disciplined middle: it costs little, it cannot miss anything that will eventually qualify if the qualifying property is monotone, and it lets the tracked set grow outward one step at a time as the evidence arrives. That converts discovery from an all-or-nothing recomputation into a slow crawl that the maintenance loop itself performs.

The general check to run on any incremental system: for each direction a tracked value can move, name the mechanism that moves it. If one direction has no mechanism, the system is a decay process with extra steps, and the missing mechanism is not an optimisation to add later — it is the half of the design that makes the other half meaningful.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the stream sections of the frequent-itemsets chapter, which note that a decaying-window score cannot be started above the contribution of a single arrival, gate the creation of new scores on all immediate subsets already being scored, and state plainly that adding genuinely new candidates requires running a separate batch computation over a fresh sample.
