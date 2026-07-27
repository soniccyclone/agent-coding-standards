---
type: lesson
title: "Characterize what a set of tools can build by the closure of values it generates, not by trying harder"
figure: hilbert
works: [grundlagen-der-geometrie]
axes: [expressiveness, primitive-count, verifiability]
subdomains: [foundations-of-computation, algorithms-and-complexity, programming-languages-and-semantics]
tags: [lesson]
---
# Characterize what a set of tools can build by the closure of values it generates, not by trying harder

**Lesson:** The final chapter of Hilbert's geometry asks a question of a shape programmers meet constantly: given this specific set of operations and no others, what exactly can be built? His operations are a straight-edge, which draws lines through points and finds their intersections, and an instrument that transfers a given segment onto a given line. He first shows that several apparently richer capabilities — dropping a perpendicular, copying an angle, drawing a parallel — reduce to those two, so the toolset is smaller than it looks. Then he translates the toolset into arithmetic: drawing and intersecting lines corresponds to the four field operations on coordinates, and transferring segments adds one further operation, taking the square root of a sum of two squares. The set of constructible points is then exactly the closure of the given data under those operations, and the question "can this be built?" becomes "does the answer lie in that closure?"

The force of the method is that it produces negative results, which trying harder never does. Because the closure is characterized, he can name a concrete right triangle whose remaining side is a number outside it and conclude that no sequence of straight-edge and segment-transfer steps will ever produce it, though a compass would. He goes further and gives a criterion phrased entirely in terms of the problem rather than the construction: counting the square roots the analytic solution needs, the construction is available precisely when the problem has the full complement of real solutions for every position of the given data. The reach of the toolset has become a computable predicate on problem statements.

This is the pattern behind every honest expressiveness argument in programming, and the reason such arguments are worth making. When you want to know whether a query language, a type system, a configuration format, or a restricted instruction set can express something, the productive move is not to keep attempting encodings; it is to find the invariant preserved by every one of its primitives, so that anything violating the invariant is provably out of reach. Two consequences follow for design. First, a small toolset is worth analyzing precisely because you can bound it — knowing the boundary is often more valuable than pushing it. Second, when the boundary excludes something you need, you now know exactly which new primitive would have to be admitted and what it would cost, which is a far better position than having discovered by exhaustion that the current set does not seem to work.

**Source:** [Grundlagen der Geometrie](../works/grundlagen-der-geometrie.md) — the closing chapter on constructions with straight-edge and segment-transferer: the reduction of the elementary construction problems to those two instruments, the identification of the corresponding closure of coordinate values, and the resulting criterion for constructibility.
