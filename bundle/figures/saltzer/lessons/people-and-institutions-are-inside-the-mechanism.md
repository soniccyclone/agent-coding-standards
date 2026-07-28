---
type: lesson
title: "People and institutions are inside the mechanism"
figure: saltzer
works: [the-protection-of-information-in-computer-systems]
axes: [cognitive-load, expressiveness]
subdomains: [operating-systems-and-systems-programming, software-engineering-and-architecture]
tags: [lesson]
---
# People and institutions are inside the mechanism

**Lesson:** A control that is correct but hard to state correctly does not produce
correct systems, because the person operating it has to translate their actual intent
into the notation the mechanism accepts, and every translation is a chance to express
something other than what was meant. When the notation is far from how the operator
thinks about the problem, the mistakes are not occasional — they are the normal case,
and they are invisible, because a wrong-but-well-formed specification looks exactly
like a right one. So the distance between the operator's mental model and the
mechanism's vocabulary is a real defect metric, not a usability nicety. Setting the
entries in a permission structure is programming, and it is programming done by people
who did not sign up to be programmers, with no tests and no feedback.

The same reasoning applies one level up, to the organizational structure a mechanism
is supposed to encode. Every real institution has authority that can override, because
people fall ill and emergencies happen, so any design that omits an override is a
design that will be worked around. But real institutions also never grant bare
override — they pair it with something that slows it down and makes it visible: a
second signer, a waiting period, a logged justification, an external authorization.
A model that reproduces the authority and drops the friction has not modeled the
organization; it has modeled the organization's org chart while removing precisely the
part that made concentrated authority tolerable. Designing the moderation on a
privileged path is as much a part of the job as designing the path.

What this asks of a programmer is to treat the humans and the surrounding organization
as components with properties, rather than as an environment to be assumed away. That
means choosing notations that let people say the thing they actually mean; expecting
that the default configuration is what most deployments will run forever, so the
default is a design decision and not a placeholder; and for every escalation path,
deciding what accompanies its use. Skipping this is how systems end up with an
impeccable enforcement core, a set of permissions nobody understands, and an
administrator account that everyone shares.

**Source:** [The Protection of Information in Computer Systems](../works/the-protection-of-information-in-computer-systems.md)
— the psychological-acceptability principle in Section I and the closing remarks
comparing configuring a protection architecture to programming one, together with
Section II's discussion of hierarchical control, its concentration of unchecked
authority, and the proposed prescript mechanism that attaches delays, logging, or
second parties to an exercise of that authority.
