---
type: lesson
title: "An abstraction is rented against whatever overhead the current hardware still hides"
figure: backus
works: [the-history-of-fortran-i-ii-and-iii, the-fortran-automatic-coding-system]
axes: [hardware-affinity, expressiveness]
subdomains: [programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# An abstraction is rented against whatever overhead the current hardware still hides

**Lesson:** Before the machine in question, systems that let people write something better than machine code were tolerable because almost all execution time went into emulating arithmetic the hardware did not have. Sloppy address computation and clumsy loop management cost nothing anyone could notice, since they were rounding errors against the emulation. Then a machine arrived with arithmetic and index registers built in, and the same overheads that had been invisible became the entire cost. The lesson generalizes past this instance: the overhead budget an abstraction lives inside is not a property of the abstraction, it is a property of what currently dominates the machine's time. Hardware improvement does not uniformly help. It removes the cover that made some designs viable, and a design that was fine last year can be exposed by a faster component it never touched.

That reframing changes where the hard problem is. If a notation will only be adopted when its output runs close to what a careful person would have written by hand, then the notation is the cheap half of the project and the mapping down to mechanism is the expensive half. This was a deliberate bet, held against widespread disbelief, and the group acted on it: they treated designing the language as a prelude and spent years on the translator, on the grounds that a factor of two in execution speed would have been fatal to acceptance regardless of how pleasant the language was. Others building similar notations at the same time had a far easier task precisely because they were content to provide an input language and not to compete with hand coding.

The uncomfortable corollary is a claim about why better ways of programming do not spread. Expressive power alone does not win; power plus an execution cost near that of the incumbent wins, and the second condition is the one that usually fails. Anyone who wants a fundamentally better way of expressing computation to become normal has to solve two problems, and treating the second as someone else's implementation detail is how good ideas stay in papers. A designer who believes this asks, of any abstraction being proposed, what it will cost against today's dominant cost — and asks again when the hardware moves.

**Source:** [The History of FORTRAN I, II, and III](../works/the-history-of-fortran-i-ii-and-iii.md) — the early sections on the economics of programming and on why the new machine's built-in arithmetic left inefficiency nowhere to hide, plus the retrospective claim that the next advance in programming requires both a more powerful language and a cheap way to execute it. Also [The FORTRAN Automatic Coding System](../works/the-fortran-automatic-coding-system.md) — the framing of the project's goal as obtaining an efficient machine program automatically from a concise mathematical specification.
