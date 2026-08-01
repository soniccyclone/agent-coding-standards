---
type: lesson
title: "Shared conventions are owed where artifacts cross, not everywhere"
figure: wirth
works: [project-oberon]
axes: [cognitive-load, expressiveness]
subdomains: [programming-environments-and-object-systems, software-engineering-and-architecture]
tags: [lesson]
---
# Shared conventions are owed where artifacts cross, not everywhere

**Lesson:** "Be consistent with the rest of the system" is usually asserted as a general virtue and is therefore easy to dismiss when it costs something. It becomes an argument with force once you attach it to a specific condition: two components owe each other identical conventions exactly to the extent that things move between them. If an item can be taken from one and placed in the other, then a single user action spans both, the interpretation of that action is chosen by whichever component the pointer happens to be over, and a divergence between them is not a matter of recall but a hazard — the same gesture on the same item does two different things depending on which side of a boundary it started, and there is no cue that a boundary was crossed. Where nothing flows between two components, divergence costs only memory, which is a real but much smaller cost, and is sometimes worth paying for a genuinely better local design.

This gives a usable procedure rather than an exhortation. Enumerate the operations that exist in both domains — designate a target, mark an insertion point, invoke a general command, move something across — and make those identical, because those are the ones a crossing action will exercise. Then enumerate the operations that are inherent to one domain and have no counterpart in the other, and let them differ without apology; forcing an artificial correspondence there buys nothing and distorts both designs. The set of conventions requiring agreement is thus derived from the set of shared operations, and is typically much smaller than "everything", which is what makes the discipline affordable.

Attach one warning to the whole exercise. Most of what feels natural in an interface is habit, and habit is routinely mistaken for fitness — the argument "this is how it is normally done" is not evidence about quality, only about exposure. Which is why the flow-of-artifacts criterion is worth having: it justifies conformity where conformity actually prevents a failure, and it withholds justification everywhere else, so the remaining conventions have to defend themselves on their own merits.

**Source:** [Project Oberon](../works/project-oberon.md) — section 13.5, which observes that there is no fixed set of rules determining the optimal interface and that convention is all too often mixed up with convenience; that Draw's conventions were adapted to those of the text system wherever possible, with the right key selecting, the left setting the caret and the middle activating commands; that certain drawing commands inherently cannot be handled as they are for texts, since a character is created by typing while a line is created by dragging; and that the copy interclicks behave identically in both, which is unsurprising because captions can be copied from texts into graphics and back, so using different conventions depending on which frame the item was pointed at would be confusing.
