---
type: lesson
title: "Decidability is lost to feature interaction, not to any one feature's power"
figure: godel
works: [on-undecidable-propositions-of-formal-mathematical-systems]
axes: [expressiveness, verifiability, primitive-count]
subdomains: [algorithms-and-complexity, programming-languages-and-semantics, foundations-of-computation]
tags: [lesson]
---
# Decidability is lost to feature interaction, not to any one feature's power

**Lesson:** Gödel drives the undecidable statement all the way down into elementary arithmetic: it can be restated as a claim about which natural numbers solve a polynomial equation, built from nothing but addition, multiplication, comparison, and quantifiers. Then comes the observation that gives the reduction its bite. A decision procedure was already known for the fragment with addition and no multiplication, and a decision procedure was sketched for the fragment with multiplication and no addition. Each operation alone leaves a tractable theory. Put both in the same language and no decision procedure can exist. Nothing about either operation is individually to blame; the loss is entirely in the interaction, in what the two together let you encode that neither could encode alone.

This is the single most useful thing to carry from these results into design work, because it inverts the intuition people actually use. The usual mental model is that complexity accumulates by addition: each feature costs a little tractability, and if you keep features few and each one modest you stay safe. The real behaviour is a threshold. A language, query system, type checker, or configuration format can absorb feature after individually harmless feature, staying decidable and staying fast, and then one addition that looks no larger than the others crosses a line and the whole thing becomes a general-purpose computational substrate with no analysis story at all. Afterwards it is hopeless to look for the guilty feature, because there isn't one — the capability is emergent, and removing any of several features would restore tractability.

What the programmer does differently is to reason about extensions in terms of what the *combination* can now encode, rather than in terms of what the new feature does on its own. The concrete discipline: before adding a construct, ask what you could build with it together with everything already present, and specifically whether the combination can now simulate arbitrary recursion or unbounded search. Templates plus arithmetic, a query language plus recursion, a config format plus interpolation plus conditionals, a type system plus dependent quantification plus unrestricted recursion — each of these families has a member that got accidentally Turing-complete in exactly this way, and the accident is always discovered downstream by whoever tried to write the analyzer, the optimizer, or the resource bound.

Gödel also notes the corollary that keeps this from being counsel of despair: the specific statement his construction produces *is* settled once you move to a stronger system, and then that stronger system has its own, and so on without a terminal level. Strengthening always works for a named problem and never works once and for all. So the useful goal is not a formalism that is powerful enough for everything, but a deliberate choice of where on the ladder each part of your system sits, and honesty about which parts have been pushed past the point where anything can be decided about them.

**Source:** [On Undecidable Propositions of Formal Mathematical Systems](../works/on-undecidable-propositions-of-formal-mathematical-systems.md) — the section reducing the undecidable statement to a quantified Diophantine form, its closing contrast between the separately decidable additive and multiplicative fragments and the undecidable combination, and the accompanying remark that each undecidable statement yields to the next type level while new ones appear there.
