---
type: lesson
title: "Generality of notation is not generality of power"
figure: peter
works: [uber-den-zusammenhang-der-verschiedenen-begriffe-der-rekursiven-funktion]
axes: [expressiveness, primitive-count]
subdomains: [foundations-of-computation]
tags: [lesson]
---
# Generality of notation is not generality of power

A defining scheme can look strictly more permissive than another and still define exactly the same things. Péter takes several definition forms that were circulating as if they were distinct notions — one where a new value may consult the entire history of earlier values rather than just the immediately preceding one, one where the argument being recursed on is itself produced by a recursive call, one where a definition mentions extra parameters — and shows each collapses back into the plainest form. The syntactic freedom was real; the extra reach was imaginary. She then adds the sharper half of the observation: at least one generalization, simultaneous recursion on several variables, genuinely does escape, so the collapse is not a blanket rule about generalizations but a fact that has to be established case by case.

This matters because programmers routinely mistake a convenient notation for a capability. Adding pattern matching over an accumulated history, adding mutual reference, adding parameters, adding sugar for a common shape — none of these necessarily changes what a language can compute or what a system can express. The honest measure of a construct is the set of behaviors reachable with it minus the set reachable without it, and that difference is usually much smaller than the difference in how comfortable the two look.

Believing this changes how you argue for a feature. You stop justifying additions by "this form is more general" and start asking what is newly reachable, which forces you to produce either a translation (proving the addition is convenience, to be judged on ergonomics alone) or a separating example (proving it is power, to be judged on cost). Both answers are useful; the vague middle where nobody has checked is what produces bloated cores full of constructs that each pull their own weight in tutorials and none in capability.

**Source:** [Über den Zusammenhang der verschiedenen Begriffe der rekursiven Funktion](../works/uber-den-zusammenhang-der-verschiedenen-begriffe-der-rekursiven-funktion.md) — the framing in the introduction, where several recursion notions in use by different authors are laid side by side, and the closing statement that admitting two of them enlarges nothing while a third is known to escape.
