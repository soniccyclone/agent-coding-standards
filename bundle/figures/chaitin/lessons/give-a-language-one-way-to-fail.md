---
type: lesson
title: "If your program must run other people's programs, give the language exactly one way to fail"
figure: chaitin
works: [the-limits-of-mathematics, algorithmic-information-theory]
axes: [primitive-count, cognitive-load, verifiability]
subdomains: [programming-languages-and-semantics, operating-systems-and-systems-programming]
tags: [lesson]
---
# If your program must run other people's programs, give the language exactly one way to fail

**Lesson:** Chaitin's whole enterprise requires a host that runs arbitrary programs, including programs produced by tossing a coin, and keeps going. That requirement drove the design of his language backwards from the host's needs. He made the semantics deliberately permissive: taking the head or tail of something that is not a list yields that thing back, an unbound name evaluates to itself, and so on down the primitive set, until the only remaining way for a syntactically well-formed expression to lack a value is to run forever. One failure mode. The host then wraps evaluation in a bounded attempt that returns a flag saying which of the two boundaries was hit, along with whatever the guest emitted along the way.

The reasoning generalises past interpreters. Every distinct failure mode at an interface is a case that every consumer must handle, and the consumer whose burden matters most is the one that has to accept input it did not write. Adding an error condition looks like diligence at the point where it is raised and looks like a tax at every one of the places that must now branch on it. Collapsing failure into a single channel with a single meaning is what lets the supervising layer be small enough to trust, which is the same trade an operating system makes when it gives a task a slice of time and declines to die when the task misbehaves.

There is a cost, and it is worth naming: permissive semantics turn some mistakes into silently strange values instead of loud errors. Chaitin accepts that because his guests are garbage by construction and there is no author to inform. When a real author exists, the balance shifts. The transferable part is the discipline of asking who consumes each failure mode and whether a new one earns the branch it forces on everyone downstream, rather than treating every additional error case as free rigour.

**Source:** [The Limits of Mathematics](../works/the-limits-of-mathematics.md) - the introduction to the language chapter, which states that the only way an expression can fail is by looping, and gives the reason as needing to run garbage safely. The design constraints are enumerated in the introduction to [Algorithmic Information Theory](../works/algorithmic-information-theory.md), where the requirement for a time-limited evaluator that never loses control is compared to a supervisor granting a slice of processor time to an untrusted task.
