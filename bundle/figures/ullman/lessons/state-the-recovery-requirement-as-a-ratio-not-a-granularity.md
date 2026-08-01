---
type: lesson
title: "State the recovery requirement as a ratio, not as a granularity"
figure: ullman
works: [mining-of-massive-datasets]
axes: [verifiability, parallelizability, cognitive-load]
subdomains: [distributed-systems-and-concurrency, software-engineering-and-architecture]
tags: [lesson]
---
# State the recovery requirement as a ratio, not as a granularity

**Lesson:** Sophisticated failure handling tends to be justified by describing the mechanism — we restart only the unit that failed, nothing else redoes its work — and that framing quietly converts a means into an end. Restated as a requirement, what anyone actually wants is that a run in the presence of failures does not take much longer than a run without them. Fine-grained restart is one way to get that. It is not the only way, and once the requirement is written as a relationship between two times rather than as a property of the restart unit, the design space opens: any scheme qualifies as long as the time spent recovering is small compared with the time between failures.

That reframing licenses mechanisms that look embarrassingly crude. Snapshotting the entire computation periodically and, on any single failure, rolling the whole thing back to the last snapshot throws away work at every healthy participant — an appalling waste under the granularity framing, and perfectly adequate under the ratio framing, provided the snapshot interval is short enough that a failure is unlikely within one interval. The mechanism is simpler by an order of magnitude, it works for computations whose shape rules out unit-level restart, and it comes with an explicit tuning knob. The knob is where the real engineering sits: too frequent and you pay snapshot cost continuously, too rare and the expected redone work grows, and the optimum is a function of the snapshot cost and the failure rate, both of which are measurable.

The habit generalises past fault tolerance to any requirement expressed as a mechanism. Someone asks for per-record retries, or exactly-once delivery, or incremental rebuilds; underneath is usually a ratio — recovery time against failure interval, error rate against tolerance, rebuild time against change frequency. Extract the ratio and you can compare mechanisms that are not otherwise comparable, and you gain the option of satisfying the requirement by moving the other term: making the run shorter reduces the chance of being interrupted at all, so speed is a fault-tolerance strategy and not merely a performance one. Arguing about mechanisms without the ratio in hand produces the familiar outcome where the elaborate scheme wins on principle and the simple one would have met the requirement.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — chapter 2's discussion of failure management in bulk-synchronous graph systems, which restarts the whole job from the most recent checkpoint and defends this by noting that the reason for restarting only failed tasks is to keep expected completion time under failures close to failure-free time, a property any scheme has so long as recovery time is much less than mean time between failures, so it suffices to checkpoint often enough that failure within an interval is improbable.
