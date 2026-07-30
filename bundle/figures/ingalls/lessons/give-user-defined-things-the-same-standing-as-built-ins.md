---
type: lesson
title: "Give user-defined things exactly the standing of built-in ones, or people will model their domain in primitives"
figure: ingalls
works: [design-principles-behind-smalltalk]
axes: [expressiveness, cognitive-load]
subdomains: [programming-languages-and-semantics, programming-environments-and-object-systems]
tags: [lesson]
---
# Give user-defined things exactly the standing of built-in ones, or people will model their domain in primitives

**Lesson:** A system's extension mechanism should admit new kinds of things on precisely equal footing with the ones the system was shipped with — same declaration, same efficiency, same privileges, same tooling — and the reason is behavioral rather than aesthetic. People reach for whatever representation is cheapest at the moment they need it. Offer a second-class way to define a domain concept and a first-class primitive that is almost adequate, and the domain concept will not get defined: a melody becomes a bag of numbers standing for pitch and duration, because numbers work everywhere and the proper abstraction is a little awkward. The model that would have made the whole program legible never gets written, and nobody experiences this as a decision.

So the design target is not that extension be possible but that it be as cheap as the alternative at every point of use. Where a built-in enjoys some advantage a user-defined thing cannot have — special syntax, escape from a check, a fast path the extension mechanism does not reach — that advantage is a standing bribe to model the problem badly. The corollary for the person doing the extending is worth stating too: a system that genuinely offers parity will be described by its users in its own terms, and the shape of what people build in it becomes evidence about whether the parity is real. If the code written on top of your framework is mostly primitives and dictionaries where it should be domain objects, the parity is not there, whatever the documentation claims.

The same principle explains why it is worth pushing self-description all the way down. Once the machinery that describes kinds of things is itself just another kind of thing, described the same way, the mechanism has no floor at which it stops applying, and the user can reach and reshape the classification machinery with the tools they already learned. That absence of a floor is what makes the equal-footing promise credible rather than a claim about the parts the designer happened to anticipate.

**Source:** [Design Principles Behind Smalltalk](../works/design-principles-behind-smalltalk.md) — the Classification principle with its explicit "equal footing with the kernel classes" clause, the argument that a user will naturally choose the most effective representation only if the system provides for it, illustrated by melodies as collections of notes rather than ad hoc integers, and the note that classes are themselves instances of a class.
