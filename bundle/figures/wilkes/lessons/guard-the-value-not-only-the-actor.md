---
type: lesson
title: "To control an operation, guard the values it accepts instead of the actors allowed to perform it"
figure: wilkes
works: [cambridge-cap-computer-and-its-operating-system]
axes: [verifiability, primitive-count, expressiveness]
subdomains: [operating-systems-and-systems-programming, software-engineering-and-architecture]
tags: [lesson]
---
# To control an operation, guard the values it accepts instead of the actors allowed to perform it

**Lesson:** There are two independent ways to prevent an operation from being misused. You can restrict who is permitted to invoke it, which requires a notion of privileged status and a body of code trusted to hold that status. Or you can leave the operation entirely unrestricted and instead control the set of values it can be given, so that anyone may perform it but nobody can supply an input that would do damage. Either discipline suffices on its own; applying both is redundant. The choice between them is the most consequential structural decision in the design, because it determines whether a trusted, mode-switching core has to exist at all.

The second route buys something the first cannot. When authority lives in unforgeable values rather than in a caller's status, authority becomes a thing that can be held, passed, narrowed and stored like any other datum, and the question "what can this code reach" becomes answerable by looking at what values it holds rather than by tracing which mode it runs in. It also dissolves a problem the first route creates: with status-based control, facilities available to the writer of the core cannot be offered to the writer of a subsystem without letting that subsystem into the core, whereas value-based authority is handed out to arbitrary depth without any of its holders being distinguished. Nothing needs to be built to support delegation; delegation is what the mechanism already is.

The price is that unforgeability must be absolute and must be enforced by something. Somewhere there has to be an operation that manufactures authority from nothing, and it has to be the one thing that cannot be reached generally — so the design does not eliminate trust, it concentrates all of it into a single point whose whole job is minting. That is a far better place to be than diffuse privilege, because a single minting point can be inspected exhaustively, and because everything outside it can be reasoned about without asking what mode it is in.

**Source:** [The Cambridge CAP Computer and Its Operating System](../works/cambridge-cap-computer-and-its-operating-system.md) — Chapter 1's contrast between privileged-mode systems, where loading the addressing registers is restricted, and the alternative where the loading operation is unprivileged but the bit patterns that may enter those registers are strictly controlled, together with the observation that either precaution rigorously enforced is sufficient alone, and the discussion of why subsystem writers can be given the same facilities as system writers under the second scheme.
