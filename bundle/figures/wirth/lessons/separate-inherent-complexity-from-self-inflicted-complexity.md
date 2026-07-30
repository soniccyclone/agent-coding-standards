---
type: lesson
title: "Before accepting a system's complexity, separate what the problem demands from what abundance permitted"
figure: wirth
works: [a-plea-for-lean-software]
axes: [cognitive-load, hardware-affinity]
subdomains: [software-engineering-and-architecture]
tags: [lesson]
---
# Before accepting a system's complexity, separate what the problem demands from what abundance permitted

**Lesson:** The interesting question about a bloated system is never whether the problem got harder — sometimes it did — but how much of the growth is traceable to the problem at all. Run the test on a component whose obligations have not changed in decades: an editor still inserts, deletes and moves text; a compiler still turns text into code; a scheduler still hands out cycles. If the resource footprint for those unchanged obligations has grown by orders of magnitude, the growth is not explained by difficulty. It is explained by the disappearance of the constraint that used to force a decision. Cheap memory and fast processors do not make bulk correct; they make it survivable, which is a different and much weaker property. A design that only works because the substrate got a thousand times faster has been subsidized, not engineered.

That reframe puts the burden of proof in the right place. Each capability has to justify its cost against the concept the system is built on, not against the question "would a user like it?" — because the answer to the second is always yes and carries no information. Users are poorly positioned to distinguish a feature that extends what the system fundamentally does from a feature that is merely pleasant, so a vendor who takes requests uncritically accumulates additions that are individually harmless and collectively incoherent: each one slightly incompatible with the original organizing idea, the incompatibility unnoticed or ignored, the design a little more contorted and its use a little more awkward. Counting features is then mistaken for measuring power. The failure mode is not any single bad feature; it is the absence of anyone asking whether a feature belongs to the same system as the rest.

Two diagnostics fall out of this and both are worth internalizing because they are cheap to apply from the outside. First, a system that needs an enormous manual is confessing that it has no generally valid rules — that its behavior must be learned case by case from tables of special situations rather than derived from a few principles. Volume of documentation measures conceptual incoherence more reliably than it measures capability. Second, incomprehensibility should provoke suspicion rather than respect. There is a persistent confusion of complexity with sophistication, and it survives partly because mystery flatters the user and partly because a customer who never masters the tool is a better customer. Whatever the motive, the inference to draw when you cannot see through a system is that its designers could not either.

**Source:** [A Plea for Lean Software](../works/a-plea-for-lean-software.md) — the opening comparison of unchanged basic obligations against grown resource demands, the causes-of-fat-software section on uncritical feature adoption and self-inflicted versus inherent complexity, and the passages on complexity misread as sophistication and on manuals as a symptom of missing concepts.
