---
type: lesson
title: "Design the principled version first so that every economy you take afterwards has a visible price"
figure: wilkes
works: [best-way-to-design-an-automatic-calculating-machine]
axes: [cognitive-load, verifiability]
subdomains: [software-engineering-and-architecture, operating-systems-and-systems-programming]
tags: [lesson]
---
# Design the principled version first so that every economy you take afterwards has a visible price

**Lesson:** The usual objection to a regular, uniformly structured design is that it spends more resources than a hand-tuned one. The answer is not to defend the regular version as final but to build it first anyway and treat it as the reference against which departures are measured. Starting from the clean layout and then economizing tends to land somewhere both clean and cheap, because each saving is taken deliberately, against a known baseline, with its structural cost stated. Starting from an economical tangle and trying to tidy it afterwards has no such property: there is nothing to compare against, so no one can say what the tidying is worth or what the tangle cost.

The mechanism here is that a baseline turns an unquantifiable trade into a series of small, individually visible ones. Without the principled layout in hand, "we gave up some regularity for efficiency" is a sentence with no content — the regularity given up was never specified. With it, each compromise is a named deviation from a named structure, and the designer can see at every step exactly how much structure is being spent and what is being bought. That visibility is what allows the compromises to stop when they stop paying, which is the part that never happens when optimization starts from scratch.

The habit generalizes past efficiency. Any design pressure that pulls against structure — a deadline, a compatibility constraint, an awkward external interface — is best absorbed as an explicit deviation from a design you actually worked out, rather than as an excuse for never working it out. The principled version does not have to survive to be worth building. Its job may be entirely to serve as the thing your compromises are measured from.

**Source:** [The Best Way to Design an Automatic Calculating Machine](../works/best-way-to-design-an-automatic-calculating-machine.md) — the reply to the objection that the systematic control scheme looks extravagant in equipment, arguing that beginning from a logical layout leads to an arrangement both logical and economical because one can see at each stage what is being sacrificed in either direction.
