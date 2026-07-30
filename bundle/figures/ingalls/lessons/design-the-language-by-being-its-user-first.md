---
type: lesson
title: "Design a language by building real applications in the version you already have, then redesigning from the scar tissue"
figure: ingalls
works: [design-principles-behind-smalltalk]
axes: [expressiveness, cognitive-load]
subdomains: [programming-languages-and-semantics, programming-environments-and-object-systems]
tags: [lesson]
---
# Design a language by building real applications in the version you already have, then redesigning from the scar tissue

**Lesson:** A notation cannot be evaluated from the designer's chair, because the thing being judged is how it feels to think in over months, and no amount of contemplation of the grammar reveals that. The working method is a loop with three distinct roles: build a substantial application inside the current system, which is the observation; let the friction encountered there dictate what the next version of the language must change, which is the theory; then implement that version, which is a prediction concrete enough to be wrong. Each turn of the loop takes years, not weeks, because the observation phase is only honest if the application is real enough that its author would have quit had the language been intolerable.

Two properties of this arrangement do the work. The first is that the designer is forced to be a heavy user of the previous version, so the defects that get fixed are the ones that actually cost something rather than the ones that are theoretically inelegant. Language flaws sort themselves by how often you trip on them, and that ordering is invisible except from the inside. The second is that each redesign is committed to as a whole system rather than accumulated as patches on the old one, which keeps the design from becoming a sediment of local fixes. Patching preserves every past mistake as a constraint; rebuilding lets a principle learned in year four restructure a decision made in year one.

The generalizable claim is that a language, or any medium people are meant to think in, is an empirical subject and should be treated with the plainest experimental discipline available: make something with it, let the making generate the complaints, change the medium rather than the complaint, and go again. The failure mode this guards against is the design that is coherent on paper and unusable in practice — which is the normal outcome when the designer never has to live downstream of the design.

**Source:** [Design Principles Behind Smalltalk](../works/design-principles-behind-smalltalk.md) — the opening description of the project's two-to-four-year cycle, explicitly paralleled to observation, theory formation, and testable prediction, with the note that Smalltalk-80 was the fifth pass through it.
