---
type: lesson
title: "Admit complexity only where it can be quarantined, not where it pays best"
figure: thompson
works: [unix-implementation]
axes: [cognitive-load, verifiability]
subdomains: [operating-systems-and-systems-programming, software-engineering-and-architecture]
tags: [lesson]
---
# Admit complexity only where it can be quarantined, not where it pays best

**Lesson:** The usual test applied to a clever algorithm is whether the gain justifies the cost — does the speedup earn the extra difficulty? That test is the wrong shape, because it weighs a local benefit against a cost that is not local. Difficulty leaks. A subtle mechanism forces everything that touches it to reason about it, so its real price is paid by code that gets no share of the benefit. The better test asks a containment question first: can this cleverness be sealed inside a boundary, such that callers get a plain description and never need to know how it is achieved? If yes, admit it. If no, take the slower, duller mechanism regardless of how much performance is on the table.

The consequence is a default that looks backwards to anyone optimising in the small: simplicity is chosen over efficiency as the standing policy, and efficiency wins only in the specific places where its machinery does not escape. This is not indifference to speed. It is the recognition that a system's total intelligibility is a finite budget spent globally, while performance gains are earned locally, so the two cannot be traded one-for-one. A design containing three localised complexities is comprehensible; the same amount of complexity smeared across the interfaces between subsystems is not, even though the sums are equal.

Notice too where the quarantine boundary usually has to sit: at the point where a mechanism's asynchrony or laziness becomes visible. When an optimisation defers work — caching writes, reordering operations, decoupling logical order from physical order — it has not been contained, because the deferral shows up as observable state in the wrong order and as errors that surface far from the call that caused them. That is the signature of complexity that escaped: not that the code is hard to read, but that its consequences are reported somewhere other than where the decision was made.

A programmer who works this way stops asking "is this optimisation worth it" and starts asking "where does this become someone else's problem". Optimisations survive review when a wall can be drawn around them; they get rejected, even profitable ones, when the wall would have holes. And when a contained optimisation later turns out to leak — error handling that cannot be made meaningful, an ordering guarantee that quietly evaporated — that leak is treated as the defect, not as an acceptable cost of speed.

**Source:** [UNIX Implementation](../works/unix-implementation.md) — the introductory statement of policy that simplicity was substituted for efficiency throughout and complex algorithms used only when their complexity could be localised, together with the block-buffering section's candid accounting of what the deferred-write cache broke.
