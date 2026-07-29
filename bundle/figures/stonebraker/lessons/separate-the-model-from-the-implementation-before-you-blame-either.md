---
type: lesson
title: "Separate the model from the implementation before you blame either"
figure: stonebraker
works: [mapreduce-and-parallel-dbmss-friends-or-foes]
axes: [parallelizability, hardware-affinity, verifiability]
subdomains: [databases-and-data-management, distributed-systems-and-concurrency]
tags: [lesson]
---
# Separate the model from the implementation before you blame either

A measured gap between two systems is evidence about two systems, not about the two ideas they embody. Most of what you find when you take a gap apart turns out to be contingent: a default storage format that forces every pass to re-decode text, a compression codec chosen without regard to whether decode cost eats the I/O it saves, a decision to materialize intermediate results rather than stream them. None of those are entailed by the programming model on either side; they are choices someone made and someone else could unmake. So the honest form of a comparison result is a sorted list — here is what the other side could fix by next release, and here is the much shorter list of differences it cannot fix without giving up something else it deliberately bought.

That shorter list is the only part with any predictive value, and you find it by asking what each difference is load-bearing for. Pulling data through local materialized structures instead of pushing it downstream is slower, but it is also exactly what makes fine-grained restart possible; scheduling work one block at a time costs more than following a precomputed plan, but it is also what lets the system react to a slow node. Those differences will still be there in ten years because deleting them would delete a property the designers wanted. The ones with no such backing will evaporate, and a critique built on them expires quietly and makes you look like you were arguing about the wrong thing.

The discipline this imposes on the arguer is uncomfortable and non-negotiable: you owe the rival design more tuning effort than you gave your own. If you have not taken the opposing community's suggestions, spent more hours on their configuration than on yours, and published the harness so someone can dispute the numbers, the gap you measured is a gap in your familiarity, not in the systems. A programmer who internalizes this stops reading benchmark results as verdicts on paradigms and starts reading them as a list of open engineering tickets, most of which belong to whichever side happened to be less carefully deployed.

**Source:** [MapReduce and Parallel DBMSs: Friends or Foes?](../works/mapreduce-and-parallel-dbmss-friends-or-foes.md) — the architectural-differences discussion, which opens by attributing the measured gap to implementation choices rather than to the two models, then walks each cause and singles out the few that are structurally tied to the fault-tolerance design.
