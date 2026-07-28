---
type: lesson
title: "Reduce in stages until the residual case is trivial"
figure: peter
works: [uber-den-zusammenhang-der-verschiedenen-begriffe-der-rekursiven-funktion]
axes: [cognitive-load, verifiability, primitive-count]
subdomains: [foundations-of-computation, programming-languages-and-semantics]
tags: [lesson]
---
# Reduce in stages until the residual case is trivial

Faced with proving that an entire family of elaborate definitions collapses into
a simple one, Péter does not attack the general case. She builds a staircase.
First shrink the arity: any number of passive parameters becomes one, so nothing
below has to carry a variable-length argument list. Then normalize the shape of
the defining term into an explicit canonical layout. Then reduce the general
case to a fixed small instance of itself. Then reduce that instance to the
target scheme. Each step is a meaning-preserving rewrite whose only job is to
make the next step statable, and the real argument happens only at the bottom,
where the surviving case is small enough to reason about directly.

She is candid that most of these steps buy nothing mathematical. One footnote
says outright that the earlier reductions serve merely to simplify the notation,
and another admits that the final method could have been applied to the general
definition immediately, but that technical clutter would have made the argument
unsurveyable. That candor is the point worth extracting. The stages are not
disguised content; they are cost control on human attention. The theorem is
unchanged by them, and the proof becomes possible because of them.

This is the same discipline as a compiler's lowering pipeline, and it deserves
the same respect in ordinary work. When a problem is stated over a
too-expressive input, the productive move is rarely a single clever handler for
everything. It is a sequence of passes, each one narrowing the language by one
feature, each one obviously correct in isolation, ending in a core small enough
that the interesting logic fits in one place and can be tested there. Two
practical corollaries follow. Order the passes so each removes a feature the
later passes would otherwise have to tolerate — that is what makes them
individually simple. And say out loud which passes are load-bearing and which
are only for legibility, because a reader who cannot tell the difference will
either distrust the whole chain or defend a stage that could be deleted.

**Source:** [Über den Zusammenhang der verschiedenen Begriffe der rekursiven Funktion](../works/uber-den-zusammenhang-der-verschiedenen-begriffe-der-rekursiven-funktion.md) — the treatment of nested recursion, which announces its plan as a step-by-step retreat to ever simpler special cases and flags in footnotes which of those steps are only notational.
