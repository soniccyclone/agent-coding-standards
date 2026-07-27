---
type: lesson
title: "Ask for the procedure that settles every instance, not the answer to the instance in front of you"
figure: hilbert
works: [mathematische-probleme]
axes: [verifiability]
subdomains: [foundations-of-computation, algorithms-and-complexity]
tags: [lesson]
---
# Ask for the procedure that settles every instance, not the answer to the instance in front of you

**Lesson:** There is a difference in kind between answering a question and building the thing that answers all questions of that shape. Hilbert's tenth problem does not ask for the integer solutions of any particular equation; it asks for a uniform mechanical process that, given an arbitrary equation from an infinite family, halts after finitely many steps with a yes-or-no verdict about solvability. Once a problem is posed that way, the object under study stops being the equations and becomes the procedure — and a procedure is something you can ask structural questions about: does one exist, how many steps does it take, what must it be allowed to assume. Framing the demand this way is what later made "no such procedure exists" a statable, provable claim rather than a confession of ignorance.

The shift matters because it relocates where the difficulty lives. Solving instances rewards cleverness that does not accumulate; each new instance may need a new trick, and you learn nothing transferable. Specifying a decider forces you to commit up front to what the inputs range over, what counts as a step, and what finite information the process is permitted to consult — and those commitments are exactly the content that makes the problem tractable to reason about. The same lecture insists that a solution must be establishable in finitely many steps from finitely many exactly formulated hypotheses; a decision procedure is that requirement applied to a whole family at once.

A programmer who thinks this way stops writing the special case and starts asking what class the special case belongs to, then asks whether that class admits a uniform decision at all. It changes what gets built: instead of a validator that handles the configurations seen so far, a checker over a defined input language whose coverage is a property you can state; instead of ad-hoc guards discovered one production incident at a time, a decision procedure over an explicitly bounded space. It also changes what gets abandoned early — if the class you have described is one where no uniform decision can exist, that is worth learning before shipping the framework that pretends otherwise, and you learn it only by having posed the question at the level of the class.

**Source:** [Mathematische Probleme](../works/mathematische-probleme.md) — the tenth problem, which asks for a process deciding solvability of Diophantine equations, read together with the lecture's earlier statement of what a satisfactory solution must be: finitely many logical steps from finitely many precisely stated hypotheses.
