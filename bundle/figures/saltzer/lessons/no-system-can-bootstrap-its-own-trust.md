---
type: lesson
title: "No system can bootstrap its own trust"
figure: saltzer
works: [the-protection-of-information-in-computer-systems]
axes: [verifiability, cognitive-load]
subdomains: [operating-systems-and-systems-programming, distributed-systems-and-concurrency, software-engineering-and-architecture]
tags: [lesson]
---
# No system can bootstrap its own trust

**Lesson:** Trace any authorization back through the steps that produced it and you
eventually leave the machine. Someone decided that a particular name inside the system
corresponds to a particular party outside it, and that decision was made on evidence
the system did not generate and cannot check. This is not a gap in a particular design;
it is structural. For one party to grant another access, the grantor must already
possess the grantee's internal identifier, and must have obtained it through a channel
the system does not mediate. The mechanism can enforce a binding faithfully forever
after; it cannot originate the binding, because the very thing being bound is a fact
about the world.

Seeing this changes how you evaluate a security story. The interesting question is
never whether the internal enforcement is sound — that part is usually the best
understood piece — but where the chain leaves the mechanism and what is holding it up
out there. A protocol can be flawless and still rest on an out-of-band step that was
never designed: a name shouted down a hallway, an email, an onboarding spreadsheet, a
support agent's judgment about a caller. That step is part of the system whether it
appears in the diagram or not, and it is usually the cheapest thing to attack. The
same reasoning exposes one-sided authentication as an unfinished design, since a
scheme that lets the machine verify the human but not the reverse leaves the human
with no way to know they are talking to the real thing.

The practical discipline is to insist on drawing the boundary honestly and then
looking just past it. Write down, for each identity your system relies on, the
external event that established it and who is accountable for that event. Doing this
tends to produce two useful surprises: some bindings turn out to rest on nothing in
particular, and some elaborate internal machinery turns out to be defending a
perimeter that is wide open a step earlier. The corollary for how identities are
modeled is that the internal name must stay tied to something that can be held
accountable — a scheme where tokens circulate freely and nobody can say who is behind
a given action has kept the enforcement and thrown away the reason enforcement mattered.

**Source:** [The Protection of Information in Computer Systems](../works/the-protection-of-information-in-computer-systems.md)
— the dynamic-authorization-of-sharing analysis in Section II, which derives a
symmetric protocol requiring prior communication outside the system by both grantor and
grantee, together with Section I's treatment of authentication, masquerading, and the
principal as the unit of accountability.
