---
type: lesson
title: "A technique you have not named is not yet an idea, and will not survive its first setting"
figure: reynolds
works: [the-discoveries-of-continuations]
axes: [cognitive-load, expressiveness]
subdomains: [programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# A technique you have not named is not yet an idea, and will not survive its first setting

**Lesson:** It is entirely possible to invent a working technique, present it correctly to the best audience in the field, and have it vanish for six years. The recorded case is a mechanical transformation that rewrote programs so that every jump became a call and no call ever returned; the transformation was right, the audience contained most of the people who would later care, and nothing came of it. The diagnosis is not bad luck. The presenter had the transformation but never isolated or named the entity the transformation manipulates — the thing standing for whatever the program will do after the current point. Without that noun, there was nothing to recognize when the same entity turned up in an interpreter's saved state, in a compiler's representation of a label, or in a semantic equation, so each appearance had to be discovered again from scratch.

The converse is documented just as sharply by the person who eventually coined the term. He had spent a year building unsatisfying machinery for the same problem; the missing move was not a technical device but the decision to introduce a concept for the remainder of the computation, after which the domains and equations followed within days. His own gloss on it is the part worth keeping: having a word made the idea easy to write down, to argue about, and to hand to other people. Naming is not clerical work performed after the thinking. It is the step that converts a private manipulation into something the rest of the field can hold, and it frequently unblocks the technical development that was stalled.

Two corollaries fall out for anyone sitting on a technique that works. First, exhibit what it buys. A derivation offered purely as a reduction — proof that the construct is dispensable — gives a reader nothing to want, and reviewers of the era noted precisely that: no application, no theoretical consequence beyond re-deriving one already-known result, therefore no perceived value. Second, expect not to see the ramifications of your own idea; the originators here used the device once and dropped it, while its generality was found by people who came to it later. That argues against treating priority as the interesting question. A second, better-motivated telling of a known idea is often the one that actually delivers it, so "this has been done before" is a weak reason to suppress an exposition and a bad reason to stop working on one.

**Source:** [The Discoveries of Continuations](../works/the-discoveries-of-continuations.md) — the account of van Wijngaarden's 1964 presentation and the observation that he discovered the transformation rather than the concept, never defining it; McIlroy's recollection that the absence of any practical or theoretical application kept the value from coming through; Wadsworth's correspondence on coining the term and the work falling into place afterward; and the rejection of J. H. Morris's more careful and correct presentation on grounds of prior anticipation.
