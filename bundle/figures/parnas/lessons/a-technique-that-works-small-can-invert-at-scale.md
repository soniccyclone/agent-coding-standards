---
type: lesson
title: "A discipline validated on small examples can invert at scale, and the fix is the missing piece, not the retreat"
figure: parnas
works: [the-modular-structure-of-complex-systems]
axes: [cognitive-load, primitive-count]
subdomains: [software-engineering-and-architecture, operating-systems-and-systems-programming]
tags: [lesson]
---
# A discipline validated on small examples can invert at scale, and the fix is the missing piece, not the retreat

**Lesson:** Concealing each volatile decision inside its own part is supposed to
reduce what a maintainer must know. Carry it out honestly on a real system and the
part count does not stay at a dozen — it reaches hundreds, because the criterion
keeps subdividing wherever two things can change independently. At that size the
guarantee reverses. Every maintainer is now, by construction, ignorant of the
inside of nearly everything, and the question "which part must I change?" has no
cheap answer: they must hunt through many descriptions to find the few that matter.
Worse, the designers lose the ability to convince themselves the decomposition is
even complete, since nothing short of exhaustive inspection would reveal that a
whole responsibility was never assigned to anyone. A technique whose entire
justification is bounded understanding has produced unbounded search.

The instructive part is what this does *not* imply. The response is not that
hiding was academic idealism, nor that a looser structure would have been wiser.
The property is real; what was missing was a companion artifact the small examples
never needed — a map, organized as a hierarchy, whose sole job is to route a reader
with a specific concern to the part that owns it without reading anything
irrelevant. That artifact answers a different question from any component's own
description, and conflating the two is why it was absent for so long: knowing how
to use a part and knowing where a given concern lives are separate needs that
demand separate documents. Notably, this map is the one thing everybody reads,
which is precisely why it has to stay small enough that letting everybody read it
is affordable.

The general habit this teaches is to distrust any practice whose demonstrations
are all small, not because the practice is wrong but because the demonstrations
cannot exhibit its scaling costs. Toy examples are silent about exactly the
expenses that dominate later, and the expenses are usually not in the mechanism
but in the navigation and completeness arguments around it. So when a principle
you believe in starts producing pain at scale, the diagnostic question is which
supporting artifact the small cases let you do without — and the way to find out
in advance is to apply the idea to a genuinely constrained real system whose
existing solution is already considered good, so that anything you learn cannot be
credited to a weak comparison.

**Source:** [The Modular Structure of Complex Systems](../works/the-modular-structure-of-complex-systems.md)
— the account of hiding "backfiring" once the A-7E decomposition grew past a couple
of dozen parts, the resulting introduction of the module guide, and the framing in
the introduction of why the team deliberately re-built a well-regarded existing
flight program rather than a tractable example.
