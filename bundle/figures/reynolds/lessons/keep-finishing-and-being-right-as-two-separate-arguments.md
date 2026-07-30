---
type: lesson
title: "Keep \"it finishes\" and \"it is right\" as two separate arguments, because one can die while the other still stands"
figure: reynolds
works: [the-craft-of-programming]
axes: [verifiability, cognitive-load]
subdomains: [formal-methods-and-verification, software-engineering-and-architecture]
tags: [lesson]
---
# Keep "it finishes" and "it is right" as two separate arguments, because one can die while the other still stands

**Lesson:** The ordinary way of stating what a piece of code guarantees is conditional: start it in a permitted state, and *if it stops*, it stops somewhere acceptable. That conditional is not a weakness to be patched out. It isolates a claim that rests on one kind of evidence — a relation preserved by every step — from a claim that rests on an entirely different kind: some quantity that each step pushes toward a wall it cannot pass. Two different obligations, two different failure modes, two different things to look at when something goes wrong. Fusing them into one guarantee saves a line of notation and costs you the ability to tell which half broke.

The reason to insist on the separation is that the two halves are not correlated. Swap one derivation step for a stronger one — a fact that lets each iteration make twice the progress — and the preservation argument survives untouched, every step still maintains exactly what it maintained before, while the termination argument quietly dies for every input that is not of the right parity: the wall is still there, but the sequence of values now steps over it instead of landing on it. Nothing in the correctness reasoning flinches. If the two were one argument you would have no way to see that the change was safe in one dimension and catastrophic in the other, and the temptation would be to conclude the whole thing is fine because the part you were looking at held.

The practical discipline that follows is to keep termination in mind while building and to make the argument afterward, in its own right. Keeping it in mind is what makes the preserved relation carry the range information the termination argument will need — bounds that look like clutter when you only care about the result turn out to be exactly what pins the quantity against its wall. Making the argument separately is what keeps you honest about the cases where no such quantity exists, and about the ones where the bound is real but nobody can prove it. A claim of the conditional form is an honest thing to publish; a claim that implies finishing and cannot demonstrate it is not.

**Source:** [The Craft of Programming](../works/the-craft-of-programming.md) — the distinction between conditional and total correctness introduced with the factorial development, and the variant derived from the doubled recurrence, which is called out as being just as valid as the original except that it terminates only for even inputs.
