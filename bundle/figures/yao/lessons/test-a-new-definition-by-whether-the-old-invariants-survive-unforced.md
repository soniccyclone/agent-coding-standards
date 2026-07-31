---
type: lesson
title: "Test a new definition by whether the old theory's invariants survive where nothing forces them to"
figure: yao
works: [theory-and-applications-of-trapdoor-functions]
axes: [verifiability, cognitive-load]
subdomains: [foundations-of-computation, formal-methods-and-verification]
tags: [lesson]
---
# Test a new definition by whether the old theory's invariants survive where nothing forces them to

**Lesson:** A newly proposed definition cannot be validated by the results it makes provable, because a definition can be tuned until the results you wanted follow, and a tuned definition describes your intentions rather than the world. The stronger check is conservative: identify the load-bearing invariants of the established theory you are generalizing, and ask whether they still hold when the new quantity is substituted for the old one. The invariant worth checking is one whose survival is not guaranteed by anything obvious — where you can sketch a plausible reason it might fail, and where its failure would cost you an interpretation you depend on. If it survives anyway, and survives by an argument drawn from the new theory's own machinery rather than by inheritance, that is evidence about the definition that no downstream theorem can supply.

The failure case tells you what you are protecting. If a conservation law of the old theory breaks under the new measure — a unit of the new quantity slipping through a bottleneck rated for fewer units of the old one — you lose more than a theorem. You lose the right to treat your units as interchangeable, and a quantity whose units behave differently depending on where they came from is not a measure of anything; it is bookkeeping. So the check is not decoration on a finished theory. It decides whether the central object is coherent enough to build on, which is why it belongs before the applications rather than after.

Ported into ordinary design, this is the discipline for replacing a definition inside a working system — a new consistency level, a new notion of equality, a new cost accounting for capacity planning. Do not evaluate the replacement only on the new cases it handles. Write down which invariants the old definition made everyone rely on, especially the ones no one states because they seemed structural, and check each against the replacement. The ones that hold for a non-obvious reason are your evidence the replacement is real; the one that quietly breaks is the source of every subsequent incident, because the whole system was built on an equivalence that stopped being true.

**Source:** [Theory and Applications of Trapdoor Functions](../works/theory-and-applications-of-trapdoor-functions.md) — the reliable-transmission section of Part 1 and the discussion following its main theorem, which argues the result matters because a channel carrying more of the new quantity than its rated capacity would destroy the inherited interpretation and force the conclusion that units of the new quantity do not all behave alike, and notes that no purely combinatorial reason forbids such a violation, so obtaining a consistent answer by complexity-based reasoning is what gives confidence the definition is on the right track.
