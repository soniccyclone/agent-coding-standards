---
type: lesson
title: "Computation and the data it consumes have physical cost, and that cost belongs in the design, not in a footnote"
figure: booch
works: [the-promise-the-limits-and-the-beauty-of-software, the-future-of-software-engineering, building-the-enchanted-land]
axes: [hardware-affinity, parallelizability]
subdomains: [software-engineering-and-architecture, distributed-systems-and-concurrency]
tags: [lesson]
---
# Computation and the data it consumes have physical cost, and that cost belongs in the design, not in a footnote

**Lesson:** Software is usually reasoned about as if it were free of physics, and in most environments that fiction survives. It stops surviving at the edges, and the edges are instructive because they reveal what was always true. On a spacecraft, program size converts into qualified storage hardware, which converts into launch mass, so the amount of code becomes a budgeted resource like fuel. Executing that code dissipates heat into a vehicle with no atmosphere to shed it into, so a long computation may have to be scheduled around the craft's orientation. Software that has to agree with signals from fast-moving platforms far away must carry corrections for effects that most programmers file under theory rather than requirements. None of these are exotic corner cases; they are the general situation with the padding removed.

The version of this that now bites ordinary systems concerns moving data rather than moving code. Data has no weight but it does have inertia in the economic sense: once a source generates enough of it, transporting it to wherever the computation lives costs more than relocating the computation to the data. That single asymmetry, applied recursively, decides a large fraction of contemporary structure, and it explains why placement keeps oscillating between concentrated and dispersed rather than settling. Each swing is not fashion; it is the ratio between generation rate, link cost, and local compute capability crossing a threshold in one direction or the other. Whoever knows which side of that threshold their workload sits on can predict the right shape; whoever does not is guessing.

The same reasoning extends to how much precision a computation actually requires. Some workloads tolerate coarse arithmetic, and where they do, the hardware that serves them best looks nothing like a general-purpose processor, which then feeds back into structure: what runs where, what is worth specializing, what can be shrunk onto a small device once the expensive part is finished elsewhere. A programmer who thinks this way treats placement, precision, and data movement as first-class architectural decisions made early, rather than as tuning applied after a design that assumed transport and arithmetic were free.

**Source:** [The Promise, the Limits, and the Beauty of Software](../works/the-promise-the-limits-and-the-beauty-of-software.md) — the account of deep-space and satellite-navigation software where code size becomes mass, execution becomes heat, and relativistic correction becomes a functional requirement. Also [The Future of Software Engineering](../works/the-future-of-software-engineering.md) on data acquiring effective inertia once generation rates outpace the cost of shipping it, and [Building the Enchanted Land](../works/building-the-enchanted-land.md) on the swing between centralized training and local inference, the reduced precision many learned computations tolerate, and the specialized hardware that follows from it.
