---
type: lesson
title: "Publish the list of what your system does not do well"
figure: saltzer
works: [protection-and-the-control-of-information-sharing-in-multics]
axes: [verifiability, cognitive-load]
subdomains: [software-engineering-and-architecture, operating-systems-and-systems-programming]
tags: [lesson]
---
# Publish the list of what your system does not do well

**Lesson:** Every serious system has a set of places its own builders know are thin,
and in most projects that set exists only as folklore in a few people's heads. The
reasons for keeping it there are real and worth naming plainly: the items are
embarrassing, they hand ammunition to critics, they may help someone attack a running
deployment, the list will be stale within months, and it is certainly incomplete
because its authors cannot see their own blind spots. Writing the list down anyway is
the more useful move, and the argument for it is not about honesty as a virtue. An
unwritten weakness cannot be prioritized, cannot be assigned, and cannot be
distinguished from an unknown one. Written down, it becomes a work queue and a record
of what the designers still consider in scope, which is information nobody else can
reconstruct.

Doing this well requires a distinction that gets collapsed all the time: between a
system that is *capable* of the property you want and a deployment that actually
*has* it. A design can be sound while the running installation is compromised by
physical access, unaudited operators, unvetted maintenance, or an administrator whose
account carries far more authority than their job needs. Those are not defects of the
design and they are not excuses either — they are a separate list, owned by whoever
operates the thing, and the design's job is to make correct operation easy rather than
to pretend it can enforce it. Similarly worth separating: a known weak area, where an
attacker is more likely to find something, from an actual exploitable defect. Conflating
them makes the list either alarmist or useless.

The habit this produces is a maintained, versioned document of known-weak areas with a
severity judgment and a reason for each, kept next to the design rather than in a
private channel — plus a companion note of what the design assumes about its operating
environment. That second document is the one most projects never write, and it is
what turns "we designed this to be safe" into a checkable claim about who has to do
what for the claim to hold.

**Source:** [Protection and the Control of Information Sharing in Multics](../works/protection-and-the-control-of-information-sharing-in-multics.md)
— the section enumerating known weaknesses, which opens by stating the reasons one is
reluctant to publish such a list and then does so anyway, and the concluding
distinction between a system designed to be securable and a site actually operated
securely.
