---
type: lesson
title: "Let a request escalate along the call chain until it meets enough authority, instead of asking who has it"
figure: wilkes
works: [cambridge-cap-computer-and-its-operating-system]
axes: [expressiveness, cognitive-load, verifiability]
subdomains: [operating-systems-and-systems-programming, software-engineering-and-architecture]
tags: [lesson]
---
# Let a request escalate along the call chain until it meets enough authority, instead of asking who has it

**Lesson:** When an action needs more authority than the code attempting it holds, the tempting design is a lookup: find out who can do this and route the request there. That requires a registry of who holds what, which has to be maintained, is a piece of global knowledge every component depends on, and is wrong whenever the real distribution of authority changes. The alternative is to let the attempt fail and hand the request back to the caller, who tries with their own authority, and so on outward until it reaches someone strong enough. No component needs to know anything about the distribution of authority; the chain of callers already encodes it, since a caller who granted you a narrower authority than their own is by construction closer to the power in question.

The same shape handles failures that a component cannot deal with locally. Rather than a central handler that must understand every possible failure, mark the point of failure and raise it in the caller, and if the caller cannot handle it either, raise it in *its* caller. The termination condition is structural — the outermost frame — and the escalation ordering falls out of the call structure rather than being configured. What makes such a scheme robust in practice is one specific precaution: the mechanism must detect that a failure occurred while an earlier failure was being handled, and skip past the frames already engaged, or the system will loop forever handling its own handling.

The general principle is to let an existing structure carry information rather than duplicating that information in a table. The call chain is already an ordering by decreasing specificity and, in a well-built system, increasing authority; a design that walks it needs no registry and stays correct as authority is redistributed. The cost is that the walk may take several steps and that each participant must be prepared to be asked something it cannot do — which is a much smaller obligation than keeping a map of the world accurate.

**Source:** [The Cambridge CAP Computer and Its Operating System](../works/cambridge-cap-computer-and-its-operating-system.md) — Chapter 3's handling of attentions, where a component whose permission is insufficient to reset one returns control to its caller, which attempts it in turn, until a component with a sufficiently powerful permission is reached; and the same chapter's fault handling, which marks the frame of the failing procedure, raises a fault in the caller when the procedure cannot handle it, and searches down the stack for an unmarked frame so that a fault occurring during fault handling bypasses the procedures already engaged.
