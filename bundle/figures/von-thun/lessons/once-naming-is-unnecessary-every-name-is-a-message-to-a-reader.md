---
type: lesson
title: "Once naming is unnecessary, every name is a message to a reader"
figure: von-thun
works: [the-prototype-implementation-of-joy]
axes: [cognitive-load, expressiveness]
subdomains: [programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# Once naming is unnecessary, every name is a message to a reader

Introducing the definition mechanism, von Thun lists the reasons a programmer might want to name something: the thing is needed in several places, the thing is recursive, or the name makes the program more intelligible. He then remarks that the first two motives carry less weight in his language than in most others — composition already lets a fragment be reused without being named, and the recursion combinators already let a program recurse without a name to call. The third motive is left standing alone. Naming, stripped of its mechanical justifications, turns out to be an act of communication and nothing else.

That reframing changes what a name has to earn. When names are load-bearing you cannot ask whether one is worth having, because the code will not work without it, and the habit of naming everything gets reinforced by necessity rather than by judgment. Remove the necessity and each definition has to justify itself on the only remaining ground: does a person reading this understand the program better because this fragment has a name? Some do, emphatically — a name is the cheapest way to tell a reader that a particular sequence of steps is one idea with a purpose. Many do not, and in a language where nothing forces them, they are pure overhead: an entry in a dictionary, an indirection to chase, a term whose meaning the reader must go and look up in order to get back to where they already were.

The general form of this applies well outside languages that eliminate parameters. Every codebase has names that exist because the mechanism demanded them — the extracted helper that exists only to be called twice, the intermediate variable that exists because the expression got long, the interface that exists because the framework wants a type. Those names are not communicating anything; they are structural residue, and they are read as though they were communication, which is worse than silence. The discipline von Thun's remark suggests is to ask of each name whether it survives the removal of its mechanical excuse. If it does, it is telling a reader something and should be as precise as you can make it. If it does not, it is noise with a plausible shape.

**Source:** [The Prototype Implementation of Joy](../works/the-prototype-implementation-of-joy.md) — the opening of the section on definitions and the main cycle, where the three motives for defining a symbol are listed and two of them are noted to be weaker in this language than elsewhere.
