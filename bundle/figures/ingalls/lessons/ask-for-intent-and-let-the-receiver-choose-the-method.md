---
type: lesson
title: "State what you want, never how it is done, because dependencies grow quadratically and only the request is safe to share"
figure: ingalls
works: [design-principles-behind-smalltalk]
axes: [cognitive-load, expressiveness]
subdomains: [software-engineering-and-architecture, programming-environments-and-object-systems]
tags: [lesson]
---
# State what you want, never how it is done, because dependencies grow quadratically and only the request is safe to share

**Lesson:** The reason to be strict about components not reaching into each other's internals is arithmetic. Parts grow linearly and the pairs of parts that could come to depend on one another grow as the square, so in any system large enough to be interesting, the number of possible entanglements outruns anyone's ability to track them. Discipline applied case by case cannot win that race. What can win is a mechanism that makes the common form of coupling structurally unavailable, so that the quadratic space of potential dependencies is never populated in the first place.

The mechanism is to split every interaction into a request and a fulfillment, and to let the caller own only the request. A name that says what is wanted commits to nothing about how it is achieved, so the two sides can be reasoned about, changed, and replaced independently; a call that says how commits the caller to the callee's current internals and quietly enrolls it in every future change to them. The same split has to cover state access as well as behavior, because a component that can read another's fields has an implicit dependency on the shape of those fields that is every bit as binding as a call — which is why the request-based interface has to be the only door, not the preferred one. An interface that is bypassable is not an interface, it is a suggestion.

The payoff shows up as substitutability: anything that answers the same requests can stand in anywhere, and adding a new participant to an existing system requires no change to the code that will use it, so long as it honors the vocabulary. The corresponding discipline for the writer is to describe programs in terms of what things do rather than what they are — never assert that a value is a particular representation, only that it responds to a particular repertoire. Every place a program names a concrete representation is a place a future variant will have to be excluded from or the code recompiled and re-audited, and those places are exactly the ones that make a model of the real world brittle.

**Source:** [Design Principles Behind Smalltalk](../works/design-principles-behind-smalltalk.md) — the Modularity principle with its N-squared dependency argument, the observation that message sending decouples the intent carried in a name from the method the recipient uses, and the Polymorphism principle illustrated by adding a new kind of vehicle to a traffic simulation without touching existing code.
