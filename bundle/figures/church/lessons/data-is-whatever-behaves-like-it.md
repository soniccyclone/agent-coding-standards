---
type: lesson
title: "Data can be defined by the behavior it supports rather than by the stuff it is made of"
figure: church
works: [the-calculi-of-lambda-conversion]
axes: [primitive-count, expressiveness]
subdomains: [programming-languages-and-semantics, foundations-of-computation]
tags: [lesson]
---
# Data can be defined by the behavior it supports rather than by the stuff it is made of

**Lesson:** A formalism with no numbers, no pairs, and no booleans in it can still do arithmetic and branch on conditions, provided you are willing to define each of those things as a function whose behavior is indistinguishable from the thing you wanted. A counting number becomes the operation of repeating something a fixed number of times. A pair becomes the operation of handing two saved values to whatever asks for them. A truth value becomes the operation of picking one of two continuations. Nothing was added to the language; the vocabulary grew entirely by definition on top of an unchanged core.

The justification is a claim about what a specification actually demands. Arithmetic asks of its numbers only that they form a progression with the right structural relationships. Anything satisfying those relationships is a legitimate number for arithmetic's purposes, and there are many inequivalent ways to satisfy them. So the choice of representation is genuinely free, and the reason to prefer one encoding over another is convenience or the theorems it preserves, never authenticity. Multiplication falling out as composition of repetitions, and exponentiation falling out as repetition of that, are not coincidences; they are what happens when the representation is chosen to make the structure you need be the structure the representation already has.

The lesson for a working programmer is to attack the question "what is this data" by asking "what must be true of it, and what operations must it support" before reaching for a record layout. Doing this exposes when a type has been over-specified with fields nobody needs, and it dissolves the false wall between data and behavior: closures capturing values are records, records are dispatch tables, and a constructor is just a function that remembers its arguments. It also sets the direction of any performance argument correctly. Encoding data as behavior is a statement about what the abstraction guarantees, and a compiler or a hand optimization is then free to replace it with bits, because the specification never demanded bits in the first place.

**Source:** [The Calculi of Lambda-Conversion](../works/the-calculi-of-lambda-conversion.md) — the chapter on lambda-definability, where positive integers are identified with iteration functions and the accompanying remark that number theory constrains its integers only up to being a progression, and the following section building ordered pairs and triads out of selection.
