---
type: lesson
title: "Eliminate the need for names instead of building machinery to scope them"
figure: von-thun
works: [mathematical-foundations-of-joy]
axes: [primitive-count, cognitive-load, expressiveness]
subdomains: [programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# Eliminate the need for names instead of building machinery to scope them

Most languages treat name management as an unavoidable cost and then spend
enormous design budget containing it: formal parameters, local variables, nested
declarations, block structure, modules, visibility qualifiers, import lists.
Each of these is a mechanism for hiding a name from code that has no business
seeing it. Von Thun's move is to attack the premise instead of the symptom — if
the amount of information requiring concealment is driven toward zero, the whole
apparatus of concealment becomes unnecessary. A design that produces no names to
hide does not need a scoping rule, and therefore does not need the reader to
carry a scoping rule in their head.

The argument holds because named things enter a program for identifiable
reasons, and those reasons can be examined one at a time rather than accepted as
a package. Something gets a name because it must refer to itself, because it is
wanted in several places, or because naming it clarifies the reading. Only the
last of these is a genuine and irreducible reason. The first two are artifacts
of the notation: given a way to hand a piece of program to something that will
run it, self-reference no longer requires a name to call, and reuse becomes a
matter of passing the fragment rather than resolving an identifier. What looked
like a fundamental requirement of programming turns out to be a consequence of
the particular abstraction mechanism a language happened to pick.

The discipline this teaches is to distinguish load-bearing complexity from
complexity you have inherited. When a language or system grows an elaborate
subsystem, ask what would have to be true for that subsystem to be pointless.
Interface leanness is usually pursued by adding walls; von Thun pursues it by
reducing what is on the other side of the wall. That reframing is available far
more often than people notice — configuration systems that exist because state
was made global, dependency-injection frameworks that exist because
construction was tangled with use, cache-invalidation logic that exists because
something was cached that could have been recomputed.

A programmer who believes this reads every large mechanism as a possible
confession. Before extending it, they look for the earlier decision that made it
necessary and price the alternative of undoing that decision. They also accept
the honest cost: von Thun's own worked example of name-free recursion is, by his
own admission, awkward and slow in its raw form, and only becomes pleasant once
the right higher-order operator is introduced. Removing a mechanism does not
automatically produce elegance — it produces a new obligation to find the
abstraction that makes the removal livable, and the design is not finished until
that abstraction exists.

**Source:** [Mathematical Foundations of Joy](../works/mathematical-foundations-of-joy.md) — the "Elimination of Definitions" section, which opens on the software-engineering problem of interdependent parts and lean interfaces, then argues Joy's answer is to minimize the information needing to be hidden rather than to hide it better; the factorial development that follows is the honest demonstration of both the cost and the payoff.
