---
type: lesson
title: "An account that begins by erasing the feature has not explained it — and the leftover mismatch is where your next design decision hides"
figure: girard
works: [the-system-f-of-variable-types-fifteen-years-later]
axes: [verifiability, expressiveness]
subdomains: [programming-languages-and-semantics, formal-methods-and-verification]
tags: [lesson]
---
# An account that begins by erasing the feature has not explained it — and the leftover mismatch is where your next design decision hides

**Lesson:** There is a seductive shortcut for explaining a construct you find hard: strip it out, explain what remains, and claim the result as an explanation of the original. Applied to polymorphism, it looks respectable — delete the type abstractions and instantiations, interpret the resulting untyped skeleton in some familiar model, then define types after the fact as subsets of that model closed under the right operations. Everything typechecks, every term gets a denotation, and the exercise is worthless for its stated purpose, on two counts. It never interprets the types at all; it ignores them and interprets something else. And whatever it does produce is hostage to an arbitrary choice of ambient model, so nothing you learn from it is a fact about the construct rather than a fact about your scaffolding. Demand an account that is *absolute* — that does not require you to pick a substrate first — and you are forced to actually engage with the feature.

The complementary discipline is what to do once you have a real account. Build it, then compare the population of things your model admits against the population your notation can name, and take the discrepancy seriously as a design finding rather than as noise. The concrete case here is instructive: the two-valued type has exactly two things you can write down, but the model of it contains four, and the extra two are not junk. One is an emptiness that a careful reader could have anticipated; the other is a genuine third value behaving like indeterminacy, which propagates sensibly through the derived operations and turns the two-valued fragment into a coherent three-valued one. That is not an embarrassment to be quotiented away, it is a proposal: the notation is missing something the structure already has room for.

The discrepancy runs the other way too, and both directions are useful. A property you would have sworn was the semantic counterpart of a syntactic one may simply not be — here, the notion of being fully defined turns out not to coincide with being maximal in the model, and not even to imply it in either direction, so the intuitive identification has to be discarded and rebuilt against what the definable things actually satisfy. The general habit is to let the syntax and the model each audit the other, and never to assume in advance which one is wrong.

A programmer who works this way stops accepting explanations of a system's hard feature that start by compiling the feature away, and starts treating "my model permits states my API cannot express" as a bug report against the API rather than a defect of the model.

**Source:** [The System F of Variable Types, Fifteen Years Later](../works/the-system-f-of-variable-types-fifteen-years-later.md) — the discussion section rejecting the type-erasing interpretation on the grounds that it ignores rather than explains types and depends on an arbitrary ambient model, and the boolean-type computation whose surplus semantic values are put forward as a candidate extension of the syntax, together with the appendix distinguishing totality from maximality.
