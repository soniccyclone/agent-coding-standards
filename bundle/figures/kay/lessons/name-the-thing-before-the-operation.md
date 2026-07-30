---
type: lesson
title: "Name the thing before the operation, at every layer, so the thing itself can answer what may be done to it"
figure: kay
works: [user-interface-a-personal-view]
axes: [cognitive-load, expressiveness, primitive-count]
subdomains: [programming-environments-and-object-systems, programming-languages-and-semantics]
tags: [lesson]
---
# Name the thing before the operation, at every layer, so the thing itself can answer what may be done to it

**Lesson:** If entities are the things that know their own capabilities, then the order in which a request is composed is not arbitrary: identify the entity first and the intent second. Written that way round, the system can answer "what is legal here" itself, because by the time the intent is needed the receiver is already known and can enumerate its own repertoire. Written the other way round — operation first, then arguments — the person composing the request has to know the available operations before they have said what they are working on, so discovery becomes an act of recall, supported only by documentation and memory. The same asymmetry decides how errors surface. A request whose receiver is fixed first can be checked against that receiver as it is being built; a request whose verb is fixed first can only be checked once everything has been supplied.

The stronger claim is that this ordering should be the same at every layer of the system, from the notation people write in down to whatever surface they point at, click on or type into. Those layers are usually designed by different people at different times and end up with unrelated grammars, so fluency in one buys nothing in the other and every user has to maintain two mental models of the same system. When the concrete surface and the abstract notation share a grammar, learning either one teaches the other, and the pictures a person forms while working directly are already the right pictures for reasoning symbolically later. This is the practical payoff of taking a computational model seriously enough to let it dictate interaction rather than treating the model as an implementation detail hidden behind a separately invented front end.

Generalize past interfaces and it is a design test for any place a request is composed: command-line tools, query languages, APIs, protocol messages. Ask whether the first thing named is the thing being addressed. Where it is, the set of valid continuations is a function of what has already been said, which is exactly what makes completion, contextual menus, incremental validation and progressive disclosure possible at all — none of those features can be bolted onto a grammar that supplies the verb before the receiver. Where it is not, expect to compensate with reference material forever, and expect that compensation to be mistaken for an inherent difficulty of the domain.

**Source:** [User Interface: A Personal View](../works/user-interface-a-personal-view.md) — the passage arguing that because an object knows what it can do, the abstract form writes the object's name first and the message afterwards, while the concrete form selects the object first so it can then offer what it is willing to do, unifying the concrete and the abstract.
