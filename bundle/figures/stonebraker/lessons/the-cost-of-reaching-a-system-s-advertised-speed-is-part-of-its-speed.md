---
type: lesson
title: "The cost of reaching a system's advertised speed is part of its speed"
figure: stonebraker
works: [mapreduce-and-parallel-dbmss-friends-or-foes]
axes: [cognitive-load, verifiability]
subdomains: [software-engineering-and-architecture, databases-and-data-management]
tags: [lesson]
---
# The cost of reaching a system's advertised speed is part of its speed

A system that is fast only after an expert configures it has two performance numbers, and the one that matters to most users is the bad one. When getting a query to finish in minutes instead of days requires a support engineer from the vendor, the honest description is not "fast system, poor documentation" — it is a system whose real throughput, integrated over everyone who tries to use it, is dominated by the tuning surface they cannot navigate. The winning alternative in that situation may be architecturally slower and still be the better tool, because it produces answers on the first day rather than after an engagement.

The trap is that the people who build a system are the worst possible judges of this. They tune it reflexively and cannot feel the tuning parameters they set correctly by habit; every measurement they take is post-expertise. A knob is only a knob to someone who knows which way to turn it, and to everyone else it is a landmine that makes the system look broken. This is why the number of settings that must be right before anything works is a first-class design property, not a documentation problem to be deferred. Defaults that produce a working system are a feature with a larger effect on aggregate delivered performance than most optimizations, and pushing that work onto a support channel is a way of hiding the cost rather than paying it.

Taking this seriously means conceding it about your own work, in public, to the people you are otherwise arguing against. The generous version of a technical fight names what the other side is actually better at — here, standing up and returning an answer without ceremony — and treats it as a specification for what your side has to fix, not as a soft advantage to be waved away because the deep architecture is sounder. A programmer who believes this measures from a clean machine, counts the steps before first output, and treats "you configured it wrong" as a defect report against the design rather than against the user.

**Source:** [MapReduce and Parallel DBMSs: Friends or Foes?](../works/mapreduce-and-parallel-dbmss-friends-or-foes.md) — the concessions in the quick-and-dirty-analysis and limited-budget sections, and the closing list of what database systems should take from the other camp, where installability and working defaults are named as the deficiency.
