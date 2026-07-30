---
type: lesson
title: "Before inventing a rule for a special case, look for an existing notion that already has the property you need"
figure: strachey
works: [the-main-features-of-cpl]
axes: [primitive-count, expressiveness, cognitive-load]
subdomains: [programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# Before inventing a rule for a special case, look for an existing notion that already has the property you need

**Lesson:** Certain requirements arrive looking like they need machinery of their own. A facility that must accept differing numbers of arguments seems to need a special rule about argument counting, and systems that go that way accumulate awkward provisions that interact badly with everything else. The alternative is to notice that some notion already in the system has the property in question — a variable-length aggregate is a variable-length aggregate — and to declare that the facility takes one of those, in a single position, as an ordinary argument. The requirement is satisfied with no new rule, and the apparent variability of the interface is now just the ordinary variability of a value.

The habit worth building is to hold the special case up against your existing vocabulary before designing for it. The question is not "what mechanism handles this" but "what already in this system has the shape this needs," and it is worth asking even when the answer requires an aggregate whose only purpose in that position is to carry the variability. What you avoid is not the code you would have written, which is generally small, but a rule that everything else must henceforth be reconciled with — and the recognizable sign of having got this wrong elsewhere is a facility whose specification is dominated by provisions about how many things it takes and in what order.

There is a useful corollary about comparisons. Because the reuse route produces no new machinery, its benefit is invisible unless you name the alternative — the contemporary system that solved the same requirement with a dedicated scheme and was widely regarded as unpleasant to use. Recording the comparison is what turns "we used a list here" into a design decision someone can learn from, and it is the only way an omission gets credited as an achievement.

**Source:** [The Main Features of CPL](../works/the-main-features-of-cpl.md) — the input facilities section, where the read operation takes an explicit list as its formal parameter, yielding a routine with an apparently variable number of actual parameters, with the stated purpose of avoiding the difficulties of a contemporary Algol implementation's input-output scheme.
