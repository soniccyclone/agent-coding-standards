---
type: lesson
title: "Turn what-happens-next into an ordinary value, and the special control constructs collapse into one"
figure: reynolds
works: [the-discoveries-of-continuations]
axes: [primitive-count, expressiveness, hardware-affinity]
subdomains: [programming-languages-and-semantics, foundations-of-computation]
tags: [lesson]
---
# Turn what-happens-next into an ordinary value, and the special control constructs collapse into one

**Lesson:** A program's pending future is normally implicit — held in a return address, a stack of frames, the position of an instruction pointer — and every control feature that has to manipulate it gets its own special-purpose machinery: one mechanism for returning, another for jumping out of a nested construct, another for the ordering constraints of argument evaluation, another for propagating a failure past several layers of caller. Make the pending future an ordinary value that gets passed like any other argument and those mechanisms stop being separate. A destination to jump to and a place to return to become the same kind of thing; a construct that abandons its surroundings is just one that ignores the future it was handed; evaluation order becomes visible in the text rather than buried in a convention. The general form of the move is to take the part of the machine state that your constructs implicitly consult and promote it to a first-class argument.

The consequence that surprises people is what happens to the mechanism you thought was expensive. The objection raised when this was first proposed was that turning every jump into a call means keeping the entire history of the computation alive. The answer is that the cost of a call comes almost entirely from arranging for it to return, and after the transformation nothing ever returns — each procedure hands control onward before it ends, so control reaching any ending at all means the whole program is done. Strip out the return machinery and a call costs exactly what a jump costs. Whenever an operation seems too expensive to use uniformly, check whether the expense belongs to a capability the uniform version no longer needs.

The honest counterweight is that a transformation of this kind relocates cost, never abolishes it. Rewriting a program this way does make every allocation obey a discipline where storage for a procedure can be released the moment it exits — but only because no procedure exits until the end, so the storage grows monotonically for the whole run and a conventional stack-based implementation is exhausted quickly. The reasoning gain is real and so is the resource consequence, and both have to be stated. A programmer evaluating any "this construct is unnecessary, here is the translation" result should ask the same question: which resource now absorbs what the eliminated construct used to manage, and is that resource one the target machine actually has in quantity?

**Source:** [The Discoveries of Continuations](../works/the-discoveries-of-continuations.md) — the background section on labels needing environments and on return addresses being treatable as ordinary parameters; the transcribed exchange with McIlroy in which the objection about maintaining the whole computation history is answered by observing that no procedure ever returns; and the accounts of Fischer's stack-discipline result and of J. H. Morris's note that the transformed program exhausts a conventional stack.
