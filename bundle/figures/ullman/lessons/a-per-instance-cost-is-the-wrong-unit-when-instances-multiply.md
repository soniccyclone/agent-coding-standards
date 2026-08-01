---
type: lesson
title: "A per-instance cost is the wrong unit when instances multiply"
figure: ullman
works: [mining-of-massive-datasets]
axes: [hardware-affinity, parallelizability, cognitive-load]
subdomains: [distributed-systems-and-concurrency, operating-systems-and-systems-programming]
tags: [lesson]
---
# A per-instance cost is the wrong unit when instances multiply

**Lesson:** The cost figure you can compute early is almost always the per-instance one, and the cost figure that decides the design is almost always that number times a multiplier nobody wrote down. A sensor reporting a few times a second produces a trickle you could keep in memory for years; the same sensor deployed densely enough to be scientifically interesting produces terabytes a day. A summary structure needing one integer per hash function lets you use absurdly many hash functions for one stream and forces you to ration them across a thousand streams. A per-item popularity counter is fine for the thousands of films in circulation and hopeless for a catalogue of everything sold online. In each case the algorithm is unchanged, the per-instance analysis is correct, and the conclusion drawn from it is wrong.

What makes this trap reliable rather than occasional is that the multiplier is usually the cheapest thing in the system to increase. Deploying more sensors, onboarding more tenants, tracking more entities, splitting one stream into per-customer streams — these are business decisions that require no engineering review and produce no design document, while the resource they multiply was budgeted once by someone reasoning about a single case. So the growth arrives without a moment at which anyone reconsiders the method. The defence is to write the resource expression with the multiplier in it from the start, even when the multiplier is one, because a formula with a variable in it invites the question of how large the variable gets and a formula without one does not.

The consequence worth internalising is that the crossover is qualitative, not gradual. Below it, the exact method — keep every element, count every entity, store the whole window — is not merely adequate but strictly better: simpler, exactly correct, easier to test. Above it the exact method is not slow, it is impossible, and every candidate replacement gives up exactness in a different direction. This means the multiplier is not a tuning parameter but a selector between families of designs, and it deserves to be estimated before the family is chosen rather than after. Estimating it badly by an order of magnitude is survivable; not estimating it at all means picking a family by accident.

The habit that follows is small and worth making automatic. For any resource figure you produce, name the unit it is per — per stream, per tenant, per shard, per request — and immediately name the count of that unit at the scale you expect to be operating at in a year. If the product exceeds what you have, you have learned something important while it is still cheap to act on. If it does not, you have learned that the simple exact method is the right one, which is a genuine result and the more common of the two.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — chapter 4's escalation of the ocean-sensor example from a stream storable forever to terabytes a day once a million sensors are deployed, together with its repeated observation that main memory constrains the number of hash functions only when many streams are processed at once, and that per-item counting works for films but not for a large product catalogue.
