---
type: lesson
title: "Find the assumption too basic to be stated, negate it, and follow the consequences — that is where new models come from"
figure: sussman
works: [the-art-of-the-propagator]
axes: [expressiveness, cognitive-load]
subdomains: [programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# Find the assumption too basic to be stated, negate it, and follow the consequences — that is where new models come from

**Lesson:** The productive assumptions to attack are not the controversial ones; they are the ones so pervasive that no design document mentions them, because everybody's design obeys them and nobody noticed choosing. Consider the rule that each place holding a value — a variable, a field of a record, the anonymous slot holding an intermediate result — receives that value from exactly one producer. It is not a feature anyone argued for, it is closer to a definition, and it is nowhere written down. Suspend it and ask what a system would have to look like if a place could receive contributions from many producers at once, and a cascade of consequences follows immediately: no individual producer needs to compute a whole value any more, so partial knowledge becomes a first-class thing to send; a fragment that arrives early can be useful to a consumer, and can even be what lets another producer deduce the refinement; and you no longer have to decide in advance which computation will be the one that supplies a given place, so the direction information travels can depend on how the system is used rather than on how it was written.

The method has a second half that is easy to skip. Negating a hidden assumption creates an obligation you did not have before, and the design's real content moves into discharging it. Here, once a place can hear from several sources, someone must say what it means to combine what they say — which is a question that simply had no referent while the one-source rule held, since with one source there is nothing to combine. Working out that obligation honestly is the work; the negation itself takes a sentence. A negation whose obligation you leave vague produces a system that is exciting in the abstract and ill-defined at every point where the old assumption used to be doing silent work.

The habit generalizes. For any system you are looking at, try to list the propositions so obvious that they would sound strange said out loud, then take each one and ask what would be gained, and what would have to be defined, if it were false. Most such experiments dead-end quickly, which costs nothing. The ones that do not dead-end tend to be reachable no other way, because incremental improvement of a design cannot find them: every step of an incremental process preserves the assumption, and the assumption was the whole constraint.

**Source:** [The Art of the Propagator](../works/the-art-of-the-propagator.md) — the introduction, which observes that conventional languages let the value in a place come from only one source, notes deliberately that this is nearly axiomatic rather than argued for, asks what happens if the restriction is relaxed, and derives from the relaxation that producers need no longer compute complete values, that partial knowledge becomes useful and refinable by later sources, and that the choice of which computation supplies a place need not be made in advance.
