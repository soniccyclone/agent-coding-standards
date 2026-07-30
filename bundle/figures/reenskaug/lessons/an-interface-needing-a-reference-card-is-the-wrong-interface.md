---
type: lesson
title: "An interface that ships with a reference card is the wrong interface, and invisible modes are why"
figure: reenskaug
works: [working-with-objects-the-ooram-software-engineering-method]
axes: [cognitive-load]
subdomains: [software-engineering-and-architecture]
tags: [lesson]
---
# An interface that ships with a reference card is the wrong interface, and invisible modes are why

**Lesson:** The author quotes, from the front pages of his local telephone directory, the procedure for redirecting incoming calls: wait for a tone, enter a punctuation-and-digits prefix, enter a destination, terminate with another symbol, wait for an acknowledgement, hang up — with a different, unrelated prefix to undo it, and further distinct prefixes for the conditional variants. The fact that these instructions are printed in the directory is presented as the evidence. Nobody remembers them; the reference card is not a convenience accompanying the design, it is the design's confession.

That is a usable diagnostic because it is observable from outside and requires no user study. If a capability is systematically accompanied by a printed or pinned crib sheet, the operations have no relationship to the concepts users hold, and the arbitrary encoding must be memorized rather than derived. The distinct prefixes for closely related variants make the point precisely: a user who understood the first cannot infer the others, since nothing about the encoding carries meaning.

The proposed replacement is instructive less for being simpler than for what it fixes. A physical switch with a lamp beside it: throw it and calls redirect, return it and they do not, with the lamp lit while the redirection is active. The state has become continuously visible rather than merely settable, and that is the deeper repair. The original design lets a user enter a persistent mode through a transient interaction and then walk away with no indication anywhere that the mode is in force — so the characteristic failure is not fumbling the sequence, it is missing calls for a week without knowing why. A mode you can enter but cannot see is a trap, and no amount of making the entry sequence more memorable addresses it.

Two properties are worth naming because they are what the light supplies. The state's representation is the same object as its control, so there is no way for the display to disagree with reality. And the display is ambient — it costs nothing to check, requires no query, and is noticed peripherally by someone not looking for it, which is the only way a forgotten mode ever gets discovered.

The transferable habit: treat accompanying documentation-at-point-of-use as a defect report against the interface, and for every persistent mode a system can enter, ask where its being-on is visible when nobody is looking for it. If the answer is "you can check," the mode is invisible.

**Source:** [Working With Objects: The OOram Software Engineering Method](../works/working-with-objects-the-ooram-software-engineering-method.md) — chapter 12 section 12.2, which reproduces from the author's local telephone directory the cryptic activation codes for Call Forward Unconditionally, on Busy, and on no Reply — each a distinct star-code sequence with tone waits and a separate cancellation code, printed on one of the first pages of the directory because they are cumbersome — and proposes instead a switch with an associated warning light, thrown when leaving the office to light the lamp and forward calls to a predefined number, and returned on arrival to cancel the service and extinguish the light.
