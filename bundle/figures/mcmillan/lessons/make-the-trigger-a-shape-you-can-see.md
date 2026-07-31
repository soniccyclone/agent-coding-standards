---
type: lesson
title: "Make the trigger a shape you can see, and defend the shape with a survey"
figure: mcmillan
works: [symbolic-model-checking-10-20-states-and-beyond]
axes: [expressiveness, cognitive-load, verifiability]
subdomains: [programming-languages-and-semantics, software-engineering-and-architecture, algorithms-and-complexity]
tags: [lesson]
---
# Make the trigger a shape you can see, and defend the shape with a survey

The paper's step-count-reducing transformation is not stated for arbitrary inputs. It is stated for terms of one particular written form — a base part, and a part that steps the accumulating variable forward — and everything else is out of scope. The authors then do something short and unusual: they acknowledge that the restriction looks severe, and answer it not by working harder on generality but by reporting that nearly everything they have actually written as a specification already fits.

Both halves of that are worth taking. Making the applicability condition *syntactic* means it can be decided by looking, which turns the optimisation into a rewrite rule rather than an analysis. The semantic version of the same condition — this computation is essentially an accumulation over a step relation — is the sort of thing you would need a whole inference pass to establish, and would establish only approximately. The shape version is a pattern match. It also composes: a caller can tell in advance whether the fast path will be taken, and can arrange to be eligible, which is impossible when eligibility depends on a judgement the compiler makes privately.

The second half is the epistemically interesting one. Once your precondition is narrow, the question "is this too narrow?" is empirical and nothing else. It is not answered by proving a more general theorem, and it is certainly not answered by intuition about what users might write. It is answered by going and looking at what has actually been written. That is a cheap study most people skip in favour of generalising, and generalising is usually the more expensive path to a worse result — a transformation that fires on everything and helps on nothing in particular.

The failure mode matters too, and is the reason a narrow trigger is safe to ship. When an input does not match the shape, the transformation simply does not fire and the ordinary path runs. Nothing becomes wrong; something merely stays slow. Restrictions with that property can be tightened and loosened freely as evidence accumulates, which is exactly what you want from a bet on the distribution of real inputs, because that distribution moves. Contrast a precondition whose violation produces a wrong answer instead of a missed opportunity: those have to be right on the first try, and are not the kind of restriction to defend with a survey.

So: state the condition as a shape, check it by inspection, count how often real inputs already have it, and design so that missing the shape costs performance rather than correctness. Then revisit the count when the inputs change, rather than treating the original narrowness as either permanent or shameful.

**Source:** [Symbolic Model Checking: 10^20 States and Beyond](../works/symbolic-model-checking-10-20-states-and-beyond.md) — the general-transformation subsection, where the iteration-reducing rewrite is restricted to relational terms of a stated syntactic form and the restriction is defended by the observation that nearly all specifications the authors have written in practice can be put in that form.
