---
type: lesson
title: "Every reliability guarantee is relative to a failure model; state it, and know what weakening it costs"
figure: lamport
works: [the-byzantine-generals-problem]
axes: [verifiability, parallelizability]
subdomains: [distributed-systems-and-concurrency]
tags: [lesson]
---

# Every reliability guarantee is relative to a failure model; state it, and know what weakening it costs

**Lesson:** No system is "fault tolerant" in the absolute; it tolerates the faults its designers imagined. The failure mode that breaks most reliability schemes is not a component stopping but a component continuing wrongly — sending conflicting information to different observers. Majority voting over replicas, the standard reflex, silently assumes all replicas saw the same input; one flaky source feeding different values to different voters defeats it, and no wiring trick escapes this, because a marginal signal can genuinely read differently at different receivers. If you cannot constrain how a component misbehaves, the only honest model is arbitrary misbehavior, and coping with it requires an actual agreement protocol among the replicas, not more redundancy.

The model, once explicit, has an exact price schedule. Arbitrary failure with plain messages requires more than two-thirds of components honest and message chains as long as the number of faults tolerated; add one assumption — messages that cannot be undetectably altered — and the two-thirds bound evaporates for any number of faults. Assume further that failed components only ever go silent, and everything gets cheaper still. Each strengthening of the failure model buys a real reduction in replication and communication cost, which means each such assumption is a load-bearing engineering decision that should be written down and justified, not an ambient hope. The same relativity applies to impossibility: what cannot be done is also defined by the model, so proving the impossibility bounds tells you exactly which assumption you must buy to escape them.

Two habits follow. First, for any reliable system, ask what its correctness argument assumes about how parts fail, and what happens when a part fails outside that set; "crash only" is an assumption, not a fact of nature. Second, be suspicious of plausible informal arguments in this territory — this is a domain where convincing hand-waved proofs of false statements are unusually easy to produce, which is itself a reason the models and bounds must be formal.

**Source:** [The Byzantine Generals Problem](../works/the-byzantine-generals-problem.md) — the framing of conflicting-information failure, the 3m+1 impossibility argument and its warning about nonrigorous reasoning, the signed-messages algorithm showing how one added assumption changes the bound, and the reliable-systems section dismantling hardware end-runs around agreement.
