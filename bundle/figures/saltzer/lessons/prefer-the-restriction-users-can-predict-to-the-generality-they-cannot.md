---
type: lesson
title: "Prefer the restriction users can predict to the generality they cannot"
figure: saltzer
works: [protection-and-the-control-of-information-sharing-in-multics]
axes: [expressiveness, cognitive-load, primitive-count]
subdomains: [operating-systems-and-systems-programming, software-engineering-and-architecture]
tags: [lesson]
---
# Prefer the restriction users can predict to the generality they cannot

**Lesson:** The default engineering instinct treats expressive power as free: if a
mechanism can express more configurations, it can serve more needs, and the ones
nobody wants simply go unused. That instinct is wrong wherever a wrong configuration
is silent. Added generality does not sit inertly — it enlarges the space of states a
person can reach by accident, and it forces them to hold more of the system in their
head to predict what any single change will do. When the cost of an unintended state
is discovered immediately, this trade is usually still worth it. When the cost is
discovered much later or never, the generality is a net loss even though every
individual feature in it was defensible.

The sharpest version of the argument shows up as a willingness to remove things. A
scheme where one shared specification applies to many objects is more flexible than
copying it into each object at creation time — and it was abandoned, because the
effect of editing the shared version differed per object and people got it wrong
constantly. An escape hatch letting arbitrary user code adjudicate each request is
maximally general — and it was abandoned, after the analysis showed how much
supporting structure it demanded and how it exposed its own users to new hazards. A
naming shortcut that also carried permissions was replaced by one that carries only a
name, because letting rights depend on which path you used to reach a thing produced
more mistakes than uses. In each case power was traded away for predictability
deliberately, after seeing real people use it.

There is a companion move that softens the trade instead of taking it: make the
mechanism resolve the common intent automatically rather than exposing the knob that
would let a user express it. Ordering conflicting rules by specificity, so that the
narrow case wins without anyone having to think about sequence, keeps the ordinary
outcome right without teaching everybody a precedence language. That is the general
shape — absorb the complexity into the mechanism's fixed behavior where the intent is
predictable, and refuse the general knob, leaving the genuinely unusual case to be
built explicitly by whoever needs it.

A programmer who thinks this way asks, of every configuration surface they design,
what a plausible misconfiguration looks like and how long it stays invisible. Where
the answer is "forever," they cut options rather than document them, and they treat
an existing feature's removal as an available move rather than a breach of contract.

**Source:** [Protection and the Control of Information Sharing in Multics](../works/protection-and-the-control-of-information-sharing-in-multics.md)
— the sequence of abandoned or rejected refinements (the shared access-specification
appendix, the trap extension, execute-only mode, permission-carrying links), the
automatic specificity ordering of list entries, and the paper's explicit conclusion
that the right direction is toward simpler and less general structures.
