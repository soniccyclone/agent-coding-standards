---
type: lesson
title: "The cases your argument fails to reach are the inputs your code fails to return on"
figure: jones
works: [software-development-a-rigorous-approach]
axes: [verifiability, cognitive-load]
subdomains: [formal-methods-and-verification, algorithms-and-complexity]
tags: [lesson]
---
# The cases your argument fails to reach are the inputs your code fails to return on

**Lesson:** Two questions about a self-referential definition look unrelated. One is operational: for which inputs does this actually come back with an answer? The other is about justification: which inputs does my reasoning cover? They are the same question. An argument that works down from a stopping case reaches exactly the values from which a chain of steps leads back to that stopping case, and those are exactly the values on which the code winds down instead of running forever. The set the argument covers and the set the code terminates on are the same set, described twice.

This is worth internalizing because it converts a hard question into an easy one. Deciding by inspection whether some input diverges means simulating; noticing that your case analysis handles zero and every step upward but never says anything about the negatives takes a second. Whenever an argument fails to close over some region of the input space, do not go looking for a cleverer argument. Go look at what the code does there. In the ordinary case it diverges, and the gap in the reasoning was a faithful report rather than a shortcoming of the reasoning.

The corollary runs the other way and is the one people skip. If you restrict the inputs so the code behaves — declare that this operation only accepts non-negative values, say — that restriction is not paperwork. It is doing load-bearing work in two places at once: it is what makes the descent to the stopping case guaranteed, and it is what makes the case analysis exhaustive. Drop it and both fail together. So the stated restriction on inputs is not a defensive nicety bolted onto a function that mostly works; it is part of what makes the function a function at all. Treating it as optional documentation and then removing it because "the type already says integer" removes the only thing standing between the code and an infinite regress.

A practical habit falls out. When writing anything recursive — or anything iterative, which is the same structure wearing different clothes — make yourself name the stopping case and name what decreases toward it. Those two names are simultaneously the skeleton of the argument that it is right and the reason it finishes. Not being able to name what decreases is not a gap in your rigour. It is the code telling you it might not stop.

**Source:** [Software Development: A Rigorous Approach](../works/software-development-a-rigorous-approach.md) — chapter 3's "Recursive Functions" section: the requirement that a recursive definition contain at least one clause computing a result without self-reference and that the remaining clauses recur only on values closer to that stopping case; and the closing discussion of the restricted multiplication example, where the pre-condition is observed to play the same part in the function and in its proof — ignoring it leaves the function undefined on part of its declared domain, while an inductive argument covering zero and each step upward simply does not reach the negative values, the two failures being one fact.
