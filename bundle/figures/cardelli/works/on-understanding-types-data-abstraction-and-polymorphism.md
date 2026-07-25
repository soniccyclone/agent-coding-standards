---
type: work
title: "On Understanding Types, Data Abstraction, and Polymorphism"
figure: cardelli
description: A survey that organizes the then-scattered literature on type systems into a coherent framework, distinguishing universal polymorphism (parametric and inclusion) from ad hoc polymorphism (overloading and coercion), and connecting these to data abstraction mechanisms like abstract data types and objects. It became the standard reference vocabulary for talking about polymorphism in programming languages. Widely taught and cited as the paper that gave the field a shared taxonomy rather than competing folk terms.
subdomains: [programming-languages-and-semantics]
year: 1985
url: http://lucacardelli.name/Papers/OnUnderstanding.pdf
access: public
host: self-archived
tags: [work]
---

# On Understanding Types, Data Abstraction, and Polymorphism

**Author(s):** Luca Cardelli and Peter Wegner
**Venue/year:** ACM Computing Surveys 17(4), December 1985, pp. 471-522.
**Source:** http://lucacardelli.name/Papers/OnUnderstanding.pdf — self-archived on Cardelli's own site (verified 200, application/pdf). Note: the site's HTTPS is misconfigured (TLS handshake resets), so the plain HTTP URL is the one that actually resolves.

## Lessons
- [Reduce a whole design vocabulary to a handful of binding forms, then measure the vocabulary by what derives from them](../lessons/derive-the-vocabulary-from-a-few-binding-forms.md)
- [Decide what your descriptions denote, and the relations between them stop being matters of taste](../lessons/fix-what-your-types-denote-and-the-relations-follow.md)
- [A classification earns its keep only when its cases differ in what an implementation must do](../lessons/keep-only-the-distinctions-that-change-behavior.md)
- [Treat guaranteed termination of your own tooling as a budget you may knowingly overspend](../lessons/spend-decidability-deliberately.md)
- [When two design goals genuinely fight, look for the construct that serves both instead of splitting the difference](../lessons/two-goals-in-tension-need-a-third-construct.md)
- [Separate the guarantee you require from the moment you establish it, and pick the moment per boundary](../lessons/when-you-check-is-not-what-you-guarantee.md)
- [Minimality is owed by the layer you reason in, speed by the layer you run on, and neither should be asked of the other](../lessons/each-layer-owes-a-different-virtue.md)
