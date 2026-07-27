---
type: lesson
title: "State a request's real requirements as data, because the code that could exploit them has not been written yet"
figure: rashid
works: [accent-a-communication-oriented-network-operating-system-kernel]
axes: [expressiveness, verifiability, hardware-affinity]
subdomains: [distributed-systems-and-concurrency, operating-systems-and-systems-programming]
tags: [lesson]
---
# State a request's real requirements as data, because the code that could exploit them has not been written yet

**Lesson:** Most systems bury what a caller actually needs inside the choice of which routine the caller invoked. Needing delivery guaranteed, or ordering preserved, or the request dropped if it goes stale, or the contents kept secret, shows up as a decision about which call to make and which flags to set at one particular layer — and then nothing further down or off to the side can see it. The consequence is that every component in the path must assume the strongest requirement, because the weaker ones were never stated. The alternative is to make the requirement part of the request itself: a piece of data traveling with the request, describing what the sender genuinely depends on, distinct from any particular implementation's way of providing it.

Two things become possible that were not possible before. First, components that were not part of the original design can act on the information. When a request carries "reliable delivery is not required" or "worthless after this much time," a relay standing between the endpoints — one nobody had in mind when the sender was written — can drop retransmissions, discard stale work, or choose a cheaper path, and it can do so without understanding anything about what the request means. Second, and more subtly, the declarations can be treated as permission rather than obligation. A component free to deliver something reliably that was only marked as best-effort can ignore every hint in the name of simplicity, and a debugging configuration can ignore all of them in the name of reproducibility, without any program becoming incorrect. That asymmetry is what makes the scheme safe to adopt: the hints strengthen what implementations may do and never what callers may assume.

The general principle underneath is that knowledge which exists only as control flow is knowledge the system cannot use. A condition encoded as "we took this branch" is available exactly once, at one place, to one piece of code; the same condition encoded as a value attached to the thing it describes is available to everything the thing subsequently touches, including code written years later by people with different concerns. This is also why it helps error detection and not just optimization: a stated requirement can be checked against actual behavior, whereas an implied one can only be violated silently.

A programmer who takes this seriously separates, at every interface, what the caller needs from how the callee currently provides it, and puts the former in the message. The discipline shows up as a slight excess of self-description that feels redundant at design time and repays itself the first time somebody needs to interpose on a path they do not control.

**Source:** [Accent: A Communication Oriented Network Operating System Kernel](../works/accent-a-communication-oriented-network-operating-system-kernel.md) — the design constraint calling for knowledge to be represented explicitly rather than embedded procedurally, realized in the message-type service classes (ordering, reliability, staleness, priority, secrecy) and the discussion of how relaying components read those classes while remaining free to treat them as advice.
