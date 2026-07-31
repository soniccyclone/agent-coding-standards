---
type: lesson
title: "Identical parts under an identical rule stay identical — diversity has to be seeded"
figure: ullman
works: [mining-of-massive-datasets]
axes: [expressiveness, verifiability]
subdomains: [algorithms-and-complexity, distributed-systems-and-concurrency]
tags: [lesson]
---
# Identical parts under an identical rule stay identical — diversity has to be seeded

**Lesson:** Provide several interchangeable components, start them in the same state, and drive them with the same rule and the same inputs, and they will remain in the same state forever. This is not a tendency, it is a theorem about the update rule: it is a function, so equal arguments give equal results at every step, and the equality is preserved by induction. The consequence is that a system built to gain something from having many components — coverage of different cases, different specialisations, different opinions — gains nothing at all, and the capacity you paid for behaves exactly like one component copied. Worse, everything looks fine. Nothing errors, the system produces plausible output, and the only symptom is a ceiling on quality that no amount of additional capacity moves.

The neutral-looking default is the trap. Setting every component to the same starting value — zero, or the same sensible constant — feels like the responsible choice, the one that introduces no arbitrary bias. It introduces the worst possible bias, which is a symmetry the dynamics cannot break. What you need instead is deliberate asymmetry at the outset: give the components different starting states, drawn at random, precisely because you have no principled reason to prefer any particular assignment of roles among them and only need them to be *different*. Randomness here is not a hedge against ignorance, it is the mechanism that makes specialisation possible.

The general check is cheap and worth making a habit: for any system with interchangeable parts, ask what distinguishes part number one from part number two, and follow the answer through the update rule. If the only distinguishing feature is the starting state, then the starting state must differ. If the parts are also fed different inputs, or the rule consults something part-specific, symmetry is already broken and you need nothing more. If neither is true, the redundancy is decorative.

This shows up well outside fitting procedures. Replicas that must elect a leader need something to break the tie or they retry in lockstep forever; back-off schedules with no jitter resynchronise the very collisions they were added to prevent; caches with identical expiry policies expire together and stampede. Each is the same phenomenon — a system that assumed variety would emerge from a process with no source of variety in it — and each is fixed the same way, by putting a small amount of independent randomness where the symmetry was.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the parameter-initialisation discussion in the gradient-descent section of the neural-nets chapter, which specifies drawing initial weights at random from a uniform or normal distribution and observes that initialising all weights to the same value would make every node in a layer behave identically, so the benefit of having different nodes recognise different features of the input would never be realised.
