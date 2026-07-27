---
type: lesson
title: "When two halves of a system look symmetric, use the symmetry to predict what must exist on the side you have not examined"
figure: steele
works: [lambda-the-ultimate-declarative]
axes: [primitive-count, expressiveness, cognitive-load]
subdomains: [programming-languages-and-semantics, foundations-of-computation]
tags: [lesson]
---
# When two halves of a system look symmetric, use the symmetry to predict what must exist on the side you have not examined

**Lesson:** Control and environment are usually studied separately, by different people, with different vocabularies. This work notices that they line up point for point. Expressions determine the order things happen in; procedures determine how far a name's meaning extends — one constrains time, the other constrains text. Evaluating an expression whose result feeds another computation forces the machinery to remember where to resume; entering a procedure forces it to remember a set of name bindings. Each side has a stack-like structure, and each side becomes tree-shaped for the same reason: as soon as a first-class escape or a first-class procedure value can outlive the construct that created it, the last-in-first-out assumption fails on that side.

The striking part is how the symmetry was used. Having established that a caller implicitly creates a place for a result to be delivered to, and believing the two sides must correspond, the author predicted that there must be a matching implicit creation on the other side — an anonymous name for an intermediate value, brought into being when a returning call's result still has further processing ahead of it — and only then looked and found such names present. The prediction preceded the observation, which is the behavior of a real structural law rather than a pleasing coincidence. When a hypothesized symmetry generates a correct prediction about a part of the system you had not inspected, that is evidence the symmetry reflects something in the domain.

This gives a working technique, not just a satisfying picture. When you find yourself with two mechanisms that seem to mirror each other — a reader path and a writer path, a serializer and a parser, an encoder and its inverse, an allocation discipline and a release discipline — write out the correspondence explicitly and then look for gaps in it. Each unmatched entry on one side is a prediction: either there is a mechanism on the other side you have not named, or the asymmetry is real and marks the exact place your design is lopsided. Both outcomes are worth having, and the check is cheap. It is also a discipline against accidental complexity: a mechanism that exists on only one side of an otherwise symmetric pair usually means someone special-cased something that did not need it.

**Source:** [Lambda: The Ultimate Declarative](../works/lambda-the-ultimate-declarative.md) — the conclusions, which tabulate the correspondences between expression evaluation and procedure application and then report that the last correspondence was predicted from the symmetry before being observed.
