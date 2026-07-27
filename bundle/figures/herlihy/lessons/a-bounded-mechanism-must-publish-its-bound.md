---
type: lesson
title: "A mechanism with a physical limit is only usable if the limit is part of its published contract"
figure: herlihy
works: [transactional-memory-architectural-support-for-lock-free-data-structures]
axes: [hardware-affinity, cognitive-load]
subdomains: [operating-systems-and-systems-programming, distributed-systems-and-concurrency]
tags: [lesson]
---

# A mechanism with a physical limit is only usable if the limit is part of its published contract

**Lesson:** An abstraction implemented in a finite physical resource inherits that resource's ceiling, and there are only three honest responses: hide the ceiling behind a slower general path, expose it as a documented floor callers may rely on, or pretend it does not exist and ship something nobody can write portable code against. The proposal here takes the middle road deliberately. Speculative state lives in a small dedicated buffer, so a speculation that touches too many locations simply fails; it can also fail because a timer fired, or the operating system switched contexts, or a page was missing — reasons having nothing to do with any actual conflict. Rather than engineering that away, the design accepts spurious failure as normal, requires every use to be written as a retry loop, and states that the instruction set must promise a minimum capacity, because without such a promise a program that works on one implementation cannot be expected to work on the next.

The reasoning generalizes past hardware to any best-effort facility: a cache, a fixed-size queue, a batch API with an undocumented request cap, a bounded retry budget. Two obligations follow. The caller's obligation is to treat failure as ordinary control flow rather than an exception, since a facility that fails for reasons unrelated to the caller's correctness cannot be made reliable by getting the caller's logic right. The provider's obligation is the harder one: publish a guaranteed floor, not a typical capacity, because a floor is the only thing anyone can build on. A number that usually holds is worse than a smaller number that always holds, and it is worse in the specific way that makes systems fail late and in production, on the machine that had a smaller buffer.

There is also a layering pattern worth taking from the same discussion. When the bounded fast path overflows, do not widen the hardware; trap into software and let a general implementation take over, so the common case stays fast and the rare case merely stays correct. This is a stronger design position than it looks, because it converts a hard capacity limit into a performance cliff, and a performance cliff is something a system can survive. A programmer who thinks this way is careful to know, for every fixed-capacity mechanism in a design, both what the guaranteed floor is and what happens on the far side of it — and treats "it has always been big enough" as an unowned risk rather than an answer.

**Source:** [Transactional Memory: Architectural Support for Lock-Free Data Structures](../works/transactional-memory-architectural-support-for-lock-free-data-structures.md) — the intended-use pattern built around an explicit retry loop, the limitations section on short durations and small data sets with forward progress delegated to software backoff, and the rationale section's argument that portability demands an architecturally guaranteed minimum size together with the overflow-into-software escape hatch.
