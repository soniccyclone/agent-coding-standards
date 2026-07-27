---
type: lesson
title: "Look for the one primitive that closes an entire design space instead of solving instances of it"
figure: herlihy
works: [wait-free-synchronization]
axes: [primitive-count, expressiveness, hardware-affinity]
subdomains: [distributed-systems-and-concurrency, algorithms-and-complexity]
tags: [lesson]
---

# Look for the one primitive that closes an entire design space instead of solving instances of it

**Lesson:** When a class of problems is being attacked one instance at a time — a hand-built concurrent queue, then a concurrent set, then a concurrent counter, each a small publishable feat — the productive move is to stop producing instances and ask what single capability would settle all of them at once. Here the answer is stark: any primitive strong enough to bring the participants to agreement is strong enough to implement every object they could want, and any primitive too weak to do that is too weak to implement anything above its own class. There is no middle ground and no partial credit. That converts an open-ended catalogue of engineering problems into a single yes-or-no question about the platform.

The proof of the strong direction is itself the lesson about how to think. Rather than reasoning about the object's state, represent the object as the sequence of operations that have been agreed upon, and let each participant's job be to get its own operation appended to that sequence. Agreement is then used only for the one thing agreement is for — deciding what comes next — and the object's actual semantics are supplied separately, as a pure relation from an operation and a prior state to a new state and a result. Concurrency and semantics are cleanly separated: the mechanism never inspects what the operation means. This is why the construction is general rather than clever. It also shows the characteristic move that makes it robust to slow participants: a participant appends not only its own pending operation but, in turn, some other participant's, so that being stalled or descheduled does not prevent your operation from being carried out by someone else. Cooperation is designed in, and removing it is exactly what degrades the guarantee from per-participant to system-wide.

The practical reading for a programmer is a sharp question to ask of any platform: is there a single primitive here that is sufficient for everything, and if not, which class of things is permanently out of reach? A language, runtime, or instruction set either supplies such a primitive or it does not, and the answer determines what can ever be built on it — not what is currently convenient. The generic construction's costs are real and its authors say so plainly, in memory quadratic and cubic in the participant count and in time bounds nobody would ship as-is; that is an argument for specialized implementations of hot structures, not an argument against knowing the closure result. Knowing the space is closed tells you that every specialized construction is an optimization rather than a discovery, and that time spent proving no hand-built solution exists is time wasted.

**Source:** [Wait-Free Synchronization](../works/wait-free-synchronization.md) — the universality section, in which sufficiency of an agreement-capable primitive is established by representing the object as an agreed-upon operation list with semantics factored out into a separate relation, together with the helping step whose omission weakens the progress guarantee, and the frankly stated space and time costs.
