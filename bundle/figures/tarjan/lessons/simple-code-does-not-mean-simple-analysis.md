---
type: lesson
title: "Simple code does not imply simple analysis, and the complicated rival is usually the worse choice"
figure: tarjan
works: [efficiency-of-a-good-but-not-linear-set-union-algorithm]
axes: [cognitive-load, verifiability]
subdomains: [algorithms-and-complexity]
tags: [lesson]
---
# Simple code does not imply simple analysis, and the complicated rival is usually the worse choice

**Lesson:** The situation this paper resolves is instructive precisely because it looks backwards. Two rival methods existed for the same bookkeeping problem: one elaborate and hard to implement, whose cost had been bounded by its authors, and one almost trivially simple — two small rules layered on the obvious representation — whose cost nobody could pin down. The elaborate one had the analytical high ground for years on the strength of nothing but being easier to bound. Tarjan's result is that the simple one is *better*, and that establishing it requires a genuinely difficult argument built on a function so fast-growing it isn't primitive recursive. His own summary of the situation is the memorable part: this may be the only example of a simple algorithm with a very complicated running time. Simplicity of the artifact and simplicity of the reasoning about it are independent dimensions, and confusing them systematically favors the wrong artifact.

The asymmetry in who pays is what makes the practical rule clear. Analysis is a one-time cost, paid by whoever does it, and once done it is quotable forever. Implementation complexity is a recurring cost paid by everyone who reads, ports, debugs, or extends the thing, for as long as it lives. So when the choice is between a simple mechanism you cannot yet justify and a complicated one you can, the correct default is to prefer the simple mechanism and invest in understanding it, rather than to adopt the complicated one because its paperwork is already filed. The reverse instinct — treating "we can bound this" as evidence of quality — is a real failure mode in engineering as much as in theory, and it shows up as elaborate frameworks chosen over plain code because the elaborate one has a story attached.

The same reasoning applies to the *result* of an analysis, not just its difficulty. The bound here is not a clean expression; it involves an extremely slow-growing function that nobody would have proposed as a design target. That ugliness is a fact about the algorithm, discovered, not a sign that the analysis went wrong. Being willing to accept an answer whose shape you did not anticipate is part of doing the analysis honestly, and it is the difference between measuring a system and confirming an expectation about it. A rule of thumb worth keeping: if every performance answer you get is a tidy power or a tidy logarithm, you are probably fitting your conclusions to the vocabulary you brought rather than to the system in front of you.

**Source:** [Efficiency of a Good But Not Linear Set Union Algorithm](../works/efficiency-of-a-good-but-not-linear-set-union-algorithm.md) — the introduction's comparison of the very complicated prior algorithm with the very simple one considered here and the survey of successively better bounds people had proved for it, and the conclusion's remark that this is probably the first and perhaps only example of a simple algorithm with a very complicated running time, alongside the inverse-Ackermann form of the final bound.
