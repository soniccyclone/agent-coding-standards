---
type: lesson
title: "When a system sits between two things that vary independently, partition by which side each part depends on"
figure: wirth
works: [project-oberon]
axes: [cognitive-load, expressiveness, hardware-affinity]
subdomains: [programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# When a system sits between two things that vary independently, partition by which side each part depends on

**Lesson:** A translator of any kind — between a notation and a machine, a protocol and a store, a request format and an execution engine — stands between two specifications that change for unrelated reasons and on unrelated schedules. That situation supplies a decomposition criterion far better than the usual ones, which sort code by what it does or by the phases it runs in. Sort instead by which of the two specifications each piece depends on. A piece that would have to be rewritten if the input notation changed goes on one side; a piece that would have to be rewritten if the target changed goes on the other; and the boundary between them is the place where the design's two futures separate.

The payoff is that each future change is confined by construction. Retargeting touches only the parts that were sorted onto the target's side, and adapting to a revised input touches only the other, and neither exercise requires anyone to first work out where the affected code lives — the sorting already answered that. It also yields a natural intermediate vocabulary: the boundary must be describable in terms that mention neither specification, which is a strong constraint and a productive one, since an interface that keeps leaking one side's concepts is telling you the sorting was done carelessly at that point.

The honest caveat is that the sorting is never perfectly clean, and the discipline is to say so rather than to force it. Some decisions genuinely depend on both — a construct whose translation is chosen because the target happens to offer a shortcut, a check that belongs to the input's rules but can only be made once the target's representation is known. Pretending these do not exist produces an interface with a growing set of exceptions that nobody has classified. Naming them, and keeping them few, is what makes the partition trustworthy: readers can rely on the rule and be told explicitly where it bends. And it is worth noticing that the two sides will not be the same size. Whichever specification is more irregular will produce more code, so the boundary that looks balanced on paper often divides a small tidy component from a large awkward one, which is a finding about the two specifications, not a defect in the split.

**Source:** [Project Oberon](../works/project-oberon.md) — section 12.1's distinction between analysing steps and code generating steps, described in rough approximation as source-language-dependent and target-independent on the one hand and source-independent and target-dependent on the other, with the acknowledgement that reality is somewhat more complex and the statement that the compiler's module structure nevertheless clearly reflects this division; together with the observation later in the same section that the syntax is defined by a small set of equations so the parser is short and perspicuous, whereas the target's instruction set is complex so the code generating program is much longer and harder to comprehend, and is distributed over three modules to keep each within reasonable size.
