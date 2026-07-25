---
type: lesson
title: "Build a base with no strategy in it, and make every policy an ordinary program above it"
figure: brinch-hansen
works: [rc-4000-software-multiprogramming-system, the-nucleus-of-a-multiprogramming-system, operating-system-principles]
axes: [primitive-count, expressiveness, cognitive-load]
subdomains: [operating-systems-and-systems-programming, software-engineering-and-architecture]
tags: [lesson]
---
# Build a base with no strategy in it, and make every policy an ordinary program above it

**Lesson:** The usual way to specify a foundational layer is to ask which services its users will need, and the answer bakes a working assumption about mode of use into the deepest code in the system. Everything above then depends on that assumption, so the layer cannot be changed and cannot be replaced, and the only remaining options are to fight it or to rewrite the world above it. The productive reframing is to ask a different question entirely: not what functions the base should perform, but what set of mechanisms would let anyone build the function they want, in an orderly way, without touching the base at all. Strategy is then not a foundational concern but ordinary application code, written in whatever language you like, replaceable while the system runs, and capable of coexisting with rival strategies at the same time.

Holding that line demands unusual discipline about what counts as a mechanism. Deciding what a process *is*, how two of them exchange information, and how one comes into existence and goes away are questions with defensible answers independent of any usage pattern. Choosing who runs next, how much store anyone gets, and what happens when a resource is scarce are not; every answer to those encodes a bet on the installation. The base gets the first list and refuses the second. Where an arbitration rule is genuinely unavoidable at the bottom, it should be the dullest one available, and the layer above must be given the means to override it — a built-in policy that cannot be escaped is the same trap in miniature.

Two consequences are easy to miss. First, the discipline buys structural freedom rather than functionality: the same small base underneath batch work, interactive sessions, and deadline-driven control means those regimes stop being different systems and become different programs. Second, and honestly acknowledged in the RC 4000 report itself, a base with no strategy delivers no service on its own. Its generality is exactly its weakness, and its value is entirely contingent on what gets built above it. Anyone applying this thinking should expect to be judged not on the elegance of the base but on the range of useful systems that turn out to be cheap to write against it.

**Source:** [RC 4000 Software Multiprogramming System](../works/rc-4000-software-multiprogramming-system.md) — the opening chapter on system objectives, which argues that the design problem is extensibility rather than function, and the later chapters on resource control and system possibilities, which show batch, time-sharing, and real-time regimes as programs rather than variants. Also [The Nucleus of a Multiprogramming System](../works/the-nucleus-of-a-multiprogramming-system.md) — the condensed statement of the same argument, plus the process-hierarchy section where control and allocation rules are deliberately kept separate from time-sharing. Also [Operating System Principles](../works/operating-system-principles.md) — the RC 4000 case study that closes the book.
