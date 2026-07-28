---
type: lesson
title: "A requirement that nothing bad happens cannot be tested into existence"
figure: saltzer
works: [the-protection-of-information-in-computer-systems]
axes: [verifiability, primitive-count, cognitive-load]
subdomains: [operating-systems-and-systems-programming, software-engineering-and-architecture, formal-methods-and-verification]
tags: [lesson]
---
# A requirement that nothing bad happens cannot be tested into existence

**Lesson:** Requirements come in two shapes and the difference is not stylistic.
A positive requirement names behavior that must occur, so you can exhibit it, and
each exhibition is evidence. A negative requirement — no unauthorized access, no
corruption, no path that shouldn't exist — names the absence of behavior over an
unbounded space of attempts, and no number of exhibitions is evidence of anything.
Sampling tells you almost nothing, because the paths you need to know about are
exactly the paths normal operation never travels. Bugs in that region do not
announce themselves through use; they sit undisturbed until someone looks for them
on purpose.

The consequence is that for negatively specified properties you have to shift your
whole confidence strategy from exercise to examination. And the moment examination
becomes the primary method, size stops being a matter of taste and becomes the
binding constraint, because examination scales terribly. Code you can read line by
line can be believed; code you cannot finish reading cannot, no matter how careful
its author was. This is why the demand for a small, plain design in this territory
is not aesthetic minimalism but a precondition for having any grounds for belief at
all. It also explains why a property of this kind gets destroyed by being tangled
into a large body of unrelated function: the property still holds or fails
somewhere in there, but nobody can any longer say which.

There is a second consequence about hardware and infrastructure that fails the same
way. A component whose only job is to refuse things can break without any visible
symptom, since a broken refuser looks exactly like a component that had nothing to
refuse. Anything whose correct behavior is invisible during normal operation needs
some deliberate, independent means of being shown to still work, because time and
use will not reveal its failure the way they reveal the failure of a component that
does something.

A programmer who takes this seriously classifies each requirement by shape before
choosing how to gain confidence in it. Positive ones get tests. Negative ones get a
budget for smallness, a single chokepoint through which the relevant operations must
pass, and periodic direct inspection — and they get defended against the pressure to
grow, because every addition to the region is an addition to what has to be read.

**Source:** [The Protection of Information in Computer Systems](../works/the-protection-of-information-in-computer-systems.md)
— Section I's framing of security as a negative kind of requirement, the economy-of-
mechanism and complete-mediation principles derived from it, and the later
observations in Section III about certification difficulty and about access-checking
hardware whose failure can go unnoticed indefinitely.
