---
type: lesson
title: "Portability comes from naming the seam where the machine shows through, not from hiding the machine"
figure: cutler
works: [oral-history-of-david-cutler, decwest-sdt-agenda-prism-vs-mips]
axes: [hardware-affinity, primitive-count, cognitive-load]
subdomains: [operating-systems-and-systems-programming, software-engineering-and-architecture]
tags: [lesson]
---
# Portability comes from naming the seam where the machine shows through, not from hiding the machine

**Lesson:** There are two ways to write software that survives a change of processor.
The common one is to abstract over the hardware until the code no longer mentions it,
which fails at exactly the points where the hardware's behavior is semantically visible:
memory ordering, cache coherence, interrupt delivery, atomicity, exception continuation.
The other way is to accept that a small set of machine-dependent facts is irreducible,
enumerate that set deliberately, confine it to a layer that exists only to be replaced,
and forbid it from leaking anywhere else. The second approach keeps the primitive count
of the machine-specific layer small and known rather than pretending it is zero.

The payoff is empirical rather than aesthetic. A system built the second way can absorb
a target change that arrives as bad news partway through a project without restructuring
anything above the seam, because the set of things that must be rewritten was decided
before anyone knew which processor would win. A system built the first way discovers its
machine dependencies one crash at a time, distributed through code that claimed to be
portable. The difference in cost is not a factor of two; it is the difference between
substituting a module and auditing everything.

The discipline has a subtler consequence that is easy to miss. When a substitution
becomes necessary and the machine-dependent layer turns out to be incomplete, the
temptation is to patch around each missing capability where it is needed. That buys the
current port and guarantees paying again at the next one, because the workarounds are
specific to the gap rather than to the abstraction. The correct response to a discovered
dependency is to promote it into the named seam, so the next substitution is a
replacement rather than another archaeology project.

A programmer who believes this asks, before writing the first line of a long-lived
system, which facts about the current machine the design is permitted to assume, and
writes that list down. Everything not on the list is a bug when it appears, regardless
of whether the code currently works.

**Source:** [Oral History of David Cutler](../works/oral-history-of-david-cutler.md) — the
description of structuring a portable kernel so that architecture-specific code was
isolated and swappable, which is what let the project survive abandoning its original
target processor and then accumulating four more. The companion argument appears in
[DECwest/SDT Agenda: PRISM vs. MIPS](../works/decwest-sdt-agenda-prism-vs-mips.md), whose
estimate of the work to retarget an operating system explicitly excludes the additional
effort of building implementation-independent solutions, and notes that skipping that
effort guarantees the same problem recurs on the next chip.
