---
type: lesson
title: "Minimality is priced per construct, and the price is how often the construct gets written"
figure: steele
works: [the-revised-report-on-scheme]
axes: [primitive-count, expressiveness, cognitive-load]
subdomains: [programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# Minimality is priced per construct, and the price is how often the construct gets written

**Lesson:** It would be easy to read a minimal-core language as the output of a rule applied uniformly: always prefer the smaller primitive. The report refuses that reading in the most direct way available — by making the trade in opposite directions on two adjacent decisions and pointing out that it has done so. For the conditional, it takes the definitionally simpler two-branch form over the traditional multi-armed one, accepting the loss of convenience because simplicity of definition dominates. For recursive local definitions, it takes the more complicated form that binds several mutually recursive procedures at once over the traditional single-binding one, accepting the loss of definitional simplicity because trying to express mutual recursion with the simpler primitive is painful enough to matter. The report draws the contrast explicitly. There is no rule; there is a weighing, done once per construct, between how hard the thing is to define and how hard it is to live with.

The weight that decides these cases is usage frequency, and the report shows its arithmetic in the one place where minimality would have bought something real and was declined anyway. The language's notation is genuinely ambiguous — a form can be read either as a call or as a special form, and the reader resolves it by privileging the special form. The ambiguity could be removed completely by requiring an explicit marker on calls, which would make the language's meaningful expressions a sparse and unconfusable subset of all expressions. The report works out why that is not worth it: calls occur about as often as all other compound forms put together, and the thing you write most often should be the thing you write least. So the ambiguity stays, priced not by taste but by count.

Crucially, the report also records the bill that comes due. Leaving the two categories ambiguous means the language's reserved words and its variables share one namespace, so a new special form can silently break existing programs — which is exactly what happened when a wanted loop construct had to be given a different, worse name because the obvious name was already in widespread use as an ordinary variable. The report names this as referential opacity that got in despite the designers' intentions. That is the honest shape of the trade: the notational saving is real, the later constraint on the namespace is also real, and both were foreseeable.

A designer who works this way stops arguing about minimality in the abstract and starts asking, for each individual decision, how many times the construct will be written, how much a reader must know to disambiguate it, and what the decision forecloses years later. They accept a larger primitive when the smaller one makes a common case laborious, accept an awkward one when the definition has to stay small, and write down which way they went and why — because the next revision of the design will have to re-litigate the case and the reasoning is the only thing that transfers.

**Source:** [The Revised Report on Scheme: A Dialect of LISP](../works/the-revised-report-on-scheme.md) — the parenthetical comparing the choice of the simple conditional against the choice of the multiple-binding recursive form, and the note working through the explicit-call-marker alternative and the naming collision it would have prevented.
