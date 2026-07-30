---
type: lesson
title: "Put the space of values on the table before arguing about the notation"
figure: scott
works: [toward-a-mathematical-semantics-for-computer-languages]
axes: [cognitive-load, expressiveness, verifiability]
subdomains: [programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# Put the space of values on the table before arguing about the notation

**Lesson:** Design arguments about a language, a protocol, or an API almost always start at the surface — what the keywords are, what the request shape looks like, which category a construct belongs to. That order is backwards. Settle first what the things are that the notation is going to talk about: what kinds of values exist, what a value of each kind can do, what an operation is allowed to depend on and allowed to change. Those commitments can be made completely and rigorously before a single piece of syntax is chosen, and once they are made the syntax largely follows. The same space of values will usually serve several plausible notations, which is the clearest evidence that the notation was never the load-bearing decision.

The reason this ordering pays is that the hard discoveries live in the value space, not the surface. Deciding that a procedure can be stored, passed, and returned like anything else is a statement about which space the values inhabit; whether that space can exist at all is then a question with an answer, and the answer may be no. Deciding that evaluating an expression can alter the state is a statement about the shape of every meaning function in the system, and it propagates into every construct whether or not you noticed. Arguments conducted at the syntax level cannot surface these consequences, so they get discovered late, as "we cannot implement this feature after all" — which is the same discovery, arrived at expensively.

There is a reciprocal move that keeps this from turning into pure top-down dogma. In logical order the foundations precede their application, but in working order you often cannot tell what apparatus the foundations must supply until you have tried the application and watched it fail. So the honest loop is: attempt the thing you want to build, notice precisely which construction the attempt demanded and could not get, then go build that construction and come back. What you must not do is let the failed attempt lower your ambition for the notation, or let the notation freeze while the semantic account is still discovering what it needs. Lay the domains out, argue about them in the open, and treat the notation as the last thing to fix rather than the first.

**Source:** [Toward a Mathematical Semantics for Computer Languages](../works/toward-a-mathematical-semantics-for-computer-languages.md) — the remark that the domains of the concepts can be laid out rigorously before the choice of language is made final and that one domain may suit several languages, together with the closing observation that although foundations logically precede applications it is hard to know what mathematical apparatus is needed until applications have been attempted.
