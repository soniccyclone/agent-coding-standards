---
type: lesson
title: "Ask whether you could stop and resume from the named state; that is the test for whether the state is complete"
figure: sussman
works: [structure-and-interpretation-of-computer-programs]
axes: [cognitive-load, hardware-affinity]
subdomains: [software-engineering-and-architecture, operating-systems-and-systems-programming]
tags: [lesson]
---
# Ask whether you could stop and resume from the named state; that is the test for whether the state is complete

**Lesson:** Two procedures compute the same function by the same multiplications in the same order, and differ in something that no reading of their outputs would reveal. One carries a running result and a counter, and those variables are the entire state: halt it between any two steps, write down the variables, and the computation can be resumed later by handing them back. The other builds a chain of deferred operations, and its variables do not describe where it is — the position in that chain lives in machinery the program cannot see, and the longer the chain grows the more of that invisible state exists.

The test is the useful artifact here, because it is concrete and can be applied to anything. Ask what you would have to write down to stop the computation now and resume it elsewhere. Whatever you must write down is the real state. If the honest answer includes "and wherever the runtime had got to," then your named variables are a partial description and the remainder is being held somewhere you do not control.

This matters far outside recursion. Anything you want to checkpoint, migrate, retry, or resume after a crash faces exactly this question, and the usual failure is discovering at the worst moment that the process's position was implicit in a call stack, a cursor, or a partially consumed iterator — none of which appear in the data model. A design that keeps its state in a fixed set of named variables with a rule for updating them can be stopped and restarted for free; one that accumulates pending work cannot, no matter how the code is arranged.

The second half is that this property is invisible in the source. A definition that mentions itself may still generate the resumable shape, and the way to tell is not to read the text but to ask what accumulates as it runs — which is why the question has to be posed about the process rather than about the procedure.

**Source:** [Structure and Interpretation of Computer Programs](../works/structure-and-interpretation-of-computer-programs.md) — chapter 1 section 1.2.1's contrast between the recursive and iterative processes for factorial, which notes that in the iterative case the program variables provide a complete description of the state, so stopping between steps requires only supplying the interpreter with three values to resume, while the recursive process carries additional hidden information maintained by the interpreter indicating where it is in the chain of deferred operations, growing with the chain's length.
