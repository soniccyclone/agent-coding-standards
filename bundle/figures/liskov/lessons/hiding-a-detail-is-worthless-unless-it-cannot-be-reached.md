---
type: lesson
title: "Hiding a detail is worthless unless the language makes it unreachable"
figure: liskov
works: [programming-with-abstract-data-types]
axes: [verifiability, cognitive-load]
subdomains: [programming-languages-and-semantics, formal-methods-and-verification, software-engineering-and-architecture]
tags: [lesson]
---
# Hiding a detail is worthless unless the language makes it unreachable

**Lesson:** There is a large gap between a detail that clients are asked not to
depend on and a detail clients are physically unable to depend on. The first is
a social arrangement, and social arrangements decay under deadline pressure: the
moment reaching into the representation is the fastest route to a working
program, someone reaches. The second is a structural property, checked
mechanically, and it holds no matter who is writing the caller or how tired
they are. Only the second one buys anything, and what it buys is not
tidiness — it is the right to change the implementation later without auditing
the whole program.

Two consequences follow that are worth more than the encapsulation itself. The
first is that verification factors cleanly. A proof that the implementation
satisfies the abstraction is entirely separate from a proof that a client is
correct, because the client's argument can only appeal to relations among the
operations — nothing else is visible to it. Two smaller independent proofs
replace one large entangled one, and neither has to be redone when the other
side changes. The second is that fault localization becomes mechanical: if a
representation-level failure occurs, the set of code that could have caused it
is exactly the code that can see the representation, which is a handful of
modules rather than the program.

Enforcement therefore has to be a property of the checker, not the style guide.
The type system is the thing doing the work, and it is doing security work as
much as engineering work — a missed check does not merely permit sloppiness, it
lets private information escape and destroys the modularity that the whole
argument rested on. A programmer who believes this treats every "just this once,
reach in and grab the field" as a proposal to give up a proof decomposition and
a fault-localization guarantee, and prices it accordingly. It also explains
why an extra type is sometimes the right answer to a leak: interposing a
distinct abstraction between two modules can confine knowledge of a
representation that would otherwise diffuse across the system.

**Source:** [Programming with Abstract Data Types](../works/programming-with-abstract-data-types.md) — the discussion of controlling the use of information, where inaccessibility (not merely irrelevance) of the representation is what splits correctness proofs in two and confines the origin of representation-level errors.
