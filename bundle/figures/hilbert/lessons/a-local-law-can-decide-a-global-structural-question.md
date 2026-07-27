---
type: lesson
title: "Look for the local, checkable law that is equivalent to the global structural question"
figure: hilbert
works: [grundlagen-der-geometrie]
axes: [verifiability, expressiveness]
subdomains: [foundations-of-computation, formal-methods-and-verification, software-engineering-and-architecture]
tags: [lesson]
---
# Look for the local, checkable law that is equivalent to the global structural question

**Lesson:** Some of the questions that matter most about a system are about the system as a whole: can this piece be embedded in a larger structure, does this component compose with others, is this fragment a genuine restriction of something bigger or an isolated accident. Such questions look untestable from inside the piece. Hilbert's treatment of Desargues's configuration shows they need not be. Working in a plane where only the connection, order, and parallel assumptions hold, he proves that the plane can be realized as a slice of a three-dimensional geometry obeying those same assumptions exactly when one particular incidence statement about two triangles holds in it. He puts the point sharply: that statement is what the space assumptions leave behind after they are eliminated. A global embeddability question has been converted into a law you can check by looking at triangles.

The construction of the equivalence is as instructive as the result. In one direction, embeddability makes the statement derivable, so its failure rules out embedding. In the other, he uses the statement to build an arithmetic out of the plane's own segments, then uses that arithmetic to construct a three-dimensional geometry whose flat slice is the original plane — the local law supplies exactly the algebraic structure needed to manufacture the extra dimension. And he shows this is not vacuous by exhibiting a plane, built from straight pieces and circular detours, in which everything else holds and the law visibly fails: a plane that cannot be a slice of any such space.

The habit worth stealing is to stop treating global structural properties as things you can only assess by trying the integration and seeing what happens. Ask instead what locally checkable identity is equivalent to the property. This is what a well-chosen algebraic law does for composability: associativity of a merge operation, commutativity of an update, idempotence of a retry are all small statements you can test on a handful of values, and each is equivalent to a global claim about whether pieces can be reassembled in arbitrary orders and groupings without changing the outcome. When you find such a law, you get both a cheap test and — as in Hilbert's second direction — often a recipe for constructing the larger structure the law was standing in for.

**Source:** [Grundlagen der Geometrie](../works/grundlagen-der-geometrie.md) — the chapter on Desargues's theorem: the demonstration that its validity is necessary and sufficient for a plane geometry to sit inside a spatial one, together with the constructed plane geometry where it fails.
