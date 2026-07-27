---
type: lesson
title: "The properties that make a notation readable are the same ones that make it cheap to process, so design for the tractable case instead of the general one"
figure: floyd
works: [the-syntax-of-programming-languages-a-survey]
axes: [cognitive-load, hardware-affinity, expressiveness]
subdomains: [programming-languages-and-semantics, algorithms-and-complexity]
tags: [lesson]
---
# The properties that make a notation readable are the same ones that make it cheap to process, so design for the tractable case instead of the general one

**Lesson:** Take the general problem of recovering structure from any artifact describable by some formalism and it may well be intractable; you can construct pathological cases that defeat every known method and will defeat the next one too. The productive response is not to keep hunting for a universal method. It is to notice that the artifacts anyone actually wants to process are not drawn from the pathological end of the space, and that the reason they are not is the same reason they are usable by people at all. Human legibility and cheap mechanical processing are not competing goals that happen to sometimes align; they are two views of one property, which is that structure becomes determinable locally and early rather than globally and late.

The pathological case makes this precise by showing what the property's absence looks like. Construct a description in which, reading left to right, a commitment must be made at every position in the first half of the artifact while no information bearing on whether the commitment was right arrives until the second half. Cost then grows exponentially, and it does so not because the description is large or the formalism weak but because information arrives after the decisions that needed it. A person reading the same artifact would be just as lost, and for exactly the same reason. Contrast a notation where every choice among alternatives is settled by looking at the first token of the construct: that is trivially machine-processable and it is also the notation a person can read without backtracking.

So the design lever is not the processing method but the notation, and the question to ask about a proposed notation is when information becomes available relative to when a decision must be made. This reframes a whole class of arguments. Complaints that a language is hard to parse are usually complaints that it defers disambiguating information, and such a language is reliably also one whose readers misread it. Conversely, a restriction that seems to be for the tool's benefit — requiring a keyword up front, forbidding a construct that could start two different ways — is usually paying the reader as well.

A programmer who has internalized this stops treating worst-case intractability as a reason to give up and stops treating "but it's expressible" as a defense of a notation. The move is to characterize the well-behaved subclass, design squarely inside it, and accept the loss of generality as the price of both a fast tool and a readable artifact. It also explains why the useful complexity result is often not about the general problem at all, but about which restriction buys tractability.

**Source:** [The Syntax of Programming Languages — A Survey](../works/the-syntax-of-programming-languages-a-survey.md) — the passage in the syntax-directed analysis section presenting a grammar that forces a choice at every character of a sentence's first half while withholding all confirming information until the second half, the accompanying admission that no method is known to avoid exponential growth even for pathological languages, and the immediately following observation that the properties making programming languages legible to human readers are what permit simple efficient analysis, illustrated by a language where each alternative is decided by its first character or word.
