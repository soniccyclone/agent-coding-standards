---
type: lesson
title: "A widely adopted middle layer stops being neutral and starts dictating the layers on both sides of it"
figure: kay
works: [steps-toward-the-reinvention-of-programming]
axes: [hardware-affinity, expressiveness, primitive-count]
subdomains: [programming-languages-and-semantics, operating-systems-and-systems-programming]
tags: [lesson]
---
# A widely adopted middle layer stops being neutral and starts dictating the layers on both sides of it

**Lesson:** An intermediate representation is introduced as a convenience: it captures the abstraction of the machinery of its day so that things above it need not think about the machinery directly. It is descriptive at that moment. But if enough gets written in it, the layer below starts being built to serve it — the machinery acquires features whose only justification is making that representation run faster — and now the representation is prescriptive in both directions. It fixes what the hardware will be good at, which fixes what the layers above can afford to do, which keeps the representation indispensable. Nothing in this loop is anyone's mistake; it is what popularity does to a description. The consequence for a designer is that the middle layer's assumptions are no longer a neutral fact about implementation. They are a constraint on the ideas you are allowed to have, arriving from an era whose machines are gone.

Escaping does not mean pretending the layer's function is unnecessary. Something in a serious pipeline has to look roughly like a stripped-down machine-level abstraction, because that job is real. The move is to keep the stage and change its authorship: it becomes a thing your system generates on its way down from a high-level statement, never a thing a person writes and never the level at which meaning is stored. Once no source text lives there, the layer can be replaced, retargeted, or improved without anything above noticing, and it stops being able to veto abstractions that its own era's machines happened to disfavor. The corresponding requirement on the toolchain is a very steep descent — few enough stages, and cheap enough to define, that a system's meaning can be expressed at genuinely high level and still arrive at real instructions without a hand-written plateau in the middle.

The general test is worth applying to any layer a project depends on: if it were replaced tomorrow, is there source text that would have to be rewritten by hand? Wherever the answer is yes, that layer is load-bearing for expression and not merely for execution, and its assumptions have been inherited whether or not they were examined. Layers you generate into are commitments you can revisit; layers you write in are commitments that outlive their reasons.

**Source:** [STEPS Toward the Reinvention of Programming](../works/steps-toward-the-reinvention-of-programming.md) — the section on getting from the machine level up to high-level languages, which argues that a low-level language is essentially the abstraction of the simple hardware of its time, notes the mutual lock-in in which hardware features get added specifically to run such code faster, and concludes that the pipeline should retain a stage at roughly that level of abstraction while requiring it always to be written by automatic processes rather than by people.
