---
type: lesson
title: "A design idea impossible to express in one substrate can be the native vocabulary of another"
figure: reenskaug
works: [working-with-objects-the-ooram-software-engineering-method]
axes: [expressiveness, primitive-count]
subdomains: [programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# A design idea impossible to express in one substrate can be the native vocabulary of another

**Lesson:** One design commitment runs through this whole method: what a participant may be *asked* depends on who is asking. The same component exposes one set of permitted messages to one collaborator and a different set to another, so authority lives in the relationship rather than in the component. Attempts to encode that in a general-purpose language's type system collapsed — typing each connection with its own interface produced an explosion of declarations and then broke outright, because a component referenced from two contexts needing different capabilities cannot satisfy both constraints at once, and passing it as a parameter yields a type error no widening repairs.

Now express the same idea in a distributed-object interface language and it is not merely possible, it is idiomatic. You declare a separate interface per collaborator — the station as seen by the panel, as seen by the door, as seen by the central unit, as seen by the timer — and then declare the component as supporting all of them. One object, several interfaces, which is exactly what those systems were built to express because they were designed around a strict separation of interface from implementation. The construct that was a fight in one substrate is the default in another.

The lesson is not that one of these substrates is better. It is that whether a design idea is expressible is a property of the *pair* — idea and substrate — not of the idea, and that discovering this is cheap if you look early and expensive if you look late. When something you are confident about turns into a war with your tools, the productive question is which substrate treats it as ordinary, because it very likely exists. And the same reasoning constrains portability in a useful way: a design survives a change of target only through the properties its targets share. This one travelled to five very different destinations because every one of them separates interface from implementation — and the one concept that failed to travel cleanly was a connection-with-identity, which had a natural equivalent in one interface language and simply no counterpart in another.

**Source:** [Working With Objects: The OOram Software Engineering Method](../works/working-with-objects-the-ooram-software-engineering-method.md) — chapter 8's mapping of role-model concepts onto CORBA IDL and Microsoft IDL, where per-collaborator interfaces for LocalStation are declared separately and combined, the accompanying note that supporting several interfaces per object is a common feature of both, and the concept table showing port mapping to an interface reference in one IDL and to nothing in the other; read against chapter 4's boxed account of the failed attempt to encode the same per-port interfaces in Eiffel's type system.
