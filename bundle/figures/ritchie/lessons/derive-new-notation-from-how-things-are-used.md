---
type: lesson
title: "Derive new notation from how the thing is used, and accept that the analogy inherits its flaws"
figure: ritchie
works: [the-development-of-the-c-language]
axes: [expressiveness, cognitive-load, primitive-count]
subdomains: [programming-languages-and-semantics]
tags: [lesson]
---
# Derive new notation from how the thing is used, and accept that the analogy inherits its flaws

**Lesson:** Faced with needing a way to write down composite types — arrays of anything, pointers to anything, functions returning anything, closed under composition — Ritchie did not invent a fresh vocabulary. He observed that for every composed type, the programmer already knows how to get at the underlying thing: index the array, call the function, dereference the pointer. So he made a declaration look exactly like the expression you would write to obtain a value of the base type. Declaring a name amounts to exhibiting the usage whose result has the type written at the front. One rule then covers arbitrarily nested combinations, with no new syntax per combination, and the reader who knows how to use a value already knows how to declare one.

The method is worth extracting from the example. When you need notation for a new construct, look for an established notation the reader already fluently reads, and define the new one so that it is the old one under a different reading. This keeps the primitive count low, makes the notation self-extending to cases the designer never enumerated, and lets existing skill transfer rather than requiring new learning.

Ritchie is also candid about the bill. The analogy is only as good as the syntax it borrows, and the one he borrowed had the dereference operator as a prefix, which forces parentheses to disambiguate anything nontrivial and forces declarations to be read from the inside out — the source of the perennial complaint that C's harder types are unreadable. He cites the observation that treating indirection as a postfix operator instead would have simplified much of the nesting, and adds the coda that by the time anyone noticed, changing it was out of the question. He separates two causes carefully: part of the difficulty is intrinsic, because a language with a genuinely rich type algebra describes complicated objects and any notation for them will be complicated, and part is a fixable accident of operator position that got frozen. He still defends the principle as sound.

A programmer who believes this designs new syntax and new APIs by finding the shape users already know and making the new thing an instance of it. But they audit the borrowed shape first, since every ergonomic defect in the model is inherited amplified by the derived form, and the derived form will be the one nobody can change later. They also distinguish complexity that comes from the problem from complexity that comes from a token's position, because only one of the two is worth arguing about.

**Source:** [The Development of the C Language](../works/the-development-of-the-c-language.md) — the derivation of declaration syntax from expression syntax in the "Embryonic C" section, read together with the critique section's discussion of inside-out reading and the suggestion that a postfix indirection operator would have been better.
