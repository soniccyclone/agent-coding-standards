---
type: lesson
title: "Into a description you may borrow anything that denotes, and nothing that sequences"
figure: jones
works: [software-development-a-rigorous-approach]
axes: [expressiveness, verifiability, cognitive-load]
subdomains: [formal-methods-and-verification, programming-languages-and-semantics]
tags: [lesson]
---
# Into a description you may borrow anything that denotes, and nothing that sequences

**Lesson:** Writing down what a piece of software must achieve, you will constantly want to reach for something already written to say it with. The question of what is legitimate to reach for has a crisp answer, and it is not the answer people expect. The test is not efficiency and it is not abstraction level. It is whether the thing you are borrowing *denotes a value* or *prescribes an order*.

Anything that merely denotes is fair game, no matter how badly it would perform. A recursion that recomputes the same subproblem exponentially many times is a perfectly good way to say which number is wanted, because it names a value and says nothing about how anyone should get there. Nobody will implement it that way and nobody was asked to. Its uselessness as code is irrelevant to its usefulness as a definition, and treating those as the same property is a common and expensive confusion — it leads people either to omit a clear definition because it would be slow, or to accept a fast one as a definition when it has smuggled in choices.

The moment you borrow something that sequences, you have said more than you meant. Take a construct like statement composition into a description and you have committed to an order of operations that the problem never demanded, and every implementation is now bound by it whether or not it matters. This is over-specification of the sneakiest kind, because it does not look like a decision; it looks like notation. Nobody reading the description later can tell which orderings were required and which were an artifact of the language you happened to write in.

Two consequences worth keeping. First, prefer a value-shaped formulation to a state-shaped one wherever you can, and drop to state only when the thing you must talk about genuinely is state — the value-shaped version is not just cleaner, it is order-free by construction, so it cannot commit the error above. Second, when a description does have to name state, the reason to describe it by a relation over before and after rather than by a sequence of moves is the same reason: a relation still says nothing about order, and a sequence always does.

**Source:** [Software Development: A Rigorous Approach](../works/software-development-a-rigorous-approach.md) — the "Specifying Operations" section of chapter 4: the Fibonacci example given as an acceptable specification device with the explicit acknowledgement that the recursive function used is a hopelessly inefficient basis for a program; the warning immediately following that the temptation to extend a specification language with programming-language statements is dangerous, with the reason given as the mathematical tractability of functions versus the over-specification of order that constructs like sequencing introduce; and the accompanying preference table recommending implicit specification for operations precisely because it avoids ordering, together with its closing note that functions are preferred to operations except where states must be discussed.
