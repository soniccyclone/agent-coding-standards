---
type: lesson
title: "Keep what lets you check, not what lets you act"
figure: wirth
works: [project-oberon]
axes: [verifiability, primitive-count, cognitive-load]
subdomains: [operating-systems-and-systems-programming, databases-and-data-management]
tags: [lesson]
---
# Keep what lets you check, not what lets you act

**Lesson:** When a component must decide whether a presented value is the right one, the obvious implementation is to keep the right one and compare. That works, and it quietly gives the component a capability far beyond what its job required: it can now produce the value, not merely recognise it, and so can anything that reads its storage. The asymmetry is the whole point. Verifying and generating are different powers, and a system that only needs to verify has no business holding the power to generate — because every place that holding is stored, copied, backed up or read becomes a place from which the value escapes, and none of those places were part of the design's reasoning.

The general move is to store an image of the value under a transformation that is easy to apply and hard to invert, and to compare images instead of originals. Checking still works, since the same input yields the same image. Producing no longer does. What makes this a discipline rather than a single technique is where the transformation is applied: it must happen at the earliest point the value is known, so that the original exists only momentarily and is never written down anywhere — not in a store, not in a transfer, not in a log. A design that transforms the value late has protected the store while leaving copies of the original along the path to it, which is the same mistake made less visibly.

The habit generalises past secrets. Any time a component holds something more powerful than its function needs — a full record when it compares one field, a writable handle when it only reads, an authority to act when it only decides whether an action is permitted — the excess is a liability that shows up in some later composition nobody has yet imagined. So the question to ask of each piece of retained state is not "is this useful here" but "what is the least that would let this component do its job", and then to check whether a cheap transformation gets you down to that. When one exists, take it: the reduction costs a function call and removes a whole category of consequence.

**Source:** [Project Oberon](../works/project-oberon.md) — section 11.5's account of user administration, in which a significant step towards protection is the introduction of a password beside the registered name so that a request is honoured only if the delivered and stored passwords match, followed by the observation that abusive attempts would aim at recovering the stored passwords and the resolution to store an encoded form, with the command that asks for a user identification and password encoding it immediately so that the original is stored nowhere, under an encoding for which constructing a corresponding decoder is difficult.
