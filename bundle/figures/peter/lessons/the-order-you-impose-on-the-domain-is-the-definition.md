---
type: lesson
title: "The order you impose on the domain is the real definition of a recursion"
figure: peter
works: [uber-die-mehrfache-rekursion]
axes: [expressiveness, verifiability, primitive-count]
subdomains: [foundations-of-computation, programming-languages-and-semantics]
tags: [lesson]
---
# The order you impose on the domain is the real definition of a recursion

A recursive definition says: the value here is assembled from values that came
before. Everything rests on "before" — and Péter's opening move is to point out
that "before" is not handed to you by the data. For a function of two arguments
there are many defensible ways to declare which argument tuples precede a given
one. Count only the tuples in strictly earlier rows and you get one scheme;
also count the tuples earlier within the current row and you get a different,
strictly more powerful one. Neither ordering is more natural than the other on
inspection; both are well-founded, both bottom out in finitely many steps, both
give definitions you can compute. But they are not equivalent in what they can
define. The choice of order, made almost invisibly, fixes the expressive
ceiling of the whole scheme.

This reframes recursion as a design decision rather than a mechanism. The
mechanism — assemble from earlier values — is fixed and boring. The interesting
degree of freedom is the well-order you lay over the argument space, and Péter
treats it as such: she explicitly names an ordering, notices its order type,
and then argues about power in terms of that type. Once the ordering is named,
questions that seemed to be about syntax become questions about combinatorics
of the ordering, and results about strength follow from properties of the order
rather than from staring at recursion equations.

The practical consequence is that "this function isn't definable by recursion"
is almost never a real statement. It is shorthand for "not definable under the
ordering I happened to adopt." A programmer who believes this stops accepting a
recursion pattern as dictated by the shape of the data structure and starts
asking what termination order the code actually depends on, then whether a
different order — lexicographic across several parameters, a measure that
mixes them, a nesting of one traversal inside another — makes the awkward case
routine. It also changes how you argue that a recursive routine terminates: not
by tracing calls, but by exhibiting the order and showing each call descends in
it. Naming the order up front turns both the design and the correctness
argument into one piece of work instead of two.

**Source:** [Über die mehrfache Rekursion](../works/uber-die-mehrfache-rekursion.md) — the introductory argument that restricting recursion to a single variable is arbitrary, where the precedence relation among argument tuples is spelled out and shown to be a choice with consequences for definability.
