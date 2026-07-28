---
type: lesson
title: "An idea about how to structure programs is untested until something forces people to use it"
figure: liskov
works: [the-power-of-abstraction]
axes: [expressiveness, verifiability, cognitive-load]
subdomains: [programming-languages-and-semantics, software-engineering-and-architecture, programming-environments-and-object-systems]
tags: [lesson]
---
# An idea about how to structure programs is untested until something forces people to use it

**Lesson:** A methodology stated in prose can be entirely convincing on its worked example and useless everywhere else. The failure mode is specific and common: the reader agrees with the principle, agrees the example demonstrates it, and then has no idea how to proceed on the program actually in front of them. The prose conveyed the conclusion without conveying the procedure, and there is no way to discover that from inside the prose. So the real test of an idea about structure is to build something that makes people do it — a mechanism, a construct, a tool that only permits the structured way — and then use it on real problems.

Embodiment tests three things that argument cannot. Whether the idea is usable at all, since if it is missing something you hit the gap immediately as an inability to express what you need, which also tells you exactly what expressive power the idea requires to be practical. Whether the idea is actually well defined, since building it forces every hand-wave to become a decision; a description that seemed complete turns out to have unspecified corners that no amount of re-reading would have revealed. And whether it is affordable, since a structuring discipline that cannot be implemented at acceptable cost will simply be abandoned in the situations that matter most.

There is a corollary about who the artifact should speak to. The point of embodying the idea is communication with the people who will apply it, and they think in whatever medium they work in. An idea delivered in the medium practitioners already inhabit reaches them; the same idea delivered as an exhortation does not. And the exercise generalizes past language design, because designing any interface poses the identical question — how much expressive power, at what cost in simplicity, performance, and ease of use — which is why practice at one transfers directly to the other.

A programmer who believes this stops trying to establish a convention by writing it down and starts asking what would make the wrong way inexpressible or the right way the easy path. When they cannot build such a thing, they treat the convention as unvalidated rather than merely unadopted. And when a principle survives contact with real use, they take the friction points seriously: those are the places where the idea was incomplete, not where the users were careless.

**Source:** [The Power of Abstraction](../works/the-power-of-abstraction.md) — the account of why the earlier methodology papers, though persuasive, left readers unable to apply the ideas to their own programs, and the stated rationale for building a language: to communicate in the medium practitioners use, to discover whether the idea works and what expressive power it needs, to force precise definitions, and to confront cost.
