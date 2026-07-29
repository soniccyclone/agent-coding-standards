---
type: lesson
title: "Snap approximate input onto the model's vocabulary at the boundary"
figure: sutherland
works: [sketchpad-a-man-machine-graphical-communication-system-afips-1963]
axes: [verifiability, cognitive-load, expressiveness]
subdomains: [programming-environments-and-object-systems, software-engineering-and-architecture]
tags: [lesson]
---
# Snap approximate input onto the model's vocabulary at the boundary

Input from the physical world arrives as measurement: a coordinate, a timestamp, a reading, all of it approximate and none of it meaningful in the model's own terms. The tempting design keeps the measurement and lets every later stage cope with slop, which means every later stage grows its own tolerance, its own rounding, its own idea of "close enough." Sutherland does the opposite. At the moment of entry, the raw position is thrown away and replaced by a position that is exactly on some element the system already knows about, if any such element is nearby; only when nothing is nearby does the raw value survive. Downstream, there is no approximation left to reason about, because the boundary already converted a measurement into a reference.

Two things make this more than a convenience. First, the substituted value is fed back visibly, so the operator sees which element was chosen before committing — the interpretation is negotiated, not silently imposed. Second, the candidate set is deliberately widened past what is literally being measured to include things that are structurally implied: the ends of a line, the crossing of two lines, the attachment sites of a repeated symbol. These are all things the model can talk about but the display never draws, and they are exactly the things a user means to indicate. Interpretation at the boundary is where the system decides what its inputs are allowed to mean, so that is where the model's vocabulary belongs.

The programmer who takes this seriously puts the normalization, resolution, and identity-matching at the trust boundary and lets the interior be total. Parse into the domain type at the edge rather than passing strings inward. Resolve a click, a fuzzy name, or a sensor sample to a domain entity once, echo the resolution back for confirmation, and let everything downstream assume exactness. The corollary is a discipline too: for every kind of thing that can be pointed at, you owe an explicit answer to "how near is this?" — including the honest answer that the question does not apply, which is far better than a default that quietly wins the match.

**Source:** [Sketchpad: A Man-Machine Graphical Communication System (AFIPS 1963)](../works/sketchpad-a-man-machine-graphical-communication-system-afips-1963.md) — the light-pen section, covering the substituted "pseudo" position, the narrowing of the device's own field of view for pointing, and the extension of candidates to structurally implied but undisplayed entities.
