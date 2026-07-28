---
type: lesson
title: "Cut the hard problem out of scope on purpose, and ship the mechanism you can implement simply"
figure: liskov
works: [the-power-of-abstraction]
axes: [primitive-count, cognitive-load, hardware-affinity]
subdomains: [programming-languages-and-semantics, software-engineering-and-architecture, programming-environments-and-object-systems]
tags: [lesson]
---
# Cut the hard problem out of scope on purpose, and ship the mechanism you can implement simply

**Lesson:** A large design carries several hard problems, and the temptation is to treat all of them as in scope because they are all real. The discipline that actually finishes things is to pick the one problem you are trying to answer and explicitly amputate the others — not defer them vaguely, but decide out loud that this work does not address them. The gain is not just time. Every additional hard problem in scope pulls the design toward compromises that serve it, and those compromises corrupt the answer to the question you actually cared about. Excluding a genuinely important concern is therefore a way of protecting the result, not a way of ducking work.

The same instinct applies one level down, to individual mechanisms. Given a construct that would handle every case at the cost of a complicated definition and an awkward implementation, and a restricted version that handles most cases with a definition anyone can hold in their head and an implementation that is nearly free, take the restricted one. The restriction should be chosen deliberately and stated: this construct covers the common shape, and the general case is not expressible. What makes this respectable rather than lazy is that the excluded cases remain achievable by ordinary means — assembled by hand out of other pieces — so the choice is between a mechanism for most cases plus a technique for the rest, versus a heavier mechanism for everything. The first is usually the better bargain, because the weight is paid by everyone and the generality is used by few.

Notice what the restriction buys concretely: a construct narrow enough to have a straightforward implementation strategy costs nothing at runtime, which means people will actually use it in preference to writing around it. A general mechanism whose implementation is expensive gets avoided in exactly the situations where performance matters, which is to say it fails at the moment it was most needed. Simplicity of definition and cheapness of implementation are usually the same property viewed from two sides.

A programmer who believes this opens a design by writing down what it will not address, and defends that list. When choosing between a complete mechanism and a partial one, they ask what fraction of real uses the partial one covers, whether the remainder is achievable another way, and what the complete one costs everybody. They also state the restriction in the interface rather than leaving users to discover its edges.

**Source:** [The Power of Abstraction](../works/the-power-of-abstraction.md) — the account of deliberately excluding concurrency and inheritance from the language's scope, and the closing exchange about iterators, where a restricted one-at-a-time construct with a trivial implementation is preferred over the more general coroutine-like mechanism, leaving the general case to methodology.
