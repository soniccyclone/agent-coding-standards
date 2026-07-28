---
type: lesson
title: "The spread of your call sites grades the abstraction"
figure: pike
works: [plan-9-from-bell-labs]
axes: [primitive-count, expressiveness, cognitive-load]
subdomains: [operating-systems-and-systems-programming, software-engineering-and-architecture]
tags: [lesson]
---
# The spread of your call sites grades the abstraction

Here is an empirical test for whether a parameterized mechanism was worth
building: look at how its callers actually parameterize it. This work applies
that test twice and gets opposite answers, which is what makes it instructive.
Process creation is offered as a single call taking a bit vector that says which
of the parent's resources — memory, descriptors, environment, namespace,
signals — are shared, copied, or made fresh. The stated evidence that this was
the right factoring is that almost no two call sites in the whole system pass
the same bits. The dimensions are genuinely independent in practice, so exposing
them separately buys real cases that a fixed menu of two process kinds could not
express at all.

The same paper's retrospective condemns another piece of flexibility by the same
standard: the dynamically reconfigurable pipeline used for network protocol
stacks permits modules to be composed at runtime, and the system never once
exploits it. The honest conclusion drawn is that a static structure would be
smaller and faster. Note that the mechanism was not stupid — it had been used
productively in an earlier system. It was simply flexibility this system did not
need, and unused flexibility is not neutral. It costs code, speed, and the
attention of everyone who has to understand why the indirection is there.

What makes the test good is that it needs no taste and no argument. Count the
distinct argument patterns at your call sites. If they cluster on two or three
combinations, you have written a parameterized thing where two or three named
things belonged, and the parameter is a way of pushing a decision onto every
caller forever. If they scatter, the axes you exposed are the real axes of the
problem and the generality is earning its keep. If nothing varies at all, delete
the parameter. Apply the count before shipping the abstraction if you can, and
after, honestly, when you can't — and be willing to publish the negative result
about your own design, as this work does.

**Source:** [Plan 9 from Bell Labs](../works/plan-9-from-bell-labs.md) — the parallel programming section's defense of a single resource-sharing process primitive over separate process and thread classes, read against the Discussion section's admission that the reconfigurable stream plumbing bought configurability the system never used.
