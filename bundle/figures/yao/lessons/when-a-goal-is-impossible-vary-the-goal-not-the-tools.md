---
type: lesson
title: "When a goal is proved unreachable, vary the goal's shape rather than reaching for stronger tools"
figure: yao
works: [protocols-for-secure-computations]
axes: [expressiveness, verifiability]
subdomains: [distributed-systems-and-concurrency, algorithms-and-complexity]
tags: [lesson]
---
# When a goal is proved unreachable, vary the goal's shape rather than reaching for stronger tools

**Lesson:** An impossibility result reads like a wall, and the reflex it provokes is to look for a bigger hammer — a stronger assumption, a more powerful primitive, a better algorithm. That reflex is usually wrong, because a good impossibility proof does not lean on the weakness of the tools; it leans on some structural feature of the goal, and the same tools will happily reach a goal shaped slightly differently. The productive response is therefore forensic: find the exact clause of the goal statement the proof consumes, then ask which nearby goals lack that clause and whether any of them is what you actually wanted.

The pattern is sharpest when two versions of an "exchange" sit either side of the line. Demand that two mutually suspicious parties swap secrets each already recognizes, and someone can always defect at the end with substantial probability, no matter how the messages are arranged. Change what the parties know at the outset — so that each is seeking something they could not verify or exploit unilaterally — and the same underlying machinery yields a protocol with arbitrarily small defection probability at polynomial cost. Nothing got stronger. The barrier was a property of the goal's information layout, and moving that layout moved the problem across the line. The same holds for the observation that no bounded-length procedure among distrustful parties can robustly produce certain biases: the obstruction is arithmetic about what finite exchanges can realize, so the answer is to want a different bias or a different robustness notion, never a cleverer schedule of messages.

Carried into ordinary design, this is what to do when a requirement is shown to be unattainable — exactly-once delivery, atomic commit without a blocking window, consistency and availability under partition. Do not treat the proof as an invitation to search harder. Extract which assumption of the requirement the proof used, present the nearest achievable requirement, and force an explicit decision about whether that one is acceptable. Half the "impossible" requirements in practice are one small relabeling away from something buildable, and the other half need to be abandoned early rather than pursued expensively.

**Source:** [Protocols for Secure Computations](../works/protocols-for-secure-computations.md) — the closing section on what cannot be done: the result that in the paper's own model one party or the other can double-cross with substantial probability when swapping known secrets, set against the immediately following construction for the variant exchange in which neither party knows the target the other is solving for, and the separate limit on robustly generating a bit of arbitrary bias.
