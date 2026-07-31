---
type: lesson
title: "When an operation's precondition is not met yet, attach it to the data as a pending obligation rather than running or failing"
figure: sussman
works: [structure-and-interpretation-of-computer-programs]
axes: [expressiveness, verifiability, parallelizability]
subdomains: [programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# When an operation's precondition is not met yet, attach it to the data as a pending obligation rather than running or failing

**Lesson:** An operation that cannot run yet because its inputs are not determined presents three options and only one of them is good. Running it anyway produces a confidently wrong answer computed from whatever the undetermined input degenerates to. Failing pushes the problem onto the caller, who must now know the operation's readiness condition and arrange the surrounding code to satisfy it — turning an internal detail into a public ordering contract. The third option is to neither run nor fail: record the operation as an obligation attached to the partial answer it applies to, and let it discharge itself at the moment its inputs become determined. The obligation travels with the data, so nothing upstream has to know it exists and nothing downstream has to remember to check.

This is what makes the approach different from the obvious fix of reordering. Reordering works when a static arrangement exists in which every operation's inputs are ready before it runs, and often none does — a condition may be ready on some branches of a search and not others, or ready only after a loop has run an unpredictable number of times, or its readiness may depend on the data rather than the program. Deferral handles all of those uniformly because readiness is evaluated per partial answer at the moment it changes, not per program point at authoring time.

The scheduling question then becomes the real design decision, and it has a clear answer. The lazy extreme — hold every obligation until the very end and discharge them all against complete answers — is correct and expensive, because everything the obligations would have eliminated gets built first, and the intermediate volume is exactly what you were trying to control. So obligations should fire at the earliest moment their inputs are determined, which means the mechanism cannot be a queue drained at the end; it has to be triggered by the act of determining a value. That requirement propagates into the representation: the partial answer must be able to carry attached obligations, and the operation that adds information to it must consult them.

The transferable form is a question worth asking of any pipeline that has an ordering constraint: is this constraint really about program order, or is it about data readiness that program order was being used to approximate? If it is readiness, encoding it as a condition attached to the data is strictly more robust than encoding it as a rule about where the code goes, because it cannot be violated by a caller who did not read the documentation, and it keeps working when the data arrives in an order nobody anticipated.

**Source:** [Structure and Interpretation of Computer Programs](../works/structure-and-interpretation-of-computer-programs.md) — chapter 4 section 4.4.4, Exercise 4.77, which recalls from section 4.4.3 that the negation and host-predicate filters give wrong answers when applied to frames in which the relevant variables are unbound, asks for a fix, and proposes performing the filtering in a delayed manner by appending to the frame a promise to filter that is fulfilled only once enough variables have been bound to make the operation possible; together with the exercise's own qualification that although one could simply wait until all other operations have been performed, efficiency argues for performing the filtering as soon as possible in order to cut down the number of intermediate frames generated.
