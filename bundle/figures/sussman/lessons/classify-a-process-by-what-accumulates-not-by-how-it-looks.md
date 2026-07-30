---
type: lesson
title: "Classify a process by what accumulates as it runs, not by what the source text looks like"
figure: sussman
works: [scheme-an-interpreter-for-extended-lambda-calculus]
axes: [cognitive-load, hardware-affinity, verifiability]
subdomains: [programming-languages-and-semantics, foundations-of-computation]
tags: [lesson]
---
# Classify a process by what accumulates as it runs, not by what the source text looks like

**Lesson:** "Recursive" and "iterative" name properties of a process, not shapes of text, and the two come apart in both directions. A procedure that mentions its own name can run in fixed space; a procedure whose body looks flat and forward-moving can retain information proportional to the input. Reading the syntax tells you nothing reliable. What does tell you is watching the computation as a sequence of rewritten expressions and asking one question: does the expression grow? A process whose successive states are all the same shape with different numbers in them is an iteration — the entire state of the computation is summarized by a fixed set of quantities. A process whose states grow with the input is a recursion, because each stage has parked a piece of pending work that a later stage must come back to, and the chain of parked pieces *is* the growth.

The sharpest case is the style where results are handed to an explicitly-passed destination rather than returned. It reads as though nothing is ever pending, and the reading is wrong: the destinations nest, one inside the next, and the nested destinations hold exactly the same pending multiplications the conventional version held on the stack. Same information, relocated from the machine's control structure into the program's data. That is worth taking seriously as a general warning, because a great deal of "eliminating the stack" is really moving the stack somewhere the accounting does not look. Also worth noting is the honest exclusion the authors make: the numbers themselves get bigger as the input grows, and that growth belongs to the function being computed, not to the control structure computing it. Charging it against the control structure would make every classification vacuous.

The habit to build is to have a growth question ready whenever you evaluate an implementation. Not "how fast is it" but "what does it retain, and as a function of what?" The answer is usually visible from the shape of successive states without any measurement, it does not depend on the language or the machine, and it survives being reimplemented. It also gives you a language-independent way to state what you require: a construct that has to run over unbounded input needs a bounded-state process, and demanding that is a stronger and more portable specification than demanding a particular looping keyword.

**Source:** [Scheme: An Interpreter for Extended Lambda Calculus](../works/scheme-an-interpreter-for-extended-lambda-calculus.md) — the substitution-semantics section, which traces the reduction sequences of three factorial programs side by side, observes that the self-calling accumulator version cycles through expressions of fixed maximum size while the conventional version's expressions grow with the argument, states the resulting definition of the iteration/recursion distinction, notes that the continuation-passing version looks iterative but stores the same pending work in nested continuations, and separates growth in the numbers computed from growth in the control structure.
