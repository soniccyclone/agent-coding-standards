---
type: lesson
title: "Quality is a balance among incompatible criteria, and what a delivery crunch destroys is the balancing"
figure: hoare
works: [the-emperors-old-clothes]
axes: [cognitive-load, hardware-affinity]
subdomains: [software-engineering-and-architecture]
tags: [lesson]
---
# Quality is a balance among incompatible criteria, and what a delivery crunch destroys is the balancing

**Lesson:** Treating quality as a single dial that gets turned up or down is the mistake that makes it invisible in a crisis. It is a collection of properties — correctness, robustness under abuse, compactness, speed, responsiveness, adaptability, comprehensibility to the next person, cost to construct, cost to change — and many of the pairs genuinely conflict, so no artifact maximizes them all and every real design is a chosen point in that space. The choice is specific to the project: what an operating system needs from that list differs from what a one-off analysis needs, and the two designers are not doing the same job badly, they are doing different jobs. Naming the criteria and stating which ones you are trading away is therefore part of the design, not commentary on it.

The failure mode is not that the criteria get ranked wrongly under pressure; it is that ranking stops happening at all. In a struggle to deliver anything, consideration of quality is the first casualty, because balancing is an activity with no artifact and no deadline attached, so it is the cheapest thing to skip and the last thing anyone notices was skipped. Afterwards the loss is hard to describe, which is why post-mortems of this kind of failure often list schedule, estimation and communication faults and never mention that nobody was weighing anything against anything.

The remedy is to write the list of criteria down before the pressure arrives, with the balance chosen for this project and the trades made explicit, so that under crunch you are consulting an existing decision rather than making one you have no time to make. This has a second use: an explicit list is what allows a team to distinguish a deliberate sacrifice from an accidental one, and to defend the sacrifice later. It also exposes a common self-deception, that a project failing on delivery is at least accumulating quality elsewhere. Usually it is accumulating nothing, because the same conditions that broke the schedule broke the weighing.

**Source:** [The Emperor's Old Clothes](../works/the-emperors-old-clothes.md) — the final section of the October 1965 inquest into the 503 Mark II failure, which records that in the struggle to deliver any software at all the first casualty was consideration of the quality of what was delivered, states that software quality is measured by a number of totally incompatible criteria that must be carefully balanced in the design and implementation of every program, and notes that the group only then drew up its list of criteria.
