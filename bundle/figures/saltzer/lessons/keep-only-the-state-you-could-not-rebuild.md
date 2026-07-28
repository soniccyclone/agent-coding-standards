---
type: lesson
title: "Keep only the state you could not rebuild"
figure: saltzer
works: [traffic-control-in-a-multiplexed-computer-system]
axes: [cognitive-load, hardware-affinity, primitive-count]
subdomains: [operating-systems-and-systems-programming, software-engineering-and-architecture]
tags: [lesson]
---
# Keep only the state you could not rebuild

**Lesson:** Go through every piece of context your system holds on behalf of a
dormant participant and ask, one item at a time, whether it could be regenerated
on demand instead of retained. Most of it can. A table of pointers that is
identical for every participant is a copy of a template. A mapping that can be
looked up again is a cache, not a fact. What cannot be regenerated is the small
residue that identifies the participant and tells a recovery path where to start
looking — and that residue is the only thing that has to be resident.

The argument for doing this item-by-item rather than in bulk is that the answer
differs per item, and the interesting engineering lives in the exceptions. A
reconstruction path can only use mechanisms that do not themselves depend on the
state being reconstructed, so the audit forces you to trace the bootstrap
sequence honestly: the fault handler that refills a mapping cannot itself fault
on the mapping it is refilling, and the routine that saves context in order to
wait cannot need the very context it is trying to fetch. Those circularities are
where a naive "just page it all out" design deadlocks. Resolving them takes real
structure — a scratch context that exists only for the duration of the pull-in,
a bootstrap module small enough to run against nothing, an ordering rule that
forbids recursive faults so the depth of the recovery path is bounded by
construction rather than by hope.

The payoff is that a ceiling turns into a non-issue. Once the resting cost of a
dormant participant is genuinely zero, the number your system can hold is bounded
by cheap storage rather than by expensive memory, and capacity planning stops
being about population and starts being about concurrent activity — which is the
quantity that was actually doing the work all along. A programmer who believes
this stops sizing systems by how many things exist, designs an explicit revival
path for anything expensive, and treats every long-lived resident structure as a
claim that must be defended: either it cannot be recreated, or it is on the
critical path of recreating something else, or it should not be resident.

**Source:** [Traffic Control in a Multiplexed Computer System](../works/traffic-control-in-a-multiplexed-computer-system.md) — chapter four's item-by-item examination of what a running process must have in memory versus a merely ready or blocked one, including the circularity that arises when the context needed to wait is itself the thing being fetched, and the resulting distinction between loaded, active, and inactive.
