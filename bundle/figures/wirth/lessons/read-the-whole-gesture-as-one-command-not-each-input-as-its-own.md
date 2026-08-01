---
type: lesson
title: "Read the whole gesture as one command, not each input as its own"
figure: wirth
works: [project-oberon]
axes: [expressiveness, primitive-count, cognitive-load]
subdomains: [programming-environments-and-object-systems, software-engineering-and-architecture]
tags: [lesson]
---
# Read the whole gesture as one command, not each input as its own

**Lesson:** When an input device offers very few distinguishable signals and the vocabulary you need is much larger, the reflex is to add signals — more buttons, modifier keys, a mode setting, a menu. There is a cheaper move available first: stop treating each signal as an event and start treating the whole interval between the first press and the last release as a single event. A command is then identified by a tuple — which signal opened the interval, where the pointer was then, the *set* of signals asserted at any time before the interval closed, and where the pointer was at the close — and three buttons yield a dozen commands with no new hardware and no mode. The multiplication is free because the raw device was already producing this information; the old design was simply discarding it by sampling at the wrong granularity.

What makes the resulting vocabulary learnable rather than merely large is which factor of the tuple carries which kind of meaning, and this is a decision, not a consequence. Let the opening signal name the operation — draw, move, select — so the user's first act commits to a family, and let anything asserted afterwards modify that family rather than replace it. Then the modified forms stay related to their base: move plus one extra becomes copy, move plus the other becomes move-the-background-instead. Each is a recognizable variation on what the hand already started doing, so the vocabulary is memorized as a small set of operations times a small set of qualifiers instead of as a flat list. The alternative assignment — where the combination means something unrelated to either part — is exactly as easy to implement and considerably worse to use, and nothing in the mechanism prevents you from choosing it.

The general shape here is worth extracting from the mouse: an interface's expressive capacity is set jointly by its alphabet and by the span over which you agree to interpret that alphabet, and the second is usually free to change while the first is not. Widening the interpretation window costs a little state in the reader and, importantly, a commitment that the interval has an unambiguous end — the release of the last signal, the arrival of a terminator, the closing of a transaction. Where such an end exists, look there before adding vocabulary. Where it does not, you are obliged to add signals, and the absence of a clean end is the real reason, worth saying out loud rather than discovering after the fact.

**Source:** [Project Oberon](../works/project-oberon.md) — section 13.2's account of the Draw system's mouse interface, in which a command is identified by the initially pressed key, the initial cursor position, the set of keys pressed until the last is released, and the final position; together with the summary table in which the three buttons alone name draw, move and select, and each interclicked second button qualifies that base operation into copy, plane-shift, or selection without deselection.
