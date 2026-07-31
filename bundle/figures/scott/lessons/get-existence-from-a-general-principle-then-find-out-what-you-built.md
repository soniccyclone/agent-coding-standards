---
type: lesson
title: "Get existence from a general principle first, then find out what you built"
figure: scott
works: [data-types-as-lattices]
axes: [cognitive-load, verifiability, expressiveness]
subdomains: [foundations-of-computation, programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# Get existence from a general principle first, then find out what you built

**Lesson:** Scott had already built recursively defined structures once, in earlier work, by an explicit limiting construction: assemble an approximating sequence, take its limit, and read off the properties of the result from how it was assembled. Here he does it differently and says why the difference matters. He writes the structure down as an equation, invokes a general fixed-point principle to get a solution immediately, and only then — with the object already in hand and known to exist — brings the algebra of his combining operators to bear on the question of what the object actually contains. Existence comes first and cheaply; characterization is a second, separate investigation.

The gain is decoupling. An explicit construction proves existence and reveals structure in a single entangled argument, which means any change to the specification invalidates both halves at once and you rebuild from scratch. Under the split, the existence half is discharged by a theorem that applies to every equation of the right shape, so it survives any respecification for free, and the structural half is a fresh question answered with general-purpose lemmas about how the combining operators behave. Changing the equation then costs you one re-run of the analysis rather than a new construction and a new proof. The same asymmetry is worth looking for anywhere you are tempted to build a thing by hand in order to know it is there: is there a general principle that hands you the object, leaving you free to study it?

There is a discipline attached that is easy to skip. Having an object handed to you by a general principle means you genuinely do not know what is in it, and the analysis afterward is obligatory rather than optional. Scott performs it in detail — establishing which elements are present, which operations are available on them, and how the cases are distinguished — because until that is done all he has is a solution to an equation, not a data type anyone can use. The failure mode of the cheap-existence route is stopping at the fixed point and treating the specification as if it were the description. It is not; the specification says only that something satisfies it, and the work of finding out what that something is has merely been postponed, not eliminated.

**Source:** [Data Types as Lattices](../works/data-types-as-lattices.md) — Section 4's limit theorem and the discussion of the recursive tree equation immediately following it, where Scott contrasts this approach with his own earlier method that required limits in order to show the structure exists at all, notes the advantage of using the recursion combinator to get existence at once and then applying the function-space, product and sum theorems to determine the nature of the retract, and then works through what the resulting type contains and which operations on it are definable.
