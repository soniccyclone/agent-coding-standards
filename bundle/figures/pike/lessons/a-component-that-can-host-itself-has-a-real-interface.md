---
type: lesson
title: "A component that can host itself has a real interface"
figure: pike
works: [the-use-of-name-spaces-in-plan-9]
axes: [verifiability, expressiveness, cognitive-load]
subdomains: [operating-systems-and-systems-programming, distributed-systems-and-concurrency]
tags: [lesson]
---
# A component that can host itself has a real interface

There is a cheap and brutal test for whether a component's interface is honest:
can the component run as a client of itself? If a window system provides its
clients exactly the environment it was itself written against, it can be nested
inside one of its own windows. If it cannot, that failure is diagnostic — it
means the component consumes something privileged that it does not offer, and
that hidden asymmetry will surface later as an inability to test it, script it,
move it, or stack anything else on top of it.

The reason this test works is that self-hosting forces the interface to be
complete without letting the implementor decide what "complete" means. Any
capability the component quietly reaches around its own abstraction to obtain
becomes an immediate, visible failure rather than an undocumented assumption.
And the same property that permits recursion permits relocation: if a
component's entire contact with the world is a named set of ordinary resources,
then supplying those resources from somewhere else — another machine, a
measurement layer, a recording — is not a feature to be built but a consequence
already in hand. Remoting, interposition, and instrumentation all turn out to be
the same trick, which is why an encapsulating monitor can wrap a program and
account for every request it makes without the program's cooperation.

For a working programmer this converts a vague aesthetic ("clean layering") into
a concrete question you can answer in an afternoon: what would break if this
thing ran inside itself? The answer names your leaks precisely. It also argues
against the common shortcut of giving a component a privileged back channel "just
for now" — the back channel costs you nesting, remote operation, and testability
in one stroke, and the loss is invisible until you need one of them.

**Source:** [The Use of Name Spaces in Plan 9](../works/the-use-of-name-spaces-in-plan-9.md) — the window-system discussion, where providing clients the same conventional device files it was built on yields recursive execution, transparent remote display, and hosting a foreign window system as a client; and the encapsulating statistics-gathering monitor described alongside it.
