---
type: lesson
title: "A broadcast is not n messages: the mode of delivery, not the payload, is what a group can build on"
figure: vardi
works: [reasoning-about-knowledge]
axes: [parallelizability, verifiability, hardware-affinity]
subdomains: [distributed-systems-and-concurrency, software-engineering-and-architecture]
tags: [lesson]
---
# A broadcast is not n messages: the mode of delivery, not the payload, is what a group can build on

**Lesson:** Vardi walks a sequence of scenarios that deliver exactly the same sentence to exactly the same recipients and produce different group states, which is the cleanest way to see that content is not the whole of a message. Tell each participant privately and nothing collective is established. Tell each one privately while ensuring that all of them also learn that all of them were told — and still nothing collective is established. Only a single event whose occurrence is itself apparent to everyone it reaches does the job, and it does it in one step rather than by climbing the levels one at a time.

The reason is that the collapse depends on a self-referential property of the situation rather than on the accumulation of facts: everyone learns the fact and everyone learns that they are in a situation with that property, which is exactly what makes the infinite tower fold. This is why the effect is not obtainable by adding more rounds of "and I told them that I told you." Each such round buys one more level; the tower is infinite. Something structurally different is required, and simultaneity of apprehension is that something.

For anyone building distributed systems the operational reading is direct. A fan-out of unicasts is not a broadcast, however careful the retry logic; a shared log that all parties read is not equivalent to n private notifications, even with delivery receipts; a status page is not a synchronous announcement. If your protocol needs participants to act together on the basis of a shared premise, the premise has to arrive by a mechanism whose own occurrence is public, and that is an architectural requirement rather than a messaging detail. The corollary is a good warning: since genuinely simultaneous public apprehension is rare in real systems, protocols that quietly assume it are assuming something the medium does not provide.

**Source:** [Reasoning About Knowledge](../works/reasoning-about-knowledge.md) — chapter one's sequence of variants on the muddy children announcement: the father taking each child aside privately, then the version with hidden microphones where all children know that all children were told, and the conclusion that what matters is the public nature of the announcement, which puts the group in a situation such that all know both the fact and that they are in that situation; together with the observation that the collapse happens all at once rather than by deducing the levels one by one.
