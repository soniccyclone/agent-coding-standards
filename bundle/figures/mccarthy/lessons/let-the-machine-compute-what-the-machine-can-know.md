---
type: lesson
title: "If a bookkeeping fact is derivable from the program's own structure, make the machine derive it instead of making the programmer track it"
figure: mccarthy
works: [recursive-functions-of-symbolic-expressions]
axes: [cognitive-load, hardware-affinity]
subdomains: [operating-systems-and-systems-programming, programming-environments-and-object-systems]
tags: [lesson]
---
# If a bookkeeping fact is derivable from the program's own structure, make the machine derive it instead of making the programmer track it

**Lesson:** Storage reclamation looks like a duty that must fall on whoever allocated the storage, and for most of computing history it did. The insight that dissolves the duty is noticing that the relevant fact is not private to the programmer at all: a piece of memory matters exactly when some chain of structural steps from a known root can still reach it, and unreachability is therefore a property the runtime can compute for itself by traversal. Nobody has to be told. Once you see the fact as derivable, asking the programmer to maintain it by hand is revealed as asking them to duplicate, unreliably and in their head, something the machine already has the information to determine.

The reason this generalizes past memory is the shape of the argument, which is worth separating from its famous instance. Find a piece of bookkeeping the programmer is currently doing manually; ask whether the information needed to do it correctly is already present in the program's structure or the runtime's state; if it is, the manual version is pure cognitive tax plus a bug source, and the correct move is to compute it. The same reasoning appears in the paper's other delegations — the stack discipline that saves and restores registers around recursive calls so a recursive routine can be written as if it had the machine to itself, and the choice not to expose whether a shared substructure is physically duplicated, since duplication changes time and space but never the answer.

The honest part of this thinking is that it does not pretend the delegation is free. Reclamation only pays off when the live set is comfortably smaller than the heap, because the traversal costs real time and must return enough storage to be worth the pause. The design is accepted with that condition stated, not hidden. So the discipline is two-sided: delegate what the machine can derive, and be explicit about the performance regime in which the delegation holds. A programmer who works this way pushes derivable invariants down into infrastructure aggressively while keeping a clear-eyed account of the operating envelope that makes each one viable.

**Source:** [Recursive Functions of Symbolic Expressions and Their Computation by Machine, Part I](../works/recursive-functions-of-symbolic-expressions.md) — the description of the free-storage list and the reclamation cycle that marks everything reachable from base registers before sweeping the rest, together with its candid note on when reclamation is and is not economical, and the neighboring discussion of the push-down list that makes recursive routines indifferent to temporary-register conflicts.
