---
type: lesson
title: "To prove one level stronger than another, make it enumerate the weaker one"
figure: peter
works: [uber-die-mehrfache-rekursion]
axes: [expressiveness, verifiability]
subdomains: [foundations-of-computation, algorithms-and-complexity]
tags: [lesson]
---
# To prove one level stronger than another, make it enumerate the weaker one

Showing that a class of definable functions is strictly smaller than another
looks like it should require ingenuity — hunt for a specific function on one
side and not the other, then argue about it. Péter's separation of the layers is
mechanical instead, and the mechanism is reusable. Reduce every definition at
level k to one rigid normal form. Because the form is rigid, a definition is
just a finite record of construction steps, so it can be coded as a number, and
the catalogue of all level-k functions becomes a single function of an extra
index argument. Then show that this catalogue function is itself definable using
one recursion at level k+1. Diagonalize against it: the catalogue's own entry,
incremented, cannot appear in the catalogue. Level k+1 therefore reaches
something level k does not, and the argument needs no cleverness about any
particular function.

The pivot is that a class's power is measured by whether it can enumerate
itself. If a level could catalogue its own inhabitants, the diagonal would be
both inside and outside it, so no honest level can. Every class is blind to its
own index, and the first place from which the class becomes visible is exactly
one notch up. Note also what makes the argument even possible: the normal-form
work, which reads as tedious bookkeeping, is what turns definitions into
finite data. Without it there is no enumeration and no diagonal. The
housekeeping is not preliminary to the theorem; it is the theorem's engine.

Two habits follow for anyone reasoning about the strength of a language, a
configuration format, a query dialect, or a type system. First, when you want to
know whether extension X really adds power, ask whether X lets you write an
interpreter for the system without X — that single question replaces a search
for witnesses. Second, expect self-description to be the boundary: a system
expressive enough to enumerate its own programs has already crossed into
territory where diagonal arguments bite, which is a feature if you wanted
reflection and a warning if you wanted decidability. Péter also notes, without
pursuing it, that a proof built from a more conceptual generalization of the
diagonal function would be preferable to hers — a useful reminder that a
correct separation and an illuminating one are different achievements.

**Source:** [Über die mehrfache Rekursion](../works/uber-die-mehrfache-rekursion.md) — the section on the diagonal procedure, which enumerates the k-fold recursive functions of k arguments and defines the enumerating function by a single recursion one level higher.
