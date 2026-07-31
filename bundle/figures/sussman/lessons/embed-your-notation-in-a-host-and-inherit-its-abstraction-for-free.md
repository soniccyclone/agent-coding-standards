---
type: lesson
title: "Embed a notation in a host language and it inherits the host abstraction machinery for free"
figure: sussman
works: [structure-and-interpretation-of-computer-programs]
axes: [expressiveness, primitive-count]
subdomains: [programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# Embed a notation in a host language and it inherits the host abstraction machinery for free

**Lesson:** Having built a small language whose values are pictures and whose operations place them beside and below one another, the authors note something they get without asking. Because the combining operations are ordinary procedures of the host language rather than constructs of a separate parser, the picture language needs *no abstraction mechanism of its own*: anything the host can do with procedures is automatically available for picture operations too. Naming a recurring arrangement, parameterizing it, passing one arrangement into another, building operations that build operations -- none of it has to be designed, because it was already there.

That is the decisive advantage of embedding a notation inside a general language rather than giving it its own syntax and interpreter, and it is easy to underrate when starting out. A standalone notation begins simple and is then asked, inevitably, for variables, then parameterized definitions, then some way to reuse a definition across files, then conditionals -- and each is designed late, under pressure, by people whose expertise is the domain rather than language design. The embedded version has all of it from the first day and none of it in its budget.

The requirement this imposes is that the domain's values be ordinary values of the host and its combiners ordinary functions. Where that holds, the domain vocabulary composes with everything the host already offers. Where a notation instead defines its own scoping, its own binding forms, or its own module system, it has begun re-implementing the host badly, and the re-implementation is where such languages accumulate their irregularities.

The reflex to take into any decision about a configuration format, a build description, a query dialect or a workflow specification: ask whether the domain's operations can simply be functions in a language you already have. If they can, the abstraction facilities come free and stay consistent. If they cannot, then be honest that you have taken on the job of designing a language, and that the parts you will need are the parts that took the general-purpose languages decades to get right.

**Source:** [Structure and Interpretation of Computer Programs](../works/structure-and-interpretation-of-computer-programs.md) - chapter 2 section 2.2.4, which observes that implementing the painter operations as ordinary Scheme procedures means no special abstraction mechanism is needed in the picture language -- since the means of combination are ordinary procedures, anything that can be done with procedures can automatically be done with painter operations -- demonstrated by abstracting a repeated arrangement into a named procedure, then by writing higher-order operations that take painter operations as arguments and produce new painter operations.
