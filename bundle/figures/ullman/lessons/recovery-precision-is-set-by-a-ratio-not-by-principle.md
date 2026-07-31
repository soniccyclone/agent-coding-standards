---
type: lesson
title: "How precisely you recover is set by a ratio, not by principle"
figure: ullman
works: [mining-of-massive-datasets]
axes: [verifiability, parallelizability, cognitive-load]
subdomains: [distributed-systems-and-concurrency, operating-systems-and-systems-programming]
tags: [lesson]
---
# How precisely you recover is set by a ratio, not by principle

**Lesson:** Fine-grained recovery — losing only the work that actually failed — feels obviously correct, and building it becomes a goal in itself. It is worth remembering what the goal actually was: that the expected time to finish in the presence of failures should not be much worse than the time to finish without them. That objective is satisfiable in many ways, and per-unit restart is only the most surgical of them. Throwing away everyone's progress back to the last saved global state satisfies it too, provided the amount of work you throw away is small compared to the amount you expect to complete between failures. When that holds, the crude mechanism is not a compromise; it is adequate, and it is enormously simpler to build and to reason about, because it never has to answer the hard question of which partial effects survived.

Once the objective is stated as a ratio, the interesting parameter falls out: how often to save. Saving costs real work every time, and saving rarely means losing more when a failure comes, so the interval has an interior optimum determined by two numbers you can actually estimate — the cost of taking a snapshot relative to doing the work, and the probability of a failure per unit of work. Neither number is a matter of taste, and neither is discoverable by thinking about the algorithm. This reframes a design argument that usually gets conducted on aesthetic grounds into an arithmetic one, and it tells you when the argument even matters: if failures are rare relative to the whole job, no recovery machinery earns its complexity, and if they are frequent relative to a snapshot, no snapshot interval saves you and the real problem is the failure rate.

The wider lesson is about how to evaluate any mechanism that exists to bound a bad case. Ask what quantity it is supposed to keep small, then check whether the cheap version already keeps it small enough at your operating point. Frequently it does, and the sophisticated version is being justified by the elegance of its guarantee rather than by any difference in the outcome. The corresponding danger is real too: an operating point can move. A recovery scheme sized for a hundred machines is a different proposition on ten thousand, because the failure rate scales with the fleet while the snapshot cost scales with the state, and the ratio that made the crude approach adequate may have quietly inverted.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the chapter on cluster programming systems, in its account of failure management in bulk-synchronous graph systems, which restarts the entire job from the most recent checkpoint and justifies this by the general condition that recovery time be much less than mean time between failures, together with the accompanying exercise on choosing the number of supersteps between checkpoints.
