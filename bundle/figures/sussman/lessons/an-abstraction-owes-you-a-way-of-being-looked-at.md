---
type: lesson
title: "An abstraction is unfinished until it supplies its own way of being looked at"
figure: sussman
works: [structure-and-interpretation-of-computer-programs]
axes: [cognitive-load, verifiability]
subdomains: [software-engineering-and-architecture, programming-environments-and-object-systems]
tags: [lesson]
---
# An abstraction is unfinished until it supplies its own way of being looked at

**Lesson:** The chapter's queue is correct, and the first person to try it at the prompt concludes it is broken. Items appear twice; the queue looks non-empty after everything has been deleted. Nothing is wrong with the code. What he is seeing is the generic printer rendering the internal representation — a structure holding two pointers into one shared chain, so the shared parts appear more than once and the abandoned parts still appear. The correct fix is not to the queue but to supply a printing procedure for queues.

The reusable observation is that a debugging view is a representation like any other, and the default one belongs to the layer underneath. Every general-purpose inspector — a REPL printer, a struct dumper, a debugger's variable pane, a JSON serializer, a logging formatter — shows you the concrete structure, because that is the only thing it knows how to walk. Everywhere the abstraction differs from its representation, and that is precisely where abstractions are interesting, the default view will show something misleading rather than something incomplete. Sharing shows up as duplication, cyclic structure hangs the printer, a lazily computed field shows a thunk, an encapsulated cache appears as unexplained garbage. The tool is not broken and neither is the code.

The consequence is a design obligation people rarely put on the list: an interface consisting of a constructor, selectors and mutators is not complete, because it gives no way to observe the object *as what it is*. Adding one is cheap and it changes the economics of every hour subsequently spent debugging, because it removes an entire category of false alarm and the fruitless investigation that follows. The absence is self-concealing — you only find out you needed it while chasing a bug that does not exist, at which point you are least able to tell that the tool is the problem.

There is a sharper version of the point for anyone building an abstraction on a substrate that already has good tooling. The better the default inspector, the more convincing its misleading output, and the longer people will trust it before suspecting the view rather than the value. So the rule is not "add a printer when the structure is complicated." It is: whenever the abstract shape of a thing differs from its concrete shape, decide who is responsible for showing it, and make that a deliverable of the abstraction rather than something each debugging session rediscovers.

**Source:** [Structure and Interpretation of Computer Programs](../works/structure-and-interpretation-of-computer-programs.md) - Exercise 3.21 in chapter 3 section 3.3.2, in which a user tries the queue implementation, sees the last inserted item apparently duplicated in the printed result and the queue apparently non-empty after all deletions, and concludes it is all wrong; the reply is that the items are not going in twice but that the standard printer does not know how to make sense of the queue representation, and that seeing the queue printed correctly requires defining a print procedure for queues — the exercise asking the reader to explain the printed results and write that procedure; together with the footnote to Exercise 3.23 warning not to make the interpreter try to print a structure containing cycles.
