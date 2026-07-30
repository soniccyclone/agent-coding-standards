---
type: lesson
title: "Name every assumption that crosses a component boundary, then freeze exactly that and improve everything behind it"
figure: reenskaug
works: [working-with-objects-the-ooram-software-engineering-method]
axes: [verifiability, cognitive-load]
subdomains: [software-engineering-and-architecture]
tags: [lesson]
---
# Name every assumption that crosses a component boundary, then freeze exactly that and improve everything behind it

**Lesson:** The dependency between two components is not the list of function signatures between them. It is everything one must understand and handle correctly for the other to work: names, parameter types, but also the order operations must occur in, who is responsible for releasing what, which protection domain applies, what concurrency is assumed. Call that the surface area. It is almost always larger than the declared interface and almost never written down, which is why upgrading a dependency produces surprises that feel unfair.

The failure mode this creates is worse than version skew, because it corrupts the ordinary remedy. Suppose a supplied component returns a count one too large, and consumers compensate by subtracting one. The compensation is invisible, reasonable, and everywhere. Now the supplier *fixes the bug* — and every consumer becomes wrong in the opposite direction. A subtler version: a new release shifts responsibility slightly between two internal operations, and any consumer who had overridden one of them is now overriding something with different obligations than when they wrote it. In both cases the supplier improved their product and broke people, with no defect on either side. That is the signature of an unspecified surface: correct changes propagate as failures.

The resolution is a contract with two halves, and the second half is the one usually missing. Make the surface as small as you can and *write it down*, then bind the supplier to keep exactly that unchanged while remaining free to alter anything behind it — and bind the consumer to depend on nothing else, modifying only the parts designated as extension points. Neither half works alone: a frozen surface with no stated boundary just freezes everything, and a stated boundary with no commitment to it is documentation. Best if violations are mechanically impossible, next best if a checker catches them, and if it must be manual then the rules still need to be explicit enough to check by hand. This is also why a reusable component cannot be merely a bundle of code — without the rules for its proper use, there is no surface, only exposure.

**Source:** [Working With Objects: The OOram Software Engineering Method](../works/working-with-objects-the-ooram-software-engineering-method.md) — chapter 5's section on frameworks, which credits the surface-area concept to Brad Cox and enumerates its contents, recounts the off-by-one bug fix and the shifted-responsibility override as real upgrade failures, and argues the resolution is a small specified surface the provider must preserve while remaining free to improve hidden parts.
