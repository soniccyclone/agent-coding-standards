---
type: lesson
title: "Price a new guarantee as a ratio to the unconstrained baseline, so you learn whether the cost belongs to the guarantee or to the problem"
figure: yao
works: [protocols-for-secure-computations]
axes: [verifiability, hardware-affinity]
subdomains: [algorithms-and-complexity, distributed-systems-and-concurrency]
tags: [lesson]
---
# Price a new guarantee as a ratio to the unconstrained baseline, so you learn whether the cost belongs to the guarantee or to the problem

**Lesson:** When you bolt a cross-cutting requirement onto a computation — privacy, durability, auditability, fault tolerance — the question that decides whether the requirement is viable is not "how expensive is the constrained version" but "how much more expensive is it than the same task with the requirement removed." Absolute cost conflates two things that behave completely differently: the intrinsic difficulty of the task, which no amount of engineering on the guarantee will reduce, and the multiplier the guarantee imposes, which is the only part you control. The right theorem to look for, and the right benchmark to run, is a bound on the constrained cost in terms of an established complexity measure of the unconstrained task. A bounded multiplier means the guarantee is essentially free at scale and you should stop optimizing it; an unbounded one means the requirement is not merely expensive but categorically changes what is achievable, and the design must change instead.

The payoff is diagnostic. Once the multiplier is known to be small, every remaining blow-up is attributable: instances that stay costly are costly because the underlying function is, and the correct response is to attack the problem's own complexity — pick a cheaper function, restrict the domain, exploit structure — rather than to keep hunting for a leaner protocol that cannot exist. This inverts the usual instinct, which is to blame the newest constraint for whatever the profile shows. Establishing the ratio first is what makes it possible to tell a costly guarantee from a costly problem wearing the guarantee's coat, and worked examples confirm the pattern: special-purpose instances with cheap unconstrained descriptions get cheap constrained protocols, while the worst-case blow-up tracks the worst-case description size exactly.

Two habits follow. Always identify, up front, the complexity measure your baseline is expressed in, because a ratio against an unstated baseline is not a measurement. And treat a proof that the multiplier is bounded as a genuine design milestone worth its own effort — it converts an open-ended worry ("can we afford to make this private/verified/replicated?") into a settled fact, and it redirects everyone downstream toward the part of the cost that is actually theirs to reduce.

**Source:** [Protocols for Secure Computations](../works/protocols-for-secure-computations.md) — the complexity subsection, which raises the worry that some functions cheap to compute plainly might become infeasible once the privacy constraint is imposed, then bounds the protocol's exchanged bits in terms of the circuit size of the function itself, and pairs that with the exponential worst-case lower bound whose source is the size of a random function's own description.
