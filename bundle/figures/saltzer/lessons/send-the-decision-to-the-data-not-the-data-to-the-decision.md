---
type: lesson
title: "Send the decision to the data, not the data to the decision"
figure: saltzer
works: [traffic-control-in-a-multiplexed-computer-system]
axes: [expressiveness, cognitive-load, parallelizability]
subdomains: [operating-systems-and-systems-programming, software-engineering-and-architecture]
tags: [lesson]
---
# Send the decision to the data, not the data to the decision

**Lesson:** The reflex when a central component has to make a judgment about many
participants is to hoist every fact the judgment might need into a shared table.
That reflex is expensive in a way that does not show up in the code: each promoted
fact becomes something the whole system must be able to see, keep resident, keep
consistent, and lock. It also freezes the judgment, because adding one new input
next year means changing a structure that everything touches. The alternative is
to invert the movement — arrange for the deciding code to execute momentarily
inside the participant's own context, where the participant's private data is
already at hand, and to return only the decision.

What this buys is not only a smaller shared surface. Once the deciding code lives
in the participant's context rather than in one privileged place, different
participants can run different versions of it, and the system stops needing a
single policy that is a compromise across every workload it serves. A participant
with hard timing requirements and one buying the cheapest possible service can be
governed by genuinely different rules under the same mechanism, because the
mechanism only requires that whoever decides respects the shared invariants —
the ordering conventions of the common structures — not that they decide the same
way. It also makes replacement safe: a new version of the policy can be tried on
one participant while everything else continues under the old one, which is a very
different proposition from a flag-day change to a central module.

The distinction worth holding onto is between the conventions and the policy. The
conventions — the format and locking discipline of the shared structures, the one
routine that performs the actual handoff — must be common and must be provided by
the system, or the arrangement degenerates into participants that can help
themselves to whatever they like. The policy on top of them can be plural. A
programmer who believes this looks at every field of a global structure and asks
whether it is there because everyone needs it or because one decision needed it,
and prefers moving that decision to leaving the field.

**Source:** [Traffic Control in a Multiplexed Computer System](../works/traffic-control-in-a-multiplexed-computer-system.md) — the "each process schedules itself" arrangement in chapter three, where the priority computation runs inside the address space of the process being made runnable, and the distributed-supervisor discussion in chapter five that draws out its consequences for heterogeneous policy and live replacement.
