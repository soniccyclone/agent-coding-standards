---
type: lesson
title: "Grow a system as a chain of subsystems that each already work, and arrange things so new code cannot break old code"
figure: brinch-hansen
works: [the-solo-operating-system-processes-monitors-and-classes, the-programming-language-concurrent-pascal]
axes: [verifiability, cognitive-load]
subdomains: [software-engineering-and-architecture, operating-systems-and-systems-programming]
tags: [lesson]
---
# Grow a system as a chain of subsystems that each already work, and arrange things so new code cannot break old code

**Lesson:** The reason large programs are terrifying to change is that confidence does not accumulate. You establish that something works, add to it, and the addition can invalidate what you established, so every increment potentially resets you to zero and the effort of staying confident grows with the size of what you've built. Break that dynamic and the character of the work changes completely. If dependency runs strictly one way, then existing parts never invoke newer parts, and newer parts reach existing ones only through interfaces that were already exercised. Confidence in the old part survives the arrival of the new one as a matter of structure rather than diligence. A system built this way is a sequence of intermediate systems, each complete and working, rather than a pile of parts that becomes a system on the day it first runs.

The practical shape of this is to build in dependency order, adding one component at a time and driving it with a small harness before anything is layered on top. What that yields, in the one case where the numbers are reported, is a defect profile that looks wrong: roughly one test run per component, most of the errors found in the throwaway harnesses rather than in the system, and a rewrite of a third of the program a year later that compiled and went back into service in a day. Two things produce that outcome together. The compiler's refusal to let new code reach into old state is what makes the guarantee real rather than aspirational. Modules that hide their internals behind a fixed set of operations are what make each component nearly correct before it is ever executed, because there is so little surface on which to be wrong.

A programmer who works this way inverts the usual relationship between construction and testing. Testing stops being a phase that validates a finished artifact and becomes the thing that certifies each rung of a ladder you are still climbing. It also changes what counts as a good module boundary: the best boundary is the one that lets the thing below it be finished and left alone. There is a real cost, which the reviewers of this work noticed — a program built as a strict hierarchy of small components is read by constant cross-reference, and reading it demands more page-turning than a flat program does.

**Source:** [The Solo Operating System](../works/the-solo-operating-system-processes-monitors-and-classes.md) — the conclusion, which reports the bottom-up construction, the run and error counts, and attributes the result to compiler-enforced access ordering plus data abstraction. Also [The Programming Language Concurrent Pascal](../works/the-programming-language-concurrent-pascal.md) — the scope-rules discussion of why a hierarchical ordering lets a tested subsystem stay correct as untested components are added above it.
