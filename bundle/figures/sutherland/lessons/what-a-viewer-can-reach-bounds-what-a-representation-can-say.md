---
type: lesson
title: "What an observer can reach bounds what a representation can say"
figure: sutherland
works: [a-head-mounted-three-dimensional-display]
axes: [expressiveness, cognitive-load]
subdomains: [programming-environments-and-object-systems, software-engineering-and-architecture]
tags: [lesson]
---
# What an observer can reach bounds what a representation can say

A model can hold every fact needed to answer a question and still fail to answer it, because the person asking cannot get to the place from which the answer is visible. Sutherland's display held complete three-dimensional structure, yet users who could only move within a few feet of one spot read some shapes wrong — not for want of data, and not because the rendering was inaccurate, but because the one vantage that disambiguated the object lay outside the volume they could occupy. Others read the same shape correctly, having brought the missing constraint with them as prior knowledge. The information content of a representation is therefore not a property of the representation alone. It is a property of the pairing between the representation and the set of observations its consumer can actually perform.

This holds because every inspectable form is a projection, and a single projection almost never determines its preimage. Understanding gets assembled from several projections taken together, so the reachable set of projections is the real budget. Shrink that set and you have shrunk expressiveness just as surely as by deleting fields from the model. Worse, the failure is silent and self-confirming: the consumer sees a coherent picture, forms a wrong interpretation, and gets no signal of incompleteness, because nothing in the view announces which distinguishing view is missing. Sutherland also noticed the inverse failure — a viewer's habits from a more familiar setting overriding what the representation was correctly reporting — which is the same phenomenon read from the other side, prior knowledge silently filling a gap the reachable views left open.

A programmer who holds this stops asking whether a system's state is fully captured and starts asking which questions can be answered from the vantages an operator can actually occupy. It changes what you build: not a richer dump, but a way to move — the ability to pivot, re-slice, follow a reference back, look at the same state from a second independent angle. It also changes how you read your own tooling's successes. When a dashboard, a log, or a debugger appears to explain an incident, the honest question is whether the explanation was derived from the views available or imported from what you already believed. If the only vantage you can occupy is the one that fits your hypothesis, the tool is confirming you, not informing you.

**Source:** [A Head-Mounted Three Dimensional Display](../works/a-head-mounted-three-dimensional-display.md) — the results discussion, where restricted head motion left wireframe objects genuinely ambiguous for some observers while prior familiarity resolved them for others.
