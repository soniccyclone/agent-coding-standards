---
type: lesson
title: "Getting the right answer and getting an answer are two different proofs with two different mechanisms"
figure: floyd
works: [assigning-meanings-to-programs]
axes: [verifiability, cognitive-load]
subdomains: [formal-methods-and-verification, algorithms-and-complexity]
tags: [lesson]
---
# Getting the right answer and getting an answer are two different proofs with two different mechanisms

**Lesson:** Reasoning that propagates claims through control flow establishes something narrower than it first appears: if the program reaches an exit, the claim at that exit holds. It says nothing about whether an exit is ever reached. This is not an oversight to be patched but a real seam in the subject, because the two questions have different logical shapes. Correctness is preserved by every step, so induction over steps settles it. Termination is a statement about the length of the whole execution, which no single step can witness. Conflating them is how people end up believing a proof covers a loop that in fact spins.

The instrument for the second question is a quantity that strictly decreases at every step and lives somewhere it cannot decrease forever. That last clause is doing all the work: descent alone proves nothing, since a value can descend without bound. What is needed is a well-founded ordering, and once you have one, a global claim about the finiteness of the whole execution is again reduced to a local check on each construct, which is why the technique composes with the correctness argument rather than replacing it. The obvious candidate for such a quantity is a bound on remaining steps, but that is often the hardest one to write. Tuples ordered lexicographically are frequently easier, because they let an outer measure stay flat while an inner one falls, which is exactly the shape of nested loops. The freedom to pick the ordering is the freedom that makes the method usable.

There is also a limit worth internalizing rather than resenting. Some computations cannot be made to always terminate without giving up the power that makes them worth writing, a search over a space that is enumerable but not decidable being the standard case. For those, unconditional termination is not a goal that was missed; it is unavailable, and the honest engineering response is to bound the search externally rather than to pretend the inner loop halts.

A programmer holding this distinction reads every correctness claim as conditional until told otherwise, and when writing a loop asks separately what it preserves and what it consumes. The second question has a practical form that survives outside formal settings: name the finite thing this loop is eating. A loop with no answer to that question is a loop with no termination argument, whatever the tests say.

**Source:** [Assigning Meanings to Programs](../works/assigning-meanings-to-programs.md) — the section on termination proofs, which introduces functions into a well-ordered set attached to each control point and notes both that step-count bounds are often the least convenient choice and that some programs intrinsically cannot be made to terminate without loss of power.
