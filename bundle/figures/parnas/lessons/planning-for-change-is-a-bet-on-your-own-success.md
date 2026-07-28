---
type: lesson
title: "Preparing for change is a prediction that you will succeed, and it will still not be enough"
figure: parnas
works: [software-aging]
axes: [cognitive-load, verifiability]
subdomains: [software-engineering-and-architecture]
tags: [lesson]
---
# Preparing for change is a prediction that you will succeed, and it will still not be enough

**Lesson:** The usual excuse for skipping the work of isolating likely changes is
that it is speculative — you cannot know what will be asked for, so why pay now
for flexibility you may never use. Parnas turns the bet around. The programs that
are never asked to change are the ones nobody cared enough about to ask. Demands
for modification are what success looks like from the inside. Declining to prepare
for them is therefore not a neutral deferral of cost; it is an implicit forecast
that the product will not matter, and it is a forecast that will be embarrassingly
falsified in exactly the cases you most wanted to win.

The second half of the argument cuts against over-confidence in the same
preparation. Isolating anticipated change works by predicting classes of change
and confining each to a small region. Prediction is the load-bearing step, and it
is done by people, imperfectly, years early. Over a long enough life the system
will be asked for something that violates the assumptions the partitioning was
built on, and at that point the structure does not bend, it breaks. This is why
Parnas insists decay is inevitable even for a team that does everything right:
not because the discipline is weak, but because it is grounded in foresight, and
foresight is finite. Anyone who thinks a sufficiently good initial decomposition
buys permanent immunity has mistaken a slowing measure for a cure.

Believing both halves changes what a plan looks like. You spend real effort up
front ranking which kinds of change are probable and confining the probable ones,
because you expect to succeed — and you simultaneously budget for scheduled
structural repair, because you expect the ranking to be partly wrong. Restructuring
becomes a normal, planned, recurring activity rather than a confession of failure,
and eventual replacement becomes something you provision for while the system is
still healthy rather than something that arrives as a crisis. The failure mode this
guards against is the one Parnas names as chronic: a difficulty that is serious but
neither sudden nor short-lived, mislabelled an emergency for decades, and therefore
never given the long-horizon treatment it actually needs.

**Source:** [Software Aging](../works/software-aging.md) — the "design for success"
argument in the preventive-medicine section, its deliberate qualification under
why aging is inevitable, and the later insistence on provisioning for replacement
rather than treating a decades-long problem as a recurring emergency.
