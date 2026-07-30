---
type: lesson
title: "Let a fixed core enforce distinctions whose meaning it cannot interpret"
figure: wilkes
works: [cambridge-cap-computer-and-its-operating-system]
axes: [primitive-count, expressiveness, verifiability]
subdomains: [operating-systems-and-systems-programming, programming-languages-and-semantics]
tags: [lesson]
---
# Let a fixed core enforce distinctions whose meaning it cannot interpret

**Lesson:** A core mechanism cannot know in advance the kinds of thing that will be built above it, and the usual conclusion — that it must therefore either be extended for each new kind or stay out of the way — is false. There is a third option: have the core manipulate opaque marks that stand for kinds, without any knowledge of what the kinds mean. It can then perform the operations that are identical across all kinds — creating, comparing, checking that an operation is being applied to something of the right kind — while remaining ignorant of every one of them. Authority to operate generically on a kind is itself represented as a value that must be presented, so the core's rule is purely mechanical: these marks match, or they do not.

The construction that makes this work is concealment: a thing of a new kind is built by taking the representation of an existing thing and sealing it under a fresh mark, producing something whose holders can pass it around and submit it to generic operations but cannot reach the representation inside. Only a holder of the corresponding kind-authority can open it. New kinds are then defined in terms of existing ones without limit, which is the layering principle applied to types rather than to procedures, and the core's size does not grow as the tower does. The reason this is a better answer than encoding each new kind as a component with its own code is that a sealed value remains a value — cheap to create, cheap to pass between activities, and usable in operations taking more than one of its kind, none of which is true when a kind is embodied as a running component.

The general form of the lesson is that enforcing a distinction and understanding a distinction are separable, and the separation is where extensibility comes from. Any place where a foundation seems to need knowledge of its clients' concepts is worth re-examining for whether it needs only to know that two concepts are different — a question answerable with tokens, matching, and refusal.

**Source:** [The Cambridge CAP Computer and Its Operating System](../works/cambridge-cap-computer-and-its-operating-system.md) — Appendix 1's type extension design, in which representations are sealed under type marks held in a central table, generic operations require presenting a capability for a type object whose only significance is to authorize them, new kinds are defined in terms of pre-existing ones following the general principle of levels of abstraction, and the microprogram carries out generic operations with no knowledge of the meaning of the objects; contrasted there with the earlier scheme where every abstract object had the same type and could not be passed cheaply between processes.
