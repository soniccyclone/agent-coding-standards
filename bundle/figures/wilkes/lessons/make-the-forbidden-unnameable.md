---
type: lesson
title: "Prefer restrictions that make the forbidden thing unnameable over restrictions that merely catch the attempt"
figure: wilkes
works: [cambridge-cap-computer-and-its-operating-system]
axes: [verifiability, cognitive-load, expressiveness]
subdomains: [operating-systems-and-systems-programming, programming-languages-and-semantics]
tags: [lesson]
---
# Prefer restrictions that make the forbidden thing unnameable over restrictions that merely catch the attempt

**Lesson:** A restriction can be built in two fundamentally different places. It can act on naming, so that what is out of bounds has no valid designation at all and an attempt to refer to it is not a wrong action but a meaningless one — this is what lexical scope does, and the programmer who thinks he can reach an out-of-scope variable is simply mistaken about what he wrote. Or it can act on execution, so that the reference is perfectly well formed, denotes exactly what the programmer intended, and is stopped when it is attempted. Both prevent the access. Only the first eliminates the possibility of the error existing in the program.

The difference compounds in every downstream activity. With naming-based restriction, the question "what could this code touch" is answered by reading the code's vocabulary, and the answer is a finite list obtainable without running anything. With execution-based restriction the same question requires reasoning about every path, because any name in scope might denote something out of bounds on some path. The first gives you a static, enumerable account of reach; the second gives you a runtime alarm and the hope that testing exercised the path. And a naming-based scheme has a property that matters enormously in practice: reach can be described per region of code rather than per moment of execution, which is what makes it possible to audit a system's structure at all.

The corresponding design instruction is to look at each restriction you are enforcing and ask whether it could be moved from the moment of use back to the act of designation. Frequently it can, and the mechanism is to give the thing being restricted no global name, so that the only way to refer to it is through a reference that has to be handed to you. What began as an access rule becomes a fact about vocabulary, and the class of errors it was defending against stops being detectable-in-principle and becomes unwritable.

**Source:** [The Cambridge CAP Computer and Its Operating System](../works/cambridge-cap-computer-and-its-operating-system.md) — Chapter 1's distinction between thinking of memory protection in terms of addressing versus in terms of lockout, illustrated by the contrast between high-level-language scope rules and a global-variable situation where the programmer knows valid addresses for objects that will trap at run time.
