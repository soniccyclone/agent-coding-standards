---
type: lesson
title: "Judge a change by the exceptions it adds to the design's rules, not by whether it works"
figure: parnas
works: [software-aging]
axes: [cognitive-load, primitive-count]
subdomains: [software-engineering-and-architecture]
tags: [lesson]
---
# Judge a change by the exceptions it adds to the design's rules, not by whether it works

**Lesson:** A large program is navigable only because it rests on a small
organizing idea. That idea is what lets a maintainer predict where the code
handling some concern must live, and what lets them believe the interfaces they
find are the interfaces that were intended. It is not written in the source; it is
the thing the source was arranged to express. Someone who does not hold that idea
can still make a change that passes every test, ships, and satisfies the customer,
while making the system permanently more expensive to understand — because the
change is placed where a person without the idea would naturally put it, which is
precisely where the idea says it does not belong.

The damage compounds in a specific and measurable way: after such a change, you
can no longer understand the system by knowing its rules. You must know the rules
*and* the accumulated list of places where the rules were violated. That list only
grows, and each entry is something no document explains and no reasoning can
reconstruct — you learn it by being burned. Run this forward far enough and you
reach the state Parnas identifies as the terminal one: the original designers no
longer understand the system, because it is no longer the system they designed,
and the people who changed it never understood it in the first place. Nobody
holds the whole thing. There was no moment when anyone did anything obviously
wrong.

So the review question for a change is not "does it work" or even "is it clean,"
but "does it leave the number of independent things a maintainer must hold where
it was?" A programmer who believes this treats a change that fits the existing
organizing idea and a change that quietly contradicts it as different in kind, not
degree, even when their diffs are the same size and both pass. It also explains
why cost control here is not a management activity: no amount of tracking,
approval, or process catches a change that is locally correct and structurally
corrosive. Only someone who holds the design's intent can see it, which makes
protecting that intent a technical responsibility that has to be assigned to
somebody by name.

**Source:** [Software Aging](../works/software-aging.md) — the "ignorant surgery"
account of the second cause of aging, and the later argument that slowing
deterioration requires each change to be checked against the original designers'
intent rather than merely against the requirement that prompted it.
