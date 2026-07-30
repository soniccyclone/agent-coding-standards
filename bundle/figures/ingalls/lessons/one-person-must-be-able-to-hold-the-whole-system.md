---
type: lesson
title: "Set the size of the whole system by what one person can master, and pay for it by deleting special cases"
figure: ingalls
works: [design-principles-behind-smalltalk]
axes: [cognitive-load, primitive-count]
subdomains: [software-engineering-and-architecture, programming-environments-and-object-systems]
tags: [lesson]
---
# Set the size of the whole system by what one person can master, and pay for it by deleting special cases

**Lesson:** Take as a binding constraint that a single individual should be able to understand the entire system, top to bottom, and let everything else be negotiated against it. This is not modesty about scope; it is a claim about where capability comes from. Whatever region of the system a person cannot see into is a region they cannot change, and any region they cannot change eventually becomes the thing standing between them and what they want to build. The constraint is uncomfortable precisely because it is not satisfied by making each part simple — a system of a thousand individually simple parts, each with its own conventions, is not masterable by anyone.

That is why the constraint cashes out as three specific design obligations rather than a general exhortation to simplicity. Keep the set of parts the user cannot alter as small as you can bear, since every fixed part is a wall someone will eventually hit. Make those few fixed parts as general as possible, since a fixed part that is nearly right for many uses beats one that is exactly right for one. And hold everything in a single framework, because the real enemy of comprehension is not quantity but discontinuity: a component that works differently from all the others demands its own separate learning, its own separate tooling, and its own separate vigilance forever. The cost of a special case is not the code it contains but the second mental model it obliges everyone downstream to maintain.

The practical form of this is a running audit against uniformity rather than against line count. Every time a subsystem acquires its own idiom — its own way of naming, of erroring, of being inspected — the system has gotten harder to hold even if it has gotten smaller. Conversely, adding volume that obeys the existing framework costs almost nothing in comprehension, because it is understood by the rules already learned. Uniformity is what lets a system grow without growing past its users.

**Source:** [Design Principles Behind Smalltalk](../works/design-principles-behind-smalltalk.md) — the Personal Mastery principle and the Good Design principle immediately derived from it, including the argument that any barrier between user and system becomes a barrier to creative expression and that a part working differently from the rest demands additional effort to control.
