---
type: lesson
title: "A feature whose case rests on a compelling example is probably a mistake, because the example is local and the cost is global"
figure: ungar
works: [programming-as-an-experience]
axes: [primitive-count, cognitive-load, expressiveness]
subdomains: [programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# A feature whose case rests on a compelling example is probably a mistake, because the example is local and the cost is global

The standard way a design acquires a bad feature is entirely reasonable-looking. Someone presents a situation the current design handles awkwardly, proposes a rule that handles it cleanly, and the rule is adopted because the example is undeniable. The flaw is not in the example; the example is usually true. The flaw is that an example can only ever demonstrate the *benefit* side of the ledger. Benefits of a feature are visible and local — this case now works. Costs are invisible and global, because a new rule does not merely exist alongside the others, it must be defined against every one of them. Add a feature to a design with n existing mechanisms and you have implicitly promised answers to n new interaction questions, and each answer is a place where behavior can surprise someone who never asked for the feature.

The observable symptom of having fallen in is a semantics that takes many pages to state precisely, and a team spending real time chasing what look like implementation bugs but turn out to be consequences of their own rules that nobody foresaw. That is the tell: when the designers themselves are repeatedly surprised by the system they specified, the specification has exceeded what a human can hold, and every user downstream will be surprised in the same way with less context to recover from it. The cost was paid by everyone, including the majority who never needed the case that motivated it.

So examples are the wrong currency for design arguments, and something else has to take their place. What survives is a small number of properties you refuse to compromise — uniformity, and the ability to change anything about a running system — chosen because they compound rather than interact. Uniformity means fewer distinct ways of doing a thing, which makes code reusable across situations that would otherwise need their own version, which makes programs smaller, which makes them comprehensible. Each of those follows from the previous one. A feature justified by an example has no such chain; it justifies itself and nothing else.

A practical version for anyone maintaining a shared abstraction: when a request arrives with a persuasive scenario attached, do not evaluate the scenario. Ask what the new rule must say about its interaction with everything already there, and make whoever wants it answer that. Frequently the answer is long enough that the request withdraws itself. And when reviewing a design that already has too much, the corresponding move is subtraction — cutting a feature that a minority relied on can be a net gain, because the interaction complexity it imposed was being paid by all.

**Source:** [Programming as an Experience: The Inspiration for Self](../works/programming-as-an-experience.md) — the minimalism discussion in the language-semantics section, where the authors name three specific rules they added on the strength of individual motivating cases and later withdrew, and generalize the pattern into a named trap for designers.
